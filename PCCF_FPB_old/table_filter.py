#!/usr/bin/env python3
import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Table):
        # Comptem columnes
        ncols = len(elem.rows[0].cells) if elem.rows else 1
        colspec = "|".join("Y" for _ in range(ncols))

        latex = [
            "\\rowcolors{2}{gray!10}{white}",
            "\\resizebox{\\textwidth}{!}{%",
            "\\begin{tabularx}{\\textwidth}{%s}" % colspec,
            "\\toprule"
        ]

        # Capçalera
        for row in elem.head.content:
            latex.append(" & ".join(pf.stringify(c) for c in row.content) + " \\\\ \\midrule")

        # Cos
        for body in elem.content:
            for row in body.content:
                latex.append(" & ".join(pf.stringify(c) for c in row.content) + " \\\\ \\hline")

        latex.append("\\end{tabularx}")
        latex.append("}")  # tanca resizebox

        return pf.RawBlock("\n".join(latex), format="latex")

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == "__main__":
    main()
