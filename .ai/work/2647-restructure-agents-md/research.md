# Research: Restructure the growing AGENTS.md (#2647)

## Issue Requirements (from GitHub issue #2647)

* `AGENTS.md` becomes a concise, model-independent entry point.
* Process-specific instructions move into clearly named files under `.agents/`.
* `AGENTS.md` directs agents to the appropriate instruction file based on the requested activity.
* No unnecessary duplication across AI-model-specific entry files.
* Compatibility with the existing `CLAUDE.md` symbolic link is preserved.
* Work is based on the branch associated with PR #2514 (`updates-agents`).

## Findings

* On `updates-agents`, `AGENTS.md` is 239 lines covering seven distinct concerns: project overview, build commands, architecture, content authoring rules, review conduct, issue/PR templates, and context-file conventions.
* All four model-specific entry files are already symbolic links to `AGENTS.md`:
  * `CLAUDE.md` → `AGENTS.md`
  * `.cursorrules` → `AGENTS.md`
  * `.gemini/styleguide.md` → `../AGENTS.md`
  * `.github/copilot-instructions.md` → `../AGENTS.md`
  Restructuring `AGENTS.md` therefore flows to every model automatically; no per-model duplication exists to remove, and the symlinks require no changes.
* CI workflows do not lint repository-root markdown; the enhanced linter is scoped to `specification/` builds.
* The "Writing Specification Content & Review Guidelines" section serves two activities (authoring and reviewing) but its content rules are shared. Splitting the shared rules into both files would violate the repository's own Requirement Ownership (DRY) rule, so content rules stay in one file and the review file references them.
