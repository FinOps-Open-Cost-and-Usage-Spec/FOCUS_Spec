### Static Conformance Requirements – Commitment Discount Quantity

| SCRID                                | Function                               | PreCondition                   | Condition                                                                                      | Requirement                     | ValidationCriteria                                                                                         | Notes                                                                                              | VersionIntroduced | Status  |
|--------------------------------------|----------------------------------------|--------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-------------------|---------|
| COMMITMENTDISCOUNTQUANTITY-C-000-M   | Summary of all applicable rules        | null                           | null                                                                                             | AND(C-001 to C-016)              | MUST satisfy all applicable conformance rules from C-001 to C-016                                         | Aggregates all rules for conformance validation                                                    | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-001-C   | Define presence in dataset             | INCLUDES_COMMITMENT_DISCOUNTS | null                                                                                             | null                             | CommitmentDiscountQuantity MUST be present in the dataset                                                 | Applies only when provider supports commitment discounts                                           | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-002-M   | Specify data type                      | null                           | null                                                                                             | null                             | CommitmentDiscountQuantity MUST be of type Decimal                                                        |                                                                                                    | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-003-M   | Ensure numeric format compliance       | null                           | null                                                                                             | null                             | CommitmentDiscountQuantity MUST conform to NumericFormat                                                  |                                                                                                    | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-004-M   | Group nullability logic (primary split)| null                           | null                                                                                             | OR(COMMITMENTDISCOUNTQUANTITY-C-005-C, COMMITMENTDISCOUNTQUANTITY-C-008-C) | null                                                                                                      | Combines valid nullability paths                                                                 | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-005-C   | Conditional nullability logic          | null                           | ChargeCategory ∈ {"Usage", "Purchase"} AND CommitmentDiscountId is not null                     | OR(COMMITMENTDISCOUNTQUANTITY-C-006-M, COMMITMENTDISCOUNTQUANTITY-C-007-O) | null                                                                                                      | Delegates to null rules based on ChargeClass                                                      | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-006-M   | Disallow null when required            | null                           | ChargeClass ≠ "Correction"                                                                       | null                             | CommitmentDiscountQuantity MUST NOT be null                                                               |                                                                                                    | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-007-O   | Allow null for correction charges      | null                           | ChargeClass = "Correction"                                                                       | null                             | CommitmentDiscountQuantity MAY be null                                                                    |                                                                                                    | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-008-C   | Disallow presence in other cases       | null                           | All other cases                                                                                   | null                             | CommitmentDiscountQuantity MUST be null                                                                   | Ensures no leakage of values outside valid context                                                | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-009-C   | Apply value and semantics if present   | null                           | ChargeCategory ∈ {"Usage", "Purchase"} AND CommitmentDiscountId is not null                      | AND(COMMITMENTDISCOUNTQUANTITY-C-010-C, COMMITMENTDISCOUNTQUANTITY-C-011-C, COMMITMENTDISCOUNTQUANTITY-C-014-C) | MUST satisfy all semantic and value conditions if value is present                                      | Composite enforcement of format + semantics                                                       | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-010-C   | Validate decimal values                | null                           | CommitmentDiscountQuantity is not null                                                           | null                             | CommitmentDiscountQuantity MUST be a valid decimal value                                                  |                                                                                                    | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-011-C   | Group purchase logic                   | null                           | ChargeCategory = "Purchase"                                                                      | OR(COMMITMENTDISCOUNTQUANTITY-C-012-C, COMMITMENTDISCOUNTQUANTITY-C-013-C) | null                                                                                                      | Split logic based on one-time vs recurring                                                        | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-012-C   | Purchase - one-time                    | null                           | ChargeFrequency = "One-Time" AND ChargeCategory = "Purchase"                                     | null                             | MUST represent quantity of CommitmentDiscountUnit eligible over the term                                 |                                                                                                    | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-013-C   | Purchase - recurring                   | null                           | ChargeFrequency = "Recurring" AND ChargeCategory = "Purchase"                                    | null                             | MUST represent quantity eligible per charge period                                                        |                                                                                                    | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-014-C   | Group usage logic                      | null                           | ChargeCategory = "Usage"                                                                         | OR(COMMITMENTDISCOUNTQUANTITY-C-015-C, COMMITMENTDISCOUNTQUANTITY-C-016-C) | null                                                                                                      | Dispatches to Used/Unused based on CommitmentDiscountStatus                                     | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-015-C   | Usage - used quantity                  | null                           | CommitmentDiscountStatus = "Used" AND ChargeCategory = "Usage"                                   | null                             | MUST represent metered quantity consumed during the charge period                                         |                                                                                                    | 1.1               | active  |
| COMMITMENTDISCOUNTQUANTITY-C-016-C   | Usage - unused quantity                | null                           | CommitmentDiscountStatus = "Unused" AND ChargeCategory = "Usage"                                 | null                             | MUST represent remaining, unused quantity during the charge period                                       |                                                                                                    | 1.1               | active  |


### DAG of Static Conformance Requirements for `CommitmentDiscountQuantity`

This diagram shows the logical structure and composite dependencies for the SCRs of the `CommitmentDiscountQuantity` column in FOCUS v1.2.

```mermaid
graph TD

%% Root Composite
C000["C-000-M: Summary of all rules"]
C001["C-001-C: Define presence"]
C002["C-002-M: Type is Decimal"]
C003["C-003-M: Numeric format"]
C004["C-004-M: Nullability grouping"]
C009["C-009-C: Value+Semantics grouping"]

%% Nullability Branch
C004 --> C005["C-005-C: Conditional nullability"]
C004 --> C008["C-008-C: Null otherwise"]

C005 --> C006["C-006-M: MUST NOT be null"]
C005 --> C007["C-007-O: MAY be null (Correction)"]

%% Value + Semantics Branch
C009 --> C010["C-010-C: Decimal validity"]
C009 --> C011["C-011-C: Purchase logic group"]
C009 --> C014["C-014-C: Usage logic group"]

%% Purchase Sub-branch
C011 --> C012["C-012-C: One-Time Purchase"]
C011 --> C013["C-013-C: Recurring Purchase"]

%% Usage Sub-branch
C014 --> C015["C-015-C: Used Quantity"]
C014 --> C016["C-016-C: Unused Quantity"]

%% Root connections
C000 --> C001
C000 --> C002
C000 --> C003
C000 --> C004
C000 --> C009

%% Styling by Rule Type
classDef mandatory fill:#fdd,stroke:#c00,stroke-width:2px;
classDef conditional fill:#ffd700,stroke:#aa0,stroke-width:1px;
classDef optional fill:#c0f5c0,stroke:#2c8c2c,stroke-width:1px;

class C000,C002,C003,C004,C006 mandatory;
class C001,C005,C008,C009,C010,C011,C012,C013,C014,C015,C016 conditional;
class C007 optional;
```
| Color      | Rule Type     |
|------------|----------------|
| 🔴 `#fdd`   | Mandatory (M)  |
| 🟡 `#ffd700`| Conditional (C)|
| 🟢 `#c0f5c0`| Optional (O)   |