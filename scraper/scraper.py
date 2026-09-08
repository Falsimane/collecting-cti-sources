import asyncio
import random
import nodriver as uc
import trafilatura
import sqlite3
from tqdm import tqdm

# Define absolute or relative paths for databases
URL_DB = "db_outputs/urls_collection.db"  
KNOWLEDGE_DB = "db_outputs/cti_knowledge.db"

def init_knowledge_db():
    """
    Initializes the CTI knowledge SQLite database and creates the 'knowledge' table.
    A timeout is configured to prevent locking errors during concurrent writes.
    """
    conn = sqlite3.connect(KNOWLEDGE_DB, timeout=30.0)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_name TEXT,
            url TEXT UNIQUE,
            title TEXT,
            publication_date TEXT,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_and_mark(site_name, url, title, pub_date, content):
    """
    Safely saves the extracted Markdown content and metadata into cti_knowledge.db,
    then updates urls_collection.db to mark the URL as scraped (scraped = 1).
    """
    # 1. Save extracted knowledge
    conn_k = sqlite3.connect(KNOWLEDGE_DB, timeout=30.0)
    cursor_k = conn_k.cursor()
    try:
        cursor_k.execute('''
            INSERT OR IGNORE INTO knowledge (site_name, url, title, publication_date, content)
            VALUES (?, ?, ?, ?, ?)
        ''', (site_name, url, title, pub_date, content))
        conn_k.commit()
    except Exception as e:
        print(f"❌ Error saving content for {url}: {e}")
    finally:
        conn_k.close()

    # 2. Mark URL as scraped
    conn_u = sqlite3.connect(URL_DB, timeout=30.0)
    cursor_u = conn_u.cursor()
    cursor_u.execute('UPDATE articles SET scraped = 1 WHERE url = ?', (url,))
    conn_u.commit()
    conn_u.close()

async def scrape_single_article(browser, site_name, url, slow_mode, semaphore, pbar):
    """
    Asynchronously scrapes a single article page using nodriver and extracts 
    clean Markdown text and metadata using Trafilatura.
    """
    async with semaphore:
        try:
            # Apply a human-like random delay if slow mode is enabled for this source
            if slow_mode:
                await asyncio.sleep(random.uniform(4.0, 8.0))

            # Fetch raw page content using the undetected browser
            page = await browser.get(url, new_tab=True)
            await asyncio.sleep(3)  # Let JavaScript render
            html_content = await page.get_content()
            await page.close()

            # Extract clean Markdown text using Trafilatura (automatically strips footers, navs, ads)
            extracted_markdown = trafilatura.extract(
                html_content, 
                output_format='markdown', 
                include_links=True,
                include_images=True,
                include_tables=True
            )

            # Extract metadata (title, publication date) using Trafilatura
            metadata = trafilatura.extract_metadata(html_content)
            title = metadata.title if metadata and metadata.title else "Sans titre"
            pub_date = metadata.date if metadata and metadata.date else "Date inconnue"

            # Fallback if content extraction returns empty
            if not extracted_markdown:
                extracted_markdown = "Content could not be extracted automatically."

            # Save the results securely
            save_and_mark(site_name, url, title, pub_date, extracted_markdown)
            
        except Exception as e:
            # Use tqdm.write to avoid breaking the progress bar output layout
            tqdm.write(f"❌ Error on {url}: {e}")
        finally:
            # Update progress bar status
            pbar.update(1)

async def main():
    init_knowledge_db()
    
    # Prompt user for execution mode selection
    print("\n--- CTI SCRAPER CONFIGURATION ---")
    print("[1] Fast Mode (Parallel processing based on sources configuration)")
    print("[2] Safe/Slow Mode (Forces 1 worker globally to prevent WAF blocks)")
    choice = input("Select execution mode (1 or 2, default is 1): ").strip()
    
    force_slow_all = (choice == "2")

    # Load sources configuration to check 'slow_mode' property per site
    import json
    with open('url_collector/sources.json', 'r', encoding='utf-8') as f:
        sources_config = json.load(f)

    # Fetch all pending URLs from the collection database
    conn = sqlite3.connect(URL_DB)
    cursor = conn.cursor()
    cursor.execute('SELECT site_name, url FROM articles WHERE scraped = 0')
    pending_articles = cursor.fetchall()
    conn.close()
    
    if not pending_articles:
        print("✨ No new articles to scrape at the moment.")
        return

    print(f"\n🚀 Starting extraction for {len(pending_articles)} articles...")
    
    # Configure browser arguments to bypass bot checks
    browser_args = [
        "--headless=new", 
        "--window-size=1920,1080",
        "--disable-blink-features=AutomationControlled",
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "--lang=en-US,en;q=0.9",
    ]
    
    browser = await uc.start(browser_args=browser_args)
    
    # Set worker limits based on mode
    max_workers = 3 if force_slow_all else 20
    semaphore = asyncio.Semaphore(max_workers)
    
    try:
        # Run tasks with a nice visual progress bar
        with tqdm(total=len(pending_articles), desc="Scraping Progress", unit="art") as pbar:
            tasks = []
            for site_name, url in pending_articles:
                # Check if slow_mode is defined for this specific source in JSON
                site_slow_flag = sources_config.get(site_name, {}).get("slow_mode", False)
                is_slow = force_slow_all or site_slow_flag
                
                tasks.append(scrape_single_article(browser, site_name, url, is_slow, semaphore, pbar))
                
            await asyncio.gather(*tasks)
            
    finally:
        try:
            browser.stop()
        except RuntimeError:
            pass

if __name__ == '__main__':
    asyncio.run(main())
    print("\n🎯 Content scraping process completed successfully!")