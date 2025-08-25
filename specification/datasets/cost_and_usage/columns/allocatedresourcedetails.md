# Allocated Resource Details

Allocated Resource Details provides information critical in understanding how resources are allocated when using split cost allocation. This information includes: allocation method name, metric used to calculate cost, the usage value/quantity, and the ratio of the cost derived from the method.

| Parent | Key | Type | Extensible | Description | Example | 
| ------ | --- | ---- | ---------- | ----------- | ------- |
| null | Method | Key-Value | TRUE | Allocation method used by the provider. | method: methodname |
| Method | Metric | Key-Value | FALSE | Metric used to calculate allocation. | Metric: CPU |
| Method | UsageValue | Key-Value | FALSE | Measured units. | UsageValue: 0.5 |
| Method | RatioValue | Key-Value | FALSE | Ratio of overall cost derived from method. | RatioValue: .05 |

The AllocatedResourceDetails column adheres to the following requirements:

* AllocatedResourceDetails SHOULD be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports provider-calculated split cost allocation.
* AllocatedResourceDetails MUST be of type String.
* AllocatedResourceDetails MUST conform to [StringHandling](#stringhandling) requirements.
* AllocatedResourceDetails nullability is defined as follows:
  * AllocatedResourceDetails MUST be null when a charge is not related to a provider-calculated split cost allocation.
  * AllocatedResourceDetails MUST NOT be null when a charge is related to a provider-calculated split cost allocation.
* AllocatedResourceDetails maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.

## Column ID

AllocatedResourceDetails

## Display Name

Allocated Resource Details

## Description

Self-contained summary of the allocated cost's purpose and price.

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Conditional     |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | JSON           |

## Introduced (version)

1.3
