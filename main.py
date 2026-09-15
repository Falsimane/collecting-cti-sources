import os
import sqlite3
import subprocess
import sys

# Path to the URL database created by the collector
URL_DB = os.path.join("db_outputs", "urls_collection.db")


def get_pending_urls_count():
  """Checks if the collection database exists and counts

  how many URLs are pending extraction (scraped = 0).
  Returns (total_urls, pending_urls).
  """
  if not os.path.exists(URL_DB):
    return None, None

  try:
    conn = sqlite3.connect(URL_DB)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='articles'"
    )
    if not cursor.fetchone():
      conn.close()
      return 0, 0

    cursor.execute("SELECT COUNT(*) FROM articles")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM articles WHERE scraped = 0")
    pending = cursor.fetchone()[0]

    conn.close()
    return total, pending
  except sqlite3.Error:
    return 0, 0


def run_collector():
  """Lance le collecteur d'URLs avec sélection interactive des sources."""
  print(
      "\n🚀 Lancement du collecteur d'URLs (20 workers par défaut)..."
  )
  script_path = os.path.join("url_collector", "collector.py")

  if not os.path.exists(script_path):
    print(f"❌ Error: Could not find collector script at '{script_path}'.")
    return

  subprocess.run([sys.executable, script_path, "20"])


def run_scraper():
  """Valide les pré-requis et lance le contenu scraper."""
  total, pending = get_pending_urls_count()

  if total is None or total == 0:
    print("\n⚠️  Action required: No URLs found to scrape!")
    print(
        "👉 You must run Step [1] (URL Collector) first to discover articles"
        " before scraping content.\n"
    )
    return

  if pending == 0:
    print(f"\n💡 All {total} collected articles have already been scraped.")
    print("   You can re-scrape specific sources from within the scraper menu.")

  print(f"\n🚀 Launching Content Scraper ({pending} pending articles ready)...")
  script_path = os.path.join("scraper", "scraper.py")

  if not os.path.exists(script_path):
    print(f"❌ Error: Could not find scraper script at '{script_path}'.")
    return

  subprocess.run([sys.executable, script_path])


def main():
  """Main CLI menu loop for the CTI pipeline."""
  while True:
    total, pending = get_pending_urls_count()

    if total is None or total == 0:
      db_status = "No URLs collected yet - run [1] first"
    else:
      db_status = f"{pending} pending / {total} total URLs"

    print("\n================ CTI PIPELINE MAIN MENU ================")
    print(f" Status: [{db_status}]")
    print("--------------------------------------------------------")
    print("[1] Run URL Collector   (Step 1: Discover & store URLs — select sources)")
    print("[2] Run Content Scraper (Step 2: Extract content, metadata & Markdown)")
    print("[3] Exit")

    choice = input("\nEnter your choice (1, 2, or 3): ").strip()

    if choice == "1":
      run_collector()
    elif choice == "2":
      run_scraper()
    elif choice == "3":
      print("👋 Exiting CTI Pipeline. Goodbye!")
      break
    else:
      print("❌ Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
  main()