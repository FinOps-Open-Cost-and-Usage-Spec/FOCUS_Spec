# Tasks: AI Usage Policy for FOCUS Project

> **Issue:** #1805 - [FR] Define policy of AI usage in FOCUS project
> **Type:** Supporting Content (governance policy)
> **Branch:** `1805-ai-usage-policy`

---

## Phase 1: Decisions ✅ COMPLETE

| # | Decision | Outcome |
|---|----------|---------|
| 1 | Policy approach | Human responsibility; same review standards; align to LF |
| 2 | Document structure | FOCUS guidelines style (hierarchical H2/H3 sections) |
| 3 | Root instructions | `AGENTS.md` at root as source; symlinks for other tools |
| 4 | Slash commands | Centralized in `.ai/commands/`; provider wrappers reference them |
| 5 | Context files | Issue-named folders (matching branch); committed; auto-delete on PR merge |
| 6 | Gitignore | Delete `.claude/.gitignore`; add patterns to root `.gitignore` |
| 7 | Attribution | No required format (follow LF); optional/informal |

---

## Phase 2: Draft Policy Document ✅ COMPLETE

### Deliverable 1: AI Usage Guidelines (CREATE)

**File:** `guidelines/ai-usage-guidelines.md`

- [x] Draft Overview section (purpose, scope, relationship to LF policy)
- [x] Draft Permitted Use section (AI tools allowed, interactive + autonomous modes)
- [x] Draft Contribution Requirements section (CLA coverage, human submitter, review process)
- [x] Draft optional Attribution section (informal, not required)
- [x] Review against LF policy for alignment

### Deliverable 2: CONTRIBUTING.md (UPDATE)

- [x] Add AI usage section referencing guidelines/ai-usage-guidelines.md
- [x] Place section after "Types of Contributions", before "Contribution Process"

---

## Phase 3: AI Agent Configuration ✅ COMPLETE

### Deliverable 3: AGENTS.md (CREATE)

**File:** `AGENTS.md` (at root)

- [x] Create AGENTS.md at root (adapted from CLAUDE.md)
- [x] Review content for agent-agnostic language
- [x] Add reference to AI usage guidelines
- [x] Add context file documentation

### Deliverable 4: Root symlinks (CREATE)

- [x] Create `CLAUDE.md` symlink → `AGENTS.md`
- [x] Create `.cursorrules` symlink → `AGENTS.md`
- [x] Create `.github/copilot-instructions.md` symlink → `../AGENTS.md`

### Deliverable 5: Centralized command (CREATE)

**File:** `.ai/commands/feature.md`

- [x] Create centralized command logic
- [x] Document context file naming pattern (match branch name)
- [x] Document working file purposes (research.md, plan.md, tasks.md)
- [x] Document cleanup guidance

### Deliverable 6: Provider command wrappers (CREATE/UPDATE)

- [x] `.claude/commands/feature.md` - Claude wrapper (minimal, references .ai/commands/)
- [x] `.cursor/commands/feature.md` - Cursor wrapper
- [x] `.github/prompts/feature.md` - Copilot wrapper

---

## Phase 4: Gitignore Updates ✅ COMPLETE

### Deliverable 7: Gitignore Files (UPDATE)

- [x] Delete `.claude/.gitignore`
- [x] Add to root `.gitignore`:
  - [x] `settings.local.json`
  - [x] `*.local.md`
- [x] Verify `.context/` files are NOT ignored

---

## Phase 5: Context Cleanup Automation ✅ COMPLETE

### Deliverable 8: GitHub Action for context cleanup

**File:** `.github/workflows/cleanup-context.yml`

- [x] Create workflow triggered on PR merge
- [x] Parse linked issues from PR title, body, and branch name
- [x] Delete matching `.context/<issue>-*/` folders
- [x] Commit and push deletion

---

## Phase 6: Working Group Review

- [ ] [manual] Present draft policy to Task Force
- [ ] [manual] Incorporate TF feedback
- [ ] [manual] Present to Members for approval
- [ ] [manual] Address any objections

---

## Phase 7: Implementation & PR

- [x] Create branch: `1805-ai-usage-policy`
- [x] Implement all deliverables
- [ ] Validate markdown linting
- [ ] Test symlinks work correctly on Windows and Unix
- [ ] Create PR, link to #1805
- [ ] [manual] Review cycle
- [ ] [manual] Merge to working draft
- [ ] Delete `.context/1805-ai-usage-policy/` after merge

---

## Notes

- This is a governance/policy issue requiring working group consensus
- The policy is non-normative (does not change the specification itself)
- AGENTS.md is the emerging LF/AAIF standard
- Context folder names match branch names for consistency
- No required attribution format (aligns with LF policy)
