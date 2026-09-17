import sqlite3
from tqdm import tqdm
from scraper.config import KNOWLEDGE_DB, URL_DB

def init_knowledge_db():
    conn = sqlite3.connect(KNOWLEDGE_DB, timeout=30.0)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_name TEXT,
            url TEXT UNIQUE,
            title TEXT,
            publication_date TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_and_mark(site_name: str, url: str, title: str, pub_date: str, content: str):
    conn_k = sqlite3.connect(KNOWLEDGE_DB, timeout=30.0)
    cursor_k = conn_k.cursor()
    try:
        cursor_k.execute(
            """
            INSERT OR REPLACE INTO knowledge (site_name, url, title, publication_date, content)
            VALUES (?, ?, ?, ?, ?)
            """,
            (site_name, url, title, pub_date, content),
        )
        conn_k.commit()
    except Exception as e:
        tqdm.write(f"❌ Error saving content for {url}: {e}")
    finally:
        conn_k.close()

    mark_url_scraped(url)


def mark_url_scraped(url: str):
    conn_u = sqlite3.connect(URL_DB, timeout=30.0)
    cursor_u = conn_u.cursor()
    cursor_u.execute("UPDATE articles SET scraped = 1 WHERE url = ?", (url,))
    conn_u.commit()
    conn_u.close()


def get_pending_articles():
    conn = sqlite3.connect(URL_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT site_name, url FROM articles WHERE scraped = 0")
    pending = cursor.fetchall()
    conn.close()
    return pending


def reset_scraped_status(selected_sources: list[str]) -> int:
    conn = sqlite3.connect(URL_DB, timeout=30.0)
    cursor = conn.cursor()
    placeholders = ",".join("?" * len(selected_sources))
    cursor.execute(
        f"UPDATE articles SET scraped = 0 WHERE site_name IN ({placeholders})",
        selected_sources,
    )
    updated = cursor.rowcount
    conn.commit()
    conn.close()
    return updated