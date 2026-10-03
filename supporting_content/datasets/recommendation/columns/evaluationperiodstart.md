# Column: EvaluationPeriodStart

## Status

Included as `EvaluationPeriodStart` and `EvaluationPeriodEnd` (Option 1 below) in the Recommendation dataset ([PR #2444](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2444)).

Originally proposed as `LookbackPeriodStart` and `LookbackPeriodEnd`. Renamed because "lookback" implies accumulated behavior over time, which reads as excluding recommendations derived from configuration state. Framing the columns as the period a recommendation was derived from covers both cases.

The alternative single-column ISO 8601 form is recorded below along with the tradeoffs. It was not adopted: [PR #2600](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2600) also declined ISO 8601 durations for `ContractCommitmentDurationType`, so the dataset does not introduce that format.

## Problem

Recommendation engines derive a recommendation from an evaluation covering some preceding period of time. Two recommendations with identical Estimated Delta Cost are not equally trustworthy when one is based on seven days of observation and the other on 90 days. Without the evaluation period in the dataset, a [*practitioner*](#glossary:practitioner) cannot judge the confidence of a recommendation, and cannot compare recommendations across [data generators](#metadata.datagenerator) that use different default periods.

## Options discussed

### Option 1: Explicit start and end timestamps (selected)

Two Date/Time columns, `EvaluationPeriodStart` and `EvaluationPeriodEnd`, both Conditional on the Includes Evaluation Periods operating model condition and nullable, following the [*inclusive start bound*](#glossary:inclusivestartbound) / [*exclusive end bound*](#glossary:exclusiveendbound) convention used by `ChargePeriodStart` / `ChargePeriodEnd`. Both are bounded against `RecommendationCreated`, since a recommendation cannot be derived from behavior observed after it was generated.

The columns were first proposed as Optional, then changed to Conditional during review. Under Optional, a data generator whose recommendations are all derived from a period of evaluation could omit both columns, so the requirement that they be populated for those recommendations would never apply. Conditional requires the columns whenever the operating model includes such recommendations, while recommendations derived from configuration state carry null values. Mandatory was not chosen because a configuration-derived recommendation has no period of evaluation.

* Consistent with existing period columns in the specification, such as `ChargePeriodStart` / `ChargePeriodEnd` and `BillingPeriodStart` / `BillingPeriodEnd`, which are the established pattern for expressing a bounded window.
* Directly filterable and comparable without computation.
* Unambiguous about which window was actually observed, including when a generator's window is irregular or was truncated by available history.
* Costs two columns instead of one.

### Option 2: ISO 8601 duration as an offset (not selected)

A single column carrying an ISO 8601 duration (e.g., `P7D`, `P30D`), interpreted as an offset back from `RecommendationCreated`.

* One column instead of two.
* Matches how generators typically describe their own windows ("30-day evaluation").
* Requires computation to resolve to actual timestamps, and depends on `RecommendationCreated` as the anchor.
* Cannot express a window that does not end at the recommendation's creation time, such as a generator that observes through the end of the prior billing period.
* Introduces an ISO 8601 duration format to the dataset, which is a broader convention decision than this single column.

## Open questions

* Do generators report their intended window (e.g., a configured 30 days) or the window actually observed (e.g., 22 days of available history)? The columns express the window observed, but no requirement currently compels that reading.
* Because the end bound is exclusive, an instantaneous evaluation cannot be expressed as a zero-length period and must be recorded as a short nonzero interval. Is that acceptable?

## Related

* `ContractCommitmentDurationType` — expresses duration as a quantity and unit rather than an ISO 8601 duration, as decided in [PR #2600](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2600).
