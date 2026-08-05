# AI #2415 Tasks

## Original Research (Completed Under Old Approach)

* [x] Fetch and review issue #2415.
* [x] Fetch and review FR #2358.
* [x] Review PR #2351 for Conditions architecture relevance.
* [x] Review PR #2360 actor column approach.
* [x] Review prior attribute PR patterns (#1816, #1800, #1501).
* [x] Review local current spec files for DatasetConfiguration, DatasetCompleteness, split cost allocation, metadata, and dataset instance concepts.

## Redesign (New Approach — Service-Specific Detail)

* [x] Replace abstract granularity-configuration / applicability-filter approach with service-specific detail configuration.
* [x] Update normative requirements in `specification/attributes/dataset_configuration.md`.
* [x] Update `supporting_content/attributes/dataset_configuration.md` with new Service-Specific Detail Configuration section.
* [x] Update `specification/attributes/attributes_overview.md` description.
* [x] Fix formatting violations: documentation-subject pattern, canonical subjects, version attribution.
* [x] Add requirement that detail levels may include dimension columns outside the column list.
* [x] Correct version attribution to 1.5; restore 1.4 table to base state.
* [x] Update pr_body.md and plan.md to reflect new approach.

## Pending

* [x] Replace granularity terminology with service-specific detail configuration.
* [x] Add record-minimization requirements for identical delivered dimensions and non-summable metrics.
* [x] Clarify split cost allocation as a defined subset of service-specific detail configuration.
* [x] Add detail-scope documentation disclosure for split cost allocation usage.
* [x] Clarify separately delivered detail as a provider-defined companion artifact unless FOCUS defines a standard dataset for that detail.
* [ ] Requirements model JSON update (deferred until approach is agreed upon).
* [ ] Move PR #2473 out of draft after final review of the updated text.
* [ ] Resolve stale outdated GitHub review threads after final review of the updated text.
