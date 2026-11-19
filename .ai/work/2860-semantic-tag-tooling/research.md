# Research: FR #2779 Semantic Markup (Incremental Rollout)

## Context

* Issue: #2779. Demo PR: #2819 (draft, branch `2779-semantic-markup-demo`, targets `working_draft_interim`).
* The demo converts the whole specification in one change (8,504 tags in 334 files). This branch keeps the demo as a demonstration and delivers the same capability incrementally.
* 1.6 work targets `working_draft_interim` during the 1.5 IPR Review (2026-11-02 to 2026-12-03).
* Semantic tags are for FOCUS 1.6 and later. They have no impact on 1.5 or earlier releases, so the 1.6 release contents can be chosen without regard to what earlier releases ship.

## Goal

A foundation change that adds the tooling for resolving semantic tags into the published specification, checks on tags, and maintenance tools, while staying backwards compatible: a specification with no tags builds a `spec.md` byte-identical to the base branch. Content is then tagged incrementally.

## Decisions

* **Tag syntax and kinds are the demo's, unchanged:** `col`, `val`, `ds`, `attr`, `omc`, `obj`, `schema`, `meta`, `term`. Files converted on the demo branch can be carried over as they are.
* **Per-file conversion status in front matter**, keyed by exactly the tag kind strings, with the value saying how far the kind has gone:

  ```yaml
  semantic:
    col: mechanical
    term: reviewed
  ```

* **`mechanical`:** the approved conversion rules converted the kind. CI fails when rerunning the converter for that kind would change the file.
* **`reviewed`:** a person also decided every open item, and the kind's completeness checks (e.g., FOCUS004, untagged ColumnId) are errors in that file. A file can't list a kind as `reviewed` while that check has findings.
* **Checks on tags that are present** (resolution, case, quoting, emphasis, headings, redundant qualifiers) run on every tag in every file.
* **The flag is temporary.** When every file lists a kind as `reviewed`, its completeness check becomes global. When all kinds are global, the `semantic:` key is removed. Because the flag is short-lived, no guard against heading anchors that equal a tag kind is added (the `# Schema` heading's `#schema` anchor is known and unlinked).
* **Mechanical first.** The conversion merges before the semantic review, because it is deterministic. The Working Group approves each conversion rule once instead of reviewing each line. Translations (entity links, italic glossary terms, plain entity IDs) and inferences (plain Display Names, quoted values, file dataset) are separate Action Items, so inferences can be approved rule by rule. The whole repository may be converted in one mechanical PR. The draft AIs are in `action-items/`.

## Demo Tooling to Bring Over

From `supporting_content/semantic_markup_prototype/` on the demo branch:

* `focus_semantic.py`, `build_registry.py`, `resolve_semantic.py`, `test_resolve_semantic.py`: core, moves to a permanent location.
* `tag_sources.py`, `convert_all.sh`, `semantic_review.py`: maintenance tools for converting files.
* `compare_rendered.sh`, `classify_rendered.py`: rendered-difference review.
* Build changes: `specification/Makefile`, `specification/markdownlnt.cfg` (front-matter extension), `vendored/MarkdownPP/Modules/Include.py` (file markers, front matter stripping).
* Not brought over: DEMO.md, CONVERSION.md, SEMANTIC_REVIEW.md, slides.html, samples, preview files.

## Known Dependencies

* `rm_extraction.yml` reads the Markdown source and is not tag-aware; it must be updated before any content is tagged.
* #2787 (file and folder renames) affects REG016 findings and converted file paths.
* REG016 (40 snake_case names) and REG017 (Requirements Model differences) would fail the build today; they start as warnings, and REG017 becomes a release check.
