import asyncio
import json
import os
import random
import subprocess
import sys
from pathlib import Path
import nodriver as uc
from tqdm import tqdm

# Sécurisation des imports absolus pour l'exécution directe
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scraper.config import BINARY_EXTENSIONS, FILE_DOWNLOAD_EXTENSIONS
from scraper.db import (
    get_pending_articles,
    init_knowledge_db,
    mark_url_scraped,
    reset_scraped_status,
    save_and_mark,
)
from scraper.network import (
    download_file,
    fetch_with_curl_cffi,
    is_bot_challenge,
)
from scraper.parser import detect_file_download_links, parse_article_html


async def scrape_single_article(
    browser, site_name: str, url: str, slow_mode: bool, semaphore: asyncio.Semaphore,
    pbar: tqdm, page_load_wait: float = 3.0, cf_retries: int = 0,
    use_curl_cffi: bool = False, cookies: dict = None, user_agent: str = None
):
    async with semaphore:
        page = None
        try:
            clean_url = url.split("?")[0].lower()

            # 1. Check direct file extensions (Si l'URL est directement un CSV, PDF, etc.)
            if any(clean_url.endswith(ext) for ext in FILE_DOWNLOAD_EXTENSIONS):
                fallback_title = url.split("/")[-1] or "Direct_Download"
                await download_file(url, site_name, fallback_title, cookies, user_agent)
                mark_url_scraped(url)
                return

            # Ignorer les images et autres binaires inutiles
            if clean_url.endswith(BINARY_EXTENSIONS) or "/is/image/" in url or "/content/dam/" in url:
                tqdm.write(f"⏭️ Skipping binary URL: {url}")
                mark_url_scraped(url)
                return

            # 2. Récupération du HTML via Nodriver (fallback interactif)
            if not use_curl_cffi:
                if slow_mode:
                    await asyncio.sleep(random.uniform(2.0, 4.0))
                
                page = await browser.get(url, new_tab=True)
                await asyncio.sleep(page_load_wait)
                html_content = await page.get_content()

                max_challenge_wait = cf_retries if cf_retries > 0 else 4
                attempts = 0
                while is_bot_challenge(html_content) and attempts < max_challenge_wait:
                    attempts += 1
                    tqdm.write(f"   ⏳ [{site_name}] Anti-bot challenge active, waiting ({attempts}/{max_challenge_wait})...")
                    try:
                        await page.evaluate("window.scrollBy(0, 200);")
                    except Exception:
                        pass
                    await asyncio.sleep(5.0)
                    html_content = await page.get_content()

            # 3. Récupération du HTML via Curl_cffi (Ultra-rapide avec cookies récoltés)
            else:
                if slow_mode:
                    await asyncio.sleep(random.uniform(1.0, 2.5))
                
                # Fetch avec vérification d'un content-type pointant vers un fichier binaire/téléchargeable
                html_content, is_file = await fetch_with_curl_cffi(url, cookies, user_agent)
                if is_file:
                    fallback_title = url.split("/")[-1] or "Direct_File"
                    await download_file(url, site_name, fallback_title, cookies, user_agent)
                    mark_url_scraped(url)
                    return

            # 4. Abort si bloqué par WAF
            if is_bot_challenge(html_content):
                tqdm.write(f"🚫 [{site_name}] WAF / Anti-Bot block active — skipping: {url}")
                return

            # Abort de sécurité si c'est une image non détectée
            if html_content.startswith(("\x89PNG", "\xff\xd8", "%PDF")) or "PNG\r\n" in html_content[:20]:
                tqdm.write(f"⚠️ Binary payload detected on {url}, skipping.")
                return

            # 5. Parsing de l'article texte
            title, pub_date, markdown, soup = parse_article_html(html_content, url)

            low_title = title.lower()
            if any(marker in low_title for marker in ["checking your browser", "just a moment", "incident id", "request unsuccessful"]):
                tqdm.write(f"🚫 [{site_name}] Challenge title detected — skipping: {url}")
                return

            save_and_mark(site_name, url, title, pub_date, markdown)

            # 6. Extraction des fichiers joints (PDF, IoCs, ZIP...)
            file_urls = detect_file_download_links(soup, url)
            for f_url in file_urls:
                await download_file(f_url, site_name, title, cookies, user_agent)

        except Exception as e:
            tqdm.write(f"❌ Error on {url}: {e}")
        finally:
            if page:
                try:
                    await page.close()
                except Exception:
                    pass
            pbar.update(1)


