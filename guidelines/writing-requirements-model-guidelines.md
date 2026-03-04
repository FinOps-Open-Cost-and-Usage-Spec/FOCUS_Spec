# Guidelines for writing model rules

The FOCUS Requirements Model is a machine-readable representation of the normative requirements defined in the FOCUS specification. Each model rule is the programmatic equivalent of a normative statement in the specification text—transforming human-readable requirements (written using keywords like MUST, SHOULD, and MAY) into structured JSON that can be programmatically validated, tested, and enforced. This one-to-one mapping between specification requirements and model rules enables automated conformance testing, tooling integration, and consistent interpretation of FOCUS requirements across different implementations. By capturing rules in a standardized format with explicit dependencies, conditions, and validation logic, the Requirements Model ensures that FOCUS datasets can be reliably validated against specification requirements.

With the formal rule definition structure now in place, FOCUS members need to understand how to read and write model rules effectively. This guide assists those working with the Requirements Model, whether creating new rules, maintaining existing ones, or validating datasets against FOCUS requirements.

The `specification/requirements_model` folder contains modular model components organized by version under `releases/X.X/` directories. A Python-based build process assembles these components into a validated `model-<version>.json` file using a corresponding JSON Schema (`model_schema.json`). The `releases/latest/` symlink always points to the most recent model version.

## Model document overview

The model document for FOCUS contains the following major sections:

| Section | Purpose |
|---------|---------|
| Details | Key details about the model document |
| ApplicabilityCriteria | Key flags used to define attributes about the data generator that need to be true for some model rules to apply |
| CheckFunctions | Method definitions to describe the actual check needed to conform to a rule |
| ModelDatasets | List of datasets defined by FOCUS and the related top level model rules associated with the dataset |
| ModelRules | Individual model rule definitions that are linked together by requirements and dependencies to form the full model ruleset |

## Steps to create model rules for FOCUS entities

An Action Item (AI) ticket should be opened to track the progress of implementing the model rules for an existing check.

### Stage 1

The first stage of conversion of rules from the normative text to model rules is for a table to be generated with the format as follows:

- `ModelRuleId` - Formal identifier for this model rule entry
- `Function` - The type of rule to be defined (Valid types: `Composite`, `Presence`, `Type`, `Format`, `Validation`)
- `Reference` - The Column/Attribute Id this rule applies to
- `EntityType` - The type of entity this rule applies to (Valid types: `Dataset`, `Column`, `Attribute`, `Object`)
- `EntityName` - The human-readable name of the entity this rule applies to
- `EntityId` - The unique identifier of the entity this rule applies to
- `Notes` - Free form notes (short) included in the model rule document
- `ModelVersionIntroduced` - Requirements Model Version this rule was added to the Model Rules
- `Status` - Status of the rule (Valid values: Active, Deprecated, Removed)
- `ModelVersionRemoved` - Requirements Model Version this rule was removed from the Model Rules
- `ApplicabilityCriteria` - Specific criteria that must be true of the data generator for this rule to apply to the dataset
- `Type` - Identifier if this is a Static or Dynamic rule, with Static rules being possible to assess model without external information being required
- `Order` - The order in which this rule should be processed or displayed
- `DatasetType` - The dataset type this rule applies to (e.g. "CAU" for Cost and Usage, "CCT" for Contract Commitment)
- `DatasetId` - The identifier of the dataset this rule belongs to (Required for Dataset, Column, and Object entity types, e.g. "CostAndUsage" for Cost and Usage, "ContractCommitment" for Contract Commitment)
- `DatasetName` - The human-readable name of the dataset this rule belongs to (Required for Column and Dataset entity types, e.g. "Cost and Usage" for Cost and Usage)
- `ValidationCriteria` - The detailed criteria that defines how this rule is to be validated
  - `MustSatisfy` - The normative text that this rule defines
  - `Keyword` - The Normative keyword that applies to this rule (Allowed Values: `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`)
  - `Requirement` - The definition of what is required for model
  - `Condition` - The definition of conditions under which this rule applies


#### Stage 1: Rule-Based Extraction of Normative Requirements

Stage 1 converts normative requirements from the FOCUS specification into structured, machine-readable JSON using the property definitions below. Apply the extraction rules deterministically to ensure each normative statement is consistently identified, classified, and represented without inference or reinterpretation. The resulting JSON must strictly conform to the defined structure, enabling consistency across releases and supporting automation, validation, and analysis workflows.

