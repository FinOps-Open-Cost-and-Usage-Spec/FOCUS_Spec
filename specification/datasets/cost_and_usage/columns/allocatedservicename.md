# Allocated Service Name

The Allocated Service Name is a display name for the [*service*](#glossary:service) to which cost is being allocated in a [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling). The Allocated Service Name identifies the consuming *service* on [*allocated charges*](#glossary:allocated-charge) and complements the origin [ServiceName](#datasets.costandusage.servicename), which is preserved on those rows per the [DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling) requirements. When a data generator complies with those requirements, the origin ServiceName on an *allocated charge* reflects the [*origin charge*](#glossary:origin-charge) *service*, not the consuming *service*. AllocatedServiceName provides an explicit, queryable field for the consuming *service* identity without overwriting the origin ServiceName.

## Requirements

AllocatedServiceName MUST adhere to the following requirements:

* AllocatedServiceName MUST be of type String.
* AllocatedServiceName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* AllocatedServiceName MUST adhere to the following nullability requirements:
  * AllocatedServiceName MUST be null when [AllocatedResourceId](#datasets.costandusage.allocatedresourceid) is null.
  * AllocatedServiceName MUST NOT be null when AllocatedResourceId is not null.

## Column ID

AllocatedServiceName

## Display Name

Allocated Service Name

## Description

A display name for the *service* to which cost is allocated in data generator-calculated split cost allocation, identifying the consuming *service* independently of the origin ServiceName.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
