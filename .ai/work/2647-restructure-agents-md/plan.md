# Plan: Restructure the growing AGENTS.md (#2647)

## Approach

Split `AGENTS.md` by activity, not by audience. Each `.agents/` file answers "what do I need to know to perform this activity", and `AGENTS.md` becomes a router.

## File Layout

* `AGENTS.md` - Concise entry point: project overview, activity routing table, repository map, model-specific entry point note, AI usage policy.
* `.agents/build-and-test.md` - Build commands, tests, lint, document build pipeline, dependencies.
* `.agents/writing-specification.md` - Specification structure, file organization, normative language, editorial conventions, validation & schema accuracy.
* `.agents/reviewing-changes.md` - Review conduct; references `writing-specification.md` for content rules (DRY).
* `.agents/requirements-model.md` - Requirements model layout and rule ID format; references `build-and-test.md` for commands.
* `.agents/project-workflow.md` - Issue/PR templates, working files, memory files, reference files.

## Principles

* Move content verbatim wherever possible; minimize the textual diff against `updates-agents`.
* Each piece of guidance is owned by exactly one file; cross-reference instead of duplicating.
* Preserve all symbolic links unchanged (`CLAUDE.md`, `.cursorrules`, `.gemini/styleguide.md`, `.github/copilot-instructions.md`).
* Adjust relative links in files that moved into `.agents/` (e.g., `../guidelines/...`).