#### High-Level Description of the Model Rule Properties

#### 1. Target Entity – Determine the entity

Identify the target for the rule: **Dataset**, **Column**, **Attribute** property, **Metadata**, **Object**etc. This sets the scope of the model requirement.

#### FOCUS Core Entities

The following architectural components define the core entities in FOCUS that shape the structure and flow of billing data.

<img width="491" height="491" alt="Image" src="https://github.com/user-attachments/assets/a30d828e-d2af-4185-984c-475998466437"/>

- **Dataset, Column, Attribute, Metadata** are the **core structural entities** where model requirements are directly assigned.


##### FOCUS Entity Reference Table

| Entity             | Description                                         | Applies To                                | Example RM Function                                                                                             |
|--------------------|-----------------------------------------------------| ----------------------------------------- |-----------------------------------------------------------------------------------------------------------------|
| `Dataset`          | Whole billing dataset                               | Structural presence, versioning, coverage | Dataset MUST include all columns required by the declared FOCUS version                                         |
| `Row`              | Individual line item in dataset                     | Logic conditions, nullability, alignment  | Rows with `ChargeCategory = Purchase` MUST contain a `SkuId`                                                    |
| `Column`           | Named field across rows                             | Data type, format, constraints            | Column `BilledCost` MUST be of type `Decimal`                                                          |
| `Object`           | JSONObject content of a column                      | Data type, format, constraints            | Object property `name` MUST be of type `String`                                                          |
| `Attribute`        | Shared formatting/logic constraint                  | Formatting consistency across columns     | All `String` columns MUST conform to `StringHandling` requirements                                              |

#### 2. RMID – Apply RMID Naming Rules

Construct a unique identifier for the rule using the format:  
`DatasetType-ColumnID-EntityType-NNN-Level`

This ensures traceability, uniqueness, and clarity.

- Use the format: `DatasetType-ColumnID-EntityType-NNN-Level`
- `DatasetType`: Short identifier for the dataset (e.g., `CAU`, `CCT`)
- `ColumnID`: UpperCamelCase (e.g., `ListUnitPrice`)
- `EntityType:`
  - `D` = Dataset  
  - `C` = Column
  - `O` = Object
  - `A` = Attribute
- `NNN:` (unique only within the dataset namespace)
  - `000` for root composite  
  - `0NN` for intermediate composites  
  - `001+` for single atomic rules
- `Level:`  
  - `M` = Mandatory (from MUST)  
  - `C` = Conditional (e.g., SHOULD under a condition)  
  - `O` = Optional (from MAY or unconditional SHOULD)

**Example**  
A rule states: "`ListUnitPrice` MUST conform to `NumericFormat`." (in Cost and Usage dataset)
→ `RMID = CAU-ListUnitPrice-C-003-M`

#### Multi-Dataset Entity Structure and Naming

The FOCUS specification supports multiple datasets, each with their own requirements. The following decisions have been made regarding entity structure and naming:

##### Dataset-Specific Requirement Entities

Each dataset will reference their own set of Requirement Entities. A single requirement item should not be referenced by multiple datasets - they should have their own entry. This ensures:

- Clear separation of concerns between datasets
- Independent evolution of dataset requirements
- Simplified validation and testing per dataset
- Reduced complexity in rule dependencies

##### Dataset-Namespaced Naming Convention

Column entities are now namespaced by the dataset they belong to. The RMID format has been updated to:

`DatasetType-ColumnID-EntityType-NNN-Level`

Where:

- `DatasetType`: Short identifier for the dataset (e.g., `CAU` for Cost and Usage)
- `ColumnID`: The column identifier in UpperCamelCase
- `EntityType`, `NNN`, `Level`: Same as previously defined

The `NNN` numbering is only unique within each dataset namespace. For example, `CAU-ListUnitPrice-C-000-M` and `CCT-ListUnitPrice-C-000-M` can both exist independently - the `000` is reused and only needs to be unique within that specific dataset abbreviation.

##### Examples

- Cost and Usage dataset: `CAU-BillingAccountName-C-000-M`
- Contract Commitment dataset: `CCT-CommitmentDiscountId-C-001-M`

##### Dataset Abbreviations

| Dataset | Abbreviation | Description |
|---------|--------------|-------------|
| Cost and Usage | CAU | Primary billing data with usage and cost information |
| Contract Commitment | CCT | Commitment discount and reservation data |

