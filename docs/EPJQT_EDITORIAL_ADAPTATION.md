# EPJ Quantum Technology editorial adaptation (frozen 2026-09-04)

This record documents the adaptation of the v1.1.6 manuscript ("Sharp
Target-Domain Certificates for Quantum-Kernel Advantage under Distribution
Shift") from the npj Quantum Information format to the *EPJ Quantum Technology*
Research-article format. The adaptation is editorial and bibliographic only.

## Scientific content is unchanged

Verified by an automated comparison of the working tree against the frozen
v1.1.6 sources (`manuscript/sn-article.tex`, `manuscript/supplementary.tex`):

- All `tabular` blocks of the main article (3), all theorem environments (3),
  all display equations (27), all `\includegraphics` figure files (7), and the
  abstract are byte-identical.
- No numeric token was removed from either source. The only numeric tokens
  added belong to the software-availability block, the "Additional file 1" and
  "Figure 1" cross-references, and the generative-AI statement.
- No file under `results/`, `data/`, `src/`, `tests/`, or any configuration,
  environment, or frozen specification was modified. Frozen specification
  hashes checked by the validators are unchanged.

## Terminology-only change in the Supplementary Information

In the cross-protocol sensitivity table (rows S2 and S4 of the specification
curve), the selection label **"Legacy ID" was renamed "ID-test"**, and the
caption now defines it: selection on the in-distribution test split of the
earlier fixed-$C$ runs, which had no disjoint validation half. This is a
terminology change only. The row values ($+0.0475$, $+0.0418$, $+0.0014$,
$+0.0122$), the row order, the definitions of the other columns, and every
other table are unchanged. The corresponding machine-readable outputs under
`results/` are untouched.

Other reader-facing relabelling of internal version names ("within-v4",
"legacy generation", "historical", "evaluation bundle") to "controlled
protocol", "earlier fixed-C protocol", "cross-protocol", and "evaluation-choice
factorial" is likewise terminology only. File names, hash salts, and result
paths keep their original identifiers.

## Editorial changes

1. Reference style option `sn-nature` replaced by the numbered
   `sn-vancouver-num` style of the same Springer Nature template (class file
   version 3.1, December 2024, unchanged). `manuscript/sn-vancouver-num.bst` is
   the template copy with one marked local edit (a space instead of a colon
   after `@misc` authors). Eight arXiv entries were normalised to
   `@article{... journal={arXiv}}` and two corporate authors were spelled out.
2. Contributions and headline results moved to pages 2--3; literature
   differentiation moved into the subsection "Relation to prior work".
3. Five references added (arXiv:2608.18155, 2608.29422, 2607.18088,
   2605.22275, 2609.02781), each described with wording checked against the
   primary abstract. Figure 1 is now cited in the text.
4. Declarations restructured to the SpringerOpen order, including the software
   block required under "Availability of data and materials", and the
   Supplementary Information declared as Additional file 1.
5. Generative-AI statement in Methods records the tools used beyond
   copy-editing (OpenAI Codex; Claude Code running the Claude Fable 5.1 model)
   with explicit human verification and no AI authorship.
6. CI gates `validate_manuscript_v8.py` and `validate_manuscript_v11.py`
   updated to the EPJ QT format and to the renamed Results subsection.

The cover letter and the private submission notes are intentionally kept out
of the repository, following the existing ignore rules. No release tag and no
Zenodo version were created for this editorial adaptation; the submission
package is identified by the commit that contains this file.
