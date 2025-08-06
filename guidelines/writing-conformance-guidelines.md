# Guidelines for writing conformance rules

As the FOCUS working group moves to introduce a formal conformance rule definition structure the requirement for FOCUS members to understand how to read and write conformance rules will increase. This guide is here to assist those who are starting their journey in writing rules for FOCUS.

The `specification/conformance` folder contains modular CR components and a Python-based build process that assembles them into a validated `cr-<version>.json` file using a corresponding JSON Schema (`cr_schema.json`).

## Conformance document overview

The conformance document for FOCUS contains the following major sections:

| Section | Purpose |
|---------|---------|
| Details | Key details about the conformance document |
| ApplicabilityCriteria | Key flags used to define attributes about the data generator that need to be true for some conformance rules to apply |
| CheckFunctions | Method definitions to describe the actual check needed to conform to a rule |
| ConformanceDatasets | List of datasets defined by FOCUS and the related top level conformance rules associated with the dataset |
| ConformanceRules | Individual conformance rule definitions that are linked together by requirements and dependancies to form the full conformance ruleset |

## Steps to apply conformance rules to existing attributes and columns

An Action Item (AI) ticket should be opened to track the progress of implementing the conformance rules for an existing check.

### Stage 1

The first stage of conversion of rules from the normative text to conformance rules is for a table to be generated with the format as follows:

| ConformanceRuleId | Function | Description | Reference | ApplicabilityCriteria | Condition | Requirement | Keyword | MustSatisfy | Type | Notes | CRVersionIntroduced | Status |
|-------------------|----------|-------------|-----------|-----------------------|-----------|-------------|---------|-------------|------|-------|-----|----|
| | | | | | | | | | | | | |

