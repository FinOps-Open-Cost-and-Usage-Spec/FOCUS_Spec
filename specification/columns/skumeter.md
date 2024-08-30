# SKU Meter

The SKU Meter describes the capability being metered or measured by a particular SKU in a charge.

Providers often have billing models in which multiple SKUs exist for a given service to describe and bill for different capabilities for that service. For example, an object storage service may have separate SKUs for capabilities such as object storage, API requests, data transfer, encryption, object management. This field helps practitioners understand which capabilities are being metered by SKUs that appear in a FOCUS dataset.

The SkuMeter column MUST be present in the billing data when a provider supports describing the capabilities contained within a SKU. The column MUST be of type String and MAY be null.

## Column ID

SkuMeter

## Display Name

SkuMeter

## Description

Describes the capability being metered or measured by a particular SKU in a charge.

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