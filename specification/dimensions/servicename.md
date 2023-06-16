# Service Name

A service represents the offering that was purchased through the provider (e.g., professional or cloud services). For cloud resources, the service is a higher-level classification of the resource type and may include multiple usage charges of different types (e.g., compute, storage, networking). The service is not a classification of the type of usage. Instead, it represents the offering you might find on a provider's website.

The Service Name is a display name for the service or offering that was purchased. The Service Name is commonly used for scenarios like analyzing aggregate cost trends over time and filtering data to investigate anomalies.

The ServiceName column MUST be present in the cost data. This column MUST be of type String and MUST NOT contain null values.

## Column ID

ServiceName

## Display Name

Service Name

## Description

A service represents the offering that was purchased through the provider (e.g., professional or cloud services).

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | True             |
| Data type       | String           |
| Allows nulls    | False            |
| Value format    | \<not specified> |

## Introduced (version)

0.5
