# Allocated Method ID

Allocated Method ID is the identifier for the method defined by the provider which was used for the provider-calculated split cost allocation.

The allocated_method_id column adheres to the following requirements:

* allocated_method_id MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports provider-calculated split cost allocation.
* allocated_method_id MUST be of type String.
* allocated_method_id MUST conform to [StringHandling](#stringhandling) requirements.
* allocated_method_id nullability is defined as follows:
  * allocated_method_id MUST be null when a [*charge*](#glossary:charge) is not related to a provider-calculated split cost allocation.
  * allocated_method_id MUST NOT be null when a *charge* is related to a provider-calculated split cost allocation.
* allocated_method_id MUST uniquely identify the method used to calculate the split cost allocation in the provider's documentation.

## Column ID

allocated_method_id

## Display Name

Allocated Method ID

## Description

Allocated Method ID is the identifier for the method defined by the provider which was used for the provider-calculated split cost allocation.

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.3
