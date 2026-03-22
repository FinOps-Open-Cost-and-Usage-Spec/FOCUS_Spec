# MarkdownPP Guidelines for FOCUS Specification

This document outlines the use of MarkdownPP in the FOCUS Specification repository, including build processes, custom enhancements, and best practices.

***Note:*** *The guidelines in this document apply to the content within the `specification/` directory.*

## Overview

The FOCUS Specification uses [MarkdownPP](https://github.com/amyreese/markdown-pp) (Markdown Preprocessor) to build the complete specification document from modular markdown files. The original instance of MarkdownPP is no longer actively maintained, and we use a locally modified version that includes enhancements specifically designed for multi-dataset technical documentation.

## Repository Structure

```text
specification/
├── spec.mdpp                    # Main preprocessor file
├── Makefile                     # Build automation
├── markdownlnt.cfg              # Markdown linting configuration
├── datasets/                    # Dataset-specific content
├── attributes/                  # Attribute specifications
├── metadata/                    # Metadata specifications
├── appendix/                    # Appendix materials
├── supported_features/          # Features enabled by FOCUS
└── requirements_model/          # Validation rules and models
```

***Note:*** *For directory and file naming conventions across the repository, see [Repository Naming Conventions](repository-naming-conventions.md).*

## MarkdownPP Usage in FOCUS

### Main Specification File (`spec.mdpp`)

The root specification file `spec.mdpp` uses MarkdownPP directives to compose the complete document.  After specifying some administrative pieces, the following statements reflect the core of the specification.  Each `INCLUDE` corresponds to a section of the document; for example, the second entry for `supported_features` corresponds to Section 2 of the spec.

```markdown
!INCLUDE "overview.md",1
!INCLUDE "supported_features/supported_features.mdpp",1
!INCLUDE "datasets/datasets.mdpp",1
!INCLUDE "attributes/attributes.mdpp",1
!INCLUDE "metadata/metadata.mdpp",1
!INCLUDE "use_case_library.md",1
!INCLUDE "glossary.md",1
!INCLUDE "appendix/appendix.mdpp",1
```

The number after any `!INCLUDE` statement is a shift parameter that adds the specified number of subheaders to the included file.  We typically use 0 or 1, but larger numbers are technically allowed.

### Multi-Dataset Table of Contents

Our enhanced MarkdownPP supports different TOC depths for different specification sections:

```markdown
## Table of Contents

!TOC 2 2 3 2 2 2 2 2
```

This will set the table of contents depth based on the header order. Depth of 2 for the first two sections (Overview and Supported Features), 3 for the third (Datasets), and 2 for the remaining (Attributes, Metadata, Use Case Library, Glossary, and Appendix).

## Makefile Integration

### Build Targets

The `specification/Makefile` provides several MarkdownPP-based build targets:

```makefile
# Generate all output formats
all: spec.md spec.pdf spec.html

# Generate HTML specification
spec.html: spec.mdpp $(DEPENDENCIES)

# Generate PDF via HTML
spec.pdf: spec.html

# Generate assembled Markdown file
spec.md: $(SPEC_SOURCE_FILES)

# Clean up build files
clean:
```

### Build Dependencies

The Makefile tracks dependencies to ensure proper rebuilding:

```makefile
SPEC_SOURCE_FILES=$(filter-out spec.md, $(wildcard *.md*)) $(wildcard supported_features/*.md*) $(wildcard columns/*.md*) $(wildcard attributes/*.md*) $(wildcard appendix/*.md*)
SPEC_SOURCE_MDFILES=$(filter-out %.mdpp, $(SPEC_SOURCE_FILES))
```

If new folder paths with Markdown and/or MarkdownPP files are added to the FOCUS repository, the build system will need to be updated to include these paths in the SPEC_SOURCE_FILES argument.

## Local MarkdownPP Modifications

We have tailored MarkdownPP to work best for FOCUS, and using the vendored version of the package is critical to create an artifact that matches the expectations of the FOCUS project output.

### Vendored Package Location

```text
vendored/MarkdownPP/
├── MarkdownPP.py              # Main interface
├── Module.py                  # Base module class
├── Processor.py               # Core processor
├── Transform.py               # Data transformation
└── Modules/
    ├── Include.py             # File inclusion
    ├── TableOfContents.py     # **MODIFIED** - Multi-dataset support
    ├── Reference.py           # Reference management
    └── ...
```

### Key Modifications

To see the actual code modifications made in this project, use the following command:

```bash
curl -s https://raw.githubusercontent.com/amyreese/markdown-pp/refs/heads/master/MarkdownPP/Modules/TableOfContents.py | diff -y --side-by-side - vendored/MarkdownPP/Modules/TableOfContents.py
```

#### 1. Enhanced Table of Contents (`TableOfContents.py`)

**CSS-Styled Output**:

```html
<!-- Original -->
- [Section](#section)

<!-- Enhanced -->
<ul class="toc tocdepth2">
    <li class="toc item"><a href="#section">Section</a></li>
</ul>
```

**Enhanced Anchors**:

```html
<a class="toc-anchor" name="section-name">&nbsp;</a>
```

**Dynamic Depth Control**:

```markdown
<!-- Different depths per section -->
!TOC 2 3 1 4

<!-- Results in: -->
<!-- Section 1: depth 2, Section 2: depth 3, etc. -->
```

**Improved Anchor Generation**:

```python
# Collision detection for duplicate section names
if short in anchor_names:
    counter = 2
    while f"{short}-{counter}" in anchor_names:
        counter += 1
    short = f"{short}-{counter}"
```

**SkipTOC Header Support**:

Headers can be excluded from table of contents generation while maintaining proper document formatting:

```markdown
<!-- Header appears in document but not in TOC -->
## My Header<!--SkipTOC-->

<!-- Also works with other header levels -->
### Another Header<!--SkipTOC-->
```

This feature automatically:

* Excludes marked headers from TOC generation
* Prevents section numbering for these headers
* Skips anchor link creation
* Ensures proper spacing around headers to meet markdown linting requirements
* Maintains document readability and structure

**Automatic Anchor Generation:**

All headers appearing after the !TOC directive automatically receive an HTML anchor generated from the header text whereby the following applies:

* Anchor text is normalized to lowercase.
* Whitespace and the following characters are removed: `,` `-` `(` `)`.
* Other special characters are preserved.
* Dots (.) are inserted between header levels to represent the full hierarchy of document sections.
* Headers marked with `<!--SkipTOC-->` will appear in the document but will not be included in the Table of Contents, and no anchor will be created.

## Best Practices

### Header Conventions

The FOCUS Specification relies on Markdown headers to define document structure, section numbering, and navigation. Consistent header usage is required to ensure predictable Table of Contents (TOC) generation and stable internal links.

#### File-Level Header Structure

* Content-oriented Markdown files (.md) SHOULD begin with a top-level header that defines the section title.
* MarkdownPP assembly files (.mdpp) that consist only of !INCLUDE directives MAY omit headers.

#### Header Syntax

To ensure predictable Table of Contents (TOC) generation, stable internal links, and reliable external references, all headers in the FOCUS Specification MUST follow these conventions:

* Headers MUST use ATX-style Markdown syntax (`#`).
* Up to six header levels (######) are supported.
* A single space MUST follow the `#` character(s).
* Headers MUST NOT use Setext-style headers (`=` or `-` underlines), even though they are technically supported.
* Headers MUST NOT be empty.
* Header text SHOULD only contain alphanumeric characters (`A-Z`, `0-9`), spaces (` `), commas (`,`), and the following special characters: hyphens (`-`), apostrophes (`'`), and parentheses (`(`, `)`).
* Other special characters SHOULD be avoided.

#### Renaming or Changing Headers After Publication

Header anchors are used by build processes (e.g., TOC generation) and may also appear in external hyperlinks. Header text and structure SHOULD remain stable after publication to maintain repository consistency, TOC accuracy, and external hyperlink integrity.

If a header change is necessary, all affected build references MUST be updated accordingly to avoid broken links.

### File Content

While markdown can be included in a .mdpp, the FOCUS project discourages this behavior, as the markdown will not natively render in GitHub and development environments such as VS Code, thereby making spec maintenance more difficult. Therefore, we encourage the use of overview .md files, limiting the use of .mdpp files to `!INCLUDE` statements only.

### File Organization

```markdown
<!-- Use descriptive include paths -->
!INCLUDE "datasets/cost_and_usage/overview.md"
!INCLUDE "datasets/cost_and_usage/columns/billedcost.md"

<!-- Group related includes -->
!INCLUDE "attributes/column_handling.md"
!INCLUDE "attributes/string_handling.md"
!INCLUDE "attributes/numeric_format.md"
```

### Header Level Management

```markdown
<!-- Adjust header levels when including -->
!INCLUDE "section.md", 2    # Shift headers down 2 levels

<!-- Example: # Title becomes ### Title -->
```

## Validation and Quality Control

### Pre-Processing Validation

```python
# validate_includes.py checks:
# - File existence
# - Circular includes
# - Header level consistency
python validate_includes.py spec.mdpp
```

If any new sections are added to the spec that require such validation, they need to be added to `validate_includes.py`.

## Styling Integration

### CSS Classes for TOC

```css
/* specification/styles/main.css */
.toc { 
    list-style: none; 
    padding-left: 0; 
}

.toc.tocdepth1 { font-size: 1.2em; font-weight: bold; }
.toc.tocdepth2 { font-size: 1.1em; margin-left: 20px; }
.toc.tocdepth3 { font-size: 1.0em; margin-left: 40px; }
.toc.tocdepth4 { font-size: 0.9em; margin-left: 60px; }

.toc.item { 
    padding: 3px 0; 
    border-bottom: 1px dotted #ccc; 
}

.toc-anchor { 
    visibility: hidden; 
    position: absolute; 
    margin-top: -60px; 
}
```

## Troubleshooting

### Common Issues

**Include Path Problems**:

```bash
# Check file exists
ls -la datasets/cost_and_usage/overview.md

# Verify relative paths
find . -name "overview.md"
```

**TOC Generation Issues**:

```markdown
<!-- Ensure proper header syntax -->
# Valid Header
## Another Valid Header

<!-- Avoid -->
#Invalid (no space)
# Too   Many    Spaces
```

**Build Failures**:

```bash
# Clean and rebuild
make clean
make
```

Most build failures are from [linting](https://pymarkdown.readthedocs.io/) issues with Markdown, and addressing these should be the first point of call. Remember that HTML and Markdown only supports six levels of headings, and many sections of the specification are already at this limit; adding headings under these sections can therefore cause issues.
