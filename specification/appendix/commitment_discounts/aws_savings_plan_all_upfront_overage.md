# AWS Savings Plan - All Upfront - 100% Utilization with Overage

| Parameter                    | Value                                                    |
| ---------------------------- | -------------------------------------------------------- |
| Scenario Type                | commitment                                               |
| Payment Model                | All Upfront                                              |
| Commitment Discount Category | Spend                                                    |
| Utilization                  | 100% (with overage to standard pricing)                  |
| Hours Generated              | 24 committed + 12 standard overflow                      |
| Annual Commitment            | &dollar;211,992.00                                       |
| List Unit Price              | &dollar;36.30/hour                                       |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_savings_plan_all_upfront_overage.csv)

## Scenario Description

This example shows an **Amazon Web Services EC2 Instance Savings Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **100% utilization with overage** where demand exceeds commitment capacity. The 24 Used rows represent full utilization of the commitment. The 12 Standard rows represent EC2 usage beyond the commitment that spills to standard pricing. Standard pricing rows have no CommitmentDiscountStatus, PricingCategory='Standard', and BilledCost=EffectiveCost at the full list price.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost             | EffectiveCost        |
| ---------------- | ----- | ---------------------- | -------------------- |
| Purchase         | 1     | &dollar;211,992.00     | &dollar;0.00         |
| Usage (Used)     | 24    | &dollar;0.00           | &dollar;580.80       |
| Usage (Standard) | 12    | &dollar;435.60         | &dollar;435.60       |
| **Total**        | 37    | **&dollar;212,435.60** | **&dollar;1,016.40** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value              |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)          |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)         |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 24.20 (USD)                |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a &dollar;24.20/hour commitment, this value is &dollar;24.20.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered | Standard      |
| ----------------------- | ------------------------ | ------------------ | ------------- |
| **ListUnitPrice**       | List (public) unit price | &dollar;36.30      | &dollar;36.30 |
| **ContractedUnitPrice** | Negotiated unit price    | &dollar;36.30      | &dollar;36.30 |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario         | BilledCost         | EffectiveCost | ListCost           |
| ---------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row** | &dollar;211,992.00 | &dollar;0.00  | &dollar;211,992.00 |
| **Used Row**     | &dollar;0.00       | &dollar;24.20 | &dollar;36.30      |
| **Standard Row** | &dollar;36.30      | &dollar;36.30 | &dollar;36.30      |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Standard pricing rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                   | Value              | Explanation                                     |
| ------------------------ | ------------------ | ----------------------------------------------- |
| ChargeCategory           | Purchase           | Commitment purchase transaction                 |
| ChargeFrequency          | One-Time           | One-time upfront payment                        |
| BilledCost               | &dollar;211,992.00 | Full annual commitment payment                  |
| EffectiveCost            | &dollar;0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                  | One commitment unit purchased                   |
| CommitmentDiscountStatus | null               | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                            |
| -------------------------- | ----------------------------------------------------- | -------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption           |
| PricingCategory            | Committed                                             | Priced under commitment discount       |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment  |
| EffectiveCost              | &dollar;24.20                                         | Amortized cost (annual / hours)        |
| ListCost                   | &dollar;36.30                                         | What you would have paid at list price |
| PricingQuantity            | 1                                                     | Units priced                           |
| ConsumedQuantity           | 1                                                     | Hours used                             |
| CommitmentDiscountQuantity | 24.20                                                 | Hourly commitment spend applied        |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                     |
| CommitmentDiscountId       | arn:aws:savingsplans::123456789012:savingsplan/sp-... | Links usage to purchase                |

## Standard Pricing Usage Row Details

| Column                     | Value         | Explanation                                   |
| -------------------------- | ------------- | --------------------------------------------- |
| ChargeCategory             | Usage         | Compute consumption (standard pricing)        |
| PricingCategory            | Standard      | No discount applied                           |
| BilledCost                 | &dollar;36.30 | Same as ListCost, no negotiation/commitments  |
| EffectiveCost              | &dollar;36.30 | Same as BilledCost, no pre/post payments      |
| ListCost                   | &dollar;36.30 | Public, non-negotiated cost                   |
| PricingQuantity            | 1             | Units priced                                  |
| ConsumedQuantity           | 1             | Hours consumed                                |
| CommitmentDiscountQuantity | null          | **No commitment applied**                     |
| CommitmentDiscountStatus   | null          | No commitment                                 |
| CommitmentDiscountId       | null          | No associated commitment                      |
| ContractedUnitPrice        | &dollar;36.30 | Equals ListUnitPrice (no negotiated discount) |
