# Implement Feature Request

**Input:** $ISSUE - GitHub issue number (e.g., `1234`)

## Process

### Phase 1: Setup

1. Fetch issue: `gh issue view $ISSUE --json title,body,labels,comments`
2. Create `.ai/work/<issue>-<kebab-name>/` working directory (name matches branch)

### Phase 2: Research

1. Analyze issue requirements (re-fetch from GitHub if needed for updates)
2. Search spec: `rg "<keywords>" specification/ supporting_content/`
3. Identify change type and files needed (see File Matrix below)
4. Read 1-2 similar implementations as patterns
5. Think about conflicts, risks, gaps, dependencies, etc. this issue has with the existing specification (cascading impacts) or with issues actively being worked.
6. Synthesize findings into `research.md` (include key issue requirements)```
6. **CHECKPOINT:** Ask user to review before planning

### Phase 3: Plan

1. Read `guidelines/contributor/normative-requirements-guidelines.md`
2. Define requirements table (# | Requirement | MUST/SHOULD/MAY | Rule ID)
3. List deliverables with paths and guideline references
4. Save lightweight execution plan outline to `plan.md`
5. **CHECKPOINT:** Ask user to review before tasks

### Phase 4: Tasks

1. Create `tasks.md` with phased checkboxes
2. Mark human tasks with `[manual]`
3. **CHECKPOINT:** Ask if user wants to start execution

### Phase 5: Execute (on approval)

1. Create branch: `git checkout -b <issue>-<kebab-name>`
2. Implement deliverables, update tasks.md as you go
3. Validate: `python validate_includes.py <folder>` and `pytest tests/`
4. Commit, push, create draft PR

## Working Folder Naming

Use `<issue-number>-<kebab-case-name>` matching your branch:

- Branch: `1805-ai-usage-policy`
- Folder: `.ai/work/1805-ai-usage-policy/`

## Working File Purposes

| File | Purpose | Lifecycle |
|------|---------|-----------|
| `research.md` | Synthesized issue requirements, investigation findings, patterns | Migrate valuable parts to `supporting_content/` as part of PR; delete folder before merge |
| `plan.md` | Implementation approach and deliverables | Delete before merge |
| `tasks.md` | Execution tracking with checkboxes | Delete before merge |

Note: Fetch issue details from GitHub rather than saving locally. This ensures current content and reduces file management.

## Cleanup

**During the PR** (before final approval):

- Migrate valuable research to `supporting_content/`
- Add relevant implementation notes to PR description or linked issue

**After approval, before merge**:

- Delete only the `.ai/work/<issue-number>-<name>/` folder for this PR
- Do not delete working files until final approval is received

After creating the PR, add this comment on `research.md` to remind reviewers:

> ⚠️ **Cleanup required before merge**: After final approval, delete `.ai/work/<folder-name>/` before merging.

## File Matrix

| Type | Create | Update |
|------|--------|--------|
| **Column** | `columns/<name>.md`, `model_rules/columns/<name>.json`, `supporting_content/columns/<name>.md` | `columns.mdpp` |
| **Attribute** | `attributes/<name>.md`, `model_rules/attributes/<name>.json`, `supporting_content/attributes/<name>.md` | `attributes.mdpp`, `dataset.md`, `costandusage.json` |

## Pattern Files

Read these for structure (don't memorize - read when needed):

- **Column:** `specification/datasets/cost_and_usage/columns/billingaccountid.md`
- **Attribute:** `specification/attributes/invoice_handling.md`
- **JSON rules:** `guidelines/contributor/writing-requirements-model-guidelines.md`

## Rule ID Suffixes

`-M` = MUST/MUST NOT | `-O` = SHOULD/MAY | `-C` = Conditional ("when"/"unless" in text)
