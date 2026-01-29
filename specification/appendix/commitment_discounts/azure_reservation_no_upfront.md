# Microsoft Azure Virtual Machine Reserved Instance (No-Upfront)

**Scenario Type:** commitment
**Payment Type:** No-Upfront
**Category:** Usage-based
**Utilization:** 100%
**Hours Generated:** 24
**Annual Commitment:** &dollar;55,333.33
**Committed Rate:** &dollar;75.80/hour
**On-Demand Rate:** &dollar;113.70/hour
**Savings:** 33%

[CSV Example](/specification/data/commitment_discount_scenarios/azure_reservation_no_upfront.csv)

## Scenario Description

This example shows a **Microsoft Azure Virtual Machine Reserved Instance** (Azure Reservation), which is a usage-based commitment where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **No-Upfront** payment option means you pay nothing at purchase time and instead pay a recurring monthly fee. This results in a recurring Purchase row each billing period with BilledCost equal to the monthly fee and EffectiveCost=0.

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

| Row Type          | Count | Total BilledCost | Total EffectiveCost |
| ----------------- | ----- | ---------------- | ------------------- |
| Purchase          | 1     | &dollar;55,333.33       | &dollar;0.00               |
| Usage (Used)      | 24    | &dollar;0.00            | &dollar;1,819.20           |
| Usage (On-Demand) | 12    | &dollar;39.35           | &dollar;39.35              |
| **Total**         | 37    | **&dollar;55,372.68**   | **&dollar;1,858.55**       |

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

| Column                  | Purpose                    | Commitment-Covered | On-Demand |
| ----------------------- | -------------------------- | ------------------ | --------- |
| **ListUnitPrice**       | On-demand (public) price   | &dollar;113.70            | &dollar;113.70   |
| **ContractedUnitPrice** | Negotiated/committed price | &dollar;75.80             | null      |

**Why this matters:** The difference between ListUnitPrice and ContractedUnitPrice represents your savings from the commitment. On-demand rows have no ContractedUnitPrice because they aren't covered by a commitment.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario          | BilledCost | EffectiveCost | ListCost   |
| ----------------- | ---------- | ------------- | ---------- |
| **Purchase Row**  | &dollar;55,333.33 | &dollar;0.00         | &dollar;55,333.33 |
| **Used Row**      | &dollar;0.00      | &dollar;75.80        | &dollar;113.70    |
| **On-Demand Row** | &dollar;9.55      | &dollar;9.55         | &dollar;9.55      |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.
* **On-demand rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                   | Value      | Explanation                                     |
| ------------------------ | ---------- | ----------------------------------------------- |
| ChargeCategory           | Purchase   | Commitment purchase transaction                 |
| ChargeFrequency          | Recurring  | Monthly recurring fee                           |
| BilledCost               | &dollar;55,333.33 | Portion of commitment payment                   |
| EffectiveCost            | &dollar;0.00      | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1          | One commitment unit purchased                   |
| CommitmentDiscountStatus | null       | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                           |
| -------------------------- | ----------------------------------------------------- | ------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption          |
| PricingCategory            | Committed                                             | Priced at committed rate              |
| BilledCost                 | &dollar;0.00                                                 | **MUST be 0** - covered by commitment |
| EffectiveCost              | &dollar;75.80                                                | Amortized cost (annual / hours)       |
| ListCost                   | &dollar;113.70                                               | What you would have paid on-demand    |
| PricingQuantity            | 1                                                     | Units priced                          |
| ConsumedQuantity           | 1                                                     | Hours used                            |
| CommitmentDiscountQuantity | 1                                                     | Units applied                         |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                    |
| CommitmentDiscountId       | /subscriptions/f0e9d8c7-b6a5-4321-0987-654321fedcb... | Links usage to purchase               |

## On-Demand Usage Row Details

| Column                     | Value    | Explanation                   |
| -------------------------- | -------- | ----------------------------- |
| ChargeCategory             | Usage    | On-demand compute consumption |
| PricingCategory            | Standard | No discount applied           |
| BilledCost                 | &dollar;9.55    | On-demand price               |
| EffectiveCost              | &dollar;9.55    | = BilledCost                  |
| ListCost                   | &dollar;9.55    | Same as BilledCost            |
| PricingQuantity            | 459      | Units priced                  |
| ConsumedQuantity           | 459      | Hours used                    |
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

Validation for No-Upfront payment option:

* Monthly fee (BilledCost): &dollar;55,333.33
* Hours generated: 24
* Hourly amortization: &dollar;55,333.33 / 24 = &dollar;2,305.56/hour

**Check:** Sum(Usage EffectiveCost) per month should equal the monthly fee.

### All Validation Rules Passed

This example data is valid according to FOCUS commitment discount rules.

