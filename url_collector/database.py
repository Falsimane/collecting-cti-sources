import os
import sqlite3
from tqdm import tqdm

DB_NAME = "db_outputs/urls_collection.db"


def init_db():
    """Initialise la base de données SQLite et la table des articles."""
    os.makedirs(os.path.dirname(DB_NAME), exist_ok=True)
    conn = sqlite3.connect(DB_NAME, timeout=30.0)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_name TEXT,
            url TEXT UNIQUE,
            scraped INTEGER DEFAULT 0
        )
    """
    )
    conn.commit()
    conn.close()


def save_batch_to_db(site_name: str, urls: list):
    """Sauvegarde un lot d'URLs en une seule transaction SQL."""
    if not urls:
        return
    conn = sqlite3.connect(DB_NAME, timeout=30.0)
    cursor = conn.cursor()
    try:
        # Tuple de 2 éléments car 'scraped' est fixé en dur à 0 dans la requête
        data = [(site_name, url) for url in urls]
        cursor.executemany(
            """
            INSERT OR IGNORE INTO articles (site_name, url, scraped) 
            VALUES (?, ?, 0)
        """,
            data,
        )
        conn.commit()
    except Exception as e:
        tqdm.write(f"❌ Erreur SQLite batch pour {site_name}: {e}")
    finally:
        conn.close()