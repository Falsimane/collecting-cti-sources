import asyncio
import json
import os
import random
import re
import sqlite3
import subprocess
import sys
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urljoin
from bs4 import BeautifulSoup, Tag
from curl_cffi.requests import AsyncSession as CffiSession
import html2text
import nodriver as uc
import trafilatura
from tqdm import tqdm

URL_DB = "db_outputs/urls_collection.db"
KNOWLEDGE_DB = "db_outputs/cti_knowledge.db"
PDF_OUTPUT_DIR = "db_outputs/pdf"

BINARY_EXTENSIONS = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".pdf",
    ".zip",
    ".ico",
)

CLOUDFLARE_MARKERS = [
    "Enable JavaScript and cookies to continue",
    "cf-browser-verification",
    "challenge-running",
    "cf_clearance",
    "Checking if the site connection is secure",
    "Vérification de sécurité en cours",
    "Ray ID:",
]


def is_cloudflare_challenge(html: str) -> bool:
  return any(marker in html for marker in CLOUDFLARE_MARKERS)


# --- PDF report detection & download ---

PDF_DOWNLOAD_KEYWORDS = [
    "download the full report",
    "download the report",
    "download report",
    "download now",
    "télécharger le rapport complet",
    "télécharger le rapport",
    "telecharger le rapport",
]


def detect_pdf_download_link(soup: BeautifulSoup, base_url: str) -> str | None:
  """Scan the page for a download button whose href points to a PDF.

  Returns the absolute PDF URL if found, otherwise None.
  Looks for <a> tags whose visible text matches known download keywords
  AND whose href ends with .pdf (or contains .pdf before query params).
  """
  for a_tag in soup.find_all("a", href=True):
    text = a_tag.get_text(separator=" ", strip=True).lower()
    if not any(kw in text for kw in PDF_DOWNLOAD_KEYWORDS):
      continue
    href = a_tag["href"]
    if isinstance(href, list):
      href = href[0]
    abs_href = urljoin(base_url, href)
    # Accept direct .pdf links or links that will likely resolve to a PDF
    if ".pdf" in abs_href.lower().split("?")[0]:
      return abs_href
  return None


async def download_pdf(pdf_url: str, site_name: str, article_title: str) -> bool:
  """Download a PDF from pdf_url and save it to db_outputs/pdf/<site_name>/.

  Returns True on success, False on failure.
  """
  dest_dir = os.path.join(PDF_OUTPUT_DIR, site_name)
  os.makedirs(dest_dir, exist_ok=True)

  # Build a safe filename from the last segment of the URL
  pdf_basename = pdf_url.split("?")[0].rstrip("/").split("/")[-1]
  if not pdf_basename.lower().endswith(".pdf"):
    # Fallback: sanitize article title
    safe_title = re.sub(r'[^\w\s-]', '', article_title)[:80].strip().replace(" ", "_")
    pdf_basename = f"{safe_title}.pdf"

  dest_path = os.path.join(dest_dir, pdf_basename)

  if os.path.exists(dest_path):
    tqdm.write(f"   📄 [{site_name}] PDF already exists: {pdf_basename}")
    return True

  try:
    async with CffiSession(impersonate="chrome124") as session:
      resp = await session.get(
          pdf_url,
          headers={
              "Accept": "application/pdf,*/*",
              "Accept-Language": "en-US,en;q=0.9",
          },
          timeout=120,
          allow_redirects=True,
      )
      if resp.status_code != 200:
        tqdm.write(
            f"   ⚠️ [{site_name}] PDF download HTTP {resp.status_code}: {pdf_url}"
        )
        return False

      with open(dest_path, "wb") as f:
        f.write(resp.content)

    tqdm.write(f"   📥 [{site_name}] PDF saved: {pdf_basename}")
    return True

  except Exception as e:
    tqdm.write(f"   ❌ [{site_name}] PDF download error: {e}")
    return False


def init_knowledge_db():
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
  conn_k = sqlite3.connect(KNOWLEDGE_DB, timeout=30.0)
  cursor_k = conn_k.cursor()
  try:
    cursor_k.execute(
        """
            INSERT OR REPLACE INTO knowledge (site_name, url, title, publication_date, content)
            VALUES (?, ?, ?, ?, ?)
        """,
        (site_name, url, title, pub_date, content),
    )
    conn_k.commit()
  except Exception as e:
    tqdm.write(f"❌ Error saving content for {url}: {e}")
  finally:
    conn_k.close()

  conn_u = sqlite3.connect(URL_DB, timeout=30.0)
  cursor_u = conn_u.cursor()
  cursor_u.execute("UPDATE articles SET scraped = 1 WHERE url = ?", (url,))
  conn_u.commit()
  conn_u.close()


