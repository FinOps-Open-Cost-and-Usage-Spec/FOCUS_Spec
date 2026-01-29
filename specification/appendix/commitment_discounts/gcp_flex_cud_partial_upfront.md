# Google Cloud Platform Spend-based CUD (Partial-Upfront)

**Scenario Type:** commitment
**Payment Type:** Partial-Upfront
**Category:** Spend-based
**Utilization:** 100%
**Hours Generated:** 24
**Annual Commitment:** $200,416.67
**Committed Rate:** $42.24/hour
**On-Demand Rate:** $63.36/hour
**Savings:** 33%

[CSV Example](/specification/data/commitment_discount_scenarios/gcp_flex_cud_partial_upfront.csv)

## Scenario Description

This example shows a **Google Cloud Platform Spend-based CUD** (Committed Use Discount (Spend)), which is a spend-based commitment where you commit to a specific dollar amount of usage per hour.

The **Partial-Upfront** payment option combines an initial upfront payment with a reduced recurring monthly fee. This results in two Purchase rows: one One-Time for the upfront portion and one Recurring for the monthly fee, both with EffectiveCost=0.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

| Row Type          | Count | Total BilledCost | Total EffectiveCost |
| ----------------- | ----- | ---------------- | ------------------- |
| Purchase          | 2     | $200,416.67      | $0.00               |
| Usage (Used)      | 24    | $0.00            | $1,013.76           |
| Usage (On-Demand) | 12    | $12.16           | $12.16              |
| **Total**         | 38    | **$200,428.83**  | **$1,025.92**       |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value        |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)    |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)   |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 1 (commitment units) |

**Key Relationships:**

1. **Used Rows:** All three quantities are typically equal (1) because one hour of usage consumes one pricing unit and applies one commitment unit.

2. **Unused Rows:** `PricingQuantity=1` and `CommitmentDiscountQuantity=1` but `ConsumedQuantity=null` because no resource was actually consumed (the commitment capacity is wasted).

3. **On-Demand Rows:** `PricingQuantity=1` and `ConsumedQuantity=1` but `CommitmentDiscountQuantity=null` because no commitment applies.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                    | Commitment-Covered | On-Demand |
| ----------------------- | -------------------------- | ------------------ | --------- |
| **ListUnitPrice**       | On-demand (public) price   | $63.36             | $63.36    |
| **ContractedUnitPrice** | Negotiated/committed price | $42.24             | null      |

**Why this matters:** The difference between ListUnitPrice and ContractedUnitPrice represents your savings from the commitment. On-demand rows have no ContractedUnitPrice because they aren't covered by a commitment.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario          | BilledCost  | EffectiveCost | ListCost    |
| ----------------- | ----------- | ------------- | ----------- |
| **Purchase Row**  | $200,416.67 | $0.00         | $200,416.67 |
| **Used Row**      | $0.00       | $42.24        | $63.36      |
| **On-Demand Row** | $1.30       | $1.30         | $1.30       |

**Critical Rules:**

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.
* **On-demand rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                   | Value       | Explanation                                     |
| ------------------------ | ----------- | ----------------------------------------------- |
| ChargeCategory           | Purchase    | Commitment purchase transaction                 |
| ChargeFrequency          | One-Time    | One-time upfront payment                        |
| BilledCost               | $185,000.00 | Portion of commitment payment                   |
| EffectiveCost            | $0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1           | One commitment unit purchased                   |
| CommitmentDiscountStatus | null        | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                           |
| -------------------------- | ----------------------------------------------------- | ------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption          |
| PricingCategory            | Committed                                             | Priced at committed rate              |
| BilledCost                 | $0.00                                                 | **MUST be 0** - covered by commitment |
| EffectiveCost              | $42.24                                                | Amortized cost (annual / hours)       |
| ListCost                   | $63.36                                                | What you would have paid on-demand    |
| PricingQuantity            | 1                                                     | Units priced                          |
| ConsumedQuantity           | 1                                                     | Hours used                            |
| CommitmentDiscountQuantity | 42.24                                                 | Units applied                         |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                    |
| CommitmentDiscountId       | projects/my-project-123456/locations/us-central1/c... | Links usage to purchase               |

## On-Demand Usage Row Details

| Column                     | Value    | Explanation                   |
| -------------------------- | -------- | ----------------------------- |
| ChargeCategory             | Usage    | On-demand compute consumption |
| PricingCategory            | Standard | No discount applied           |
| BilledCost                 | $1.30    | On-demand price               |
| EffectiveCost              | $1.30    | = BilledCost                  |
| ListCost                   | $1.30    | Same as BilledCost            |
| PricingQuantity            | 65       | Units priced                  |
| ConsumedQuantity           | 65       | Hours used                    |
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

**Partial-Upfront Payment Validation:**

* Upfront payment: $185,000.00
* Monthly fee: $15,416.67
* Annual total: $185,000.00 + ($15,416.67 × 12) = $370,000.04
* Hourly amortization: $370,000.04 / 24 = $15,416.67/hour

**Check:** Sum(Usage EffectiveCost) should equal upfront + accumulated monthly fees.

### ✅ All Validation Rules Passed

This example data is valid according to FOCUS commitment discount rules.
