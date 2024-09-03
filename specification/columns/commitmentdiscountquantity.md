# Commitment Discount Quantity

Commitment Discount Quantity is the amount of a [*commitment discount*](#commitment-discount) purchased or accounted for in *commitment discount* related [*rows*](#glossary:row). The amounts are denominated in [*Commitment Discount Units*](#glossary:commitmentdiscountunit). For a purchase, the Commitment Discount Quantity is either the total of *Commitment Discount Units* over a *commitment discount's* [*term*](#glossary:term) or the apportioned amount for the [*charge period*](#glossary:chargeperiod). For committed usage, the Commitment Discount Quantity is either the number of *Commitment Discount Units* consumed by a [*row*](glossary:#row) that is covered by a *commitment discount* or is the unused portion of a *commitment discount* over a *charge period*. The CommitmentDiscountQuantity column only applies to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount). Commitment Discount Quantity is commonly used in commitment discount analysis and optimization use cases.

For usage-based *commitment discounts* (i.e. when *CommitmentDiscountCategory* is "Usage"), the Commitment Discount Quantity reflects the amount of resource hours consumed. If *size-flexibility* is applicable, this amount is further multiplied by a pre-determined, SKU attribute called an *instance type ratio*, to produce a normalized quantity based on [*resource's*](#glossary:resource) [*instance-size*](#glossary:instance-size). *Size-flexibility* allows a usage-based *commitment discount* to cover less expensive SKUs with smaller *instance type ratios*, or conversely, partially cover a more expensive SKU with a larger *instance type ratio*.

Commitment Discount Quantity is commonly used in commitment discount analysis and optimization use cases. For purchases, the Commitment Discount Quantity helps customers track how many total *Commitment Discount Units* are available across *commitment discounts* at various points in time, and for committed usage, it helps customers track how efficiently their *commitment discounts* apply to their workloads. The *commitment discount's* utilization rate is used to measure this efficiency and can be derived by dividing the used portion of CommitmentDiscountQuantity by the sum of CommitmentDiscountQuantity for the *charge period*. With this information, customers can analyze their existing *commitment discount* strategy to make more informed decisions on additional purchases.

**Important:** When aggregating Commitment Discount Quantity for utilization calculations, it's important to exclude *commitment discount* purchases (i.e. when *ChargeCategory* is "Purchase") that are paid to cover future eligible charges (e.g., *Commitment Discount*). This exclusion helps prevent double counting of these quantities in the aggregation.

The CommitmentDiscountQuantity column adheres to the following requirements:

* CommitmentDiscountQuantity MUST be present a FOCUS dataset when the provider supports *commitment discounts*.
* CommitmentDiscountQuantity MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* CommitmentDiscountQuantity MAY be negative if [*ChargeClass*](#chargeclass) is "Correction".

In cases where the *ChargeCategory* is "Purchase" and [*CommitmentDiscountId*](#commitmentdiscountid) is not null, the following applies:

* When [*ChargeFrequency*](#chargefrequency) is "One-Time", and *CommitmentDiscountId* is not null, CommitmentDiscountQuantity MUST be the positive quantity of *CommitmentDiscountUnits*, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term*.
* When *ChargeFrequency* is "Recurring", and *CommitmentDiscountId* is not null, CommitmentDiscountQuantity MUST be the positive quantity of *CommitmentDiscountUnits* that is eligible for consumption for each *charge period* that corresponds with the purchase.

In cases where the *ChargeCategory* is "Usage" and *CommitmentDiscountId* is not null, the following applies:

* When *CommitmentDiscountStatus* is "Used", and *ChargeClass* is not "Correction", CommitmentDiscountQuantity MUST be the positive, metered quantity of *CommitmentDiscountUnits* that is consumed over the *row's* *charge period*.
* When *CommitmentDiscountStatus* is "Unused", and *ChargeClass* is not "Correction", CommitmentDiscountQuantity MUST be the remaining, positive, unused quantity of *CommitmentDiscountUnits* for the *row's* *charge period*.

In cases where the *CommitmentDiscountUnit* are present, the following applies:

* When the [*CommitmentDiscountCategory*](#commitmentdiscountcategory) is "Usage", where *size-flexibility* is applicable for the commitment discount, the CommitmentDiscountUnit SHOULD be "Normalized Hours". If *size-flexibility* is not applicable, CommitmentDiscountUnit SHOULD be "Hours".
* When the *CommitmentDiscountCategory* is "Spend", the CommitmentDiscountUnit SHOULD match the [*BillingCurrency*](#billingcurrency).

CommitmentDiscountQuantity MUST be null for all other *ChargeCategory* values.

## Column ID

CommitmentDiscountQuantity

## Display Name

Commitment Discount Quantity

## Description

The amount of a *commitment discount* purchased or accounted for in *commitment discount* related *rows*.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | Decimal          |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.1
