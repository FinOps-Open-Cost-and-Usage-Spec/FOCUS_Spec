# SKU Capability

The SKU Capability describes the capability provided by the SKU that is being metered or measured in a given charge.

Providers often have billing models in which multiple SKUs exist for a given service to describe and bill for different capabilities for that service. This field helps practitioners understand and differentiate between the SKUs that appear in a FOCUS dataset. For example, an object storage service may have separate SKUs for capabilities such as object storage, API requests, data transfer, encryption, object management. This field describes the differences in capabilities between these SKUs.

The SkuCapability column MUST be present in the billing data when a provider supports describing the capabilities contained within a SKU. The column MUST be of type String and MAY be null.

## Column ID

SkuCapability

## Display Name

SkuCapability

## Description

Describes the capability provided by a SKU that is represented by a given charge.

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