---
dataset: CostAndUsage
---

# Aura Web Resource Reservation - All Upfront - 100% Utilization

| Parameter                    | Value              |
| ---------------------------- | ------------------ |
| Scenario Type                | commitment         |
| Payment Model                | All Upfront        |
| Commitment Discount Category | Usage              |
| Utilization                  | 100%               |
| Hours Generated              | 24                 |
| Annual Commitment            | $402,960.00 |
| List Unit Price              | $69.00/hour |

[CSV Example](/specification/data/commitment_discount_scenarios/aura_web_resource_reservation_all_upfront_100pct.csv)

## Scenario Description

This example shows an **Aura Web Resource Reservation**, which is a commitment (with a [Commitment Discount Category](#col) of `Usage`) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full [BilledCost](#col) and zero [EffectiveCost](#col) (since the cost is amortized to usage rows).

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have [CommitmentDiscountStatus](#col)='Used', indicating the commitment was fully applied. [BilledCost](#col)=0 on usage rows because they're covered by the commitment.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost             | EffectiveCost        |
| ---------------- | ----- | ---------------------- | -------------------- |
| Purchase         | 1     | $402,960.00     | $0.00         |
| Usage (Used)     | 24    | $0.00           | $1,104.00     |
| **Total**        | 25    | **$402,960.00** | **$1,104.00** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: Pricing Quantity vs. Consumed Quantity vs. Commitment Discount Quantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value        |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)    |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)   |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 1 (commitment units) |

**For usage-based commitments:** [CommitmentDiscountQuantity](#col) represents the quantity of resources (e.g., instance hours), not a dollar amount. For a 1-hour reservation, [CommitmentDiscountQuantity](#col) = 1.

### Pricing Columns: List Unit Price vs. Contracted Unit Price

| Column                  | Purpose                  | Commitment-Covered |
| ----------------------- | ------------------------ | ------------------ |
| **ListUnitPrice**       | List (public) unit price | $69.00      |
| **ContractedUnitPrice** | Negotiated unit price    | $69.00      |

**Why this matters:** [ContractedUnitPrice](#col) reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, [ContractedUnitPrice](#col) equals [ListUnitPrice](#col). Commitment discount savings are reflected in [EffectiveCost](#col), not in unit prices.

### Cost Columns: Billed Cost vs. Effective Cost vs. List Cost

| Scenario         | BilledCost         | EffectiveCost | ListCost           |
| ---------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row** | $402,960.00 | $0.00  | $402,960.00 |
| **Used Row**     | $0.00       | $46.00 | $69.00      |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

## Purchase Row Details

| Column                     | Value                                                    | Explanation                                                                           |
| -------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| ChargeCategory             | Purchase                                                 | Commitment purchase transaction                                                       |
| ChargeFrequency            | One-Time                                                 | One-time upfront payment                                                              |
| BilledCost                 | $402,960.00                                              | Full annual commitment payment                                                        |
| EffectiveCost              | $0.00                                                    | **must be 0** - cost is amortized to usage rows                                       |
| PricingQuantity            | 1                                                        | One commitment unit purchased                                                         |
| CommitmentDiscountStatus   | null                                                     | Status only applies to usage rows                                                     |
| CommitmentDiscountQuantity | 8760.00                                                  | Total commitment capacity for the 1-year term (1 instance-hr/hr &times; 8,760 hrs/yr) |
| CommitmentDiscountUnit     | Hours                                                    | Unit of commitment capacity (usage-based)                                             |
| SkuId                      | AURAWEB-USEAST1-COMPUTE-PURCHASE                         | Commitment purchase SKU                                                               |
| SkuPriceId                 | AURAWEB-USEAST1-COMPUTE-RESERVATION-PURCHASE-ALL-UPFRONT | Price point for the all upfront purchase fee                                          |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                     | Explanation                                                       |
| -------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------- |
| ChargeCategory             | Usage                                                     | Compute resource consumption                                      |
| PricingCategory            | Committed                                                 | Priced under commitment discount                                  |
| BilledCost                 | $0.00                                                     | **must be 0** - covered by commitment                             |
| EffectiveCost              | $46.00                                                    | Amortized cost (annual / hours)                                   |
| ListCost                   | $69.00                                                    | What you would have paid at list price                            |
| PricingQuantity            | 1                                                         | Units priced                                                      |
| ConsumedQuantity           | 1                                                         | Hours used                                                        |
| CommitmentDiscountQuantity | 1                                                         | Commitment units applied                                          |
| CommitmentDiscountStatus   | Used                                                      | Commitment applied                                                |
| CommitmentDiscountId       | auraweb:compute:us-east-1:123456789012:resource-reserv... | Links usage to purchase                                           |
| SkuId                      | AURAWEB-USEAST1-COMPUTE-USAGE                             | Resource usage SKU (differs from Purchase)                        |
| SkuPriceId                 | AURAWEB-USEAST1-COMPUTE-USAGE-RESERVATION-ALL-UPFRONT     | Price point for committed usage under the all upfront reservation |
