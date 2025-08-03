### Conformance Requirements – `Commitment Discount Quantity`
text: [commitmentdiscountquantity-v1_2.md](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/v1.2/specification/columns/commitmentdiscountquantity.md)

These requirements define the mandatory structure and validation rules for the `Commitment Discount Quantity` column in FOCUS version 1.2.

| CRID                               | Function         | Reference                    | Keyword  | ApplicabilityCriteria                  | Condition                                                                                                   | MustSatisfy                                                                                          | Requirement                                                                                                                                                                             | Type   | CRVersionIntroduced | Status | Notes                                        |
| ---------------------------------- | ---------------- | ---------------------------- | -------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------- | ------ | -------------------------------------------- |
| CommitmentDiscountQuantity-C-000-C | Composite        | Commitment Discount Quantity | MUST     | Provider supports commitment discounts | All_Rows                                                                                                   | All CommitmentDiscountQuantity rules MUST be enforced                                                | AND(CommitmentDiscountQuantity-D-001-C, CommitmentDiscountQuantity-C-002-M, CommitmentDiscountQuantity-C-003-M, CommitmentDiscountQuantity-C-004-C, CommitmentDiscountQuantity-C-009-C) | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-D-001-C | Presence         | Commitment Discount Quantity | MUST     | Provider supports commitment discounts | All_Rows                                                                                                   | MUST be present in a FOCUS dataset                                                                   | null                                                                                                                                                                                    | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-002-M | DataType         | Commitment Discount Quantity | MUST     | All_Rows                              | All_Rows                                                                                                   | MUST be of type Decimal                                                                              | null                                                                                                                                                                                    | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-003-M | Format           | Commitment Discount Quantity | MUST     | All_Rows                              | All_Rows                                                                                                   | MUST conform to NumericFormat                                                                        | NumericFormat:CR                                                                                                                                                                       | static | 1.2                 | active | Cross-attribute reference: NumericFormat\:CR |
| CommitmentDiscountQuantity-C-004-C | Composite        | Commitment Discount Quantity | MUST     | All_Rows                              | All_Rows                                                                                                   | Nullability MUST follow conditional rules                                                            | AND(CommitmentDiscountQuantity-C-005-C, CommitmentDiscountQuantity-C-008-M)                                                                                                             | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-005-C | Composite        | Commitment Discount Quantity | MUST     | All_Rows                              | ChargeCategory IN ("Usage", "Purchase") AND CommitmentDiscountId IS NOT NULL                                | Conditional nullability rules for non-Correction charges MUST be enforced                            | AND(CommitmentDiscountQuantity-C-006-M, CommitmentDiscountQuantity-C-007-O)                                                                                                             | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-006-M | NullabilityRules | Commitment Discount Quantity | MUST NOT | All_Rows                              | ChargeCategory IN ("Usage", "Purchase") AND CommitmentDiscountId IS NOT NULL AND ChargeClass ≠ "Correction" | MUST NOT be null                                                                                     | null                                                                                                                                                                                    | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-007-O | NullabilityRules | Commitment Discount Quantity | MAY      | All_Rows                              | ChargeCategory IN ("Usage", "Purchase") AND CommitmentDiscountId IS NOT NULL AND ChargeClass = "Correction" | MAY be null                                                                                          | null                                                                                                                                                                                    | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-008-M | NullabilityRules | Commitment Discount Quantity | MUST     | All_Rows                              | All other cases (not matched by above conditions)                                                           | MUST be null                                                                                         | null                                                                                                                                                                                    | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-009-C | Composite        | Commitment Discount Quantity | MUST     | All_Rows                              | CommitmentDiscountQuantity IS NOT NULL                                                                      | Rules for interpreting non-null CommitmentDiscountQuantity MUST be enforced                          | AND(CommitmentDiscountQuantity-C-010-M, CommitmentDiscountQuantity-C-011-C, CommitmentDiscountQuantity-C-012-C)                                                                         | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-010-M | Validation       | Commitment Discount Quantity | MUST     | All_Rows                              | CommitmentDiscountQuantity IS NOT NULL                                                                      | MUST be a valid decimal value                                                                        | null                                                                                                                                                                                    | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-011-C | Composite        | Commitment Discount Quantity | MUST     | All_Rows                              | ChargeCategory = "Purchase" AND CommitmentDiscountQuantity IS NOT NULL                                      | Purchase ChargeQuantity interpretation rules MUST be enforced                                        | AND(CommitmentDiscountQuantity-C-013-M, CommitmentDiscountQuantity-C-014-M)                                                                                                             | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-012-C | Composite        | Commitment Discount Quantity | MUST     | All_Rows                              | ChargeCategory = "Usage" AND CommitmentDiscountQuantity IS NOT NULL                                         | Usage ChargeQuantity interpretation rules MUST be enforced                                           | AND(CommitmentDiscountQuantity-C-015-M, CommitmentDiscountQuantity-C-016-M)                                                                                                             | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-013-M | Validation       | Commitment Discount Quantity | MUST     | All_Rows                              | ChargeCategory = "Purchase" AND ChargeFrequency = "One-Time"                                                | MUST be the quantity of CommitmentDiscountUnit, paid upfront, eligible over commitment discount term | null                                                                                                                                                                                    | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-014-M | Validation       | Commitment Discount Quantity | MUST     | All_Rows                              | ChargeCategory = "Purchase" AND ChargeFrequency = "Recurring"                                               | MUST be the quantity of CommitmentDiscountUnit eligible per charge period                            | null                                                                                                                                                                                    | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-015-M | Validation       | Commitment Discount Quantity | MUST     | All_Rows                              | ChargeCategory = "Usage" AND CommitmentDiscountStatus = "Used"                                              | MUST be the metered quantity of CommitmentDiscountUnit consumed in the charge period                 | null                                                                                                                                                                                    | static | 1.2                 | active |                                              |
| CommitmentDiscountQuantity-C-016-M | Validation       | Commitment Discount Quantity | MUST     | All_Rows                              | ChargeCategory = "Usage" AND CommitmentDiscountStatus = "Unused"                                            | MUST be the unused quantity of CommitmentDiscountUnit in the charge period                           | null                                                                                                                                                                                    | static | 1.2                 | active |                                              |

