# Contracted Unit Price

The Contracted Unit Price represents the agreed-upon unit price for a single [Pricing Unit](#pricingunit) of the associated SKU, inclusive of [*negotiated discounts*](#glossary:negotiated-discount), if present, while excluding negotiated [*commitment discounts*](#glossary:commitment-discount) or any other discounts. This price is denominated in the [Billing Currency](#billingcurrency). The Contracted Unit Price is commonly used for calculating savings based on negotiation activities. If negotiated discounts are not applicable, the Contracted Unit Price defaults to the [List Unit Price](#listunitprice).

---
The ContractedUnitPrice column adheres to the following requirements:

* ContractedUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports negotiated pricing concepts.
* If present, ContractedUnitPrice adheres to the following additional requirements:
* ContractedUnitPrice MUST be of type Decimal.
* ContractedUnitPrice MUST conform to [Numeric Format](#numericformat) requirements.
  * If [ChargeCategory](#chargecategory) is "Tax", ContractedUnitPrice adheres to the following additional requirement:
    * ContractedUnitPrice MUST be null.
  * Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", ContractedUnitPrice adheres to the following additional requirement:
    * ContractedUnitPrice MUST NOT be null.
  * Else ContractedUnitPrice adheres to the following additional requirement:
    * ContractedUnitPrice MAY be null.
  * If ContractedUnitPrice is not null, ContractedUnitPrice adheres to the following additional requirements:
    * ContractedUnitPrice MUST be a non-negative decimal value.
    * ContractedUnitPrice MUST be denominated in the BillingCurrency.
    * The product of ContractedUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ContractedCost](#contractedcost) if PricingQuantity is not null and ChargeClass is not "Correction".
  * Discrepancies in ContractedUnitPrice, ContractedCost, or PricingQuantity MAY be addressed independently if ChargeClass is "Correction".

---
The ContractedUnitPrice column adheres to the following requirements:

* The ContractedUnitPrice column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports negotiated pricing concepts.
* This column MUST be a Decimal within the range of non-negative decimal values, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency.
* It MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.
* When ContractedUnitPrice is present and not null, multiplying ContractedUnitPrice by [PricingQuantity](#pricingquantity) MUST equal [ContractedCost](#contractedcost), except in cases of ChargeClass "Correction", which may address PricingQuantity or any cost discrepancies independently.

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
