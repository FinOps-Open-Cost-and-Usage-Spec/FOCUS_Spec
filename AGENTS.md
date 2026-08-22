# AGENTS.md

This file is the model-independent entry point for AI coding assistants working with this repository. It provides a short project orientation and directs agents to the activity-specific instruction files under `.agents/`.

## Project Overview

This is the FinOps Open Cost and Usage Specification (FOCUS) repository - a technical specification for standardizing cloud, SaaS, and billing data schemas. The repository contains both human-readable specification documents (Markdown to HTML/PDF) and machine-readable validation rules (JSON).

FOCUS defines datasets for billing data from cloud providers (AWS, Azure, GCP), SaaS vendors, and on-premises systems. The primary dataset is **Cost and Usage**, which can be joined with the supplemental **Contract Commitment** dataset. Key concepts include account hierarchies (billing accounts, sub-accounts, resources) and service hierarchies (categories, names, SKUs). For detailed schema information, read the specification files in `specification/`.

## Activity Instructions

Read the instruction file that matches the requested activity before starting work. Read multiple files when an activity spans several areas (e.g., writing content and then building the spec to verify it).

| Activity | Instruction File |
|---|---|
| Building the spec, running tests, linting markdown | `.agents/build-and-test.md` |
| Writing or editing specification content | `.agents/writing-specification.md` |
| Reviewing pull requests or specification changes | `.agents/reviewing-changes.md` |
| Working with the requirements model (specification validation) | `.agents/requirements-model.md` |
| Creating issues or PRs, managing working files | `.agents/project-workflow.md` |

Guidance that applies to a single activity lives only in its instruction file. Do not duplicate guidance from `.agents/` files into this file or into model-specific entry files.

## Repository Map

* `specification/` - Specification source files and build tooling
* `specification/requirements_model/` - Machine-readable validation rules (JSON) and tests
* `guidelines/` - Development processes and conventions
* `supporting_content/` - Background info from spec development
* `.agents/` - Activity-specific instruction files for AI agents
* `.ai/` - Per-issue working files (`.ai/work/`) and persistent memory (`.ai/memory/`)

## Model-Specific Entry Points

`CLAUDE.md`, `.cursorrules`, `.gemini/styleguide.md`, and `.github/copilot-instructions.md` are symbolic links to this file. All AI models share this single entry point; model-specific files MUST NOT carry their own guidance.

## AI Usage Policy

AI-assisted contributions are permitted and follow the same review standards as human-authored content. See [AI Usage Guidelines](guidelines/contributors/ai-usage-guidelines.md) for details.
