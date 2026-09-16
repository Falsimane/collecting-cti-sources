import os
import sqlite3
import re
from tqdm import tqdm

# On calcule les chemins absolus par rapport au dossier courant du projet
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
KNOWLEDGE_DB = os.path.join(PROJECT_ROOT, "db_outputs", "cti_knowledge.db")
EXPORT_DIR = os.path.join(PROJECT_ROOT, "db_outputs", "markdown_exports")

def export_articles_to_markdown():
    """Exporte les articles de la base de données vers des fichiers Markdown locaux."""
    print("\n" + "="*50)
    answer = input("💾 Voulez-vous exporter les articles en fichiers Markdown locaux ? (y/n) [default: n]: ").strip().lower()
    if answer != "y":
        print("⏭️ Exportation ignorée.")
        return

    if not os.path.exists(KNOWLEDGE_DB):
        print(f"⚠️ La base de données {KNOWLEDGE_DB} est introuvable.")
        return

    conn = sqlite3.connect(KNOWLEDGE_DB)
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            """
            SELECT site_name, url, title, publication_date, content 
            FROM knowledge 
            WHERE content IS NOT NULL AND content != 'Content could not be extracted automatically.'
            """
        )
        articles = cursor.fetchall()
    except sqlite3.OperationalError:
        print("⚠️ Table 'knowledge' introuvable. Aucune donnée à exporter.")
        conn.close()
        return

    conn.close()

    if not articles:
        print("⚠️ Aucun article valide trouvé dans la base de données pour l'export.")
        return

    print(f"\n📦 Préparation de l'export pour {len(articles)} articles...")
    os.makedirs(EXPORT_DIR, exist_ok=True)
    
    exported_count = 0
    for site_name, url, title, pub_date, content in tqdm(articles, desc="Génération des fichiers", unit="fichier"):
        
        site_dir = os.path.join(EXPORT_DIR, site_name)
        os.makedirs(site_dir, exist_ok=True)
        
        safe_title = re.sub(r'[\\/*?:"<>|]', "", title).strip()[:100]
        if not safe_title:
            safe_title = "Article_Sans_Titre"
            
        safe_date = re.sub(r'[\\/*?:"<>|]', "", pub_date).strip() if pub_date else "Date_inconnue"
        
        filename = f"{safe_date} - {safe_title}.md"
        filepath = os.path.join(site_dir, filename)
        
        md_content = f"# {title}\n\n"
        md_content += f"- **Source :** {site_name}\n"
        md_content += f"- **URL :** {url}\n"
        md_content += f"- **Date :** {pub_date}\n\n"
        md_content += "---\n\n"
        md_content += content
        
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(md_content)
            exported_count += 1
        except Exception as e:
            tqdm.write(f"❌ Erreur lors de l'export de {filename} : {e}")

    print(f"\n✅ Export terminé ! {exported_count} fichiers stockés dans :\n   {EXPORT_DIR}")

if __name__ == "__main__":
    export_articles_to_markdown()