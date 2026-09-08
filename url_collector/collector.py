import asyncio
import nodriver as uc
from nodriver.cdp import network
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
import json
import sqlite3
import os
from tqdm import tqdm

DB_NAME = "db_outputs/urls_collection.db"

# Seuil de sécurité universel : nombre de pages consécutives sans nouvelle URL avant d'arrêter
MAX_EMPTY_PAGES_TOLERANCE = 5

def init_db():
    """
    Initializes the SQLite database and creates the 'articles' table 
    if it does not already exist.
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

def save_to_db(site_name: str, url: str):
    """
    Saves a newly discovered URL into the SQLite database.
    Duplicates are ignored thanks to the UNIQUE constraint on the url column.
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
        tqdm.write(f"❌ Erreur SQLite pour {url}: {e}")
    finally:
        conn.close()

def build_paginated_url(base_url: str, page_num: int, pattern: str) -> str:
    """
    Constructs the paginated URL preserving query parameters (Rapid7) 
    or path-based segments (WordPress).
    """
    if page_num == 1:
        return base_url

    parsed = urlparse(base_url)
    if "blog_category" in base_url or parsed.query:
        path_clean = parsed.path.rstrip('/')
        return urlunparse((
            parsed.scheme,
            parsed.netloc,
            f"{path_clean}/page/{page_num}/",
            parsed.params,
            parsed.query,
            parsed.fragment
        ))
    return urljoin(base_url, pattern.format(page=page_num))

async def crawl_single_source(browser, site: str, data: dict, semaphore: asyncio.Semaphore, pbar: tqdm, shared_urls: set):
    """
    Asynchronously crawls a single CTI source with a universal circuit-breaker tolerance.
    """
    async with semaphore:
        base_url = data["url"]
        pag_type = data.get("pagination_pattern", "page/{page}/")
        is_click_mode = pag_type == "click"
        card_sel = data.get("card_selector", "card")
        keyword = data.get("keyword", "")

        page = await browser.get("about:blank", new_tab=True)
        current_status = 200

        def on_response(event: network.ResponseReceived):
            nonlocal current_status
            if event.type_ == network.ResourceType.DOCUMENT:
                current_status = event.response.status

        page.add_handler(network.ResponseReceived, on_response)
        page_num = 1
        consecutive_empty_pages = 0

        try:
            await page.get(base_url)
            await asyncio.sleep(4.0)

            while True:
                # -------------------------------------------------------------
                # 1. NAVIGATION (URL OU SIMULATION DE CLIC)
                # -------------------------------------------------------------
                if page_num > 1:
                    if is_click_mode:
                        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                        await asyncio.sleep(1.5)

                        click_success = await page.evaluate(f"""
                            (() => {{
                                const elements = Array.from(document.querySelectorAll('button, a, div, li, span'));
                                const btn = elements.find(el => el.textContent.trim() === '{page_num}' && el.children.length === 0);
                                if (btn) {{
                                    btn.click();
                                    return true;
                                }}
                                return false;
                            }})()
                        """)

                        if click_success:
                            await asyncio.sleep(4.0)
                        else:
                            tqdm.write(f"🛑 [{site}] Arrêt : bouton de la page {page_num} introuvable (fin de catalogue).")
                            break
                    else:
                        target_url = build_paginated_url(base_url, page_num, pag_type)

                        # Navigation simple
                        await page.get(target_url)
                        await asyncio.sleep(3.5)

                        # 1. Détection de redirection CMS (ex: HarfangLab qui revient sur la page 1 ou /insidethelab/)
                        current_browser_url = await page.evaluate("window.location.href")
                        if str(page_num) not in current_browser_url and (
                            "page" not in current_browser_url
                            or "/page/1" in current_browser_url
                        ):
                            tqdm.write(
                                f"🛑 [{site}] Arrêt : redirection détectée vers"
                                f" {current_browser_url} (fin de catalogue)."
                            )
                            break

                # -------------------------------------------------------------
                # 2. VÉRIFICATION DU DOM & DES CARTES D'ARTICLES
                # -------------------------------------------------------------
                html = await page.get_content()
                soup = BeautifulSoup(html, "html.parser")

                # Arrêt 3 : Mention 404 explicite dans le titre
                page_title = soup.find('title').get_text().lower() if soup.find('title') else ""
                if "404" in page_title or "not found" in page_title or "page non trouvée" in page_title:
                    tqdm.write(f"🛑 [{site}] Arrêt : mention 404 dans le titre à la page {page_num}.")
                    break

                cards = soup.find_all(['a', 'div', 'article', 'li'], class_=re.compile(rf'\b{card_sel}\b'))
                
                # Arrêt 4 : La page ne contient structurellement AUCUNE carte d'article
                if not cards:
                    tqdm.write(f"🛑 [{site}] Arrêt : aucun conteneur d'article dans le DOM à la page {page_num}.")
                    break

                # -------------------------------------------------------------
                # 3. EXTRACTION ET COMPTAGE DES NOUVELLES URLS
                # -------------------------------------------------------------
                new_on_page = 0
                for card in cards:
                    if keyword and not card.find(string=re.compile(keyword, re.IGNORECASE)):
                        continue

                    link = card if card.name == 'a' else card.find('a', href=True)
                    if link and link.get('href'):
                        abs_url = urljoin(base_url, link.get('href'))
                        if abs_url not in shared_urls:
                            shared_urls.add(abs_url)
                            save_to_db(site, abs_url)
                            new_on_page += 1

                # -------------------------------------------------------------
                # 4. RÈGLE UNIVERSELLE : CIRCUIT BREAKER (TOLÉRANCE DE N PAGES)
                # -------------------------------------------------------------
                if new_on_page == 0:
                    consecutive_empty_pages += 1
                    tqdm.write(f"   ⚠️ [{site}] Page {page_num} : 0 nouvelle URL (marge de sécurité : {consecutive_empty_pages}/{MAX_EMPTY_PAGES_TOLERANCE}).")
                    
                    if consecutive_empty_pages >= MAX_EMPTY_PAGES_TOLERANCE:
                        tqdm.write(f"🛑 [{site}] Arrêt : seuil de {MAX_EMPTY_PAGES_TOLERANCE} pages consécutives sans aucun nouvel article atteint.")
                        break
                else:
                    # Réinitialisation du compteur dès qu'une URL valide est trouvée
                    consecutive_empty_pages = 0
                    tqdm.write(f"   ➔ [{site}] Page {page_num} analysée ({new_on_page} URLs ajoutées).")

                pbar.update(1)
                page_num += 1

        except Exception as e:
            tqdm.write(f"❌ Erreur sur {site} (page {page_num}): {e}")
        finally:
            await page.close()

async def main():
    init_db()

    with open('url_collector/sources.json', 'r', encoding='utf-8') as f:
        sources_cti = json.load(f)

    browser_args = [
        "--headless=new",
        "--window-size=1920,1080",
        "--disable-blink-features=AutomationControlled",
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "--lang=en-US,en;q=0.9",
    ]
    browser = await uc.start(browser_args=browser_args)

    semaphore = asyncio.Semaphore(300)
    shared_urls = set()

    try:
        with tqdm(desc="Collecte globale", unit="page") as pbar:
            tasks = [
                crawl_single_source(browser, site, data, semaphore, pbar, shared_urls)
                for site, data in sources_cti.items()
            ]
            await asyncio.gather(*tasks)
    finally:
        try:
            browser.stop()
        except RuntimeError:
            pass

    print(f"\n🎯 Collecte terminée : {len(shared_urls)} URLs enregistrées dans {DB_NAME}.")

if __name__ == '__main__':
    asyncio.run(main())