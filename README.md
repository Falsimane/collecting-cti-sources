# Scraping CTI Sources

Pipeline Python pour collecter des URLs d’articles CTI puis extraire leur contenu en Markdown, avec stockage local SQLite.

## Fonctionnement du projet

Le projet se lance via un menu principal (`main.py`) avec 2 étapes :

1. **URL Collector** (`url_collector/collector.py`)
   - Parcourt les sources définies dans `url_collector/sources.json`
   - Gère la pagination (pattern d’URL ou clic)
   - Filtre les cartes d’articles avec `card_selector` + `keyword`
   - Enregistre les URLs uniques dans `db_outputs/urls_collection.db` (`articles.scraped = 0`)

2. **Content Scraper** (`scraper/scraper.py`)
   - Lit les URLs non scrapées depuis `db_outputs/urls_collection.db`
   - Ouvre chaque page avec `nodriver`
   - Extrait contenu + métadonnées via `trafilatura`
   - Stocke le résultat dans `db_outputs/cti_knowledge.db`
   - Marque chaque URL traitée (`articles.scraped = 1`)

## Arborescence utile

- `main.py` : menu CLI de la pipeline
- `url_collector/collector.py` : collecte d’URLs
- `scraper/scraper.py` : scraping du contenu
- `url_collector/sources.json` : configuration des sources
- `db_outputs/` : bases SQLite générées localement
- `pyproject.toml` : dépendances Python

## Prérequis

- Python 3.12+
- `uv`

## Installation

```bash
uv sync
```

## Lancement

```bash
uv run python main.py
```

Puis choisir :
- `[1]` pour collecter/mettre à jour les URLs
- `[2]` pour scraper le contenu des URLs en attente

## Configuration des sources

Chaque source dans `url_collector/sources.json` supporte notamment :

- `url` : page de départ
- `card_selector` : classe CSS ciblant les blocs d’articles
- `keyword` : mot-clé attendu dans le bloc
- `max_pages` : nombre maximal de pages à parcourir
- `pagination_pattern` :
  - `click` pour pagination par clic
  - ou pattern URL (`page/{page}/`, etc.)
- `slow_mode` : active des délais supplémentaires pour la source

## Bases de données générées

- `db_outputs/urls_collection.db`
  - table `articles(id, site_name, url, scraped)`
- `db_outputs/cti_knowledge.db`
  - table `knowledge(id, site_name, url, title, publication_date, content)`

## Notes

- Les doublons d’URLs sont évités (`url` en `UNIQUE`).
- Le scraper ne traite que les URLs avec `scraped = 0`.
- Si aucune URL n’est collectée, l’étape de scraping est bloquée par le menu principal.
