# Dataset Configuration

Dataset Configuration allows FinOps practitioners to tailor the structure, content, and level of detail of a [*FOCUS dataset*](#glossary:FOCUS-dataset). Datasets provided by data generators are often massive, and their ingestion can lead to excessive storage costs and slow processing times. By selecting only the columns and detail levels needed for a given workflow, FinOps practitioners can optimize the dataset for better performance and lower storage costs.

Common scenarios where dataset configuration is valuable include:

* **Managing Scale**: Trim large exports to reduce time and cost of data preparation
* **Reducing Noise**: Tailor datasets for specific workflows (e.g., cost allocation, commitment analysis)
* **Managing Detail**: Request finer-grained records for cost areas where detailed attribution is needed (e.g., per-user or per-feature costs for a shared service)
* **Lowering Barriers**: Strip away technical complexity for spreadsheet users
* **Enabling Comparison**: Remove custom (`x_`) columns for standardized cross-provider reporting

## Requirements

Dataset conforming to DatasetConfiguration attribute MUST adhere to the following requirements:

* *FOCUS dataset* MUST be configurable to include only a user-defined selection of columns.
* *FOCUS dataset* MUST adhere to all column-level specifications defined in the FOCUS schema, regardless of the selected or default configuration (e.g., column selection, detail level).
* *FOCUS dataset* MAY offer configurable detail levels for provider-defined detail scopes.
* *FOCUS dataset* detail-level configuration MUST be a mapping of provider-defined scope keys to detail level values when configurable detail levels are offered.
* *FOCUS dataset* detail-level value MUST be either a string identifying the requested level or an object containing a `level` property (string) and an optional `delivery-type` property (string).
* *FOCUS dataset* detail-level documentation MUST adhere to the following requirements when configurable detail levels are offered:
  * *FOCUS dataset* detail-level documentation MUST include all offered scope keys and their allowed level values.
  * *FOCUS dataset* detail-level documentation MUST include the effect of each detail level on dataset records, including columns added, effect on row counts, and relationship to other delivered dataset instances that represent the same underlying usage or charges.
  * *FOCUS dataset* detail-level documentation MUST include available `delivery-type` values and their behavior when `delivery-type` configuration is supported.
* *FOCUS dataset* MAY offer a default detail level for each scope key when more than one level is offered for that scope key.
* *FOCUS dataset* default detail level MUST be the least granular level offered for that scope key when a default detail level is offered.
* *FOCUS dataset* MAY offer a default column set.
* *FOCUS dataset* default column set MUST include all applicable [*FOCUS columns*](#glossary:FOCUS-column) when a default column set is offered.

## Example

A practitioner configures their FOCUS Cost and Usage dataset to include only these columns:

* BillingAccountId
* ServiceName
* BilledCost
* EffectiveCost
* Tags

Even though columns like `CommitmentDiscountId` and `ResourceId` are excluded, the included cost columns (`BilledCost`, `EffectiveCost`) still reflect commitment discounts correctly. The dataset remains conformant to the FOCUS specification because each included column follows all requirements for that column, including requirements that reference columns not in the dataset.

A practitioner whose provider offers configurable detail levels requests user-level attribution for LLM costs:

```json
{
  "columns": ["BillingAccountId", "ServiceName", "BilledCost", "EffectiveCost"],
  "detail-level": {
    "llm-costs": "user-level"
  }
}
```

The provider's documentation describes that `"llm-costs"` is a scope key covering AI inference charges, that `"user-level"` adds a user identifier column to matching records, and that records outside this scope are delivered at the default detail level.

A practitioner who also wants to control how the detailed records are delivered uses the extended form:

```json
{
  "detail-level": {
    "llm-costs": {"level": "user-level", "delivery-type": "detail-file"}
  }
}
```

## Attribute ID

DatasetConfiguration

## Attribute Name

Dataset Configuration

## Description

Defines configuration options for controlling the structure, content, and level of detail of a FOCUS dataset.

## Version Introduced

1.4 (column selection); 1.5 (detail level configuration)
