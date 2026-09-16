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
- `[1]` pour collecter/mettre à jour les URLs (avec sélection interactive des sources)
- `[2]` pour scraper le contenu des URLs en attente

### Sélection des sources

Au lancement du collecteur (étape 1), un menu interactif s'affiche :
- Entrer `A` (ou laisser vide) pour scraper **toutes** les sources
- Entrer des numéros séparés par des virgules (ex: `1,3,5`) pour ne scraper que les sources choisies

Pour exécuter directement sur toutes les sources sans le prompt interactif :
```bash
uv run python url_collector/collector.py 20 --all
```

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

## Bases de données et fichiers générés

- `db_outputs/urls_collection.db`
  - table `articles(id, site_name, url, scraped)`
- `db_outputs/cti_knowledge.db`
  - table `knowledge(id, site_name, url, title, publication_date, content)`
- `db_outputs/pdf/<site_name>/`
  - Rapports PDF téléchargés automatiquement lors du scraping

## Notes

- Les doublons d'URLs sont évités (`url` en `UNIQUE`).
- Le scraper ne traite que les URLs avec `scraped = 0`.
- Si aucune URL n'est collectée, l'étape de scraping est bloquée par le menu principal.
- Le scraper détecte automatiquement les boutons de téléchargement PDF (« Download the full report content », « Télécharger le rapport complet », etc.) et sauvegarde les PDF dans `db_outputs/pdf/`.