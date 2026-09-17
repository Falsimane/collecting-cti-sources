import os

URL_DB = os.path.join("db_outputs", "urls_collection.db")
KNOWLEDGE_DB = os.path.join("db_outputs", "cti_knowledge.db")

# Dossier unifié pour toutes les extractions (PDF, CSV, TXT, ZIP...)
FILES_OUTPUT_DIR = os.path.join("db_outputs", "output_files")

# Extensions ignorées pour le scraping de texte (images, etc.)
BINARY_EXTENSIONS = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".ico",
)

BOT_CHALLENGE_MARKERS = [
    # Cloudflare
    "checking your browser",
    "just a moment...",
    "enable javascript and cookies to continue",
    "cf-browser-verification",
    "challenge-running",
    "cf_clearance",
    "checking if the site connection is secure",
    "vérification de sécurité en cours",
    "ray id:",
    "<title>just a moment...</title>",
    # Imperva / Incapsula
    "incapsula incident id",
    "_incapsula_resource",
    "powered by incapsula",
    "unsuccessful. incapsula",
    "/_incapsula_resource",
    "request unsuccessful. incapsula",
    "incapsula_resource",
]

# Extensions de fichiers considérées comme des rapports ou des IoCs à télécharger
FILE_DOWNLOAD_EXTENSIONS = {".pdf", ".csv", ".txt", ".xlsx", ".zip", ".yar", ".yara"}

# Regex pour détecter les intentions de téléchargement dans le texte d'un lien
FILE_DOWNLOAD_REGEX = r"(?i)(read.*report|download.*report|full.*report|report here|iocs?|indicators of compromise)"

CURL_PROFILES = ["chrome110", "chrome120", "chrome124", "safari15_3"]