# Allocated Service Name

The Allocated Service Name is a display name for the [*service*](#glossary:service) to which cost is being allocated in a [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling). The Allocated Service Name is used to identify the consuming *service* in [*charges*](#glossary:charge) where the data generator is allocating costs from the [origin charge's](#glossary:origin-charge) [ServiceName](#datasets.costandusage.servicename) to a different *service*, as is the case for [allocated charges](#glossary:allocated-charge).

## Requirements

AllocatedServiceName MUST adhere to the following requirements:

* AllocatedServiceName MUST be of type String.
* AllocatedServiceName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* AllocatedServiceName MUST adhere to the following nullability requirements:
  * AllocatedServiceName MUST be null when [AllocatedResourceId](#datasets.costandusage.allocatedresourceid) is null.
  * AllocatedServiceName MUST NOT be null when AllocatedResourceId is not null.
* When AllocatedServiceName is not null, the relationship between AllocatedServiceName and [AllocatedServiceCategory](#datasets.costandusage.allocatedservicecategory) MUST adhere to the following requirements:
  * AllocatedServiceName MUST have one and only one AllocatedServiceCategory that best aligns with its primary purpose, except when no suitable AllocatedServiceCategory is available.
  * AllocatedServiceName MUST be associated with the AllocatedServiceCategory "Other" when no suitable AllocatedServiceCategory is available.

## Column ID

AllocatedServiceName

## Display Name

Allocated Service Name

## Description

A display name for the *service* to which cost is allocated in data generator-calculated split cost allocation.

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
