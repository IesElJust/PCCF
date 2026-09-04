#!/bin/bash

# 🌍 Configuració d'entorn UTF-8
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"

echo "📁 Generant la web amb MkDocs..."
mkdocs build || { echo "❌ Error en MkDocs build"; exit 1; }
echo "✅ Web generada correctament."

# 🧠 Llegir fitxers del nav:
echo "🔍 Extraient fitxers de 'nav:' en mkdocs.yml..."
files=($(grep -oP '[[:alnum:]_./-]+\.md' mkdocs.yml | sed 's@^docs/@@'))

if [ ${#files[@]} -eq 0 ]; then
    echo "⚠️ No s'han detectat pàgines en el nav."
    exit 1
fi

echo "✅ S'han detectat ${#files[@]} pàgines: ${files[*]}"

# 🧪 Processar fitxers HTML -> Markdown
for file in "${files[@]}"; do
    base="${file%.md}"
    html1="site/${base}/index.html"
    html2="site/${base}.html"
    html_file=""

    if [ -f "$html1" ]; then
        html_file="$html1"
    elif [ -f "$html2" ]; then
        html_file="$html2"
    else
        echo "⚠️ Fitxer HTML no trobat per $file"
        continue
    fi

    safe_base="$(echo "$base" | tr '/ ' '__')"
    filtered="filtered_${safe_base}.html"
    markdown="converted_${safe_base}.md"

    echo "🔧 Filtrant $html_file..."
    python3 extract_main_content.py "$html_file" "$filtered" || { echo "❌ Error en extract_main_content.py"; exit 1; }

    echo "📝 Convertint $filtered a Markdown..."
    pandoc --strip-comments --wrap=none "$filtered" -o "$markdown" || { echo "❌ Error en pandoc"; exit 1; }
done

# 💾 Guardar fitxer combinat
echo "" > combined.md

# 📎 Afegir preàmbul YAML primer
if [ -f "docs/preamble.md" ]; then
    echo "✅ Afegint preàmbul (docs/preamble.md) al principi"
    cat docs/preamble.md >> combined.md
    echo -e "\n\n" >> combined.md
fi

# ➕ Afegir la resta de fitxers convertits
for file in "${files[@]}"; do
    base="${file%.md}"
    safe_base="$(echo "$base" | tr '/ ' '__')"
    markdown="converted_${safe_base}.md"
    if [ -f "$markdown" ]; then
        cat "$markdown" >> combined.md
        echo -e "\n\n" >> combined.md
    else
        echo "⚠️ No s'ha trobat $markdown (s'omet)."
    fi
done

# Normalitzar encoding
iconv -f UTF-8 -t UTF-8 combined.md -o combined_tmp.md && mv combined_tmp.md combined.md
echo "✅ Fitxer Markdown combinat generat: combined.md"

# 📖 Detectar versió de Pandoc per bibliografia
pandoc_version=$(pandoc --version | head -n1 | awk '{print $2}')
major=$(echo $pandoc_version | cut -d. -f1)
minor=$(echo $pandoc_version | cut -d. -f2)

echo "🔎 Pandoc versió detectada: $pandoc_version"

pandoc_cmd="pandoc combined.md --template eisvogel --pdf-engine=xelatex"

if [ "$major" -ge 2 ] && [ "$minor" -ge 11 ]; then
    pandoc_cmd="$pandoc_cmd --citeproc --bibliography=bibliografia.bib"
else
    pandoc_cmd="$pandoc_cmd --filter pandoc-citeproc --bibliography=bibliografia.bib"
fi

# 🖨️ Generar PDF amb Eisvogel
echo "📚 Generant PDF amb Eisvogel..."
$pandoc_cmd -o output.pdf || { echo "❌ Error generant output.pdf"; exit 1; }

if [ -f "output.pdf" ]; then
    echo "✅ PDF generat correctament: output.pdf"
else
    echo "❌ Error: no s'ha generat el PDF"
    exit 1
fi

# 🧹 Neteja final
echo "🧽 Netejant fitxers temporals..."
rm -f filtered_*.html converted_*.md

echo "🎉 Procés complet!"
