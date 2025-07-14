### Static Conformance Requirements – Availability Zone

| SCRItem                     | Function                  | Reference          | PreCondition                | Condition                                                   | Requirement               | Validation Criteria                                                                                               | Notes                                                                                         | VersionIntroduced | Status  |
|----------------------------|---------------------------|--------------------|-----------------------------|-------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-------------------|---------|
| AVAILABILITYZONE-C-000-C   | Summary of all rules      | Availability Zone  | SUPPORTS_AVAILABILITY_ZONE | null                                                        | AND of C-001 to C-004     | MUST satisfy all applicable conformance rules from C-001 to C-004                                                | Precondition: Rule applies only when SUPPORTS_AVAILABILITY_ZONE is true                      | 0.5               | active  |
| AVAILABILITYZONE-C-001-C   | Define presence           | Availability Zone  | SUPPORTS_AVAILABILITY_ZONE | null                                                        | null                      | AvailabilityZone is RECOMMENDED to be present when the provider supports deploying in an availability zone       | Precondition: SUPPORTS_AVAILABILITY_ZONE                                                     | 0.5               | active  |
| AVAILABILITYZONE-C-002-M   | Specify data type         | Availability Zone  | null                        | null                                                        | null                      | AvailabilityZone MUST be of type String                                                                           |                                                                                               | 0.5               | active  |
| AVAILABILITYZONE-C-003-M   | Ensure string formatting  | Availability Zone  | null                        | null                                                        | null                      | AvailabilityZone MUST conform to StringHandling requirements                                                      |                                                                                               | 0.5               | active  |
| AVAILABILITYZONE-C-004-C   | Null when not applicable  | Availability Zone  | null                        | Charge is not specific to an availability zone              | null                      | AvailabilityZone MUST be null when a charge is not specific to an availability zone                              |                                                                                               | 0.5               | active  |

### DAG of Static Conformance Requirements for `Availability Zone`

This diagram shows the logical structure and composite dependencies for the SCRs of the `Availability Zone` column in FOCUS v1.2.

```mermaid
graph TD

%% Root Composite
AZ000["C-000-C: Summary of all rules"]
AZ001["C-001-C: Define presence"]
AZ002["C-002-M: Type is String"]
AZ003["C-003-M: String format"]
AZ004["C-004-C: Null when not applicable"]

%% Root connections
AZ000 --> AZ001
AZ000 --> AZ002
AZ000 --> AZ003
AZ000 --> AZ004

%% Styling by Rule Type
classDef mandatory fill:#fdd,stroke:#c00,stroke-width:2px;
classDef conditional fill:#ffd700,stroke:#aa0,stroke-width:1px;
classDef optional fill:#c0f5c0,stroke:#2c8c2c,stroke-width:1px;

class AZ000,AZ001,AZ004 conditional;
class AZ002,AZ003 mandatory;
```

| Color      | Rule Type     |
|------------|----------------|
| 🔴 `#fdd`   | Mandatory (M)  |
| 🟡 `#ffd700`| Conditional (C)|
| 🟢 `#c0f5c0`| Optional (O)   |

## SCR - Availability Zone
This is the final output from stage 2. At this point it is left to identify any dependency between this column and other FOCUS v1.2 columns.

### SCR - Availability Zone - JSON Format

