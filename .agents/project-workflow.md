# Project Workflow

Instructions for creating issues and pull requests, and for managing per-issue working files and persistent memory.

## Issue and Pull Request Templates

GitHub does not auto-apply templates when issues or PRs are created via API. AI agents MUST include the required template content in the body.

### Pull Requests

PR bodies MUST complete `.github/pull_request_template.md`, including the summary, "Type of Change", and "Author Checklist" (with [AI Usage Guidelines](../guidelines/contributors/ai-usage-guidelines.md) attestation).

### Issues

Issue templates are `.yml` form definitions in `.github/ISSUE_TEMPLATE/`. Use the correct title prefix and fill all fields marked required in the template.

| Type | Title Prefix | Template |
|---|---|---|
| Action Item | `[AI] ` | `action-item.yml` |
| Feature Request | `[FR] ` | `feature-request.yml` |
| Feedback | `[Feedback] ` | `feedback.yml` |
| Maintenance | `[Maintenance] ` | `maintenance.yml` |
| Work Item | `[WI]` | `work-item.yml` |

## Context Files

### Working Files

Per-issue working files are stored in `.ai/work/<issue-number>-<kebab-case-name>/`:

* `research.md` - Investigation findings and synthesized issue requirements
* `plan.md` - Implementation approach
* `tasks.md` - Execution tracking

**Naming convention**: Use `<issue-number>-<kebab-case-name>` matching your branch name (e.g., branch `1805-ai-usage-policy` → folder `.ai/work/1805-ai-usage-policy/`).

Fetch issue details from GitHub (`gh issue view`) rather than saving locally. Summarize relevant requirements into research.md.

These files are committed during active work. After the PR is approved but before merging, delete the working folder. This is a manual step - do not delete working files until final approval is received. Valuable research should be moved to `supporting_content/` before approval.

### Memory Files

Persistent learnings are stored in `.ai/memory/` and are not deleted.

## Reference Files

* `.ai/memory/` - Saved context and memory across sessions
* `specification/glossary.md` - FOCUS terminology definitions
* `guidelines/` - Development processes and conventions
