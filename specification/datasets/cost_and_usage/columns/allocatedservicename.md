# Allocated Service Name

The Allocated Service Name is a display name for the [*service*](#glossary:service) to which cost is being allocated in a [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling). The Allocated Service Name identifies the consuming *service* on [*allocated charges*](#glossary:allocated-charge) and complements the origin [Service Name](#datamodel.costandusage.servicename), which is preserved on those rows per the Data Generator-Calculated Split Cost Allocation Handling requirements. When a data generator complies with those requirements, the origin Service Name on an *allocated charge* reflects the [*origin charge*](#glossary:origin-charge) *service*, not the consuming *service*. Allocated Service Name provides an explicit, queryable field for the consuming *service* identity without overwriting the origin Service Name.

## Requirements

AllocatedServiceName MUST adhere to the following requirements:

* AllocatedServiceName MUST be of type String.
* AllocatedServiceName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* AllocatedServiceName MUST adhere to the following nullability requirements:
  * AllocatedServiceName MUST be null when a [*charge*](#glossary:charge) is not related to a data generator-calculated split cost allocation.
  * AllocatedServiceName MUST be null when a *charge* represents the unallocated portion of the origin *charge* after split cost allocation.
  * AllocatedServiceName MUST NOT be null when a *charge* represents the allocated portion of the origin *charge*.
* AllocatedServiceName SHOULD match the ServiceName of the *service* to which cost is allocated when that *service* is represented by ServiceName in the FOCUS dataset.

## Column ID

AllocatedServiceName

## Display Name

Allocated Service Name

## Description

The display name of the *service* to which cost is allocated in data generator-calculated split cost allocation.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datamodel.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
