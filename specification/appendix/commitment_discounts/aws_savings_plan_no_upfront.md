# Amazon Web Services EC2 Instance Savings Plan (No-Upfront)

| Parameter         | Value              |
| ----------------- | ------------------ |
| Scenario Type     | commitment         |
| Payment Type      | No-Upfront         |
| Category          | Spend-based        |
| Utilization       | 100%               |
| Hours Generated   | 24                 |
| Annual Commitment | &dollar;38,583.33  |
| Committed Rate    | &dollar;52.85/hour |
| On-Demand Rate    | &dollar;79.28/hour |
| Savings           | 33%                |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_savings_plan_no_upfront.csv)

## Scenario Description

This example shows a **Amazon Web Services EC2 Instance Savings Plan** (Savings Plan), which is a spend-based commitment where you commit to a specific dollar amount of usage per hour.

The **No-Upfront** payment option means you pay nothing at purchase time and instead pay a recurring monthly fee. This results in a recurring Purchase row each billing period with BilledCost equal to the monthly fee and EffectiveCost=0.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

| Row Type          | Count | Total BilledCost      | Total EffectiveCost  |
| ----------------- | ----- | --------------------- | -------------------- |
| Purchase          | 1     | &dollar;38,583.33     | &dollar;0.00         |
| Usage (Used)      | 24    | &dollar;0.00          | &dollar;1,268.40     |
| Usage (On-Demand) | 12    | &dollar;13.18         | &dollar;13.18        |
| **Total**         | 37    | **&dollar;38,596.51** | **&dollar;1,281.58** |

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

| Column                  | Purpose                    | Commitment-Covered | On-Demand     |
| ----------------------- | -------------------------- | ------------------ | ------------- |
| **ListUnitPrice**       | On-demand (public) price   | &dollar;79.28      | &dollar;79.28 |
| **ContractedUnitPrice** | Negotiated/committed price | &dollar;52.85      | null          |

**Why this matters:** The difference between ListUnitPrice and ContractedUnitPrice represents your savings from the commitment. On-demand rows have no ContractedUnitPrice because they aren't covered by a commitment.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario          | BilledCost        | EffectiveCost | ListCost          |
| ----------------- | ----------------- | ------------- | ----------------- |
| **Purchase Row**  | &dollar;38,583.33 | &dollar;0.00  | &dollar;38,583.33 |
| **Used Row**      | &dollar;0.00      | &dollar;52.85 | &dollar;79.28     |
| **On-Demand Row** | &dollar;6.10      | &dollar;6.10  | &dollar;6.10      |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.
* **On-demand rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                   | Value             | Explanation                                     |
| ------------------------ | ----------------- | ----------------------------------------------- |
| ChargeCategory           | Purchase          | Commitment purchase transaction                 |
| ChargeFrequency          | Recurring         | Monthly recurring fee                           |
| BilledCost               | &dollar;38,583.33 | Portion of commitment payment                   |
| EffectiveCost            | &dollar;0.00      | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                 | One commitment unit purchased                   |
| CommitmentDiscountStatus | null              | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                           |
| -------------------------- | ----------------------------------------------------- | ------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption          |
| PricingCategory            | Committed                                             | Priced at committed rate              |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment |
| EffectiveCost              | &dollar;52.85                                         | Amortized cost (annual / hours)       |
| ListCost                   | &dollar;79.28                                         | What you would have paid on-demand    |
| PricingQuantity            | 1                                                     | Units priced                          |
| ConsumedQuantity           | 1                                                     | Hours used                            |
| CommitmentDiscountQuantity | 52.85                                                 | Units applied                         |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                    |
| CommitmentDiscountId       | arn:aws:savingsplans::123456789012:savingsplan/sp-... | Links usage to purchase               |

## On-Demand Usage Row Details

| Column                     | Value        | Explanation                   |
| -------------------------- | ------------ | ----------------------------- |
| ChargeCategory             | Usage        | On-demand compute consumption |
| PricingCategory            | Standard     | No discount applied           |
| BilledCost                 | &dollar;6.10 | On-demand price               |
| EffectiveCost              | &dollar;6.10 | = BilledCost                  |
| ListCost                   | &dollar;6.10 | Same as BilledCost            |
| PricingQuantity            | 265          | Units priced                  |
| ConsumedQuantity           | 265          | Hours used                    |
| CommitmentDiscountQuantity | null         | **No commitment applied**     |
| CommitmentDiscountStatus   | null         | No commitment                 |
| CommitmentDiscountId       | (empty)      | No associated commitment      |
| ContractedUnitPrice        | null         | No contracted rate            |

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

### Rule 3: On-Demand Cost Equality

```text
FOR ALL rows WHERE PricingCategory = 'Standard' AND ChargeCategory = 'Usage':
    ASSERT BilledCost = EffectiveCost
    ASSERT BilledCost = ListCost
```

**Rationale:** On-demand usage has no discount or amortization. All cost columns should be equal.

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

Validation for No-Upfront payment option:

* Monthly fee (BilledCost): &dollar;38,583.33
* Hours generated: 24
* Hourly amortization: &dollar;38,583.33 / 24 = &dollar;1,607.64/hour

### All Validation Rules Passed

This example data is valid according to FOCUS commitment discount rules.
