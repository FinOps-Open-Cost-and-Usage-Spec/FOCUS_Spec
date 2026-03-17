# AWS Savings Plan - All Upfront - 100% Utilization

| Parameter                    | Value               |
| ---------------------------- | ------------------- |
| Scenario Type                | commitment          |
| Payment Model                | All Upfront         |
| Commitment Discount Category | Spend               |
| Utilization                  | 100%                |
| Hours Generated              | 24                  |
| Annual Commitment            | &dollar;628,004.40  |
| List Unit Price              | &dollar;107.54/hour |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_savings_plan_all_upfront_100pct.csv)

## Scenario Description

This example shows an **Amazon Web Services EC2 Instance Savings Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost             | EffectiveCost        |
| ---------------- | ----- | ---------------------- | -------------------- |
| Purchase         | 1     | &dollar;628,004.40     | &dollar;0.00         |
| Usage (Used)     | 24    | &dollar;0.00           | &dollar;1,720.56     |
| **Total**        | 25    | **&dollar;628,004.40** | **&dollar;1,720.56** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value              |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)          |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)         |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 71.69 (USD)                |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a &dollar;71.69/hour commitment, this value is &dollar;71.69.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered |
| ----------------------- | ------------------------ | ------------------ |
| **ListUnitPrice**       | List (public) unit price | &dollar;107.54     |
| **ContractedUnitPrice** | Negotiated unit price    | &dollar;107.54     |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario         | BilledCost         | EffectiveCost | ListCost           |
| ---------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row** | &dollar;628,004.40 | &dollar;0.00  | &dollar;628,004.40 |
| **Used Row**     | &dollar;0.00       | &dollar;71.69 | &dollar;107.54     |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

## Purchase Row Details

| Column                     | Value                                | Explanation                                                 |
| -------------------------- | ------------------------------------ | ----------------------------------------------------------- |
| ChargeCategory             | Purchase                             | Commitment purchase transaction                             |
| ChargeFrequency            | One-Time                             | One-time upfront payment                                    |
| BilledCost                 | &dollar;628,004.40                   | Full annual commitment payment                              |
| EffectiveCost              | &dollar;0.00                         | **must be 0** - cost is amortized to usage rows             |
| PricingQuantity            | 628,004.40                           | Total commitment in USD (PricingUnit = USD)                 |
| CommitmentDiscountStatus   | null                                 | Status only applies to usage rows                           |
| CommitmentDiscountQuantity | 628,004.40                           | Full annual commitment (&dollar;71.69/hr &times; 8,760 hrs) |
| CommitmentDiscountUnit     | USD                                  | Unit of commitment capacity (spend-based)                   |
| SkuId                      | AWS-USEAST1-COMPUTE-PURCHASE         | Commitment purchase SKU                                     |
| SkuPriceId                 | AWS-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase                            |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                                |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| ChargeCategory             | Usage                                                 | Compute resource consumption               |
| PricingCategory            | Committed                                             | Priced under commitment discount           |
| BilledCost                 | &dollar;0.00                                          | **must be 0** - covered by commitment      |
| EffectiveCost              | &dollar;71.69                                         | Amortized cost (annual / hours)            |
| ListCost                   | &dollar;107.54                                        | What you would have paid at list price     |
| PricingQuantity            | 1                                                     | Units priced                               |
| ConsumedQuantity           | 1                                                     | Hours used                                 |
| CommitmentDiscountQuantity | 71.69                                                 | Hourly commitment spend applied            |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                         |
| CommitmentDiscountId       | arn:aws:savingsplans::123456789012:savingsplan/sp-... | Links usage to purchase                    |
| SkuId                      | AWS-USEAST1-COMPUTE-USAGE                             | Resource usage SKU (differs from Purchase) |
| SkuPriceId                 | AWS-USEAST1-COMPUTE-USAGE-COMMITTED                   | Price point for committed usage            |