This namespacing approach prevents naming conflicts between datasets and provides clear traceability of which dataset a requirement belongs to.

#### 3. Function – Classify the rule type

Categorize the type of logic the rule enforces. This helps determine how it should be validated.

- Use `Presence` for rules requiring the column’s inclusion in the dataset.
- Use `Type` to enforce primitive types like `Decimal`, `String`, `Boolean`.
- Use `Format` for pattern-based constraints (e.g., `DateTimeFormat`, `UUID`, `NumericFormat`).
- Use `Nullability` to define conditional nullability rules (e.g., "MUST NOT be null when condition X" or "MAY be null when condition Y").
- Use `Validation` for business logic or fixed-value conditions not covered above, including unconditional NOT NULL rules.
- Use `Composite` to group multiple RMIDs with logical expressions (`AND` / `OR` / `NOT`).
- Use `Ambiguous` only when no clear classification is possible.

**Examples**  
Rule states "`BillingPeriodStart` MUST be of type `DateTime`":  
→ `Function = Type`

Rule states "`CommitmentDiscountQuantity` MUST NOT be null when `ChargeCategory` is `Purchase`":  
→ `Function = Nullability`

#### 4. Reference – Identify the reference target

Provide the identifier for the column or attribute that the rule applies to, using the PascalCase ID format.

- For columns: Use the ColumnId (e.g., `CommitmentDiscountQuantity`)
- For attributes: Use the attribute name (e.g., `NumericFormat`, `StringHandling`)
- This field should match the ID as defined in the FOCUS specification

**Example**  
If the rule applies to the column with ID `CommitmentDiscountQuantity`:  
→ `Reference = CommitmentDiscountQuantity`

#### 5. Keyword – Extract the normative keyword

Determine the obligation level using the normative keyword from the source text, such as `MUST`, `SHOULD`, or `MAY`.

- Identify the first normative keyword present in the requirement:
  - `MUST`, `MUST NOT` → Mandatory
  - `SHOULD`, `SHOULD NOT` → Optional (unless conditional)
  - `MAY`, `MAY NOT` → Optional
- Normalize the keyword to uppercase.
- Only one keyword should be assigned per RM Item.
- For composite rules, choose the highest obligation level from constituent RMIDs  
  (e.g., prioritize `MUST` > `SHOULD` > `MAY`).
- If `SHOULD` is used conditionally, treat the rule as `Conditional` and define the `Condition`.

**Example**  
A rule states: “Rows SHOULD include `SkuId` when `ChargeCategory = Purchase`.”  
→ `Keyword = SHOULD`

#### 6. Applicability Criteria – Determine if the rule should be evaluated

Specify provider capability flags that determine when the rule applies. Use keys defined in the ApplicabilityCriteria section of the model.

- Use an empty list `[]` when no applicability gating is required
- Use array of criteria keys when rule depends on provider capabilities  
  (e.g., `["COMMITMENT_DISCOUNT_SUPPORTED"]`, `["CAPACITY_RESERVATION_SUPPORTED"]`)
- Common criteria: `REGION_SUPPORTED`, `TAGGING_SUPPORTED`, `SUB_ACCOUNT_SUPPORTED`

**Example**  
A rule requires capacity reservation support:  
→ `ApplicabilityCriteria = ["CAPACITY_RESERVATION_SUPPORTED"]`

#### 7. Condition – Specify when to test

Define the row-level logic that determines whether the rule applies to a given record using CheckFunction objects.

- Use empty object `{}` when the rule applies to all rows unconditionally
- Use CheckFunction structure when rule applies conditionally (same structure as Requirement field)

**Examples:**

Unconditional rule (applies to all rows):
```json
"Condition": {}
```

Conditional rule when ChargeCategory equals "Purchase":
```json
"Condition": {
  "CheckFunction": "CheckValue",
  "ColumnName": "ChargeCategory",
  "Value": "Purchase"
}
```

Conditional rule when ContractCommitmentCategory equals "Usage":
```json
"Condition": {
  "CheckFunction": "CheckValue",
  "ColumnName": "ContractCommitmentCategory",
  "Value": "Usage"
}
```

#### 8. MustSatisfy – Define how to test the rule

Copy the actual normative text from the column specification that this rule enforces, including the full sentence with the column name.

