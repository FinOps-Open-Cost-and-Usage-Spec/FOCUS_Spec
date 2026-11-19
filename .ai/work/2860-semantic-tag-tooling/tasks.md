# Tasks: AI #2860 Semantic Tag Tooling (FR #2779)

* [x] Create branch `2779-semantic-markup` from `working_draft_interim` (12770c1a)
* [x] Create branch `2860-semantic-tag-tooling` for AI #2860 (same base); working folder renamed to match
* [x] Record decisions in research.md and plan.md
* [x] Draft the Action Items (`action-items/`), with counts measured at 12770c1a
* [x] Create the AIs on GitHub under #2779: #2860, #2861, #2862, #2863
* [x] Mark #2860 as Critical Path in the project view
* [ ] Set assignees
* [ ] Reconcile the FR's Maintainer Assessment (pilot, per-area phasing) with the AIs
* [x] Move core tooling and tests to `specification/tools/semantic/` (registry lookups split into `registry.py`; the prototype Pandoc filter is not carried over)
* [x] Integrate the registry, status check, and resolver into the Makefile; linter front matter; markdown-pp Include markers
* [x] Parse and validate `semantic:` kind statuses (FOCUS020)
* [x] FOCUS004 only for `col: reviewed`; `tag_sources.py --check` (FOCUS021) for `mechanical` kinds, run by the build
* [x] REG017 skipped in the build (`--rm-release none`); `make check-requirements-model` runs it with `--fail-on REG017`
* [x] `--kinds` in tag_sources.py and convert_all.sh; path filter in convert_all.sh; `--out -` in build_registry.py
* [x] `rm_extraction.yml`: no change. The extract step passed on #2819 with 8,504 tags and front matter in 334 files; Matt's assessment found all 181 shared entities unchanged. Ask to amend the #2860 DoD item
* [x] Editorial Guidelines (Semantic Tags section) and AGENTS.md
* [x] Untagged build: spec.md and spec.html byte-identical to 12770c1a (sha 5af46a95, 1172cc1e)
* [x] Demo billedcost.md (with the demo glossary aliases) resolves identically to the demo; Billing Period pilot in scratch: 145 tags, build passes, rerun idempotent
* [x] Tests: 48 in `specification/tools/semantic/tests`, run locally with pytest; CI for them is a future AI
* [ ] User review of #2860 wording; commit and open the PR when asked
* [ ] Semantic review AIs (later): each kind needs a completeness check before its `semantic:` key can be removed; only `col` has one today (FOCUS004)
