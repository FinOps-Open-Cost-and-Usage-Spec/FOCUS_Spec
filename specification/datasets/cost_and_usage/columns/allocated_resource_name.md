# Allocated Resource Name

The Allocated Resource Name is a display name which cost is being allocated to in a provider-calculated split cost allocation. The Allocated Resource Name is used to understand what the cost is being allocated to in [*charges*](#glossary:charge) where the provider is allocating costs to something other than the charge's [ResourceID](#ResourceId).

The allocated_resource_name column adheres to the following requirements:

* allocated_resource_name MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports provider-calculated split cost allocation.
* allocated_resource_name MUST be of type String.
* allocated_resource_name MUST conform to [StringHandling](#stringhandling) requirements.
* allocated_resource_name nullability is defined as follows:
  * allocated_resource_name MUST be null when [allocated_resource_id](#allocated_resource_id) is null.
  * allocated_resource_name MUST NOT be null when allocated_resource_id is not null.
* allocated_resource_name MAY duplicate allocated_resource_id when a separate display name is not applicable.

## Column ID

allocated_resource_name

## Display Name

Allocated Resource Name

## Description

The Allocated Resource Name is a display name which cost is being allocated to in a provider-calculated split cost allocation.

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Conditional     |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

1.3
