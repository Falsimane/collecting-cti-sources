import asyncio
import json
import os
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import nodriver as uc
from nodriver.cdp import network
from tqdm import tqdm
import sys  

from database import init_db, save_to_db, DB_NAME
from pagination import build_paginated_url, get_page_html, handle_scroll_pagination, MAX_EMPTY_PAGES_TOLERANCE

async def crawl_single_source(browser, site: str, data: dict, semaphore: asyncio.Semaphore, pbar: tqdm, shared_urls: set):
    """Exécute la collecte pour une source donnée selon sa méthode de pagination."""
    async with semaphore:
        base_url = data["url"]
        pag_type = data.get("pagination_pattern", "page/{page}/")
        is_click_mode = pag_type == "click"
        card_sel = data.get("card_selector", "card")
        keyword = data.get("keyword", "").strip()
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

        try:
            await page.get(base_url)
            await asyncio.sleep(4.5)

            if pag_type == "scroll":
                tqdm.write(f"📜 [{site}] Démarrage de la collecte par Infinite Scroll (max {max_scrolls} scrolls)...")
                await handle_scroll_pagination(
                    page, site, base_url, card_sel, keyword, next_btn_sel, shared_urls, pbar, max_scrolls
                )
                return

            while True:
                if page_num > 1:
                    if is_click_mode:
                        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                        await asyncio.sleep(1.5)

                        click_success = await page.evaluate(f"""
                            (() => {{
                                const elements = Array.from(document.querySelectorAll('button, a, div, li, span'));
                                const btn = elements.find(el => el.textContent.trim() === '{page_num}' && el.children.length === 0);
                                if (btn) {{
                                    btn.click(); return true;
                                }}
                                return false;
                            }})()
                        """)
                        if click_success: await asyncio.sleep(4.0)
                        else:
                            tqdm.write(f"🛑 [{site}] Arrêt : bouton page {page_num} introuvable.")
                            break
                    else:
                        target_url = build_paginated_url(base_url, page_num, pag_type)
                        current_status = 200
                        await page.get(target_url)
                        await asyncio.sleep(3.5)

                        if current_status >= 400:
                            tqdm.write(f"🛑 [{site}] Arrêt : code HTTP {current_status} à la page {page_num}.")
                            break

                        current_browser_url = await page.evaluate("window.location.href")
                        if str(page_num) not in current_browser_url and ("page" not in current_browser_url or "/page/1" in current_browser_url):
                            tqdm.write(f"🛑 [{site}] Arrêt : redirection vers {current_browser_url}.")
                            break

                html = await get_page_html(page)
                if not html: break

                soup = BeautifulSoup(html, "html.parser")
                title_tag = soup.find("title")
                page_title = title_tag.get_text().lower() if title_tag and hasattr(title_tag, "get_text") else ""
                
                if "404" in page_title or "not found" in page_title or "page non trouvée" in page_title:
                    tqdm.write(f"🛑 [{site}] Arrêt : 404 dans le titre à la page {page_num}.")
                    break

                # Correction Pylance sur la lambda class_ et find_all
                def class_filter(c):
                    if not c:
                        return False
                    if isinstance(c, list):
                        c = " ".join(c)
                    return card_sel in str(c).split()

                cards = soup.find_all(["a", "div", "article", "li"], class_=class_filter)
                if not cards:
                    cards = soup.find_all(class_=re.compile(re.escape(card_sel), re.I))

                articles_found = 0
                new_on_page = 0

                for card in cards:
                    if keyword and keyword.lower() not in card.get_text().lower(): continue
                    link = card if card.name == "a" else card.find("a", href=True)
                    if link and link.has_attr("href"):
                        href_val = link.get("href")
                        # Sécurisation Pylance pour s'assurer que href est bien une string exploitable
                        if isinstance(href_val, list):
                            href_val = href_val[0] if href_val else ""
                        if not href_val or not isinstance(href_val, str):
                            continue

                        abs_url = urljoin(base_url, href_val)
                        
                        low_url = abs_url.lower()
                        if any(err in low_url for err in ['403', '404', '500', 'error', 'access-denied', 'block']):
                            continue

                        articles_found += 1
                        if abs_url not in shared_urls:
                            shared_urls.add(abs_url)
                            save_to_db(site, abs_url)
                            new_on_page += 1

                if articles_found == 0:
                    consecutive_empty_pages += 1
                    tqdm.write(f"   ⚠️ [{site}] Page {page_num} : 0 article trouvé ({consecutive_empty_pages}/{MAX_EMPTY_PAGES_TOLERANCE}).")
                    if consecutive_empty_pages >= MAX_EMPTY_PAGES_TOLERANCE:
                        tqdm.write(f"🛑 [{site}] Arrêt : catalogue épuisé.")
                        break
                else:
                    consecutive_empty_pages = 0
                    tqdm.write(f"   ➔ [{site}] Page {page_num} analysée ({articles_found} articles vus, {new_on_page} inédits).")

                pbar.update(1)
                page_num += 1

        except Exception as e:
            tqdm.write(f"❌ Erreur sur {site}: {e}")
        finally:
            await page.close()

async def main():
  init_db()

  workers = 20
  if len(sys.argv) > 1:
    try:
      workers = int(sys.argv[1])
    except ValueError:
      pass

  with open(
      os.path.join(os.path.dirname(__file__), "sources.json"),
      "r",
      encoding="utf-8",
  ) as f:
    sources_cti = json.load(f)

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

  try:
    with tqdm(
        desc=f"Collecte globale ({workers} workers)", unit="page"
    ) as pbar:
      tasks = [
          crawl_single_source(
              browser, site, data, semaphore, pbar, shared_urls
          )
          for site, data in sources_cti.items()
      ]
      await asyncio.gather(*tasks)
  finally:
    try:
      browser.stop()
    except RuntimeError:
      pass

  print(
      f"\n🎯 Collecte terminée : {len(shared_urls)} URLs inédites enregistrées."
  )

if __name__ == "__main__":
    asyncio.run(main())