# Semantic Markup Demo Branch

> **Note:** This branch demonstrates feature request [#2779](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2779), which is proposed for FOCUS 1.6. It is for understanding the concept and for local testing. It is not intended to be merged as is.

The branch is cut from `working_draft`. A representative set of specification files is rewritten with semantic tags, and the real build (`make`) resolves those tags into today's links and formatting. Every file that is not converted keeps its hand-written markup, and both kinds coexist in one build.

## Try It

```bash
cd specification
make spec.html
```

```bash
cd supporting_content/semantic_markup_prototype
PYTHON=/path/to/venv/bin/python ./compare_rendered.sh
```

The first command builds the specification with the tags resolved. The second lists every line of the published `spec.md` that differs from `origin/working_draft`, word by word. You can also open any converted file on GitHub to see how the tagged source reads.

## What Changed in the Build

| File | Change |
| :--- | :--- |
| `vendored/MarkdownPP/Modules/Include.py` | Marks each included file's start and end, and drops YAML front matter from included files |
| `specification/Makefile` | Builds and checks the entity registry, assembles `spec.semantic.md`, and resolves it into `spec.md` |
| `specification/markdownlnt.cfg` | Enables the linter's front matter extension |
| `.gitignore` | Ignores the two new build intermediates |

`resolve_semantic.py` converts Markdown to Markdown, so everything after it is unchanged: the linter, Pandoc, wkhtmltopdf, the link tests, and the published `spec.md` artifact all see ordinary Markdown. With no tags in the source, the resolved `spec.md` is byte-identical to the current build.

Build-time checks:

* Definition checks (REG codes) run on every build. Errors fail the build.
* Unknown entities, invalid values, and ambiguous ColumnIds fail the build with the source file and line number.
* `tests/test_spec_links.py` confirms that every resolved anchor exists in `spec.html`.

`make force=1` downgrades both to warnings.

## Converted Files

| File | What it shows |
| :--- | :--- |
| `datasets/cost_and_usage/columns/billedcost.md` | Glossary-heavy prose, self-references, aliases (*covered*, *cash-based*), and the "invoice issuer" decision |
| `datasets/cost_and_usage/columns/chargeclass.md` | An allowed value tag (`["Correction"](#val:ChargeClass)`) and plain words that become glossary terms |
| `datasets/cost_and_usage/columns/resourcetype.md` | Operating model condition and attribute references, and a Content Constraints table |
| `datasets/invoice_detail/columns/billedcost.md` | A ColumnId shared by two datasets, which resolves to the file's own dataset, plus dataset-qualified IDs (`CostAndUsage.BilledCost`) |
| `attributes/numeric_format.md` | Attribute self-references and glossary terms in normative text |
| `operating_model_conditions/includesresourcetypeassignment.md` | An operating model condition referring to itself |
| `appendix/saas_examples/consumption_currency_pricing_model.md` | Non-normative prose with explicit dataset qualifiers where a ColumnId exists in several datasets |
| `glossary.md` | Front matter declaring two aliases |

Conversion followed the migration steps:

1. `tag_sources.py` made 239 mechanical changes and listed what it could not decide.
2. Judgment calls were made by hand:
   * Self-references by Display Name in prose (e.g., "Billed Cost represents...") are tagged, per the recommendation on #2779.
   * In `chargeclass.md`, "correction" and "charges" are tagged as glossary terms where the same file already treated them as terms.
   * "invoice issuer" in both BilledCost files points to the glossary term, not the InvoiceIssuerName column.
   * In the appendix, ColumnIds shared by several datasets are qualified with `CostAndUsage`, because the example rows are Cost and Usage rows.
   * Ordinary phrases such as "Billing Period" in the appendix are left untagged, because whether plain prose may stay untagged is an open question.

## Review of Rendered Differences

`compare_rendered.sh` reports 26 changed lines in the published `spec.md`. The build resolves 266 semantic references in total. Each one was reviewed and classified using the change types in the Specification Change Guidelines.

| Classification | Lines | Change | Why |
| :--- | ---: | :--- | :--- |
| No visible change | 7 | Table padding in Content Constraints rows | Cell widths differ; the rendered tables are identical |
| Editorial | 12 | Repeat links removed: *covered*, *covered charge*, *covering charge*, *invoice issuer* (Description), and repeated InvoiceDetail column links in Requirements | The Editorial Guidelines link an entity only on its first occurrence in a source file |
| Editorial | 2 | *commitments* now linked at its first mention (one of these lines also has a repeat link removed) | It was styled as a glossary term but never linked |
| Editorial | 4 | "correction", "corrections", and "charges" in ChargeClass now italicized as glossary terms | The same file already treated these words as glossary terms elsewhere |
| Bug fix (needs Working Group confirmation) | 2 | "invoice issuer" in the BilledCost introductions now links the glossary term instead of the InvoiceIssuerName column | The sentence describes the party that issues the invoice, and both files' Descriptions already used the glossary term |
| Regression | 0 | None | |

No normative wording changed. The words of every requirement are the same, and only link styling differs.

One mistake was caught before it reached the output. A hand edit tagged the `# Billed Cost` heading, which is the column's definition, and the REG002 definition check reported it on the next build.

## Known Limitations

* **Requirements Model extraction.** `.github/workflows/rm_extraction.yml` extracts normative statements from the Markdown source. It has not been made tag-aware, so a PR from this branch would show extraction differences.
* **PDF.** The PDF step (wkhtmltopdf) was not run locally. It uses the same resolved `spec.md` and `spec.html`, so it should behave like the HTML build.
* **`build.sh`.** The prototype's `build.sh` compares the samples against the unconverted spec files. On this branch those spec files are already converted, so use `make` and `compare_rendered.sh` instead.
* **Open questions.** The questions in #2779 are still open: dataset scope, plain prose, value links, self-references, and the Requirements Model.
