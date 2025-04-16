# Service Name

A [*service*](#glossary:service) represents an offering that can be purchased from a provider (e.g., cloud virtual machine, SaaS database, professional services from a systems integrator). A *service* offering can include various types of usage or other [*charges*](#glossary:charge). For example, a cloud database *service* may include compute, storage, and networking *charges*.

The Service Name is a display name for the offering that was purchased. The Service Name is commonly used for scenarios like analyzing aggregate cost trends over time and filtering data to investigate anomalies.

The ServiceName column adheres to the following requirements:

* ServiceName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ServiceName MUST be of type String.
* ServiceName MUST conform to [StringHandling](#stringhandling) requirements.
* ServiceName MUST NOT be null.
* The relationship between ServiceName and [ServiceCategory](#servicecategory) is defined as follows:
  * ServiceName MUST have one and only one ServiceCategory that best aligns with its primary purpose, except when no suitable ServiceCategory is available.
  * ServiceName MUST be associated with the ServiceCategory "Other" when no suitable ServiceCategory is available.
* The relationship between ServiceName and [ServiceSubcategory](#servicesubcategory) is defined as follows:
  * ServiceName SHOULD have one and only one ServiceSubcategory that best aligns with its primary purpose, except when no suitable ServiceSubcategory is available.
  * ServiceName SHOULD be associated with the ServiceSubcategory "Other" when no suitable ServiceSubcategory is available.

## Column ID

ServiceName

## Display Name

Service Name

## Description

An offering that can be purchased from a provider (e.g., cloud virtual machine, SaaS database, professional *services* from a systems integrator).

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column type     | Dimension        |
| Feature level   | Mandatory        |
| Allows nulls    | False            |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

0.5
