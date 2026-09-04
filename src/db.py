import sqlite3
from models import Article


class ThreatIntelDatabase:
    def __init__(self, db_path: str = "threat_intel.db"):
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self) -> None:
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS articles (
                    url TEXT PRIMARY KEY,
                    domain TEXT,
                    title TEXT,
                    publication_date TEXT,
                    content TEXT,
                    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

    def is_new(self, url: str) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM articles WHERE url = ?", (url,))
        return cursor.fetchone() is None

    def save(self, article: Article) -> None:
        with self.conn:
            self.conn.execute(
                """
                INSERT OR IGNORE INTO articles (url, domain, title, publication_date, content)
                VALUES (?, ?, ?, ?, ?)
                """,
                (article.url, article.domain, article.title, article.publication_date, article.content),
            )