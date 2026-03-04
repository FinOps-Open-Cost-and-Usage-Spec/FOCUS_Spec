# Guidelines for writing model rules

As the FOCUS working group moves to introduce a formal rule definition structure the requirement for FOCUS members to understand how to read and write rules will increase. This guide is here to assist those who are starting their journey in writing rules for FOCUS.

The `specification/requirements_model` folder contains modular model components and a Python-based build process that assembles them into a validated `model-<version>.json` file using a corresponding JSON Schema (`model_schema.json`).

## Model document overview

The model document for FOCUS contains the following major sections:

| Section | Purpose |
|---------|---------|
| Details | Key details about the model document |
| ApplicabilityCriteria | Key flags used to define attributes about the data generator that need to be true for some model rules to apply |
| CheckFunctions | Method definitions to describe the actual check needed to conform to a rule |
| ModelDatasets | List of datasets defined by FOCUS and the related top level model rules associated with the dataset |
| ModelRules | Individual model rule definitions that are linked together by requirements and dependencies to form the full model ruleset |

## Steps to apply model rules to existing attributes and columns

An Action Item (AI) ticket should be opened to track the progress of implementing the model rules for an existing check.

### Stage 1

The first stage of conversion of rules from the normative text to model rules is for a table to be generated with the format as follows:

