# AI Usage Guidelines

## Overview

This document defines the FOCUS Working Group's policy for using AI tools in specification development. It aligns with the [Linux Foundation Generative AI Policy](https://www.linuxfoundation.org/legal/generative-ai) and applies to all contributions to this repository.

AI tools may be used to assist with FOCUS contributions. AI-generated content is permitted and follows the same intellectual property, licensing, and review standards as human-authored content.

## Permitted Use

AI tools (such as GitHub Copilot, Claude Code, Cursor, and similar coding assistants) may be used in two modes:

- **Interactive**: A human contributor works with AI assistance in real-time. The human reviews, edits, and submits the contribution.
- **Autonomous**: A human requests AI to work independently. The AI creates a PR and assigns it to the human for review. The PR serves as the human review checkpoint.

In both modes, the human contributor takes responsibility for the submitted content.

## Contribution Requirements

### Human Responsibility

A CLA-covered human contributor MUST take responsibility for all contributions. AI agents MAY create PRs on behalf of a human who requested the work. The responsible human is accountable for:

- Reviewing AI-generated output for correctness and quality
- Ensuring compliance with FOCUS normative requirements and editorial conventions
- Verifying no third-party intellectual property conflicts exist
- Confirming the AI tool's terms of service do not conflict with FOCUS licensing

### Review Process

AI-assisted contributions follow the same review process as human-authored contributions:

1. Task Force review for technical accuracy
2. Member review for broader alignment
3. Standard approval workflow per [Development Processes](development-processes.md)

AI-generated content does not bypass any approval workflow or receive different treatment during review.

### CLA Coverage

**Interactive mode**: The human contributor's existing CLA coverage applies. No separate CLA is required for AI tools used interactively where the human controls orchestration and PR submittal.

**Autonomous mode**: AI agents that create PRs directly MUST be onboarded through the Linux Foundation CLA process. To onboard an AI agent, submit a [Maintenance Task](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/new?template=maintenance.md) issue.

## Attribution

Attribution for AI assistance is optional. Contributors may note AI tool usage in pull request descriptions if they choose, but this is not required.

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

### Working File Lifecycle

Working folders (`.ai/<branch-name>/`) contain research, plans, and task tracking for active issues. Before a PR merges:

1. **Migrate valuable content**: Include broadly useful research in `supporting_content/` as part of the PR
2. **Capture execution details**: Add relevant implementation notes to the PR description or linked issue
3. **Delete the working folder**: Remove the `.ai/<branch-name>/` folder as part of the PR

A PR health check confirms no working folders remain before the PR can merge.

These configuration files help AI tools work effectively within the repository, producing consistent content that aligns with project goals and conventions.

## References

- [Linux Foundation Generative AI Policy](https://www.linuxfoundation.org/legal/generative-ai)
- [Apache Software Foundation Generative Tooling Guidance](https://www.apache.org/legal/generative-tooling.html)
- [FOCUS Development Processes](development-processes.md)
- [FOCUS CLA and IPR Requirements](../ipr.md)
