# Guidelines for writing model rules

The FOCUS Requirements Model is a machine-readable representation of the normative requirements defined in the FOCUS specification. Each model rule is the programmatic equivalent of a normative statement in the specification text—transforming human-readable requirements (written using keywords like MUST, SHOULD, and MAY) into structured JSON that can be programmatically validated, tested, and enforced. This one-to-one mapping between specification requirements and model rules enables automated conformance testing, tooling integration, and consistent interpretation of FOCUS requirements across different implementations. By capturing rules in a standardized format with explicit dependencies, conditions, and validation logic, the Requirements Model ensures that FOCUS datasets can be reliably validated against specification requirements.

With the formal rule definition structure now in place, FOCUS members need to understand how to read and write model rules effectively. This guide assists those working with the Requirements Model, whether creating new rules, maintaining existing ones, or validating datasets against FOCUS requirements.

The `specification/requirements_model` folder contains modular model components organized by version under `releases/X.Y/` directories. A Python-based build process assembles these components into a validated `model-<version>.json` file using a corresponding JSON Schema (`model_schema.json`). The `releases/latest/` symlink always points to the most recent model version.

## Model document overview

The model document for FOCUS contains the following major sections:

| Section | Purpose |
|---------|---------|
| Details | Key details about the model document |
| ApplicabilityCriteria | Key flags used to define attributes about the data generator that need to be true for some model rules to apply |
| CheckFunctions | Method definitions to describe the actual check needed to conform to a rule |
| ModelDatasets | List of datasets defined by FOCUS and the related top level model rules associated with the dataset |
| Schemas | Reusable JSON Schema definitions that can be referenced by validation rules |
| ModelRules | Individual model rule definitions that are linked together by requirements and dependencies to form the full model ruleset |

## Steps to create model rules for FOCUS entities

An Action Item (AI) ticket should be opened to track the progress of implementing the model rules for an existing check.

### Stage 1

The first stage of conversion of rules from the normative text to model rules is for a table to be generated with the format as follows:

- `ModelRuleId` - Formal identifier for this model rule entry
- `Function` - The type of rule to be defined (Valid types: `Composite`, `Presence`, `Type`, `Format`, `Validation`, `Nullability`)
- `Reference` - The Column/Attribute Id this rule applies to
- `EntityType` - The type of entity this entry applies to (Valid types for ModelRules: `Dataset`, `Column`, `Attribute`, `Object`; valid type for Schemas entries: `Schema`)
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
- `DatasetName` - The human-readable name of the dataset this rule belongs to (Required for Dataset, Column, and Object entity types, e.g. "Cost and Usage" for Cost and Usage)
- `ValidationCriteria` - The detailed criteria that defines how this rule is to be validated
  - `MustSatisfy` - The normative text that this rule defines
  - `Keyword` - The Normative keyword that applies to this rule (Allowed Values: `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`)
  - `Requirement` - The definition of what is required for model
  - `Condition` - The definition of conditions under which this rule applies
  - `Dependencies` - A list of prerequisite rules that must be evaluated before this rule, ordered by sequence


#### Stage 1: Rule-Based Extraction of Normative Requirements

Stage 1 converts normative requirements from the FOCUS specification into structured, machine-readable JSON using the property definitions below. Apply the extraction rules deterministically to ensure each normative statement is consistently identified, classified, and represented without inference or reinterpretation. The resulting JSON must strictly conform to the defined structure, enabling consistency across releases and supporting automation, validation, and analysis workflows.

#### High-Level Description of the Model Rule Properties

#### 1. Target Entity – Determine the entity

Identify the target for the rule:

- **Attribute**
- **Dataset**
- **Column**
- **Object**
- **Schema**

This sets the scope of the model requirement.

#### FOCUS Core Entities

The following architectural components define the core entities in FOCUS that shape the structure and flow of billing data.

<img width="491" height="491" alt="Image" src="https://github.com/user-attachments/assets/a30d828e-d2af-4185-984c-475998466437"/>

- **Dataset, Column, Object, Attribute, and Schema** are the **core structural entities** used across the requirements model.


##### FOCUS Entity Reference Table

