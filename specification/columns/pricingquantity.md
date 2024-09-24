# Pricing Quantity

The Pricing Quantity represents the volume of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Pricing Unit](#pricingunit). Distinct from [Consumed Quantity](#consumedquantity) (complementary to [Consumed Unit](#consumedunit)), it focuses on pricing and cost, not *resource* and *service* consumption.

Important: When aggregating Pricing Quantity for savings calculations, it's important to exclude either one-time or recurring charges (Charge Category "Purchase") that are paid to cover future eligible charges (e.g., Commitment Discount) or the covered charges themselves. This exclusion helps prevent double counting of these units in the aggregation. Which set of units to exclude depends on whether units are aggregated on a billed basis (exclude covered charges) or accrual basis (exclude Purchases for future charges). For instance, units categorized as Charge Category "Purchase" and their related Charge Category "Tax" charges for a Commitment Discount might be excluded from an accrual basis cost aggregation of List Cost. This is because the "Usage" and "Tax" charge records provided during the term of the commitment discount already specify the Pricing Quantity. Purchase units that cover future eligible units can be identified by filtering for Charge Category "Purchase" records with a Billed Cost greater than 0 and an Effective Cost equal to 0.

The PricingQuantity column MUST be present in a FOCUS dataset. This column MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements. The value MAY be negative in cases where [ChargeClass](#chargeclass) is "Correction". This column MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory. When unit prices are not null, multiplying PricingQuantity by a unit price MUST produce a result equal to the corresponding cost metric, except in cases of ChargeClass "Correction", which may address PricingQuantity or any cost discrepancies independently.

## Column ID

PricingQuantity

## Display Name

Pricing Quantity

## Description

The volume of a given SKU associated with a *resource* or *service* used or purchased, based on the Pricing Unit.

## Content constraints

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
