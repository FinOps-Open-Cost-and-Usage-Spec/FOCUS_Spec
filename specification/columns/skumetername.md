# SKU Meter Name

The SKU Meter Name describes the capability being metered or measured by a particular SKU in a charge.

Providers often have billing models in which multiple SKUs exist for a given service to describe and bill for different capabilities for that service. For example, an object storage service may have separate SKUs for capabilities such as object storage, API requests, data transfer, encryption, object management. This field helps practitioners understand which capabilities are being metered by the different SKUs that appear in a FOCUS dataset.

The SkuMeterName column adheres to the following requirements:
 * SkuMeterName MUST be present in the billing data when when the provider includes a [SkuId](#skuid).
 * SkuMeterName MUST be of type String.
 * SkuMeterName MUST be null when SkuId is null.

## Examples
ComputeUsage, BlockVolumeUsage, DataTransfer, ApiRequests

## Column ID

SkuMeterName

## Display Name

SKU Meter Name

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
