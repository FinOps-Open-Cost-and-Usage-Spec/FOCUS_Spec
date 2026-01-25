# Scenario Completeness

FinOps practitioners need to achieve the same analysis and reporting scenarios with [*FOCUS datasets*](#glossary:FOCUS-dataset) that are possible with native datasets. When *FOCUS datasets* lack the information needed for critical scenarios, like organizational hierarchy attribution, commitment discount tracking, or provider-specific optimizations, practitioners cannot adopt FOCUS. Incomplete scenario coverage forces practitioners to use proprietary native datasets, making FOCUS an added overhead rather than an open, provider-agnostic alternative.

This attribute ensures [*data generators*](#glossary:data-generator) provide complete scenario coverage by including custom columns (prefixed with `x_`) that enable scenarios not supported by FOCUS columns alone. Custom columns bridge the gap between FOCUS standardization and provider-specific capabilities, allowing practitioners to adopt *FOCUS datasets* without losing analytical capabilities.

## Attribute ID

ScenarioCompleteness

## Attribute Name

Scenario Completeness

## Description

Defines requirements for a *FOCUS dataset* to include custom columns that enable the same analysis and reporting scenarios available in native datasets.

## Requirements

* A *FOCUS dataset* MUST include custom columns necessary to achieve the same analysis and reporting scenarios that are available with native cost and usage datasets.
  * A *FOCUS dataset* MAY exclude columns from the native dataset that do not support any analysis or reporting scenarios.
  * A *FOCUS dataset* SHOULD maintain the same data fidelity for custom columns as their native dataset equivalents.
  * A *FOCUS dataset* MAY preserve non-FOCUS versions of custom columns even after FOCUS equivalents are introduced to enable migration without breaking changes.
* A *FOCUS dataset* SHOULD include custom columns that enable correlation between *FOCUS datasets* and native datasets (e.g., native [*charge*](#glossary:charge) identifiers).
* A *FOCUS dataset* SHOULD provide documentation describing custom columns, their purpose, and relationship to native columns.
* A *FOCUS dataset* MUST handle custom column values consistently to preserve data integrity when rows are split or aggregated to conform to other FOCUS requirements.

## Exceptions

None

## Introduced (version)

1.4
