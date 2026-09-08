import asyncio
import nodriver as uc
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
import json
import sqlite3
import os
from tqdm import tqdm

# Define the local database name for URL storage
DB_NAME = "db_outputs/urls_collection.db"

def init_db():
    """
    Initializes the SQLite database and creates the 'articles' table 
    if it does not already exist. Also ensures the target directory exists.
    """
    os.makedirs(os.path.dirname(DB_NAME), exist_ok=True)
    conn = sqlite3.connect(DB_NAME, timeout=30.0)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_name TEXT,
            url TEXT UNIQUE,
            scraped INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(site_name, url):
    """
    Saves a unique article URL into the SQLite database. 
    Duplicates are ignored thanks to the UNIQUE constraint and INSERT OR IGNORE.
    """
    conn = sqlite3.connect(DB_NAME, timeout=30.0)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT OR IGNORE INTO articles (site_name, url, scraped) 
            VALUES (?, ?, 0)
        ''', (site_name, url))
        conn.commit()
    except Exception as e:
        tqdm.write(f"❌ Database error for {url}: {e}")
    finally:
        conn.close()

async def extract_cti_urls(config):
    """
    Asynchronous function to launch an undetected browser instance,
    crawl configured CTI sources, manage pagination, and extract relevant 
    article URLs with a tqdm progress bar tracking page extraction.
    """
    init_db()  # Ensure database and directory exist
    url_articles = set()
    
    # Calculate total pages across all sources for the tqdm progress bar
    total_pages_to_crawl = sum(data.get("max_pages", 1) for data in config.values())

    browser_args = [
        "--headless=new", 
        "--window-size=1920,1080",
        "--disable-blink-features=AutomationControlled",
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "--lang=en-US,en;q=0.9",
    ]
    
    browser = await uc.start(browser_args=browser_args)
    
    try:
        with tqdm(total=total_pages_to_crawl, desc="Collecting CTI URLs", unit="page") as pbar:
            for site, data in config.items():
                base_url = data["url"]
                max_pages = data.get("max_pages", 1)
                pag_type = data.get("pagination_pattern", "url")
                
                tqdm.write(f"\n🔍 Scraping {site} ({max_pages} pages configured)...")
                page = await browser.get(base_url)
                await asyncio.sleep(5)  # Let dynamic scripts execute
                
                for page_num in range(1, max_pages + 1):
                    pbar.set_postfix({"site": site, "page": page_num, "urls_found": len(url_articles)})
                    
                    if page_num > 1:
                        # Pagination via clicking (e.g. SPAs)
                        if pag_type == "click":
                            try:
                                target_page_text = str(page_num)
                                next_btn = await page.find(target_page_text)
                                if next_btn:
                                    await next_btn.click()
                                    await asyncio.sleep(4)
                                else:
                                    tqdm.write(f"⚠️ Pagination button '{target_page_text}' not found for {site}. Skipping remaining pages.")
                                    # Advance remaining planned pages for this site to keep progress bar accurate
                                    pbar.update(max_pages - page_num + 1)
                                    break
                            except Exception as e:
                                tqdm.write(f"❌ Click pagination error on {site}: {e}")
                                pbar.update(max_pages - page_num + 1)
                                break
                        else:
                            # Pagination via URL path reconstruction
                            parsed_base = urlparse(base_url)
                            if "blog_category" in base_url:
                                path_clean = parsed_base.path.rstrip('/')
                                paginated_path = f"{path_clean}/page/{page_num}/"
                                target_url = urlunparse((
                                    parsed_base.scheme,
                                    parsed_base.netloc,
                                    paginated_path,
                                    parsed_base.params,
                                    parsed_base.query,
                                    parsed_base.fragment
                                ))
                            else:
                                pattern = data.get("pagination_pattern", "page/{page}/")
                                target_url = urljoin(base_url, pattern.format(page=page_num))
                            
                            page = await browser.get(target_url)
                            await asyncio.sleep(4)
                    
                    content = await page.get_content()
                    soup = BeautifulSoup(content, 'html.parser')
                    
                    cards = soup.find_all(['a', 'div', 'article', 'li'], class_=re.compile(rf'\b{data["card_selector"]}\b'))
                    
                    if not cards:
                        tqdm.write(f"⚠️ No article cards found for {site} on page {page_num}. Ending site crawl.")
                        pbar.update(max_pages - page_num + 1)
                        break
                    
                    found_on_page = 0
                    for card in cards:
                        if card.find(string=re.compile(data["keyword"], re.IGNORECASE)):
                            link = card if card.name == 'a' else card.find('a', href=True)
                            if link and link.get('href'):
                                href = link.get('href')
                                absolute_url = urljoin(base_url, href)
                                
                                if absolute_url not in url_articles:
                                    url_articles.add(absolute_url)
                                    save_to_db(site, absolute_url)  
                                    found_on_page += 1
                                    
                    tqdm.write(f"   ➔ [{site}] Page {page_num}: {found_on_page} new URLs collected.")
                    pbar.update(1)
                    pbar.set_postfix({"site": site, "page": page_num, "urls_found": len(url_articles)})
                        
    finally:
        try:
            browser.stop()
        except RuntimeError:
            pass
            
    return url_articles

if __name__ == '__main__':
    with open('url_collector/sources.json', 'r', encoding='utf-8') as f:
        sources_cti = json.load(f)
        
    try:
        urls = asyncio.run(extract_cti_urls(sources_cti))
    except RuntimeError:
        urls = set()
    
    print(f"\n🎯 Total of {len(urls)} unique URLs collected and stored in '{DB_NAME}'!")