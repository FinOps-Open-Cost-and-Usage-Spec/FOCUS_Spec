PANDOC=$(shell which pandoc)
MARKDOWNPP=$(shell which markdown-pp)
PYMARKDOWNLNT=$(shell which pymarkdownlnt)
ifeq ($(shell uname -s), Darwin)
	SED=$(shell which gsed)
else
	SED=$(shell which sed)
endif
ifeq ($(STYLE),)
STYLE="styles/draft.css"
endif
PDF_MARGINS=--variable margin-top=15 --variable margin-bottom=15 --variable margin-left=0 --variable margin-right=0
SPEC_SOURCE_FILES=$(filter-out spec.md, $(wildcard *.md*)) $(wildcard dimensions/*.md*)
SPEC_SOURCE_MDFILES=$(filter-out %.mdpp, $(SPEC_SOURCE_FILES))
all: spec.md spec.pdf spec.html

spec.pdf: spec.md
	$(PANDOC) spec.md -o $@ -f gfm --css=${STYLE} $(PDF_MARGINS) --pdf-engine=wkhtmltopdf

spec.html: 
	$(PANDOC) spec.md -o $@ -f gfm -s --css=${STYLE}

spec.md: $(SPEC_SOURCE_FILES)
	./validate_includes.py dimensions
	./validate_includes.py attributes
	./validate_includes.py appendix
	$(MARKDOWNPP) spec.mdpp -o $@
	$(SED) -i 's|\(<a name=\".*\">\)</a>|\1\&nbsp;</a>|g' $@
	$(SED) -ri '/^[0-9]+.[0-9]+.[0-9]+\\\.\ \ /d' $@
	$(SED) -i 'N;/^\n<a name=/!P;D' $@
	$(PYMARKDOWNLNT) --config markdownlnt.cfg scan $(SPEC_SOURCE_MDFILES)
	$(PYMARKDOWNLNT) --config markdownlnt.cfg scan $@

clean:
	rm -f spec.pdf spec.html spec.md
