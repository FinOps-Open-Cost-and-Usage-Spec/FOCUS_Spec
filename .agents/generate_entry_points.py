#!/usr/bin/env python3
"""Generate model-specific entry points for non-agentic AI consumers.

Some AI tools (automated PR review bots such as Gemini Code Assist and
GitHub Copilot code review) inject their instruction file verbatim into a
prompt and cannot follow "read this other file" references. For those
consumers, this script materializes a single file that concatenates the
model-independent entry point with the content and review rules.

Sources (single source of truth; never edit the generated files):
  AGENTS.md
  .agents/writing-specification.md
  .agents/reviewing-changes.md

Targets:
  .gemini/styleguide.md
  .github/copilot-instructions.md

Run from the repository root:
  python3 .agents/generate_entry_points.py
"""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

SOURCES = [
    "AGENTS.md",
    ".agents/writing-specification.md",
    ".agents/reviewing-changes.md",
]

TARGETS = [
    ".gemini/styleguide.md",
    ".github/copilot-instructions.md",
]

HEADER = (
    "<!-- GENERATED FILE - DO NOT EDIT.\n"
    "     This file is generated for AI tools that inject instructions verbatim\n"
    "     and cannot follow file references. Edit the sources instead:\n"
    "     {sources}\n"
    "     Then regenerate with: python3 .agents/generate_entry_points.py -->\n\n"
).format(sources=", ".join(SOURCES))


def main() -> None:
    body = "\n\n".join(
        (REPO_ROOT / source).read_text(encoding="utf-8").strip()
        for source in SOURCES
    )
    content = HEADER + body + "\n"
    for target in TARGETS:
        path = REPO_ROOT / target
        if path.is_symlink():
            path.unlink()
        path.write_text(content, encoding="utf-8")
        print(f"wrote {target} ({len(content)} bytes)")


if __name__ == "__main__":
    main()
