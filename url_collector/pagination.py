import asyncio
import re
from urllib.parse import urljoin, urlparse, urlunparse
from bs4 import BeautifulSoup
from tqdm import tqdm
from database import save_to_db

MAX_EMPTY_PAGES_TOLERANCE = 5

def build_paginated_url(base_url: str, page_num: int, pattern: str) -> str:
    """Construit l'URL de pagination en conservant les arguments existants."""
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

async def get_page_html(page) -> str:
    """Tente de récupérer le HTML complet de façon robuste."""
    for _ in range(3):
        try:
            content = await page.get_content()
            if content: return content
        except Exception:
            pass
        try:
            content = await page.evaluate("document.documentElement.outerHTML")
            if content: return str(content)
        except Exception:
            pass
        await asyncio.sleep(1.0)
    return ""

async def handle_scroll_pagination(
    page, site: str, base_url: str, card_sel: str, keyword: str, 
    next_btn_sel: str | None, shared_urls: set, pbar: tqdm, max_scrolls: int
):
    """Gère l'Infinite Scroll avec une limite de sécurité (max_scrolls)."""
    iteration = 1
    consecutive_empty = 0

    await page.evaluate("""
        (() => {
            const overlay = document.getElementById('onetrust-consent-sdk');
            if (overlay) overlay.style.display = 'none';
        })();
    """)

    while iteration <= max_scrolls:
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(1.5)
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(1.5)

        clicked = await page.evaluate(f"""
            (() => {{
                let btn = null;
                if ('{next_btn_sel}') {{
                    btn = document.querySelector('{next_btn_sel}');
                }}
                if (!btn) {{
                    const elements = Array.from(document.querySelectorAll('a, button, div, span'));
                    btn = elements.find(el => 
                        el.textContent && 
                        (el.textContent.trim().toLowerCase().includes('view more') || 
                         el.textContent.trim().toLowerCase().includes('load more'))
                    );
                }}
                if (btn && btn.offsetParent !== null) {{
                    btn.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                    btn.click();
                    return true;
                }}
                return false;
            }})()
        """)
        await asyncio.sleep(4.5 if clicked else 2.5)

        html = await get_page_html(page)
        if not html:
            consecutive_empty += 1
            if consecutive_empty >= MAX_EMPTY_PAGES_TOLERANCE: break
            continue

        soup = BeautifulSoup(html, "html.parser")
        cards = soup.find_all(["a", "div", "article", "li"], class_=lambda c: c and card_sel in c.split())
        if not cards:
            cards = soup.find_all(class_=re.compile(re.escape(card_sel), re.I))

        articles_found = 0
        new_found = 0

        for card in cards:
            if keyword and keyword.lower() not in card.get_text().lower():
                continue

            link = card if card.name == "a" else card.find("a", href=True)
            if link and link.get("href"):
                abs_url = urljoin(base_url, link.get("href"))
                
                low_url = abs_url.lower()
                if any(err in low_url for err in ['403', '404', '500', 'error', 'access-denied', 'block']):
                    continue

                articles_found += 1
                if abs_url not in shared_urls:
                    shared_urls.add(abs_url)
                    save_to_db(site, abs_url)
                    new_found += 1

        if articles_found == 0:
            consecutive_empty += 1
            tqdm.write(f"   ⚠️ [{site}] Scroll #{iteration} : 0 article ({consecutive_empty}/{MAX_EMPTY_PAGES_TOLERANCE}).")
            if consecutive_empty >= MAX_EMPTY_PAGES_TOLERANCE:
                tqdm.write(f"🛑 [{site}] Arrêt : flux épuisé.")
                break
        else:
            consecutive_empty = 0
            tqdm.write(f"   ➔ [{site}] Scroll #{iteration} analysé ({articles_found} articles, {new_found} inédits).")
            pbar.update(1)

        iteration += 1

    if iteration > max_scrolls:
        tqdm.write(f"🛑 [{site}] Arrêt : Limite maximale de {max_scrolls} scrolls atteinte.")