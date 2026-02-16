# AI Usage Guidelines

## Overview

This document defines the FOCUS Working Group's policy for using AI tools in specification development. It aligns with the [Linux Foundation Generative AI Policy](https://www.linuxfoundation.org/legal/generative-ai) and applies to all contributions to this repository.

AI tools may be used to assist with FOCUS contributions. AI-generated content is permitted and follows the same intellectual property, licensing, and review standards as human-authored content.

The use of AI in specification development is still evolving, and this is therefore a living document that will shift as AI usage patterns mature.
## Usage Modes

AI tools (e.g., GitHub Copilot, Claude Code, Cursor, and similar coding assistants) are typically used in two modes:

- **Interactive**: A human contributor works with AI assistance in real-time. The human reviews, edits, and submits the contribution.
- **Autonomous**: A human requests AI to work independently. The AI creates a PR, comments, or suggestions and assigns them to the human for review. The PR serves as the human review checkpoint.

## Contribution Requirements

### Human Responsibility

* A human contributor covered by a [Contributor License Agreement](https://github.com/FinOps-Open-Cost-and-Usage-Spec/EasyCLA) (CLA) MUST take responsibility for all contributions.
* AI agents MAY create PRs on behalf of a human who requested the work.
* The CLA-covered human MUST be accountable for:
  * Reviewing AI-generated output for correctness and quality
  * Ensuring compliance with FOCUS normative requirements and editorial conventions
  * Verifying no third-party intellectual property conflicts exist
  * Confirming the AI tool's terms of service do not conflict with FOCUS licensing

### Review Process

AI-assisted contributions follow the same review process as human-authored contributions:

1. **Human Self-Review**: The CLA-covered contributor MUST thoroughly review and validate all AI-generated content before requesting peer review. When possible, the responsible human SHOULD provide an approving review as sign-off.
2. **Technical Validation**: The relevant Task Force MUST review the contribution for technical accuracy and schema compliance.
3. **Strategic Alignment**: WG Members MUST review the contribution to ensure it aligns with broader community goals and the FOCUS roadmap.
4. **Standard Approval**: All contributions MUST follow the established workflow per [Development Processes](development-processes.md).

AI-generated content does not bypass any approval workflow or receive different treatment during review.

### CLA Coverage

**Interactive Mode:** 
* Human contributions made using AI tools MUST be covered by the contributor’s existing CLA. No separate CLA is required for AI tools used interactively where the human controls orchestration and PR submission.
* Per the [Linux Foundation Generative AI Policy](https://www.linuxfoundation.org/legal/generative-ai), the contributor MUST ensure that the terms and conditions of the AI tool do not place any contractual restrictions on its output that are inconsistent with FOCUS' [open source software license](https://creativecommons.org/licenses/by/4.0/) and [intellectual property policies](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/operating_procedures.md#514-consistency--ipr-reviews).
* The contributor MUST assume full responsibility for ensuring the AI-generated content adheres to all project standards and legal requirements.

**Autonomous mode**: 
* AI agents that create PRs directly MUST be onboarded through the Linux Foundation CLA process. 
* To onboard an AI agent, a contributor MUST submit a [Maintenance Task](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/new?template=maintenance.yml) issue.

## Attribution

The contributor MAY attribute AI assistance and/or tool usage in pull request descriptions, but this is not required.

The FOCUS project does not mandate a specific attribution format. This aligns with the Linux Foundation policy, which focuses on human responsibility rather than disclosure requirements.

## AI Agent Configuration

This repository includes configuration files for AI coding assistants:

- `AGENTS.md` - Project context and conventions (at root for tool compatibility)
- `.ai/commands/` - Reusable workflow definitions
- `.ai/memory/` - Persistent learnings across sessions
- `.ai/<branch-name>/` - Working files for active issues (deleted after PR merge)

Tool-specific wrapper files reference the centralized configuration:

- `CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md` - Symlinks to `AGENTS.md`
- `.claude/commands/`, `.cursor/commands/`, `.github/prompts/` - Tool-specific wrappers for interactive use

### Creating Shared Commands

To create a new shared command available across all supported AI tools:

1. **Create the main workflow** in `.ai/commands/<name>.md` with full process documentation
2. **Create tool-specific wrappers** that reference the main workflow:

| Tool | File | Format |
| --- | --- | --- |
| Claude Code | `.claude/commands/<name>.md` | YAML frontmatter with `allowed-tools`, then reference |
| Cursor | `.cursor/commands/<name>.md` | Simple reference to `.ai/commands/<name>.md` |
| GitHub Copilot | `.github/prompts/<name>.prompt.md` | Simple reference to `.ai/commands/<name>.md` |

See existing commands (e.g., `feature`, `pr-update`) for examples.

### Working File Lifecycle

Working folders (`.ai/work/<issue-number>-<kebab-case-name>/`) contain research, plans, and task tracking for active issues. Use the same naming convention as your branch.

After a PR is approved but before merging:

1. **Migrate valuable content**: Include broadly useful research in `supporting_content/`
2. **Capture execution details**: Add relevant implementation notes to the PR description or linked issue
3. **Delete the working folder**: Remove the `.ai/work/` folder in a final commit

**Important**: Do not delete working files until final approval is received. A PR readiness check will remind you when cleanup is needed.

These configuration files help AI tools work effectively within the repository, producing consistent content that aligns with project goals and conventions.

## References

- [Linux Foundation Generative AI Policy](https://www.linuxfoundation.org/legal/generative-ai)
- [Apache Software Foundation Generative Tooling Guidance](https://www.apache.org/legal/generative-tooling.html)
- [FOCUS Development Processes](development-processes.md)
- [FOCUS CLA and IPR Requirements](../ipr.md)
