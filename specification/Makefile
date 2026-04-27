PANDOC=$(shell which pandoc)
MARKDOWNPP=../vendored/bin/markdown-pp
PYMARKDOWNLNT=python3 ./enhanced_markdown_lint.py
WKHTMLTOPDF=$(shell which wkhtmltopdf)
PANDOC_PROJECT_RELATIVE_LINKS=../vendored/pandoc-project-relative-links/pandoc-project-relative-links.py

ifeq ($(STYLE),)
STYLE=working_draft
endif
ifeq ($(BRANCH),)
BRANCH=working_draft
endif

PATH_TO_PROJECT_ROOT=https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/$(BRANCH)
PDF_MARGINS=--variable margin-top=15 --variable margin-bottom=25 --variable margin-left=0 --variable margin-right=10
PDF_FOOTER=--pdf-engine-opt="--footer-right" --pdf-engine-opt="[page] of [topage]" --pdf-engine-opt="--footer-font-name" --pdf-engine-opt="Palatino" --pdf-engine-opt="--footer-font-size" --pdf-engine-opt="8"

# 1. Define only the subdirectories you want to search recursively
SPEC_SOURCE_DIRS=supported_features attributes appendix datasets metadata data schemas

# 2. Grab the markdown files in the root folder without recursing
ROOT_FILES=$(wildcard *.md *.mdpp)

# 3. Grab the markdown files recursively ONLY from the allowed subdirectories
SUBDIR_FILES=$(shell find $(SPEC_SOURCE_DIRS) -type f \( -name "*.md" -o -name "*.mdpp" \) 2>/dev/null)

# 4. Combine them, sort them, and filter out spec.md
SPEC_SOURCE_FILES=$(filter-out ./spec.md spec.md, $(sort $(ROOT_FILES) $(SUBDIR_FILES)))
SPEC_SOURCE_MDFILES=$(filter-out %.mdpp, $(SPEC_SOURCE_FILES))

export TOCDEPTH=2
OS=$(shell uname)

# Set to 1 to force build even if linter finds errors (e.g., make force=1)
force?=0

.PHONY: all clean lint

all: spec.md spec.pdf spec.html

spec.html: spec.md
	$(PANDOC) spec.md -o $@ -f gfm-tex_math_dollars -F $(PANDOC_PROJECT_RELATIVE_LINKS) -M pathToProjectRoot=$(PATH_TO_PROJECT_ROOT) -s --css=styles/${STYLE}_html.css

spec.pdf: spec.html
	$(PANDOC) spec.md -o spec_pdf.html -f gfm-tex_math_dollars -F $(PANDOC_PROJECT_RELATIVE_LINKS) -M pathToProjectRoot=$(PATH_TO_PROJECT_ROOT) -s --css=styles/${STYLE}.css $(PDF_MARGINS)
	$(WKHTMLTOPDF) --enable-local-file-access --footer-right "[page] of [topage]" --footer-font-name "Palatino" --footer-font-size 8 spec_pdf.html $@

lint:
	@echo "Running linter on markdown files in the following directories:"
	@for dir in $$(find $(SPEC_SOURCE_DIRS) -type f \( -name "*.md" -o -name "*.mdpp" \) -exec dirname {} \; | sort -u); do \
		echo "  - $$dir"; \
	done
ifeq ($(force),1)
	-@$(PYMARKDOWNLNT) --config markdownlnt.cfg scan $(SPEC_SOURCE_MDFILES)
else
	@$(PYMARKDOWNLNT) --config markdownlnt.cfg scan $(SPEC_SOURCE_MDFILES)
endif

spec.md: $(SPEC_SOURCE_FILES)
	@echo "Running linter on markdown files in the following directories:"
	@for dir in $$(find $(SPEC_SOURCE_DIRS) -type f \( -name "*.md" -o -name "*.mdpp" \) -exec dirname {} \; | sort -u); do \
		echo "  - $$dir"; \
	done
ifeq ($(force),1)
	-@$(PYMARKDOWNLNT) --config markdownlnt.cfg scan $(SPEC_SOURCE_MDFILES)
else
	@$(PYMARKDOWNLNT) --config markdownlnt.cfg scan $(SPEC_SOURCE_MDFILES)
endif
	@if [ "${STYLE}" = "working_draft" ]; then \
	  cp versions/working_draft.md version.md; \
	  echo "working draft"; \
	  if [ "$(OS)" = "Darwin" ]; then \
	    echo "osx";\
	    sed -i '' 's~Working Draft (Unversioned)~Offline Build (Unversioned)~' version.md; \
	  elif [ "$(OS)" = "Linux" ]; then \
	    sed -i "s~Working Draft (Unversioned)~Branch: ${GITHUB_REF_NAME} (Unversioned)~" version.md; \
	  fi; \
	else \
	  echo "foo ${STYLE} s";\
	  cp versions/${STYLE}.md version.md; \
	fi
	@echo "Validating includes..."
	@for dir in $$(find $(SPEC_SOURCE_DIRS) -type f \( -name "*.md" -o -name "*.mdpp" \) -exec dirname {} \; | sort -u); do \
		mdpp_file="$$dir/$$(basename $$dir).mdpp"; \
		if [ -f "$$mdpp_file" ]; then \
			./validate_includes.py $$dir || exit 1; \
		fi; \
	done
	@echo "Checking for misaligned code block markers (\`\`\`)..."
	@grep -nH '^[[:space:]][[:space:]]*```$$' $(SPEC_SOURCE_FILES) 2>/dev/null | \
	while IFS=: read -r file line _; do \
		echo "WARNING: Found code block escape that is not aligned to the start of the line in file $$file on line $$line"; \
	done || true
	PYTHONPATH=../vendored/ $(MARKDOWNPP) spec.mdpp -o $@
ifeq ($(force),1)
	-@$(PYMARKDOWNLNT) --config markdownlnt.cfg scan $@
else
	@$(PYMARKDOWNLNT) --config markdownlnt.cfg scan $@
endif

clean:
	rm -f spec.pdf spec.html spec.md spec_pdf.html version.md
