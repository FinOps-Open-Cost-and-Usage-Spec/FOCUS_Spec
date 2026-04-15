# Aura Web Flexible Spend Plan - All Upfront - 50% Utilization

| Parameter                    | Value               |
| ---------------------------- | ------------------- |
| Scenario Type                | commitment          |
| Payment Model                | All Upfront         |
| Commitment Discount Category | Spend               |
| Utilization                  | 50%                 |
| Hours Generated              | 24                  |
| Annual Commitment            | $693,003.60  |
| List Unit Price              | $118.67/hour |

[CSV Example](/specification/data/commitment_discount_scenarios/aura_web_flexible_spend_plan_all_upfront_50pct.csv)

## Scenario Description

This example shows an **Aura Web Flexible Spend Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **underutilization** at 50% where only 12 of 24 commitment hours are consumed. The remaining 12 hours appear as 'Unused' rows with CommitmentDiscountStatus='Unused'. These unused rows still have EffectiveCost to reflect the wasted commitment value.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost             | EffectiveCost        |
| ---------------- | ----- | ---------------------- | -------------------- |
| Purchase         | 1     | $693,003.60     | $0.00         |
| Usage (Used)     | 12    | $0.00           | $949.32       |
| Usage (Unused)   | 12    | $0.00           | $949.32       |
| **Total**        | 25    | **$693,003.60** | **$1,898.64** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value              |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)          |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)         |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 79.11 (USD)                |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a $79.11/hour commitment, this value is $79.11.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered |
| ----------------------- | ------------------------ | ------------------ |
| **ListUnitPrice**       | List (public) unit price | $118.67     |
| **ContractedUnitPrice** | Negotiated unit price    | $118.67     |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario         | BilledCost         | EffectiveCost | ListCost           |
| ---------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row** | $693,003.60 | $0.00  | $693,003.60 |
| **Used Row**     | $0.00       | $79.11 | $118.67     |
| **Unused Row**   | $0.00       | $79.11 | $79.11      |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.
* **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.

## Purchase Row Details

| Column                     | Value                                | Explanation                                                 |
| -------------------------- | ------------------------------------ | ----------------------------------------------------------- |
| ChargeCategory             | Purchase                             | Commitment purchase transaction                             |
| ChargeFrequency            | One-Time                             | One-time upfront payment                                    |
| BilledCost                 | $693,003.60                   | Full annual commitment payment                              |
| EffectiveCost              | $0.00                         | **must be 0** - cost is amortized to usage rows             |
| PricingQuantity            | 693,003.60                           | Total commitment in USD (PricingUnit = USD)                 |
| CommitmentDiscountStatus   | null                                 | Status only applies to usage rows                           |
| CommitmentDiscountQuantity | 693,003.60                           | Full annual commitment ($79.11/hr &times; 8,760 hrs) |
| CommitmentDiscountUnit     | USD                                  | Unit of commitment capacity (spend-based)                   |
| SkuId                      | AURAWEB-USEAST1-COMPUTE-PURCHASE         | Commitment purchase SKU                                     |
| SkuPriceId                 | AURAWEB-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase                            |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                                |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| ChargeCategory             | Usage                                                 | Compute resource consumption               |
| PricingCategory            | Committed                                             | Priced under commitment discount           |
| BilledCost                 | $0.00                                          | **must be 0** - covered by commitment      |
| EffectiveCost              | $79.11                                         | Amortized cost (annual / hours)            |
| ListCost                   | $118.67                                        | What you would have paid at list price     |
| PricingQuantity            | 1                                                     | Units priced                               |
| ConsumedQuantity           | 1                                                     | Hours used                                 |
| CommitmentDiscountQuantity | 79.11                                                 | Hourly commitment spend applied            |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                         |
| CommitmentDiscountId       | auraweb:flexspend::123456789012:flexspendplan/fsp-... | Links usage to purchase                    |
| SkuId                      | AURAWEB-USEAST1-COMPUTE-USAGE                             | Resource usage SKU (differs from Purchase) |
| SkuPriceId                 | AURAWEB-USEAST1-COMPUTE-USAGE-COMMITTED                   | Price point for committed usage            |

## Unused Commitment Row Details

| Column                     | Value                                                          | Explanation                                        |
| -------------------------- | -------------------------------------------------------------- | -------------------------------------------------- |
| ChargeCategory             | Usage                                                          | Represents commitment capacity                     |
| BilledCost                 | $0.00                                                   | No additional billing (already paid at purchase)   |
| EffectiveCost              | $79.11                                                  | **Wasted value** - lost commitment                 |
| PricingQuantity            | 79.11                                                          | Hourly commitment in USD (PricingUnit = USD)       |
| ListCost                   | $79.11                                                  | $1.00 &times; 79.11 USD                     |
| ConsumedQuantity           | null                                                           | **No resource consumed**                           |
| CommitmentDiscountQuantity | 79.11                                                          | Commitment wasted                                  |
| CommitmentDiscountStatus   | Unused                                                         | Commitment not utilized                            |
| ResourceId                 | auraweb:flexspend::123456789012:flexspendplan/fsp-abc123def456 | must equal CommitmentDiscountId (no resource used) |
| ResourceName               | Compute Flexible Spend Plan                                      | Carried from Purchase row (no resource consumed)   |
| ResourceType               | Commitment                                                     | Carried from Purchase row (no resource consumed)   |
| SkuId                      | AURAWEB-USEAST1-COMPUTE-PURCHASE                                   | must match Purchase row (no resource consumed)     |
| SkuPriceId                 | AURAWEB-USEAST1-COMPUTE-PURCHASE-UPFRONT                           | must match Purchase row                            |

For spend-based unused rows, PricingUnit is USD and PricingQuantity is the hourly commitment amount. ListCost = ListUnitPrice ($1.00) &times; PricingQuantity, which equals the wasted commitment dollars per hour.
