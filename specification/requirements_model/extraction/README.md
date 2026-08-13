# Requirements Model Extraction

This directory contains a Node.js tool that generates Requirements Model JSON
directly from the FOCUS specification markdown. It replaces manual authoring of
`model_rules/` files: the normative bullet list under each entity's
`## Requirements` heading is parsed and expanded into a family of machine-readable
rules, with stable Rule IDs carried forward across releases.

## Contents

| File | Role |
|---|---|
| `extract_rm.js` | The extractor. Reads spec markdown, writes `output/model_rules/`. |
| `verify.js` | Correctness audit of the generated output (structural + deep transformation). |
| `validate_markdown.js` | Pre-flight check that spec markdown is shaped as the extractor expects. |
| `markdown_util.js` | Shared helpers (inline rendering, entity decoding, path naming) used by all three. |
| `requirements_model_contract.json` | Declares where each entity type lives in the spec and which headings to read. |
| `*.test.js` | Node built-in test-runner tests for the utilities and verifier. |
| `output/` | Generated rule files (see `output/README.md`). |

The per-release sentence-to-check-function lookup lives outside this directory,
at `../releases/<version>/check_function_lookup.json`, alongside the baseline
rule files it is versioned with.

## Quick start

```bash
cd specification/requirements_model/extraction
npm install            # installs marked
npm run validate       # confirm the markdown is well-formed (optional but recommended)
npm run extract        # generate output/model_rules/
npm run verify         # audit the generated output
npm run diff           # report which entities differ from releases/latest
npm test               # run the unit tests
```

The extractor always diffs the current branch's markdown against the baseline model
in `releases/latest`, so corrections made there are picked up on the next run. Both
the baseline directory and the stamped version can be overridden:

```bash
NEW_VERSION=1.6 npm run extract                  # stamp new rules with a bumped version

# Diff against an older release. NEW_VERSION is derived from the baseline, so set it
# explicitly here or new rules are stamped with the old release's version.
BASELINE_DIR=1.4 NEW_VERSION=1.5 npm run extract
DATASET_FOLDERS=billing_period npm run extract   # limit to specific dataset folders
```

## What the extraction does, step by step

The extractor (`extract_rm.js`, `main()`) runs the following pipeline. Every step
is driven by `requirements_model_contract.json` so that file locations and
heading names are never hard-coded.

### 1. Load the contract and per-release inputs

* Read `requirements_model_contract.json` — this declares, for each entity type
  (DataModel, Dataset, Column, Attribute, Condition), the spec location, the
  entity type name, the Rule-ID artifact type letter, an optional ID prefix, and
  the heading names that hold the entity ID, display name, and requirements.
* Load the check-function lookup for the target version from
  `../releases/<NEW_VERSION>/check_function_lookup.json`. This maps a normalized
  requirement sentence (with the entity name replaced by `{entity}`) to a
  `{ function, requirement }` pair. Absent file is tolerated as an empty lookup.
* Scan `specification/conditions/` to build an anchor-to-ConditionId map, so
  that `#conditions.<anchor>` links in the markdown resolve to real Condition IDs.

### 2. Walk the entities

Entities are processed in an order that respects dependencies:

1. **DataModel** — `specification/datasets/data_model.md` (single entity).
2. **Attributes** — every `*.md` in `specification/attributes/` that has both an
   ID heading and a Requirements heading (overview files without those are
   skipped). Attributes are processed *before* datasets and columns because a
   column's "MUST conform to <Attribute>" rule needs the attribute's root Rule ID
   to record as a dependency.
3. **Datasets and their Columns** — every dataset folder under
   `specification/datasets/` that contains a `dataset.md`, then each `*.md` under
   that folder's `columns/`.

### 3. Parse each markdown file into a requirement tree

For one entity file (`emit` -> `parseRequirementTree`):