- `ModelRuleId` - Is the formal Id given to this entry in the model rules (See: [RM Expression Format](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/1121-ai-align-on-approach-for-scrs/specification/requirements_model/README.md#-cr-expression-format))
- `Function` - The type of rule to be defined (Valid types: `Composite`, `Presence`, `Type`, `Format`, `Validation`)
- `Reference` - The Column/Attribute Id this rule applies to
- `EntityType` - The type of entity this rule applies to (Valid types: `Dataset`, `Column`, `Attribute`, `Object`, `Metadata`)
- `EntityName` - The human-readable name of the entity this rule applies to
- `EntityId` - The unique identifier of the entity this rule applies to
- `Notes` - Free form notes (short) included in the model rule document
- `ModelVersionIntroduced` - Requirement Model Version this rule was added to the Model Rules (See: [Model Versioning](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/1121-ai-align-on-approach-for-scrs/specification/requirements_model/README.md#versioning))
- `Status` - Status of the rule (Valid values: Active, Deprecated, Removed)
- `ModelVersionRemoved` - Requirement Model Version this rule was removed from the Model Rules
- `ApplicabilityCriteria` - Specific criteria that must be true of the data generator for this rule to apply to the dataset
- `Type` - Identifier if this is a Static or Dynamic rule, with Static rules being possible to assess model without external information being required
- `Order` - The order in which this rule should be processed or displayed
- `DatasetType` - The dataset type this rule applies to (e.g. "CAU" for Cost and Usage, "CCT" for Contract Commitment)
- `DatasetId` - The identifier of the dataset this rule belongs to (Required for Column and Dataset entity types, e.g. "CostAndUsage" for Cost and Usage, "ContractCommitment" for Contract Commitment)
- `DatasetName` - The human-readable name of the dataset this rule belongs to (Required for Column and Dataset entity types, e.g. "Cost and Usage" for Cost and Usage,
- `ValidationCriteria` - The detailed criteria that defines how this rule is to be validated,
  - `MustSatisfy` - The normative text that this rule defines
  - `Keyword` - The Normative keyword that applies to this rule (Allowed Values: `MUST`, `RECOMMENDED`, `SHOULD`, `MAY`, `OPTIONAL`)
  - `Requirement` - The definition of what is required for model
  - `Condition` - The definition of conditions under which this rule applies


#### Stage 1: Rule-Based Extraction of Normative Requirements

Stage 1 defines a rule-based extraction process for converting normative requirements from FOCUS Releases into a structured, machine-readable JSON representation. The objective of this stage is not to model the extraction visually, but to ensure that each normative statement in the specification is deterministically identified, classified, and represented using the set of JSON properties defined in the previous section.

During Stage 1, normative requirements are extracted by applying a fixed set of authoring and interpretation rules that govern how requirements are detected, how scope and applicability are determined, and how each requirement is expressed without inference or reinterpretation. The resulting JSON output must strictly conform to the required property structure, enabling consistency across releases and supporting downstream automation, validation, and analysis workflows.

This stage intentionally avoids diagrammatic representations, as the extraction logic is entirely driven by the prescribed rules and constraints. The focus is on accuracy, repeatability, and structural alignment with the defined JSON model, ensuring that Stage 1 produces a faithful and complete representation of the normative requirements as written in the FOCUS specification.

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
| `Column`           | Named field across rows                             | Data type, format, constraints            | Each item in `AllocatedMethodDetailsObject.Elements` MUST be an object.                                                         |
| `Object`           | JSONObject content of a column                      | Data type, format, constraints            | Column `BillingPeriodStart` MUST be of type `DateTime`                                                          |
| `Attribute`        | Shared formatting/logic constraint                  | Formatting consistency across columns     | All `String` columns MUST conform to `StringHandling` requirements                                              |

#### 2. RMID – Apply RMID Naming Rules

Construct a unique identifier for the rule using the format:  
`{{ColumnID}}-{{EntityType}}-{{NNN}}-{{Level}}`

This ensures traceability, uniqueness, and clarity.

- Use the format: `DatasetType-ColumnID-EntityType-NNN-Level`
- `DatasetType`: Short identifier for the dataset (e.g., `CAU`, `CC`, `META`)
- `ColumnID`: UpperCamelCase (e.g., `ListUnitPrice`)
- `EntityType:`
  - `D` = Dataset  
  - `C` = Column
  - `O` = Object
  - `A` = Attribute  
  - `M` = Metadata
  - `O` = Object
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

The `NNN` numbering is only unique within each dataset namespace. For example, `CAU-ListPrice-C-000-M` and `CC-ListPrice-C-000-M` can both exist independently - the `000` is reused and only needs to be unique within that specific dataset abbreviation.

##### Examples

- Cost and Usage dataset: `CAU-BillingAccountName-C-000-M`
- Contract Commitment dataset: `CC-CommitmentDiscountId-C-001-M`

##### Dataset Abbreviations

| Dataset | Abbreviation | Description |
|---------|--------------|-------------|
| Cost and Usage | CAU | Primary billing data with usage and cost information |
| Contract Commitment | CCT | Commitment discount and reservation data |

This namespacing approach prevents naming conflicts between datasets and provides clear traceability of which dataset a requirement belongs to.

#### 3. Function – Classify the rule type

Categorize the type of logic the rule enforces. This helps determine how it should be validated.

- Use `Presence` for rules requiring the column’s inclusion in the dataset.
- Use `DataType` to enforce primitive types like `Decimal`, `String`, `Boolean`.
- Use `Format` for pattern-based constraints (e.g., `DateTimeFormat`, `UUID`, `NumericFormat`).
- Use `NullabilityRules` to define when values must or must not be null.
- Use `Validation` for business logic or fixed-value conditions not covered above.
- Use `Composite` to group multiple RMIDs with logical expressions (`AND` / `OR` / `NOT`).
- Use `Ambiguous` only when no clear classification is possible.

**Example**  
A rule states: "`BillingPeriodStart` MUST be of type `DateTime`."  
→ `Function = Format`

#### 4. Reference – Identify the reference target

Point to the human-readable column or attribute name that the rule applies to, as defined in the FOCUS specification.

- Use the `display_name` for the column as written in the spec.
- For rules related to attribute-level constraints (e.g., `NumericFormat`), use the attribute name.
- This field should exactly match the title of the column or attribute from the normative requirements.

**Example**  
If the rule applies to the column `CommitmentDiscountQuantity`, set:  
→ `Reference = Commitment Discount Quantity`

#### 5. Keyword – Extract the normative keyword

Determine the obligation level using the normative keyword from the source text, such as `MUST`, `SHALL`, `SHOULD`, or `MAY`.

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

#### 6. Applicability Criteria (GATE) – Determine if the rule should be evaluated

Define the dataset-level or service-provider-level condition that determines when the rule is relevant for evaluation.

- Use `"All_Rows"` when no structural gating is defined.
- Use a dataset-level statement (e.g., `"Dataset includes ChargeCategory column"`) for presence rules.
- Use a service provider or environment condition if the rule depends on system capabilities  
  (e.g., `"Service Provider supports capacity reservation"`).
- For composite rules, inherit the most restrictive gating condition from child RM Items.
- Do not leave this field blank. Only omit if the applicability is inherited from a parent composite.

**Example**  
A presence rule states: “Column `CapacityReservationId` MUST be present when the service provider supports capacity reservation.”  
→ `ApplicabilityCriteria = Service Provider supports capacity reservation`

#### 7. Condition (GATE) – Specify when to test

Define the row-level logic that determines whether the rule should be applied to a given record in the dataset.

- Use `"All_Rows"` if the rule applies to every row in the dataset.
- If the rule applies conditionally, extract the condition from the normative text using simple boolean logic.

**Example patterns:**

- `ChargeCategory = "Purchase"`
- `CommitmentDiscountQuantity IS NOT NULL`

- Always express conditions in a machine-readable, testable format.
- Never leave this field empty or set to `null`.

**Example**  
A rule states: “`SkuId` MUST be present when `ChargeCategory = Purchase`.”  
→ `Condition = ChargeCategory = "Purchase"`

#### 8. MustSatisfy – Define how to test the rule

State the actual behavior or constraint being enforced by the rule in a testable format, using the original normative keyword.

- Express the rule in clear, declarative language.
- Use the same keyword (`MUST`, `SHOULD`, `MAY`) as in the normative requirement.
- Keep the logic atomic — this field should describe only the rule itself, not any dependencies or logical groupings.
- Exclude conditional logic — that belongs in the `Condition` field.

**Example**  
A rule states: “`BillingPeriodStart` MUST be of type `DateTime`.”  
→ `MustSatisfy = MUST be of type DateTime`

#### 9. Requirement – Identify logical dependencies

Define whether the rule groups or depends on other RMIDs or attribute rule sets.

- Use a logical expression (`AND()`, `OR()`, `NOT()`) to group RMIDs in composite rules.
- If the rule refers to a shared attribute rule set (e.g., `NumericFormat`, `StringHandling`), use:  
  `Requirement = NumericFormat:RM`
- Set to `"null"` for atomic rules that do not depend on other rules or attributes.
- Always define this field for composite rules, and make sure referenced RMIDs exist or appear later in the table.

**Example**  
A rule states: “The following rules MUST be enforced for `CommitmentDiscountQuantity` when it is not null…” and lists three RMs.  
→ `Requirement = AND(CommitmentDiscountQuantity-C-010-M, CommitmentDiscountQuantity-C-011-C, CommitmentDiscountQuantity-C-012-C)`

#### 10. Validation Type – Indicate static vs. dynamic

Specify whether the rule can be validated using only the dataset itself or if it depends on external systems or metadata.

- Use `static` if the rule can be enforced by examining the dataset alone:  
  Example: value types, nullability, formatting, or schema presence.
- Use `dynamic` if validation depends on:
  - External invoice records  
  - Catalog metadata  
  - Service Provider configuration or billing systems
- For composite rules, set to `dynamic` if any child RM Item is dynamic.

**Example**  
A rule states: “`BillingAccountType` MUST align with the service provider’s contractual agreement.”  
→ `Validation Type = dynamic`

#### 11. ModelVersionIntroduced – Version tracking

Record the version of the FOCUS specification in which this rule was introduced.

- For all rules generated from FOCUS v1.2, set this field to `"1.2"`.
- Do not infer or omit — this value is fixed for each release of the specification.
- This field enables forward/backward compatibility during conformance testing.

**Example**  
→ `ModelVersionIntroduced = 1.2`

#### 12. Status – Set rule lifecycle status

Indicate whether the rule is `active`, `deprecated`, or `removed` for future use.

- Default to `active` unless the normative text explicitly states otherwise.
- Use `deprecated` if the rule is marked for removal or obsolescence.
- Use `removed` if the rule is removed from the model.

**Example**  
A rule marked in the spec as legacy:  
“This requirement will be removed in future versions.”  
→ `Status = deprecated`

#### 13. Notes – Capture comments

Use this field to add clarifying comments, editorial notes, or cross-references to other RM Items or attributes.

- Add contextual information for better understanding of the rule.
- For attribute-based dependencies, always include a note like:  
  `Cross-attribute reference: NumericFormat:RM`
- For column-to-column dependencies, use:  
  `Cross-column reference: BillingPeriodEnd-C-001-M`
- Leave blank only when no additional clarification is needed.

**Example**  
A rule that delegates to `NumericFormat`  
→ `Notes = Cross-attribute reference: NumericFormat:RM`

#### 14. DatasetId and DatasetName – Dataset Association

For Column and Dataset entity types, these fields establish the relationship between the rule and its parent dataset.

**Reasoning Rules**

- `DatasetId` must match the identifier of the dataset the entity belongs to
- `DatasetName` must match the human-readable name of the dataset
- Both fields are required for all Column and Dataset entity types
- For Cost and Usage dataset: `DatasetId = "CostAndUsage"`, `DatasetName = "Cost and Usage"`
- For Contract Commitment dataset: `DatasetId = "ContractCommitment"`, `DatasetName = "Contract Commitment"`
- These fields ensure proper dataset-rule association and enable dataset-specific validation

**Example**  
For a rule applying to a column in the Cost and Usage dataset:  
→ `DatasetId = CostAndUsage`  
→ `DatasetName = Cost and Usage`

### Stage 2

The second phase of conversion is to take the table created in Stage 1 and create the entries in the `specification/requirements_model` folder that adds the rules to the formal JSON structure.

#### Folder structure

- `cr_details.json`: Metadata like versioning
- `applicability_criteria.json`: Feature flags controlling rule application
- `check_functions.json`: Logical validation functions and their arguments
- `model_datasets.json`: Maps datasets (e.g. FOCUS) to rule sets
- `model_rules/attributes/`: JSON files defining multiple `ModelRules` for a single attribute
- `model_rules/columns/`: JSON files defining multiple `ModelRules` for a single column

#### Steps

- Assign the Action Item (AI) to yourself to signal that you are working on the item (See: [GitHub Issues](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues))
- Open a branch with the source of git branch `1121-ai-align-on-approach-for-scrs` for your development work with the naming format as follows `ai number`-cr-`entity-name`-1121. (example: 1255-cr-AvailabilityZone-1121)
- Pull your branch to your development environment and perform all work specific to this AI in this branch.
- Add a file into the relevant folder `model_rules/attributes/` or `model_rules/columns/` with name `entity-name`.json (example: availabilityzone.json)
- Write your rules into this file based on the rules in the Stage 1 table from the AI ticket (See: [ModelRule Templates](#modelrule-templates) for helpers)
- If you need to add new ApplicabilityCriteria add them to `applicability_criteria.json` avoiding duplication
- If you need to add new CheckFunctions add them to `check_functions.json` avoiding duplication
- Add your top level model rule entry into the relevant Dataset entries in the `model_datasets.json` file
- Commit your changes to your branch and then move onto raising the PR section
If you need assistance reach out to Mike Fuller in the FOCUS slack

## Pull Request Workflow

- Navigate to Github and raise a pull request (PR) from your `ai number`-cr-`entity-name`-1121 branch to the `1121-ai-align-on-approach-for-scrs` branch
- Ensure you link the opened PR to your issue ticket by using the development cog on the right side of the PR page
- Assign the PR to `mike-finopsorg`
- Announce your PR in the [#tf-conformance-requirements](https://f2-focus.slack.com/archives/C096UTPE3NF) slack channel for other members to see
- Once reviewed and the members have had time (5 days) to add any feedback, Mike will merge the PR into the `1121-ai-align-on-approach-for-scrs` branch which will get full review when that branch is reviewed to merge into the `working_draft` branch via the PR [FR #1054: Initial commit with Model Data structure](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/1209)

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
- The `Order` field is optional but recommended for rules that need explicit sequencing

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
        "CAU-OtherRule-C-001-M",    // Order: 5
        "CAU-AnotherRule-C-002-M"   // Order: 15
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
    "Order": 10,
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
    "Order": 10,
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
    "Order": 10,
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
    "Order": 10,
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
    "Order": 10,
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
    "Order": 10,
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
