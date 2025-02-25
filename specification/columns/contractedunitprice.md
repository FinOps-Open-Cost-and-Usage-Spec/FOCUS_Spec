# Contracted Unit Price

The Contracted Unit Price represents the agreed-upon unit price for a single [Pricing Unit](#pricingunit) of the associated SKU, inclusive of [*negotiated discounts*](#glossary:negotiated-discount), if present, while excluding negotiated [*commitment discounts*](#glossary:commitment-discount) or any other discounts. This price is denominated in the [Billing Currency](#billingcurrency). The Contracted Unit Price is commonly used for calculating savings based on negotiation activities. If negotiated discounts are not applicable, the Contracted Unit Price defaults to the [List Unit Price](#listunitprice).

The ContractedUnitPrice column adheres to the following requirements:

* ContractedUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports negotiated pricing concepts.
* ContractedUnitPrice adheres to the following additional requirements:
* ContractedUnitPrice MUST be of type Decimal.
* ContractedUnitPrice MUST conform to [Numeric Format](#numericformat) requirements.
* ContractedUnitPrice nullability is defined as follows:
  * ContractedUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * ContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* When ContractedUnitPrice is not null, ContractedUnitPrice adheres to the following additional requirements:
  * ContractedUnitPrice MUST be a non-negative decimal value.
  * ContractedUnitPrice MUST be denominated in the BillingCurrency.
  * The product of ContractedUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ContractedCost](#contractedcost) when PricingQuantity is not null and ChargeClass is not "Correction".
* Discrepancies in ContractedUnitPrice, ContractedCost, or PricingQuantity MAY be addressed independently when ChargeClass is "Correction".

## Column ID

ContractedUnitPrice

## Display Name

Contracted Unit Price

## Description

The agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of negotiated discounts, if present, while excluding negotiated commitment discounts or any other discounts.

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