### DAG of Conformance Requirements for `Commitment Discount Quantity`

This diagram shows the logical structure and composite dependencies for the CRs of the `Commitment Discount Quantity` column in FOCUS v1.2.

```mermaid

graph TD

%% Root Composite
CDQ000["CommitmentDiscountQuantity-C-000-C: Enforce all CommitmentDiscountQuantity rules"]
CDQ001["CommitmentDiscountQuantity-D-001-C: MUST be present in FOCUS dataset"]
CDQ002["CommitmentDiscountQuantity-C-002-M: MUST be of type Decimal"]
CDQ003["CommitmentDiscountQuantity-C-003-M: MUST conform to NumericFormat"]
CDQ004["CommitmentDiscountQuantity-C-004-C: Nullability MUST follow conditional rules"]
CDQ009["CommitmentDiscountQuantity-C-009-C: Rules for interpreting non-null values MUST be enforced"]

%% Nullability Composites
CDQ004 --> CDQ005
CDQ004 --> CDQ008
CDQ005["CommitmentDiscountQuantity-C-005-C: Nullability for Usage/Purchase with CommitmentDiscountId"]
CDQ008["CommitmentDiscountQuantity-C-008-M: MUST be null in all other cases"]

CDQ005 --> CDQ006
CDQ005 --> CDQ007
CDQ006["CommitmentDiscountQuantity-C-006-M: MUST NOT be null unless ChargeClass = Correction"]
CDQ007["CommitmentDiscountQuantity-C-007-O: MAY be null when ChargeClass = Correction"]

%% Non-null interpretation composite
CDQ009 --> CDQ010
CDQ009 --> CDQ011
CDQ009 --> CDQ012

CDQ010["CommitmentDiscountQuantity-C-010-M: MUST be a valid decimal value"]

%% Purchase case
CDQ011["CommitmentDiscountQuantity-C-011-C: Purchase interpretation rules"]
CDQ011 --> CDQ013
CDQ011 --> CDQ014
CDQ013["CommitmentDiscountQuantity-C-013-M: One-Time purchase quantity rule"]
CDQ014["CommitmentDiscountQuantity-C-014-M: Recurring purchase quantity rule"]

%% Usage case
CDQ012["CommitmentDiscountQuantity-C-012-C: Usage interpretation rules"]
CDQ012 --> CDQ015
CDQ012 --> CDQ016
CDQ015["CommitmentDiscountQuantity-C-015-M: Used commitment discount quantity"]
CDQ016["CommitmentDiscountQuantity-C-016-M: Unused commitment discount quantity"]

%% Root connections
CDQ000 --> CDQ001
CDQ000 --> CDQ002
CDQ000 --> CDQ003
CDQ000 --> CDQ004
CDQ000 --> CDQ009

%% External attribute rule
CDQ003 --> NF["NumericFormat:CR"]

%% Styling by Rule Type
classDef mandatory fill:#fdd,stroke:#c00,stroke-width:2px;
classDef conditional fill:#ffd700,stroke:#aa0,stroke-width:1px;
classDef optional fill:#c0f5c0,stroke:#2c8c2c,stroke-width:1px;

class CDQ002,CDQ003,CDQ006,CDQ008,CDQ010,CDQ013,CDQ014,CDQ015,CDQ016 mandatory;
class CDQ000,CDQ001,CDQ004,CDQ005,CDQ009,CDQ011,CDQ012 conditional;
class CDQ007 optional;
class NF mandatory;
```
| Color      | Rule Type     |
|------------|----------------|
| 🔴 `#fdd`   | Mandatory (M)  |
| 🟡 `#ffd700`| Conditional (C)|
| 🟢 `#c0f5c0`| Optional (O)   |