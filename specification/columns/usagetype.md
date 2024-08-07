# Usage Type

The Usage Type describes the type of service usage that is being billed for in a given charge. Cloud services have billing models in which charges are created based on more than one usage parameter. This field enables practitioners to differentiate between when charges for a given service are for different types of usage. For example, an object storage service may have charges for usage types of object storage, API requests, data transfer, encryption, object management, and more, and separate charges may appear in a FOCUS dataset for each of these.

The UsageType column MUST be present in the billing data when a cloud provider charges for more than one type of usage for a given cloud service offering. The column MUST be of type String and MAY be null.

## Column ID

UsageType

## Display Name

Usage Type

## Description

Describes the type of service usage that is being billed for in a given charge. 

## Content Constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.1