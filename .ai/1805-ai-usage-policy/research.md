# Research: AI Usage Policy for FOCUS Project

## Summary

Issue #1805 requests a clear policy for AI usage in the FOCUS project. The immediate trigger was PR #1801 (created by GitHub Copilot) being blocked by EasyCLA because `copilot-swe-agent` is not a covered contributor.

## Current State Analysis

### 1. EasyCLA Requirements

The FOCUS project uses the Linux Foundation's EasyCLA to manage contributor authorization:
- All contributors must be covered under the FOCUS Membership Agreement
- Contributors must be authorized by their organization's CLA Manager
- The EasyCLA bot blocks PRs from unauthorized contributors
- **No explicit policy exists for AI/bot contributors**

### 2. Existing Governance Documents

| Document | AI Policy Coverage |
|----------|-------------------|
| [CONTRIBUTING.md](../../CONTRIBUTING.md) | No AI mentions |
| [development-processes.md](../../guidelines/development-processes.md) | No AI mentions |
| [github-guidelines.md](../../guidelines/github-guidelines.md) | No AI mentions |
| [ipr.md](../../ipr.md) | No AI mentions |

### 3. The EasyCLA Problem

From PR #1801, the EasyCLA bot blocked the PR with:
> "login: @Copilot / name: copilot-swe-agent[bot] . The commit is not authorized under a signed CLA."

AI tools like Copilot are not individuals who can sign CLAs, creating a gap in the current contribution model.

---

## Industry Precedents

### Linux Foundation Generative AI Policy

