### Static Conformance Requirements – Availability Zone

 CRID                     | Function         | Reference         | Keyword  | ApplicabilityCriteria                         | MustSatisfy                                                          | Requirement                                                                                                                           | Condition                                       | Type    | CRVersionIntroduced | Status | Notes |
|--------------------------|------------------|-------------------|----------|----------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|---------|----------------------|--------|-------|
| AVAILABILITYZONE-C-000-M | Composite         | Availability Zone | MUST     | All_Rows                                     | All AvailabilityZone rules MUST be enforced                          | AND(AVAILABILITYZONE-C-001-C, AVAILABILITYZONE-C-002-M, AVAILABILITYZONE-C-003-M, AVAILABILITYZONE-C-004-M)                          | ALL_ROWS                                       | static  | 1.2                  | active |       |
| AVAILABILITYZONE-C-001-C | Presence          | Availability Zone | SHOULD   | Provider supports availability zone deployment | SHOULD be present in a FOCUS dataset                                 | null                                                                                                                                | ALL_ROWS                                       | static  | 1.2                  | active |       |
| AVAILABILITYZONE-C-002-M | DataType          | Availability Zone | MUST     | All_Rows                                     | MUST be of type String                                               | null                                                                                                                                | ALL_ROWS                                       | static  | 1.2                  | active |       |
| AVAILABILITYZONE-C-003-M | Format            | Availability Zone | MUST     | All_Rows                                     | MUST conform to StringHandling requirements                          | null                                                                                                                                | ALL_ROWS                                       | static  | 1.2                  | active |       |
| AVAILABILITYZONE-C-004-M | NullabilityRules  | Availability Zone | MUST     | All_Rows                                     | MUST be null when charge is not specific to an availability zone     | null                                                                                                                                | Charge does not relate to a specific zone     | static  | 1.2                  | active |       |

### DAG of Static Conformance Requirements for `Availability Zone`

This diagram shows the logical structure and composite dependencies for the SCRs of the `Availability Zone` column in FOCUS v1.2.

```mermaid
graph TD

%% Root Composite
AZ000["C-000-M: Summary of all rules"]
AZ001["C-001-C: SHOULD be present if AZs are supported"]
AZ002["C-002-M: Type is String"]
AZ003["C-003-M: Conform to StringHandling"]
AZ004["C-004-M: Null when not tied to specific AZ"]

%% Root connections
AZ000 --> AZ001
AZ000 --> AZ002
AZ000 --> AZ003
AZ000 --> AZ004

%% Styling by Rule Type
classDef mandatory fill:#fdd,stroke:#c00,stroke-width:2px;
classDef conditional fill:#ffd700,stroke:#aa0,stroke-width:1px;
classDef optional fill:#c0f5c0,stroke:#2c8c2c,stroke-width:1px;

class AZ000 mandatory;
class AZ001 conditional;
class AZ002,AZ003,AZ004 mandatory;
```

| Color      | Rule Type     |
|------------|----------------|
| 🔴 `#fdd`   | Mandatory (M)  |
| 🟡 `#ffd700`| Conditional (C)|
| 🟢 `#c0f5c0`| Optional (O)   |