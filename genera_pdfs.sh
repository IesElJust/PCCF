#!/bin/bash

# Crear el directori errors si no existeix
mkdir -p errors

# Comprovar si l'entorn virtual està actiu
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activant l'entorn virtual..."
    source venv/bin/activate
else
    echo "L'entorn virtual ja està actiu."
fi

# Recórrer tots els fitxers 'genera_pdf.py'
#for i in `find . -name genera_pdf.py | grep PMDM`; do
for i in `find . -name genera_pdf.py`; do
    dir_name=$(dirname $i)
    folder_name="${dir_name##*/}"
    output_file="${folder_name}.pdf"
    # Ruta absoluta del fitxer d'errors
    error_file="$(pwd)/errors/${folder_name}.txt"
    
    # Canviar al directori correcte abans d'executar el script
    #cd "$dir_name" || exit 1  # Si no es pot canviar de directori, aturem l'script
    
    # Executar el script amb stderr redirigit
    #python3 genera_pdf.py "$output_file" 2>"$error_file" &
    bash -c "cd $dir_name && python3 genera_pdf.py $output_file 2>$error_file"
    #echo "cd $dir_name && python3 genera_pdf.py $output_file"
    #echo  $error_file
    
    # Tornar al directori original després d'executar el script
    # cd - || exit 1
done

wait
