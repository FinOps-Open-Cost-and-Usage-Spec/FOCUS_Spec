# AWS Reserved Instance - Partial Upfront - 100% Utilization

| Parameter                    | Value              |
| ---------------------------- | ------------------ |
| Scenario Type                | commitment         |
| Payment Model                | Partial Upfront    |
| Commitment Discount Category | Usage              |
| Utilization                  | 100%               |
| Hours Generated              | 24                 |
| Annual Commitment            | &dollar;440,014.80 |
| List Unit Price              | &dollar;75.35/hour |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_reserved_instance_partial_upfront_100pct.csv)

## Scenario Description

This example shows an **Amazon Web Services EC2 Reserved Instance**, which is a commitment (with a Commitment Discount Category of `Usage`) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **Partial Upfront** payment option combines an initial upfront payment with a reduced recurring monthly fee. This results in two Purchase rows: one One-Time for the upfront portion and one Recurring for the monthly fee, both with zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost             | EffectiveCost        |
| ---------------- | ----- | ---------------------- | -------------------- |
| Purchase         | 2     | &dollar;236,884.68     | &dollar;0.00         |
| Usage (Used)     | 24    | &dollar;0.00           | &dollar;1,205.52     |
| Usage (Standard) | 3     | &dollar;11.52          | &dollar;11.52        |
| **Total**        | 29    | **&dollar;236,896.20** | **&dollar;1,217.04** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value        |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)    |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)   |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 1 (commitment units) |

**For usage-based commitments:** CommitmentDiscountQuantity represents the quantity of resources (e.g., instance hours), not a dollar amount. For a 1-hour reservation, CommitmentDiscountQuantity = 1.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered | Standard      |
| ----------------------- | ------------------------ | ------------------ | ------------- |
| **ListUnitPrice**       | List (public) unit price | &dollar;75.35      | &dollar;3.84  |
| **ContractedUnitPrice** | Negotiated unit price    | &dollar;75.35      | &dollar;3.84  |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario                     | BilledCost         | EffectiveCost | ListCost           |
| ---------------------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row (One-Time)**  | &dollar;220,007.40 | &dollar;0.00  | &dollar;220,007.40 |
| **Purchase Row (Recurring)** | &dollar;16,877.28  | &dollar;0.00  | &dollar;16,877.28  |
| **Used Row**                 | &dollar;0.00       | &dollar;50.23 | &dollar;75.35      |
| **Standard Row**             | &dollar;3.84       | &dollar;3.84  | &dollar;3.84       |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Standard pricing rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                   | Value              | Explanation                                     |
| ------------------------ | ------------------ | ----------------------------------------------- |
| ChargeCategory           | Purchase           | Commitment purchase transaction                 |
| ChargeFrequency          | One-Time           | One-time upfront payment                        |
| BilledCost               | &dollar;220,007.40 | Upfront portion (50% of annual commitment)      |
| EffectiveCost            | &dollar;0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                  | One commitment unit purchased                   |
| CommitmentDiscountStatus | null               | Status only applies to usage rows               |

## Recurring Purchase Row Details

| Column                   | Value             | Explanation                                                |
| ------------------------ | ----------------- | ---------------------------------------------------------- |
| ChargeCategory           | Purchase          | Commitment purchase transaction                            |
| ChargeFrequency          | Recurring         | Monthly recurring fee                                      |
| BilledCost               | &dollar;16,877.28 | Monthly portion (hourly rate / 2 &times; 672 hours in Feb) |
| EffectiveCost            | &dollar;0.00      | **MUST be 0** - cost is amortized to usage rows            |
| PricingQuantity          | 1                 | One commitment unit purchased                              |
| CommitmentDiscountStatus | null              | Status only applies to usage rows                          |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                            |
| -------------------------- | ----------------------------------------------------- | -------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption           |
| PricingCategory            | Committed                                             | Priced under commitment discount       |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment  |
| EffectiveCost              | &dollar;50.23                                         | Amortized cost (annual / hours)        |
| ListCost                   | &dollar;75.35                                         | What you would have paid at list price |
| PricingQuantity            | 1                                                     | Units priced                           |
| ConsumedQuantity           | 1                                                     | Hours used                             |
| CommitmentDiscountQuantity | 1                                                     | Commitment units applied               |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                     |
| CommitmentDiscountId       | arn:aws:ec2:us-east-1:123456789012:reserved-instan... | Links usage to purchase                |

## Standard Pricing Usage Row Details

| Column                     | Value         | Explanation                                   |
| -------------------------- | ------------- | --------------------------------------------- |
| ChargeCategory             | Usage         | Compute consumption (standard pricing)        |
| PricingCategory            | Standard      | No discount applied                           |
| BilledCost                 | &dollar;3.84  | Same as ListCost, no negotiation/commitments  |
| EffectiveCost              | &dollar;3.84  | Same as BilledCost, no pre/post payments      |
| ListCost                   | &dollar;3.84  | Public, non-negotiated cost                   |
| PricingQuantity            | 1             | Units priced                                  |
| ConsumedQuantity           | 1             | Hours consumed                                |
| CommitmentDiscountQuantity | null          | **No commitment applied**                     |
| CommitmentDiscountStatus   | null          | No commitment                                 |
| CommitmentDiscountId       | null          | No associated commitment                      |
| ContractedUnitPrice        | &dollar;3.84  | Equals ListUnitPrice (no negotiated discount) |
