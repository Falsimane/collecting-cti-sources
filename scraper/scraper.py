import asyncio
import json
import random
import sqlite3
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import html2text
import nodriver as uc
import trafilatura
from tqdm import tqdm

# Define absolute or relative paths for databases
URL_DB = "db_outputs/urls_collection.db"
KNOWLEDGE_DB = "db_outputs/cti_knowledge.db"


def init_knowledge_db():
  """Initializes the CTI knowledge SQLite database and creates the 'knowledge' table."""
  conn = sqlite3.connect(KNOWLEDGE_DB, timeout=30.0)
  cursor = conn.cursor()
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_name TEXT,
            url TEXT UNIQUE,
            title TEXT,
            publication_date TEXT,
            content TEXT
        )
    """)
  conn.commit()
  conn.close()


def save_and_mark(site_name, url, title, pub_date, content):
  """Safely saves the extracted Markdown content and metadata into cti_knowledge.db,

  then updates urls_collection.db to mark the URL as scraped (scraped = 1).
  """
  conn_k = sqlite3.connect(KNOWLEDGE_DB, timeout=30.0)
  cursor_k = conn_k.cursor()
  try:
    cursor_k.execute(
        """
            INSERT OR IGNORE INTO knowledge (site_name, url, title, publication_date, content)
            VALUES (?, ?, ?, ?, ?)
        """,
        (site_name, url, title, pub_date, content),
    )
    conn_k.commit()
  except Exception as e:
    print(f"❌ Error saving content for {url}: {e}")
  finally:
    conn_k.close()

  conn_u = sqlite3.connect(URL_DB, timeout=30.0)
  cursor_u = conn_u.cursor()
  cursor_u.execute("UPDATE articles SET scraped = 1 WHERE url = ?", (url,))
  conn_u.commit()
  conn_u.close()


async def scrape_single_article(
    browser, site_name, url, slow_mode, semaphore, pbar
):
  """Asynchronously scrapes a single article page using nodriver,

  converts images to absolute URLs, and transforms content to clean Markdown.
  """
  async with semaphore:
    try:
      if slow_mode:
        await asyncio.sleep(random.uniform(4.0, 8.0))

      page = await browser.get(url, new_tab=True)
      await asyncio.sleep(3)
      html_content = await page.get_content()
      await page.close()

      # Extract metadata (title, publication date) using Trafilatura
      metadata = trafilatura.extract_metadata(html_content)
      title = metadata.title if metadata and metadata.title else "Sans titre"
      pub_date = metadata.date if metadata and metadata.date else "Date inconnue"

      # Universal generic parsing with BeautifulSoup
      soup = BeautifulSoup(html_content, "html.parser")

      # Conversion des images en URLs absolues distantes (gère le lazy-loading data-src)
      for img in soup.find_all("img"):
        real_src = (
            img.get("data-src") or img.get("data-original") or img.get("src")
        )
        if isinstance(real_src, list):
          real_src = real_src[0] if real_src else None
        if isinstance(real_src, str) and not real_src.startswith("data:image"):
          img["src"] = urljoin(url, real_src)
          if "data-src" in img.attrs:
            del img["data-src"]

      # Automatic detection of the main content container (fallback hierarchy)
      target_area = (
          soup.find("article")
          or soup.find("main")
          or soup.find(class_=lambda c: isinstance(c, str) and "post" in c.lower())
          or soup.body
      )

      if target_area:
        # Strip out common non-content clutter automatically
        for unwanted in target_area([
            "script",
            "style",
            "nav",
            "header",
            "footer",
            "aside",
        ]):
          unwanted.decompose()

        # Convert clean HTML to Markdown, preserving links and absolute remote images
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.body_width = 0

        extracted_markdown = h.handle(str(target_area))
      else:
        extracted_markdown = "Content could not be extracted automatically."

      if not extracted_markdown.strip():
        extracted_markdown = "Content could not be extracted automatically."

      save_and_mark(site_name, url, title, pub_date, extracted_markdown)

    except Exception as e:
      tqdm.write(f"❌ Error on {url}: {e}")
    finally:
      pbar.update(1)


async def main():
  init_knowledge_db()

  print("\n--- CTI SCRAPER CONFIGURATION ---")
  print("[1] Fast Mode (Parallel processing based on sources configuration)")
  print("[2] Safe/Slow Mode (Forces 1 worker globally to prevent WAF blocks)")
  choice = input("Select execution mode (1 or 2, default is 1): ").strip()
  force_slow_all = choice == "2"

  with open("url_collector/sources.json", "r", encoding="utf-8") as f:
    sources_config = json.load(f)

  conn = sqlite3.connect(URL_DB)
  cursor = conn.cursor()
  cursor.execute("SELECT site_name, url FROM articles WHERE scraped = 0")
  pending_articles = cursor.fetchall()
  conn.close()

  if not pending_articles:
    print("✨ No new articles to scrape at the moment.")
    return

  print(f"\n🚀 Starting extraction for {len(pending_articles)} articles...")

  browser_args = [
      "--headless=new",
      "--window-size=1920,1080",
      "--disable-blink-features=AutomationControlled",
      (
          "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
          " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0"
          " Safari/537.36"
      ),
      "--lang=en-US,en;q=0.9",
  ]

  browser = await uc.start(browser_args=browser_args)
  max_workers = 3 if force_slow_all else 20
  semaphore = asyncio.Semaphore(max_workers)

  try:
    with tqdm(
        total=len(pending_articles), desc="Scraping Progress", unit="art"
    ) as pbar:
      tasks = []
      for site_name, url in pending_articles:
        site_slow_flag = (
            sources_config.get(site_name, {}).get("slow_mode", False)
        )
        is_slow = force_slow_all or site_slow_flag
        tasks.append(
            scrape_single_article(
                browser, site_name, url, is_slow, semaphore, pbar
            )
        )

      await asyncio.gather(*tasks)

  finally:
    try:
      browser.stop()
    except RuntimeError:
      pass


if __name__ == "__main__":
  asyncio.run(main())
  print("\n🎯 Content scraping process completed successfully!")