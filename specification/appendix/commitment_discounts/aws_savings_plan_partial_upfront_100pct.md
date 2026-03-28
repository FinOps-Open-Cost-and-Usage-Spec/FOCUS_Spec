# AWS Savings Plan - Partial Upfront - 100% Utilization

| Parameter                    | Value              |
| ---------------------------- | ------------------ |
| Scenario Type                | commitment         |
| Payment Model                | Partial Upfront    |
| Commitment Discount Category | Spend              |
| Utilization                  | 100%               |
| Hours Generated              | 24                 |
| Annual Commitment            | &dollar;447,986.40 |
| List Unit Price              | &dollar;76.71/hour |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_savings_plan_partial_upfront_100pct.csv)

## Scenario Description

This example shows an **Amazon Web Services EC2 Instance Savings Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **Partial Upfront** payment option combines an initial upfront payment with a reduced recurring monthly fee. This results in two Purchase rows: one One-Time for the upfront portion and one Recurring for the monthly fee, both with zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost             | EffectiveCost        |
| ---------------- | ----- | ---------------------- | -------------------- |
| Purchase         | 2     | &dollar;241,176.24     | &dollar;0.00         |
| Usage (Used)     | 24    | &dollar;0.00           | &dollar;1,227.36     |
| **Total**        | 26    | **&dollar;241,176.24** | **&dollar;1,227.36** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value              |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)          |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)         |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 51.14 (USD)                |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a &dollar;51.14/hour commitment, this value is &dollar;51.14.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered |
| ----------------------- | ------------------------ | ------------------ |
| **ListUnitPrice**       | List (public) unit price | &dollar;76.71      |
| **ContractedUnitPrice** | Negotiated unit price    | &dollar;76.71      |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario                     | BilledCost         | EffectiveCost | ListCost           |
| ---------------------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row (One-Time)**  | &dollar;223,993.20 | &dollar;0.00  | &dollar;223,993.20 |
| **Purchase Row (Recurring)** | &dollar;17,183.04  | &dollar;0.00  | &dollar;17,183.04  |
| **Used Row**                 | &dollar;0.00       | &dollar;51.14 | &dollar;76.71      |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

## Purchase Row Details

| Column                     | Value                                | Explanation                                                                 |
| -------------------------- | ------------------------------------ | --------------------------------------------------------------------------- |
| ChargeCategory             | Purchase                             | Commitment purchase transaction                                             |
| ChargeFrequency            | One-Time                             | One-time upfront payment                                                    |
| BilledCost                 | &dollar;223,993.20                   | Upfront portion (50% of annual commitment)                                  |
| EffectiveCost              | &dollar;0.00                         | **must be 0** - cost is amortized to usage rows                             |
| PricingQuantity            | 223,993.20                           | Upfront portion in USD (PricingUnit = USD)                                  |
| CommitmentDiscountStatus   | null                                 | Status only applies to usage rows                                           |
| CommitmentDiscountQuantity | 447,986.40                           | Full annual commitment capacity (&dollar;51.14/hr &times; 8,760 hrs)        |
| CommitmentDiscountUnit     | USD                                  | Unit of commitment capacity (spend-based)                                   |
| SkuId                      | AWS-USEAST1-COMPUTE-PURCHASE         | Commitment purchase SKU                                                     |
| SkuPriceId                 | AWS-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase                                            |

## Recurring Purchase Row Details

| Column                     | Value                                  | Explanation                                                                |
| -------------------------- | -------------------------------------- | -------------------------------------------------------------------------- |
| ChargeCategory             | Purchase                               | Commitment purchase transaction                                            |
| ChargeFrequency            | Recurring                              | Monthly recurring fee                                                      |
| BilledCost                 | &dollar;17,183.04                      | Monthly portion (hourly rate / 2 &times; 672 hours in Feb)                 |
| EffectiveCost              | &dollar;0.00                           | **must be 0** - cost is amortized to usage rows                            |
| PricingQuantity            | 17,183.04                              | Monthly portion in USD (PricingUnit = USD)                                 |
| CommitmentDiscountStatus   | null                                   | Status only applies to usage rows                                          |
| CommitmentDiscountQuantity | 34,366.08                              | Full monthly commitment capacity (&dollar;51.14/hr &times; 672 hrs)        |
| CommitmentDiscountUnit     | USD                                    | Unit of commitment capacity (spend-based)                                  |
| SkuId                      | AWS-USEAST1-COMPUTE-PURCHASE           | Commitment purchase SKU                                                    |
| SkuPriceId                 | AWS-USEAST1-COMPUTE-PURCHASE-RECURRING | Price point for recurring purchase                                         |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                                |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| ChargeCategory             | Usage                                                 | Compute resource consumption               |
| PricingCategory            | Committed                                             | Priced under commitment discount           |
| BilledCost                 | &dollar;0.00                                          | **must be 0** - covered by commitment      |
| EffectiveCost              | &dollar;51.14                                         | Amortized cost (annual / hours)            |
| ListCost                   | &dollar;76.71                                         | What you would have paid at list price     |
| PricingQuantity            | 1                                                     | Units priced                               |
| ConsumedQuantity           | 1                                                     | Hours used                                 |
| CommitmentDiscountQuantity | 51.14                                                 | Hourly commitment spend applied            |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                         |
| CommitmentDiscountId       | arn:aws:savingsplans::123456789012:savingsplan/sp-... | Links usage to purchase                    |
| SkuId                      | AWS-USEAST1-COMPUTE-USAGE                             | Resource usage SKU (differs from Purchase) |
| SkuPriceId                 | AWS-USEAST1-COMPUTE-USAGE-COMMITTED                   | Price point for committed usage            |
