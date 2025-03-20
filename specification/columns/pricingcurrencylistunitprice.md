# Pricing Currency List Unit Price

The Pricing Currency List Unit Price represents the suggested provider-published unit price for a single [Pricing Unit](#pricingunit) of the associated SKU, exclusive of any discounts. This price is denominated in the [Pricing Currency](#pricingcurrency). The Pricing Currency List Unit Price is commonly used for calculating savings based on various rate optimization activities.

The PricingCurrencyListUnitPrice column adheres to the following requirements:

* PricingCurrencyListUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports pricing and billing in different currencies.
* PricingCurrencyListUnitPrice MUST be of type Decimal.
* PricingCurrencyListUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
* PricingCurrencyListUnitPrice nullability is defined as follows:
  * PricingCurrencyListUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * PricingCurrencyListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * PricingCurrencyListUnitPrice MAY be null in all other cases.
* When PricingCurrencyListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
  * PricingCurrencyListUnitPrice MUST be a non-negative decimal value.
  * PricingCurrencyListUnitPrice MUST be denominated in the PricingCurrency.
  * The product of PricingCurrencyListUnitPrice, [PricingQuantity](#pricingquantity), and [PricingToBillingExchangeRate](#pricingtobillingexchangerate) MUST match the [ListCost](#listcost) when PricingQuantity is not null and ChargeClass is not "Correction".
  * Discrepancies in PricingCurrencyListUnitPrice, ListCost, or PricingQuantity MAY be addressed independently when ChargeClass is "Correction".

## Column ID

PricingCurrencyListUnitPrice

## Display Name

Pricing Currency List Unit Price

## Description

The suggested provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts and expressed in Pricing Currency.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Content Constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column type     | Metric                               |
| Feature level   | Conditional                          |
| Allows nulls    | True                                 |
| Data type       | Decimal                              |
| Value format    | [Numeric Format](#numericformat)     |
| Number range    | Any valid non-negative decimal value |

## Introduced (version)

1.2
