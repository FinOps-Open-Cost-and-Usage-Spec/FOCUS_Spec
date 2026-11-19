# Service Name

A [service](#term) represents an offering that can be purchased from a service provider (e.g., cloud virtual machine, SaaS database, professional services from a systems integrator). A [service](#term) offering can include various types of usage or other [charges](#term). For example, a cloud database [service](#term) may include compute, storage, and networking [charges](#term).

The [Service Name](#col) is a display name for the offering that was purchased. The [Service Name](#col) is commonly used for scenarios like analyzing aggregate cost trends over time and filtering data to investigate anomalies.

## Requirements

[ServiceName](#col) MUST adhere to the following requirements:

* [ServiceName](#col) MUST be of type String.
* [ServiceName](#col) MUST conform to [StringHandling](#attr) requirements.
* [ServiceName](#col) MUST NOT be null.
* The relationship between [ServiceName](#col) and [ServiceCategory](#col) MUST adhere to the following requirements:
  * [ServiceName](#col) MUST have one and only one [ServiceCategory](#col) that best aligns with its primary purpose, except when no suitable [ServiceCategory](#col) is available.
  * [ServiceName](#col) MUST be associated with the [ServiceCategory](#col) "Other" when no suitable [ServiceCategory](#col) is available.
* The relationship between [ServiceName](#col) and [ServiceSubcategory](#col) MUST adhere to the following requirements:
  * [ServiceName](#col) SHOULD have one and only one [ServiceSubcategory](#col) that best aligns with its primary purpose, except when no suitable [ServiceSubcategory](#col) is available.
  * [ServiceName](#col) SHOULD be associated with the [ServiceSubcategory](#col) "Other" when no suitable [ServiceSubcategory](#col) is available.

## Column ID

ServiceName

## Display Name

Service Name

## Description

An offering that can be purchased from a service provider (e.g., cloud virtual machine, SaaS database, professional [services](#term) from a systems integrator).

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | Not applicable                            |
| Column type                | Dimension                                 |
| Feature level              | Mandatory                                 |
| Allows nulls               | False                                     |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

0.5
