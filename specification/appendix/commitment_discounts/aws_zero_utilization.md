# Amazon Web Services EC2 Instance Savings Plan (All-Upfront)

**Scenario Type:** commitment
**Payment Type:** All-Upfront
**Category:** Spend-based
**Utilization:** 0%
**Hours Generated:** 24
**Annual Commitment:** $353,000.00

[CSV Example](/specification/data/commitment_discount_scenarios/aws_zero_utilization.csv)

## Scenario Description

This example shows a **Amazon Web Services EC2 Instance Savings Plan** (Savings Plan), which is a spend-based commitment where you commit to a specific dollar amount of usage per hour.

The **All-Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and EffectiveCost=0 (since the cost is amortized to usage rows).

This scenario demonstrates **zero utilization** where the commitment is purchased but no resources are consumed. All usage rows have CommitmentDiscountStatus='Unused', representing wasted commitment capacity. The EffectiveCost on these rows reflects the cost of unused commitment that cannot be recovered.

## Row Summary

| Row Type          | Count | Total BilledCost | Total EffectiveCost |
| ----------------- | ----- | ---------------- | ------------------- |
| Purchase          | 1     | $353,000.00      | $0.00               |
| Usage (Used)      | 0     | $0.00            | $0.00               |
| Usage (Unused)    | 24    | $0.00            | $967.20             |
| Usage (On-Demand) | 12    | $12.84           | $12.84              |
| **Total**         | 37    | **$353,012.84**  | **$980.04**         |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value        |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)    |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)   |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 1 (commitment units) |

The following key relationships apply between quantity columns:

1. **Used Rows:** All three quantities are typically equal (1) because one hour of usage consumes one pricing unit and applies one commitment unit.

2. **Unused Rows:** `PricingQuantity=1` and `CommitmentDiscountQuantity=1` but `ConsumedQuantity=null` because no resource was actually consumed (the commitment capacity is wasted).

3. **On-Demand Rows:** `PricingQuantity=1` and `ConsumedQuantity=1` but `CommitmentDiscountQuantity=null` because no commitment applies.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                    | Commitment-Covered | On-Demand   |
| ----------------------- | -------------------------- | ------------------ | ----------- |
| **ListUnitPrice**       | On-demand (public) price   | (list rate)        | (list rate) |
| **ContractedUnitPrice** | Negotiated/committed price | (committed rate)   | null        |

**Why this matters:** The difference between ListUnitPrice and ContractedUnitPrice represents your savings from the commitment. On-demand rows have no ContractedUnitPrice because they aren't covered by a commitment.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario          | BilledCost | EffectiveCost | ListCost |
| ----------------- | ---------- | ------------- | -------- |
| **Unused Row**    | $0.00      | $40.30        | null     |
| **On-Demand Row** | $2.85      | $2.85         | $2.85    |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.
* **On-demand rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                   | Value       | Explanation                                     |
| ------------------------ | ----------- | ----------------------------------------------- |
| ChargeCategory           | Purchase    | Commitment purchase transaction                 |
| ChargeFrequency          | One-Time    | One-time upfront payment                        |
| BilledCost               | $353,000.00 | Full annual commitment payment                  |
| EffectiveCost            | $0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1           | One commitment unit purchased                   |
| CommitmentDiscountStatus | null        | Status only applies to usage rows               |

## Unused Commitment Row Details

| Column                     | Value   | Explanation                                      |
| -------------------------- | ------- | ------------------------------------------------ |
| ChargeCategory             | Usage   | Represents commitment capacity                   |
| BilledCost                 | $0.00   | No additional billing (already paid at purchase) |
| EffectiveCost              | $40.30  | **Wasted value** - lost commitment               |
| PricingQuantity            | 1       | Commitment units unused                          |
| ConsumedQuantity           | null    | **No resource consumed**                         |
| CommitmentDiscountQuantity | 40.30   | Commitment wasted                                |
| CommitmentDiscountStatus   | Unused  | Commitment not utilized                          |
| ResourceId                 | (empty) | No resource associated                           |

## On-Demand Usage Row Details

| Column                     | Value    | Explanation                   |
| -------------------------- | -------- | ----------------------------- |
| ChargeCategory             | Usage    | On-demand compute consumption |
| PricingCategory            | Standard | No discount applied           |
| BilledCost                 | $2.85    | On-demand price               |
| EffectiveCost              | $2.85    | = BilledCost                  |
| ListCost                   | $2.85    | Same as BilledCost            |
| PricingQuantity            | 124      | Units priced                  |
| ConsumedQuantity           | 124      | Hours used                    |
| CommitmentDiscountQuantity | null     | **No commitment applied**     |
| CommitmentDiscountStatus   | null     | No commitment                 |
| CommitmentDiscountId       | (empty)  | No associated commitment      |
| ContractedUnitPrice        | null     | No contracted rate            |

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

Validation for All-Upfront payment option:

* Annual commitment: $353,000.00
* Hours in term: 24
* Hourly amortization: $353,000.00 / 24 = $14,708.33/hour
* Daily amortization (365 days): $353,000.00 / 365 = $967.12/day
* Sum(Usage EffectiveCost): $0.00

**Check:** $0.00 should approach $353,000.00 over the full term.

### All Validation Rules Passed

This example data is valid according to FOCUS commitment discount rules.
