import json
from pathlib import Path
import httpx

from db import ThreatIntelDatabase
from discovery import get_discovery_engine
from extractor import deduce_selectors, parse_article_data, update_source_config
from models import Article, SourceConfig


class ScraperPipeline:
    def __init__(self, sources_file: str = "sources.json"):
        self.sources_file = sources_file
        self.db = ThreatIntelDatabase()
        self.http_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    def load_configs(self) -> list[SourceConfig]:
        path = Path(self.sources_file)
        if not path.exists():
            raise FileNotFoundError(f"Configuration {self.sources_file} introuvable.")
        raw_data = json.loads(path.read_text(encoding="utf-8"))
        return [SourceConfig.from_dict(key=k, data=v) for k, v in raw_data.items()]

    def run(self) -> None:
        for cfg in self.load_configs():
            print(f"\n{'='*65}\n[*] Source : {cfg.key} [{cfg.engine.upper()}]\n{'='*65}")

            engine = get_discovery_engine(cfg.engine)
            found_urls = engine.discover(cfg)
            new_urls = [u for u in found_urls if self.db.is_new(u)]
            print(f"[+] {len(found_urls)} URLs trouvées | {len(new_urls)} nouvelles.")

            if not new_urls:
                continue

            self._ingest_articles(cfg, new_urls)

    def _ingest_articles(self, cfg: SourceConfig, urls: list[str]) -> None:
        selectors = cfg.selectors or {}

        with httpx.Client(headers=self.http_headers, follow_redirects=True, timeout=20.0) as client:
            for idx, url in enumerate(urls, start=1):
                print(f"--> [{idx}/{len(urls)}] {url}")
                try:
                    res = client.get(url)
                    if res.status_code != 200:
                        print(f"    [-] Statut HTTP : {res.status_code}")
                        continue
                except httpx.HTTPError as err:
                    print(f"    [-] Erreur réseau : {err}")
                    continue

                # Déduction automatique si la source n'a pas encore de sélecteurs définis
                if not selectors or not selectors.get("content"):
                    print(f"    [*] Apprentissage des sélecteurs pour '{cfg.key}'...")
                    selectors = deduce_selectors(res.text)
                    update_source_config(self.sources_file, cfg.key, selectors)
                    cfg.selectors = selectors

                data = parse_article_data(res.text, selectors)

                article = Article(
                    url=url,
                    domain=cfg.key,
                    title=data["title"],
                    publication_date=data["date"],
                    content=data["content"],
                )
                self.db.save(article)
                print(f"    [✓] Titre : {article.title[:55]}...")
                print(f"        Date  : {article.publication_date}")
                print(f"        Taille: {len(article.content)} car.")


if __name__ == "__main__":
    ScraperPipeline("sources.json").run()