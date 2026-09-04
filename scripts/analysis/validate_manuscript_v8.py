"""Fail-fast EPJ Quantum Technology format gates for the manuscript."""
from __future__ import annotations

import re
from pathlib import Path


MAIN = Path("manuscript/sn-article.tex")
SUPPLEMENT = Path("manuscript/supplementary.tex")
GENERATED_TABLE_ROWS = Path("manuscript/generated")


def uncommented(text: str) -> str:
    return "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("%")
    )


def tex_words(text: str) -> list[str]:
    text = re.sub(r"\\(?:texttt|emph|textbf|mathrm)\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[A-Za-z@]+(?:\[[^\]]*\])?", " ", text)
    text = text.replace("\\%", " percent ")
    text = re.sub(r"[{}$\\]", " ", text)
    return re.findall(
        r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿ0-9]+)*",
        text,
    )


def extract_one(pattern: str, text: str, label: str) -> str:
    match = re.search(pattern, text, flags=re.DOTALL)
    if not match:
        raise ValueError(f"missing {label}")
    return match.group(1).strip()


def validate_main(text: str) -> None:
    active = uncommented(text)
    documentclass = extract_one(
        r"\\documentclass\[([^\]]+)\]\{sn-jnl\}",
        active,
        "active document class",
    )
    if "sn-vancouver-num" not in documentclass:
        raise ValueError(
            "active document class must use the numbered sn-vancouver-num style"
        )
    if "referee" not in documentclass or "lineno" not in documentclass:
        raise ValueError("document class must keep double spacing and line numbers")

    title = extract_one(
        r"\\title(?:\[[^\]]*\])?\{([^{}]+)\}",
        active,
        "article title",
    )
    title_words = tex_words(title)
    pdf_title = extract_one(
        r"pdftitle=\{([^{}]+)\}",
        active,
        "PDF metadata title",
    )
    if pdf_title != title:
        raise ValueError("PDF metadata title differs from article title")

    abstract = extract_one(
        r"\\abstract\{(.*?)\}\s*\\keywords",
        active,
        "unstructured abstract",
    )
    abstract_words = tex_words(abstract)
    if len(abstract_words) > 350:
        raise ValueError(
            f"abstract has {len(abstract_words)} words, limit is 350"
        )
    if re.search(r"\\(?:cite|section|subsection)\b", abstract):
        raise ValueError("abstract contains a citation or subheading command")

    display_items = len(
        re.findall(r"\\begin\{(?:figure\*?|table\*?)\}", active)
    )

    discussion_start = active.find(r"\section{Discussion}")
    methods_start = active.find(r"\section{Methods}")
    data_start = active.find(r"\bmhead{Availability of data and materials}")
    if not (0 <= discussion_start < methods_start < data_start):
        raise ValueError("Discussion, Methods, and Declarations order is invalid")
    if r"\subsection{Use of generative AI}" not in active:
        raise ValueError("generative-AI disclosure is missing from Methods")
    for heading in (
        "Ethics approval and consent to participate",
        "Consent for publication",
        "Availability of data and materials",
        "Competing interests",
        "Funding",
        "Authors' contributions",
        "Acknowledgements",
        "Supplementary information",
    ):
        if rf"\bmhead{{{heading}}}" not in active:
            raise ValueError(f"declaration heading is missing: {heading}")
    for field in (
        "Project name:",
        "Project home page:",
        "Archived version:",
        "Operating system(s):",
        "Programming language:",
        "License:",
    ):
        if field not in active:
            raise ValueError(f"software availability field is missing: {field}")
    if "Additional file 1" not in active:
        raise ValueError("Additional file 1 is not declared")

    print(
        "[ok] EPJ QT main format: "
        f"title={len(title_words)} words, abstract={len(abstract_words)} words, "
        f"display_items={display_items}"
    )


def validate_supplement(text: str) -> None:
    active = uncommented(text)
    if re.search(r"supplementary\s+methods", active, flags=re.IGNORECASE):
        raise ValueError("Supplementary Information contains Supplementary Methods")
    if re.search(
        r"\\section\*?\{[^{}]*methods[^{}]*\}",
        active,
        flags=re.IGNORECASE,
    ):
        raise ValueError("Supplementary Information contains a Methods section")
    if r"\section*{Supplementary Results:" not in active:
        raise ValueError("Supplementary Results structure is missing")
    generated_files = sorted(GENERATED_TABLE_ROWS.glob("v8_*_rows.tex"))
    if not generated_files:
        raise ValueError("generated v0.8 table rows are missing")
    for path in generated_files:
        for row in path.read_text(encoding="utf-8").splitlines():
            if not row.strip() or row.strip() in {r"\addlinespace", r"\midrule"}:
                continue
            if row not in active:
                raise ValueError(
                    f"{path}: generated row is not represented verbatim in "
                    "Supplementary Information"
                )
    print("[ok] Supplementary Information contains results/diagnostics only")
    print(
        "[ok] Supplementary v0.8 tables match "
        f"{len(generated_files)} generated row files"
    )


def main() -> None:
    if not MAIN.is_file() or not SUPPLEMENT.is_file():
        raise FileNotFoundError("main or Supplementary LaTeX source is missing")
    validate_main(MAIN.read_text(encoding="utf-8"))
    validate_supplement(SUPPLEMENT.read_text(encoding="utf-8"))
    print("[ok] all EPJ Quantum Technology manuscript-format gates passed")


if __name__ == "__main__":
    main()