async def fetch_with_curl_cffi(url: str) -> str:
  async with CffiSession(impersonate="chrome124") as session:
    resp = await session.get(
        url,
        headers={
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            "sec-ch-ua": (
                '"Chromium";v="124", "Google Chrome";v="124",'
                ' "Not-A.Brand";v="99"'
            ),
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "Upgrade-Insecure-Requests": "1",
        },
        timeout=60,
        allow_redirects=True,
    )
    content_type = resp.headers.get("content-type", "").lower()
    if "image/" in content_type or "application/pdf" in content_type:
      raise ValueError(f"Content-Type binaire détecté : {content_type}")
    return resp.text


def extract_accurate_date(soup: BeautifulSoup, html_content: str) -> str:
  def publish_filter(c: Any) -> bool:
    if not c:
      return False
    if isinstance(c, list):
      c = " ".join(c)
    lower_c = str(c).lower()
    return any(
        k in lower_c for k in ["publish_info", "published-date", "post-date"]
    )

  publish_div = soup.find(class_=publish_filter)
  if publish_div and isinstance(publish_div, Tag):
    p_tag = publish_div.find("p") or publish_div
    text = p_tag.get_text(strip=True) if hasattr(p_tag, "get_text") else ""
    date_match = re.search(
        r"([A-Za-z]+\s+\d{1,2},\s+\d{4})|(\d{4}-\d{2}-\d{2})", text
    )
    if date_match:
      return date_match.group(0)

  meta_queries = [
      {"property": "article:published_time"},
      {"name": "publish-date"},
      {"property": "og:published_time"},
  ]
  for query in meta_queries:
    tag = soup.find("meta", attrs=query)  # type: ignore
    if tag and tag.has_attr("content"):
      content_val = tag.get("content")
      if isinstance(content_val, str):
        return content_val.split("T")[0]

  for script in soup.find_all("script", type="application/ld+json"):
    try:
      if script.string:
        data = json.loads(script.string)
        items = data if isinstance(data, list) else data.get("@graph", [data])
        for item in items:
          if isinstance(item, dict) and any(
              k in item.get("@type", "")
              for k in ["Article", "BlogPosting", "NewsArticle"]
          ):
            cand = item.get("datePublished") or item.get("dateCreated")
            if cand and isinstance(cand, str):
              return cand.split("T")[0]
    except Exception:
      continue

  meta = trafilatura.extract_metadata(html_content)
  if meta and meta.date:
    return meta.date

  return "Date inconnue"


