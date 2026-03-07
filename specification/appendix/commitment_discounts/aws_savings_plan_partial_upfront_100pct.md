# AWS Savings Plan - Partial Upfront - 100% Utilization

| Parameter                  | Value              |
| -------------------------- | ------------------ |
| Scenario Type              | commitment         |
| Payment Model              | Partial Upfront    |
| Commitment Discount Category | Spend              |
| Utilization                | 100%               |
| Hours Generated            | 24                 |
| Annual Commitment          | &dollar;242,666.67 |
| List Unit Price            | &dollar;76.71/hour |
| Savings                    | 33%                |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_savings_plan_partial_upfront_100pct.csv)

## Scenario Description

This example shows an **Amazon Web Services EC2 Instance Savings Plan**, which is a commitment (CommitmentDiscountCategory: Spend) where you commit to a specific dollar amount of usage per hour.

The **Partial Upfront** payment option combines an initial upfront payment with a reduced recurring monthly fee. This results in two Purchase rows: one One-Time for the upfront portion and one Recurring for the monthly fee, both with zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

| Row Type         | Count | BilledCost       | EffectiveCost  |
| ---------------- | ----- | ---------------------- | -------------------- |
| Purchase         | 2     | &dollar;242,666.67     | &dollar;0.00         |
| Usage (Used)     | 24    | &dollar;0.00           | &dollar;1,227.36     |
| Usage (Standard) | 12    | &dollar;19.27          | &dollar;19.27        |
| **Total**        | 38    | **&dollar;242,685.94** | **&dollar;1,246.63** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value        |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)    |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)   |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 1 (commitment units) |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a &dollar;51.14/hour commitment, this value is &dollar;51.14.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered | Standard      |
| ----------------------- | ------------------------ | ------------------ | ------------- |
| **ListUnitPrice**       | List (public) unit price | &dollar;76.71      | &dollar;76.71 |
| **ContractedUnitPrice** | Negotiated unit price    | &dollar;51.14      | null          |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario         | BilledCost         | EffectiveCost | ListCost           |
| ---------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row** | &dollar;242,666.67 | &dollar;0.00  | &dollar;242,666.67 |
| **Used Row**     | &dollar;0.00       | &dollar;51.14 | &dollar;76.71      |
| **Standard Row** | &dollar;5.38       | &dollar;5.38  | &dollar;5.38       |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.
* **Standard pricing rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                   | Value              | Explanation                                     |
| ------------------------ | ------------------ | ----------------------------------------------- |
| ChargeCategory           | Purchase           | Commitment purchase transaction                 |
| ChargeFrequency          | One-Time           | One-time upfront payment                        |
| BilledCost               | &dollar;224,000.00 | Portion of commitment payment                   |
| EffectiveCost            | &dollar;0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                  | One commitment unit purchased                   |
| CommitmentDiscountStatus | null               | Status only applies to usage rows               |

## Recurring Purchase Row Details

| Column                   | Value             | Explanation                                     |
| ------------------------ | ----------------- | ----------------------------------------------- |
| ChargeCategory           | Purchase          | Commitment purchase transaction                 |
| ChargeFrequency          | Recurring         | Monthly recurring fee                           |
| BilledCost               | &dollar;18,666.67 | Monthly portion of commitment payment           |
| EffectiveCost            | &dollar;0.00      | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                 | One commitment unit purchased                   |
| CommitmentDiscountStatus | null              | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                            |
| -------------------------- | ----------------------------------------------------- | -------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption           |
| PricingCategory            | Committed                                             | Priced under commitment discount       |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment  |
| EffectiveCost              | &dollar;51.14                                         | Amortized cost (annual / hours)        |
| ListCost                   | &dollar;76.71                                         | What you would have paid at list price |
| PricingQuantity            | 1                                                     | Units priced                           |
| ConsumedQuantity           | 1                                                     | Hours used                             |
| CommitmentDiscountQuantity | 51.14                                                 | Commitment dollars applied             |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                     |
| CommitmentDiscountId       | arn:aws:savingsplans::123456789012:savingsplan/sp-... | Links usage to purchase                |

## Standard Pricing Usage Row Details

| Column                     | Value         | Explanation                                   |
| -------------------------- | ------------- | --------------------------------------------- |
| ChargeCategory             | Usage         | Compute consumption (standard pricing)        |
| PricingCategory            | Standard      | No discount applied                           |
| BilledCost                 | &dollar;5.38  | List unit price                               |
| EffectiveCost              | &dollar;5.38  | = BilledCost                                  |
| ListCost                   | &dollar;5.38  | Same as BilledCost                            |
| PricingQuantity            | 234           | Units priced                                  |
| ConsumedQuantity           | 234           | Hours used                                    |
| CommitmentDiscountQuantity | null          | **No commitment applied**                     |
| CommitmentDiscountStatus   | null          | No commitment                                 |
| CommitmentDiscountId       | null       | No associated commitment                      |
| ContractedUnitPrice        | &dollar;76.71 | Equals ListUnitPrice (no negotiated discount) |