* The `marked` lexer produces an AST.
* The body of the `## Requirements` section is located. Its lead-in paragraph
  (the anchor sentence, e.g. `BillingPeriod MUST adhere to the following
  requirements:`) becomes the tree root, and the nested bullet list becomes the
  tree's children.
* Each bullet's inline tokens are rendered to plain text via
  `markdown_util.renderInline`, which keeps link and emphasis display text and
  decodes HTML entities so the stored text matches the source exactly. Nested
  bullets become child nodes. `#conditions.<anchor>` links on a bullet are
  recorded as that rule's condition anchors.

### 4. Classify each node into a rule

`flattenTree` turns the tree into a pre-order list, then each node is classified
(`classify`) in this precedence order:

1. **Composite** — a node with children becomes an `AND` over its child rules
   (`CheckModelRule` items), and lists those children as `Dependencies`.
2. **Presence** — a leaf matching `MUST include <X>`. For datasets this emits a
   `ColumnPresent` requirement; the data model records the reference generically.
3. **Check-function lookup** — a leaf whose normalized sentence is a key in the
   lookup gets a populated domain `Requirement` (Type, Nullability, Format, etc.),
   with `{entity}` substituted back to the real entity name.
4. **Attribute conformance** — a leaf matching `MUST conform to <Attribute>
   requirements`, where `<Attribute>` is a real generated attribute, records a
   dependency on that attribute's root rule (no inline requirement).
5. **Unclassified** — any remaining leaf is emitted with an empty `Requirement`
   and recorded as a warning so the lookup can be extended.

A rule with a populated `Requirement` is typed `Static`; an empty one is `Dynamic`.
The BCP-14 keyword (`MUST`, `SHOULD NOT`, `MAY`, ...) is extracted from the
sentence, and the status letter (M / O / C) is derived from the keyword and
whether the sentence is conditional (contains `when`).

### 5. Assign stable Rule IDs

Rule IDs are stable across releases (`expandTree`). Format:

* `<DatasetType>-<ArtifactName>-<ArtifactType>-<NumericId>-<Status>` for
  dataset-scoped entities (e.g. `BIP-BillingPeriod-D-004-M`), where the
  `DatasetType` prefix comes from the contract's `DatasetTypes` map.
* `<ArtifactName>-<ArtifactType>-<NumericId>-<Status>` otherwise.

ID assignment:

* The `releases/latest` rule file(s) are loaded as a baseline. If a derived
  rule's requirement text (normalized) matches a baseline rule, that rule's
  existing ID is reused, preserving its `ModelVersionIntroduced`.
* A new requirement takes the next free NumericId above the baseline maximum.
* A baseline rule with no matching requirement in the current markdown is
  **tombstoned**: carried into the output with `Status: "Removed"`,
  `ModelVersionRemoved: <NEW_VERSION>`, and `Order: -1`. A rule already removed
  in the baseline is carried through unchanged.
* Except when that rule's `ModelVersionIntroduced` is `NEW_VERSION`. It was added
  during the current drafting cycle and never published, so a tombstone would
  announce the removal of something no consumer ever saw. It is **dropped** from
  the output instead and reported, since the baseline copy must be deleted by hand.
  Its NumericId stays reserved until that deletion happens.

Output for each entity is sorted by NumericId and written to its own JSON file
under `output/model_rules/`, mirroring the `releases/<v>/model_rules/` layout.

### 6. Report

The extractor prints a per-entity rule count, followed by up to three summaries:

* **Accepted as Dynamic** — a count of sentences with no derivable check function
  that matched a baseline rule already curated with an empty `Requirement`. These
  need no action; the count is printed so the total stays visible.
* **Unpublished removals** — baseline rules introduced in `NEW_VERSION` that are no
  longer in the markdown. These are dropped from the output rather than tombstoned,
  and each is listed with its Rule ID and baseline file because **this output folder
  is not the baseline**: the copy in `releases/latest` has to be deleted by hand.