async def scrape_single_article(
    browser,
    site_name,
    url,
    slow_mode,
    semaphore,
    pbar,
    page_load_wait: float = 3.0,
    cf_retries: int = 0,
    use_curl_cffi: bool = False,
):
  async with semaphore:
    try:
      clean_url = url.split("?")[0].lower()
      if (
          clean_url.endswith(BINARY_EXTENSIONS)
          or "/is/image/" in url
          or "/content/dam/" in url
      ):
        tqdm.write(f"⏭️ Skipping binary URL: {url}")
        conn_u = sqlite3.connect(URL_DB, timeout=30.0)
        conn_u.cursor().execute(
            "UPDATE articles SET scraped = 1 WHERE url = ?", (url,)
        )
        conn_u.commit()
        conn_u.close()
        return

      if slow_mode:
        await asyncio.sleep(random.uniform(2.0, 4.0))

      if use_curl_cffi:
        html_content = await fetch_with_curl_cffi(url)
      else:
        page = await browser.get(url, new_tab=True)
        await asyncio.sleep(page_load_wait)
        html_content = await page.get_content()

        if is_cloudflare_challenge(html_content) and cf_retries > 0:
          for _ in range(cf_retries):
            await asyncio.sleep(5)
            html_content = await page.get_content()
            if not is_cloudflare_challenge(html_content):
              break

        await page.close()

      if is_cloudflare_challenge(html_content):
        tqdm.write(f"🚫 [{site_name}] CF challenge actif — skipping: {url}")
        return

      if (
          html_content.startswith(("\x89PNG", "\xff\xd8", "%PDF"))
          or "PNG\r\n" in html_content[:20]
          or "IHDR" in html_content[:50]
      ):
        tqdm.write(f"⚠️ Contenu binaire détecté pour {url}, ignoré.")
        return

      soup = BeautifulSoup(html_content, "html.parser")

      meta = trafilatura.extract_metadata(html_content)
      h1_tag = soup.find("h1")
      h1_text = (
          h1_tag.get_text(strip=True)
          if h1_tag and hasattr(h1_tag, "get_text")
          else ""
      )
      title = (
          meta.title
          if meta and meta.title
          else (h1_text if h1_text else "Sans titre")
      )

      pub_date = extract_accurate_date(soup, html_content)

      for img in soup.find_all("img"):
        real_src = (
            img.get("data-src") or img.get("data-original") or img.get("src")
        )
        if isinstance(real_src, list):
          real_src = real_src[0] if real_src else None
        if isinstance(real_src, str) and not real_src.startswith("data:image"):
          img["src"] = urljoin(url, real_src)
          if img.has_attr("data-src"):
            del img["data-src"]

      # --- DESTRUCTION PRÉVENTIVE DU BRUIT ---
      # Avant même de chercher la zone de texte, on détruit les menus, popups, headers et footers
      for unwanted in soup.find_all(["nav", "header", "footer", "aside", "form"]):
          unwanted.decompose()
      for unwanted in soup.select("#header, .header, .secondary-menu, .announcement-banner, #footer, .footer-page-content, #wrap_all > .header"):
          unwanted.decompose()

      def aem_blog_filter(c: Any) -> bool:
        if not c:
          return False
        if isinstance(c, list):
          c = " ".join(c)
        return "container-wp--main-content-blog" in str(c)

      def content_keywords_filter(c: Any) -> bool:
        if not c:
          return False
        if isinstance(c, list):
          c = " ".join(c)
        lower_c = str(c).lower()
        return any(
            k in lower_c
            for k in [
                "post-content",
                "article-content",
                "entry-content",
                "blog-content",
                "cmp-text",
            ]
        )

      def post_class_filter(c: Any) -> bool:
        if not c:
          return False
        if isinstance(c, list):
          c = " ".join(c)
        lower_c = str(c).lower()
        if "post" not in lower_c:
          return False
        return not any(
            sub in lower_c
            for sub in [
                "image",
                "thumb",
                "header",
                "banner",
                "author",
                "navigation",
            ]
        )

      # On priorise les conteneurs spécifiques (dont celui de DFIR Report) avant de fallback sur 'article' ou 'main'
      target_area = (
          soup.find(class_=aem_blog_filter)
          or soup.find(class_=re.compile(r"entry-content-wrapper", re.I)) # Ciblage spécifique DFIR Report
          or soup.find("article")
          or soup.find("main")
          or soup.find(class_=content_keywords_filter)
          or soup.find(class_=post_class_filter)
          or soup.body
      )

      if target_area and isinstance(target_area, Tag):
        # Ultime nettoyage de la zone cible trouvée
        for unwanted in target_area([
            "script",
            "style",
            "nav",
            "header",
            "footer",
            "aside",
            "form",
            ".blog_main_navigation",
            ".cmp-experiencefragment--header",
            ".cmp-experiencefragment--footer",
            ".modal_insert_location",
            ".container-wp--right-sidebar-blog",
        ]):
          unwanted.decompose()

        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.body_width = 0

        extracted_markdown = h.handle(str(target_area)).strip()
      else:
        extracted_markdown = "Content could not be extracted automatically."

      extracted_markdown = re.sub(
          r"^\s*!\[\]\(https://assets\.crowdstrike\.com/is/image/[^\)]+\)\s*",
          "",
          extracted_markdown,
      ).strip()

      if not extracted_markdown or len(extracted_markdown) < 50:
        extracted_markdown = "Content could not be extracted automatically."

      save_and_mark(site_name, url, title, pub_date, extracted_markdown)

      # --- PDF report detection & download ---
      pdf_url = detect_pdf_download_link(soup, url)
      if pdf_url:
        await download_pdf(pdf_url, site_name, title)

    except Exception as e:
      tqdm.write(f"❌ Error on {url}: {e}")
    finally:
      pbar.update(1)


