# Commitment Discount Cost

Commitment Discount Cost represents the cost calculated by multiplying the [Commitment Discount Unit Price](#glossary:commitmentdiscountunitprice) and the corresponding [Pricing Quantity](#pricingquantity). Commitment Discount Cost is denominated in the [Billing Currency](#billingcurrency) and is commonly used to calculate savings incurred by [*commitment discounts*](#commitment-discount).

The CommitmentDiscountCost column adheres to the following requirements:

* CommitmentDiscountCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountCost MUST be of type Decimal.
* CommitmentDiscountCost MUST conform to [Numeric Format](#numericformat) requirements.
* CommitmentDiscountCost MUST be denominated in the *BillingCurrency*.
* CommitmentDiscountCost MUST be present when [*CommitmentDiscountId*](#glossary:commitmentdiscountid) is present.
* CommitmentDiscountCost MUST equal [*PricingQuantity*](#pricingquantity) * ([*CommitmentDiscountUnitPrice*](#commitmentdiscountunitprice) - ([*ListUnitPrice*](#listunitprice) - [*ContractedUnitPrice*](#contractedunitprice))).
* [*BilledCost*](#billedcost) MUST equal CommitmentDiscountCost when [*ChargeCategory*](#chargecategory) is "Purchase" and *ChargeClass* is not "Correction".
* [*EffectiveCost*](#billedcost) MUST equal CommitmentDiscountCost when *ChargeCategory* is "Usage" and *ChargeClass* is not "Correction".
* CommitmentDiscountCost MAY be null or any valid decimal value if *ChargeClass* is "Correction".

When [*CommitmentDiscountCategory*](#commitmentdiscountcategory) is "Spend" and *ChargeClass* is not "Correction", the following applies:

* When [*ChargeCategory*](#chargecategory)] is "Purchase", CommitmentDiscountCost MUST be the predefined amount of spend committed for each [*charge period*](glossary:chargeperiod) of the *commitment discount's* [*term*].
* When *ChargeCategory* is "Usage", CommitmentDiscountUnitPrice MUST be the [*effective unit price*](glossary:effective-unit-price) of the covering resource's SKU.

When *CommitmentDiscountCategory* is "Usage" and *ChargeClass* is not "Correction", the following applies:

* CommitmentDiscountUnitPrice MUST be the *effective unit price* of the preselected SKU.
* When [*commitment discount flexibility*](glossary:commitment-discount-flexibility) applies, the CommitmentDiscountCost of the covering resource's SKU MAY be calculated from a different *CommitmentDiscountUnitPrice* than the purchasing SKU.
* When *commitment discount flexibility* does not apply, the CommitmentDiscountCost of the covering resource's SKU MUST be calculated from the same *CommitmentDiscountUnitPrice* as the purchasing SKU.

## Column ID

CommitmentDiscountCost

## Display Name

Commitment Discount Cost

## Description

Cost calculated by multiplying Commitment Discount Unit Price and the corresponding Pricing Quantity.

## Usability Constraints

**Aggregation:** When aggregating Commitment Discount Cost for savings calculations, it's important to exclude *commitment discount* purchases (i.e. when *ChargeCategory* is "Purchase") that are paid to cover future eligible charges (e.g., *commitment discount*). Otherwise, when accounting for all upfront or accrued purchases, it's important to exclude *commitment discount* usage (i.e. when *ChargeCategory* is "Usage"). This exclusion helps prevent double counting of these quantities in the aggregation.

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