**Source:** [Linux Foundation Generative AI Policy](https://www.linuxfoundation.org/legal/generative-ai)

Key principles:
- **AI-generated contributions ARE permitted** to LF projects
- Contributions should follow the same peer review standards as traditional contributions
- Contributors must verify AI tool terms don't conflict with project licenses
- Third-party copyrighted materials require permission and attribution
- Individual projects may establish project-specific guidance

### Apache Software Foundation Generative Tooling Guidance

**Source:** [ASF Generative Tooling Guidance](https://www.apache.org/legal/generative-tooling.html)

Key requirements:
1. **Tool Terms Compliance**: AI tool terms must not restrict output use inconsistently with open source
2. **Content Originality/Licensing**: Output must either be non-copyrightable, contain no third-party materials, or have proper licensing for any third-party content
3. **Due Diligence**: Contributors should obtain "reasonable certainty" about the above

**Attribution**: Recommended practice is to use `Generated-by:` token in commit messages for machine-parsable provenance tracking.

**CLA Implications**: The Apache ICLA requires disclosure of any copyrighted materials that are not the contributor's original creation - this applies equally to AI-generated work.

### OpenSSF AI/ML Security Working Group

**Source:** [OpenSSF Best Practices](https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions)

OpenSSF has established:
- AI/ML Security Working Group exploring risks with AI tools
- Security-focused guidance for AI code assistant usage
- Recommendation that AI-generated contributions follow the same third-party licensing requirements

### EasyCLA Bot Handling

**Source:** [EasyCLA Project](https://github.com/linuxfoundation/easycla)

- EasyCLA has added support for "skipping CLA checks for configured bots"
- Recent updates address "GitHub bots (like Copilot) having no login but only email"
- Microsoft CLA system allows pre-approved bots via an `approvedBots.csv` file
- CLA assistant tool allows bot users (Dependabot, etc.) to be approved in dashboard

---

## Key Questions to Address

1. **Contribution Authorization**: Should AI tools be allowed to author commits? If so, under whose CLA?
2. **Human Oversight**: What level of human review is required for AI-generated content?
3. **Attribution**: How should AI contributions be attributed in commits?
4. **IP/Legal**: Are there IP concerns with AI-generated contributions to an open specification?
5. **Quality Control**: What review standards apply to AI-generated content?

---

## Policy Approach Options

### Option A: Human-Authored Only (Conservative)
- All commits must be authored by a CLA-covered human contributor
- AI tools can assist but cannot be the commit author
- Simplest approach, no CLA changes needed
- **Precedent**: Some organizations follow this implicitly

### Option B: AI as Co-Author (Moderate - Recommended)
- AI contributions allowed when sponsored by a CLA-covered human
- Human takes responsibility for the content (aligns with LF and ASF policies)
- Requires commit message conventions (e.g., `Generated-by:` or `Co-Authored-By:`)
- **Precedent**: Linux Foundation, Apache Software Foundation

### Option C: Register AI Tools as Approved Bots (Technical)
- Work with Linux Foundation to configure EasyCLA to skip checks for specific bots
- Requires EasyCLA configuration changes
- **Precedent**: Microsoft CLA system, CLA assistant

### Option D: Combined Approach (Comprehensive)
- Option B (human sponsorship + attribution) as the content policy
- Option C (EasyCLA configuration) as the technical enablement
- Best of both worlds: clear governance + practical implementation

---

## Recommended Policy Elements

Based on industry precedents, a FOCUS AI Usage Policy should include:

### 1. Permitted Use
- AI tools MAY be used to assist in creating contributions
- AI-generated content IS permitted following standard review processes

### 2. Human Responsibility
- A CLA-covered contributor MUST take responsibility for AI-generated content
- The sponsoring human is accountable for:
  - Reviewing AI output for correctness
  - Ensuring no third-party IP conflicts
  - Ensuring compliance with FOCUS normative requirements

### 3. Attribution Requirements
Following ASF precedent:
- Contributions containing AI-generated content SHOULD include attribution
- Recommended format: `Generated-by: <tool-name>` in commit message
- Alternative: `Co-Authored-By: <AI Tool>` (GitHub convention)

### 4. Quality Standards
- AI-generated content MUST meet the same quality standards as human-authored content
- All normative changes require Task Force and Member review per existing processes
- AI-generated content does not bypass any approval workflow

### 5. Prohibited Uses
- AI tools MUST NOT be used to bypass CLA requirements
- AI-generated content MUST NOT introduce third-party copyrighted material without proper licensing

---

## Technical Implementation

### EasyCLA Options

1. **Whitelist AI Bots**: Configure EasyCLA to skip checks for specific bots (e.g., `copilot-swe-agent`)
   - Requires Linux Foundation coordination

2. **Human Commits Only**: Require all commits be made by human accounts
   - AI tools can draft PRs, but human must create the actual commit

### Recommended Approach

Require human-authored commits with AI attribution in commit messages. This:
- Maintains CLA integrity
- Provides clear provenance tracking
- Aligns with Linux Foundation and ASF precedents
- Requires no EasyCLA configuration changes

---

## Deliverable Type

This issue requests **Supporting Content** - specifically a governance policy document.

Recommended deliverables:
1. **New file**: `guidelines/ai-usage-guidelines.md` - The core policy document
2. **Update**: `CONTRIBUTING.md` - Add reference to AI policy section
3. **Update**: `development-processes.md` - Add AI attribution guidance

---

## Sources

- [Linux Foundation Generative AI Policy](https://www.linuxfoundation.org/legal/generative-ai)
- [ASF Generative Tooling Guidance](https://www.apache.org/legal/generative-tooling.html)
- [OpenSSF AI Code Assistant Guide](https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions)
- [EasyCLA GitHub](https://github.com/linuxfoundation/easycla)
- [CLAs and DCOs - FINOS](https://osr.finos.org/docs/bok/artifacts/clas-and-dcos)
- [Agentic AI Foundation (AAIF) Announcement](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)

---

## AI Agent Instruction Files

### The Multi-Agent Problem

Different AI coding agents use different instruction file formats:

| Agent | Primary File | Location | Format |
|-------|-------------|----------|--------|
| Claude Code | `CLAUDE.md` | Root | Markdown |
| GitHub Copilot | `copilot-instructions.md` | `.github/` | Markdown |
| Cursor | `.cursorrules` or `.cursor/rules/*.mdc` | Root or `.cursor/` | Plain text or MDC |
| OpenAI Codex | `AGENTS.md` | Root | Markdown |
| Google Jules | `AGENTS.md` | Root | Markdown |
| VS Code (generic) | `AGENTS.md` | Root | Markdown |

**Source:** [AGENTS.md Specification](https://agents.md/), [GitHub Copilot Docs](https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)

### AGENTS.md as Emerging Standard

AGENTS.md is an open standard under the Linux Foundation's Agentic AI Foundation (AAIF):
- Adopted by 60,000+ open source projects
- Supported by Copilot, Cursor, Codex, Jules, VS Code, and others
- AAIF founding members include Anthropic, OpenAI, Block, AWS, Google, Microsoft

**Source:** [Agentic AI Foundation Announcement](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)

### Consolidation Strategies for Root Instructions

**1. Symlink Approach (Recommended)**

Use one primary file and symlink others:

```bash
# Make AGENTS.md the source of truth
mv CLAUDE.md AGENTS.md
ln -s AGENTS.md CLAUDE.md
ln -s AGENTS.md .github/copilot-instructions.md
ln -s AGENTS.md .cursorrules
```

**Source:** [CLAUDE.md to AGENTS.md Migration Guide](https://solmaz.io/log/2025/09/08/claude-md-agents-md-migration-guide/)

**2. Reference File Approach**

Create minimal reference files that point to a primary:

```markdown
# CLAUDE.md
See @AGENTS.md
```

**3. Agentlink Tool**

Automated symlink management via `.agentlink.yaml`:

```yaml
source: AGENTS.md
links:
  - CLAUDE.md
  - .github/copilot-instructions.md
  - .cursorrules
```

**Source:** [Agentlink](https://github.com/martinmose/agentlink)

### Slash Commands / Reusable Prompts

Unlike root instruction files, slash commands have **no cross-platform standard**. Each AI agent uses a different directory:

| Platform | Command Location | Format |
|----------|-----------------|--------|
| Claude Code | `.claude/commands/` | Markdown |
| Cursor | `.cursor/commands/` | Markdown |
| GitHub Copilot | `.github/prompts/` | Markdown |
| Amp | `.agents/commands/` | Markdown |
| Factory | `.factory/commands/` | Markdown |

**Sources:** [Claude Code Docs](https://code.claude.com/docs/en/slash-commands), [Cursor Docs](https://cursor.com/docs/agent/chat/commands), [GitHub Copilot Feature Request](https://github.com/github/copilot-cli/issues/618)

**Key finding:** No consolidation path exists for commands. Options:

1. **Duplicate commands** across platform directories (maintenance burden)
2. **Pick one platform** and accept others won't have commands
3. **Symlink command files** to a shared source directory
4. **Wait for standardization** (AAIF may address this eventually)

**Recommendation:** Start with Claude Code commands in `.claude/commands/`. If other platforms are needed, symlink individual command files rather than duplicating content.

---

## Context File Strategy Analysis

### Current FOCUS State

| File/Directory | Exists | Purpose |
|----------------|--------|---------|
| `CLAUDE.md` | Yes | Claude Code root instructions |
| `.claude/commands/feature.md` | Yes | Claude Code skill for feature implementation |
| `.context/memory/` | Yes | Persistent AI learnings |
| `.context/<issue>/` | Yes | Per-issue working files |
| `AGENTS.md` | No | - |
| `.github/copilot-instructions.md` | No | - |
| `.cursorrules` | No | - |

### File Purpose Analysis

#### Root Instruction Files (CLAUDE.md / AGENTS.md)

**Purpose:** Project-level context for AI agents
- Project overview and architecture
- Build commands
- Code conventions
- File organization patterns

**Risk of not having:** AI agents lack project context, produce inconsistent output

**Existing alternatives:** `CLAUDE.md` exists; `guidelines/*.md` has detailed info but not AI-optimized

#### Command/Skill Files (.claude/commands/)

**Purpose:** Reusable workflows for specific tasks
- Feature implementation process
- PR creation
- Code review patterns

**Risk of not having:** Inconsistent AI-driven workflows, repeated prompting

**Existing alternatives:** None - these are Claude Code-specific

#### Memory Files (.context/memory/)

**Purpose:** Persistent learnings across sessions
- Development process understanding
- Historical decisions
- Patterns learned from past work

**Risk of not having:** AI must re-learn context each session

**Existing alternatives:** `guidelines/development-processes.md` covers some of this

#### Working Files (.context/<issue>/)

**Purpose:** Per-issue working space
- `feature-request.md` - Issue capture
- `research.md` - Investigation findings
- `plan.md` - Implementation approach
- `tasks.md` - Execution tracking

**Risk of not having:** Loss of work-in-progress context

**Existing alternatives:** None - these are ephemeral working files

### Proposed Context File Structure

```
FOCUS_Spec/
├── AGENTS.md                    # Primary AI instructions (source of truth)
├── CLAUDE.md → AGENTS.md        # Symlink for Claude Code
├── .github/
│   └── copilot-instructions.md → ../AGENTS.md  # Symlink for Copilot
├── .claude/
│   ├── commands/
│   │   └── feature.md           # Claude Code feature skill
│   └── settings.local.json
├── .context/
│   ├── .gitignore               # Ignore ephemeral issue folders
│   ├── memory/                  # Committed - persistent AI context
│   │   ├── development-process.md
│   │   └── focus-development-process.md
│   └── <issue-kebab>/           # Gitignored - ephemeral working files
│       ├── feature-request.md
│       ├── research.md
│       ├── plan.md
│       └── tasks.md
└── guidelines/
    └── ai-usage-guidelines.md   # Human-readable policy
```

### Commit vs Gitignore Recommendation

| Path | Commit? | Rationale |
|------|---------|-----------|
| `AGENTS.md` | Yes | Project instructions for all AI agents |
| `CLAUDE.md` | Yes (symlink) | Backward compatibility |
| `.github/copilot-instructions.md` | Yes (symlink) | Copilot support |
| `.claude/commands/*.md` | Yes | Reusable workflows |
| `.context/memory/*.md` | Yes | Persistent AI learnings |
| `.context/<issue>/*` | No | Ephemeral working files |
| `guidelines/ai-usage-guidelines.md` | Yes | Human-readable policy |

### Content Duplication Analysis

**Problem:** Multiple files could contain overlapping information:
- `AGENTS.md` (AI instructions)
- `CLAUDE.md` (same, via symlink)
- `guidelines/ai-usage-guidelines.md` (human policy)
- `.claude/commands/feature.md` (workflow)

**Solution:**

1. **AGENTS.md** = Technical context for AI agents
   - Build commands, architecture, conventions
   - What AI needs to work in the codebase

2. **guidelines/ai-usage-guidelines.md** = Human policy
   - CLA requirements, attribution, review process
   - What humans need to know about AI contributions

3. **.claude/commands/*.md** = Workflows
   - Step-by-step processes
   - References AGENTS.md and guidelines as needed

4. **.context/memory/** = Learnings
   - Things not obvious from code
   - Historical context, decisions

**Key principle:** Each file has a distinct audience and purpose; cross-reference rather than duplicate.

---

## Best Practices from Industry

### AI Contribution Attribution

A growing number of open source projects are adopting disclosure rules for AI-assisted contributions. Marking contributions helps preserve legal clarity and community trust, and makes it easier for reviewers to evaluate code in context.

**Source:** [GitHub Blog - Advancing responsible practices for open source AI](https://github.blog/news-insights/policy-news-and-insights/advancing-responsible-practices-for-open-source-ai/)

Common attribution formats:

- `Assisted-by:` (recommended by some)
- `Generated-by:` (ASF recommendation)
- `Co-authored by:` (GitHub convention)

### Context File Version Control

From [comprehensive AI agent file analysis](https://gist.github.com/0xdevalias/f40bc5a6f84c4c5ad862e314894b2fa6):

**Commit to repository:**

- Root instruction files (`AGENTS.md`, `.cursorrules`, etc.)
- Tool-specific rule directories (`.cursor/rules/`, `.claude/commands/`)
- Project-level MCP configurations

**Gitignore (personal/local):**

- `*.local.md` files (personal preferences)
- User-level configurations (`~/.claude/`, `~/.cursor/`)
- `settings.local.json` files

### Working File Lifecycle

For AI working files (research, plans, tasks):

**Best practices from [Anthropic engineering](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents):**

- Use structured progress files (`claude-progress.txt`) for agent state
- Commit small, logical changes often
- Tag AI-generated branches (e.g., `agent-update-auth-flow`)
- Treat every AI output as a draft requiring human oversight

**Cleanup approaches observed:**

1. **Delete after merge** - Working files are ephemeral, remove when PR complete
2. **Archive to separate location** - Move to `archive/` or `docs/decisions/`
3. **Keep as historical record** - Some projects keep all context files
4. **Selective retention** - Keep research.md, delete feature-request.md/tasks.md

**Recommendation:** Delete ephemeral working files after PR merge; keep memory files permanently.

---

## LF Policy Document Structure

The Linux Foundation Generative AI Policy uses a simple, accessible structure:

1. **Opening statement** - Context and purpose
2. **Core principle** - AI contributions permitted under same standards
3. **Numbered requirements** - 2 key points (tool terms, third-party IP)
4. **Additional guidance** - Helpful tool features
5. **Project variation** - Individual projects may add restrictions

This is intentionally minimal - flowing prose with numbered key points, not a hierarchical document.

---

## Agentic AI Foundation (AAIF)

**Source:** [AAIF Official Site](https://aaif.io/), [LF Announcement](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)

AAIF is a Linux Foundation initiative launched December 2025 to coordinate open, interoperable infrastructure for agentic AI. Founding members include Anthropic, OpenAI, Block, AWS, Google, Microsoft.

### AAIF Projects

Three foundational projects:
- **MCP (Model Context Protocol)** - Universal protocol for connecting AI models to tools/data
- **goose** - Open source, local-first AI agent framework
- **AGENTS.md** - Simple standard for giving AI coding agents project-specific guidance

### AAIF Governance Principles

From [OpenAI announcement](https://openai.com/index/agentic-ai-foundation/):

1. **Open Governance** - Transparent, inclusive; contributors from all backgrounds shape direction
2. **AI Innovation** - Encourages exploration; keeps governance small and responsive
3. **Sustainability and Neutrality** - Neutral infrastructure; inclusion based on adoption/quality, not funding
4. **Focused Scope** - Agentic AI only, not all of AI/ML/data science

### AAIF Security Guidelines

Key measures (from [Solo.io analysis](https://www.solo.io/blog/aaif-announcement-agentgateway)):
- Strict allow-listing and policy enforcement for tool usage
- Cryptographic server identity and attestation
- Sandboxed execution with least privilege
- Auditing, immutable logging, human-in-the-loop approvals for high-risk actions
- Conformance test suites and security checklists

**Note:** AAIF does not yet have published AI usage/contribution policies for member projects. Their focus is on technical standards (MCP, AGENTS.md), not governance policies for AI contributions. Projects should follow LF policies as baseline.

---

## FOCUS Guidelines Structure

Existing FOCUS guidelines (`guidelines/*.md`) use a consistent structure:
- **Overview section** - Purpose and scope
- **Hierarchical headings** - H2/H3 sections for topics
- **Process-oriented** - Step-by-step procedures
- **Cross-references** - Links to related docs

Example from `development-processes.md`:
- H1: FOCUS Development Process
- H2: Overview, Git Issues, Pull Requests, etc.
- H3: Naming and Descriptions, Issue Types, etc.

---

## Document Structure Recommendation

| Source | Style | Recommendation |
|--------|-------|----------------|
| LF Generative AI Policy | Minimal prose, numbered points | Reference for core principles |
| AAIF | No contribution policy yet | Watch for future guidance |
| FOCUS guidelines | Hierarchical sections | **Follow for structure** |
| ASF | Numbered requirements | Reference for specifics |

**Recommendation:** Follow FOCUS guidelines structure (hierarchical H2/H3 sections) to match existing repo conventions, but keep content concise following LF's principle of minimal governance.

---

## Next Steps

1. Present research findings and options to working group
2. Get consensus on policy approach (recommend Option B or D)
3. Decide on context file structure (AGENTS.md as primary, symlinks for others)
4. Draft AI usage guidelines document (following LF structure)
5. Update CONTRIBUTING.md and development-processes.md
6. Create/update AI agent instruction files
7. If EasyCLA changes needed, coordinate with Linux Foundation
