import asyncio
import json
import os
import sys
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import nodriver as uc
from nodriver.cdp import network

from database import init_db, save_batch_to_db

from pagination import (
    build_paginated_url,
    get_page_html,
    handle_scroll_pagination,
    MAX_EMPTY_PAGES_TOLERANCE,
    extract_cards,
    get_card_link,
)


async def crawl_single_source(
    browser,
    site: str,
    data: dict,
    semaphore: asyncio.Semaphore,
    shared_urls: set,
    source_stats: dict,
):
    """Exécute la collecte pour une source donnée selon sa méthode de pagination."""
    async with semaphore:
        base_url = data["url"]
        pag_type = data.get("pagination_pattern", "page/{page}/")
        is_click_mode = pag_type == "click"
        card_sel = data.get("card_selector", "card")
        page_load_wait = data.get("page_load_wait", 3.5)
        url_must_include = data.get("url_must_include", "")

        raw_keyword = data.get("keyword", "")
        if isinstance(raw_keyword, str):
            keyword = raw_keyword.strip()
            keywords = [keyword.lower()] if keyword else []
        elif isinstance(raw_keyword, list):
            keywords = [kw.strip().lower() for kw in raw_keyword if kw.strip()]
        else:
            keywords = []

        next_btn_sel = data.get("next_button_selector", "")
        max_scrolls = data.get("max_pages", 15)

        page = await browser.get("about:blank", new_tab=True)
        current_status = 200

        def on_response(event: network.ResponseReceived):
            nonlocal current_status
            if event.type_ == network.ResourceType.DOCUMENT:
                current_status = event.response.status

        page.add_handler(network.ResponseReceived, on_response)
        page_num = 1
        consecutive_empty_pages = 0
        total_site_urls = 0

        try:
            await page.get(base_url)
            await asyncio.sleep(page_load_wait)

            if pag_type == "scroll":
                print(f"📜 [{site}] Démarrage Infinite Scroll (max {max_scrolls} scrolls)...")
                total_site_urls = await handle_scroll_pagination(
                    page, site, base_url, card_sel, keywords, next_btn_sel, shared_urls, max_scrolls, url_must_include
                )
                return

            while True:
                if page_num > 1:
                    if is_click_mode:
                        await page.evaluate("""
                            (() => {
                                const overlays = document.querySelectorAll('#onetrust-consent-sdk, .cc-window, [id*="cookie"], [class*="cookie"]');
                                overlays.forEach(el => el.style.display = 'none');
                            })();
                        """)
                        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                        await asyncio.sleep(1.5)

                        click_success = await page.evaluate(f"""
                            (() => {{
                                const elements = Array.from(document.querySelectorAll('button, a, div, li, span'));
                                const btn = elements.find(el => el.textContent.trim() === '{page_num}' && el.children.length === 0 && el.offsetParent !== null);
                                if (btn) {{
                                    btn.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                                    btn.click(); 
                                    return true;
                                }}
                                return false;
                            }})()
                        """)
                        if click_success:
                            await asyncio.sleep(4.0)
                        else:
                            print(f"🛑 [{site}] Arrêt : bouton page {page_num} introuvable.")
                            break
                    else:
                        target_url = build_paginated_url(base_url, page_num, pag_type)
                        current_status = 200
                        await page.get(target_url)
                        await asyncio.sleep(page_load_wait)

                        if current_status >= 400:
                            print(f"🛑 [{site}] Arrêt : code HTTP {current_status} à la page {page_num}.")
                            break

                        current_browser_url = await page.evaluate("window.location.href")
                        if str(page_num) not in current_browser_url and ("page" not in current_browser_url or "/page/1" in current_browser_url):
                            print(f"🛑 [{site}] Arrêt : redirection vers {current_browser_url}.")
                            break

                html = await get_page_html(page)
                if not html:
                    break

                soup = BeautifulSoup(html, "html.parser")
                title_tag = soup.find("title")
                page_title = title_tag.get_text().lower() if title_tag and hasattr(title_tag, "get_text") else ""

                if any(err in page_title for err in ["404", "not found", "page non trouvée"]):
                    print(f"🛑 [{site}] 404 — arrêt")
                    break

                cards = extract_cards(soup, card_sel)
                new_on_page = 0
                batch_urls = []

                for card in cards:
                    card_full_text = card.get_text(separator=' ', strip=True).lower()

                    if keywords and not any(kw in card_full_text for kw in keywords):
                        continue

                    href_val = get_card_link(card)
                    if not href_val:
                        continue

                    abs_url = urljoin(base_url, href_val)
                    low_url = abs_url.lower()

                    # FILTRE STRICT URL
                    if url_must_include and url_must_include.lower() not in low_url:
                        continue

                    if any(err in low_url for err in ['403', '404', '500', 'error', 'access-denied', 'block']):
                        continue
                    if any(tax in low_url for tax in ['/category/', '/tag/', '/tags/', '/author/']):
                        continue

                    if abs_url not in shared_urls:
                        shared_urls.add(abs_url)
                        batch_urls.append(abs_url)
                        new_on_page += 1

                if batch_urls:
                    save_batch_to_db(site, batch_urls)

                total_site_urls += new_on_page
                
                print(f"   [{site}] {total_site_urls}")

                if new_on_page == 0:
                    consecutive_empty_pages += 1
                    if consecutive_empty_pages >= MAX_EMPTY_PAGES_TOLERANCE:
                        print(f"🛑 [{site}] {total_site_urls} — terminé")
                        break
                else:
                    consecutive_empty_pages = 0

                page_num += 1

        except Exception as e:
            print(f"❌ Erreur sur {site}: {e}")
        finally:
            source_stats[site] = total_site_urls
            await page.close()


