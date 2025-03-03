PANDOC=$(shell which pandoc)
MARKDOWNPP=../vendored/bin/markdown-pp
PYMARKDOWNLNT=$(shell which pymarkdownlnt)
WKHTMLTOPDF=$(shell which wkhtmltopdf)
ifeq ($(STYLE),)
STYLE="working_draft"
endif
PDF_MARGINS=--variable margin-top=15 --variable margin-bottom=25 --variable margin-left=0 --variable margin-right=10
PDF_FOOTER=--pdf-engine-opt="--footer-right" --pdf-engine-opt="[page] of [topage]" --pdf-engine-opt="--footer-font-name" --pdf-engine-opt="Palatino" --pdf-engine-opt="--footer-font-size" --pdf-engine-opt="8"
SPEC_SOURCE_FILES=$(filter-out spec.md, $(wildcard *.md*)) $(wildcard columns/*.md*) $(wildcard attributes/*.md*) $(wildcard appendix/*.md*)
SPEC_SOURCE_MDFILES=$(filter-out %.mdpp, $(SPEC_SOURCE_FILES))
export TOCDEPTH=2
all: spec.md spec.pdf spec.html

spec.html: spec.md
	$(PANDOC) spec.md -o $@ -f gfm -s --css=styles/${STYLE}_html.css

spec.pdf: spec.html
	$(PANDOC) spec.md -o spec_pdf.html -f gfm -s --css=styles/${STYLE}.css $(PDF_MARGINS)
	$(WKHTMLTOPDF) --enable-local-file-access --footer-right "[page] of [topage]" --footer-font-name "Palatino" --footer-font-size 8 spec_pdf.html $@

spec.md: $(SPEC_SOURCE_FILES)
ifneq ("$(wildcard versions/${STYLE}.md)","")
	cp versions/${STYLE}.md version.md
else
	cp versions/working_draft.md version.md
endif
	./validate_includes.py columns
	./validate_includes.py attributes
	./validate_includes.py metadata
	./validate_includes.py metadata/data_generator
	./validate_includes.py metadata/schema
	./validate_includes.py metadata/schema/column_definition
	./validate_includes.py appendix
	./validate_includes.py appendix/examples
	./validate_includes.py appendix/examples/metadata_examples
	./validate_includes.py appendix/examples/saas_examples
	PYTHONPATH=../vendored/ $(MARKDOWNPP) spec.mdpp -o $@
	$(PYMARKDOWNLNT) --config markdownlnt.cfg scan $(SPEC_SOURCE_MDFILES)
	$(PYMARKDOWNLNT) --config markdownlnt.cfg scan $@

clean:
	rm -f spec.pdf spec.html spec.md spec_pdf.md version.md
