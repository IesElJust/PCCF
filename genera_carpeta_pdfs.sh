#!/bin/bash

# Directori d'origen
source_dir="Programacions"
source_hardcoded_dir="pdfs_extra"

# Directori de destinació
destination_dir="PDFs"

# Crear la carpeta PDFs si no existeix
mkdir -p "$destination_dir"

# Buscar i copiar tots els fitxers .pdf mantenint l'estructura de directoris
find "$source_dir" -type f -name "*.pdf" -exec cp --parents {} "$destination_dir" \;

# Afegim les programacions extra
cp -r "$source_hardcoded_dir" "$destination_dir"

echo "Els PDFs s'han copiat correctament a $destination_dir."
