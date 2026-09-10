import sqlite3
import re

KNOWLEDGE_DB = "db_outputs/cti_knowledge.db"

def clean_crowdstrike_banner_robust():
    conn = sqlite3.connect(KNOWLEDGE_DB)
    cur = conn.cursor()

    # Diagnostic : Afficher les noms de sites exacts présents dans la base
    cur.execute("SELECT DISTINCT site_name FROM knowledge")
    print(f"📋 Sites présents dans la base : {cur.fetchall()}")

    # Récupération sans filtre strict sur le nom au cas où le site_name serait différent
    cur.execute("SELECT id, site_name, content FROM knowledge WHERE LOWER(site_name) LIKE '%crowdstrike%'")
    rows = cur.fetchall()

    print(f"🔍 {len(rows)} article(s) trouvé(s) avec le filtre crowdstrike.")
    updated_count = 0

    # Pattern exact pour trouver la chaîne au tout début du contenu (avec espaces optionnels)
    target_pattern = re.compile(r'^\s*!\[\]\(https://assets\.crowdstrike\.com/is/image/[^\)]+\)', re.MULTILINE)

    for row_id, site_name, content in rows:
        if not content:
            continue
          
        # Supprime la chaîne exacte au début ou n'importe où sur une ligne
        cleaned_content = target_pattern.sub('', content).strip()

        if cleaned_content != content:
            cur.execute("UPDATE knowledge SET content = ? WHERE id = ?", (cleaned_content, row_id))
            updated_count += 1

    conn.commit()
    conn.close()

    print(f"\n✨ Nettoyage terminé :")
    print(f"   • {updated_count} article(s) nettoyé(s).")

if __name__ == "__main__":
    clean_crowdstrike_banner_robust()