### Conformance Requirements – `Billing Account ID`

| CRID                     | Function         | Reference          | Keyword  | ApplicabilityCriteria                    | Condition | MustSatisfy                                                     | Requirement                                                                                                                                                     | Type   | CRVersionIntroduced | Status | Notes |
| ------------------------ | ---------------- | ------------------ | -------- | ---------------------------------------- | --------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------- | ------ | ----- |
| BillingAccountId-C-000-M | Composite        | Billing Account ID | MUST     | Dataset includes BillingAccountId column | All Rows  | All BillingAccountId rules MUST be enforced.                    | AND(BillingAccountId-D-001-M, BillingAccountId-C-002-M, BillingAccountId-C-003-M, BillingAccountId-C-004-M, BillingAccountId-C-005-M, BillingAccountId-C-006-O) | static | 1.2                 | active |       |
| BillingAccountId-D-001-M | Presence         | Billing Account ID | MUST     | Dataset includes BillingAccountId column | All Rows  | BillingAccountId MUST be present in a FOCUS dataset.            | null                                                                                                                                                            | static | 1.2                 | active |       |
| BillingAccountId-C-002-M | DataType         | Billing Account ID | MUST     | All Rows                                 | All Rows  | BillingAccountId MUST be of type String.                        | null                                                                                                                                                            | static | 1.2                 | active |       |
| BillingAccountId-C-003-M | Validation       | Billing Account ID | MUST     | All Rows                                 | All Rows  | BillingAccountId MUST conform to StringHandling requirements.   | StringHandling\:CR                                                                                                                                              | static | 1.2                 | active |       |
| BillingAccountId-C-004-M | NullabilityRules | Billing Account ID | MUST NOT | All Rows                                 | All Rows  | BillingAccountId MUST NOT be null.                              | null                                                                                                                                                            | static | 1.2                 | active |       |
| BillingAccountId-C-005-M | Validation       | Billing Account ID | MUST     | All Rows                                 | All Rows  | BillingAccountId MUST be a unique identifier within a provider. | null                                                                                                                                                            | static | 1.2                 | active |       |
| BillingAccountId-C-006-O | Validation       | Billing Account ID | SHOULD   | All Rows                                 | All Rows  | BillingAccountId SHOULD be a fully-qualified identifier.        | null                                                                                                                                                            | static | 1.2                 | active |       |


### DAG of Conformance Requirements for `Billing Account ID`
This diagram shows the logical structure and composite dependencies for the CRs of the `Billing Account ID` column in FOCUS v1.2.

```mermaid

graph TD

%% Root Composite
BA000["BillingAccountId-C-000-C: Enforce all BillingAccountId rules"]
BA001["BillingAccountId-D-001-M: MUST be present in dataset"]
BA002["BillingAccountId-C-002-M: MUST be of type String"]
BA003["BillingAccountId-C-003-M: MUST conform to StringHandling"]
BA004["BillingAccountId-C-004-M: MUST NOT be null"]
BA005["BillingAccountId-C-005-M: MUST be a unique identifier within provider"]
BA006["BillingAccountId-C-006-O: SHOULD be a fully-qualified identifier"]

%% Root connections
BA000 --> BA001
BA000 --> BA002
BA000 --> BA003
BA000 --> BA004
BA000 --> BA005
BA000 --> BA006

%% Styling by Rule Type
classDef mandatory fill:#fdd,stroke:#c00,stroke-width:2px;
classDef conditional fill:#ffd700,stroke:#aa0,stroke-width:1px;
classDef optional fill:#c0f5c0,stroke:#2c8c2c,stroke-width:1px;

class BA000 conditional;
class BA001,BA002,BA003,BA004,BA005 mandatory;
class BA006 optional;
```

| Color      | Rule Type     |
|------------|----------------|
| 🔴 `#fdd`   | Mandatory (M)  |
| 🟡 `#ffd700`| Conditional (C)|
| 🟢 `#c0f5c0`| Optional (O)   |
