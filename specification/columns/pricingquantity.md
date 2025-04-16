# Pricing Quantity

The Pricing Quantity represents the volume of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Pricing Unit](#pricingunit). Distinct from [Consumed Quantity](#consumedquantity) (complementary to [Consumed Unit](#consumedunit)), it focuses on pricing and cost, not *resource* and *service* consumption.

The PricingQuantity column adheres to the following requirements:

* PricingQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PricingQuantity MUST be of type Decimal.
* PricingQuantity MUST conform to [NumericFormat](#numericformat) requirements.
* PricingQuantity nullability is defined as follows:
  * PricingQuantity MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * PricingQuantity MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * PricingQuantity MAY be null in all other cases.
* When PricingQuantity is not null, PricingQuantity adheres to the following additional requirements:
  * PricingQuantity MUST be a valid decimal value.
  * The product of PricingQuantity and a unit price (e.g., [ContractedUnitPrice](#contractedunitprice)) MUST match the corresponding cost metric (e.g., [ContractedCost](#contractedcost)) when the unit price is not null and ChargeClass is not "Correction".
* Discrepancies in PricingQuantity, unit prices (e.g., ContractedUnitPrice), or costs (e.g., ContractedCost) MAY exist when ChargeClass is "Correction".

## Column ID

PricingQuantity

## Display Name

Pricing Quantity

## Description

The volume of a given SKU associated with a *resource* or *service* used or purchased, based on the Pricing Unit.

## Usability Constraints

### Aggregation

When aggregating Pricing Quantity for specific use case scenarios, it's important to exclude certain types of charges to avoid double counting. Specifically, principal charges (defined as the original charge that is amortized over time across multiple other charges, with the [Amortization Class](#amortizationclass) set to "Principal") or amortized charges (representing the results of amortization from a previous charge, with the Amortization Class set to "Amortized Charge"). Both of these charges specify Pricing Quantity, so including both would lead to double counting.

In the case of a [commitment discount](#glossary:commitment-discount), principal charges typically refer to Charge Category "Purchase" charges (both one-time and recurring) that are paid to cover future eligible charges, along with their related Charge Category "Tax" charges. Amortized charges, on the other hand, correspond to Charge Category "Usage" records that are covered by these purchases.

## Content Constraints

|    Constraint   |      Value                |
|:----------------|:--------------------------|
| Column type     | Metric                    |
| Feature level   | Mandatory                 |
| Allows nulls    | True                      |
| Data type       | Decimal                   |
| Value format    | [Numeric Format](#numericformat) |
| Number Range    | Any valid decimal value   |

## Introduced (version)

1.0-preview
