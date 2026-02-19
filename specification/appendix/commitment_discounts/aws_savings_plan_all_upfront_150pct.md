# AWS Savings Plan - All Upfront - 150% Utilization

| Parameter         | Value                                             |
| ----------------- | ------------------------------------------------- |
| Scenario Type     | commitment                                        |
| Payment Model     | All-Upfront                                       |
| CommitmentDiscountCategory | Spend                                       |
| Utilization       | 150% (100% committed + 50% overflow to standard pricing) |
| Hours Generated   | 48 (24 committed + 24 overflow to standard pricing)      |
| Annual Commitment | &dollar;212,000.00                                |
| Effective Unit Price | &dollar;24.20/hour                                |
| List Unit Price   | &dollar;36.30/hour                                |
| Savings           | 33%                                               |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_savings_plan_all_upfront_150pct.csv)

## Scenario Description

This example shows an **Amazon Web Services EC2 Instance Savings Plan** (Savings Plan), which is a commitment (CommitmentDiscountCategory: Spend) where you commit to a specific dollar amount of usage per hour.

The **All-Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and EffectiveCost=0 (since the cost is amortized to usage rows).

This scenario demonstrates **overflow** at 150% utilization where demand exceeds commitment capacity by 50%. The first 24 hours represent 100% utilization of the commitment, while the additional 12 hours represent 50% overflow that spills to standard pricing. Standard pricing rows have no CommitmentDiscountStatus, PricingCategory='Standard', and BilledCost=EffectiveCost at the full list price.

## Row Summary

| Row Type          | Count | Total BilledCost       | Total EffectiveCost  |
| ----------------- | ----- | ---------------------- | -------------------- |
| Purchase          | 1     | &dollar;212,000.00     | &dollar;0.00         |
| Usage (Used)      | 24    | &dollar;0.00           | &dollar;580.80       |
| Usage (Standard) | 24    | &dollar;459.18         | &dollar;459.18       |
| **Total**         | 49    | **&dollar;212,459.18** | **&dollar;1,039.98** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value        |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)    |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)   |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 1 (commitment units) |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For a $24.20/hour commitment, this value is $24.20.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                    | Commitment-Covered | Standard     |
| ----------------------- | -------------------------- | ------------------ | ------------- |
| **ListUnitPrice**       | List (public) unit price   | &dollar;36.30      | &dollar;36.30 |
| **ContractedUnitPrice** | Negotiated unit price | &dollar;24.20      | null          |

**Why this matters:** The difference between ListUnitPrice and ContractedUnitPrice represents your savings from the contract. Standard pricing rows have no ContractedUnitPrice because they aren't covered by a commitment.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario          | BilledCost         | EffectiveCost | ListCost           |
| ----------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row**  | &dollar;212,000.00 | &dollar;0.00  | &dollar;212,000.00 |
| **Used Row**      | &dollar;0.00       | &dollar;24.20 | &dollar;36.30      |
| **Standard Row** | &dollar;36.30      | &dollar;36.30 | &dollar;36.30      |

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
| BilledCost               | &dollar;212,000.00 | Full annual commitment payment                  |
| EffectiveCost            | &dollar;0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                  | One commitment unit purchased                   |
| CommitmentDiscountStatus | null               | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                           |
| -------------------------- | ----------------------------------------------------- | ------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption          |
| PricingCategory            | Committed                                             | Priced under commitment discount              |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment |
| EffectiveCost              | &dollar;24.20                                         | Amortized cost (annual / hours)       |
| ListCost                   | &dollar;36.30                                         | What you would have paid at list price    |
| PricingQuantity            | 1                                                     | Units priced                          |
| ConsumedQuantity           | 1                                                     | Hours used                            |
| CommitmentDiscountQuantity | 24.20                                                 | Units applied                         |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                    |
| CommitmentDiscountId       | arn:aws:savingsplans::123456789012:savingsplan/sp-... | Links usage to purchase               |

## Standard Pricing Usage Row Details

| Column                     | Value         | Explanation                   |
| -------------------------- | ------------- | ----------------------------- |
| ChargeCategory             | Usage         | Compute consumption (standard pricing) |
| PricingCategory            | Standard      | No discount applied           |
| BilledCost                 | &dollar;36.30 | List unit price               |
| EffectiveCost              | &dollar;36.30 | = BilledCost                  |
| ListCost                   | &dollar;36.30 | Same as BilledCost            |
| PricingQuantity            | 1             | Units priced                  |
| ConsumedQuantity           | 1             | Hours used                    |
| CommitmentDiscountQuantity | null          | **No commitment applied**     |
| CommitmentDiscountStatus   | null          | No commitment                 |
| CommitmentDiscountId       | (empty)       | No associated commitment      |
| ContractedUnitPrice        | null          | No contracted unit price            |

## Validation Rules

Use these rules to validate FOCUS commitment data.

### Rule 1: Purchase Row Effective Cost

```text
FOR ALL rows WHERE ChargeCategory = 'Purchase':
    ASSERT EffectiveCost = 0
```

**Rationale:** Purchase costs are distributed to usage rows through amortization. The purchase itself has no effective cost.

### Rule 2: Commitment-Covered Usage Has Zero Billed Cost

```text
FOR ALL rows WHERE CommitmentDiscountStatus IN ('Used', 'Unused'):
    ASSERT BilledCost = 0
```

**Rationale:** Usage covered by a commitment has already been paid for through the purchase transaction.

### Rule 3: Standard Pricing Cost Equality

```text
FOR ALL rows WHERE PricingCategory = 'Standard' AND ChargeCategory = 'Usage':
    ASSERT BilledCost = EffectiveCost
    ASSERT BilledCost = ListCost
```

**Rationale:** Standard pricing usage has no discount or amortization. All cost columns should be equal.

### Rule 4: Commitment Link Integrity

```text
FOR ALL rows WHERE CommitmentDiscountStatus IS NOT NULL:
    ASSERT CommitmentDiscountId IS NOT EMPTY
    ASSERT CommitmentDiscountId matches a Purchase row ResourceId
```

**Rationale:** Every Used/Unused row must link back to its originating purchase.

### Rule 5: Amortization Balance

```text
FOR commitment period:
    ASSERT Sum(Purchase.BilledCost) = Sum(Usage.EffectiveCost WHERE CommitmentDiscountStatus IS NOT NULL)
```

**Rationale:** The total effective cost of commitment-covered usage should equal the purchase cost when summed over the commitment term.

### Validation for This Scenario

Validation for All-Upfront payment option:

* Annual commitment: &dollar;212,000.00
* Hours in term: 24
* Hourly amortization: &dollar;212,000.00 / 24 = &dollar;8,833.33/hour
* Daily amortization (365 days): &dollar;212,000.00 / 365 = &dollar;580.82/day
* Sum(Usage EffectiveCost): &dollar;580.80

### All Validation Rules Passed

This example data is valid according to FOCUS commitment discount rules.