def select_sources_to_rescrape(sources_config: dict) -> None:
    answer = input("\n🔄 Do you want to re-scrape already-scraped sources? (y/n) [default: n]: ").strip().lower()
    if answer != "y":
        return

    source_names = list(sources_config.keys())
    if not source_names:
        return

    print("\n📋 Available sources:")
    print("  [0] All sources")
    for idx, name in enumerate(source_names, start=1):
        print(f"  [{idx}] {name}")

    raw = input("\n👉 Enter source numbers to re-scrape (comma-separated, e.g. 1,3) or 0 for all: ").strip()
    if not raw:
        return

    try:
        choices = [int(x.strip()) for x in raw.split(",")]
    except ValueError:
        return

    selected_sources = source_names if 0 in choices else [source_names[c - 1] for c in choices if 1 <= c <= len(source_names)]
    updated = reset_scraped_status(selected_sources)
    print(f"\n✅ Reset {updated} article(s) from {len(selected_sources)} source(s) to re-scrape.")


def run_post_cleanup():
    scripts_dir = os.path.join(ROOT_DIR, "scripts")
    if not os.path.isdir(scripts_dir):
        return

    script_files = [f for f in os.listdir(scripts_dir) if f.endswith(".py") and f not in ["__init__.py", "export_markdown.py"]]
    if not script_files:
        return

    print("\n🧹 Lancement automatique des scripts de nettoyage ('scripts/')...")
    for script_name in sorted(script_files):
        script_path = os.path.join(scripts_dir, script_name)
        print(f"   ▶️ Exécution de : {script_name}")
        try:
            subprocess.run([sys.executable, script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de l'exécution de {script_name} : {e}")


async def main():
    init_knowledge_db()
    
    with open(os.path.join(ROOT_DIR, "url_collector", "sources.json"), "r", encoding="utf-8") as f:
        sources_config = json.load(f)

    select_sources_to_rescrape(sources_config)
    pending_articles = get_pending_articles()

    if not pending_articles:
        print("✨ No new articles to scrape at the moment.")
        return

    print(f"\n🚀 Starting extraction for {len(pending_articles)} articles...")

    # Groupe les articles par source pour traiter les WAF site par site
    articles_by_site = {}
    for site, url in pending_articles:
        articles_by_site.setdefault(site, []).append(url)

    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    browser_args = [
        "--headless=new",
        "--window-size=1920,1080",
        "--disable-blink-features=AutomationControlled",
        f"--user-agent={USER_AGENT}",
        "--lang=en-US,en;q=0.9",
    ]
    
    browser = await uc.start(browser_args=browser_args)

    try:
        with tqdm(total=len(pending_articles), desc="Scraping Progress", unit="art") as pbar:
            
            # Traitement séquentiel SITE par SITE
            for site_name, urls in articles_by_site.items():
                site_cfg = sources_config.get(site_name, {})
                is_slow = site_cfg.get("slow_mode", False)
                use_cffi = site_cfg.get("use_curl_cffi", False)
                
                cookies = {}
                
                # --- WAF COOKIE HARVESTING ---
                if is_slow:
                    base_url = site_cfg.get("url", urls[0])
                    domain_root = "/".join(base_url.split("/")[:3])
                    
                    tqdm.write(f"\n🛡️ [{site_name}] Pre-flight WAF clearance in progress...")
                    page = await browser.get(domain_root, new_tab=True)
                    await asyncio.sleep(8.0)
                    
                    try:
                        await page.evaluate("window.scrollBy(0, 300);")
                    except: pass
                    
                    await asyncio.sleep(2.0)
                    
                    try:
                        cdp_cookies = await page.send(uc.cdp.network.get_cookies(urls=[domain_root]))
                        cookies = {c.name: c.value for c in cdp_cookies}
                        tqdm.write(f"   ✅ [{site_name}] Harvested {len(cookies)} session cookies.")
                    except Exception as e:
                        tqdm.write(f"   ⚠️ [{site_name}] Failed to harvest cookies: {e}")
                    
                    await page.close()

                # Concurrence dynamique : 1 worker max pour les sites stricts, 3 pour les autres
                site_concurrency = 1 if is_slow else 3
                semaphore = asyncio.Semaphore(site_concurrency)

                tasks = []
                for url in urls:
                    tasks.append(
                        scrape_single_article(
                            browser, site_name, url, is_slow, semaphore, pbar,
                            page_load_wait=float(site_cfg.get("page_load_wait", 3.0)),
                            cf_retries=int(site_cfg.get("cf_retries", 0)),
                            use_curl_cffi=use_cffi, cookies=cookies, user_agent=USER_AGENT
                        )
                    )

                batch_size = 10
                for i in range(0, len(tasks), batch_size):
                    await asyncio.gather(*tasks[i:i+batch_size])
                    await asyncio.sleep(1.0 if not is_slow else 3.0)

    finally:
        try:
            browser.stop()
        except RuntimeError:
            pass
        await asyncio.sleep(0.5)

    run_post_cleanup()


if __name__ == "__main__":
    try:
        asyncio.run(main())
        print("\n🎯 Content scraping process completed successfully!")
    except KeyboardInterrupt:
        print("\n\n⚠️ Interruption utilisateur détectée (Ctrl+C). Fermeture propre des processus...")
        sys.exit(0)