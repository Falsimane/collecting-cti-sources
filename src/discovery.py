import re
from abc import ABC, abstractmethod
from urllib.parse import urljoin, urlparse

import httpx
from playwright.sync_api import Locator, Page, sync_playwright
from selectolax.lexbor import LexborHTMLParser

from models import SourceConfig


def clean_article_urls(links: list[str], current_url: str, explicit_path: str | None = None) -> set[str]:
    parsed_base = urlparse(current_url)
    base_netloc = parsed_base.netloc
    listing_path = parsed_base.path.rstrip("/")

    # Récupère le mot-clé de section (ex: 'insidethelab', 'posts', etc.)
    target_segment = (explicit_path if explicit_path else parsed_base.path).strip("/")

    cleaned = set()

    for href in links:
        if not href or not (href.startswith("http://") or href.startswith("https://")):
            continue

        parsed = urlparse(href)

        # 1. Même domaine
        if parsed.netloc != base_netloc:
            continue

        candidate_path = parsed.path.rstrip("/")

        # 2. Le chemin doit contenir le segment cible
        if target_segment and target_segment not in candidate_path:
            continue

        # 3. Ne doit pas être la page racine ou la page de listing
        if candidate_path in ("", listing_path):
            continue

        cleaned.add(f"{parsed.scheme}://{parsed.netloc}{candidate_path}")

    return cleaned


class BaseDiscovery(ABC):
    @abstractmethod
    def discover(self, cfg: SourceConfig) -> list[str]:
        pass


class HttpxDiscovery(BaseDiscovery):
    def discover(self, cfg: SourceConfig) -> list[str]:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        try:
            with httpx.Client(headers=headers, follow_redirects=True, timeout=15.0) as client:
                res = client.get(cfg.domain)
                if res.status_code != 200:
                    return []
        except httpx.HTTPError:
            return []

        parser = LexborHTMLParser(res.text)
        raw_links = [urljoin(str(res.url), a.attributes.get("href", "")) for a in parser.css("a[href]")]
        return list(clean_article_urls(raw_links, str(res.url), cfg.article_path))


class PlaywrightDiscovery(BaseDiscovery):
    def discover(self, cfg: SourceConfig) -> list[str]:
        pagination = cfg.pagination or {}
        max_pages = pagination.get("max_pages", 5)
        next_selector = pagination.get("next_selector", "a.next, .pagination-next, a[rel='next']")
        urls: set[str] = set()

        with sync_playwright() as p:
            # 1. Lancement avec flag anti-détection
            browser = p.chromium.launch(
                headless=True,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--disable-web-security",
                    "--no-sandbox",
                    "--disable-setuid-sandbox",
                    "--disable-info-bars",
                    "--disable-extensions",
                    "--disable-dev-shm-usage",
                    "--window-size=1920,1080",
                    "-disable-features=IsolateOrigins,site-per-process",
                      ]
            )

            # 2. Contexte avec profil navigateur standard
            context = browser.new_context(
                user_agent=(
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                    ' like Gecko) Chrome/120.0.0.0 Safari/537.36'
                ),
                permissions=["geolocation", "notifications"],
                ignore_https_errors=False,
                accept_downloads=True,                
                viewport={'width': 1920, 'height': 1080},
                locale="en-US"
            )
            page = context.new_page()

            # 3. Masquage de navigator.webdriver
            page.add_init_script(
                "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
            )

            response = page.goto(cfg.domain, wait_until="networkidle", timeout=60000)
            if response and response.status in (403, 503):
                print(f"    [-] Statut HTTP {response.status} : blocage potentiel.")

            # Gestion de la bannière cookie si configurée
            if cfg.cookie_element:
                self._apply_action(page, cfg.cookie_element)

            # Application du filtre si requis
            if cfg.needs_filtering and cfg.filter_elements:
                self._apply_action(page, cfg.filter_elements)

            # Parcours paginé et extraction
            for _ in range(1, max_pages + 1):
                try:
                    page.wait_for_selector("a[href]", timeout=8000)
                except Exception:
                    pass

                # Extraction directe via le DOM JS
                raw_urls = page.eval_on_selector_all(
                    "a[href]",
                    "elements => elements.map(el => el.href)"
                )

                found = clean_article_urls(raw_urls, page.url, cfg.article_path)
                urls.update(found)

                # Pagination
                next_btn = page.locator(next_selector)
                if next_btn.count() > 0 and next_btn.first.is_visible():
                    next_btn.first.click()
                    page.wait_for_timeout(2000)
                else:
                    break

            context.close()
            browser.close()

        return list(urls)

    def _apply_action(self, page: Page, element_cfg: dict) -> None:
        for strategy, params in element_cfg.items():
            try:
                locator: Locator | None = None

                if strategy == "get-by-role":
                    locator = page.get_by_role(params.get("role"), name=re.compile(params.get("name"), re.IGNORECASE))
                elif strategy == "get-by-text":
                    locator = page.get_by_text(params.get("text"), exact=params.get("exact", False))
                elif strategy == "get-by-label":
                    locator = page.get_by_label(params.get("label"))
                elif strategy in ("css", "locator"):
                    locator = page.locator(params.get("selector"))

                if locator:
                    index = params.get("index")
                    target = locator.nth(index) if index is not None else locator.first

                    state = params.get("state", "visible")
                    try:
                        target.wait_for(state=state, timeout=4000)
                    except Exception:
                        target = locator.locator("visible=true").first
                        target.wait_for(state="visible", timeout=3000)

                    if params.get("role") in ("radio", "checkbox"):
                        target.check(force=True)
                    else:
                        target.click()

                    page.wait_for_timeout(1500)
            except Exception:
                pass


def get_discovery_engine(engine_name: str) -> BaseDiscovery:
    engines: dict[str, type[BaseDiscovery]] = {
        "httpx": HttpxDiscovery,
        "playwright": PlaywrightDiscovery,
    }
    engine_class = engines.get(engine_name.lower())
    if not engine_class:
        raise ValueError(f"Moteur inconnu : '{engine_name}'.")
    return engine_class()