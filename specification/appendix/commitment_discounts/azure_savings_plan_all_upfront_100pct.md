# Azure Savings Plan - All Upfront - 100% Utilization

| Parameter                    | Value              |
| ---------------------------- | ------------------ |
| Scenario Type                | commitment         |
| Payment Model                | All Upfront        |
| Commitment Discount Category | Spend              |
| Utilization                  | 100%               |
| Hours Generated              | 24                 |
| Annual Commitment            | &dollar;462,002.40 |
| List Unit Price              | &dollar;79.11/hour |

[CSV Example](/specification/data/commitment_discount_scenarios/azure_savings_plan_all_upfront_100pct.csv)

## Scenario Description

This example shows a **Microsoft Azure Compute Savings Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost             | EffectiveCost        |
| ---------------- | ----- | ---------------------- | -------------------- |
| Purchase         | 1     | &dollar;462,002.40     | &dollar;0.00         |
| Usage (Used)     | 24    | &dollar;0.00           | &dollar;1,265.76     |
| Usage (Standard) | 3     | &dollar;9.21           | &dollar;9.21         |
| **Total**        | 28    | **&dollar;462,011.61** | **&dollar;1,274.97** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value              |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)          |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)         |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 52.74 (USD)                |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a &dollar;52.74/hour commitment, this value is &dollar;52.74.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered | Standard      |
| ----------------------- | ------------------------ | ------------------ | ------------- |
| **ListUnitPrice**       | List (public) unit price | &dollar;79.11      | &dollar;3.07  |
| **ContractedUnitPrice** | Negotiated unit price    | &dollar;79.11      | &dollar;3.07  |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario         | BilledCost         | EffectiveCost | ListCost           |
| ---------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row** | &dollar;462,002.40 | &dollar;0.00  | &dollar;462,002.40 |
| **Used Row**     | &dollar;0.00       | &dollar;52.74 | &dollar;79.11      |
| **Standard Row** | &dollar;3.07       | &dollar;3.07  | &dollar;3.07       |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Standard pricing rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                     | Value                                 | Explanation                                                 |
| -------------------------- | ------------------------------------- | ----------------------------------------------------------- |
| ChargeCategory             | Purchase                              | Commitment purchase transaction                             |
| ChargeFrequency            | One-Time                              | One-time upfront payment                                    |
| BilledCost                 | &dollar;462,002.40                    | Full annual commitment payment                              |
| EffectiveCost              | &dollar;0.00                          | **MUST be 0** - cost is amortized to usage rows             |
| PricingQuantity            | 1                                     | One commitment unit purchased                               |
| CommitmentDiscountStatus   | null                                  | Status only applies to usage rows                           |
| CommitmentDiscountQuantity | 462,002.40                            | Full annual commitment (&dollar;52.74/hr &times; 8,760 hrs) |
| CommitmentDiscountUnit     | USD                                   | Unit of commitment capacity (spend-based)                   |
| SkuId                      | Azure-EASTUS-COMPUTE-PURCHASE         | Commitment purchase SKU                                     |
| SkuPriceId                 | Azure-EASTUS-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase                            |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                                |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| ChargeCategory             | Usage                                                 | Compute resource consumption               |
| PricingCategory            | Committed                                             | Priced under commitment discount           |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment      |
| EffectiveCost              | &dollar;52.74                                         | Amortized cost (annual / hours)            |
| ListCost                   | &dollar;79.11                                         | What you would have paid at list price     |
| PricingQuantity            | 1                                                     | Units priced                               |
| ConsumedQuantity           | 1                                                     | Hours used                                 |
| CommitmentDiscountQuantity | 52.74                                                 | Hourly commitment spend applied            |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                         |
| CommitmentDiscountId       | /subscriptions/f0e9d8c7-b6a5-4321-0987-654321fedcb... | Links usage to purchase                    |
| SkuId                      | Azure-EASTUS-COMPUTE-USAGE                            | Resource usage SKU (differs from Purchase) |
| SkuPriceId                 | Azure-EASTUS-COMPUTE-USAGE-COMMITTED                  | Price point for committed usage            |

## Standard Pricing Usage Row Details

| Column                     | Value                                  | Explanation                                   |
| -------------------------- | -------------------------------------- | --------------------------------------------- |
| ChargeCategory             | Usage                                  | Compute consumption (standard pricing)        |
| PricingCategory            | Standard                               | No discount applied                           |
| BilledCost                 | &dollar;3.07                           | Same as ListCost, no negotiation/commitments  |
| EffectiveCost              | &dollar;3.07                           | Same as BilledCost, no pre/post payments      |
| ListCost                   | &dollar;3.07                           | Public, non-negotiated cost                   |
| PricingQuantity            | 1                                      | Units priced                                  |
| ConsumedQuantity           | 1                                      | Hours consumed                                |
| CommitmentDiscountQuantity | null                                   | **No commitment applied**                     |
| CommitmentDiscountStatus   | null                                   | No commitment                                 |
| CommitmentDiscountId       | null                                   | No associated commitment                      |
| ContractedUnitPrice        | &dollar;3.07                           | Equals ListUnitPrice (no negotiated discount) |
| SkuId                      | Azure-EASTUS-COMPUTE-ONDEMAND          | Standard (on-demand) resource SKU             |
| SkuPriceId                 | Azure-EASTUS-COMPUTE-ONDEMAND-STANDARD | Price point for standard pricing              |
