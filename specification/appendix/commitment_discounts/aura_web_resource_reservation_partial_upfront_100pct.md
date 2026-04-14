# Aura Web Resource Reservation - Partial Upfront - 100% Utilization

| Parameter                    | Value              |
| ---------------------------- | ------------------ |
| Scenario Type                | commitment         |
| Payment Model                | Partial Upfront    |
| Commitment Discount Category | Usage              |
| Utilization                  | 100%               |
| Hours Generated              | 24                 |
| Annual Commitment            | $440,014.80 |
| List Unit Price              | $75.35/hour |

[CSV Example](/specification/data/commitment_discount_scenarios/aura_web_resource_reservation_partial_upfront_100pct.csv)

## Scenario Description

This example shows an **Aura Web Resource Reservation**, which is a commitment (with a Commitment Discount Category of `Usage`) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **Partial Upfront** payment option combines an initial upfront payment with a reduced recurring monthly fee. This results in two Purchase rows: one One-Time for the upfront portion and one Recurring for the monthly fee, both with zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost             | EffectiveCost        |
| ---------------- | ----- | ---------------------- | -------------------- |
| Purchase         | 2     | $236,884.68     | $0.00         |
| Usage (Used)     | 24    | $0.00           | $1,205.52     |
| **Total**        | 26    | **$236,884.68** | **$1,205.52** |

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
| **ListUnitPrice**       | List (public) unit price | $75.35      |
| **ContractedUnitPrice** | Negotiated unit price    | $75.35      |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., enterprise-negotiated rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario                     | BilledCost         | EffectiveCost | ListCost           |
| ---------------------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row (One-Time)**  | $220,007.40 | $0.00  | $220,007.40 |
| **Purchase Row (Recurring)** | $16,877.28  | $0.00  | $16,877.28  |
| **Used Row**                 | $0.00       | $50.23 | $75.35      |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` must be 0. Usage is covered by the commitment.

## Purchase Row Details

| Column                     | Value                                | Explanation                                                                          |
| -------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------ |
| ChargeCategory             | Purchase                             | Commitment purchase transaction                                                      |
| ChargeFrequency            | One-Time                             | One-time upfront payment                                                             |
| BilledCost                 | $220,007.40                   | Upfront portion (50% of annual commitment)                                           |
| EffectiveCost              | $0.00                         | **must be 0** - cost is amortized to usage rows                                      |
| PricingQuantity            | 1                                    | One commitment unit purchased                                                        |
| CommitmentDiscountStatus   | null                                 | Status only applies to usage rows                                                    |
| CommitmentDiscountQuantity | 8760.00                              | Full commitment capacity for the 1-year term (1 instance-hr/hr &times; 8,760 hrs/yr) |
| CommitmentDiscountUnit     | Hours                                | Unit of commitment capacity (usage-based)                                            |
| SkuId                      | AW-USEAST1-COMPUTE-PURCHASE         | Commitment purchase SKU                                                              |
| SkuPriceId                 | AW-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase                                                     |

## Recurring Purchase Row Details

| Column                     | Value                                  | Explanation                                                    |
| -------------------------- | -------------------------------------- | -------------------------------------------------------------- |
| ChargeCategory             | Purchase                               | Commitment purchase transaction                                |
| ChargeFrequency            | Recurring                              | Monthly recurring fee                                          |
| BilledCost                 | $16,877.28                      | Monthly portion (hourly rate / 2 &times; 672 hours in Feb)     |
| EffectiveCost              | $0.00                           | **must be 0** - cost is amortized to usage rows                |
| PricingQuantity            | 1                                      | One commitment unit purchased                                  |
| CommitmentDiscountStatus   | null                                   | Status only applies to usage rows                              |
| CommitmentDiscountQuantity | 672.00                                 | Commitment capacity for Feb (1 instance-hr/hr &times; 672 hrs) |
| CommitmentDiscountUnit     | Hours                                  | Unit of commitment capacity (usage-based)                      |
| SkuId                      | AW-USEAST1-COMPUTE-PURCHASE           | Commitment purchase SKU                                        |
| SkuPriceId                 | AW-USEAST1-COMPUTE-PURCHASE-RECURRING | Price point for recurring purchase                             |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                                |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| ChargeCategory             | Usage                                                 | Compute resource consumption               |
| PricingCategory            | Committed                                             | Priced under commitment discount           |
| BilledCost                 | $0.00                                          | **must be 0** - covered by commitment      |
| EffectiveCost              | $50.23                                         | Amortized cost (annual / hours)            |
| ListCost                   | $75.35                                         | What you would have paid at list price     |
| PricingQuantity            | 1                                                     | Units priced                               |
| ConsumedQuantity           | 1                                                     | Hours used                                 |
| CommitmentDiscountQuantity | 1                                                     | Commitment units applied                   |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                         |
| CommitmentDiscountId       | aw:compute:us-east-1:123456789012:resource-reserv... | Links usage to purchase                    |
| SkuId                      | AW-USEAST1-COMPUTE-USAGE                             | Resource usage SKU (differs from Purchase) |
| SkuPriceId                 | AW-USEAST1-COMPUTE-USAGE-COMMITTED                   | Price point for committed usage            |
