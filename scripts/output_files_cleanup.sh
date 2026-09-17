#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$SCRIPT_DIR/../db_outputs/output_files"

cd "$TARGET_DIR" || exit 1

# Parcourir tous les sous-dossiers
for src_folder in */; do
    # Nettoyer le nom (enlever le / de fin)
    clean_name="${src_folder%/}"
    
    # IGNORER les dossiers de catégories pour ne traiter que les vraies sources
    if [[ "$clean_name" =~ ^(iocs|pdf|yara_rules|zip|misc)$ ]]; then
        continue
    fi

    if [ -d "$src_folder" ]; then
        echo "[*] Structuration de la source : $clean_name"
        
        # Création des sous-dossiers de catégories à l'intérieur de CETTE source
        mkdir -p "${src_folder}iocs"
        mkdir -p "${src_folder}pdf"
        mkdir -p "${src_folder}yara_rules"
        mkdir -p "${src_folder}zip"
        mkdir -p "${src_folder}misc"

        # Déplacement des fichiers (uniquement à la racine du dossier source, sans descendre plus bas)
        find "$src_folder" -maxdepth 1 -type f \( -name "*.csv" -o -name "*.tsv" -o -name "*.txt" \) -exec mv {} "${src_folder}iocs/" \; 2>/dev/null
        find "$src_folder" -maxdepth 1 -type f -name "*.pdf" -exec mv {} "${src_folder}pdf/" \; 2>/dev/null
        find "$src_folder" -maxdepth 1 -type f \( -name "*.yar" -o -name "*.yara" \) -exec mv {} "${src_folder}yara_rules/" \; 2>/dev/null
        find "$src_folder" -maxdepth 1 -type f -name "*.zip" -exec mv {} "${src_folder}zip/" \; 2>/dev/null
        
        # Tout le reste va dans misc
        find "$src_folder" -maxdepth 1 -type f -exec mv {} "${src_folder}misc/" \; 2>/dev/null

        # Nettoyage : suppression des sous-dossiers de catégories s'ils sont restés vides
        for sub_dir in iocs pdf yara_rules zip misc; do
            target_sub="${src_folder}${sub_dir}"
            if [ -d "$target_sub" ] && [ -z "$(ls -A "$target_sub")" ]; then
                rmdir "$target_sub"
            fi
        done
    fi
done

echo "Fichiers triés et structurés par source avec succès !"