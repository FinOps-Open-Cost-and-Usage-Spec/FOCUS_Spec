# CrestNode Resource Reservation - No Upfront - 100% Utilization

| Parameter                    | Value               |
| ---------------------------- | ------------------- |
| Scenario Type                | commitment          |
| Payment Model                | No Upfront          |
| Commitment Discount Category | Usage               |
| Utilization                  | 100%                |
| Hours Generated              | 24                  |
| Annual Commitment            | $664,008.00  |
| List Unit Price              | $113.70/hour |

[CSV Example](/specification/data/commitment_discount_scenarios/crestnode_resource_reservation_no_upfront_100pct.csv)

## Scenario Description

This example shows a **CrestNode Resource Reservation**, which is a commitment (with a Commitment Discount Category of `Usage`) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **No Upfront** payment option means you pay nothing at purchase time and instead pay a recurring monthly fee. This results in a recurring Purchase row each billing period with BilledCost equal to the monthly fee and zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost            | EffectiveCost        |
| ---------------- | ----- | --------------------- | -------------------- |
| Purchase         | 1     | $55,334.00     | $0.00         |
| Usage (Used)     | 24    | $0.00          | $1,819.20     |
| **Total**        | 25    | **$55,334.00** | **$1,819.20** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value        |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)    |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)   |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 1 (commitment units) |

**For usage-based commitments:** CommitmentDiscountQuantity represents the quantity of resources (e.g., instance hours), not a dollar amount. For a 1-hour reservation, CommitmentDiscountQuantity = 1.

### Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered |
| ----------------------- | ------------------------ | ------------------ |
| **ListUnitPrice**       | List (public) unit price | $113.70     |
| **ContractedUnitPrice** | Negotiated unit price    | $113.70     |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario         | BilledCost        | EffectiveCost | ListCost          |
| ---------------- | ----------------- | ------------- | ----------------- |
| **Purchase Row** | $55,334.00 | $0.00  | $55,334.00 |
| **Used Row**     | $0.00      | $75.80 | $113.70    |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

## Purchase Row Details

| Column                     | Value                                 | Explanation                                                    |
| -------------------------- | ------------------------------------- | -------------------------------------------------------------- |
| ChargeCategory             | Purchase                              | Commitment purchase transaction                                |
| ChargeFrequency            | Recurring                             | Monthly recurring fee                                          |
| BilledCost                 | $55,334.00                     | Monthly recurring payment (annual / 12)                        |
| EffectiveCost              | $0.00                          | **must be 0** - cost is amortized to usage rows                |
| PricingQuantity            | 1                                     | One commitment unit purchased                                  |
| CommitmentDiscountStatus   | null                                  | Status only applies to usage rows                              |
| CommitmentDiscountQuantity | 672.00                                | Commitment capacity for Feb (1 instance-hr/hr &times; 672 hrs) |
| CommitmentDiscountUnit     | Hours                                 | Unit of commitment capacity (usage-based)                      |
| SkuId                      | CRESTNODE-EASTUS-COMPUTE-PURCHASE            | Commitment purchase SKU                                        |
| SkuPriceId                 | CRESTNODE-EASTUS-COMPUTE-PURCHASE-MONTHLY    | Price point for recurring purchase                             |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                                |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| ChargeCategory             | Usage                                                 | Compute resource consumption               |
| PricingCategory            | Committed                                             | Priced under commitment discount           |
| BilledCost                 | $0.00                                          | **must be 0** - covered by commitment      |
| EffectiveCost              | $75.80                                         | Amortized cost (annual / hours)            |
| ListCost                   | $113.70                                        | What you would have paid at list price     |
| PricingQuantity            | 1                                                     | Units priced                               |
| ConsumedQuantity           | 1                                                     | Hours used                                 |
| CommitmentDiscountQuantity | 1                                                     | Commitment units applied                   |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                         |
| CommitmentDiscountId       | crestnode:compute:eastus:f0e9d8c7-b6a5-4321-0987-654321...   | Links usage to purchase                    |
| SkuId                      | CRESTNODE-EASTUS-COMPUTE-USAGE                               | Resource usage SKU (differs from Purchase) |
| SkuPriceId                 | CRESTNODE-EASTUS-COMPUTE-USAGE-COMMITTED                     | Price point for committed usage            |
