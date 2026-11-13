# [AI] Add semantic tag tooling to the specification build

## Action Item Details

**Parent Issue:** #2779

**Detailed Description**

FR #2779 proposes semantic tags, such as `[BilledCost](#col)` and `[charges](#term)`, that name the entity a reference means. The build resolves each tag to today's link and italics conventions and checks it. The demo branch `2779-semantic-markup-demo` (draft PR #2819) built and tested the tooling, then converted the whole specification in one change. This AI brings only the tooling into the build, with no change to specification content, so the content can be converted in separate steps that are each reviewable (the AIs that follow).

The change is backwards compatible. With no tags in the source, the build output is byte-identical to the base branch, and every existing link and convention keeps working. Tags and hand-written links can coexist in the same file.

It brings over, from `supporting_content/semantic_markup_prototype/` on the demo branch:

* **The entity registry** (`build_registry.py`). It reads every entity from the file that defines it (column files, `glossary.md`, attributes, operating model conditions, datasets, JSON objects and schemas, metadata) and checks each definition's structure (REG001 to REG017).
* **The resolver** (`resolve_semantic.py`, `focus_semantic.py`). It turns tags into ordinary Markdown links and italics and checks every tag (FOCUS001 to FOCUS019). The tests come with it (`test_resolve_semantic.py`).
* **Build changes.** A Makefile step builds the registry and resolves the tags. The linter configuration accepts front matter. markdown-pp's Include module marks where each included file begins and ends, and strips front matter (`vendored/MarkdownPP/Modules/Include.py`).
* **Tools for the conversion AIs.** The converter (`tag_sources.py`, `convert_all.sh`) takes a list of paths and a list of kinds. The rendered comparison (`compare_rendered.sh`, `classify_rendered.py`) lists every difference in the published specification against a base commit, sorted by kind.

**Conversion status per file.** Each converted file records, for each tag kind, how far its conversion has gone. The keys are the tag kinds exactly as tags write them:

```yaml
semantic:
  col: mechanical
  term: mechanical
```

* `mechanical`: the approved conversion rules have converted this kind in this file. CI fails when rerunning the converter for this kind would change the file. A reference added later in the old style is therefore reported, along with the tag that would replace it.
* `reviewed`: a person has also decided every item the converter left open, so the completeness checks for this kind become errors in this file (for example FOCUS004, an untagged ColumnId). A file can't list a kind as `reviewed` while that kind's completeness check has findings in it.
* The checks on tags that are present (resolution, case, quoting, emphasis, headings, redundant qualifiers) run on every tag in every file, whatever the file lists.
* The key is temporary. Once every file lists a kind as `reviewed`, that kind's completeness checks apply everywhere. Once that is true for every kind, the key is removed. From then on, the build, which CI runs on every push, reports any untagged reference in the pull request that adds it.

**The Requirements Model extraction.** The existing `rm_extraction.yml` workflow (added in #2669) builds the FOCUS Requirements Model from the specification's Markdown on every pull request that changes `specification/`, and compares it with the published model. On draft PR #2819, which tags the whole specification and adds front matter to 334 files, its extract step passed, and the 181 entities it shares with the 1.5 model were unchanged. The workflow needs no change for tags.

Decisions for this AI:

* **Where the tools live.** Proposed: `specification/tools/semantic/`.
* **Where tags are resolved.** The demo resolves tags from Markdown to Markdown before Pandoc. `spec.md`, which `working_draft.yml` releases as the latest draft, keeps today's conventions, and every downstream step stays unchanged. The alternative is a panflute filter in the Pandoc step, next to `pandoc-project-relative-links.py`. With a filter, the checks run as a separate lint step, `spec.md` contains tags, and the compatibility comparison moves to `spec.html`. Which Markdown the 1.6 release ships is a separate decision for the Working Group.
* **Severity of the definition checks that have findings today.** REG016 reports 41 entity files and folders not named after their entity ID, which PR #2787 renames. REG017 reports 28 differences between the registry and the Requirements Model. Proposed: both start as warnings, and REG017 also runs as a check before each Requirements Model release.

Semantic tags apply to FOCUS 1.6 and later and don't affect 1.5 or earlier releases.

**Definition of Done**

* [ ] The tooling and its tests are in the decided location, and the tests run locally with pytest. Running them in CI is proposed separately, in #2867.
* [ ] With no tags in the source, the published build output is byte-identical to the base branch (`spec.md` and `spec.html` when tags are resolved before Pandoc, or `spec.html` when a Pandoc filter resolves them), and the PR shows the comparison.
* [ ] A file converted on the demo branch, copied into a scratch build, resolves to the same links and italics as on the demo branch. The file is not committed.
* [ ] `semantic:` is validated. The build reports an error for an unknown kind or status, for a `reviewed` kind whose completeness check has findings, and for a `mechanical` kind where rerunning the converter would change the file.
* [ ] `rm_extraction.yml` passes with no change to the workflow.
* [ ] The Editorial Guidelines and `AGENTS.md` describe the tag syntax and the `semantic:` key, and state that the existing conventions remain valid for untagged text.
* [ ] The three decisions above are recorded on this issue.
* [ ] The PR is merged into `working_draft_interim` (or into `working_draft` after the 1.5 IPR Review ends on 2026-12-03).
