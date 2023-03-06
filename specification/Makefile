PANDOC=$(shell which pandoc)
OPTS=-f gfm --variable mainfont="DejaVu Sans" --metadata title="FOCUS Specification Draft" --pdf-engine=wkhtmltopdf
DEPS=Makefile

all: $(wildcard *.md) $(DEPS)
	$(PANDOC) *.md -o spec.pdf $(OPTS)

clean:
	rm -f spec.pdf