```JSON
{
    "SCRDetails": {
      "Version": "0.5"
    },
    "PreConditions": {
      "SUPPORTS_AVAILABILITY_ZONE": {
        "Description": "Rule applies only when SUPPORTS_AVAILABILITY_ZONE is true"
      }
    },
    "Attributes": {},
    "AttributeChecks": {
      "AVAILABILITYZONE-C-000-C": {
        "Function": "Composite",
        "Reference": "Availability Zone",
        "Notes": "Precondition: Rule applies only when SUPPORTS_AVAILABILITY_ZONE is true",
        "VersionIntroduced": "0.5",
        "Status": "active",
        "ValidationCriteria": {
          "mustSatisfy": "MUST satisfy all applicable conformance rules from C-001 to C-004"
        }
      },
      "AVAILABILITYZONE-C-001-C": {
        "Function": "Presence",
        "Reference": "Availability Zone",
        "Notes": "Precondition: SUPPORTS_AVAILABILITY_ZONE",
        "VersionIntroduced": "0.5",
        "Status": "active",
        "ValidationCriteria": {
          "mustSatisfy": "AvailabilityZone is RECOMMENDED to be present when the provider supports deploying in an availability zone"
        }
      },
      "AVAILABILITYZONE-C-002-M": {
        "Function": "Type",
        "Reference": "Availability Zone",
        "VersionIntroduced": "0.5",
        "Status": "active",
        "ValidationCriteria": {
          "mustSatisfy": "AvailabilityZone MUST be of type String"
        }
      },
      "AVAILABILITYZONE-C-003-M": {
        "Function": "Format",
        "Reference": "Availability Zone",
        "VersionIntroduced": "0.5",
        "Status": "active",
        "ValidationCriteria": {
          "mustSatisfy": "AvailabilityZone MUST conform to StringHandling requirements"
        }
      },
      "AVAILABILITYZONE-C-004-C": {
        "Function": "Conditional",
        "Reference": "Availability Zone",
        "VersionIntroduced": "0.5",
        "Status": "active",
        "ValidationCriteria": {
          "mustSatisfy": "AvailabilityZone MUST be null when a charge is not specific to an availability zone"
        }
      }
    },
    "CheckFunction": {},
    "ConformanceTables": {
      "AVAILABILITYZONE": {
        "ConformanceRuleSets": [
          "AVAILABILITYZONE-C-000-C"
        ]
      }
    },
    "ConformanceRuleSets": {
      "AVAILABILITYZONE-C-000-C": {
        "Type": "Composite",
        "Rules": {
          "Operator": "AND",
          "Items": [
            "AVAILABILITYZONE-C-001-C",
            "AVAILABILITYZONE-C-002-M",
            "AVAILABILITYZONE-C-003-M",
            "AVAILABILITYZONE-C-004-C"
          ]
        }
      }
    },
    "ConformanceRules": [
      {
        "SCRItem": "AVAILABILITYZONE-C-001-C",
        "Function": "Presence",
        "Reference": "Availability Zone",
        "VersionIntroduced": "0.5",
        "Status": "active",
        "PreConditions": [
          "SUPPORTS_AVAILABILITY_ZONE"
        ],
        "ValidationCriteria": {
          "mustSatisfy": "AvailabilityZone is RECOMMENDED to be present when the provider supports deploying in an availability zone"
        },
        "DisplayOrder": 0,
        "SourceText": "AvailabilityZone is RECOMMENDED to be present when the provider supports deploying in an availability zone",
        "ColumnID": "AVAILABILITYZONE"
      },
      {
        "SCRItem": "AVAILABILITYZONE-C-002-M",
        "Function": "Type",
        "Reference": "Availability Zone",
        "VersionIntroduced": "0.5",
        "Status": "active",
        "PreConditions": [],
        "ValidationCriteria": {
          "mustSatisfy": "AvailabilityZone MUST be of type String"
        },
        "DisplayOrder": 1,
        "SourceText": "AvailabilityZone MUST be of type String",
        "ColumnID": "AVAILABILITYZONE"
      },
      {
        "SCRItem": "AVAILABILITYZONE-C-003-M",
        "Function": "Format",
        "Reference": "Availability Zone",
        "VersionIntroduced": "0.5",
        "Status": "active",
        "PreConditions": [],
        "ValidationCriteria": {
          "mustSatisfy": "AvailabilityZone MUST conform to StringHandling requirements"
        },
        "DisplayOrder": 2,
        "SourceText": "AvailabilityZone MUST conform to StringHandling requirements",
        "ColumnID": "AVAILABILITYZONE"
      },
      {
        "SCRItem": "AVAILABILITYZONE-C-004-C",
        "Function": "Conditional",
        "Reference": "Availability Zone",
        "VersionIntroduced": "0.5",
        "Status": "active",
        "PreConditions": [],
        "ValidationCriteria": {
          "mustSatisfy": "AvailabilityZone MUST be null when a charge is not specific to an availability zone"
        },
        "DisplayOrder": 3,
        "SourceText": "AvailabilityZone MUST be null when a charge is not specific to an availability zone",
        "ColumnID": "AVAILABILITYZONE"
      },
      {
        "SCRItem": "AVAILABILITYZONE-C-000-C",
        "Function": "Composite",
        "Reference": "Availability Zone",
        "VersionIntroduced": "0.5",
        "Status": "active",
        "PreConditions": [
          "SUPPORTS_AVAILABILITY_ZONE"
        ],
        "ValidationCriteria": {
          "mustSatisfy": "MUST satisfy all applicable conformance rules from C-001 to C-004"
        },
        "DisplayOrder": 4,
        "SourceText": "MUST satisfy all applicable conformance rules from C-001 to C-004",
        "ColumnID": "AVAILABILITYZONE"
      }
    ],
    "Requirement": {
      "Operator": "AND",
      "Items": [
        "AVAILABILITYZONE-C-001-C",
        "AVAILABILITYZONE-C-002-M",
        "AVAILABILITYZONE-C-003-M",
        "AVAILABILITYZONE-C-004-C"
      ]
    }
  }
```

```mermaid
graph TD

%% Class Definitions
classDef precondition fill:#ffeeba,stroke:#c69500,stroke-width:2px,color:#000;
classDef mandatory fill:#fdd,stroke:#a00,stroke-width:2px,color:#000;
classDef conditional fill:#ffd700,stroke:#b8860b,stroke-width:2px,color:#000;

%% Precondition
SUPPORTS_AVAILABILITY_ZONE[/"Precondition:\nSUPPORTS_AVAILABILITY_ZONE"/]:::precondition --> AVAILABILITYZONE-C-001-C

%% Atomic Rules
AVAILABILITYZONE-C-001-C["C-001: Presence\nRECOMMENDED if provider supports availability zone"]:::conditional --> AVAILABILITYZONE-C-000-C
AVAILABILITYZONE-C-002-M["C-002: Type\nMUST be String"]:::mandatory --> AVAILABILITYZONE-C-000-C
AVAILABILITYZONE-C-003-M["C-003: Format\nMUST conform to StringHandling"]:::mandatory --> AVAILABILITYZONE-C-000-C
AVAILABILITYZONE-C-004-C["C-004: Conditional\nMUST be null when charge is not AZ-specific"]:::conditional --> AVAILABILITYZONE-C-000-C

%% Composite Rule
AVAILABILITYZONE-C-000-C["C-000: Composite\nMUST satisfy C-001 to C-004\n(AND)"]:::conditional
```