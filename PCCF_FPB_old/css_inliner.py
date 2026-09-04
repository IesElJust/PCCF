from bs4 import BeautifulSoup
import re
import sys

# 📥 Gestionar arguments des de la línia de comandes
if len(sys.argv) != 4:
    print("Ús: python css_inliner.py <input_html> <css_file> <output_html>")
    sys.exit(1)

input_html = sys.argv[1]
css_file = sys.argv[2]
output_html = sys.argv[3]

# 📖 Llegir l'HTML
with open(input_html, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# 🎨 Llegir el fitxer CSS
with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

# 🧠 Convertir el CSS en un diccionari de seleccions i estils
css_rules = {}
for rule in re.findall(r'([^{]+)\s*\{([^}]+)\}', css):
    selector, properties = rule
    selector = selector.strip()
    properties = properties.strip()

    # Ignorar pseudo-selectors i media queries
    if ":" in selector or "@" in selector:
        continue

    css_rules[selector] = properties

# 🛠️ Funció per aplicar estils inline
def apply_inline_styles(element, selector):
    if selector in css_rules:
        existing_style = element.get("style", "")
        new_style = css_rules[selector]
        element["style"] = f"{existing_style} {new_style}".strip()

# 🧩 Aplicar estils a taules, files i columnes
for table in soup.find_all("table"):
    apply_inline_styles(table, "table")

for th in soup.find_all("th"):
    for css_class in th.get("class", []):
        apply_inline_styles(th, f".{css_class}")

for td in soup.find_all("td"):
    for css_class in td.get("class", []):
        apply_inline_styles(td, f".{css_class}")

# 🏷️ Assignar classe genèrica "styled-table" a totes les taules
for table in soup.find_all("table"):
    existing_classes = table.get("class", [])
    if "styled-table" not in existing_classes:
        existing_classes.append("styled-table")
    table["class"] = existing_classes

# 💾 Guardar l'HTML amb estils inline
with open(output_html, "w", encoding="utf-8") as f:
    f.write(str(soup))

print(f"✅ CSS inline aplicat correctament a {output_html}")
