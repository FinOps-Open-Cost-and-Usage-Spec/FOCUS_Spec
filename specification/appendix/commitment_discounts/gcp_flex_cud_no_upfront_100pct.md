# GCP Flex CUD - No Upfront - 100% Utilization

| Parameter                    | Value              |
| ---------------------------- | ------------------ |
| Scenario Type                | commitment         |
| Payment Model                | No Upfront         |
| Commitment Discount Category | Spend              |
| Utilization                  | 100%               |
| Hours Generated              | 24                 |
| Annual Commitment            | &dollar;553,018.80 |
| List Unit Price              | &dollar;94.70/hour |

[CSV Example](/specification/data/commitment_discount_scenarios/gcp_flex_cud_no_upfront_100pct.csv)

## Scenario Description

This example shows a **Google Cloud Platform Spend-based CUD**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **No Upfront** payment option means you pay nothing at purchase time and instead pay a recurring monthly fee. GCP CUDs are billed monthly with no upfront payment option. This results in a recurring Purchase row each billing period with BilledCost equal to the monthly fee and zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost            | EffectiveCost        |
| ---------------- | ----- | --------------------- | -------------------- |
| Purchase         | 1     | &dollar;42,423.36     | &dollar;0.00         |
| Usage (Used)     | 24    | &dollar;0.00          | &dollar;1,515.12     |
| Usage (Standard) | 3     | &dollar;8.10          | &dollar;8.10         |
| **Total**        | 28    | **&dollar;42,431.46** | **&dollar;1,523.22** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value              |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)          |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)         |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 63.13 (USD)                |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a &dollar;63.13/hour commitment, this value is &dollar;63.13.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered | Standard     |
| ----------------------- | ------------------------ | ------------------ | ------------ |
| **ListUnitPrice**       | List (public) unit price | &dollar;94.70      | &dollar;2.70 |
| **ContractedUnitPrice** | Negotiated unit price    | &dollar;94.70      | &dollar;2.70 |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario         | BilledCost        | EffectiveCost | ListCost          |
| ---------------- | ----------------- | ------------- | ----------------- |
| **Purchase Row** | &dollar;42,423.36 | &dollar;0.00  | &dollar;42,423.36 |
| **Used Row**     | &dollar;0.00      | &dollar;63.13 | &dollar;94.70     |
| **Standard Row** | &dollar;2.70      | &dollar;2.70  | &dollar;2.70      |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Standard pricing rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                     | Value                                   | Explanation                                                    |
| -------------------------- | --------------------------------------- | -------------------------------------------------------------- |
| ChargeCategory             | Purchase                                | Commitment purchase transaction                                |
| ChargeFrequency            | Recurring                               | Monthly recurring fee                                          |
| BilledCost                 | &dollar;42,423.36                       | Monthly fee (hourly rate &times; 672 hours in Feb)             |
| EffectiveCost              | &dollar;0.00                            | **MUST be 0** - cost is amortized to usage rows                |
| PricingQuantity            | 42,423.36                               | Total commitment in USD (PricingUnit = USD)                    |
| CommitmentDiscountStatus   | null                                    | Status only applies to usage rows                              |
| CommitmentDiscountQuantity | 42,423.36                               | Commitment capacity for Feb (&dollar;63.13/hr &times; 672 hrs) |
| CommitmentDiscountUnit     | USD                                     | Unit of commitment capacity (spend-based)                      |
| SkuId                      | GCP-USCENTRAL1-COMPUTE-PURCHASE         | Commitment purchase SKU                                        |
| SkuPriceId                 | GCP-USCENTRAL1-COMPUTE-PURCHASE-MONTHLY | Price point for recurring purchase                             |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                                |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| ChargeCategory             | Usage                                                 | Compute resource consumption               |
| PricingCategory            | Committed                                             | Priced under commitment discount           |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment      |
| EffectiveCost              | &dollar;63.13                                         | Amortized cost (annual / hours)            |
| ListCost                   | &dollar;94.70                                         | What you would have paid at list price     |
| PricingQuantity            | 1                                                     | Units priced                               |
| ConsumedQuantity           | 1                                                     | Hours used                                 |
| CommitmentDiscountQuantity | 63.13                                                 | Hourly commitment spend applied            |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                         |
| CommitmentDiscountId       | projects/my-project-123456/locations/us-central1/c... | Links usage to purchase                    |
| SkuId                      | GCP-USCENTRAL1-COMPUTE-USAGE                          | Resource usage SKU (differs from Purchase) |
| SkuPriceId                 | GCP-USCENTRAL1-COMPUTE-USAGE-COMMITTED                | Price point for committed usage            |

## Standard Pricing Usage Row Details

| Column                     | Value                                    | Explanation                                   |
| -------------------------- | ---------------------------------------- | --------------------------------------------- |
| ChargeCategory             | Usage                                    | Compute consumption (standard pricing)        |
| PricingCategory            | Standard                                 | No discount applied                           |
| BilledCost                 | &dollar;2.70                             | Same as ListCost, no negotiation/commitments  |
| EffectiveCost              | &dollar;2.70                             | Same as BilledCost, no pre/post payments      |
| ListCost                   | &dollar;2.70                             | Public, non-negotiated cost                   |
| PricingQuantity            | 1                                        | Units priced                                  |
| ConsumedQuantity           | 1                                        | Hours consumed                                |
| CommitmentDiscountQuantity | null                                     | **No commitment applied**                     |
| CommitmentDiscountStatus   | null                                     | No commitment                                 |
| CommitmentDiscountId       | null                                     | No associated commitment                      |
| ContractedUnitPrice        | &dollar;2.70                             | Equals ListUnitPrice (no negotiated discount) |
| SkuId                      | GCP-USCENTRAL1-COMPUTE-ONDEMAND          | Standard (on-demand) resource SKU             |
| SkuPriceId                 | GCP-USCENTRAL1-COMPUTE-ONDEMAND-STANDARD | Price point for standard pricing              |
