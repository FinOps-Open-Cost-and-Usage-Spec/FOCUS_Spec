### Static Conformance Requirements – `Billed Cost`

| CRID               | Function         | Reference   | Keyword  | ApplicabilityCriteria | MustSatisfy                                                           | Requirement                                                                                                                                     | Condition                  | Type    | CRVersionIntroduced | Status | Notes                                     |
| ------------------ | ---------------- | ----------- | -------- | --------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------- | ------------------- | ------ | ----------------------------------------- |
| BILLEDCOST-C-000-M | Composite        | Billed Cost | MUST     | All_Rows              | All BilledCost rules MUST be enforced                                 | AND(BILLEDCOST-C-001-M, BILLEDCOST-C-002-M, BILLEDCOST-C-003-M, BILLEDCOST-C-004-M, BILLEDCOST-C-005-M, BILLEDCOST-C-006-M, BILLEDCOST-C-007-M) | ALL_ROWS                   | static  | 1.2                 | active |                                           |
| BILLEDCOST-D-001-M | Presence         | Billed Cost | MUST     | All_Rows              | MUST be present in a FOCUS dataset                                    | null                                                                                                                                            | ALL_ROWS                   | static  | 1.2                 | active |                                           |
| BILLEDCOST-C-002-M | DataType         | Billed Cost | MUST     | All_Rows              | MUST be of type Decimal                                               | null                                                                                                                                            | ALL_ROWS                   | static  | 1.2                 | active |                                           |
| BILLEDCOST-C-003-M | Format           | Billed Cost | MUST     | All_Rows              | MUST conform to NumericFormat                                         | null                                                                                                                                            | ALL_ROWS                   | static  | 1.2                 | active |                                           |
| BILLEDCOST-C-004-M | Validation       | Billed Cost | MUST     | All_Rows              | MUST be a valid decimal value                                         | null                                                                                                                                            | ALL_ROWS                   | static  | 1.2                 | active |                                           |
| BILLEDCOST-C-005-M | NullabilityRules | Billed Cost | MUST NOT | All_Rows              | MUST NOT be null                                                      | null                                                                                                                                            | ALL_ROWS                   | static  | 1.2                 | active |                                           |
| BILLEDCOST-C-006-M | Validation       | Billed Cost | MUST     | All_Rows              | MUST be 0 for charges where payments are received by a third party    | null                                                                                                                                            | ChargeType = "Marketplace" | static  | 1.2                 | active |                                           |
| BILLEDCOST-C-007-M | Validation       | Billed Cost | MUST     | All_Rows              | MUST be denominated in the BillingCurrency                            | null                                                                                                                                            | ALL_ROWS                   | static  | 1.2                 | active |                                           |
| BILLEDCOST-C-008-M | Validation       | Billed Cost | MUST     | All_Rows              | MUST match the sum of the payable amount on the corresponding invoice | null                                                                                                                                            | Aggregated by InvoiceId    | dynamic | 1.2                 | active | Cross-column reference: INVOICEID-C-001-M |


### DAG of Static Conformance Requirements for `Billed Cost`

This diagram shows the logical structure and composite dependencies for the SCRs of the `Billed Cost` column in FOCUS v1.2.

```mermaid
graph TD

%% Root Composite
BC000["C-000-M: Summary of all rules"]
BC001["D-001-M: MUST be present"]
BC002["C-002-M: Type is Decimal"]
BC003["C-003-M: Numeric format"]
BC004["C-004-M: Valid decimal"]
BC005["C-005-M: MUST NOT be null"]
BC006["C-006-M: 0 for marketplace charges"]
BC007["C-007-M: Denominated in BillingCurrency"]
BC008["C-008-M: MUST match invoice total"]

%% Root connections
BC000 --> BC001
BC000 --> BC002
BC000 --> BC003
BC000 --> BC004
BC000 --> BC005
BC000 --> BC006
BC000 --> BC007
BC000 --> BC008

%% Styling by Rule Type
classDef mandatory fill:#fdd,stroke:#c00,stroke-width:2px;
classDef conditional fill:#ffd700,stroke:#aa0,stroke-width:1px;
classDef optional fill:#c0f5c0,stroke:#2c8c2c,stroke-width:1px;

class BC000,BC001,BC002,BC003,BC004,BC005,BC006,BC007,BC008 mandatory;
```