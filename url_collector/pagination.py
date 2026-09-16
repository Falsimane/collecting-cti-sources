import asyncio
import re
from urllib.parse import urljoin, urlparse, urlunparse
from bs4 import BeautifulSoup
from database import save_batch_to_db

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
            if content:
                return content
        except Exception:
            pass
        try:
            content = await page.evaluate("document.documentElement.outerHTML")
            if content:
                return str(content)
        except Exception:
            pass
        await asyncio.sleep(1.0)
    return ""


HTML_TAGS = {"article", "div", "section", "li", "a", "main"}


def extract_cards(soup, card_sel: str):
    """Extrait les cartes de manière robuste via sélecteur CSS natif ou Fallback Regex."""
    parts = []
    for part in card_sel.split(','):
        part = part.strip()
        if (
            not part.startswith('.') 
            and not part.startswith('#') 
            and not part.startswith('>') 
            and not part.startswith('[')
            and part.lower() not in HTML_TAGS
        ):
            part = f".{part}"
        parts.append(part)
    
    css_selector = ", ".join(parts)
    
    try:
        cards = soup.select(css_selector)
        if cards:
            return cards
    except Exception:
        pass
        
    fallback_class = [c.strip().lstrip('.>') for c in card_sel.split(',')][0]
    return soup.find_all(class_=re.compile(re.escape(fallback_class), re.I))


def get_card_link(card, base_url: str = ""):
    """Extrait l'URL de l'article en privilégiant le titre et en ignorant les taxonomies."""
    raw_href = None

    if card.name == "a" and card.get("href"):
        raw_href = card.get("href")

    if not raw_href:
        title_el = card.find(["h1", "h2", "h3", "h4", "h5", "h6"]) or card.find(
            class_=re.compile(r"(title|heading|entry-title|post-title)", re.I)
        )
        if title_el:
            link = title_el if title_el.name == "a" else title_el.find("a", href=True)
            if link and link.get("href"):
                raw_href = link.get("href")

    if not raw_href:
        for a in card.find_all("a", href=True):
            href = a.get("href")
            if isinstance(href, list):
                href = href[0] if href else ""
            if not href or not isinstance(href, str):
                continue
            low_href = href.lower()
            if any(tax in low_href for tax in ["/category/", "/tag/", "/tags/", "/author/", "/topic/", "/topics/", "#", "javascript:"]):
                continue
            raw_href = href
            break

    if not raw_href:
        first_a = card.find("a", href=True)
        if first_a:
            raw_href = first_a.get("href")

    if not raw_href:
        return None

    if isinstance(raw_href, list):
        raw_href = raw_href[0]

    return urljoin(base_url, raw_href) if base_url else raw_href


async def handle_scroll_pagination(
    page, site: str, base_url: str, card_sel: str, keywords: list, 
    next_btn_sel: str | None, shared_urls: set, max_scrolls: int, url_must_include: str = ""
) -> int:
    """Gère l'Infinite Scroll par batch SQLite et retourne le nombre d'URLs uniques trouvées."""
    iteration = 1
    consecutive_empty = 0
    local_site_urls = set()

    await page.evaluate("""
        (() => {
            const overlays = document.querySelectorAll('#onetrust-consent-sdk, .cc-window, [id*="cookie"], [class*="cookie"]');
            overlays.forEach(el => el.style.display = 'none');
        })();
    """)

    # On sécurise max_scrolls pour forcer un entier
    max_scrolls = int(max_scrolls) if max_scrolls else 15

    while iteration <= max_scrolls:
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(1.5)
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(1.5)

        clicked = await page.evaluate(f"""
            (() => {{
                let btn = null;
                if ('{next_btn_sel}') {{
                    const btns = Array.from(document.querySelectorAll('{next_btn_sel}'));
                    btn = btns.reverse().find(el => el.offsetParent !== null);
                }}
                if (!btn) {{
                    const elements = Array.from(document.querySelectorAll('a, button, div, span'));
                    btn = elements.reverse().find(el => 
                        el.offsetParent !== null && el.textContent && 
                        (el.textContent.trim().toLowerCase().includes('view more') || 
                         el.textContent.trim().toLowerCase().includes('load more'))
                    );
                }}
                if (btn) {{
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
            if consecutive_empty >= MAX_EMPTY_PAGES_TOLERANCE:
                break
            continue

        soup = BeautifulSoup(html, "html.parser")
        cards = extract_cards(soup, card_sel)

        batch_new_urls = []

        for card in cards:
            card_full_text = card.get_text(separator=' ', strip=True).lower()

            if keywords and not any(kw in card_full_text for kw in keywords):
                continue

            abs_url = get_card_link(card, base_url)
            if not abs_url:
                continue

            low_url = abs_url.lower()

            # FILTRE STRICT URL (pour Rapid7 et autres)
            if url_must_include and url_must_include.lower() not in low_url:
                continue

            if any(err in low_url for err in ['403', '404', '500', 'error', 'access-denied', 'block']):
                continue
            if any(tax in low_url for tax in ['/category/', '/tag/', '/tags/', '/author/']):
                continue

            if abs_url not in shared_urls and abs_url not in local_site_urls:
                shared_urls.add(abs_url)
                local_site_urls.add(abs_url)
                batch_new_urls.append(abs_url)

        new_found = len(batch_new_urls)
        if batch_new_urls:
            save_batch_to_db(site, batch_new_urls)

        print(f"   [{site}] {len(local_site_urls)}")

        if new_found == 0:
            consecutive_empty += 1
            if consecutive_empty >= MAX_EMPTY_PAGES_TOLERANCE:
                print(f"🛑 [{site}] {len(local_site_urls)} — terminé")
                break
        else:
            consecutive_empty = 0

        iteration += 1

    if iteration > max_scrolls:
        print(f"🛑 [{site}] {len(local_site_urls)} — terminé")

    return len(local_site_urls)