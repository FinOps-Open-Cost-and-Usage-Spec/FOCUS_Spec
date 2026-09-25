# Pricing Currency Contracted Unit Price

Pricing Currency Contracted Unit Price represents the negotiated unit price per [Pricing Unit](#datamodel.costandusage.pricingunit) for the [*SKU Price*](#glossary:sku-price) identified by the given [SKU Price ID](#datamodel.costandusage.skupriceid). It is the unit price before any currency exchange rate conversion or the application of any discount-bearing [*commitment programs*](#glossary:commitment-program) (e.g., [*commitment discount*](#glossary:commitment-discount)).

When no negotiated pricing terms apply to the *charge*, Pricing Currency Contracted Unit Price equals [Pricing Currency List Unit Price](#datamodel.costandusage.pricingcurrencylistunitprice).

Pricing Currency Contracted Unit Price is denominated in the [Pricing Currency](#datamodel.costandusage.pricingcurrency). Pricing Currency Contracted Unit Price is commonly used for negotiation activities.

## Requirements

PricingCurrencyContractedUnitPrice MUST adhere to the following requirements:

* PricingCurrencyContractedUnitPrice MUST be of type Decimal.
* PricingCurrencyContractedUnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* PricingCurrencyContractedUnitPrice MUST adhere to the following nullability requirements:
  * PricingCurrencyContractedUnitPrice MUST be null when SkuPriceId is null.
  * PricingCurrencyContractedUnitPrice MUST be null when [ChargeCategory](#datamodel.costandusage.chargecategory) is "Tax".
  * PricingCurrencyContractedUnitPrice MUST NOT be null when SkuPriceId is not null.
  * PricingCurrencyContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#datamodel.costandusage.chargeclass) is not "Correction".
  * PricingCurrencyContractedUnitPrice MAY be null in all other cases.
* When PricingCurrencyContractedUnitPrice is not null, PricingCurrencyContractedUnitPrice MUST adhere to the following requirements:
  * PricingCurrencyContractedUnitPrice MUST be a non-negative decimal value.
  * PricingCurrencyContractedUnitPrice MUST be denominated in the PricingCurrency.
  * PricingCurrencyContractedUnitPrice MUST reflect negotiated pricing terms for the *SKU Price* identified by the given SkuPriceId, excluding negotiated currency exchange rates and independent of any discount-bearing *commitment programs* being applied to the *charge*.
  * PricingCurrencyContractedUnitPrice MUST NOT reflect any unit price impact dependent on a discount-bearing *commitment program* being applied to the *charge*.
  * PricingCurrencyContractedUnitPrice MUST equal PricingCurrencyListUnitPrice when no negotiated pricing terms other than negotiated currency exchange rates apply to the *charge*.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

PricingCurrencyContractedUnitPrice

## Display Name

Pricing Currency Contracted Unit Price

## Description

The negotiated unit price per Pricing Unit for the *SKU Price* identified by the given SKU Price ID, expressed in Pricing Currency.

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
