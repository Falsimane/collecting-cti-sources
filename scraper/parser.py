import json
import re
from typing import Any
from urllib.parse import urljoin
from bs4 import BeautifulSoup, Tag
import html2text
import trafilatura
from scraper.config import FILE_DOWNLOAD_EXTENSIONS, FILE_DOWNLOAD_REGEX

def detect_file_download_links(soup: BeautifulSoup, base_url: str) -> list[str]:
    """Détecte tous les liens vers des fichiers (PDF, CSV, etc.) ou des IoCs dans le HTML."""
    found_links = set()
    
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if isinstance(href, list):
            href = href[0]
            
        abs_href = urljoin(base_url, href).split("#")[0]
        low_href = abs_href.lower().split("?")[0]
        text = a_tag.get_text(separator=" ", strip=True).lower()
        
        # 1. Le lien pointe directement vers une extension cible (.pdf, .csv, etc.)
        has_file_ext = any(low_href.endswith(ext) for ext in FILE_DOWNLOAD_EXTENSIONS)
        
        # 2. Le texte du lien évoque un rapport ou des IoCs
        has_matching_text = bool(re.search(FILE_DOWNLOAD_REGEX, text))
        
        if (has_file_ext or has_matching_text) and not abs_href.endswith("/"):
            # Sécurité : on ignore les liens qui renvoient juste à la racine du site
            if abs_href != base_url and "javascript:" not in low_href:
                found_links.add(abs_href)
                
    return list(found_links)


def extract_accurate_date(soup: BeautifulSoup, html_content: str) -> str:
    def publish_filter(c: Any) -> bool:
        if not c:
            return False
        if isinstance(c, list):
            c = " ".join(c)
        lower_c = str(c).lower()
        return any(k in lower_c for k in ["publish_info", "published-date", "post-date"])

    publish_div = soup.find(class_=publish_filter)
    if publish_div and isinstance(publish_div, Tag):
        p_tag = publish_div.find("p") or publish_div
        text = p_tag.get_text(strip=True) if hasattr(p_tag, "get_text") else ""
        date_match = re.search(r"([A-Za-z]+\s+\d{1,2},\s+\d{4})|(\d{4}-\d{2}-\d{2})", text)
        if date_match:
            return date_match.group(0)

    queries: list[dict[str, Any]] = [
        {"property": "article:published_time"},
        {"name": "publish-date"},
        {"property": "og:published_time"},
    ]
    for query in queries:
        tag = soup.find("meta", attrs=query)
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


def parse_article_html(html_content: str, url: str) -> tuple[str, str, str, BeautifulSoup]:
    soup = BeautifulSoup(html_content, "html.parser")

    meta = trafilatura.extract_metadata(html_content)
    h1_tag = soup.find("h1")
    h1_text = h1_tag.get_text(strip=True) if h1_tag and hasattr(h1_tag, "get_text") else ""
    title = meta.title if meta and meta.title else (h1_text if h1_text else "Sans titre")

    pub_date = extract_accurate_date(soup, html_content)

    # Normalize relative images
    for img in soup.find_all("img"):
        real_src = img.get("data-src") or img.get("data-original") or img.get("src")
        if isinstance(real_src, list):
            real_src = real_src[0] if real_src else None
        if isinstance(real_src, str) and not real_src.startswith("data:image"):
            img["src"] = urljoin(url, real_src)
            if img.has_attr("data-src"):
                del img["data-src"]

    # Decompose structural boilerplate
    for unwanted in soup.find_all(["nav", "header", "footer", "aside", "form"]):
        unwanted.decompose()
    for unwanted in soup.select(
        "#header, .header, .secondary-menu, .announcement-banner, #footer, .footer-page-content, #wrap_all > .header"
    ):
        unwanted.decompose()

    def content_keywords_filter(c: Any) -> bool:
        lower_c = str(c).lower() if c else ""
        return any(
            k in lower_c
            for k in ["post-content", "article-content", "entry-content", "blog-content", "cmp-text"]
        )

    def post_class_filter(c: Any) -> bool:
        lower_c = str(c).lower() if c else ""
        if "post" not in lower_c:
            return False
        return not any(sub in lower_c for sub in ["image", "thumb", "header", "banner", "author", "navigation"])

    target_area = (
        soup.find(class_=lambda c: "container-wp--main-content-blog" in str(c) if c else False)
        or soup.find(class_=re.compile(r"entry-content-wrapper", re.I))
        or soup.find("article")
        or soup.find("main")
        or soup.find(class_=content_keywords_filter)
        or soup.find(class_=post_class_filter)
        or soup.body
    )

    if target_area and isinstance(target_area, Tag):
        for unwanted in target_area([
            "script", "style", "nav", "header", "footer", "aside", "form",
            ".blog_main_navigation", ".cmp-experiencefragment--header",
            ".cmp-experiencefragment--footer", ".modal_insert_location",
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

    if not extracted_markdown or len(extracted_markdown) < 50:
        extracted_markdown = "Content could not be extracted automatically."

    return title, pub_date, extracted_markdown, soup