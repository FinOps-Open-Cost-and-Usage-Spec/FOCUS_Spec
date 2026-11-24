# Semantic Tag Tools

These scripts let the specification source state which FOCUS entity a reference means, using semantic tags such as `[BilledCost](#col)` and `[charges](#term)`, and check those references on every build (FR #2779). For how to write tags and the `semantic:` front matter, see [Semantic Tags](../../../guidelines/contributors/editorial-guidelines.md#semantic-tags) in the Editorial Guidelines.

Semantic tags apply to FOCUS 1.6 and later. Text without tags passes through the build unchanged, so tagged and untagged files can coexist.

## Scripts

| Script | What it does | When it runs |
| :--- | :--- | :--- |
| `build_registry.py` | Reads every entity from the file that defines it (columns, allowed values, datasets, attributes, operating model conditions, JSON objects and schemas, metadata, glossary terms) and writes the entity registry as JSON. Checks each definition's structure (REG codes). | Every build |
| `tag_sources.py` | Converts references written in today's conventions to tags and records each converted kind in the file's `semantic:` front matter. With `--check`, changes nothing and reports each line a file listed as `mechanical` would still convert (FOCUS021). | `--check` in every build; conversion by hand |
| `resolve_semantic.py` | Turns tags into today's links and italics in the assembled specification and checks every tag (FOCUS codes). | Every build |
| `registry.py` | Shared lookups: which entity a tag names, in which dataset or metadata collection. | Imported by the scripts above |
| `convert_all.sh` | Runs `tag_sources.py` on the files the build includes, optionally limited to paths and tag kinds. | By hand |
| `compare_rendered.sh` | Builds the published `spec.md` for a base commit and for the working tree, and lists every changed line. | By hand |
| `classify_rendered.py` | Sorts each difference between two `spec.md` files into whitespace, link added, link removed, link retargeted, italics, or text changed. Called by `compare_rendered.sh`. | By hand |

Each script's docstring describes its options in full.

## How the Build Uses Them

`make spec.md` in `specification/` runs these steps after the existing lint and include checks:

1. `build_registry.py` writes `semantic-registry.json` and reports definition findings. The build skips the Requirements Model comparison (REG017).
2. `tag_sources.py --check` checks the conversion status of every source file.
3. markdown-pp assembles `spec.semantic.md`, marking where each included file begins and ends and dropping front matter.
4. `resolve_semantic.py` resolves the tags into `spec.md`, which Pandoc then turns into `spec.html`.

`spec.semantic.md` and `semantic-registry.json` are build outputs and are not committed. `make force=1` reports errors without stopping the build.

## Common Commands

Run these from `specification/`, with the Python environment from `requirements.txt` active.

Write the registry to stdout, with the findings on stderr:

```bash
python3 tools/semantic/build_registry.py --spec-dir . --out - --rm-release none
```

Compare the specification with the Requirements Model before a model release (fails on any REG017 finding):

```bash
make check-requirements-model
```

Convert one area, or only some tag kinds. The report is written to `tools/semantic/build/convert-run.txt`:

```bash
tools/semantic/convert_all.sh datasets/billing_period
tools/semantic/convert_all.sh --kinds col,term datasets/billing_period
```

Check converted files without changing them:

```bash
python3 tools/semantic/tag_sources.py --check --registry semantic-registry.json datasets/billing_period/columns/*.md
```

Compare the published output with the base branch, after a conversion. The full list is in `tools/semantic/build/compare/classification.tsv`:

```bash
tools/semantic/compare_rendered.sh origin/working_draft_interim
```

Everything the scripts write under `tools/semantic/build/` is ignored by git.

## Tests

The tests run locally with pytest. Running them in CI is proposed in #2867.

```bash
python3 -m pytest specification/tools/semantic/tests
```

Run the command from the repository root.

## Check Codes

An error stops the build unless `make force=1` is used. Warnings and information are reported and do not stop it. A finding means two places disagree; it does not say which one is wrong.

### Definition Checks

Reported by `build_registry.py`.

| Code | Level | Finding |
| :--- | :--- | :--- |
| REG001 | Error | A column file has no Column ID or no Display Name section |
| REG002 | Warning | A column file's H1 differs from its Display Name |
| REG003 | Warning | A Column ID is not PascalCase |
| REG004 | Warning | An Allowed Values table has no "Value" column and no column headed with the Display Name, so its values cannot be referenced |
| REG005 | Warning | The same allowed value is listed twice for one column |
| REG006 | Warning | A glossary key does not match its term |
| REG007 | Warning | The Content Constraints "Dataset" row does not name the column's own dataset |
| REG008 | Error | A name or alias is shared by two entities of the same kind |
| REG009 | Info | A name or alias is shared by entities of different kinds, so tags must state the kind |
| REG010 | Error | A glossary anchor is malformed, so its term would be dropped |
| REG011 | Warning | Unknown front matter key in a defining file, or an alias for an unknown glossary key |
| REG012 | Warning | A file under `datasets/` declares a dataset in front matter |
| REG013 | Error | An ID section without its name section, or the reverse, or a definition file with neither |
| REG014 | Warning | A dataset, attribute, operating model condition, or metadata file's H1, or a JSON object's heading, differs from its name |
| REG016 | Warning | A file or folder that defines an entity is not named after its ID in lowercase |
| REG017 | Warning | The specification and the Requirements Model disagree on an entity (only with `make check-requirements-model`, where it fails) |

### Tag Checks

Reported by `resolve_semantic.py`, except FOCUS021, which `tag_sources.py --check` reports.

| Code | Level | Finding |
| :--- | :--- | :--- |
| FOCUS001 | Error | A tag names no entity, or a column that several datasets define without a qualifier |
| FOCUS003 | Warning | A requirement names an entity by its Display Name, where normative text uses its ID |
| FOCUS004 | Error | An untagged ColumnId, only in files that list `col: reviewed` |
| FOCUS008 | Error | A value tag names a value its column does not allow |
| FOCUS010 | Error | Front matter names an unknown dataset |
| FOCUS011 | Warning | The tag text names a different entity than the tag's explicit ID |
| FOCUS012 | Warning | The tag text and the entity's ID or Display Name differ only in case |
| FOCUS013 | Warning | A glossary term is written in a case the glossary conventions do not allow |
| FOCUS014 | Error | A value tag's text is not in double quotes |
| FOCUS015 | Warning | A value tag sits on a line that does not name its column |
| FOCUS016 | Error | Emphasis inside a tag; the build sets the style |
| FOCUS017 | Error | A tag in a heading |
| FOCUS018 | Error | An explicit ID or dataset qualifier that changes nothing |
| FOCUS019 | Error | A requirement mixes ColumnIds and Display Names |
| FOCUS020 | Error | `semantic:` front matter names an unknown kind or status |
| FOCUS021 | Error | A file lists a kind as `mechanical`, but rerunning the converter would change a line (`tag_sources.py --check`) |

Codes not listed here were retired during the prototype and are not reused.
