# Tasks: Issue 1597 — Add 1.3 to 1.4 Version Migration Guide

## Phase 1: Prep
- [ ] Verify all candidate spec link paths resolve in the 1.4 tree
- [ ] Confirm working branch (worktree already on `claude/romantic-snyder-44cb5d`; no new branch needed)

## Phase 2: Authoring
- [ ] Generalize the "Document Structure" intro to cover multiple migrations
- [ ] Write Overview (classification table)
- [ ] Write What's Unchanged
- [ ] Write What's New in FOCUS 1.4
- [ ] Write What Requires Migration
- [ ] Write Practitioner topics (Provider/Publisher pointer, ContractApplied, awareness note)
- [ ] Write Data Generator guidance (attribute remap, new datasets, sequence/phasing)
- [ ] Write Affected Supported Features
- [ ] Write Additional Resources

## Phase 3: Verify
- [ ] Self-review against editorial guardrails (lists, IDs, no em/en dashes, link-once)
- [ ] Verify every link path resolves
- [ ] Run enhanced_markdown_lint on the file

## Phase 4: Ship
- [ ] Migrate useful research to supporting_content (if any)
- [ ] Commit + push
- [ ] Create draft PR vs `working_draft` using the PR template
- [ ] Add cleanup reminder comment referencing the .ai/work folder
