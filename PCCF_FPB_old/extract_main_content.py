import sys
import os
from bs4 import BeautifulSoup

EMOJI_DIR = "pdf_images"

FALLBACKS = {
    "📎": "[clip]",
    "📝": "[nota]",
    "📋": "[llista]",
    "💡": "[idea]",
    "📊": "[gràfic]",
    "📂": "[carpeta]",
    "🗓️": "[calendari]",
}

def emoji_to_filename(emoji: str) -> str:
    """Converteix un emoji (pot ser compost) en un nom de fitxer .png"""
    return "_".join(f"{ord(ch):x}" for ch in emoji) + ".png"

def replace_emojis(soup):
    os.makedirs(EMOJI_DIR, exist_ok=True)

    for txt in soup.find_all(string=True):
        new_text = str(txt)
        for emoji, fallback in FALLBACKS.items():
            if emoji in new_text:
                png_file = emoji_to_filename(emoji)
                png_path = os.path.join(EMOJI_DIR, png_file)

                if os.path.exists(png_path):
                    img_tag = soup.new_tag("img", src=f"{EMOJI_DIR}/{png_file}", width="20")
                    new_text = new_text.replace(emoji, str(img_tag))
                else:
                    new_text = new_text.replace(emoji, fallback)

        if new_text != str(txt):
            txt.replace_with(BeautifulSoup(new_text, "html.parser"))

def extract_main_content(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Eliminar elements que no volem
    for tag in soup(["nav", "aside", "header", "footer"]):
        tag.decompose()

    main_content = soup.select_one("div.md-content article")

    if main_content:
        # Eliminar atributs id dels encapçalaments
        for header in main_content.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
            header.attrs.pop("id", None)

        # 🔧 Afegim classe a les taules perquè el filtre les detecte
        for table in main_content.find_all("table"):
            table["class"] = table.get("class", []) + ["keep-html"]

        # Substituir emojis
        replace_emojis(main_content)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(str(main_content))


if __name__ == "__main__":
    input_html = sys.argv[1]
    output_html = sys.argv[2]
    extract_main_content(input_html, output_html)