- `ConformanceRuleId` - Is the formal Id given to this entry in the conformance rules (See: [CR Expression Format](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/1121-ai-align-on-approach-for-scrs/specification/conformance/README.md#-cr-expression-format))
- `Function` - The type of rule to be defined (Valid types: `Composite`, `Presence`, `Type`, `Format`, `Validation`)
- `Description` - Free form description mostly used to help with tracking the work in stage 1
- `Reference` - The Column/Attribute Id this rule applies to
- `ApplicabilityCriteria` - Specific criteria that must be true of the data generator for this rule to apply to the dataset
- `Condition` - The definition of conditions under which this rule applies
- `Requirement` - The definition of what is required for conformance
- `Keyword` - The Normative keyword that applies to this rule (Allowed Values: `MUST`, `RECOMMENDED`, `SHOULD`, `MAY`, `OPTIONAL`)
- `MustSatisfy` - The normative text that this rule defines
- `Type` - Identifier if this is a Static or Dynamic rule, with Static rules being possible to assess conformance without external information being required
- `Notes` - Free form notes (short) included in the conformance rule document
- `CRVersionIntroduced` - CR Version this rule was added to the Conformance Rules (See: [CR Versioning](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/1121-ai-align-on-approach-for-scrs/specification/conformance/README.md#versioning))
- `Status` - Status of the rule (Valid values: Active, Depreciated)

### Stage 2

The second phase of conversion is to take the table created in Stage 1 and create the entries in the `specification/conformance` folder that adds the rules to the formal JSON structure.

#### Folder structure

- `cr_details.json`: Metadata like versioning
- `applicability_criteria.json`: Feature flags controlling rule application
- `check_functions.json`: Logical validation functions and their arguments
- `conformance_datasets.json`: Maps datasets (e.g. FOCUS) to rule sets
- `conformance_rules/attributes/`: JSON files defining multiple `ConformanceRules` for a single attribute
- `conformance_rules/colunns/`: JSON files defining multiple `ConformanceRules` for a single column

#### Steps

- Assign the Action Item (AI) to yourself to signal that you are working on the item (See: [GitHub Issues](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues))
- Open a branch with the source of git branch `1121-ai-align-on-approach-for-scrs` for your development work with the naming format as follows `ai number`-cr-`entity-name`-1121. (example: 1255-cr-AvailabilityZone-1121)
- Pull your branch to your development environment and perform all work specific to this AI in this branch.
- Add a file into the relevant folder `conformance_rules/attributes/` or `conformance_rules/colunns/` with name `entity-name`.json (example: availabilityzone.json)
- Write your rules into this file based on the rules in the Stage 1 table from the AI ticket (See: [ConformanceRule Templates](#conformancerule-templates) for helpers)
- If you need to add new ApplicabilityCriteria add them to `applicability_criteria.json` avoiding duplication
- If you need to add new CheckFunctions add them to `check_functions.json` avoiding duplication
- Add your top level conformance rule entry into the relevant Dataset entries in the `conformance_datasets.json` file

If you need assistance reach out to Mike Fuller in the FOCUS slack

## ConformanceRule Templates

### Base column composite rule

Base rule for a column which links all related Conformance Rules for the column.

```json
  "SampleColumn-C-000-M": {
    "Function": "Composite",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "Notes": "",
    "CRVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "Type": "Static",
    "ValidationCriteria": {
      "MustSatisfy": "",
      "Keyword": "MUST",
      "Requirement": {
        "CheckFunction": "AND",
        "Items": [
          {
            "CheckFunction": "CheckConformanceRule",
            "ConformanceRuleId": "SampleColumn-C-001-M"
          },
          {
            "CheckFunction": "CheckConformanceRule",
            "ConformanceRuleId": "SampleColumn-C-002-M"
          },
          {
            "CheckFunction": "CheckConformanceRule",
            "ConformanceRuleId": "SampleColumn-C-003-M"
          }
        ]
      },
      "Condition": {},
      "Dependencies": []
    }
  }
```

### Presence requirement rule

```json
  "SampleColumn-C-001-M": {
    "Function": "Presence",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "Notes": "",
    "CRVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "Type": "Static",
    "ValidationCriteria": {
      "MustSatisfy": "MUST be present in a FOCUS dataset",
      "Keyword": "MUST",
      "Requirement": {
        "CheckFunction": "ColumnPresent",
        "ColumnName": "SampleColumn"
      },
      "Condition": {},
      "Dependencies": []
    }
  }
```

### NOT NULL requirement rule

Common rule for columns with a NOT NULL requirement. Can also be used when there is a NOT NULL condition.

```json
  "SampleColumn-C-002-M": {
    "Function": "Validation",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "Notes": "",
    "CRVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "Type": "Static",
    "ValidationCriteria": {
      "MustSatisfy": "MUST NOT be null",
      "Keyword": "MUST",
      "Requirement": {
        "CheckFunction": "CheckNotValue",
        "ColumnName": "SampleColumn",
        "Value": null
      },
      "Condition": {},
      "Dependencies": []
    }
  }
```

### Type Decimal requirement rule

```json
  "SampleColumn-C-003-M": {
    "Function": "Type",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "Notes": "",
    "CRVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "Type": "Static",
    "ValidationCriteria": {
      "MustSatisfy": "MUST be of type Decimal",
      "Keyword": "MUST",
      "Requirement": {
        "CheckFunction": "TypeDecimal",
        "ColumnName": "SampleColumn"
      },
      "Condition": {},
      "Dependencies": []
    }
  }
```

### Format Numeric requirement rule

```json
  "SampleColumn-C-004-M": {
    "Function": "Format",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "Notes": "",
    "CRVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "Type": "Static",
    "ValidationCriteria": {
      "MustSatisfy": "MUST conform to NumericFormat requirements",
      "Keyword": "MUST",
      "Requirement": {
        "CheckFunction": "FormatNumeric",
        "ColumnName": "SampleColumn"
      },
      "Condition": {},
      "Dependencies": []
    }
  }
```

### Type String requirement rule

```json
  "SampleColumn-C-003-M": {
    "Function": "Type",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "Notes": "",
    "CRVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "Type": "Static",
    "ValidationCriteria": {
      "MustSatisfy": "MUST be of type String",
      "Keyword": "MUST",
      "Requirement": {
        "CheckFunction": "TypeString",
        "ColumnName": "SampleColumn"
      },
      "Condition": {},
      "Dependencies": []
    }
  }
```

### Format String Handling rule

```json
  "SampleColumn-C-003-M": {
    "Function": "Type",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "Notes": "",
    "CRVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "Type": "Static",
    "ValidationCriteria": {
      "MustSatisfy": "MUST conform to StringHandling requirements",
      "Keyword": "MUST",
      "Requirement": {
        "CheckFunction": "FormatString",
        "ColumnName": "SampleColumn"
      },
      "Condition": {},
      "Dependencies": []
    }
  }
```
