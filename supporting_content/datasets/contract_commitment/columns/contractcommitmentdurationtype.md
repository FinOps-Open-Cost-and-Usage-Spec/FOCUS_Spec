# Column: ContractCommitmentDurationType

## Problem

`ContractCommitmentDurationType` uses the `[Numeric Value] [Unit]` format with time units spanning Minute through Year. The format permits several non-equivalent encodings of the same purchased term, and before this change no requirement selected among them.

For a one-year commitment, "1 Year" and "12 Months" were both conformant. For a one-week commitment, "1 Week" and "7 Days" were both conformant. The two governing requirements were `SHOULD`, and neither expressed a preference for one encoding over another:

* `ContractCommitmentDurationType SHOULD use the "[Numeric Value] [Unit]" format`
* `ContractCommitmentDurationType SHOULD present the unit of time as one of the allowed values.`

Two providers selling an identical one-year term could therefore emit different strings while both conforming. Because the column is a dimension used for grouping, cross-provider aggregation fragments a single logical term into multiple buckets. This affects commitment planning, renewal forecasting, and weighted-average-term reporting.

The units are also not always exactly interchangeable. A year is not always 365 days, and a month is not a fixed number of days, so treating "365 Days" as a restatement of "1 Year" is not arithmetically sound. Selecting a canonical encoding is therefore a data-correctness concern, not only a presentation concern.

## Options considered

### Option 1: Canonical largest-whole-unit normalization (selected)

Require the largest allowed unit that expresses the purchased term as a whole number.

* "1 Year" is required rather than "12 Months".
* "1 Week" is required rather than "7 Days".
* "4 Months" and "10 Days" are unchanged, because no larger allowed unit divides them evenly.

Selected because:

* It does not change scenario coverage and simplifies scenario enablement: a generator already emitting the natural form (the common case in practice) needs no change. A generator emitting a non-natural encoding (e.g., "12 Months") must update to the canonical form, and a consumer filtering or grouping on a value that was not already conformant may need to update its queries. "Non-breaking" is not an accurate description of that impact.
* It preserves the existing string format, the data type, and nullability. No consumer parsing logic changes.
* It reuses vocabulary already in the column, so no new concepts are introduced to the specification.
* It resolves the ambiguity at the point where it originates, which is the choice of unit.

Scope decision: reduction applies only across exact conversions between adjacent units (60 minutes to an hour, 24 hours to a day, 7 days to a week, 12 months to a year). Inexact relationships are deliberately excluded, which is why "365 Days" is not treated as reducible to "1 Year". The existing recommendation that the value reflect the standard duration of the purchased offering already covers that case.

Resolved by Task Force 1 (2026-09-01): `Quarter`/`Quarters` are dropped entirely, both from this column's allowed values and from the Quarter/Week addition this PR otherwise made to `UnitFormat` (Week stays). A quarter implies alignment with a calendar or fiscal quarter, and three consecutive months do not necessarily fall on those bounds, so treating "3 Months" as reducible to "1 Quarter" would have been incorrect. Dropping `Quarter` also removes the need for a reduction ladder decision on it. The column's unit vocabulary now references UnitFormat's allowed time-based unit names directly instead of duplicating the list locally, so the two lists cannot drift apart again.

### Option 2: ISO 8601 duration format (not selected)

Express the term as an ISO 8601 duration, such as `P1Y` or `P3M`.

Not selected because:

* ISO 8601 durations appear nowhere in the FOCUS specification today. ISO 8601 is referenced only for date and time instants, through the `DateTimeFormat` attribute, which constrains values to the extended format with UTC offset. Introducing duration syntax would add a new representational convention to the specification.
* It is a breaking change. Every existing conformant value would have to be rewritten, and every consumer parsing the column would need new logic.
* ISO 8601 does not by itself remove the ambiguity being fixed. `P1Y` and `P12M` are both well-formed durations, so a canonical-form rule would still be required on top of the new format.
* The column is a categorical classifier intended for grouping and display rather than duration arithmetic, so the machine-readable benefits of ISO 8601 are limited here.

This option is recorded explicitly so reviewers can weigh it, since it is the most plausible alternative.

### Option 3: Separate quantity and unit columns (not selected)

Split the column into a numeric quantity column and a unit column, following the shape of `PricingQuantity` / `PricingUnit` and `ContractCommitmentQuantity` / `ContractCommitmentUnit`.

Not selected because:

* The existing quantity/unit column pairs in FOCUS always measure usage, never time. `ContractCommitmentUnit` is defined as a service-provider-specified measurement unit for the amount in `ContractCommitmentQuantity` and conforms to `UnitFormat`. Reusing the pattern for a time term would give it a second, unrelated meaning.
* It is a breaking schema change that adds a column and removes or redefines an existing mandatory one.
* It does not resolve the ambiguity either. A quantity of 12 with a unit of "Months" and a quantity of 1 with a unit of "Year" would remain equally valid, so a canonical-form rule would still be needed.

## Requirements model

The largest-whole-unit MUST is `CCT-ContractCommitmentDurationType-C-008-M`. It is typed `Dynamic` and carries an empty `Requirement`, matching the adjacent `C-006-O` and `C-007-O` rules: the underlying check is a divisibility test against the next larger allowed unit, and the available `CheckFunctions` provide no divisibility primitive, so the rule cannot be expressed as a static check. Automating it would require a dedicated check function, for example one that parses a quantity and unit and tests reducibility against a conversion table.

## Open items

* **SKU/offering term consistency is out of scope for this column.** Task Force 1 raised a scenario on 2026-09-01: two terms for the same purchased offering (e.g., a 1-month and a 12-month option) should stay in the same time unit so the largest-whole-unit MUST does not make them harder to compare. That scenario is about comparing purchase options across SKUs, which is `PurchaseDurationType` / SKU Price dataset territory (#2424) — that dataset carries `SkuId` to formally scope "same offering" against. The Contract Commitment dataset records commitments already entered into, not a catalog of options, and has no comparable identifier, and "offering" is not itself a defined FOCUS term. This PR does not add a requirement here; the scenario should be tracked against #2424 instead.
