import json
from pathlib import Path
import re
from selectolax.lexbor import LexborHTMLParser, LexborNode

# Formats de date courants dans les blogs de cybersécurité
DATE_PATTERNS = [
    # 1. "August 24, 2026" ou "August 24 2026" (Mois Jour, Année)
    r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)[\s\u00a0]+\d{1,2}(?:st|nd|rd|th)?(?:,)?[\s\u00a0]+\d{4}\b",

    # 2. "8 August 2025" ou "24 August 2026" (Jour Mois Année)
    r"\b\d{1,2}(?:st|nd|rd|th)?[\s\u00a0]+(?:January|February|March|April|May|June|July|August|September|October|November|December)[\s\u00a0]+\d{4}\b",

    # 3. Mois abrégés : "Aug 24, 2026" ou "24 Aug 2026"
    r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.?[\s\u00a0]+\d{1,2}(?:st|nd|rd|th)?(?:,)?[\s\u00a0]+\d{4}\b",
    r"\b\d{1,2}(?:st|nd|rd|th)?[\s\u00a0]+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.?[\s\u00a0]+\d{4}\b",

    # 4. Formats numériques : 2025.07.08, 2025-07-08, 2025/07/08
    r"\b\d{4}[./-]\d{2}[./-]\d{2}\b",

    # 5. Formats numériques : 08/07/2025, 08-07-2025
    r"\b\d{1,2}[./-]\d{1,2}[./-]\d{4}\b",

    # 6. Formats ISO : 2025-07-08T14:30:00Z
    r"\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\b",

    # 7. Formats avec jour de la semaine : "Monday, August 24, 2026"
    r"\b(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),[\s\u00a0]+(?:January|February|March|April|May|June|July|August|September|October|November|December)[\s\u00a0]+\d{1,2}(?:st|nd|rd|th)?(?:,)?[\s\u00a0]+\d{4}\b",

    # 8. Formats avec jour de la semaine et mois abrégé : "Mon, Aug 24, 2026"
    r"\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),[\s\u00a0]+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.?[\s\u00a0]+\d{1,2}(?:st|nd|rd|th)?(?:,)?[\s\u00a0]+\d{4}\b",

    # 9. Formats avec jour de la semaine et format numérique : "Mon, 24 Aug 2026"
    r"\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),[\s\u00a0]+\d{1,2}(?:st|nd|rd|th)?[\s\u00a0]+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.?[\s\u00a0]+\d{4}\b",
]

def extract_date(parser: LexborHTMLParser, date_selector: str | None = "auto") -> str:
    """Extrait la date de publication de manière robuste."""
    # 1. Si un sélecteur CSS spécifique est fourni (autre que "auto")
    if date_selector and date_selector != "auto":
        node = parser.css_first(date_selector)
        if node:
            dt = node.attributes.get("datetime")
            return dt.strip() if dt else node.text().strip()

    # 2. Recherche standard via attributs sémantiques HTML
    sem_node = parser.css_first("time, [itemprop='datePublished'], meta[property='article:published_time']")
    if sem_node:
        dt = sem_node.attributes.get("datetime") or sem_node.attributes.get("content")
        if dt:
            return dt.strip()
        if sem_node.text().strip():
            return sem_node.text().strip()

    # 3. Nettoyage du DOM pour éviter de matcher du CSS/JS (ex: hexagone #45bfff)
    for noise in parser.css("script, style, noscript, svg, header, footer, nav"):
        noise.decompose()

    body_text = parser.body.text() if parser.body else ""

    # 4. Parcours des regex ordonnées par spécificité
    for pat in DATE_PATTERNS:
        match = re.search(pat, body_text, re.IGNORECASE)
        if match:
            return match.group(0).strip()

    return "Date inconnue"


def _get_clean_tag_selector(node: LexborNode | None, fallback: str) -> str:
    if not node:
        return fallback
    node_id = node.attributes.get("id")
    if node_id and not any(ch.isdigit() for ch in node_id):
        return f"#{node_id}"

    classes = [c for c in node.attributes.get("class", "").split() if not any(x.isdigit() for x in c)]
    if classes:
        return f"{node.tag}.{classes[0]}"

    return node.tag


def deduce_selectors(html: str) -> dict:
    parser = LexborHTMLParser(html)
    return {
        "title": _get_clean_tag_selector(parser.css_first("h1, h2"), "h1"),
        "date": "auto",
        "content": _get_clean_tag_selector(parser.css_first("article, main, .entry-content"), "article"),
    }


def parse_article_data(html: str, selectors: dict) -> dict[str, str]:
    parser = LexborHTMLParser(html)

    title_sel = selectors.get("title") or "h1"
    content_sel = selectors.get("content") or "article"
    date_sel = selectors.get("date") or "auto"

    t_el = parser.css_first(title_sel)
    c_el = parser.css_first(content_sel)
    extracted_date = extract_date(parser, date_sel)

    return {
        "title": t_el.text().strip() if t_el else "Sans titre",
        "date": extracted_date,
        "content": " ".join(c_el.text().split()) if c_el else "Contenu non extrait",
    }


def update_source_config(sources_file: str, key: str, selectors: dict) -> None:
    path = Path(sources_file)
    data = json.loads(path.read_text(encoding="utf-8"))
    data[key]["selectors"] = selectors
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")