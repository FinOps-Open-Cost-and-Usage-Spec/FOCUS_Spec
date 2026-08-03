# Column: ContractCommitmentDurationType

## Problem

`ContractCommitmentDurationType` uses the `[Numeric Value] [Unit]` format with an allowed-unit list spanning Minute through Year. The format permits several non-equivalent encodings of the same purchased term, and before this change no requirement selected among them.

For a one-year commitment, "1 Year" and "12 Months" were both conformant. For a one-week commitment, "1 Week" and "7 Days" were both conformant. The two governing requirements were `SHOULD`, and neither expressed a preference for one encoding over another:

* `ContractCommitmentDurationType SHOULD be expressed with a quantity and time unit, where quantity is a positive integer, and time-unit is a standardized unit of time, either singular or plural`
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

* It is additive. A generator already emitting the natural form of a term is unaffected, so the change is non-breaking in practice.
* It preserves the existing string format, the allowed-value list, the data type, and nullability. No consumer parsing logic changes.
* It reuses vocabulary already in the column, so no new concepts are introduced to the specification.
* It resolves the ambiguity at the point where it originates, which is the choice of unit.

Scope decision: reduction applies only across exact conversions between adjacent units (60 minutes to an hour, 24 hours to a day, 7 days to a week, 12 months to a year, 4 quarters to a year). Inexact relationships are deliberately excluded, which is why "365 Days" is not treated as reducible to "1 Year". The existing recommendation that the value reflect the standard duration of the purchased offering already covers that case.

Open question for reviewers: `Quarter` is not treated as a reduction target, so "3 Months" remains valid and is not required to become "1 Quarter". This preserves the "3 Months" example already present in the column and reflects that `Quarter` is absent from the `UnitFormat` allowed time-based units, appearing only in this column's local list. Reviewers may prefer to either add `Quarter` to the reduction ladder or remove it from the allowed values.

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

The corresponding rule is `CCT-ContractCommitmentDurationType-C-008-M`.

It is typed `Dynamic` and carries an empty `Requirement`, matching the adjacent `C-006-O` and `C-007-O` rules. Two reasons:

* Confirming that a value uses the largest whole unit requires the purchased term from the commercial offering, which is not derivable from the dataset alone.
* The underlying check is a divisibility test against the next larger allowed unit. The available `CheckFunctions` provide no divisibility primitive, and expressing divisibility by 7, 12, 24, or 60 as a regular expression over unbounded integers produces patterns tens of thousands of characters long, which are not reviewable.

Automating this rule would require a dedicated check function, for example one that parses a quantity and unit and tests reducibility against a conversion table.
