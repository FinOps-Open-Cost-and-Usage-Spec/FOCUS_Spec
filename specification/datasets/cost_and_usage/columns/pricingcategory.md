# Pricing Category

[Pricing Category](#col) describes the pricing model used for a [charge](#term) at the time of use or purchase. It can be useful for distinguishing between [charges](#term) incurred at the [list unit price](#term) or a reduced price and exposing optimization opportunities, like increasing [commitment discount](#term) coverage.

## Requirements

[PricingCategory](#col) MUST adhere to the following requirements:

* [PricingCategory](#col) MUST be of type String.
* [PricingCategory](#col) MUST adhere to the following nullability requirements:
  * [PricingCategory](#col) MUST be null when [SkuPriceId](#col) is null.
  * [PricingCategory](#col) MUST be null when [ChargeCategory](#col) is ["Tax"](#val:CostAndUsage.ChargeCategory).
  * [PricingCategory](#col) MUST NOT be null when [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) or "Purchase" and [ChargeClass](#col) is not ["Correction"](#val:CostAndUsage.ChargeClass).
  * [PricingCategory](#col) MAY be null in all other cases.
* When [PricingCategory](#col) is not null, [PricingCategory](#col) MUST adhere to the following requirements:
  * [PricingCategory](#col) MUST be one of the allowed values.
  * [PricingCategory](#col) MUST be ["Standard"](#val:PricingCategory) when pricing is predetermined at the agreed upon rate for the [billing account](#term).
  * [PricingCategory](#col) MUST be ["Committed"](#val:PricingCategory) when the [charge](#term) is subject to an existing [commitment discount](#term) and is not the purchase of the [commitment discount](#term).
  * [PricingCategory](#col) MUST be ["Dynamic"](#val:PricingCategory) when pricing is determined by the service provider and may change over time, regardless of predetermined agreement pricing.
  * [PricingCategory](#col) MUST be ["Other"](#val:PricingCategory) when there is a pricing model but none of the allowed values apply.

## Allowed Values

| Value     | Description                                                                                                                                                                                                                          |
| :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Standard  | *Charges* priced at the agreed upon rate for the billing account, including [*negotiated discounts*](#glossary:negotiated-discount). This pricing includes any flat rate and volume/tiered pricing but does not include dynamic pricing or reduced pricing due to the application of a *commitment discount*. This does include the purchase of a commitment discount at agreed upon rates. |
| Dynamic   | *Charges* priced at a variable rate determined by the service provider. This includes any product or service with a unit price the service provider can change without notice, like interruptible or low priority [*resources*](#glossary:resource). |
| Committed | *Charges* with reduced pricing due to the application of the *commitment discount* specified by the [Commitment Discount ID](#datamodel.costandusage.commitmentdiscountid). |
| Other     | *Charges* priced in a way not covered by another pricing category. |

## Column ID

PricingCategory

## Display Name

Pricing Category

## Description

Describes the pricing model used for a [charge](#term) at the time of use or purchase.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Multiple Pricing Categories](#omc)                                                        |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | Allowed values                            |

## Version Introduced

1.0-preview
