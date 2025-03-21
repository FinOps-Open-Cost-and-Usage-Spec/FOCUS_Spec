# Commitment Discount Cost

Commitment Discount Cost represents the cost calculated by multiplying the [*commitment discount unit price*](#glossary:commitment-discount-unit-price) and the corresponding [Pricing Quantity](#pricingquantity). Commitment Discount Cost is denominated in the [Billing Currency](#billingcurrency) and is commonly used to calculate the discounted cost of [*commitment discount's*](#glossary:commitment-discount) purchase or resource utilizing the *commitment discount*.

The CommitmentDiscountCost column adheres to the following requirements:

* The CommitmentDiscountCost column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountCost MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency.
* CommitmentDiscountCost MUST be present when [*CommitmentDiscountId*](#glossary:commitmentdiscountid) is present.
* When [CommitmentDiscountUnitPrice](#commitmentdiscountunitprice) is present and not null, multiplying the CommitmentDiscountUnitPrice by PricingQuantity MUST produce the CommitmentDiscountCost, except in cases of [ChargeClass](#chargeclass) "Correction", which may address PricingQuantity or any cost discrepancies independently.
* [*BilledCost*](#billedcost) MUST match CommitmentDiscountCost inclusive of any negotiated discounts (i.e. `CommitmentDiscountCost - (CommitmentDiscountCost - ContractedCost)`) when [Charge Category](#chargecategory) is "Purchase" and [*ChargeClass*](#chargeclass) is not "Correction".
* [*EffectiveCost*](#billedcost) MUST match CommitmentDiscountCost inclusive of any negotiated discounts (i.e. `CommitmentDiscountCost - (CommitmentDiscountCost - ContractedCost)`) when [Charge Category](#chargecategory) is "Usage" and [*ChargeClass*](#chargeclass) is not "Correction".
* CommitmentDiscountCost MAY be null or any valid decimal value if [*ChargeClass*](#chargeclass) is "Correction".

## Column ID

CommitmentDiscountCost

## Display Name

Commitment Discount Cost

## Description

Cost calculated by multiplying Commitment Discount Unit Price and the corresponding Pricing Quantity.

## Usability Constraints

**Aggregation:** When aggregating Commitment Discount Cost for commitment utilization calculations, it's important to exclude *commitment discount* purchases (i.e. when ChargeCategory is "Purchase") that are paid to cover future eligible charges (e.g., *commitment discount*). Otherwise, when accounting for all upfront or accrued purchases, it's important to exclude *commitment discount* usage (i.e. when ChargeCategory is "Usage"). This exclusion helps prevent double counting of these quantities in the aggregation.

## Content Constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Metric           |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | Decimal          |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.2
