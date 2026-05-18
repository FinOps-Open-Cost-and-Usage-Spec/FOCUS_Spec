# Allocated Service Category

The Allocated Service Category is the highest-level classification of the [*service*](#glossary:service) to which cost is being allocated in a [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling), based on the core function of the *service*. The Allocated Service Category is used to classify the consuming *service* in [*charges*](#glossary:charge) where the data generator is allocating costs from the [origin charge's](#glossary:origin-charge) [ServiceCategory](#datasets.costandusage.servicecategory) to a different *service*, as is the case for [allocated charges](#glossary:allocated-charge).

## Requirements

AllocatedServiceCategory MUST adhere to the following requirements:

* AllocatedServiceCategory MUST be of type String.
* AllocatedServiceCategory MUST adhere to the following nullability requirements:
  * AllocatedServiceCategory MUST be null when [AllocatedResourceId](#datasets.costandusage.allocatedresourceid) is null.
  * AllocatedServiceCategory MUST NOT be null when AllocatedResourceId is not null.
* When AllocatedServiceCategory is not null, AllocatedServiceCategory MUST be one of the allowed values.

## Allowed Values

AllocatedServiceCategory MUST use the values defined for [ServiceCategory](#datasets.costandusage.servicecategory).

## Column ID

AllocatedServiceCategory

## Display Name

Allocated Service Category

## Description

Highest-level classification of the *service* to which cost is allocated in data generator-calculated split cost allocation, based on the core function of the *service*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

## Version Introduced

1.5
