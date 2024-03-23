# Pricing Subcategory

Pricing Subcategory describes the pricing model used for a charge within a specific [Pricing Category](#pricingcategory). It can be useful for distinguishing between charges that share the same Pricing Category, but have different pricing rules that may result in a lower prices, like flat-rate compared to volume-based discounts.

The PricingSubcategory column adheres to the following requirements:

* PricingSubcategory MUST be present in the billing data and MUST be of type String.
* PricingSubcategory MUST be null when [PricingCategory](#pricingcategory) is null and MUST NOT be null when PricingCategory is not null.
* PricingSubcategory MUST be one of the allowed values based on the PricingCategory for that row.
* When PricingCategory is "On-Demand":
  * If the charge leverages volume-based or tiered pricing, PricingSubcategory MUST be "Tiered" and the provider SHOULD include a custom column that indicates what pricing tier is applied.
  * If the charge leverages reduced pricing due to a companion SKU or service, PricingSubcategory SHOULD be "Bundled".
  * If the charge leverages reduced pricing due to a prerelease SKU or service, PricingSubcategory SHOULD be "Preview".
* When PricingCategory is "Commitment-Based":
  * If CommitmentDiscountCategory is "Spend", PricingSubcategory MUST be "Committed Spend".
  * If CommitmentDiscountCategory is "Usage", PricingSubcategory MUST be "Committed Usage".
* When PricingCategory is "Dynamic":
  * If the charge leverages a spot price based on market demand, PricingSubcategory SHOULD be "Spot".
* When PricingCategory is "Other", PricingSubcategory MUST be "Other".

## Column ID

PricingSubcategory

## Display Name

Pricing Subcategory

## Description

Describes the kind of pricing model used for a charge within a specific Pricing Category.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Column required | True           |
| Allows nulls    | True           |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values when PricingCategory is "On-Demand":

| Value    | Description                                                                                                           |
| :------- | :-------------------------------------------------------------------------------------------------------------------- |
| Standard | On-demand charges priced at a flat rate for a SKU that does not support volume-based or tiered pricing.               |
| Tiered   | On-demand charges priced at a specific volume-based or tiered level.                                                  |
| Bundled  | On-demand charges priced at a free or reduced rate due to a companion SKU or service that was also used or purchased. |
| Preview  | On-demand charges priced at a free or reduced rate for a prerelease version of the SKU being used or purchased.       |
| Other    | On-demand charges priced in a way not covered above.                                                                  |

Allowed values when PricingCategory is "Commitment-Based":

| Value           | Description                                                                                                        |
| :-------------- | :----------------------------------------------------------------------------------------------------------------- |
| Committed Spend | Charges priced at a reduced rate due to a spend-based commitment-based discount.                                   |
| Committed Usage | Charges priced at a reduced rate due to a usage-based commitment-based discount.                                   |
| Other           | Charges priced at a reduced rate due to a commitment-based discount that is not exclusively spend- or usage-based. |

Allowed values when PricingCategory is "Dynamic":

| Value | Description                                                                            |
| :---- | :------------------------------------------------------------------------------------- |
| Spot  | Charges using a variable spot price determined by the provider based on market demand. |
| Other | Charges using a variable price that is not a spot price.                               |

## Introduced (version)

1.0
