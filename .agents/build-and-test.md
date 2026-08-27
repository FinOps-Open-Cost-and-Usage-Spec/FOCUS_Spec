# Building, Testing, and Linting

Instructions for building the specification artifacts, generating the requirements model JSON, running tests, and linting markdown.

## Build Commands

### Build the Specification (from `specification/` directory)

```bash
cd specification
make                          # Builds spec.md, spec.html, spec.pdf
make STYLE=working_draft      # Build as working draft (default)
make STYLE=main               # Build as publication version
make STYLE=candidate_release  # Build as candidate release
make clean                    # Clean generated files
```

### Build Requirements Model JSON

```bash
cd specification/requirements_model
./build_json.py --build-only  # Generate model JSON only
./build_json.py               # Run tests then generate JSON
```

### Run Tests

```bash
cd specification/requirements_model
pytest tests/                 # Run all requirements model tests
pytest tests/test_schema.py   # Run a single test file
```

### Lint Markdown

Linting is automatically run as part of `make`. The build will stop if the linter detects issues and will not create the spec.md, spec.html, or spec.pdf files.

To force the build to continue despite linter errors (useful for previewing changes or CI/CD), use:

```bash
make force=1
```

To lint individual files:

```bash
cd specification
python3 enhanced_markdown_lint.py --config markdownlnt.cfg scan <file.md>
```

> **Note:** The enhanced linter provides contextual error messages showing actual vs expected values.

## Document Build Pipeline

1. **Source files**: `*.md` and `*.mdpp` files in `specification/` subdirectories
2. **markdown-pp**: Processes `spec.mdpp` template, resolving `!INCLUDE` directives to assemble the full spec
3. **validate_includes.py**: Ensures all `.md` files in each directory are included in corresponding `.mdpp` templates
4. **pymarkdownlnt**: Lints all markdown files
5. **Pandoc**: Converts assembled markdown to HTML with custom filters
6. **wkhtmltopdf**: Generates PDF from HTML

## Dependencies

**Python packages** (in requirements.txt):

* pymarkdownlnt, panflute, watchdog
* pytest, jsonschema (for requirements model tests)

**System tools**:

* Pandoc (markdown processing)
* wkhtmltopdf (PDF generation)
* GNU Make
