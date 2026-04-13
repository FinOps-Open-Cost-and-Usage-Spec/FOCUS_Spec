# Azure Reservation - All Upfront - 100% Utilization

| Parameter                    | Value              |
| ---------------------------- | ------------------ |
| Scenario Type                | commitment         |
| Payment Model                | All Upfront        |
| Commitment Discount Category | Usage              |
| Utilization                  | 100%               |
| Hours Generated              | 24                 |
| Annual Commitment            | $358,021.20 |
| List Unit Price              | $61.31/hour |

[CSV Example](/specification/data/commitment_discount_scenarios/azure_reservation_all_upfront_100pct.csv)

## Scenario Description

This example shows a **Microsoft Azure Virtual Machine Reserved Instance**, which is a commitment (with a Commitment Discount Category of `Usage`) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they are covered by the commitment.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost             | EffectiveCost        |
| ---------------- | ----- | ---------------------- | -------------------- |
| Purchase         | 1     | $358,021.20     | $0.00         |
| Usage (Used)     | 24    | $0.00           | $980.88       |
| **Total**        | 25    | **$358,021.20** | **$980.88**   |

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

| Column                  | Purpose                  | Commitment-Covered |
| ----------------------- | ------------------------ | ------------------ |
| **ListUnitPrice**       | List (public) unit price | $61.31      |
| **ContractedUnitPrice** | Negotiated unit price    | $61.31      |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario         | BilledCost         | EffectiveCost | ListCost           |
| ---------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row** | $358,021.20 | $0.00  | $358,021.20 |
| **Used Row**     | $0.00       | $40.87 | $61.31      |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

## Purchase Row Details

| Column                     | Value                                 | Explanation                                                                           |
| -------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------- |
| ChargeCategory             | Purchase                              | Commitment purchase transaction                                                       |
| ChargeFrequency            | One-Time                              | One-time upfront payment                                                              |
| BilledCost                 | $358,021.20                    | Full annual commitment payment                                                        |
| EffectiveCost              | $0.00                          | **must be 0** - cost is amortized to usage rows                                       |
| PricingQuantity            | 1                                     | One commitment unit purchased                                                         |
| CommitmentDiscountStatus   | null                                  | Status only applies to usage rows                                                     |
| CommitmentDiscountQuantity | 8760.00                               | Total commitment capacity for the 1-year term (1 instance-hr/hr &times; 8,760 hrs/yr) |
| CommitmentDiscountUnit     | Hours                                 | Unit of commitment capacity (usage-based)                                             |
| SkuId                      | Azure-EASTUS-COMPUTE-PURCHASE         | Commitment purchase SKU                                                               |
| SkuPriceId                 | Azure-EASTUS-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase                                                      |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                                |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| ChargeCategory             | Usage                                                 | Compute resource consumption               |
| PricingCategory            | Committed                                             | Priced under commitment discount           |
| BilledCost                 | $0.00                                          | **must be 0** - covered by commitment      |
| EffectiveCost              | $40.87                                         | Amortized cost (annual / hours)            |
| ListCost                   | $61.31                                         | What you would have paid at list price     |
| PricingQuantity            | 1                                                     | Units priced                               |
| ConsumedQuantity           | 1                                                     | Hours used                                 |
| CommitmentDiscountQuantity | 1                                                     | Commitment units applied                   |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                         |
| CommitmentDiscountId       | /subscriptions/f0e9d8c7-b6a5-4321-0987-654321fedcb... | Links usage to purchase                    |
| SkuId                      | Azure-EASTUS-COMPUTE-USAGE                            | Resource usage SKU (differs from Purchase) |
| SkuPriceId                 | Azure-EASTUS-COMPUTE-USAGE-COMMITTED                  | Price point for committed usage            |
