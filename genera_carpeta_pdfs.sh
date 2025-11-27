#!/bin/bash

# Directori d'origen
source_dir="Programacions"
source_hardcoded_dir="pdfs_extra/*"

# Directori de destinació
destination_dir="PDFs"

# Crear la carpeta PDFs si no existeix
mkdir -p "$destination_dir"


# Afegim les programacions extra
#mkdir -p "${destination_dir}/${source_dir}"
#cp -r "${source_hardcoded_dir}" "${destination_dir}/${source_dir}/"


# Buscar i copiar tots els fitxers .pdf mantenint l'estructura de directoris
find "$source_dir" -type f -name "*.pdf" -exec cp --parents {} "$destination_dir" \;

# Afegim les programacions extra
#exec cp -r "$source_hardcoded_dir" "$destination_dir/$source_dir/"

cp -r pdfs_extra/* PDFs/Programacions/

echo "Els PDFs s'han copiat correctament a $destination_dir."
