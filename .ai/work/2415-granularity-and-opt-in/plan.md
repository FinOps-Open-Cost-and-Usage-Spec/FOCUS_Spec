# AI #2415 Plan

## Goal

Draft a PR under FR #2358 that models configurable dataset granularity for high-cardinality actor dimensions and keeps PR #2360 unblocked.

## Recommended Implementation Plan

1. Expand `DatasetConfiguration` rather than adding a column-level `Delivery grain` field.
2. Add requirements for documented granularity configurations.
3. Preserve `PrincipalId` and `ConsumerId` as normal reusable CostAndUsage columns.
4. Recommend PR #2360 update its actor conditions to attribution-specific names.
5. Add documentation expectations for configurations that may include actor-level or privacy-sensitive identifiers.
6. Add documentation expectations for metric behavior across configured grains, including summable metrics, non-summable metrics such as unit prices/rates, and supplement/double-counting behavior across delivered dataset instances.
7. Add supporting content with examples showing service-scoped opt-in for Service-A, Service-B, and future session/trace grains.
8. Add a proposed `granularity representation mode` taxonomy: `Expanded`, `Embedded`, and `Referenced`.
9. Add PR open questions comparing expanded CostAndUsage dataset instances, embedded JSON breakdown columns, and referenced one-to-many detail datasets/files.
10. Update requirements model JSON for the normative DatasetConfiguration changes.

## Draft PR Scope

In scope:

* Attribute language for configurable granularity configurations.
* Documentation requirements for configured granularities.
* Documentation requirements or guidance for privacy-sensitive / actor-level granularity.
* Documentation requirements or guidance for metric representation across granular configurations.
* Proposed representation-mode terminology for lower-grain detail.
* Non-normative examples for service-specific opt-in and multiple grain levels.
* PR description open question on expanded rows versus embedded JSON versus referenced detail dataset/file.
* PR description documenting the dependency on PR #2360.

Out of scope:

* Adding `SessionId`, `TraceId`, or other future high-cardinality columns.
* Reworking split cost allocation.
* Defining a general PII compliance regime or resolving plain-text PII rules for `PrincipalId` / `ConsumerId`.
* Creating a new supporting actor/session/trace detail dataset in the initial PR.
* Creating a new JSON breakdown column or object schema in the initial PR.
* Requiring metadata schema changes, unless maintainers want that in the same PR.
* Changing all column content-constraint tables.
