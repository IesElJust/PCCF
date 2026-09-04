#!/usr/bin/env python3
import panflute as pf
import re

def action(elem, doc):
    if isinstance(elem, pf.Para):
        txt = pf.stringify(elem).strip()
        if txt.startswith("!!!"):
            m = re.match(r'!!!\s+(\w+)(\s+"(.*)")?', txt)
            if m:
                kind = m.group(1).lower()
                title = m.group(3) if m.group(3) else kind.capitalize()

                colors = {
                    "tip": ("blue!5", "blue!75!black"),
                    "note": ("blue!5", "blue!75!black"),
                    "warning": ("yellow!10", "yellow!80!black"),
                    "caution": ("red!5", "red!75!black"),
                }
                colback, colframe = colors.get(kind, ("blue!5", "blue!75!black"))

                latex = f"""
\\begin{{tcolorbox}}[title={{{title}}},colback={colback},colframe={colframe}]
"""
                doc.in_admonition = latex
                return []  # Eliminem la línia original

    # Si estem dins d'una admonició, capturem paràgrafs normals
    if getattr(doc, "in_admonition", None):
        if isinstance(elem, pf.Para):
            text = pf.stringify(elem)
            latex = doc.in_admonition + text + "\n\\end{tcolorbox}"
            doc.in_admonition = None
            return pf.RawBlock(latex, format="latex")

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == "__main__":
    main()
