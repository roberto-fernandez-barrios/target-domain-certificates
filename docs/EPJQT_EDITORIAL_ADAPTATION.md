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
7. Bibliography closed against the September 2026 literature (same day,
   after an adversarial bibliographic audit found no novelty blocker): three
   references added with one sentence each, worded from the primary
   abstracts (Dervovic and Cashmore, AISTATS 2025, PMLR 258:1909--1917;
   Islam, arXiv:2608.15617; Ulichney and Coston, arXiv:2606.14506), and two
   metadata updates (Bazinet et al. to its UAI 2026 version of record, PMLR
   337:491--520; DOI added to Thanasilp et al., Nature Communications 2024).
   No numeric token, table, theorem, equation, or figure changed.

The cover letter and the private submission notes are intentionally kept out
of the repository, following the existing ignore rules. No release tag and no
Zenodo version were created for this editorial adaptation; the submission
package is identified by the commit that contains this file.

## Pre-submission technical QA patch (2026-09-06)

A closed technical patch followed an adversarial pre-submission audit of the
package at commit 4966bbe. Automated comparison against that commit shows all
`tabular` blocks, theorem environments, display equations, `\includegraphics`
files, the abstract, the bibliography key set, and the cited keys unchanged.
The only numeric change is item 1.

1. Transcription fix. The Introduction and Results gave the SVC zero-label
   upper-endpoint range as 0.002--0.050; Table 1, Supplementary Table 4, and
   `results/v9/partial_identification/analysis/frontier_summary.csv` give 0.054
   for EMBER m2 SVC (tier 115; 0.050 is EMBER m1). Both sentences now read
   0.002--0.054. The GPC range and the overall range in the abstract were
   already correct.
2. Title page. `\orcidtext` no longer prints a literal "[ORCID]" superscript
   (the iDs stay in the source for the submission form); "24.," in the street
   address became "24,".
3. Cross-references and terminology. "Supplementary Figure 5 and Table 11" now
   reads "... and Supplementary Table 11"; twelve bare "Table N" / "Figure N"
   references inside the Supplementary Information now read "Supplementary
   Table N" / "Supplementary Figure N"; "GP" was unified to "GPC" (five
   sentences, four rows of Supplementary Table 12); "ToN-IoT scanning under
   GPC" now names the row cited, "the ToN-IoT constructed shift under GPC";
   abbreviations are expanded at first use (SVC, GPC, ID, OOD, PSD, RBF, QML,
   ATC, MILP, LODO, NIDS, BCa) and "KRR construction" reads "kernel-ridge
   construction".
4. Internal version labels. "v5 train-only semantic encoding" -> "frozen
   train-only semantic encoding"; "v0.9 extension" -> "finite-shot certificate
   extension"; Supplementary "v0.9 retrospective artifacts" -> "retrospective
   certificate artifacts" and "v1.0 prospective inputs" -> "prospective
   replication inputs". Hash salts, script names, file names, and `results/v*`
   paths are unchanged. The Figure 5 panel c title "Within-v4 factorial" became
   "Evaluation-choice factorial" (`scripts/reporting/make_v8_figures.py`); the
   figure was regenerated from the same frozen inputs with Matplotlib 3.11.0
   and differs from v1.1.6 only in that title string.
5. Bibliography rendering. Two marked local guards in `sn-vancouver-num.bst`
   suppress the stray ". ." (empty `pages` in `@inproceedings`) and ";." (empty
   volume, number, and pages in `@article`) that appeared in references 19, 42,
   54, and 64; a stray comma was removed from the UNSW-NB15 title (reference
   56); the UCI entry carries the same "Accessed 2 August 2026" note as the
   other web references. The set and order of references are unchanged.
6. Verification. Main (63 pages) and Supplementary Information (16 pages)
   compile with 0 undefined references, 0 multiply-defined labels, and
   0 overfull boxes; gates v8--v11 and the 120-test suite pass.
