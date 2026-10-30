# SKU Meter

[SKU Meter](#col) describes the functionality being metered or measured by a particular SKU in a [charge](#term).

Service providers often have billing models in which multiple SKUs exist for a given service to describe and bill for different functionalities for that service. For example, an object storage service may have separate SKUs for functionalities such as object storage, API requests, data transfer, encryption, and object management. This field helps practitioners understand which functionalities are being metered by the different SKUs that appear in a [Cost and Usage](#ds) [FOCUS dataset](#term).

## Requirements

[SkuMeter](#col) MUST adhere to the following requirements:

* [SkuMeter](#col) MUST be of type String.
* [SkuMeter](#col) MUST conform to [StringHandling](#attr) requirements.
* [SkuMeter](#col) MUST adhere to the following nullability requirements:
  * [SkuMeter](#col) MUST be null when [SkuId](#col) is null.
  * [SkuMeter](#col) SHOULD NOT be null when [SkuId](#col) is not null.
* [SkuMeter](#col) SHOULD remain consistent over time for a given [ServiceProviderName](#col) and [SkuId](#col).

## Examples

Compute Usage, Block Volume Usage, Data Transfer, API Requests

## Column ID

SkuMeter

## Display Name

SKU Meter

## Description

Describes the functionality being metered or measured by a particular SKU in a [charge](#term).

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Unit Pricing](#omc)                                          |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.1
