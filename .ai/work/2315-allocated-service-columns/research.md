# Research: FR #2315 — AllocatedServiceName + AllocatedServiceCategory

## Source

GitHub FR [#2315](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2315) — "Improve split cost allocation guidance for data generators and practitioners".

Maintainer comment (Matt Cowsert) narrowed scope to two new columns: `AllocatedServiceName` and `AllocatedServiceCategory`. Graham confirmed: "AllocatedServiceName and AllocatedServiceCategory... the FR calls fo two columns only the focus 1.3 design work i did explains why these shoul be there".

## Problem

Data Generator-Calculated Split Cost Allocation (introduced in 1.3) requires the data generator to preserve the *origin charge* dimensions — including ServiceName and ServiceCategory — on split allocated rows. This preserves invoice reconciliation but leaves the *consuming* service implicit: practitioners can only infer it by external lookup against `AllocatedResourceId`.

Graham's FOCUS 1.3 ETL (finopshub `silver_focus_aws_v13`) rehomes ServiceName on split rows (ctx parent → ch consumer), which violates the current `DataGeneratorCalculatedSplitCostAllocationHandling` MUST. This PR resolves that gap by keeping the origin dimensions intact and adding consumer-side dimensions alongside.

## Design Decision: Consumer-Side Semantics

Two reasonable semantics were considered:

1. **Origin-preserving** — `AllocatedServiceName` carries the origin service. Duplicative with `ServiceName` on allocated rows.
2. **Consumer-side (chosen)** — `AllocatedServiceName` carries the consuming service, matching the `AllocatedResourceId` convention (X = origin, AllocatedX = consumer).

Graham: "Flip to consumer — convention-consistent".

## Nullability Pattern

Both new columns piggyback on `AllocatedResourceId` using the same two-bullet pattern as `AllocatedResourceName`:

* MUST be null when `AllocatedResourceId` is null.
* MUST NOT be null when `AllocatedResourceId` is not null.

This keeps the nullability envelope consistent across the Allocated\* family and avoids introducing a separate applicability predicate.

## Scope (Approved by Graham)

* Two column `.md` definitions.
* `columns.mdpp` alphabetical insertion.
* `dataset.md` summary table + two MUST-include presence bullets.
* Requirements-model JSON rules for both columns (C-000…C-005 for Category; C-000…C-008 for Name including the AllocatedServiceCategory relationship rule).
* `costandusage.json` dataset-level D-077-C and D-078-C presence rules + top-level composite/dependencies references.
* Appendix worked example showing shared-compute split across consumer services of a different `ServiceCategory`.

## Pull Requests

| Part | PR | Description | Status |
| :--- | :--- | :--- | :--- |
| Part 1 | [#2395](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2395) | AllocatedServiceName column + appendix example | Open |
| Part 2 | [#2493](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2493) | Update split cost allocation supported features | Open (depends on #2395) |
| Part 3 | [#2494](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2494) | Add split cost allocation producer field mapping | Open (depends on #2395) |
| RM | [#2554](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2554) | AllocatedServiceName requirements model rules | Open (depends on #2395) |

## Out of Scope (Flagged in FR discussion, deferred)

* `AllocatedRatio` — Graham: "these are not the direction of the spec effectivecost and billedcost remain the main cost columns".
* `UnallocatedCost` — same.
* `ParentResourceCost` — same.
