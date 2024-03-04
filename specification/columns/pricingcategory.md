# Pricing Category

Pricing Category describes the pricing model used for a charge at the time of use or purchase. It can be useful for distinguishing between charges at the [List Unit Price](#ListUnitPrice) or a reduced price and exposing optimization opportunities, like increasing [commitment-based discount](#glossary:commitment-based-discount) coverage.

The PricingCategory column adheres to the following requirements:

* PricingCategory MUST be present in the billing data when the provider supports pricing categorizations and MUST be of type String.
* PricingCategory MUST be null if [SkuPriceId](#skupriceid) is null and MUST NOT be null if SkuPriceId is not null.
* PricingCategory MUST be one of the allowed values.
* PricingCategory MUST be "On-Demand" when pricing is predetermined at the standard rate for the [billing account](#glossary:billing-account).
* PricingCategory MUST be "Commitment-Based" when [CommitmentDiscountId](#commitmentdiscountid) is not null.
* PricingCategory MUST be "Dynamic" when pricing is determined by the provider and may change over time, regardless of predetermined agreement pricing.
* PricingCategory MUST be "Other" when there is a pricing model but none of the current allowed values apply.

## Column ID

PricingCategory

## Display name

Pricing Category

## Description

Describes the pricing model used for a charge at the time of use or purchase.

## Content constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| FOCUS Essential | False          |
| Allows nulls    | True           |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value            | Description                     |
| :--------------- | :-------------------------------|
| On-Demand        | Charges priced at the standard rate for the billing account. This includes any flat rate and volume/tiered pricing but does not include dynamic or commitment-based discount pricing. |
| Dynamic          | Charges priced at a variable rate determined by the provider. This includes any product or service with a unit price the provider can change without notice, like interruptible or low priority resources.   |
| Commitment-Based | Charges with reduced prices due to a commitment-based discount specified by the Commitment Discount ID.   |
| Other            | Charges priced in a way not covered by another pricing category.  |

## Introduced (version)

1.0
