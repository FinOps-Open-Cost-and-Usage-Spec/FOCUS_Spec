# AI #2415 Plan

## Goal

Draft a PR under FR #2358 that models scoped detail configuration in DatasetConfiguration, enabling practitioners to opt into optional higher-cardinality detail for documented areas of a FOCUS dataset.

## Approach

Extend `DatasetConfiguration` with requirements for the resulting dataset and detail-scope documentation. The specification does not define a request payload, property name, or transport mechanism. Providers can expose selection through an API parameter, export setting, query interface, or another access mechanism.

Scoped detail configuration is broader than split cost allocation. Data Generator-Calculated Split Cost Allocation Handling is treated as a defined subset for detail levels that split an origin charge into allocated charges.

## Implementation

1. Update `specification/attributes/dataset_configuration.md`:
   * Add requirements for selecting one detail level per detail scope when multiple levels are offered.
   * Add requirements for selecting one delivery method when a selected detail level has multiple delivery methods.
   * Require detail-scope documentation to identify FOCUS dimension criteria, offered detail levels, populated columns, split cost allocation usage, available delivery methods, related artifacts, and relationship columns for separately delivered detail.
   * Add record-minimization guidance for records with identical delivered dimensions and non-summable metrics.

2. Update `supporting_content/attributes/dataset_configuration.md`:
   * Explain detail scopes, data coverage, delivery methods, record minimization, actor attribution, and split cost allocation relationship.
   * Clarify that separately delivered detail is provider-defined unless FOCUS defines a standard dataset for that detail.
   * Keep metadata changes illustrative and deferred to a separate PR.

3. Update `specification/attributes/attributes_overview.md`:
   * Describe DatasetConfiguration as covering schema and level of detail.

## Out of Scope

* Defining `PrincipalId`, `ConsumerId`, `SessionId`, `TraceId`, or other future high-cardinality columns.
* Defining a request payload, field names, or transport mechanism for selection.
* Defining metadata schema changes for selected scoped detail.
* Defining a new standard detail dataset.
* Updating requirements model JSON before the task force settles the normative wording.