- Use the exact text from the specification document
- Include the column/entity name in the statement
- Preserve the normative keyword (`MUST`, `SHOULD`, `MAY`) as written in the specification

**Examples:**

From the specification text "`ContractCommitmentQuantity` MUST be of type Decimal.":  
→ `MustSatisfy = "ContractCommitmentQuantity MUST be of type Decimal."`

From the specification text "`ContractCommitmentQuantity` MUST conform to NumericFormat requirements.":  
→ `MustSatisfy = "ContractCommitmentQuantity MUST conform to NumericFormat requirements."`

#### 9. Requirement – Identify the check function and arguments

Define the specific validation check that implements this rule using CheckFunction objects.

For **Composite rules**, use logical CheckFunctions to group other rules:
- `CheckFunction: "AND"` with `Items` array containing nested requirement references
- `CheckFunction: "OR"` with `Items` array containing nested requirement references

For **Atomic rules**, use specific CheckFunction types from the model:
- `ColumnPresent` - Check if a column exists in the dataset
- `CheckNotValue` - Verify a column does not contain a specific value
- `CheckValue` - Verify a column contains a specific value
- `TypeDecimal`, `TypeString`, `TypeBoolean` - Check data type
- `FormatNumeric`, `FormatString`, `FormatDateTime` - Check format compliance
- See CheckFunctions section in the model for complete list

**Examples:**

Composite rule grouping three child rules:
```json
"Requirement": {
  "CheckFunction": "AND",
  "Items": [
    {
      "CheckFunction": "CheckModelRule",
      "ModelRuleId": "CAU-CommitmentDiscountQuantity-C-010-M"
    },
    {
      "CheckFunction": "CheckModelRule",
      "ModelRuleId": "CAU-CommitmentDiscountQuantity-C-011-C"
    },
    {
      "CheckFunction": "CheckModelRule",
      "ModelRuleId": "CAU-CommitmentDiscountQuantity-C-012-C"
    }
  ]
}
```

Atomic rule checking column presence:
```json
"Requirement": {
  "CheckFunction": "ColumnPresent",
  "ColumnName": "BilledCost"
}
```

#### 10. Type – Specify validation dependency classification

Indicates whether the rule can be validated using only the dataset itself or requires external dependencies.

- `Static` - Rule can be validated by examining the dataset alone (data types, nullability, formatting, schema presence)
- `Dynamic` - Rule requires external dependencies (invoice records, catalog metadata, provider configuration)

For composite rules, use `Dynamic` if any child rule is dynamic.

**Example**  
Rule checks data type: `Type = Static`  
Rule validates against provider catalog: `Type = Dynamic`

#### 11. ModelVersionIntroduced – Version tracking

Record the version of the FOCUS specification in which this rule was introduced.

- For all rules generated from FOCUS v1.2, set this field to `"1.2"`.
- Do not infer or omit — this value is fixed for each release of the specification.
- This field enables forward/backward compatibility during conformance testing.

**Example**  
→ `ModelVersionIntroduced = 1.2`

#### 12. Status – Set rule lifecycle status

Indicate whether the rule is `Active`, `Deprecated`, or `Removed`.

- Default to `Active` unless the normative text explicitly states otherwise.
- Use `Deprecated` if the rule is marked for removal or obsolescence.
- Use `Removed` if the rule is removed from the model.

**Example**  
A rule marked in the spec as legacy:  
“This requirement will be removed in future versions.”  
→ `Status = Deprecated`

#### 13. Notes – Capture comments

Use this field to add clarifying comments, editorial notes.

- Add contextual information for better understanding of the rule.
- Leave blank only when no additional clarification is needed.

#### 14. DatasetId and DatasetName – Dataset Association

For Column and Dataset entity types, these fields establish the relationship between the rule and its parent dataset.

**Reasoning Rules**

- `DatasetId` must match the identifier of the dataset the entity belongs to
- `DatasetName` must match the human-readable name of the dataset
- Both fields are required for all Column and Dataset entity types
- These fields ensure proper dataset-rule association and enable dataset-specific validation

**Example**  
For a rule applying to a column in the Cost and Usage dataset:  
→ `DatasetId = CostAndUsage`  
→ `DatasetName = Cost and Usage`

#### 15. Dependencies – Track rule relationships

The Dependencies array lists prerequisite rules that must be evaluated before the current rule. This establishes the dependency graph and evaluation order.

**When to use Dependencies:**

