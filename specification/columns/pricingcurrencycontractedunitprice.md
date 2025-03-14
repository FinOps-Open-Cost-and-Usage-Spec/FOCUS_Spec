# Pricing Currency Contracted Unit Price

The Pricing Currency Contracted Unit Price represents the agreed-upon unit price for a single [Pricing Unit](#pricingunit) of the associated SKU, inclusive of [*negotiated discounts*](#glossary:negotiated-discount), if present, while excluding negotiated [*commitment discounts*](#glossary:commitment-discount) or any other discounts. This price is denominated in the [Pricing Currency](#pricingcurrency). The Pricing Currency Contracted Unit Price is commonly used for calculating savings based on negotiation activities. If negotiated discounts are not applicable, the Pricing Currency Contracted Unit Price defaults to the [Pricing Currency List Unit Price](#pricingcurrencylistunitprice).

The PricingCurrencyContractedUnitPrice column adheres to the following requirements:

* PricingCurrencyContractedUnitPrice presence in a [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
  * PricingCurrencyContractedUnitPrice MUST be present in a FOCUS dataset when the provider presents prices in a virtual currency (e.g. credits, tokens).
  * PricingCurrencyContractedUnitPrice MUST be present in a FOCUS dataset when the provider presents prices and bills in different national currencies (e.g. priced in USD and billed in EUR).
  * PricingCurrencyContractedUnitPrice MAY be present in a FOCUS dataset in all other cases.
* PricingCurrencyContractedUnitPrice adheres to the following additional requirements:
* PricingCurrencyContractedUnitPrice MUST be of type Decimal.
* PricingCurrencyContractedUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
* PricingCurrencyContractedUnitPrice nullability is defined as follows:
  * PricingCurrencyContractedUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * PricingCurrencyContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * PricingCurrencyContractedUnitPrice MAY be null in all other cases.
* When PricingCurrencyContractedUnitPrice is not null, PricingCurrencyContractedUnitPrice adheres to the following additional requirements:
  * PricingCurrencyContractedUnitPrice MUST be a non-negative decimal value.
  * PricingCurrencyContractedUnitPrice MUST be denominated in the BillingCurrency.
  * The product of PricingCurrencyContractedUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ContractedCost](#contractedcost) when PricingQuantity is not null and ChargeClass is not "Correction".
* Discrepancies in PricingCurrencyContractedUnitPrice, ContractedCost, or PricingQuantity MAY be addressed independently when ChargeClass is "Correction".

## Column ID

PricingCurrencyContractedUnitPrice

## Display Name

Pricing Currency Contracted Unit Price

## Description

The agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of negotiated discounts, if present, while excluding negotiated commitment discounts or any other discounts, and expressed in Pricing Currency.

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

1.0
