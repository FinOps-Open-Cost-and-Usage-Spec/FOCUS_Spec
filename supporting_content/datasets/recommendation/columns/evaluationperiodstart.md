# Column: EvaluationPeriodStart

## Status

Proposed as `EvaluationPeriodStart` and `EvaluationPeriodEnd` (Option 1 below) during review of the Recommendation dataset ([PR #2444](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2444)).

Originally proposed as `LookbackPeriodStart` and `LookbackPeriodEnd`. Renamed because "lookback" implies accumulated behavior over time, which reads as excluding recommendations derived from configuration state. Framing the columns as the period a recommendation was derived from covers both cases.

The representation question remains open. Consensus in review was to look at duration expression holistically across the dataset rather than settle it column by column, so the alternative single-column ISO 8601 form is recorded below along with the tradeoffs. Adopting Option 2 later would replace both columns.

## Problem

Recommendation engines derive a recommendation from an evaluation covering some preceding period of time. Two recommendations with identical estimated cost impact are not equally trustworthy when one is based on seven days of observation and the other on 90 days. Without the evaluation period in the dataset, a [*practitioner*](#glossary:practitioner) cannot judge the confidence of a recommendation, and cannot compare recommendations across [data generators](#metadata.datagenerator) that use different default periods.

There is currently no column in the Recommendation dataset expressing the period a recommendation was derived from.

## Options discussed

### Option 1: Explicit start and end timestamps (proposed)

Two Date/Time columns, `EvaluationPeriodStart` and `EvaluationPeriodEnd`, both Optional and nullable, following the [*inclusive start bound*](#glossary:inclusivestartbound) / [*exclusive end bound*](#glossary:exclusiveendbound) convention used by `ChargePeriodStart` / `ChargePeriodEnd`. Both are bounded against `RecommendationCreated`, since a recommendation cannot be derived from behavior observed after it was generated.

Optional was chosen because the dataset is useful without these columns: prioritizing by cost impact, filtering by category, and joining to Cost and Usage all work when the columns are absent. An evaluation period sharpens confidence in a recommendation rather than carrying the dataset's core value.

Under the Evaluation framing, an evaluation period arguably applies to every recommendation, including one derived from configuration state, where the period covers the moment the configuration was assessed. That is an argument for Mandatory and nullable rather than Optional, and is recorded as an open question below.

* Consistent with existing period columns in the specification, such as `ChargePeriodStart` / `ChargePeriodEnd` and `BillingPeriodStart` / `BillingPeriodEnd`, which are the established pattern for expressing a bounded window.
* Directly filterable and comparable without computation.
* Unambiguous about which window was actually observed, including when a generator's window is irregular or was truncated by available history.
* Costs two columns instead of one.

### Option 2: ISO 8601 duration as an offset

A single column carrying an ISO 8601 duration (e.g., `P7D`, `P30D`), interpreted as an offset back from `RecommendationCreated`.

* One column instead of two.
* Matches how generators typically describe their own windows ("30-day evaluation").
* Requires computation to resolve to actual timestamps, and depends on `RecommendationCreated` as the anchor.
* Cannot express a window that does not end at the recommendation's creation time, such as a generator that observes through the end of the prior billing period.
* Introduces an ISO 8601 duration format to the dataset, which is a broader convention decision than this single column.

## Open questions

* Do generators report their intended window (e.g., a configured 30 days) or the window actually observed (e.g., 22 days of available history)? The proposed columns express the window observed, but no requirement currently compels that reading.
* Should these columns be Mandatory and nullable, or Conditional, rather than Optional? If an evaluation period applies to every recommendation, Mandatory keeps the columns dependably present in the schema. Conditional would require stating a condition that cleanly separates recommendation types, which is fuzzier than the contract-commitment one.
* Because the end bound is exclusive, an instantaneous evaluation cannot be expressed as a zero-length period and must be recorded as a short nonzero interval. Is that acceptable?
* Under Optional, a consumer must handle both a missing column and a null value as separate cases. Is that acceptable, or is it an argument for Conditional?
* If ISO 8601 durations are adopted for `ContractCommitmentDurationType`, should this column follow, replacing both columns with the Option 2 form? This is the holistic question the group deferred.
* Should a recommendation derived from a window be required to populate these columns, rather than merely permitted to?

## Related

* `ContractCommitmentDurationType` — open question on expressing duration as a quantity and unit versus a single string, discussed in [PR #2444](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2444). Both this column and that one concern how the dataset expresses durations, which is why the group preferred to resolve them together.
