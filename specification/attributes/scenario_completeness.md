# Scenario Completeness

FinOps practitioners need to achieve the same analysis and reporting scenarios with [*FOCUS datasets*](#glossary:FOCUS-dataset) that are possible with native datasets. When *FOCUS datasets* lack the information needed for critical scenarios, like organizational hierarchy attribution, commitment discount tracking, or provider-specific optimizations, practitioners cannot adopt FOCUS. Incomplete scenario coverage forces practitioners to use proprietary native datasets, making FOCUS an added overhead rather than an open, provider-agnostic alternative.

This attribute ensures [*data generators*](#glossary:data-generator) provide complete scenario coverage by including custom columns (prefixed with `x_`) that enable scenarios not supported by FOCUS columns alone. Custom columns bridge the gap between FOCUS standardization and provider-specific capabilities, allowing practitioners to adopt *FOCUS datasets* without losing analytical capabilities.

## Attribute ID

ScenarioCompleteness

## Attribute Name

Scenario Completeness

## Description

Indicates how *data generators* should include custom columns to ensure *FOCUS datasets* enable the same analysis and reporting scenarios available in native datasets.

## Requirements

* *Data generators* MUST include custom columns necessary to achieve the same analysis and reporting scenarios with *FOCUS datasets* that are available with their native cost and usage datasets.
  * *Data generators* MAY exclude native columns that do not support any analysis or reporting scenarios.
  * Custom columns SHOULD maintain the same granularity and accuracy as their native dataset equivalents.
  * *Data generators* MAY preserve non-FOCUS versions of custom columns even after FOCUS equivalents are introduced to enable migration without breaking changes.
* *Data generators* SHOULD include custom columns that enable correlation between *FOCUS datasets* and native datasets (e.g., native [*charge*](#glossary:charge) identifiers).
* *Data generators* SHOULD provide documentation describing custom columns, their purpose, and relationship to native columns.
* When rows are split or aggregated to conform to FOCUS requirements, custom column values MUST be handled consistently to preserve data integrity.

## Exceptions

None

## Introduced (version)

1.4
