# Plan: AI Usage Policy for FOCUS Project

**Issue:** #1805 - [FR] Define policy of AI usage in FOCUS project
**Status:** Implementation complete - Ready for review
**Branch:** `1805-ai-usage-policy`

## Context

This issue was triggered by PR #1801 being blocked because GitHub Copilot (`copilot-swe-agent`) isn't covered under EasyCLA. We need a policy for AI contributions.

Research is complete. See `research.md` for full details including industry precedents (LF, ASF, AAIF), AI agent file formats, and context file lifecycle best practices.

## Decisions (Complete)

| # | Decision | Outcome |
|---|----------|---------|
| 1 | Policy approach | Human responsibility; same review standards; align to LF |
| 2 | Document structure | FOCUS guidelines style (hierarchical H2/H3 sections) |
| 3 | Root instructions | `AGENTS.md` at root as source; symlinks for other tools |
| 4 | Slash commands | Centralized in `.ai/commands/`; provider wrappers reference them |
| 5 | Context files | Issue-named folders (matching branch); committed; delete before PR merge |
| 6 | Gitignore | Delete `.claude/.gitignore`; add patterns to root `.gitignore` |
| 7 | Attribution | No required format (follow LF); optional/informal |

## Deliverables

1. `guidelines/ai-usage-guidelines.md` - Human policy (CREATE)
2. `CONTRIBUTING.md` - Add AI section (UPDATE)
3. `AGENTS.md` - Root file, source of truth (CREATE from CLAUDE.md)
4. `.ai/commands/feature.md` - Centralized command logic (CREATE)
5. Root symlinks: CLAUDE.md, .cursorrules, .github/copilot-instructions.md (CREATE)
6. `.claude/commands/feature.md` - Wrapper referencing .ai/commands/ (UPDATE)
7. `.cursor/commands/feature.md` - Cursor wrapper (CREATE)
8. `.github/prompts/feature.md` - Copilot wrapper (CREATE)
9. Root `.gitignore` - Add local file patterns (UPDATE)
10. `.github/workflows/cleanup-context.yml` - PR health check for working folders (CREATE)

## File Structure After Implementation

```text
FOCUS_Spec/
├── AGENTS.md                    # Source of truth (at root for tool compatibility)
├── CLAUDE.md → AGENTS.md        # Symlink
├── .cursorrules → AGENTS.md     # Symlink
├── .ai/
│   ├── commands/
│   │   └── feature.md           # Centralized command logic
│   ├── memory/                  # Permanent
│   └── <branch-name>/           # Delete before PR merge
├── .claude/
│   └── commands/
│       └── feature.md           # Claude wrapper
├── .cursor/
│   └── commands/
│       └── feature.md           # Cursor wrapper
├── .github/
│   ├── copilot-instructions.md → ../AGENTS.md
│   ├── prompts/
│   │   └── feature.prompt.md    # Copilot wrapper
│   └── workflows/
│       └── cleanup-context.yml  # PR health check
└── guidelines/
    └── ai-usage-guidelines.md
```

## Key Design Decisions

### Two Modes of AI Usage

| Mode | Who does the work | Who submits | Who is responsible |
|------|-------------------|-------------|-------------------|
| Interactive | Human with AI assistance | Human | Human who submitted |
| Autonomous | AI working independently | Human who requested | Human who requested |

### Context File Naming

Context folders match branch names for consistency:

- Branch: `1805-ai-usage-policy`
- Context: `.ai/1805-ai-usage-policy/`

### Command Architecture

```text
.ai/commands/feature.md           # Centralized process logic
       ↑
.claude/commands/feature.md       # Claude wrapper (references above)
.cursor/commands/feature.md       # Cursor wrapper (references above)
.github/prompts/feature.prompt.md # Copilot wrapper (references above)
```

This allows provider-specific customization while maintaining a single source of truth for processes.
