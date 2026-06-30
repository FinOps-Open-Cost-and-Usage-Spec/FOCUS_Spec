# AI #2415 Plan

## Goal

Draft a PR under FR #2358 that models configurable detail levels in the DatasetConfiguration request, enabling practitioners to opt into finer-grained records for specific cost areas.

## Approach

Extend `DatasetConfiguration` with a `detail-level` configuration key that maps provider-defined scope keys to provider-defined level values. This is a request-side model: practitioners specify what detail they want in their configuration request; providers document what is available.

This replaces the earlier "granularity configurations" / "applicability filter" approach, which was framed as documentation requirements on providers rather than as a concrete request schema for practitioners.

## Implementation

1. Update `specification/attributes/dataset_configuration.md`:
   * Replace "granularity configuration" / "applicability filter" language with `detail-level` / "scope key" language
   * Add normative requirements for the `detail-level` key, its two value forms (string and object), and provider documentation obligations
   * Add JSON examples showing both shorthand and extended forms

2. Update `supporting_content/attributes/dataset_configuration.md`:
   * Replace "Dataset Instance Granularities" section with "Detail Level Configuration" section
   * Document scope keys, level values, delivery types, cardinality trade-offs, hierarchical levels, and actor attribution
   * Update metadata example to use the `detail-level` shape
   * Update "Developed for 1.4" table

3. Update requirements model JSON if normative requirements are finalized.

## JSON Shapes

Shorthand (level only):
```json
{
  "detail-level": {
    "llm-costs": "user-level",
    "shared-platform": "feature"
  }
}
```

Extended (level + delivery-type):
```json
{
  "detail-level": {
    "llm-costs": {"level": "user-level", "delivery-type": "detail-file"},
    "shared-platform": {"level": "feature", "delivery-type": "inline"}
  }
}
```

Both forms may appear together in the same `detail-level` object.

## Open Questions

* Should delivery types (`inline`, `added-lines`, `detail-file`) be enumerated as FOCUS-defined values or remain fully provider-defined?
* Should scope keys be allowed to reference column values (e.g., ServiceName values) or must they be provider-defined opaque strings?
* Should the configuration key name be hyphenated (`detail-level`) or camelCase (`detailLevel`) to be consistent with other configuration keys?
* How does this interact with PR #2360 (`PrincipalId` / `ConsumerId`)? Actor columns would appear in expanded records at actor-level detail.

## Out of Scope

* Adding `SessionId`, `TraceId`, or other future high-cardinality columns.
* Reworking split cost allocation.
* Defining a general PII compliance regime for actor identifiers.
* Creating a new supporting actor/session/trace detail dataset.
* Creating a new JSON breakdown column or object schema.
* Requiring metadata schema changes (metadata example is illustrative only).
