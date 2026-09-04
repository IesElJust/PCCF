#!/usr/bin/env python3
import panflute as pf
import re

def action(elem, doc):
    if isinstance(elem, pf.Str):
        text = elem.text

        # Busca seqüències de 3 o més guions baixos
        matches = list(re.finditer(r'_{3,}', text))
        if not matches:
            return None

        result = []
        last_end = 0
        for m in matches:
            # Afig text normal abans de la seqüència
            if m.start() > last_end:
                result.append(pf.Str(text[last_end:m.start()]))

            length = m.end() - m.start()
            # Amplada proporcional (cada "_" ≈ 0.15 cm)
            cm = round(length * 0.15, 2)
            latex = f"\\rule{{{cm}cm}}{{0.4pt}}"
            result.append(pf.RawInline(latex, format="latex"))

            last_end = m.end()

        # Afig text després de l’última seqüència
        if last_end < len(text):
            result.append(pf.Str(text[last_end:]))

        return result

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == "__main__":
    main()
