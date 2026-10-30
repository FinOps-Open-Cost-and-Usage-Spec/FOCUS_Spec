# Semantic Review of the Tags

> **Note:** This review is part of the demo branch for feature request #2779, proposed for FOCUS 1.6. It is one commit, so it can be compared with the mechanical conversion before it, reviewed on its own, or rolled back.

The mechanical conversion (`convert_all.sh`) translates the identity that the existing markup already states, and leaves anything it cannot decide for a person. This review is that person's pass over the whole specification: every existing tag was checked for semantic correctness, and every item the converter left open was decided by reading its context. In an implementation the two steps would stay separate, because the mechanical step can be rerun at any time; this branch carries both so that it demonstrates the full conversion.

## Summary

| Change | Count |
| :--- | ---: |
| Existing tags corrected | 7 |
| Tags added where judgment settles an open item | 377 |
| Open items deliberately left as plain text | 60 |
| Files changed | 63 |
| Semantic tags before and after | 8,127 and 8,504 |

Every change, with its file, line, before and after text, and reason, is in [`semantic-review-changes.tsv`](semantic-review-changes.tsv). The rules that produced them are in [`semantic_review.py`](semantic_review.py).

Compared with the mechanical conversion, the published specification differs in 80 lines: 72 links added at a first mention, 9 links removed because a mention became a repeat, and 3 links that now point somewhere else. No visible words change.

## How the Existing Tags Were Reviewed

The 8,127 tags reduce to 685 distinct patterns of kind, text, and resolved entity. A tag whose text is exactly an ID that only one dataset defines cannot be wrong, which leaves 550 patterns. Each was checked against its contexts, with extra checks for the risky cases: a role word linked to a column, a glossary term written in a column's capitalization, a name shared by a dataset and a glossary term, a metadata name outside the metadata section, and a value tag after its column.

## Corrections

| File | Before | After | Why |
| :--- | :--- | :--- | :--- |
| `hostprovidername.md` | `[Service Provider](#col:ServiceProviderName)` | `[Service Provider](#term)` | The party whose services are deployed, not the column |
| `billingperiodcreated.md` | `[Billing Period](#term) record` | `[Billing Period](#ds) record` | A record of the Billing Period dataset, not the time window |
| `deprecated.md` | `[Dataset Instance](#meta)` | `[Dataset Instance](#term)` | The dataset instance holding the column, not the metadata object |
| `contractcommitmentperiodend.md` | `[Contract Commitment Period Start](#col:ContractPeriodStart)` | `[Contract Commitment Period Start](#col)` | The text and the example mean ContractCommitmentPeriodStart; this is the FOCUS011 finding |
| `skupricecreated.md`, `skupricelastupdated.md`, `price_effectivity_and_currency.md` | `[SKU Price](#term) record` | `[SKU Price](#ds) record` | A record of the SKU Price dataset; the glossary's SKU Price is a construct that excludes prices |

## Tags Added

| Decision | Tags |
| :--- | ---: |
| A column in a file that mixes datasets, with the dataset chosen from context | 188 |
| A dataset named by a name it shares with a glossary term (SKU Price, Billing Period, Contract Commitment) | 105 |
| A column named by its Display Name capitalization (List Unit Price, Contracted Unit Price, Billing Currency, Availability Zone) | 50 |
| A metadata field or collection | 25 |
| The plural of a column ("SKU Price IDs"), which needs an explicit ID | 6 |
| A glossary term (an italic possessive, *SKU Price's*) | 3 |

The rules behind them:

* **Dataset or concept.** A shared name followed by "dataset", "record", "schema", or "column names", joined to another dataset, included in the data model, or listed with other datasets names the dataset. Otherwise it is the concept, used as ordinary prose ("The Billing Period is the month of April 2025"), and stays plain.
* **Capitalization.** List Unit Price, Contracted Unit Price, Billing Currency, and Availability Zone in their Display Name capitalization mean the column, as #2765 proposes. In a column's own file they are self-references; in the glossary's own entries they are the term.
* **Mixed datasets.** In the SKU Price examples and the catalog supported feature, columns describe SKU Price records. On the rate optimization page, a sentence about a charge (charged, billed, consumption, a correction, or Cost and Usage) means the Cost and Usage column, and a sentence about the catalog means the SKU Price column. Columns listed under a dataset bullet take that dataset. A join key ("joining SKU Price to Cost and Usage on SKU Price ID") means both datasets and stays plain.
* **Explicit qualifiers.** Files that mix datasets get explicit qualifiers (`[SKU Price ID](#col:SkuPrice.SkuPriceId)`) rather than a `dataset:` default, because a default would turn their existing Cost and Usage tags into errors.
* **Metadata.** "Applicable Metadata" lists on the metadata supported features pages are tagged by their nesting (e.g., Dataset Instance ID under Recency means the Recency field). FOCUS Version and Data Generator Version mean the schema fields, except "adopt FOCUS Version 1.1", which is the version of FOCUS.

## Left as Plain Text

| Reason | Items |
| :--- | ---: |
| The concept, used as ordinary prose | 29 |
| The data generator role, which has no glossary entry | 12 |
| The dataset instance as a concept | 4 |
| A join key that means both datasets | 4 |
| Other (a formula, a JSON property, the glossary's own term, the version of FOCUS, a column in both Invoice Detail and Cost and Usage) | 11 |

## Findings That a Tag Cannot Fix

These are inconsistencies in the source, not in the tags. They are reported, not changed, because fixing them changes the specification's wording or needs a decision.

* **The data generator role.** "data generator" is linked to the Data Generator metadata section 16 times (7 links and 9 italic links), and written as plain text 12 more times. The glossary has no entry for the role. In `time_sector_complete.md` the role is even written as the ID "DataGenerator".
* **Host Provider.** In `serviceprovidername.md`, "a Host Provider" (the party) links to the HostProviderName column, because the glossary has no host provider entry.
* **AllocationMethod.** A requirement in `allocatedmethoddetails.md` names "AllocationMethod", which is not an entity ID; it links to AllocatedMethodId.
* **Schema ID casing.** The registry derives `SKUPriceEligibilityObjectSchema` from the heading "SKU Price Eligibility Object Schema", while its file name and references use `SkuPriceEligibilityObjectSchema`. References resolve because IDs match without regard to case.
* **Display Names in Requirements.** Ten FOCUS003 findings remain; nine are notes or "See" lines placed under a Requirements heading.
