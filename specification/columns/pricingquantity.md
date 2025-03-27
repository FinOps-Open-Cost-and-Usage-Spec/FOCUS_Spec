# Pricing Quantity

The Pricing Quantity represents the volume of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Pricing Unit](#pricingunit). Distinct from [Consumed Quantity](#consumedquantity) (complementary to [Consumed Unit](#consumedunit)), it focuses on pricing and cost, not *resource* and *service* consumption.

The PricingQuantity column adheres to the following requirements:

* The PricingQuantity column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* The value MAY be negative in cases where [ChargeClass](#chargeclass) is "Correction".
* This column MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.
* When unit prices (e.g. [ContractedUnitPrice](#contractedunitprice)) are not null, multiplying PricingQuantity by a unit price MUST produce a result equal to the corresponding cost metric (e.g. [ContractedCost](#contractedcost)), except in cases of ChargeClass "Correction", which may address PricingQuantity or any cost discrepancies independently.

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
