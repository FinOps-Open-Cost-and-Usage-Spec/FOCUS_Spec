# Pricing Quantity

The Pricing Quantity represents the volume of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Pricing Unit](#pricingunit). Distinct from [Consumed Quantity](#consumedquantity) (complementary to [Consumed Unit](#consumedunit)), it focuses on pricing and cost, not *resource* and *service* consumption.

---
The PricingQuantity column adheres to the following requirements:

* PricingQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PricingQuantity MUST be of type Decimal.
* PricingQuantity MUST conform to [Numeric Format](#numericformat) requirements.
* If [ChargeCategory](#chargecategory) is "Tax", PricingQuantity adheres to the following additional requirement:
  * PricingQuantity MUST be null.
* Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", PricingQuantity adheres to the following additional requirement:
  * PricingQuantity MUST NOT be null.
* Else PricingQuantity adheres to the following additional requirement:
  * PricingQuantity MAY be null.
* If PricingQuantity is not null, PricingQuantity adheres to the following additional requirements:
  * PricingQuantity MUST be a valid decimal value.
  * The product of PricingQuantity and a unit price (e.g., [ListUnitPrice](#listunitprice)) MUST match the corresponding cost metric (e.g., [ListCost](#contractedcost)) when unit prices are not null and ChargeClass is not "Correction".
  * The product of PricingQuantity and a unit price (e.g., ListUnitPrice) MAY deviate from the corresponding cost metric (e.g., ListCost) when ChargeClass is "Correction" and discrepancies in PricingQuantity, unit prices, or costs are addressed independently.

---

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

**Aggregation:** When aggregating Pricing Quantity for commitment utilization calculations, it's important to exclude *commitment discount* purchases (i.e. when *ChargeCategory* is "Purchase") that are paid to cover future eligible charges (e.g., *Commitment Discount*). Otherwise, when accounting for all upfront or accrued purchases, it's important to exclude *commitment discount* usage (i.e. when *ChargeCategory* is "Usage"). This exclusion helps prevent double counting of these quantities in the aggregation.

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
