### Conformance Requirements – `Billed Cost`

| CRID               | Function         | Reference   | Keyword  | ApplicabilityCriteria | Condition                            | MustSatisfy                                                           | Requirement                                                                                                                                     | Type    | CRVersionIntroduced | Status | Notes                                     |
| ------------------ | ---------------- | ----------- | -------- | --------------------- | ------------------------------------ | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------- | ------ | ----------------------------------------- |
| BilledCost-C-000-M | Composite        | Billed Cost | MUST     | Dataset includes BilledCost column | All_Rows                             | All BilledCost rules MUST be enforced                                 | AND(BilledCost-D-001-M, BilledCost-C-002-M, BilledCost-C-003-M, BilledCost-C-004-M, BilledCost-C-005-M, BilledCost-C-006-M, BilledCost-C-007-M, BilledCost-C-008-M) | static  | 1.2                 | active |                                           |
| BilledCost-D-001-M | Presence         | Billed Cost | MUST     | Dataset includes BilledCost column | All_Rows                             | MUST be present in a FOCUS dataset                                    | null                                                                                                                                             | static  | 1.2                 | active |                                           |
| BilledCost-C-002-M | DataType         | Billed Cost | MUST     | All_Rows              | All_Rows                             | MUST be of type Decimal                                               | null                                                                                                                                             | static  | 1.2                 | active |                                           |
| BilledCost-C-003-M | Format           | Billed Cost | MUST     | All_Rows              | All_Rows                             | MUST conform to NumericFormat                                         | NumericFormat:CR                                                                                                                                              | static  | 1.2                 | active | Cross-attribute reference: NumericFormat:CR |
| BilledCost-C-004-M | NullabilityRules | Billed Cost | MUST NOT | All_Rows              | All_Rows                             | MUST NOT be null                                                      | null                                                                                                                                             | static  | 1.2                 | active |                                           |
| BilledCost-C-005-M | Validation       | Billed Cost | MUST     | All_Rows              | All_Rows                             | MUST be a valid decimal value                                         | null                                                                                                                                             | static  | 1.2                 | active |                                           |
| BilledCost-C-006-M | Validation       | Billed Cost | MUST     | All_Rows              | ChargeType = "Marketplace"           | MUST be 0 for charges where payments are received by a third party    | null                                                                                                                                             | static  | 1.2                 | active |                                           |
| BilledCost-C-007-M | Validation       | Billed Cost | MUST     | All_Rows              | All_Rows                             | MUST be denominated in the BillingCurrency                            | null                                                                                                                                             | static  | 1.2                 | active | Cross-column reference: BillingCurrency-C-001-M |
| BilledCost-C-008-M | Validation       | Billed Cost | MUST     | All_Rows              | Aggregated by InvoiceId              | MUST match the sum of the payable amount on the corresponding invoice | null                                                                                                                                             | dynamic | 1.2                 | active | Cross-column reference: InvoiceId-C-001-M; Cross-column reference: InvoiceIssuer-C-001-M |

### DAG of Conformance Requirements for `Billed Cost`

This diagram shows the logical structure and composite dependencies for the CRs of the `Billed Cost` column in FOCUS v1.2.

```mermaid

graph TD

%% Root Composite
BC000["BilledCost-C-000-M: Enforce all BilledCost rules"]
BC001["BilledCost-D-001-M: MUST be present in a FOCUS dataset"]
BC002["BilledCost-C-002-M: MUST be of type Decimal"]
BC003["BilledCost-C-003-M: MUST conform to NumericFormat"]
BC004["BilledCost-C-004-M: MUST NOT be null"]
BC005["BilledCost-C-005-M: MUST be a valid decimal value"]
BC006["BilledCost-C-006-M: MUST be 0 for marketplace transactions"]
BC007["BilledCost-C-007-M: MUST be denominated in BillingCurrency"]
BC008["BilledCost-C-008-M: MUST match invoice total for given InvoiceId"]

%% Attribute dependency
NFCR["NumericFormat:CR"]

%% Root connections
BC000 --> BC001
BC000 --> BC002
BC000 --> BC003
BC000 --> BC004
BC000 --> BC005
BC000 --> BC006
BC000 --> BC007
BC000 --> BC008

%% Attribute reference
BC003 --> NFCR

%% Styling by Rule Type
classDef mandatory fill:#fdd,stroke:#c00,stroke-width:2px;
classDef conditional fill:#ffd700,stroke:#aa0,stroke-width:1px;
classDef optional fill:#c0f5c0,stroke:#2c8c2c,stroke-width:1px;

class BC000,BC001,BC002,BC003,BC004,BC005,BC006,BC007,BC008 mandatory;
class NFCR mandatory;
```


| Color        | Rule Type       |
| ------------ | --------------- |
| 🔴 `#fdd`    | Mandatory (M)   |
| 🟡 `#ffd700` | Conditional (C) |
| 🟢 `#c0f5c0` | Optional (O)    |
