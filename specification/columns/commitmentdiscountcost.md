# Commitment Discount Cost

Commitment Discount Cost represents the cost calculated by multiplying the [Commitment Discount Unit Price](#glossary:commitmentdiscountunitprice) and the corresponding [Pricing Quantity](#pricingquantity) inclusive of any [*negotiated discounts*](#glossary:negotated-discount) that may apply. Commitment Discount Cost is denominated in the [Billing Currency](#billingcurrency) and is commonly used to calculate savings incurred by [*commitment discounts*](#commitment-discount).

The CommitmentDiscountCost column adheres to the following requirements:

* CommitmentDiscountCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountCost MUST be of type Decimal.
* CommitmentDiscountCost MUST conform to [Numeric Format](#numericformat) requirements.
* CommitmentDiscountCost MUST be denominated in the *BillingCurrency*.
* CommitmentDiscountCost MUST be present when [*CommitmentDiscountId*](#glossary:commitmentdiscountid) is present.
* CommitmentDiscountCost MUST equal [*PricingQuantity*](#pricingquantity) * ([*CommitmentDiscountUnitPrice*](#commitmentdiscountunitprice) - ([*ListUnitPrice*](#listunitprice) - [*ContractedUnitPrice*](#contractedunitprice))).
* CommitmentDiscountCost MUST equal the [*covering cost*](#glossary:coveringcost) for all [*rows*](#glossary:row) of the same [*charge period*](#glossary:chargeperiod) and [*CommitmentDiscountID*](#commitmentdiscountid) before any applicable [*negotiated discounts*](#glossary:negotiateddiscount) when [*ChargeCategory*](#chargecategory) is "Usage", [*PricingCategory*](#pricingcategory) is "Committed", and [*ChargeClass*](#chargeclass) is not "Correction".
* CommitmentDiscountCost MAY equal the *covering cost* before any applicable *negotiated discounts* when [*ChargeCategory*](#chargecategory) is "Purchase", depending on the payment schedule of the *commitment discount*.
* [*BilledCost*](#billedcost) MUST equal CommitmentDiscountCost when [*ChargeCategory*](#chargecategory) is "Purchase" and *ChargeClass* is not "Correction".
* [*EffectiveCost*](#billedcost) MUST equal CommitmentDiscountCost when *ChargeCategory* is "Usage" and *ChargeClass* is not "Correction".
* CommitmentDiscountCost MAY be null or any valid decimal value if *ChargeClass* is "Correction".

When a provider supports [*commitment discount flexibility*](glossary:commitment-discount-flexibility) for a [*CommitmentDiscountType*](#commitmentdiscounttype) and *ChargeClass* is not "Correction", the following applies:

* When *commitment discount flexibility* applies, the CommitmentDiscountCost of the covering resource's [*SkuId*](#skuid) MAY be calculated from a different *CommitmentDiscountUnitPrice* than the purchasing *SkuId*.
* When *commitment discount flexibility* does not apply, the CommitmentDiscountCost of the covering resource's *SkuId* MUST be calculated from the same *CommitmentDiscountUnitPrice* as the purchasing *SkuId*.

## Column ID

CommitmentDiscountCost

## Display Name

Commitment Discount Cost

## Description

Cost calculated by multiplying Commitment Discount Unit Price and the corresponding Pricing Quantity inclusive of any *negotiated discounts* that may apply.

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
