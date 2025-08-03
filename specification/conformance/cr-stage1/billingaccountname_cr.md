### Conformance Requirements – `Billing Account Name`

| CRID                       | Function         | Reference            | Keyword | ApplicabilityCriteria                                     | Condition | MustSatisfy                                                      | Requirement                                                                                                         | Type   | CRVersionIntroduced | Status | Notes                                         |
| -------------------------- | ---------------- | -------------------- | ------- | --------------------------------------------------------- | --------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------ | ------------------- | ------ | --------------------------------------------- |
| BillingAccountName-C-000-C | Composite        | Billing Account Name | MUST    | Dataset includes BillingAccountName column                | All_Rows | All BillingAccountName rules MUST be enforced                    | AND(BillingAccountName-D-001-M, BillingAccountName-C-002-M, BillingAccountName-C-003-M, BillingAccountName-C-004-C) | static | 1.2                 | active |                                               |
| BillingAccountName-D-001-M | Presence         | Billing Account Name | MUST    | Dataset includes BillingAccountName column                | All_Rows | MUST be present in a FOCUS dataset                               | null                                                                                                                | static | 1.2                 | active |                                               |
| BillingAccountName-C-002-M | DataType         | Billing Account Name | MUST    | All_Rows                                                  | All_Rows | MUST be of type String                                           | null                                                                                                                | static | 1.2                 | active |                                               |
| BillingAccountName-C-003-M | Format           | Billing Account Name | MUST    | All_Rows                                                  | All_Rows | MUST conform to StringHandling                                   | StringHandling\:CR                                                                                                  | static | 1.2                 | active | Cross-attribute reference: StringHandling\:CR |
| BillingAccountName-C-004-C | NullabilityRules | Billing Account Name | MUST    | Provider supports assigning a billing account display name | All_Rows | MUST NOT be null when provider supports assigning a display name | null                                                                                                                | static | 1.2                 | active |                                               |

### DAG of Conformance Requirements for `Billing Account Name`
This diagram shows the logical structure and composite dependencies for the CRs of the `Billing Account Name` column in FOCUS v1.2.

```mermaid

graph TD

%% Nodes
BAN000["BillingAccountName-C-000-C: Enforce all BillingAccountName rules"]
BAN001["BillingAccountName-D-001-M: Column MUST be present in a FOCUS dataset"]
BAN002["BillingAccountName-C-002-M: Column MUST be of type String"]
BAN003["BillingAccountName-C-003-M: Column MUST conform to StringHandling rules"]
BAN004["BillingAccountName-C-004-C: Column MUST NOT be null when provider assigns display name"]

%% Root connections
BAN000 --> BAN001
BAN000 --> BAN002
BAN000 --> BAN003
BAN000 --> BAN004

%% External Attribute Rule
SHCR["StringHandling:CR"]
BAN003 --> SHCR

%% Styling by Rule Type
classDef mandatory fill:#fdd,stroke:#c00,stroke-width:2px;
classDef conditional fill:#ffd700,stroke:#aa0,stroke-width:1px;
classDef optional fill:#c0f5c0,stroke:#2c8c2c,stroke-width:1px;

class BAN000,BAN004 conditional;
class BAN001,BAN002,BAN003 mandatory;
class SHCR mandatory;
```


| Color      | Rule Type     |
|------------|----------------|
| 🔴 `#fdd`   | Mandatory (M)  |
| 🟡 `#ffd700`| Conditional (C)|
| 🟢 `#c0f5c0`| Optional (O)   |

