### Conformance Requirements – `Charge Category`

text: [chargecategory-v1_2.md](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/v1.2/specification/columns/chargecategory.md)

These requirements define the mandatory structure and validation rules for the `Charge Category` column in FOCUS version 1.2.

| CRID                   | Function         | Reference       | Keyword  | ApplicabilityCriteria                  | Condition | MustSatisfy                                | Requirement                                                                                         | Type   | CRVersionIntroduced | Status | Notes |
| ---------------------- | ---------------- | --------------- | -------- | -------------------------------------- | --------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------- | ------ | ------------------- | ------ | ----- |
| ChargeCategory-C-000-M | Composite        | Charge Category | MUST     | All_Rows                              | All_Rows | All Charge Category rules MUST be enforced | AND(ChargeCategory-D-001-M, ChargeCategory-C-002-M, ChargeCategory-C-003-M, ChargeCategory-C-004-M) | static | 1.2                 | active |       |
| ChargeCategory-D-001-M | Presence         | Charge Category | MUST     | Dataset includes ChargeCategory column | All_Rows | MUST be present in a FOCUS dataset         | null                                                                                                | static | 1.2                 | active |       |
| ChargeCategory-C-002-M | DataType         | Charge Category | MUST     | All_Rows                              | All_Rows | MUST be of type String                     | null                                                                                                | static | 1.2                 | active |       |
| ChargeCategory-C-003-M | NullabilityRules | Charge Category | MUST NOT | All_Rows                              | All_Rows | MUST NOT be null                           | null                                                                                                | static | 1.2                 | active |       |
| ChargeCategory-C-004-M | Validation       | Charge Category | MUST     | All_Rows                              | All_Rows | MUST be one of the allowed values          | null                                                                                                | static | 1.2                 | active |       |

### DAG of Conformance Requirements for `Charge Category`
This diagram shows the logical structure and composite dependencies for the CRs of the `Charge Category` column in FOCUS v1.2.

```mermaid

graph TD

%% Root Composite
CC000["ChargeCategory-C-000-M: Enforce all ChargeCategory rules"]
CC001["ChargeCategory-D-001-M: MUST be present in dataset"]
CC002["ChargeCategory-C-002-M: MUST be of type String"]
CC003["ChargeCategory-C-003-M: MUST NOT be null"]
CC004["ChargeCategory-C-004-M: MUST be one of the allowed values"]

%% Root connections
CC000 --> CC001
CC000 --> CC002
CC000 --> CC003
CC000 --> CC004

%% Styling by Rule Type
classDef mandatory fill:#fdd,stroke:#c00,stroke-width:2px;
classDef conditional fill:#ffd700,stroke:#aa0,stroke-width:1px;
classDef optional fill:#c0f5c0,stroke:#2c8c2c,stroke-width:1px;

class CC000,CC001,CC002,CC003,CC004 mandatory;
```

| Node Type          | Description                                                                 |
|--------------------|------------------------------|
| 🟥 Red (C-XXX-M)    | **Mandatory (M)**            |
| 🟨 Yellow (C-XXX-C) | **Conditional (C)**          |
| 🟩 Green (C-XXX-O)  | **Optional (O)**             |