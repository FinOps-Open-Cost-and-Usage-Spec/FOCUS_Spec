# SKU Price Lifecycle Status

SKU Price Lifecycle Status represents the current publication and availability state of the specified [*SKU Price*](#glossary:sku-price). [*Service providers*](#glossary:service-provider) continuously update their rate cards with new offerings, price changes, and the retirement of legacy infrastructure, making this column essential for practitioners to filter catalogs and forecast future pricing impacts.

## Requirements

SkuPriceLifecycleStatus MUST adhere to the following requirements:

* SkuPriceLifecycleStatus MUST be of type String.
* SkuPriceLifecycleStatus MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* SkuPriceLifecycleStatus MUST NOT be null.
* SkuPriceLifecycleStatus MUST be one of the allowed values.
* SkuPriceLifecycleStatus MUST be "Active" when the *SKU Price* is currently effective and available for use or purchase.
* SkuPriceLifecycleStatus MUST be "Preview" when the *SKU Price* applies to an offering in a pre-release, beta, or early access state.
* SkuPriceLifecycleStatus MUST be "Deprecated" when the *SKU Price* is still valid for existing deployments but is slated for retirement or no longer available for new consumption.
* SkuPriceLifecycleStatus MUST be "Inactive" when the *SKU Price* is temporarily suspended or disabled but not permanently retired.
* SkuPriceLifecycleStatus MUST be "Archived" when the *SKU Price* is permanently retired, superseded, or no longer effective.
* SkuPriceLifecycleStatus MUST be "Other" when there is a lifecycle state but none of the allowed values apply.

## Allowed Values

| Value      | Description                                                                                                                                      |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| Active     | The *SKU Price* is currently effective and available for use or purchase.                                                                        |
| Preview    | The *SKU Price* applies to an offering that is in a pre-release, beta, or early access state.                                                    |
| Deprecated | The *SKU Price* is still valid for existing deployments but is slated for retirement or no longer available for new consumption.                 |
| Inactive   | The *SKU Price* is currently disabled, suspended, or otherwise temporarily not applicable.                                                       |
| Archived   | The *SKU Price* is permanently retired, superseded, or no longer effective (often representing a historical rate).                               |
| Other      | The *SKU Price* has a lifecycle state not covered by another allowed value.                                                                      |

## Column ID

SkuPriceLifecycleStatus

## Display Name

SKU Price Lifecycle Status

## Description

The current publication and availability state of the specified SKU Price.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

## Version Introduced

1.5
