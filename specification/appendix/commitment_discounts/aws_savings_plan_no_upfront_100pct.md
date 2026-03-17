# AWS Savings Plan - No Upfront - 100% Utilization

| Parameter                    | Value              |
| ---------------------------- | ------------------ |
| Scenario Type                | commitment         |
| Payment Model                | No Upfront         |
| Commitment Discount Category | Spend              |
| Utilization                  | 100%               |
| Hours Generated              | 24                 |
| Annual Commitment            | &dollar;462,966.00 |
| List Unit Price              | &dollar;79.28/hour |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_savings_plan_no_upfront_100pct.csv)

## Scenario Description

This example shows an **Amazon Web Services EC2 Instance Savings Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **No Upfront** payment option means you pay nothing at purchase time and instead pay a recurring monthly fee. This results in a recurring Purchase row each billing period with BilledCost equal to the monthly fee and zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost            | EffectiveCost        |
| ---------------- | ----- | --------------------- | -------------------- |
| Purchase         | 1     | &dollar;35,515.20     | &dollar;0.00         |
| Usage (Used)     | 24    | &dollar;0.00          | &dollar;1,268.40     |
| Usage (Standard) | 3     | &dollar;11.52         | &dollar;11.52        |
| **Total**        | 28    | **&dollar;35,526.72** | **&dollar;1,279.92** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value              |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)          |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)         |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 52.85 (USD)                |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a &dollar;52.85/hour commitment, this value is &dollar;52.85.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered | Standard      |
| ----------------------- | ------------------------ | ------------------ | ------------- |
| **ListUnitPrice**       | List (public) unit price | &dollar;79.28      | &dollar;3.84  |
| **ContractedUnitPrice** | Negotiated unit price    | &dollar;79.28      | &dollar;3.84  |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario         | BilledCost        | EffectiveCost | ListCost          |
| ---------------- | ----------------- | ------------- | ----------------- |
| **Purchase Row** | &dollar;35,515.20 | &dollar;0.00  | &dollar;35,515.20 |
| **Used Row**     | &dollar;0.00      | &dollar;52.85 | &dollar;79.28     |
| **Standard Row** | &dollar;3.84      | &dollar;3.84  | &dollar;3.84      |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Standard pricing rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                     | Value                                | Explanation                                                      |
| -------------------------- | ------------------------------------ | ---------------------------------------------------------------- |
| ChargeCategory             | Purchase                             | Commitment purchase transaction                                  |
| ChargeFrequency            | Recurring                            | Monthly recurring fee                                            |
| BilledCost                 | &dollar;35,515.20                    | Monthly recurring payment (hourly rate &times; 672 hours in Feb) |
| EffectiveCost              | &dollar;0.00                         | **MUST be 0** - cost is amortized to usage rows                  |
| PricingQuantity            | 35,515.20                            | Total commitment in USD (PricingUnit = USD)                      |
| CommitmentDiscountStatus   | null                                 | Status only applies to usage rows                                |
| CommitmentDiscountQuantity | 35,515.20                            | Commitment capacity for Feb (&dollar;52.85/hr &times; 672 hrs)   |
| CommitmentDiscountUnit     | USD                                  | Unit of commitment capacity (spend-based)                        |
| SkuId                      | AWS-USEAST1-COMPUTE-PURCHASE         | Commitment purchase SKU                                          |
| SkuPriceId                 | AWS-USEAST1-COMPUTE-PURCHASE-MONTHLY | Price point for recurring purchase                               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                                |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| ChargeCategory             | Usage                                                 | Compute resource consumption               |
| PricingCategory            | Committed                                             | Priced under commitment discount           |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment      |
| EffectiveCost              | &dollar;52.85                                         | Amortized cost (annual / hours)            |
| ListCost                   | &dollar;79.28                                         | What you would have paid at list price     |
| PricingQuantity            | 1                                                     | Units priced                               |
| ConsumedQuantity           | 1                                                     | Hours used                                 |
| CommitmentDiscountQuantity | 52.85                                                 | Hourly commitment spend applied            |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                         |
| CommitmentDiscountId       | arn:aws:savingsplans::123456789012:savingsplan/sp-... | Links usage to purchase                    |
| SkuId                      | AWS-USEAST1-COMPUTE-USAGE                             | Resource usage SKU (differs from Purchase) |
| SkuPriceId                 | AWS-USEAST1-COMPUTE-USAGE-COMMITTED                   | Price point for committed usage            |

## Standard Pricing Usage Row Details

| Column                     | Value                                 | Explanation                                   |
| -------------------------- | ------------------------------------- | --------------------------------------------- |
| ChargeCategory             | Usage                                 | Compute consumption (standard pricing)        |
| PricingCategory            | Standard                              | No discount applied                           |
| BilledCost                 | &dollar;3.84                          | Same as ListCost, no negotiation/commitments  |
| EffectiveCost              | &dollar;3.84                          | Same as BilledCost, no pre/post payments      |
| ListCost                   | &dollar;3.84                          | Public, non-negotiated cost                   |
| PricingQuantity            | 1                                     | Units priced                                  |
| ConsumedQuantity           | 1                                     | Hours consumed                                |
| CommitmentDiscountQuantity | null                                  | **No commitment applied**                     |
| CommitmentDiscountStatus   | null                                  | No commitment                                 |
| CommitmentDiscountId       | null                                  | No associated commitment                      |
| ContractedUnitPrice        | &dollar;3.84                          | Equals ListUnitPrice (no negotiated discount) |
| SkuId                      | AWS-USEAST1-COMPUTE-ONDEMAND          | Standard (on-demand) resource SKU             |
| SkuPriceId                 | AWS-USEAST1-COMPUTE-ONDEMAND-STANDARD | Price point for standard pricing              |