| Entity             | Description                                         | Applies To                                | Example RM Function                                                                                             |
|--------------------|-----------------------------------------------------| ----------------------------------------- |-----------------------------------------------------------------------------------------------------------------|
| `Dataset`          | Whole billing dataset                               | Structural presence, versioning, coverage | Dataset MUST include all columns required by the declared FOCUS version                                         |
| `Column`           | Named field across rows                             | Data type, format, constraints            | Column `BilledCost` MUST be of type `Decimal`                                                          |
| `Object`           | JSONObject content of a column                      | Data type, format, constraints            | Object property `name` MUST be of type `String`                                                          |
| `Attribute`        | Shared formatting/logic constraint                  | Formatting consistency across columns     | All `String` columns MUST conform to `StringHandling` requirements                                              |
| `Schema`           | Reusable JSON Schema definition                     | Formal structural validation of JSON data | `AllocatedMethodDetailsObject` MUST conform to `AllocatedMethodDetailsObjectSchema`                            |

For detailed guidance on working with each entity type, see the [Working with Entity Types](#working-with-entity-types) section below.

#### 2. RMId – Apply Requirements Model ID (RMId) Naming Rules

Construct a unique identifier for the rule using the appropriate format based on entity type. This ensures traceability, uniqueness, and clarity.

##### RMId Format by Entity Type

**For Attributes:**  
`AttributeName-EntityType-NNN-Level`

**For Datasets, Columns, and Objects:**  
`DatasetType-EntityId-EntityType-NNN-Level`

**For Schemas entries:**  
`DatasetType-EntityId-S-NNN-Level`

##### RMId Component Definitions

- `AttributeName`: Name of the attribute (e.g., `NumericFormat`, `StringHandling`, `InvoiceHandling`)
- `DatasetType`: Short identifier for the dataset (e.g., `CAU`, `CCT`)
- `EntityId`: UpperCamelCase identifier for the entity (e.g., `ListUnitPrice`, `CostAndUsage`, `AllocatedMethodDetailsObject`)
- `EntityType:`
  - `D` = Dataset  
  - `C` = Column
  - `O` = Object
  - `A` = Attribute
  - `S` = Schema
- `NNN:` Sequential number (unique only within the entity namespace)
  - `000` for root composite  
  - `0NN` for intermediate composites  
  - `001+` for single atomic rules
- `Level:`  
  - `M` = Mandatory (from MUST)  
  - `C` = Conditional (e.g., SHOULD under a condition)  
  - `O` = Optional (from MAY or unconditional SHOULD)

##### RMId Examples

**Attribute rule example:**  
→ `RMId = NumericFormat-A-001-M`

**Column rule example:**  
→ `RMId = CAU-ListUnitPrice-C-003-M`

**Dataset rule example:**  
→ `RMId = CAU-CostAndUsage-D-008-M`

**Object rule example:**  
→ `RMId = CAU-AllocatedMethodDetailsObject-O-001-M`

**Schema entry example:**  
→ `RMId = CAU-AllocatedMethodDetailsObjectSchema-S-001-M`

#### Multi-Dataset Entity Structure and Naming

The FOCUS specification supports multiple datasets, each with their own requirements. The following decisions have been made regarding entity structure and naming:

##### Dataset-Specific Requirement Entities

Each dataset will reference their own set of Requirement Entities. A single requirement item should not be referenced by multiple datasets - they should have their own entry. This ensures:

- Clear separation of concerns between datasets
- Independent evolution of dataset requirements
- Simplified validation and testing per dataset
- Reduced complexity in rule dependencies

##### Dataset-Namespaced Naming Convention

Column entities are now namespaced by the dataset they belong to. The RMId format has been updated to:

`DatasetType-ColumnId-EntityType-NNN-Level`

Where:

- `DatasetType`: Short identifier for the dataset (e.g., `CAU` for Cost and Usage)
- `ColumnId`: The column identifier in UpperCamelCase
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

#### Suffix Determination Logic

The suffix (`-M`, `-O`, or `-C`) at the end of each RMId is determined through a precedence-based algorithm that evaluates scope, dependencies, and normative keywords. Understanding this logic is critical for correctly constructing RMIds.

##### Precedence Hierarchy

The suffix is determined by applying the following rules in order. Once a rule matches, the suffix is set and no further rules are evaluated:

**1. Scope Precedence (Always `-C`)**

If a rule has **any** of the following scope indicators, it **MUST** use the `-C` suffix:
- Non-empty `ApplicabilityCriteria` array (e.g., `["COMMITMENT_DISCOUNT_SUPPORTED"]`)
- Non-empty `Condition` object (row-level conditions)
- Conditional keywords in `MustSatisfy` text: "when", "unless", or "where"

**Examples:**

```json
// ApplicabilityCriteria present → -C
"CAU-AvailabilityZone-C-000-C": {
  "ApplicabilityCriteria": ["AVAILABILITY_ZONE_SUPPORTED"],
  ...
}

// Condition present → -C
"CCT-ContractCommitmentQuantity-C-004-C": {
  "ValidationCriteria": {
    "Condition": {
      "CheckFunction": "CheckValue",
      "ColumnName": "ContractCommitmentCategory",
      "Value": "Usage"
    }
  },
  ...
}

// "when" in MustSatisfy → -C
"MustSatisfy": "ConsumedQuantity MUST be null when ChargeCategory is not 'Usage'."
```

**2. Composite Rules with All-Scoped Requirements (→ `-C`)**

For `Function: "Composite"` rules where **ALL** rules referenced in the `Requirement` field have scope (per rule 1), the composite rule **MUST** use `-C` suffix.

**Example:**
```json
// All child rules have ApplicabilityCriteria → Parent gets -C
"CAU-SampleColumn-C-003-C": {
  "Function": "Composite",
  "ValidationCriteria": {
    "Requirement": {
      "CheckFunction": "AND",
      "Items": [
        {
          "CheckFunction": "CheckModelRule",
          "ModelRuleId": "CAU-SampleColumn-C-004-C"
        },
        {
          "CheckFunction": "CheckModelRule",
          "ModelRuleId": "CAU-SampleColumn-C-005-C"
        }
      ]
    }
  }
}
```

**3. Composite Rules with Presence Dependencies (→ `-M` or `-O`)**

For `Function: "Composite"` rules that don't match rules 1 or 2, examine the `Dependencies` array for rules with `Function: "Presence"`:

- If **ANY** Presence dependency has `Keyword` in `{"MUST", "SHOULD"}` → use `-M` suffix
- Else if **ANY** Presence dependency has other keyword → use `-O` suffix
- If no Presence dependencies match, continue to rule 4

**Example:**
```json
// Has Presence dependency with MUST → -M
"CAU-SampleColumn-C-000-M": {
  "Function": "Composite",
  "ValidationCriteria": {
    "Dependencies": [
      "CAU-SampleDataset-D-010-M"  // This is Presence rule with Keyword: "MUST"
    ]
  }
}
```

**4. Base Keyword Handling (No scope, non-composite or no special dependencies)**

For rules that don't match rules 1-3, use the normative `Keyword` field:
- `MUST` or `MUST NOT` → `-M` suffix
- `MAY`, `SHOULD`, `SHOULD NOT` → `-O` suffix

**Examples:**
```json
// MUST keyword, no scope → -M
"CAU-BilledCost-C-001-M": {
  "ApplicabilityCriteria": [],
  "ValidationCriteria": {
    "Keyword": "MUST",
    "MustSatisfy": "BilledCost MUST be of type Decimal.",
    "Condition": {}
  }
}

// MAY keyword, no scope → -O
"InvoiceHandling-A-003-O": {
  "ApplicabilityCriteria": [],
  "ValidationCriteria": {
    "Keyword": "MAY",
    "MustSatisfy": "Informational line items... MAY be excluded.",
    "Condition": {}
  }
}
```

##### Validation

The test suite validates suffix correctness in `test_suffix_by_keyword_and_scope.py`. This test:
- Checks all rules for proper suffix assignment
- Fails if a rule does not end with the correct suffix

When creating new rules, run the test suite to validate your suffix choices:
```bash
pytest specification/requirements_model/tests/test_suffix_by_keyword_and_scope.py
```

##### Quick Reference

| Condition | Suffix |
|-----------|--------|
| Has ApplicabilityCriteria | `-C` |
| Has non-empty Condition | `-C` |
| "when"/"unless"/"where" in MustSatisfy | `-C` |
| Composite with all scoped children | `-C` |
| Composite with MUST/SHOULD Presence dep | `-M` |
| Composite with other Presence dep | `-O` |
| MUST/MUST NOT keyword (no scope) | `-M` |
| MAY/SHOULD/SHOULD NOT (no scope) | `-O` |

#### 3. Function – Classify the rule type

Categorize the type of logic the rule enforces. This helps determine how it should be validated.

Note: This property applies to `ModelRules` entries only. `Schemas` entries do not use a `Function` field.

- Use `Presence` for rules requiring the column’s inclusion in the dataset.
- Use `Type` to enforce primitive types like `Decimal`, `String`, `Boolean`.
- Use `Format` for pattern-based constraints (e.g., `DateTimeFormat`, `UUID`, `NumericFormat`).
- Use `Nullability` to define nullability rules, both conditional (e.g., "MUST NOT be null when condition X") and unconditional (e.g., "MUST NOT be null").
- Use `Validation` for business logic or fixed-value conditions not covered above.
- Use `Composite` to group multiple RMIds with logical expressions (`AND` / `OR` / `NOT`).

**Examples**  
Rule states "`BillingPeriodStart` MUST be of type `DateTime`":  
→ `Function = Type`

Rule states "`CommitmentDiscountQuantity` MUST NOT be null when `ChargeCategory` is `Purchase`":  
→ `Function = Nullability`

#### 4. Reference – Identify the reference target

Provide the identifier for the column or attribute that the rule applies to, using the PascalCase Id format.

- For datasets: Use the DatasetId (e.g., `CostAndUsage`)
- For columns: Use the ColumnId (e.g., `CommitmentDiscountQuantity`)
- For objects: Use the ObjectId (e.g., `AllocatedMethodDetailsObject`)
- For attributes: Use the attribute name (e.g., `NumericFormat`, `StringHandling`)
- For schemas in `Schemas`: `Reference` is not used; use `EntityId` and `Schema`
- This field should match the Id as defined in the FOCUS specification

**Example**  
If the rule applies to the column with Id `CommitmentDiscountQuantity`:  
→ `Reference = CommitmentDiscountQuantity`

#### 5. Keyword – Extract the normative keyword

Determine the obligation level using the normative keyword from the source text, such as `MUST`, `SHOULD`, or `MAY`.

- Identify the first normative keyword present in the requirement:
  - `MUST`, `MUST NOT` → Mandatory
  - `SHOULD`, `SHOULD NOT` → Optional
  - `MAY` → Optional
- Normalize the keyword to uppercase.
- Only one keyword should be assigned per RM Item.
- For composite rules, choose the highest obligation level from constituent RMIds  
  (e.g., prioritize `MUST` > `SHOULD` > `MAY`).

**Example**  
A rule states: “Rows SHOULD include `SkuId` when `ChargeCategory = Purchase`.”  
→ `Keyword = SHOULD`

#### 6. Applicability Criteria – Determine if the rule should be evaluated

Specify provider capability flags that determine when the rule applies. These keys are defined in the `applicability_criteria.json` file for each model version.

- Use an empty list `[]` when no applicability gating is required
- Use array of criteria keys when rule depends on provider capabilities  
  (e.g., `["COMMITMENT_DISCOUNT_SUPPORTED"]`, `["CAPACITY_RESERVATION_SUPPORTED"]`)

**ApplicabilityCriteria Reference:**

The following provider capability flags are defined in the model. Use these to gate rules that depend on specific data generator capabilities.

**Location**: `specification/requirements_model/releases/X.Y/applicability_criteria.json` (or `releases/latest/applicability_criteria.json` for current version)

| Key | Description |
|-----|-------------|
| `ACCOUNT_NAMING_SUPPORTED` | Provider supports account naming features |
| `AVAILABILITY_ZONE_SUPPORTED` | Provider supports availability zone identification |
| `BILLING_BASED_ON_PROVISIONED_RESOURCES_SUPPORTED` | Billing is based on provisioned resources |
| `CAPACITY_RESERVATION_SUPPORTED` | Provider supports capacity reservations |
| `COMMITMENT_DISCOUNT_SUPPORTED` | Provider supports commitment-based discounts |
| `CONTRACT_COMMITMENTS_SUPPORTED` | Provider supports contract commitments |
| `DATA_GENERATOR_SPLIT_COST_ALLOCATION_SUPPORTED` | Data generator performs split cost allocation |
| `MULTIPLE_BILLING_ACCOUNT_TYPES_SUPPORTED` | Provider supports multiple billing account types |
| `MULTIPLE_PRICING_CATEGORIES_SUPPORTED` | Provider supports multiple pricing categories |
| `MULTIPLE_SUB_ACCOUNT_TYPES_SUPPORTED` | Provider supports multiple sub-account types |
| `NEGOTIATED_PRICING_SUPPORTED` | Provider supports negotiated pricing |
| `PRICING_BILLING_CURRENCY_DIFFERENCES_SUPPORTED` | Pricing and billing currencies can differ |
| `PUBLIC_PRICE_LIST_SUPPORTED` | Provider publishes a public price list |
| `REGION_SUPPORTED` | Provider supports regional identification |
| `RESOURCE_TYPE_ASSIGNMENT_SUPPORTED` | Provider supports resource type assignment |
| `SUB_ACCOUNT_SUPPORTED` | Provider supports sub-accounts |
| `TAGGING_SUPPORTED` | Provider supports resource tagging |
| `UNIT_PRICING_SUPPORTED` | Provider supports unit-based pricing |
| `USAGE_MEASUREMENT_SUPPORTED` | Provider measures and reports usage |
| `VIRTUAL_CURRENCY_SUPPORTED` | Provider uses virtual currency |

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
- Use `CheckFunction: "CheckModelRule"` inside the `Items` array to reference other RMIds

For **Atomic rules**, use specific CheckFunction types from the model:
- `ColumnPresent` - Check if a column exists in the dataset
- `CheckNotValue` - Verify a column does not contain a specific value
- `CheckValue` - Verify a column contains a specific value
- `TypeDecimal`, `TypeString` - Check data type
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

Note: Do not confuse the Type property (Static/Dynamic) with the Function property value of "Type" (which refers to data types like Decimal or String).

Indicates whether the rule can be validated using only the dataset itself or requires external dependencies.

- `Static` - Rule can be validated by examining the dataset alone (data types, nullability, formatting, schema presence)
- `Dynamic` - Rule requires external dependencies (invoice records, catalog metadata, provider configuration)

For composite rules, use `Dynamic` if any child rule is dynamic.

**Example**  
Rule checks data type: `Type = Static`  
Rule validates against provider catalog: `Type = Dynamic`

#### 11. ModelVersionIntroduced – Version tracking

Record the version of the FOCUS specification in which this rule was introduced.

- Set this field to the model version where the rule first appears (e.g., `"1.2"`, `"1.3"`)
- This value is fixed for each release and should not be changed once set
- This field enables forward/backward compatibility during conformance testing and version-specific rule filtering

**Version-Specific Model Structure:**

The Requirements Model uses a multi-version structure under `specification/requirements_model/releases/`:
- Each version has its own directory: `releases/1.2/`, `releases/1.3/`, etc.
- The `releases/latest/` symlink points to the most recent model version
- When creating new rules, work in the appropriate version directory (typically `releases/latest/`)
- The build process generates separate `build/model-X.Y.json` files for each version
- Tests are parametrized to run against all model versions

**When working with versions:**
- New rules added in a release should set `ModelVersionIntroduced` to that release version
- Rules inherited from previous versions keep their original `ModelVersionIntroduced` value
- The test suite validates rules against their declared version compatibility

**Example**  
New rule added in FOCUS v1.3:  
→ `ModelVersionIntroduced = "1.3"`

Rule originally from FOCUS v1.2 (unchanged):  
→ `ModelVersionIntroduced = "1.2"`

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

For Dataset, Column, Object, and Schema entity types, these fields establish the relationship between the entry and its parent dataset.

**Reasoning Rules**

- `DatasetId` must match the identifier of the dataset the entity belongs to
- `DatasetName` must match the human-readable name of the dataset
- Both fields are required for Dataset, Column, Object, and Schema entity types
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

**Special Requirement for Column Root Composites:**

Column root composite rules (`-C-000-M` or `-C-000-C`) **MUST** include their Dataset presence rule as the first dependency. This ensures the dataset exists and contains the column before any column-level validation occurs.

**Ordering Requirements:**

- Dependencies must be listed in ascending order by their `Order` field values
- For Column root composites, the Dataset presence rule comes first
- This ensures rules are evaluated in the correct sequence
- Automated tests validate dependency ordering

**Examples:**

Unconditional rule with no dependencies:
→ `Dependencies = []`

Column root composite with Dataset presence rule first:
```json
"CAU-ChargeCategory-C-000-M": {
  "ValidationCriteria": {
    "Dependencies": [
      "CAU-CostAndUsage-D-008-M",
      "CAU-ChargeCategory-C-001-M",
      "CAU-ChargeCategory-C-002-M",
      "CAU-ChargeCategory-C-003-M"
    ]
  }
}
```

Nullability rule that depends on another column:
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

### Working with Entity Types

This section provides detailed guidance for creating requirements model entries for each entity type in FOCUS.

#### Working with Attribute Entity Types

Attribute entity types define cross-cutting requirements that apply to multiple columns across datasets. Attributes ensure consistency in formatting, handling, and validation logic.

**What They Represent:**
- Cross-column formatting rules (e.g., `NumericFormat`, `StringHandling`, `DateTimeFormat`)
- Shared business logic patterns (e.g., `DiscountHandling`, `InvoiceHandling`)
- Common data type constraints (e.g., `CurrencyFormat`, `UnitFormat`)

**Key Characteristics:**

1. **Naming Convention**: Attribute EntityIds use descriptive names (e.g., `NumericFormat`, `StringHandling`, `DiscountHandling`)
2. **RMId Format**: Use `-A-` in EntityType position: `NumericFormat-A-001-M`
3. **No DatasetType**: Attributes are not dataset-specific, so RMId starts with the attribute name
4. **Referenced by Columns**: Column rules reference attribute rules to inherit common requirements

**Creating Attribute Rules:**

1. Extract attribute requirements from the FOCUS specification (attributes are defined by the spec)
2. Create attribute composite rule (`-A-000-M`) grouping all related attribute requirements from the spec
3. Create individual atomic rules for each specific constraint defined in the spec
4. Column rules reference these attribute rules using `CheckFunction: "CheckModelRule"` with the attribute RMId

**File Organization:**

Attribute rules are stored in: `specification/requirements_model/releases/X.Y/model_rules/attributes/`

#### Working with Dataset Entity Types

Dataset entity types define requirements for entire datasets, including structural presence, versioning, and mandatory column requirements.

**What They Represent:**
- Dataset-level presence validation
- Dataset versioning and metadata requirements
- Mandatory column coverage for the dataset
- Dataset-wide configuration rules

**Key Characteristics:**

1. **Naming Convention**: Dataset EntityIds match the dataset identifier (e.g., `CostAndUsage`, `ContractCommitment`)
2. **RMId Format**: Use `-D-` in EntityType position: `CAU-CostAndUsage-D-001-M`
3. **Root Composite Pattern**: Dataset root composite (`-D-000-M`) groups all dataset-level requirements
4. **Dataset Coverage**: Dataset rules typically reference all mandatory column composite rules

**Creating Dataset Rules:**

1. Create dataset root composite (`-D-000-M`) as the entry point for all dataset requirements
2. Reference all mandatory column composites in the dataset's Dependencies
3. Add dataset-level validation rules (metadata, versioning, coverage)
4. Ensure proper ordering of dependencies

**File Organization:**

Dataset rules are stored in: `specification/requirements_model/releases/X.Y/model_rules/datasets/<dataset_id>/`

#### Working with Column Entity Types

Column entity types define requirements for individual columns within a dataset, including presence, data type, format, nullability, and value constraints.

**What They Represent:**
- Column presence requirements
- Data type validation (Decimal, String, Boolean, DateTime)
- Format constraints (conformance to attributes like NumericFormat)
- Nullability rules (conditional and unconditional)
- Allowed value constraints

**Key Characteristics:**

1. **Naming Convention**: Column EntityIds match the column identifier in PascalCase (e.g., `BilledCost`, `ChargeCategory`)
2. **RMId Format**: Use `-C-` in EntityType position: `CAU-BilledCost-C-001-M`
3. **Root Composite Pattern**: Column root composite (`-C-000-M` or `-C-000-C`) groups all column requirements
4. **Common Rule Sequence**: Presence → Type → Format → Nullability → Validation

**Creating Column Rules:**

1. Create column root composite (`-C-000-M` or `-C-000-C`) grouping all column requirements
2. Add Dataset presence rule as first dependency in the root composite Dependencies array
3. Add Presence rule if column is required in the dataset
4. Add Type rule defining the data type
5. Add Format rule referencing applicable attribute (e.g., `NumericFormat`, `StringHandling`)
6. Add Nullability or Validation rules for null handling and value constraints
7. Reference attribute rules where applicable for common formatting

**File Organization:**

Column rules are stored in: `specification/requirements_model/releases/X.Y/model_rules/datasets/<dataset_id>/columns/`

#### Working with Object Entity Types

Object entity types validate the internal structure and properties of JSON object columns. While Column entity types validate the column itself (presence, type, nullability), Object entity types validate the **content** of JSON object values.

**What They Represent:**
- JSON object content validation (required keys, property types, property constraints)
- Column entity type (`-C-`) handles column-level validation (presence, data type, nullability)
- Object entity type (`-O-`) handles JSON object structure validation

**Key Characteristics:**

1. **Naming Convention**: Object EntityIds end with "Object" suffix (e.g., `AllocatedMethodDetailsObject`, `ContractAppliedObject`)
2. **RMId Format**: Use `-O-` in EntityType position: `CAU-AllocatedMethodDetailsObject-O-001-M`
3. **Root Composite Pattern**: 
   - Nullable columns: Use `-O-000-C` with Condition checking column is not null
   - NOT NULL columns: Use `-O-000-M` with empty Condition `{}`
4. **Conditional Application**: Object rules only apply when an object value exists (when column is not null)

**Creating Object Rules:**

1. Create Column entity rules first for the column itself
2. Create Object root composite (`-O-000-C` or `-O-000-M`) that references all child Object rules
3. Create individual Object rules for each property requirement from the specification
4. Copy MustSatisfy text exactly from the specification
5. Match EntityId to column name (e.g., `AllocatedMethodDetails` → `AllocatedMethodDetailsObject`)

**File Organization:**

Object rules are stored in: `specification/requirements_model/releases/X.Y/model_rules/datasets/<dataset_id>/objects/`

#### Working with Schema Entity Types

Schema entity types define reusable JSON Schema documents used to validate JSON content through model checks.

**What They Represent:**
- Formal JSON Schema definitions (Draft 2020-12 or other supported drafts)
- Reusable schema artifacts that can be referenced by validation rules
- Structured validation logic decoupled from per-rule inline JSON path checks

**Key Characteristics:**

1. **Naming Convention**: Schema EntityIds use PascalCase and typically end with `Schema` (e.g., `AllocatedMethodDetailsObjectSchema`)
2. **RMId Format**: Use `-S-` in EntityType position: `CAU-AllocatedMethodDetailsObjectSchema-S-001-M`
3. **EntityType**: Must be `Schema`
4. **Schema Content**: `Schema` MUST contain a dereferenced JSON object in build output

**Creating Schema Entries:**

1. Add schema JSON files under `json_schemas/datasets/<dataset_id>/`
2. Add an entry in `json_schemas/json_schemas.json` with Dataset metadata and a `Schema` file reference
3. Use `file('relative/path.json')` paths relative to the version's `json_schemas/` folder
4. Validate with `./build_json.py --build-only` to confirm dereferencing into top-level `Schemas`

**File Organization:**

Schema entries are stored in: `specification/requirements_model/releases/X.Y/json_schemas/json_schemas.json`

Schema source files are stored in: `specification/requirements_model/releases/X.Y/json_schemas/datasets/<dataset_id>/`

### Stage 2

The second phase of conversion is to take the table created in Stage 1 and create the entries in the `specification/requirements_model` folder that adds the rules to the formal JSON structure.

#### Folder structure

Version-specific model content is organized under `specification/requirements_model/releases/X.Y/` where X.Y represents the model version (e.g., 1.2, 1.3). A `latest` symlink points to the most recent version.

**Version-specific structure** (`releases/X.Y/`):
- `model_details.json`: Metadata like versioning for this model version
- `applicability_criteria.json`: Feature flags controlling rule application
- `check_functions.json`: Logical validation functions and their arguments
- `model_datasets.json`: Maps datasets (e.g. FOCUS) to rule sets
- `json_schemas/json_schemas.json`: Registry of reusable JSON Schema entries for the version
- `json_schemas/datasets/<dataset_id>/`: JSON Schema source files referenced by `json_schemas.json`
- `model_rules/attributes/`: JSON files defining multiple `ModelRules` for a single attribute
- `model_rules/datasets/<dataset_id>/`: JSON files defining multiple `ModelRules` for a single dataset
- `model_rules/datasets/<dataset_id>/columns/`: JSON files defining multiple `ModelRules` for a single column
- `model_rules/datasets/<dataset_id>/objects/`: JSON files defining multiple `ModelRules` for properties within JSON object columns

**Build output** (top-level):
- `build/model-X.Y.json`: Built complete model JSON files for all versions

**Convenience paths:**
- `releases/latest/`: Symlink to the latest model version directory
- All work should be done in the appropriate version directory under `releases/X.Y/`

#### Steps

- Assign the Action Item (AI) to yourself to signal that you are working on the item (See: [GitHub Issues](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues))
- Open a branch with the source of git feature branch for your development work.
- Pull your branch to your development environment and perform all work specific to this AI in this branch.
- Navigate to the appropriate model version directory under `specification/requirements_model/releases/X.Y/` (or use the `latest` symlink for current development)
- Add a file into the relevant folder `model_rules/attributes/`, `model_rules/datasets/<dataset_id>/columns/`, or `model_rules/datasets/<dataset_id>/objects/` with name `entity-name.json` (example: availabilityzone.json)
- Write your rules into this file based on the rules in the Stage 1 table from the AI ticket (See: [ModelRule Templates](#modelrule-templates) for helpers)
- If you need reusable JSON Schema definitions, add source schema files under `json_schemas/datasets/<dataset_id>/` and register them in `json_schemas/json_schemas.json`
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
2. Assemble all version-specific JSON files from `releases/X.Y/` directories
3. Resolve `Schemas.*.Schema` file references into dereferenced JSON content
4. Generate complete `build/model-X.Y.json` files for each version
5. Validate the generated JSON against `model_schema.json`

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
- RMId format and uniqueness
- Dependency references exist and are valid
- Order field consistency in Dependencies arrays
- CheckFunction argument structure
- ApplicabilityCriteria key validity
- Cross-reference integrity between rules

**Troubleshooting build errors:**

- **JSON syntax errors**: Check for missing commas, brackets, or quotes in your rule files
- **Schema validation failures**: Ensure all required fields are present (Function, Reference, EntityType, etc.)
- **Schemas file reference failures**: Ensure `Schema` uses `file('...')` paths relative to `releases/X.Y/json_schemas/` and that the target file exists in that folder tree
- **Dependency errors**: Verify all ModelRuleIds in Dependencies arrays exist
- **RMId conflicts**: Ensure your RMId is unique within the dataset namespace

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

| RMId                     | Order Value |
|:-------------------------|:------------|
| CAU-SampleColumn-C-001-M | 10          |
| CAU-OtherRule-C-001-M    | 20          |
| CAU-AnotherRule-C-002-M  | 30          |

```json
{
  "CAU-SampleColumn-C-001-M": {
    "Order": 10,
    "ValidationCriteria": {
      "Dependencies": [
        "CAU-OtherRule-C-001-M",
        "CAU-AnotherRule-C-002-M"
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

### Schemas entry template

Use this template when registering a reusable JSON Schema in `json_schemas/json_schemas.json`.

```json
{
  "Schemas": {
    "CAU-SampleObjectSchema-S-001-M": {
      "EntityType": "Schema",
      "EntityName": "Sample Object Schema",
      "EntityId": "SampleObjectSchema",
      "DatasetType": "CAU",
      "DatasetId": "CostAndUsage",
      "DatasetName": "Cost and Usage",
      "Schema": "file('datasets/cost_and_usage/sampleobjectschema.json')"
    }
  }
}
```

Notes:
- The schema entry ID should follow the `DatasetType-EntityId-S-NNN-Level` pattern.
- `EntityType` must be `Schema`.
- The `Schema` path must be relative to `releases/X.Y/json_schemas/`.
- During build, `file('...')` is dereferenced and replaced with the JSON content in `build/model-X.Y.json`.

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
    "DatasetId": "SampleDataset",
    "DatasetName": "Sample Dataset",
    "Type": "Static",
    "Order": 0,
    "ValidationCriteria": {
      "MustSatisfy": "SampleColumn MUST meet all column requirements.",
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
      "Dependencies": [
        "CAU-SampleDataset-D-008-M",
        "CAU-SampleColumn-C-001-M",
        "CAU-SampleColumn-C-002-M",
        "CAU-SampleColumn-C-003-M"
      ]
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
      "MustSatisfy": "SampleColumn MUST be present in a FOCUS dataset",
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

Common rule for columns with an unconditional NOT NULL requirement.

```json
  "CAU-SampleColumn-C-002-M": {
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
    "Order": 20,
    "ValidationCriteria": {
      "MustSatisfy": "SampleColumn MUST NOT be null",
      "Keyword": "MUST NOT",
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
      "MustSatisfy": "SampleColumn MUST be one of the allowed values",
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
      "MustSatisfy": "SampleColumn MUST be of type Decimal",
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
      "MustSatisfy": "SampleColumn MUST conform to NumericFormat requirements",
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
      "MustSatisfy": "SampleColumn MUST be of type String",
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
      "MustSatisfy": "SampleColumn MUST conform to StringHandling requirements",
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
