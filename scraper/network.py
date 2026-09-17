import os
import re
from curl_cffi.requests import AsyncSession as CffiSession
from tqdm import tqdm
from scraper.config import BOT_CHALLENGE_MARKERS, FILES_OUTPUT_DIR


def is_bot_challenge(html: str) -> bool:
    """Vérifie si le HTML retourné est une page de challenge Anti-Bot/WAF."""
    if not html:
        return False
    lower_html = html.lower()
    return any(marker in lower_html for marker in BOT_CHALLENGE_MARKERS)


async def fetch_with_curl_cffi(url: str, cookies: dict = None, user_agent: str = None) -> tuple[str, bool]:
    """Récupère le code HTML. Retourne (contenu_html, is_file) pour intercepter les téléchargements cachés."""
    profile = "chrome124"
    session_kwargs = {}
    if cookies is not None:
        session_kwargs["cookies"] = cookies
    if user_agent:
        session_kwargs["headers"] = {"User-Agent": user_agent}
    
    file_mime_types = ["application/pdf", "text/csv", "application/zip", "application/vnd.ms-excel", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]
    
    try:
        async with CffiSession(impersonate=profile, **session_kwargs) as session:
            resp = await session.get(url, timeout=45, allow_redirects=True)
            
            # Recherche case-insensitive du Content-Type
            content_type = ""
            for k, v in resp.headers.items():
                if k.lower() == "content-type":
                    content_type = v.lower()
                    break
            
            if any(mime in content_type for mime in file_mime_types):
                return "", True
            return resp.text, False
            
    except Exception as e:
        if "Impersonating" in str(e):
            async with CffiSession(impersonate="chrome124", **session_kwargs) as session:
                resp = await session.get(url, timeout=45, allow_redirects=True)
                
                content_type = ""
                for k, v in resp.headers.items():
                    if k.lower() == "content-type":
                        content_type = v.lower()
                        break
                        
                if any(mime in content_type for mime in file_mime_types):
                    return "", True
                return resp.text, False
        raise e


async def download_file(file_url: str, site_name: str, article_title: str, cookies: dict = None, user_agent: str = None) -> bool:
    """Télécharge un fichier (PDF, CSV, ZIP...) dans le dossier spécifique à la source."""
    
    # --- FIX GITHUB : Conversion vers le CDN brut pour éviter le Rate-Limit (Erreur 429) ---
    if "github.com" in file_url and "/blob/" in file_url:
        file_url = file_url.replace("https://github.com", "https://raw.githubusercontent.com").replace("/blob/", "/")
        file_url = file_url.split("?")[0] # On nettoie les paramètres inutiles

    dest_dir = os.path.join(FILES_OUTPUT_DIR, site_name)
    os.makedirs(dest_dir, exist_ok=True)

    clean_url = file_url.split("?")[0].rstrip("/")
    filename = clean_url.split("/")[-1]
    
    ext = ""
    if "." in filename:
        ext = "." + filename.split(".")[-1].lower()
    
    if ext not in [".pdf", ".csv", ".txt", ".xlsx", ".zip", ".yar", ".yara"]:
        ext = ".pdf"
        
    safe_title = re.sub(r"[^\w\s-]", "", article_title)[:80].strip().replace(" ", "_")
    
    if len(filename) < 5 or not filename.endswith(ext):
        file_basename = f"{safe_title}{ext}"
    else:
        file_basename = filename

    dest_path = os.path.join(dest_dir, file_basename)
    
    if os.path.exists(dest_path):
        tqdm.write(f"   📄 [{site_name}] File already exists: {file_basename}")
        return True

    profile = "chrome124"
    headers = {"Accept": "*/*", "Accept-Language": "en-US,en;q=0.9"}
    if user_agent:
        headers["User-Agent"] = user_agent

    try:
        async with CffiSession(impersonate=profile, cookies=cookies, headers=headers) as session:
            resp = await session.get(file_url, timeout=120, allow_redirects=True)
            
            if resp.status_code != 200:
                tqdm.write(f"   ⚠️ [{site_name}] File download HTTP {resp.status_code}: {file_url}")
                return False

            # =========================================================
            # ANTI-CORRUPTION SHIELD : Bloque le HTML infiltré
            # =========================================================
            
            # 1. Vérification par En-tête (robuste)
            content_type = ""
            for k, v in resp.headers.items():
                if k.lower() == "content-type":
                    content_type = v.lower()
                    break

            if "text/html" in content_type:
                tqdm.write(f"   ⚠️ [{site_name}] Fausse alerte (Page Web ignorée via header) : {file_url}")
                return False
                
            # 2. Vérification par contenu binaire brut (La sécurité ultime)
            head = resp.content[:100].lower()
            if b"<!doctype html" in head or b"<html" in head:
                tqdm.write(f"   ⚠️ [{site_name}] Fausse alerte (Page HTML déguisée en fichier ignorée) : {file_url}")
                return False

            # 3. Vérification de la signature stricte pour les PDF
            if ext == ".pdf" and not resp.content.startswith(b"%PDF"):
                tqdm.write(f"   ⚠️ [{site_name}] Fichier PDF corrompu rejeté : {file_url}")
                return False

            with open(dest_path, "wb") as f:
                f.write(resp.content)

        tqdm.write(f"   📥 [{site_name}] File saved: {file_basename}")
        return True
    except Exception as e:
        tqdm.write(f"   ❌ [{site_name}] File download error: {e}")
        return False