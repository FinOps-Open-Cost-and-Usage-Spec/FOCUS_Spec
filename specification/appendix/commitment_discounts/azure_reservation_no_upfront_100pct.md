# Azure Reservation - No Upfront - 100% Utilization

| Parameter                  | Value               |
| -------------------------- | ------------------- |
| Scenario Type              | commitment          |
| Payment Model              | No Upfront          |
| Commitment Discount Category | Usage               |
| Utilization                | 100%                |
| Hours Generated            | 24                  |
| Annual Commitment          | &dollar;55,333.33   |
| List Unit Price            | &dollar;113.70/hour |
| Savings                    | 33%                 |

[CSV Example](/specification/data/commitment_discount_scenarios/azure_reservation_no_upfront_100pct.csv)

## Scenario Description

This example shows a **Microsoft Azure Virtual Machine Reserved Instance**, which is a commitment (CommitmentDiscountCategory: Usage) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **No Upfront** payment option means you pay nothing at purchase time and instead pay a recurring monthly fee. This results in a recurring Purchase row each billing period with BilledCost equal to the monthly fee and EffectiveCost=0.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

| Row Type         | Count | Total BilledCost      | Total EffectiveCost  |
| ---------------- | ----- | --------------------- | -------------------- |
| Purchase         | 1     | &dollar;55,333.33     | &dollar;0.00         |
| Usage (Used)     | 24    | &dollar;0.00          | &dollar;1,819.20     |
| Usage (Standard) | 12    | &dollar;39.35         | &dollar;39.35        |
| **Total**        | 37    | **&dollar;55,372.68** | **&dollar;1,858.55** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value        |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)    |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)   |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 1 (commitment units) |

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered | Standard       |
| ----------------------- | ------------------------ | ------------------ | -------------- |
| **ListUnitPrice**       | List (public) unit price | &dollar;113.70     | &dollar;113.70 |
| **ContractedUnitPrice** | Negotiated unit price    | &dollar;75.80      | null           |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario         | BilledCost        | EffectiveCost | ListCost          |
| ---------------- | ----------------- | ------------- | ----------------- |
| **Purchase Row** | &dollar;55,333.33 | &dollar;0.00  | &dollar;55,333.33 |
| **Used Row**     | &dollar;0.00      | &dollar;75.80 | &dollar;113.70    |
| **Standard Row** | &dollar;9.55      | &dollar;9.55  | &dollar;9.55      |

The following critical rules apply to commitment discount data:

- **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
- **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
- **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.
- **Standard pricing rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                   | Value             | Explanation                                     |
| ------------------------ | ----------------- | ----------------------------------------------- |
| ChargeCategory           | Purchase          | Commitment purchase transaction                 |
| ChargeFrequency          | Recurring         | Monthly recurring fee                           |
| BilledCost               | &dollar;55,333.33 | Portion of commitment payment                   |
| EffectiveCost            | &dollar;0.00      | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                 | One commitment unit purchased                   |
| CommitmentDiscountStatus | null              | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                            |
| -------------------------- | ----------------------------------------------------- | -------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption           |
| PricingCategory            | Committed                                             | Priced under commitment discount       |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment  |
| EffectiveCost              | &dollar;75.80                                         | Amortized cost (annual / hours)        |
| ListCost                   | &dollar;113.70                                        | What you would have paid at list price |
| PricingQuantity            | 1                                                     | Units priced                           |
| ConsumedQuantity           | 1                                                     | Hours used                             |
| CommitmentDiscountQuantity | 1                                                     | Units applied                          |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                     |
| CommitmentDiscountId       | /subscriptions/f0e9d8c7-b6a5-4321-0987-654321fedcb... | Links usage to purchase                |

## Standard Pricing Usage Row Details

| Column                     | Value          | Explanation                                   |
| -------------------------- | -------------- | --------------------------------------------- |
| ChargeCategory             | Usage          | Compute consumption (standard pricing)        |
| PricingCategory            | Standard       | No discount applied                           |
| BilledCost                 | &dollar;9.55   | List unit price                               |
| EffectiveCost              | &dollar;9.55   | = BilledCost                                  |
| ListCost                   | &dollar;9.55   | Same as BilledCost                            |
| PricingQuantity            | 459            | Units priced                                  |
| ConsumedQuantity           | 459            | Hours used                                    |
| CommitmentDiscountQuantity | null           | **No commitment applied**                     |
| CommitmentDiscountStatus   | null           | No commitment                                 |
| CommitmentDiscountId       | null        | No associated commitment                      |
| ContractedUnitPrice        | &dollar;113.70 | Equals ListUnitPrice (no negotiated discount) |
