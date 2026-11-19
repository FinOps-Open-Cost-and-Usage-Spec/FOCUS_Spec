# Draft Action Items for FR #2779

Created on GitHub on 2026-11-11 as sub-issues of #2779: #2860, #2861, #2862, #2863 (type Action Item, milestone v1.6). The files are the source text; edit the issues on GitHub from here on. Each file holds one issue. Its first line is the title, and the rest is the body, following `.github/ISSUE_TEMPLATE/action-item.yml` (Detailed Description, Definition of Done) and the layout of recent AIs such as #2735 and #2528.

| Order | File | Title | Depends on | One PR |
| :--- | :--- | :--- | :--- | :--- |
| 1 (#2860) | `1-tooling.md` | [AI] Add semantic tag tooling to the specification build | None | Tooling and build only, with no content change |
| 2 (#2861) | `2-rules.md` | [AI] Decide the conversion and rendering rules for semantic tags | 1 | Rule documents, converter switches, tests |
| 3 (#2862) | `3-translations.md` | [AI] Convert existing references to semantic tags with the translation rules | 2 | The conversion in the chosen scope, or one PR per area if the team chooses areas |
| 4 (#2863) | `4-inferences.md` | [AI] Tag plain Display Names, quoted values, and file datasets with the inference rules | 3 | One commit per rule |

Later: semantic review AIs, which move kinds from `mechanical` to `reviewed`. They are created when the review starts, probably one per area.

## Before Creating

* FR #2779 still has the `needs triage` label. AIs normally follow the FR's acceptance into a release, but the triage guidelines let the PM start the Maintainer Assessment in parallel. Ask the PM whether to create these now or after triage.
* Create them in order. Each one refers back to earlier ones through the placeholders `AI #<tooling>`, `AI #<rules>`, and `AI #<translations>`. Replace those with the real numbers before creating the next one.

## After Creating

* Set the issue type to Action Item, since `gh issue create` doesn't apply the template's type.
* Add each one as a sub-issue of #2779.
* Set the milestone to v1.6.
* Mark AI 1 as `Critical Path` in the project view. When it closes, AI 2 becomes the Critical Path.
* PR titles start with `AI #<n>:`.

```bash
f=1-tooling.md
gh issue create --repo FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec \
  --title "$(head -1 "$f" | sed 's/^# //')" --body "$(tail -n +3 "$f")"
```

## How the Counts Were Measured

All counts are for `working_draft_interim` at `12770c1a`, measured on 2026-11-11 with a copy of the demo converter (`tag_sources.py` at `dd881b80`) that adds a switch for each rule. Each translation rule was run alone. Each inference rule was run alone on top of all three translations. The rendered differences come from the demo resolver and `classify_rendered.py`, compared with the base build. With every rule on, the copy reproduces the demo's mechanical commit (`37e3a214^`), apart from the sample files reviewed by hand: 8,106 tags against 8,127, and the same 450 open items and 57 inferred datasets.

The counts for each rule differ from the "Where the Tags Came From" table in the demo's `CONVERSION.md` (e.g., entity links 2,616 here against 3,149 there). That table compared converted lines with the originals and describes itself as approximate. These counts switch each rule on and off.
