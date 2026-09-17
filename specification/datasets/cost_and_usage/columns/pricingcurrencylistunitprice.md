# Pricing Currency List Unit Price

Pricing Currency List Unit Price represents the provider-suggested unit price per [Pricing Unit](#datamodel.costandusage.pricingunit) for the [*SKU Price*](#glossary:sku-price) identified by the given [SKU Price ID](#datamodel.costandusage.skupriceid). It is the unit price before the application of any negotiated unit price adjustments or discount-bearing [*commitment programs*](#glossary:commitment-program) (e.g., [*commitment discount*](#glossary:commitment-discount)).

Pricing Currency List Unit Price is denominated in the [Pricing Currency](#datamodel.costandusage.pricingcurrency). Pricing Currency List Unit Price is commonly used for rate optimization activities.

## Requirements

PricingCurrencyListUnitPrice MUST adhere to the following requirements:

* PricingCurrencyListUnitPrice MUST be of type Decimal.
* PricingCurrencyListUnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* PricingCurrencyListUnitPrice MUST adhere to the following nullability requirements:
  * PricingCurrencyListUnitPrice MUST be null when SkuPriceId is null.
  * PricingCurrencyListUnitPrice MUST be null when [ChargeCategory](#datamodel.costandusage.chargecategory) is "Tax".
  * PricingCurrencyListUnitPrice MUST NOT be null when SkuPriceId is not null.
  * PricingCurrencyListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#datamodel.costandusage.chargeclass) is not "Correction".
  * PricingCurrencyListUnitPrice MAY be null in all other cases.
* When PricingCurrencyListUnitPrice is not null, PricingCurrencyListUnitPrice MUST adhere to the following requirements:
  * PricingCurrencyListUnitPrice MUST be a non-negative decimal value.
  * PricingCurrencyListUnitPrice MUST be denominated in the PricingCurrency.
  * PricingCurrencyListUnitPrice MUST represent the provider-suggested unit price per PricingUnit for the *SKU Price* identified by the given SkuPriceId.
  * PricingCurrencyListUnitPrice MUST NOT reflect negotiated unit price adjustments for the associated *SKU Price*.
  * PricingCurrencyListUnitPrice MUST NOT reflect any unit price impact dependent on a discount-bearing *commitment program* being applied to the *charge*.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

PricingCurrencyListUnitPrice

## Display Name

Pricing Currency List Unit Price

## Description

The provider-suggested unit price per Pricing Unit for the *SKU Price* identified by the given SKU Price ID, expressed in Pricing Currency.

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Cost and Usage](#datamodel.costandusage)   |
| Operating Model Conditions |                                             |
| ├─ Must                    | [Includes Virtual Currency](#operatingmodelconditions.includesvirtualcurrency) and [Includes Unit Pricing](#operatingmodelconditions.includesunitpricing) |
| └─ Should                  | [Includes Pricing-Billing Currency Differences](#operatingmodelconditions.includespricing-billingcurrencydifferences) and [Includes Unit Pricing](#operatingmodelconditions.includesunitpricing) |
| Column type                | Metric                                      |
| Feature level              | Conditional                                 |
| Allows nulls               | True                                        |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attributes.numericformat) |
| Number range               | Any valid non-negative decimal value        |

## Version Introduced

1.2
