# LatticeScale Dynamic Compute Commitment - No Upfront - 100% Utilization

| Parameter                    | Value              |
| ---------------------------- | ------------------ |
| Scenario Type                | commitment         |
| Payment Model                | No Upfront         |
| Commitment Discount Category | Spend              |
| Utilization                  | 100%               |
| Hours Generated              | 24                 |
| Annual Commitment            | $553,018.80 |
| List Unit Price              | $94.70/hour |

[CSV Example](/specification/data/commitment_discount_scenarios/latticescale_dynamic_compute_commitment_no_upfront_100pct.csv)

## Scenario Description

This example shows a **LatticeScale Dynamic Compute Commitment**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **No Upfront** payment option means you pay nothing at purchase time and instead pay a recurring monthly fee. LatticeScale commitments are billed monthly with no upfront payment option. This results in a recurring Purchase row each billing period with BilledCost equal to the monthly fee and zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost            | EffectiveCost        |
| ---------------- | ----- | --------------------- | -------------------- |
| Purchase         | 1     | $42,423.36     | $0.00         |
| Usage (Used)     | 24    | $0.00          | $1,515.12     |
| **Total**        | 25    | **$42,423.36** | **$1,515.12** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs. ConsumedQuantity vs. CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value              |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)          |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)         |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 63.13 (USD)                |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a $63.13/hour commitment, this value is $63.13.

### Pricing Columns: ListUnitPrice vs. ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered |
| ----------------------- | ------------------------ | ------------------ |
| **ListUnitPrice**       | List (public) unit price | $94.70      |
| **ContractedUnitPrice** | Negotiated unit price    | $94.70      |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs. EffectiveCost vs. ListCost

| Scenario         | BilledCost        | EffectiveCost | ListCost          |
| ---------------- | ----------------- | ------------- | ----------------- |
| **Purchase Row** | $42,423.36 | $0.00  | $42,423.36 |
| **Used Row**     | $0.00      | $63.13 | $94.70     |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

## Purchase Row Details

| Column                     | Value                                   | Explanation                                                    |
| -------------------------- | --------------------------------------- | -------------------------------------------------------------- |
| ChargeCategory             | Purchase                                | Commitment purchase transaction                                |
| ChargeFrequency            | Recurring                               | Monthly recurring fee                                          |
| BilledCost                 | $42,423.36                       | Monthly fee (hourly rate &times; 672 hours in Feb)             |
| EffectiveCost              | $0.00                            | **must be 0** - cost is amortized to usage rows                |
| PricingQuantity            | 42,423.36                               | Total commitment in USD (PricingUnit = USD)                    |
| CommitmentDiscountStatus   | null                                    | Status only applies to usage rows                              |
| CommitmentDiscountQuantity | 42,423.36                               | Commitment capacity for Feb ($63.13/hr &times; 672 hrs) |
| CommitmentDiscountUnit     | USD                                     | Unit of commitment capacity (spend-based)                      |
| SkuId                      | LATTICESCALE-USCENTRAL1-COMPUTE-PURCHASE         | Commitment purchase SKU                                        |
| SkuPriceId                 | LATTICESCALE-USCENTRAL1-COMPUTE-PURCHASE-MONTHLY | Price point for recurring purchase                             |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                                |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| ChargeCategory             | Usage                                                 | Compute resource consumption               |
| PricingCategory            | Committed                                             | Priced under commitment discount           |
| BilledCost                 | $0.00                                          | **must be 0** - covered by commitment      |
| EffectiveCost              | $63.13                                         | Amortized cost (annual / hours)            |
| ListCost                   | $94.70                                         | What you would have paid at list price     |
| PricingQuantity            | 1                                                     | Units priced                               |
| ConsumedQuantity           | 1                                                     | Hours used                                 |
| CommitmentDiscountQuantity | 63.13                                                 | Hourly commitment spend applied            |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                         |
| CommitmentDiscountId       | latticescale:compute:us-central1:proj-123456:commitment-dis... | Links usage to purchase                    |
| SkuId                      | LATTICESCALE-USCENTRAL1-COMPUTE-USAGE                          | Resource usage SKU (differs from Purchase) |
| SkuPriceId                 | LATTICESCALE-USCENTRAL1-COMPUTE-USAGE-COMMITTED                | Price point for committed usage            |
