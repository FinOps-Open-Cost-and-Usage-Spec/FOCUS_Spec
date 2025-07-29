### Static Conformance Requirements – Billing Account Type

| CRID                      | Function         | Reference            | Keyword  | ApplicabilityCriteria                                             | MustSatisfy                                                                 | Requirement                                                                                                                                                        | Condition                                 | Type    | CRVersionIntroduced | Status | Notes                                     |
|---------------------------|------------------|----------------------|----------|------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|---------|---------------------|--------|-------------------------------------------|
| BILLINGACCOUNTTYPE-C-000-M | Composite        | Billing Account Type | MUST     | All_Rows                                                         | All BillingAccountType rules MUST be enforced                              | AND(BILLINGACCOUNTTYPE-D-001-C, BILLINGACCOUNTTYPE-C-002-M, BILLINGACCOUNTTYPE-C-003-M, BILLINGACCOUNTTYPE-C-004-C, BILLINGACCOUNTTYPE-C-007-M)                  | ALL_ROWS                                 | static  | 1.2                 | active |                                           |
| BILLINGACCOUNTTYPE-D-001-C | Presence         | Billing Account Type | MUST     | Provider supports multiple BillingAccountType values             | MUST be present in a FOCUS dataset                                         | null                                                                                                                                                             | Provider supports multiple values         | static  | 1.2                 | active |                                           |
| BILLINGACCOUNTTYPE-C-002-M | DataType         | Billing Account Type | MUST     | All_Rows                                                         | MUST be of type String                                                     | null                                                                                                                                                             | ALL_ROWS                                 | static  | 1.2                 | active |                                           |
| BILLINGACCOUNTTYPE-C-003-M | Validation       | Billing Account Type | MUST     | All_Rows                                                         | MUST conform to StringHandling requirements                                | null                                                                                                                                                             | ALL_ROWS                                 | static  | 1.2                 | active |                                           |
| BILLINGACCOUNTTYPE-C-004-C | Composite        | Billing Account Type | MUST     | All_Rows                                                         | Nullability rules MUST be enforced                                         | AND(BILLINGACCOUNTTYPE-C-005-M, BILLINGACCOUNTTYPE-C-006-M)                                                                                                       | ALL_ROWS                                 | static  | 1.2                 | active |                                           |
| BILLINGACCOUNTTYPE-C-005-M | NullabilityRules | Billing Account Type | MUST     | All_Rows                                                         | MUST be null when BillingAccountId is null                                 | null                                                                                                                                                             | BillingAccountId IS NULL                 | static  | 1.2                 | active | Cross-column reference: BILLINGACCOUNTID  |
| BILLINGACCOUNTTYPE-C-006-M | NullabilityRules | Billing Account Type | MUST     | All_Rows                                                         | MUST NOT be null when BillingAccountId is not null                         | null                                                                                                                                                             | BillingAccountId IS NOT NULL             | static  | 1.2                 | active | Cross-column reference: BILLINGACCOUNTID  |
| BILLINGACCOUNTTYPE-C-007-M | Validation       | Billing Account Type | MUST     | All_Rows                                                         | MUST be a consistent, readable display value                               | null                                                                                                                                                             | ALL_ROWS                                 | static  | 1.2                 | active |                                           |


### DAG of Static Conformance Requirements for `Billing Account Type`
This diagram shows the logical structure and composite dependencies for the SCRs of the `Billing Account Type` column in FOCUS v1.2.

```mermaid
graph TD

%% Root Composite
BAT000["C-000-M: Summary of all rules"]
BAT001["D-001-C: Presence when provider supports multiple types"]
BAT002["C-002-M: Type is String"]
BAT003["C-003-M: Conform to StringHandling"]
BAT004["C-004-C: Enforce nullability rules"]
BAT005["C-005-M: MUST be null if BillingAccountId is null"]
BAT006["C-006-M: MUST NOT be null if BillingAccountId is not null"]
BAT007["C-007-M: Consistent readable value"]

%% Root connections
BAT000 --> BAT001
BAT000 --> BAT002
BAT000 --> BAT003
BAT000 --> BAT004
BAT000 --> BAT007

%% Nullability composite connections
BAT004 --> BAT005
BAT004 --> BAT006

%% Styling by Rule Type
classDef mandatory fill:#fdd,stroke:#c00,stroke-width:2px;
classDef conditional fill:#ffd700,stroke:#aa0,stroke-width:1px;
classDef optional fill:#c0f5c0,stroke:#2c8c2c,stroke-width:1px;

class BAT000 mandatory;
class BAT001 conditional;
class BAT002,BAT003,BAT005,BAT006,BAT007 mandatory;
class BAT004 conditional;
```

| Color      | Rule Type     |
|------------|----------------|
| 🔴 `#fdd`   | Mandatory (M)  |
| 🟡 `#ffd700`| Conditional (C)|
| 🟢 `#c0f5c0`| Optional (O)   |