def select_sources(sources_cti: dict) -> dict:
    if "--all" in sys.argv:
        return sources_cti

    source_names = list(sources_cti.keys())

    print("\n================ SÉLECTION DES SOURCES ================")
    print("[A] Toutes les sources")
    for i, name in enumerate(source_names, start=1):
        url = sources_cti[name]["url"]
        print(f"[{i}] {name:20s}  ({url})")
    print("========================================================")

    choice = input("\nEntrez 'A' pour tout scraper, ou les numéros séparés par des virgules (ex: 1,3,5) : ").strip()

    if choice.lower() == "a" or choice == "":
        print("✅ Toutes les sources sélectionnées.")
        return sources_cti

    selected = {}
    for part in choice.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            idx = int(part)
            if 1 <= idx <= len(source_names):
                key = source_names[idx - 1]
                selected[key] = sources_cti[key]
            else:
                print(f"⚠️  Numéro {idx} ignoré (hors limites 1-{len(source_names)}).")
        except ValueError:
            print(f"⚠️  Entrée '{part}' ignorée (pas un nombre valide).")

    if not selected:
        print("❌ Aucune source valide sélectionnée. Abandon.")
        sys.exit(1)

    print(f"✅ {len(selected)} source(s) sélectionnée(s) : {', '.join(selected.keys())}")
    return selected


async def main():
    init_db()

    workers = 20
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        workers = int(sys.argv[1])

    sources_path = os.path.join(os.path.dirname(__file__), "sources.json")
    with open(sources_path, "r", encoding="utf-8") as f:
        sources_cti = json.load(f)

    sources_cti = select_sources(sources_cti)

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

    semaphore = asyncio.Semaphore(workers)
    shared_urls = set()
    source_stats = {}

    print(f"\n🚀 Collecte en cours sur {len(sources_cti)} source(s) avec {workers} worker(s)...")

    try:
        tasks = [
            crawl_single_source(browser, site, data, semaphore, shared_urls, source_stats)
            for site, data in sources_cti.items()
        ]
        await asyncio.gather(*tasks)
    finally:
        try:
            browser.stop()
        except RuntimeError:
            pass
        
    await asyncio.sleep(0.5)

    print("\n┌────────────────────┬────────┐")
    print("│ Source             │  URLs  │")
    print("├────────────────────┼────────┤")
    for src, count in sorted(source_stats.items()):
        print(f"│ {src:18s} │ {count:6d} │")
    print("├────────────────────┼────────┤")
    print(f"│ {'TOTAL':18s} │ {sum(source_stats.values()):6d} │")
    print("└────────────────────┴────────┘")

    print(f"\n🎯 Collecte terminée : {len(shared_urls)} URLs inédites enregistrées.")


if __name__ == "__main__":
    asyncio.run(main())