def select_sources_to_rescrape(sources_config: dict) -> None:
  answer = (
      input(
          "\n🔄 Do you want to re-scrape already-scraped sources? (y/n)"
          " [default: n]: "
      )
      .strip()
      .lower()
  )
  if answer != "y":
    return

  source_names = list(sources_config.keys())
  if not source_names:
    print("⚠️  No sources found in sources.json.")
    return

  print("\n📋 Available sources:")
  print("  [0] All sources")
  for idx, name in enumerate(source_names, start=1):
    print(f"  [{idx}] {name}")

  raw = input(
      "\n👉 Enter source numbers to re-scrape (comma-separated, e.g. 1,3) or 0"
      " for all: "
  ).strip()
  if not raw:
    print("⚠️  No selection made. Skipping re-scrape reset.")
    return

  try:
    choices = [int(x.strip()) for x in raw.split(",")]
  except ValueError:
    print("❌ Invalid input. Skipping re-scrape reset.")
    return

  selected_sources = (
      source_names
      if 0 in choices
      else [
          source_names[c - 1] for c in choices if 1 <= c <= len(source_names)
      ]
  )

  conn = sqlite3.connect(URL_DB, timeout=30.0)
  cursor = conn.cursor()
  placeholders = ",".join("?" * len(selected_sources))
  cursor.execute(
      f"UPDATE articles SET scraped = 0 WHERE site_name IN ({placeholders})",
      selected_sources,
  )
  updated = cursor.rowcount
  conn.commit()
  conn.close()

  print(
      f"\n✅ Reset {updated} article(s) from {len(selected_sources)}"
      " source(s) to re-scrape:"
  )
  for name in selected_sources:
    print(f"   • {name}")


def run_post_cleanup():
  """Exécute dynamiquement tous les scripts de nettoyage présents

  dans le dossier 'scripts/' du projet.
  """
  scripts_dir = os.path.join(
      os.path.dirname(os.path.dirname(__file__)), "scripts"
  )

  if not os.path.isdir(scripts_dir):
    print(f"⚠️ Le dossier de scripts '{scripts_dir}' est introuvable.")
    return

  script_files = [
      f
      for f in os.listdir(scripts_dir)
      if f.endswith(".py") and f != "__init__.py"
  ]

  if not script_files:
    print("✨ Aucun script de nettoyage trouvé dans le dossier 'scripts/'.")
    return

  print(
      "\n🧹 Lancement automatique des scripts de nettoyage du dossier"
      " 'scripts/'..."
  )

  for script_name in script_files:
    script_path = os.path.join(scripts_dir, script_name)
    print(f"   ▶️ Exécution de : {script_name}")
    try:
      result = subprocess.run(
          [sys.executable, script_path], capture_output=True, text=True, check=True
      )
      if result.stdout.strip():
        for line in result.stdout.strip().splitlines():
          print(f"      {line}")
    except subprocess.CalledProcessError as e:
      print(f"❌ Erreur lors de l'exécution de {script_name} : {e}")
      if e.stderr:
        print(f"      {e.stderr.strip()}")


async def main():
  init_knowledge_db()

  with open("url_collector/sources.json", "r", encoding="utf-8") as f:
    sources_config = json.load(f)

  select_sources_to_rescrape(sources_config)

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
  max_workers = 3
  semaphore = asyncio.Semaphore(max_workers)

  try:
    with tqdm(
        total=len(pending_articles), desc="Scraping Progress", unit="art"
    ) as pbar:
      # Traitement par lots de 10 articles pour protéger nodriver et éviter le timeout réseau
      batch_size = 10
      for i in range(0, len(pending_articles), batch_size):
        batch = pending_articles[i : i + batch_size]
        tasks = []

        for site_name, url in batch:
          site_cfg = sources_config.get(site_name, {})
          is_slow = site_cfg.get("slow_mode", False)

          page_load_wait = float(site_cfg.get("page_load_wait", 3.0))
          cf_retries = int(site_cfg.get("cf_retries", 0))
          use_cffi = site_cfg.get("use_curl_cffi", False)

          tasks.append(
              scrape_single_article(
                  browser,
                  site_name,
                  url,
                  is_slow,
                  semaphore,
                  pbar,
                  page_load_wait=page_load_wait,
                  cf_retries=cf_retries,
                  use_curl_cffi=use_cffi,
              )
          )

        await asyncio.gather(*tasks)
        await asyncio.sleep(1.0)  # Micro-pause entre les lots

  finally:
    try:
      browser.stop()
    except RuntimeError:
      pass

  run_post_cleanup()


if __name__ == "__main__":
  try:
    asyncio.run(main())
    print("\n🎯 Content scraping process completed successfully!")
  except KeyboardInterrupt:
    print(
        "\n\n⚠️ Interruption utilisateur détectée (Ctrl+C). Fermeture propre"
        " des processus..."
    )
    sys.exit(0)