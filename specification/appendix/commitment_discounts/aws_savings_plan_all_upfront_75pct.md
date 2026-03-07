# AWS Savings Plan - All Upfront - 75% Utilization

| Parameter                  | Value              |
| -------------------------- | ------------------ |
| Scenario Type              | commitment         |
| Payment Model              | All Upfront        |
| Commitment Discount Category | Spend              |
| Utilization                | 75%                |
| Hours Generated            | 24                 |
| Annual Commitment          | &dollar;459,000.00 |
| List Unit Price            | &dollar;78.60/hour |
| Savings                    | 33%                |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_savings_plan_all_upfront_75pct.csv)

## Scenario Description

This example shows an **Amazon Web Services EC2 Instance Savings Plan**, which is a commitment (CommitmentDiscountCategory: Spend) where you commit to a specific dollar amount of usage per hour.

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **underutilization** at 75% where only 18 of 24 commitment hours are consumed. The remaining 6 hours appear as 'Unused' rows with CommitmentDiscountStatus='Unused'. These unused rows still have EffectiveCost to reflect the wasted commitment value.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost       | EffectiveCost  |
| ---------------- | ----- | ---------------------- | -------------------- |
| Purchase         | 1     | &dollar;459,000.00     | &dollar;0.00         |
| Usage (Used)     | 18    | &dollar;0.00           | &dollar;943.20       |
| Usage (Unused)   | 6     | &dollar;0.00           | &dollar;314.40       |
| Usage (Standard) | 12    | &dollar;10.15          | &dollar;10.15        |
| **Total**        | 37    | **&dollar;459,010.15** | **&dollar;1,267.75** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value        |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)    |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)   |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 1 (commitment units) |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a &dollar;52.40/hour commitment, this value is &dollar;52.40.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered | Standard      |
| ----------------------- | ------------------------ | ------------------ | ------------- |
| **ListUnitPrice**       | List (public) unit price | &dollar;78.60      | &dollar;78.60 |
| **ContractedUnitPrice** | Negotiated unit price    | &dollar;78.60      | &dollar;78.60 |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario         | BilledCost         | EffectiveCost | ListCost           |
| ---------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row** | &dollar;459,000.00 | &dollar;0.00  | &dollar;459,000.00 |
| **Used Row**     | &dollar;0.00       | &dollar;52.40 | &dollar;78.60      |
| **Unused Row**   | &dollar;0.00       | &dollar;52.40 | null               |
| **Standard Row** | &dollar;3.96       | &dollar;3.96  | &dollar;3.96       |

ListCost is null for unused rows because no resource was consumed. The opportunity cost is reflected in EffectiveCost.

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
| BilledCost               | &dollar;459,000.00 | Full annual commitment payment                  |
| EffectiveCost            | &dollar;0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                  | One commitment unit purchased                   |
| CommitmentDiscountStatus | null               | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                            |
| -------------------------- | ----------------------------------------------------- | -------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption           |
| PricingCategory            | Committed                                             | Priced under commitment discount       |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment  |
| EffectiveCost              | &dollar;52.40                                         | Amortized cost (annual / hours)        |
| ListCost                   | &dollar;78.60                                         | What you would have paid at list price |
| PricingQuantity            | 1                                                     | Units priced                           |
| ConsumedQuantity           | 1                                                     | Hours used                             |
| CommitmentDiscountQuantity | 52.40                                                 | Commitment dollars applied             |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                     |
| CommitmentDiscountId       | arn:aws:savingsplans::123456789012:savingsplan/sp-... | Links usage to purchase                |

## Unused Commitment Row Details

| Column                     | Value         | Explanation                                      |
| -------------------------- | ------------- | ------------------------------------------------ |
| ChargeCategory             | Usage         | Represents commitment capacity                   |
| BilledCost                 | &dollar;0.00  | No additional billing (already paid at purchase) |
| EffectiveCost              | &dollar;52.40 | **Wasted value** - lost commitment               |
| PricingQuantity            | 1             | Commitment units unused                          |
| ConsumedQuantity           | null          | **No resource consumed**                         |
| CommitmentDiscountQuantity | 52.40         | Commitment wasted                                |
| CommitmentDiscountStatus   | Unused        | Commitment not utilized                          |
| ResourceId                 | null       | No resource associated                           |

## Standard Pricing Usage Row Details

| Column                     | Value         | Explanation                                   |
| -------------------------- | ------------- | --------------------------------------------- |
| ChargeCategory             | Usage         | Compute consumption (standard pricing)        |
| PricingCategory            | Standard      | No discount applied                           |
| BilledCost                 | &dollar;3.96  | List unit price                               |
| EffectiveCost              | &dollar;3.96  | = BilledCost                                  |
| ListCost                   | &dollar;3.96  | Same as BilledCost                            |
| PricingQuantity            | 172           | Units priced                                  |
| ConsumedQuantity           | 172           | Hours used                                    |
| CommitmentDiscountQuantity | null          | **No commitment applied**                     |
| CommitmentDiscountStatus   | null          | No commitment                                 |
| CommitmentDiscountId       | null       | No associated commitment                      |
| ContractedUnitPrice        | &dollar;78.60 | Equals ListUnitPrice (no negotiated discount) |