- When your rule references a column that must exist (add that column's composite rule)
- When your Condition uses a column (add that column's composite rule)
- When logical evaluation order matters (e.g., type checking before format checking)
- When your rule builds on another rule's validation

**Ordering Requirements:**

- Dependencies must be listed in ascending order by their `Order` field values
- This ensures rules are evaluated in the correct sequence
- Automated tests validate dependency ordering

**Examples:**

Unconditional rule with no dependencies:
→ `Dependencies = []`

Nullability rule that depends on ChargeCategory column:
```json
"Dependencies": [
  "CAU-ChargeCategory-C-000-M"
]
```

Complex rule depending on multiple prerequisites (ordered by Order field):
```json
"Dependencies": [
  "CAU-BilledCost-C-000-M",        // Order: 10
  "CAU-BillingCurrency-C-000-M",   // Order: 20
  "CAU-ChargeCategory-C-000-M"     // Order: 30
]
```

#### 16. ModelVersionRemoved – Track removed rules

Record the model version when a rule is removed from the specification. Only populate this field when `Status = "Removed"`.

**When to use:**

- A rule has been completely removed from the FOCUS specification
- Enables version-specific rule filtering and backward compatibility
- Leave empty for Active and Deprecated rules

**Examples:**

Active rule (most common):
→ `Status = "Active"`, `ModelVersionRemoved` field omitted or empty

Rule removed in version 1.4:
→ `Status = "Removed"`, `ModelVersionRemoved = "1.4"`

**Note:** Deprecated rules should not have ModelVersionRemoved populated until they are actually removed in a future version.

### Stage 2

The second phase of conversion is to take the table created in Stage 1 and create the entries in the `specification/requirements_model` folder that adds the rules to the formal JSON structure.

#### Folder structure

Version-specific model content is organized under `specification/requirements_model/releases/X.X/` where X.X represents the model version (e.g., 1.2, 1.3). A `latest` symlink points to the most recent version.

**Version-specific structure** (`releases/X.X/`):
- `cr_details.json`: Metadata like versioning for this model version
- `applicability_criteria.json`: Feature flags controlling rule application
- `check_functions.json`: Logical validation functions and their arguments
- `model_datasets.json`: Maps datasets (e.g. FOCUS) to rule sets
- `model_rules/attributes/`: JSON files defining multiple `ModelRules` for a single attribute
- `model_rules/columns/`: JSON files defining multiple `ModelRules` for a single column

**Build output** (top-level):
- `build/model-X.X.json`: Built complete model JSON files for all versions

**Convenience paths:**
- `releases/latest/`: Symlink to the latest model version directory
- All work should be done in the appropriate version directory under `releases/X.X/`

#### Steps

- Assign the Action Item (AI) to yourself to signal that you are working on the item (See: [GitHub Issues](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues))
- Open a branch with the source of git feature branch for the development work in progress for your development work.
- Pull your branch to your development environment and perform all work specific to this AI in this branch.
- Navigate to the appropriate model version directory under `specification/requirements_model/releases/X.X/` (or use the `latest` symlink for current development)
- Add a file into the relevant folder `model_rules/attributes/` or `model_rules/datasets/<dataset_id>/columns/` with name `entity-name`.json (example: availabilityzone.json)
- Write your rules into this file based on the rules in the Stage 1 table from the AI ticket (See: [ModelRule Templates](#modelrule-templates) for helpers)
- If you need to add new ApplicabilityCriteria add them to `applicability_criteria.json` in the version directory, avoiding duplication
- If you need to add new CheckFunctions add them to `check_functions.json` in the version directory, avoiding duplication
- Add your top level model rule entry into the relevant Dataset entries in the `model_datasets.json` file
- Validate and test your changes (see Build and Test workflow below)
- Commit your changes to your branch and then move onto raising the PR section

#### Build and Test Workflow

Before committing your changes, validate that your model rules are correctly structured and pass all tests.

**Building the model JSON:**

From the `specification/requirements_model` directory, run the build script:

```bash
cd specification/requirements_model
./build_json.py
```

This script will:
1. Run all pytest tests to validate rule structure and dependencies
2. Assemble all version-specific JSON files from `releases/X.X/` directories
3. Generate complete `build/model-X.X.json` files for each version
4. Validate the generated JSON against `model_schema.json`

**Build-only mode:**

To skip tests and only generate the JSON (useful during development):

```bash
./build_json.py --build-only
```

**Running tests independently:**

To run the test suite without building:

```bash
cd specification/requirements_model
pytest tests/
```

Or run specific test files:

```bash
pytest tests/test_schema.py
pytest tests/test_dependencies.py
```

**Common validation checks:**

The tests verify:
- JSON structure conformance to `model_schema.json`
- RMID format and uniqueness
- Dependency references exist and are valid
- Order field consistency in Dependencies arrays
- CheckFunction argument structure
- ApplicabilityCriteria key validity
- Cross-reference integrity between rules

**Troubleshooting build errors:**

- **JSON syntax errors**: Check for missing commas, brackets, or quotes in your rule files
- **Schema validation failures**: Ensure all required fields are present (Function, Reference, EntityType, etc.)
- **Dependency errors**: Verify all ModelRuleIds in Dependencies arrays exist
- **RMID conflicts**: Ensure your RMID is unique within the dataset namespace

## Pull Request Workflow

- Navigate to Github and raise a pull request (PR) from your branch to the base development feature branch
- Ensure you link the opened PR to your issue ticket by using the development cog on the right side of the PR page
- Announce your PR in the [#tf-conformance-requirements](https://f2-focus.slack.com/archives/C096UTPE3NF) slack channel for other members to see
- Once reviewed and the members have had time (5 days) to add any feedback, TF-RM leader will merge the PR into the base feature development branch which will get full review when that branch is reviewed to merge into the `working_draft` branch via the PR for the RM feature development.

## Order Field Usage

The `Order` field is used to specify the sequence in which rules should be processed or displayed. This field provides explicit control over rule ordering within the requirements model.

### Purpose and Usage

The `Order` field serves several important functions:

1. **Rule Presentation Order**: Controls the sequence in which rules appear in generated documentation and summaries
2. **Logical Processing Sequence**: Ensures rules are evaluated in the correct order when dependencies exist
3. **Dependency Ordering**: Dependencies arrays must be ordered according to the `Order` field values of the referenced rules

### Order Field Guidelines

**Assignment Rules:**

- Use incremental values (e.g., 10, 20, 30) to allow for future insertions
- Lower values indicate higher priority/earlier processing
- Rules without an `Order` field are ignored for ordering purposes
- The `Order` field is required for rules to show explicit sequencing

**Dependency Array Ordering:**

- All dependencies in the `Dependencies` array must be listed in ascending order by their `Order` field values
- This ensures consistent processing and validation of rule dependencies

**Example Order Values:**

```json
{
  "CAU-SampleColumn-C-001-M": {
    "Order": 10,
    "ValidationCriteria": {
      "Dependencies": [
        "CAU-OtherRule-C-001-M",    // Order: 20
        "CAU-AnotherRule-C-002-M"   // Order: 30
      ]
    }
  }
}
```

**Best Practices:**

- Use multiples of 10 (10, 20, 30...) to allow for future rule insertion
- Maintain consistent ordering within related rule groups
- Document the rationale for specific ordering decisions in rule notes
- Validate dependency ordering using automated tests

## ModelRule Templates

### Base column composite rule

Base rule for a column which links all related Model Rules for the column.

```json
  "CAU-SampleColumn-C-000-M": {
    "Function": "Composite",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "EntityId": "SampleColumn",
    "EntityName": "Sample Column",
    "Notes": "",
    "ModelVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "DatasetType": "CAU",
    "DatasetId": "CostAndUsage",
    "DatasetName": "Cost and Usage",
    "Type": "Static",
    "Order": 0,
    "ValidationCriteria": {
      "MustSatisfy": "",
      "Keyword": "MUST",
      "Requirement": {
        "CheckFunction": "AND",
        "Items": [
          {
            "CheckFunction": "CheckModelRule",
            "ModelRuleId": "CAU-SampleColumn-C-001-M"
          },
          {
            "CheckFunction": "CheckModelRule",
            "ModelRuleId": "CAU-SampleColumn-C-002-M"
          },
          {
            "CheckFunction": "CheckModelRule",
            "ModelRuleId": "CAU-SampleColumn-C-003-M"
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
  "CAU-SampleColumn-C-001-M": {
    "Function": "Presence",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "EntityId": "SampleColumn",
    "EntityName": "Sample Column",
    "Notes": "",
    "ModelVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "DatasetType": "CAU",
    "DatasetId": "CostAndUsage",
    "DatasetName": "Cost and Usage",
    "Type": "Static",
    "Order": 10,
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
  "CAU-SampleColumn-C-002-M": {
    "Function": "Validation",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "EntityId": "SampleColumn",
    "EntityName": "Sample Column",
    "Notes": "",
    "ModelVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "DatasetType": "CAU",
    "DatasetId": "CostAndUsage",
    "DatasetName": "Cost and Usage",
    "Type": "Static",
    "Order": 20,
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

### Allowed Value requirement rule

Common rule for columns with a MUST be one of the allowed values requirement.

```json
  "CAU-SampleColumn-C-003-M": {
    "Function": "Validation",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "EntityId": "SampleColumn",
    "EntityName": "Sample Column",
    "Notes": "",
    "ModelVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "DatasetType": "CAU",
    "DatasetId": "CostAndUsage",
    "DatasetName": "Cost and Usage",
    "Type": "Static",
    "Order": 30,
    "ValidationCriteria": {
      "MustSatisfy": "MUST be one of the allowed values",
      "Keyword": "MUST",
      "Requirement": {
        "CheckFunction": "OR",
        "Items": [
          {
            "CheckFunction": "CheckValue",
            "ColumnName": "SampleColumn",
            "Value": "AllowedValue1"
          },
          {
            "CheckFunction": "CheckValue",
            "ColumnName": "SampleColumn",
            "Value": "AllowedValue2"
          },
          {
            "CheckFunction": "CheckValue",
            "ColumnName": "SampleColumn",
            "Value": "AllowedValue3"
          }
        ]
      },
      "Condition": {},
      "Dependencies": []
    }
  }
```

### Type Decimal requirement rule

```json
  "CAU-SampleColumn-C-004-M": {
    "Function": "Type",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "EntityId": "SampleColumn",
    "EntityName": "Sample Column",
    "Notes": "",
    "ModelVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "DatasetType": "CAU",
    "DatasetId": "CostAndUsage",
    "DatasetName": "Cost and Usage",
    "Type": "Static",
    "Order": 40,
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
  "CAU-SampleColumn-C-005-M": {
    "Function": "Format",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "EntityId": "SampleColumn",
    "EntityName": "Sample Column",
    "Notes": "",
    "ModelVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "DatasetType": "CAU",
    "DatasetId": "CostAndUsage",
    "DatasetName": "Cost and Usage",
    "Type": "Static",
    "Order": 50,
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
  "CAU-SampleColumn-C-006-M": {
    "Function": "Type",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "EntityId": "SampleColumn",
    "EntityName": "Sample Column",
    "Notes": "",
    "ModelVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "DatasetType": "CAU",
    "DatasetId": "CostAndUsage",
    "DatasetName": "Cost and Usage",
    "Type": "Static",
    "Order": 60,
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
  "CAU-SampleColumn-C-007-M": {
    "Function": "Format",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "EntityId": "SampleColumn",
    "EntityName": "Sample Column",
    "Notes": "",
    "ModelVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "DatasetType": "CAU",
    "DatasetId": "CostAndUsage",
    "DatasetName": "Cost and Usage",
    "Type": "Static",
    "Order": 70,
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

### Nullability requirement rule (conditional)

Common rule for columns with conditional nullability requirements. Use when a column MUST NOT be null under certain conditions or MAY be null under others.

```json
  "CAU-SampleColumn-C-008-C": {
    "Function": "Nullability",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "EntityId": "SampleColumn",
    "EntityName": "Sample Column",
    "Notes": "",
    "ModelVersionIntroduced": "1.2",
    "Status": "Active",
    "ApplicabilityCriteria": [],
    "DatasetType": "CAU",
    "DatasetId": "CostAndUsage",
    "DatasetName": "Cost and Usage",
    "Type": "Static",
    "Order": 80,
    "ValidationCriteria": {
      "MustSatisfy": "SampleColumn MUST NOT be null when ChargeCategory is \"Purchase\".",
      "Keyword": "MUST NOT",
      "Requirement": {
        "CheckFunction": "CheckNotValue",
        "ColumnName": "SampleColumn",
        "Value": null
      },
      "Condition": {
        "CheckFunction": "CheckValue",
        "ColumnName": "ChargeCategory",
        "Value": "Purchase"
      },
      "Dependencies": [
        "CAU-ChargeCategory-C-000-M"
      ]
    }
  }
```
