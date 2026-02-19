# Azure Reservation - All Upfront - 100% Utilization

| Parameter         | Value              |
| ----------------- | ------------------ |
| Scenario Type     | commitment         |
| Payment Model     | All-Upfront        |
| CommitmentDiscountCategory | Usage        |
| Utilization       | 100%               |
| Hours Generated   | 24                 |
| Annual Commitment | &dollar;358,000.00 |
| Effective Unit Price | &dollar;40.87/hour |
| List Unit Price   | &dollar;61.31/hour |
| Savings           | 33%                |

[CSV Example](/specification/data/commitment_discount_scenarios/azure_reservation_all_upfront_100pct.csv)

## Scenario Description

This example shows a **Microsoft Azure Virtual Machine Reserved Instance** (Azure Reservation), which is a commitment (CommitmentDiscountCategory: Usage) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **All-Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and EffectiveCost=0 (since the cost is amortized to usage rows).

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

| Row Type          | Count | Total BilledCost       | Total EffectiveCost  |
| ----------------- | ----- | ---------------------- | -------------------- |
| Purchase          | 1     | &dollar;358,000.00     | &dollar;0.00         |
| Usage (Used)      | 24    | &dollar;0.00           | &dollar;980.88       |
| Usage (Standard) | 12    | &dollar;22.31          | &dollar;22.31        |
| **Total**         | 37    | **&dollar;358,022.31** | **&dollar;1,003.19** |

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
| **ListUnitPrice**       | List (public) unit price   | &dollar;61.31      | &dollar;61.31 |
| **ContractedUnitPrice** | Negotiated unit price | &dollar;40.87      | null          |

| **ContractedUnitPrice** | Negotiated unit price | &dollar;61.31      | &dollar;61.31 |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario          | BilledCost         | EffectiveCost | ListCost           |
| ----------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row**  | &dollar;358,000.00 | &dollar;0.00  | &dollar;358,000.00 |
| **Used Row**      | &dollar;0.00       | &dollar;40.87 | &dollar;61.31      |
| **Standard Row** | &dollar;3.47       | &dollar;3.47  | &dollar;3.47       |

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
| BilledCost               | &dollar;358,000.00 | Full annual commitment payment                  |
| EffectiveCost            | &dollar;0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                  | One commitment unit purchased                   |
| CommitmentDiscountStatus | null               | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                           |
| -------------------------- | ----------------------------------------------------- | ------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption          |
| PricingCategory            | Committed                                             | Priced under commitment discount              |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment |
| EffectiveCost              | &dollar;40.87                                         | Amortized cost (annual / hours)       |
| ListCost                   | &dollar;61.31                                         | What you would have paid at list price    |
| PricingQuantity            | 1                                                     | Units priced                          |
| ConsumedQuantity           | 1                                                     | Hours used                            |
| CommitmentDiscountQuantity | 1                                                     | Units applied                         |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                    |
| CommitmentDiscountId       | /subscriptions/f0e9d8c7-b6a5-4321-0987-654321fedcb... | Links usage to purchase               |

## Standard Pricing Usage Row Details

| Column                     | Value        | Explanation                   |
| -------------------------- | ------------ | ----------------------------- |
| ChargeCategory             | Usage        | Compute consumption (standard pricing) |
| PricingCategory            | Standard     | No discount applied           |
| BilledCost                 | &dollar;3.47 | List unit price               |
| EffectiveCost              | &dollar;3.47 | = BilledCost                  |
| ListCost                   | &dollar;3.47 | Same as BilledCost            |
| PricingQuantity            | 167          | Units priced                  |
| ConsumedQuantity           | 167          | Hours used                    |
| CommitmentDiscountQuantity | null         | **No commitment applied**     |
| CommitmentDiscountStatus   | null         | No commitment                 |
| CommitmentDiscountId       | (empty)      | No associated commitment      |
| ContractedUnitPrice        | &dollar;61.31 | Equals ListUnitPrice (no negotiated discount) |

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

* Annual commitment: &dollar;358,000.00
* Hours in term: 24
* Hourly amortization: &dollar;358,000.00 / 24 = &dollar;14,916.67/hour
* Daily amortization (365 days): &dollar;358,000.00 / 365 = &dollar;980.82/day
* Sum(Usage EffectiveCost): &dollar;980.88

### All Validation Rules Passed

This example data is valid according to FOCUS commitment discount rules.
