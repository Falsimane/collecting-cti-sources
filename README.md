# Scraping CTI Sources

This project collects public threat-intelligence articles from configured sources, stores them in a local SQLite database, and learns selectors automatically when a source has not been configured yet.

It uses:
- Python 3.12+
- `uv` for dependency management
- `httpx` for HTTP requests
- `playwright` for JavaScript-heavy sites
- `selectolax` for HTML parsing

## Project structure

- `src/main.py` — entry point for the scraper pipeline
- `src/discovery.py` — source discovery logic (`httpx` and `playwright` engines)
- `src/extractor.py` — extraction of article title/date/content
- `src/db.py` — SQLite storage layer
- `src/models.py` — dataclasses for articles and source config
- `sources.json` — list of sources to scrape
- `threat_intel.db` — generated SQLite database

## Requirements

- Python 3.12 or newer
- `uv` installed
- A browser runtime for Playwright (Chromium)

## Install uv

If you do not already have `uv` installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If the install script adds `uv` to a non-standard PATH, make sure `~/.local/bin` is on your PATH or call `uv` using the full path.

You can verify the installation with:

```bash
uv --version
```

## Install dependencies

From the project root:

```bash
cd /path/to/scraping-cti-sources
uv sync
```

This creates the project environment and installs the dependencies declared in `pyproject.toml`.

## Install Playwright browsers

Some sources use the Playwright discovery engine. Install the browser runtime once:

```bash
uv run playwright install --with-deps chromium
```

## Run the scraper

From the project root:

```bash
uv run python src/main.py
```

This reads `sources.json`, discovers article URLs, extracts content, and saves new entries into `threat_intel.db`.

If a source has no selectors yet, the app attempts to learn the correct selectors automatically from the first fetched page and updates `sources.json`.

## Common workflow

1. Update `sources.json` with the domains you want to monitor.
2. Run:

```bash
uv sync
uv run python src/main.py
```

3. Check the SQLite database:

```bash
sqlite3 threat_intel.db
```

4. Query the articles table:

```sql
SELECT * FROM articles LIMIT 10;
```

## Notes

- The project writes new data only for URLs not already present in the SQLite database.
- The scraper is designed for public web pages and may need source-specific adjustments for anti-bot or dynamic content handling.
- `sources.json` is the central place to configure domains, engines, selectors, cookie handling, and pagination parameters.

## Useful commands

Create a fresh environment:

```bash
uv sync --reinstall
```

Run Python with the project environment without activating the venv manually:

```bash
uv run python -c "print('ready')"
```

If you want to use the local virtual environment directly:

```bash
source .venv/bin/activate
python src/main.py
```
