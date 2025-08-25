# Allocated Resource Details

Allocated Resource Details provides information critical in understanding how resources are allocated when using split cost allocation. This information includes but is not limited to: allocation method name, metric used to calculate cost, the usage value/quantity, and the ratio of the cost derived from the method.

The AllocatedResourceDetails column adheres to the following requirements:

* AllocatedResourceDetails MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports provider-calculated split cost allocation.
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
| Value format    | JSON.           |

## Introduced (version)

1.3