* **No check-function mapping** — sentences that resolved to neither a check function
  nor a curated baseline `Requirement`, so those sentences can be added to the lookup.

## Completeness (`npm run diff`)

`verify.js` checks that the transformation is internally consistent. `diff_model.js`
answers a different question: **how much of the model can the extractor actually
derive?** An entity is fully derived when its generated file is byte-identical to the
hand-authored copy in `releases/latest`. Anything less is a gap — a missing
check-function mapping, a curated value the sentence cannot express, or a rule the
markdown no longer states.

Entities are matched by mirrored relative path. Each shared entity lands in one bucket:

| Bucket | Meaning |
|---|---|
| `identical (byte-equal)` | Fully derived. |
| `formatting only` | Same rules, same key order, different whitespace. |
| `key order only` | Same rules and values, keys emitted in a different order. |
| `content differs` | Rules added, removed, or changed. |

Baseline entities with no generated counterpart are split by cause, so that only the
last of the three counts as a gap:

* **out of extractor scope** — `conditions/` and `datasets/*/objects/`. The contract
  defines no Objects entity, and conditions markdown is read only for the
  anchor-to-`ConditionId` map.
* **tombstone-only** — every rule is already `Removed` and the markdown is gone, so
  there is nothing left to derive.
* **missing (has active rules)** — a real gap.

The run ends with one verdict line:

* `✅ Model COMPLETE` — every in-scope entity is byte-identical.
* `✅ Content COMPLETE` — all rules and values match; some entities differ only in key
  order or whitespace.
* `❌ Model has gaps: N entities differ … in content` — a real derivation gap.

Only content differences, missing baseline entities, and generated-only entities count
as gaps. Key order and whitespace do not: the hand-authored baseline carries **25
distinct rule key orders**, so byte equality is unreachable until the baseline is
normalized from generated output. Treating that drift as a gap would mean encoding 25
orderings into the generator. `--strict` therefore fails on content gaps only.

For entities that differ, the detail section lists rules present on only one side and,
for changed rules, each differing field as `path: baseline -> generated`.

```bash
npm run diff                  # summary + per-entity detail
npm run diff -- --summary     # counts and verdict only
npm run diff -- --strict      # exit 1 on a content gap (for CI gating)
```

Run `npm run extract` first; the diff reads `output/model_rules/` and does not
regenerate it. `BASELINE_DIR` selects the baseline, exactly as for extraction.

## Verification

`verify.js` audits the generated output in two layers and exits non-zero on any
failure:

* **Structural integrity** over every output file — no duplicate Rule IDs or
  NumericIds, files sorted by NumericId, active-rule dependencies resolve
  (within the file or to external `ATT-*` rules), composite `Items` match
  `Dependencies`, `Keyword` matches the sentence, dataset/column rules carry a
  `DatasetType` and an ID prefixed with it, and no raw HTML entities leaked into
  any `MustSatisfy`.
* **Deep transformation audit** of the `billing_period` dataset file — expected
  rules are independently re-derived from the two inputs (the `releases/latest`
  baseline JSON and the current markdown) and compared against the output,
  checking coverage, ID reuse, `ModelVersionIntroduced`, and tombstoning.

`validate_markdown.js` is a lighter pre-flight check that the spec markdown is
shaped the way the extractor requires (present Requirements section, anchor
paragraph, well-formed bullet list) before extraction is attempted.

## Environment variables

| Variable | Default | Effect |
|---|---|---|
| `BASELINE_DIR` | `latest` | Directory under `releases/` to use as the baseline for stable IDs and curated Requirements. Also selects the check-function lookup. |
| `NEW_VERSION` | baseline's `ModelVersion` | Version stamped into `ModelVersionIntroduced` / `ModelVersionRemoved` for new and tombstoned rules. |
| `DATASET_FOLDERS` | (all) | Comma-separated dataset folders to limit extraction to. |
| `DATASET_FOLDER` | `billing_period` | Dataset file targeted by the `verify.js` deep audit. |
