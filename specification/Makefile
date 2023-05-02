PANDOC=$(shell which pandoc)
MARKDOWNPP=$(shell which markdown-pp)
PYMARKDOWNLNT=$(shell which pymarkdownlnt)
SED=$(shell which sed)

DOC_TITLE="FOCUS: FinOps Open Cost and Usage Specification"
MAIN_FONT="DejaVu Sans"
DEPS=Makefile
SED_PATTERN=
SPEC_SOURCE_FILES=$(filter-out spec.md, $(wildcard *.md*)) $(wildcard dimensions/*.md*)
SPEC_SOURCE_MDFILES=$(filter-out %.mdpp, $(SPEC_SOURCE_FILES))
all: spec.md spec.pdf

spec.pdf: spec.md
	$(PANDOC) spec.md -o $@ -f gfm --variable mainfont=$(MAIN_FONT) --metadata title=$(DOC_TITLE) --pdf-engine=wkhtmltopdf

spec.md: $(SPEC_SOURCE_FILES)
	$(MARKDOWNPP) spec.mdpp -o $@
ifeq ($(shell uname -s), Darwin)
	$(SED) -i '' 's|\(<a name=\".*\">\)</a>|\1\&nbsp;</a>|g' $@
else
	$(SED) -i 's|\(<a name=\".*\">\)</a>|\1\&nbsp;</a>|g' $@
endif
	$(PYMARKDOWNLNT) --config markdownlnt.cfg scan $(SPEC_SOURCE_MDFILES)
	$(PYMARKDOWNLNT) --config markdownlnt.cfg scan $@

clean:
	rm -f spec.pdf spec.md
