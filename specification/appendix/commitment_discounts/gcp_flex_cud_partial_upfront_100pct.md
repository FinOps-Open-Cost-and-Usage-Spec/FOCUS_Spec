# GCP Flex CUD - Partial Upfront - 100% Utilization

| Parameter                    | Value              |
| ---------------------------- | ------------------ |
| Scenario Type                | commitment         |
| Payment Model                | Partial Upfront    |
| Commitment Discount Category | Spend              |
| Utilization                  | 100%               |
| Hours Generated              | 24                 |
| Annual Commitment            | &dollar;200,416.67 |
| List Unit Price              | &dollar;63.36/hour |
| Savings                      | 33%                |

[CSV Example](/specification/data/commitment_discount_scenarios/gcp_flex_cud_partial_upfront_100pct.csv)

## Scenario Description

This example shows a **Google Cloud Platform Spend-based CUD**, which is a commitment (CommitmentDiscountCategory: Spend) where you commit to a specific dollar amount of usage per hour.

The **Partial Upfront** payment option combines an initial upfront payment with a reduced recurring monthly fee. This results in two Purchase rows: one One-Time for the upfront portion and one Recurring for the monthly fee, both with zero EffectiveCost.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost             | EffectiveCost        |
| ---------------- | ----- | ---------------------- | -------------------- |
| Purchase         | 2     | &dollar;108,559.03     | &dollar;0.00         |
| Usage (Used)     | 24    | &dollar;0.00           | &dollar;1,013.76     |
| Usage (Standard) | 12    | &dollar;12.16          | &dollar;12.16        |
| **Total**        | 38    | **&dollar;108,571.19** | **&dollar;1,025.92** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value        |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)    |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)   |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 1 (commitment units) |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a &dollar;42.24/hour commitment, this value is &dollar;42.24.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered | Standard      |
| ----------------------- | ------------------------ | ------------------ | ------------- |
| **ListUnitPrice**       | List (public) unit price | &dollar;63.36      | &dollar;63.36 |
| **ContractedUnitPrice** | Negotiated unit price    | &dollar;63.36      | &dollar;63.36 |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario                     | BilledCost         | EffectiveCost | ListCost           |
| ---------------------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row (One-Time)**  | &dollar;100,208.34 | &dollar;0.00  | &dollar;100,208.34 |
| **Purchase Row (Recurring)** | &dollar;8,350.69   | &dollar;0.00  | &dollar;8,350.69   |
| **Used Row**                 | &dollar;0.00       | &dollar;42.24 | &dollar;63.36      |
| **Standard Row**             | &dollar;1.30       | &dollar;1.30  | &dollar;1.30       |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.
* **Standard pricing rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                   | Value              | Explanation                                     |
| ------------------------ | ------------------ | ----------------------------------------------- |
| ChargeCategory           | Purchase           | Commitment purchase transaction                 |
| ChargeFrequency          | One-Time           | One-time upfront payment                        |
| BilledCost               | &dollar;100,208.34 | Upfront portion (50% of annual commitment)      |
| EffectiveCost            | &dollar;0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                  | One commitment unit purchased                   |
| CommitmentDiscountStatus | null               | Status only applies to usage rows               |

## Recurring Purchase Row Details

| Column                   | Value             | Explanation                                     |
| ------------------------ | ----------------- | ----------------------------------------------- |
| ChargeCategory           | Purchase          | Commitment purchase transaction                 |
| ChargeFrequency          | Recurring         | Monthly recurring fee                           |
| BilledCost               | &dollar;8,350.69  | Monthly portion (remaining 50% / 12 months)     |
| EffectiveCost            | &dollar;0.00      | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                 | One commitment unit purchased                   |
| CommitmentDiscountStatus | null              | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                            |
| -------------------------- | ----------------------------------------------------- | -------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption           |
| PricingCategory            | Committed                                             | Priced under commitment discount       |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment  |
| EffectiveCost              | &dollar;42.24                                         | Amortized cost (annual / hours)        |
| ListCost                   | &dollar;63.36                                         | What you would have paid at list price |
| PricingQuantity            | 1                                                     | Units priced                           |
| ConsumedQuantity           | 1                                                     | Hours used                             |
| CommitmentDiscountQuantity | 42.24                                                 | Commitment dollars applied             |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                     |
| CommitmentDiscountId       | projects/my-project-123456/locations/us-central1/c... | Links usage to purchase                |

## Standard Pricing Usage Row Details

| Column                     | Value         | Explanation                                   |
| -------------------------- | ------------- | --------------------------------------------- |
| ChargeCategory             | Usage         | Compute consumption (standard pricing)        |
| PricingCategory            | Standard      | No discount applied                           |
| BilledCost                 | &dollar;1.30  | List unit price                               |
| EffectiveCost              | &dollar;1.30  | = BilledCost                                  |
| ListCost                   | &dollar;1.30  | Same as BilledCost                            |
| PricingQuantity            | 65            | Units priced                                  |
| ConsumedQuantity           | 65            | Hours used                                    |
| CommitmentDiscountQuantity | null          | **No commitment applied**                     |
| CommitmentDiscountStatus   | null          | No commitment                                 |
| CommitmentDiscountId       | null          | No associated commitment                      |
| ContractedUnitPrice        | &dollar;63.36 | Equals ListUnitPrice (no negotiated discount) |
