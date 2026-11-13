# Plan: FR #2779 Semantic Markup Foundation

## Principle

With no tags in the source, the build produces a `spec.md` byte-identical to `working_draft_interim`. Every tag-dependent completeness check is scoped to the kinds a file lists as `reviewed` in `semantic:`.

## Steps

1. **Move the core tooling** from the demo's `supporting_content/semantic_markup_prototype/` to a permanent location (proposed: `specification/tools/semantic/`), with its tests.
2. **Build integration:** Makefile step (registry, markdown-pp to `spec.semantic.md`, resolver to `spec.md`), linter front-matter setting, markdown-pp `Include.py` file markers and front matter stripping.
3. **`semantic:` front matter:** parse the mapping of kind to `mechanical` or `reviewed`, and report an unknown kind or status as an error.
4. **Self-verification:** a `mechanical` kind fails when rerunning the converter would change the file. A `reviewed` kind gates its completeness checks and fails while they have findings.
5. **Severity:** definition checks REG001-REG016 start as warnings where they have findings today. REG017 moves to a release check target.
6. **Maintenance tools:** `tag_sources.py` and `convert_all.sh` take paths and a `--kinds` filter, and write `<kind>: mechanical` for the kinds they convert. Each conversion rule gets its own switch (AI 2). `compare_rendered.sh` reports rendered differences against the base.
7. **Source readers:** make `rm_extraction.yml` (and any other reader of the Markdown source) strip tags to plain text.
8. **Documentation:** Editorial Guidelines section on tags and the `semantic:` list; AGENTS.md update. Existing link conventions stay valid.
9. **Verify:** untagged build byte-identical to base; carry one demo-converted file over and confirm it builds and that its listed kinds pass.

## Rollout

Four Action Items, one PR each, drafted in `action-items/`: 1. tooling (steps above), 2. conversion and rendering rules, 3. translations, 4. inferences. Semantic review AIs follow later.

## Open

* Scope of the translations PR (kinds and files) for the Working Group; proposed: everything in one PR.
* Whether to add the `preserve` mode (resolve tags without changing link placement).
* Final location of the tooling.
* Release bundle (team discussion): which Markdown the 1.6 release includes for agents; the tagged Markdown plus the registry JSON is the candidate. Semantic tags have no impact on 1.5 or earlier, so their releases keep what they ship.
* Where tags are resolved: Markdown to Markdown before Pandoc (demo), or a panflute filter in the Pandoc step, like `pandoc-project-relative-links.py`. With a filter, the checks stay a separate lint step on the tagged source, the filter reads the `<!-- focus:begin/end -->` markers for per-file scope, and the backwards-compatibility comparison moves from `spec.md` to `spec.html`.
