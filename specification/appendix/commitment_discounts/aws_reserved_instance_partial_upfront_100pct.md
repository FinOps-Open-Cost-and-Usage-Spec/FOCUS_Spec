# AWS Reserved Instance - Partial Upfront - 100% Utilization

| Parameter         | Value              |
| ----------------- | ------------------ |
| Scenario Type     | commitment         |
| Payment Model     | Partial-Upfront    |
| CommitmentDiscountCategory | Usage        |
| Utilization       | 100%               |
| Hours Generated   | 24                 |
| Annual Commitment | &dollar;238,333.33 |
| Effective Unit Price | &dollar;50.23/hour |
| List Unit Price   | &dollar;75.35/hour |
| Savings           | 33%                |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_reserved_instance_partial_upfront_100pct.csv)

## Scenario Description

This example shows an **Amazon Web Services EC2 Reserved Instance** (Reserved Instance), which is a commitment (CommitmentDiscountCategory: Usage) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **Partial-Upfront** payment option combines an initial upfront payment with a reduced recurring monthly fee. This results in two Purchase rows: one One-Time for the upfront portion and one Recurring for the monthly fee, both with EffectiveCost=0.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

| Row Type          | Count | Total BilledCost       | Total EffectiveCost  |
| ----------------- | ----- | ---------------------- | -------------------- |
| Purchase          | 2     | &dollar;238,333.33     | &dollar;0.00         |
| Usage (Used)      | 24    | &dollar;0.00           | &dollar;1,205.52     |
| Usage (Standard) | 12    | &dollar;19.82          | &dollar;19.82        |
| **Total**         | 38    | **&dollar;238,353.15** | **&dollar;1,225.34** |

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

| Column                  | Purpose                    | Commitment-Covered | Standard     |
| ----------------------- | -------------------------- | ------------------ | ------------- |
| **ListUnitPrice**       | List (public) unit price   | &dollar;75.35      | &dollar;75.35 |
| **ContractedUnitPrice** | Negotiated unit price | &dollar;50.23      | null          |

| **ContractedUnitPrice** | Negotiated unit price | &dollar;75.35      | &dollar;75.35 |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario          | BilledCost         | EffectiveCost | ListCost           |
| ----------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row**  | &dollar;238,333.33 | &dollar;0.00  | &dollar;238,333.33 |
| **Used Row**      | &dollar;0.00       | &dollar;50.23 | &dollar;75.35      |
| **Standard Row** | &dollar;5.84       | &dollar;5.84  | &dollar;5.84       |

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
| BilledCost               | &dollar;220,000.00 | Portion of commitment payment                   |
| EffectiveCost            | &dollar;0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                  | One commitment unit purchased                   |
| CommitmentDiscountStatus | null               | Status only applies to usage rows               |

## Recurring Purchase Row Details

| Column                   | Value              | Explanation                                     |
| ------------------------ | ------------------ | ----------------------------------------------- |
| ChargeCategory           | Purchase           | Commitment purchase transaction                 |
| ChargeFrequency          | Recurring          | Monthly recurring fee                           |
| BilledCost               | &dollar;18,333.33  | Monthly portion of commitment payment           |
| EffectiveCost            | &dollar;0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                  | One commitment unit purchased                   |
| CommitmentDiscountStatus | null               | Status only applies to usage rows               |

## Recurring Purchase Row Details

| Column                   | Value              | Explanation                                     |
| ------------------------ | ------------------ | ----------------------------------------------- |
| ChargeCategory           | Purchase           | Commitment purchase transaction                 |
| ChargeFrequency          | Recurring          | Monthly recurring fee                           |
| BilledCost               | &dollar;18,333.33  | Monthly portion of commitment payment           |
| EffectiveCost            | &dollar;0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                  | One commitment unit purchased                   |
| CommitmentDiscountStatus | null               | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                           |
| -------------------------- | ----------------------------------------------------- | ------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption          |
| PricingCategory            | Committed                                             | Priced under commitment discount              |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment |
| EffectiveCost              | &dollar;50.23                                         | Amortized cost (annual / hours)       |
| ListCost                   | &dollar;75.35                                         | What you would have paid at list price    |
| PricingQuantity            | 1                                                     | Units priced                          |
| ConsumedQuantity           | 1                                                     | Hours used                            |
| CommitmentDiscountQuantity | 1                                                     | Units applied                         |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                    |
| CommitmentDiscountId       | arn:aws:ec2:us-east-1:123456789012:reserved-instan... | Links usage to purchase               |

## Standard Pricing Usage Row Details

| Column                     | Value        | Explanation                   |
| -------------------------- | ------------ | ----------------------------- |
| ChargeCategory             | Usage        | Compute consumption (standard pricing) |
| PricingCategory            | Standard     | No discount applied           |
| BilledCost                 | &dollar;5.84 | List unit price               |
| EffectiveCost              | &dollar;5.84 | = BilledCost                  |
| ListCost                   | &dollar;5.84 | Same as BilledCost            |
| PricingQuantity            | 254          | Units priced                  |
| ConsumedQuantity           | 254          | Hours used                    |
| CommitmentDiscountQuantity | null         | **No commitment applied**     |
| CommitmentDiscountStatus   | null         | No commitment                 |
| CommitmentDiscountId       | (empty)      | No associated commitment      |
| ContractedUnitPrice        | &dollar;75.35 | Equals ListUnitPrice (no negotiated discount) |

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

Validation for Partial-Upfront payment option:

* Upfront payment: &dollar;220,000.00
* Monthly fee: &dollar;18,333.33
* Annual total: &dollar;220,000.00 + (&dollar;18,333.33 × 12) = &dollar;439,999.96
* Hourly amortization: &dollar;439,999.96 / 24 = &dollar;18,333.33/hour

### All Validation Rules Passed

This example data is valid according to FOCUS commitment discount rules.
