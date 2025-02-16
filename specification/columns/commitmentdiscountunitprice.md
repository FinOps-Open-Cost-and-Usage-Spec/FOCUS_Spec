# Commitment Discount Unit Price

Commitment Discount Unit Price represents the [*covering cost*](#glossary:coveringcost) of the associated [*commitment discount's*](#glossary:commitmentdiscount) purchase or discounted unit price of a utilizing resource's [Sku Id](#skuid) before any applicable [*negotiated discounts*](#negotiated-discount]). This price is denominated in the [Billing Currency](#billingcurrency) and is commonly used to calculate the discounted cost of a purchase or resource utilizing the *commitment discount*.

The CommitmentDiscountUnitPrice column adheres to the following requirements:

* CommitmentDiscountUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountUnitPrice MUST be a Decimal within the range of non-negative decimal values.
* CommitmentDiscountUnitPrice MUST conform to [Numeric Format](#numericformat) requirements.
* CommitmentDiscountUnitPrice MUST be denominated in the [*BillingCurrency*](#billingcurrency).
* CommitmentDiscountUnitPrice MUST be present when [*CommitmentDiscountId*](#commitmentdiscountid) is present.
* CommitmentDiscountUnitPrice MUST NOT include *negotiated discounts*
* CommitmentDiscountUnitPrice MAY be null or any valid decimal value if [*ChargeClass*](#chargeclass) is "Correction".

When [*CommitmentDiscountCategory*](#commitmentdiscountcategory) is "Spend", *ChargeClass* is not "Correction", and before any applicable *negotiated discounts*, the following applies:

* When [*ChargeCategory*](#chargecategory) is "Purchase", CommitmentDiscountUnitPrice MUST equal the *covering cost* associated with the *commitment discount*.
* When *ChargeCategory* is "Usage", [*CommitmentDiscountCost*](#commitmentdiscountcost) across all [*rows*](#glossary:row) of the same [*charge period*](#glossary:chargeperiod) and [*CommitmentDiscountId*](#commitmentdiscountid) MUST equal the *covering cost* associated with the *commitment discount*.

When *CommitmentDiscountCategory* is "Usage", *ChargeClass* is not "Correction", and before any applicable *negotiated discounts*, the following applies:

* CommitmentDiscountUnitPrice MUST equal the *covering cost* of the preselected [*SkuId*](#skuid).
* When *commitment discount flexibility* applies, the CommitmentDiscountUnitPrice of the covering resource's *SkuId* MAY be different than the purchasing *SkuId*.
* When [*commitment discount flexibility*](glossary:commitment-discount-flexibility) does not apply, the CommitmentDiscountUnitPrice of the covering resource's *SkuId* MUST match the purchasing *SkuId*.

## Column ID

CommitmentDiscountUnitPrice

## Display Name

Commitment Discount Unit Price

## Description

The *covering cost* of the associated *commitment discount's* purchase or discounted unit price of a utilizing resource's *SkuId* before any *negotiated discounts* are applied.

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

1.2
