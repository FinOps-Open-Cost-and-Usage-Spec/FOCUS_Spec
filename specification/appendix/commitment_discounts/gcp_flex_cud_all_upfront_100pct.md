# GCP Flex CUD - All Upfront - 100% Utilization

| Parameter                  | Value              |
|----------------------------|--------------------|
| Scenario Type              | commitment         |
| Payment Model              | All-Upfront        |
| CommitmentDiscountCategory | Spend              |
| Utilization                | 100%               |
| Hours Generated            | 24                 |
| Annual Commitment          | &dollar;553,000.00 |
| List Unit Price            | &dollar;94.70/hour |
| Savings                    | 33%                |

[CSV Example](/specification/data/commitment_discount_scenarios/gcp_flex_cud_all_upfront_100pct.csv)

## Scenario Description

This example shows a **Google Cloud Platform Spend-based CUD** (Committed Use Discount (Spend)), which is a commitment (CommitmentDiscountCategory: Spend) where you commit to a specific dollar amount of usage per hour.

The **All-Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and EffectiveCost=0 (since the cost is amortized to usage rows).

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

| Row Type         | Count | Total BilledCost       | Total EffectiveCost  |
|------------------|-------|------------------------|----------------------|
| Purchase         | 1     | &dollar;553,000.00     | &dollar;0.00         |
| Usage (Used)     | 24    | &dollar;0.00           | &dollar;1,515.12     |
| Usage (Standard) | 12    | &dollar;25.52          | &dollar;25.52        |
| **Total**        | 37    | **&dollar;553,025.52** | **&dollar;1,540.64** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value        |
|--------------------------------|---------------------------------------|-------------------------------|----------------------|
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)    |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)   |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 1 (commitment units) |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a &dollar;63.13/hour commitment, this value is &dollar;63.13.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered | Standard      |
|-------------------------|--------------------------|--------------------|---------------|
| **ListUnitPrice**       | List (public) unit price | &dollar;94.70      | &dollar;94.70 |
| **ContractedUnitPrice** | Negotiated unit price    | &dollar;63.13      | null          |

| **ContractedUnitPrice** | Negotiated unit price | &dollar;94.70      | &dollar;94.70 |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario         | BilledCost         | EffectiveCost | ListCost           |
|------------------|--------------------|---------------|--------------------|
| **Purchase Row** | &dollar;553,000.00 | &dollar;0.00  | &dollar;553,000.00 |
| **Used Row**     | &dollar;0.00       | &dollar;63.13 | &dollar;94.70      |
| **Standard Row** | &dollar;9.76       | &dollar;9.76  | &dollar;9.76       |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.
* **Standard pricing rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                   | Value              | Explanation                                     |
|--------------------------|--------------------|-------------------------------------------------|
| ChargeCategory           | Purchase           | Commitment purchase transaction                 |
| ChargeFrequency          | One-Time           | One-time upfront payment                        |
| BilledCost               | &dollar;553,000.00 | Full annual commitment payment                  |
| EffectiveCost            | &dollar;0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                  | One commitment unit purchased                   |
| CommitmentDiscountStatus | null               | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                            |
|----------------------------|-------------------------------------------------------|----------------------------------------|
| ChargeCategory             | Usage                                                 | Compute resource consumption           |
| PricingCategory            | Committed                                             | Priced under commitment discount       |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment  |
| EffectiveCost              | &dollar;63.13                                         | Amortized cost (annual / hours)        |
| ListCost                   | &dollar;94.70                                         | What you would have paid at list price |
| PricingQuantity            | 1                                                     | Units priced                           |
| ConsumedQuantity           | 1                                                     | Hours used                             |
| CommitmentDiscountQuantity | 63.13                                                 | Commitment dollars applied             |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                     |
| CommitmentDiscountId       | projects/my-project-123456/locations/us-central1/c... | Links usage to purchase                |

## Standard Pricing Usage Row Details

| Column                     | Value         | Explanation                                   |
|----------------------------|---------------|-----------------------------------------------|
| ChargeCategory             | Usage         | Compute consumption (standard pricing)        |
| PricingCategory            | Standard      | No discount applied                           |
| BilledCost                 | &dollar;9.76  | List unit price                               |
| EffectiveCost              | &dollar;9.76  | = BilledCost                                  |
| ListCost                   | &dollar;9.76  | Same as BilledCost                            |
| PricingQuantity            | 488           | Units priced                                  |
| ConsumedQuantity           | 488           | Hours used                                    |
| CommitmentDiscountQuantity | null          | **No commitment applied**                     |
| CommitmentDiscountStatus   | null          | No commitment                                 |
| CommitmentDiscountId       | (empty)       | No associated commitment                      |
| ContractedUnitPrice        | &dollar;94.70 | Equals ListUnitPrice (no negotiated discount) |
