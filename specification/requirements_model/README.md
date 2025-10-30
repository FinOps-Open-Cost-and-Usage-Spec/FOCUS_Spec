# FOCUS Requirements Model (RM)

The FOCUS Requirements Model is a structured, testable set of rules that define how each column in a dataset must behave in order to comply with the FOCUS specification. These rules are extracted from **verbose normative text** in the FOCUS specification and translated into precise **logic statements** that can be programmatically validated. Each requirement includes elements such as _applicability conditions_, _expected behavior_, and _dependencies_ on other rules—enabling both human-readable documentation and automated conformance checking.

## Introduction

This document outlines a structured approach to converting verbose technical requirements from the FOCUS v1.2 specification into precise, programmatically testable rules. The goal is to enable consistent validation, documentation, and visualization of rules across all dataset columns using structured JSON representations.

The project is divided into three main stages, each with a defined scope and estimated effort:

### Stage 1 – Extract Normative Requirements from FOCUS v1.2  

**Estimated Effort: 40% of total project time**

This foundational stage involves analyzing the **FOCUS v1.2** Technical Specification to extract **atomic** and **composite**  normative requirements for each attribute and dataset column. These requirements are now captured in a **structured JSON format** that define logic, applicability, conditions, and dependencies.

The current output for **Stage 1** is **AI-assisted**, with over 85% of rules estimated to be valid. However, member review is critical, as the text of some requirements are complex to formalize in a prompt. The quality and accuracy of this stage directly impact the success of subsequent stages, especially JSON generation and dependency modeling.

### Stage 2 – Convert Extracted Rules into JSON Format  

**Estimated Effort: 35% of total project time**

This stage focuses on refining and validating the **JSON structures** generated in **Stage 1**. Each rule is reviewed, updated, and validated against a shared schema. The refinement process can be largely automated by copying and adapting predefined JSON templates, which are repeated per column.

The validated JSON output enables programmatic testing, integration into tooling, and long-term maintainability, making it a crucial bridge between human-readable requirements and automated validation workflows.

### Stage 3 – Model Dependencies Between ModelIds  

**Estimated Effort: 25% of total project time**

This stage focuses on interpreting the `Requirement` field of each **RuleId** to explicitly map dependencies to other **ModelIds** using logical structures such as `AND`, `OR`, and `NOT`. The output is used to construct a dependency graph for each column, enabling accurate validation of composite rules.

**Stage 3** can only be properly completed once both **Stage 1** and **Stage 2** are finalized, as it depends on having both accurate ModelId identifiers and their JSON representations available for analysis.

These three stages form the foundation of the modeling workflow. Once complete, additional outputs will be generated from the JSON representations, including:

- A standardized Markdown table of normative requirements for each column
- A visual **DAG** _(Directed Acyclic Graph)_ diagram that maps ModelId dependencies

This process enables reliable validation, clearer documentation, and easier integration with tooling.

This repository contains modular model components and a Python-based build process that assembles them into a validated `model-<version>.json` file using a corresponding JSON Schema (`model_schema.json`).

---

## 🎯 Purpose

The model format is designed to help specification authors:

- Clearly define mandatory and optional requirements
- Manage dependencies between conditions and validations
- Maintain backward compatibility across versions
- Support documentation generation and validation tooling
- Enable automated testing of data generator datasets against the FOCUS specification

---

## 🔤 Feature Classifications

| Classification | Definition | Notes |
|----------------|------------|-------|
| **Mandatory (M)** | Required for interoperability and conformance | MUST be implemented |
| **Optional (O)** | Enhances functionality | MAY be implemented |
| **Conditional (C)** | Required only if certain conditions are met (e.g. implementation choices, external dependencies, regulations) | MAY unless the condition is met — then MUST |

---

## 📘 Artifact Types

In FOCUS, artifacts refer to either **columns** or **attributes**:

- **Column** — Structural data elements in the FOCUS schema  
  _e.g._: `ListUnitPrice-C-001-M`
- **Attribute** — Semantic labels or metadata affecting formatting, interpretation, or contract-based logic  
  _e.g._: `DateTimeFormat-A-001-M`
- **Dataset** - Requirement affecting the dataset as a whole.
  _e.g._: `BilledCost-D-001-M`
- **Other** - There is a possibility we may define other entities such as e.g. `Provider`

---

## 🧩 Feature Types & Grouping

| Code  | Name                         | Description         |
|-------|------------------------------|---------------------|
| **MCF** | Mandatory Column Features     | Required columns     |
| **OCF** | Optional Column Features      | Optional columns     |
| **MAF** | Mandatory Attribute Features  | Required attributes  |
| **OAF** | Optional Attribute Features   | Optional attributes  |

**Usage Examples:**

- `ListUnitPrice:MCF` → All mandatory column features for `ListUnitPrice`
- `FOCUS:MCF` → All mandatory column features across the entire specification

### Group Reference Formats

- `ArtifactName:FeatureType` — e.g. `ListUnitPrice:MCF`
- `FOCUS:FeatureType` — e.g. `FOCUS:OCF`

---

## 🧾 Model Expression Format

### Full Rule Identifier Format

```text
<ArtifactName>-<ArtifactType>-<NumericId>-<ArtifactStatus>
```

**Example:** `ListUnitPrice-C-001-M`

| Segment         | Meaning                                      |
|-----------------|----------------------------------------------|
| `ArtifactName`  | ColumnID (e.g. ListUnitPrice)                |
| `ArtifactType`  | `C` (Column), `A` (Attribute), `D` (Dataset) |
| `NumericId`     | Sequence ID (e.g. 001)                       |
| `ArtifactStatus`| `M`, `O`, or `C`                             |

---

## 📐 RFC 2119 Keyword Mapping

| Keyword                | Default Model Classification | Notes                                      |
|------------------------|----------------------------|--------------------------------------------|
| **MUST / SHALL**       | Mandatory (M)               | Typically maps to MCF or MAF               |
| **SHOULD / RECOMMENDED** | Optional (O)              | May be elevated to mandatory in some contexts |
| **MAY / OPTIONAL**     | Optional (O)                | Rarely becomes mandatory                   |

---

## Versioning

In general, the version of each FOCUS Requirement Model (RM) is aligned with the version of the FOCUS Specification to which it applies. However, there may be occasions where a correction or clarification is required due to an error or bug in a previously published model definition.

To accommodate these changes without altering the core FOCUS Specification version, the `Version` field of a FOCUS Requirements Model may differ slightly from the associated FOCUS Specification version. This allows us to make targeted corrections while preserving compatibility and traceability.

Versioning Format:

The version string is defined using the following ABNF:

```ini
version        = spec-version [ "-" "Bugfix" bugfix-num ]
spec-version   = major "." minor
major          = 1*DIGIT
minor          = 2*DIGIT / 1*DIGIT
bugfix-num     = 1*DIGIT
```

- major and minor represent the FOCUS Specification version (e.g., 1.2, 1.13, 2.01)
- An optional -Bugfix# suffix identifies a correction to the original model version

Example:
If the model originally aligned with FOCUS Specification version `1.2`, but a correction is later made, the updated model version would be `1.2-Bugfix1`, a further correction would end up being `1.2-Bugfix2`

This approach ensures clear linkage to the original specification version while allowing for transparent and controlled updates to individual model definitions.

## 📁 File & Folder Structure

### 🔄 Input Files

- `model_details.json`: Metadata like versioning
- `applicability_criteria.json`: Feature flags controlling rule application
- `check_functions.json`: Logical validation functions and their arguments
- `model_datasets.json`: Maps datasets (e.g. FOCUS) to rule sets
- `model_rules/`: JSON files defining multiple `ModelRules`

### 📤 Output

- `model-<version>.json`: Final merged and validated JSON document

### 📏 Schema

- `model_schema.json`: JSON Schema (Draft 7) for validating `model-<version>.json`

### 🛠 Build Script

- `build_model_json.py`: Python script that builds and validates the final model file

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install jsonschema
```

### 2. Build and Validate

```bash
python build_model_json.py
```

This will:

- Merge all input files into `model_json.json`
- Validate the result against `model_schema.json`
- Print success or detailed validation errors

### 3. Output Example

```bash
✅ model-<version>.json written
✅ model-<version>.json is valid according to model_schema.json
```

Or on error:

```bash
❌ Validation failed:
- [ModelRules.0.ListUnitPrice-C-004-C.ValidationCriteria.Check.Value] None is not of type 'string', 'number', 'boolean'
- [CheckFunction.ColumnByColumnEqualsColumnValue.Arguments.2] 'ResultColumnName' is a required property
```

---

## 📘  Model Rule  Format

Each JSON file in `model_rules/` contains one or more rules structured as:

```json
{
  "ListUnitPrice-C-001-C": {
    "Function": "Validation",
    "Reference": "SampleColumn",
    "EntityType": "Column",
    "Notes": "",
    "ModelVersionIntroduced": "1.2",
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
}
```

---

## ✅ Schema Validation Highlights

The schema enforces:

- Required keys like `Details`, `ApplicabilityCriteria`, `CheckFunction`, etc.
- Proper data types (e.g., arrays, strings, objects)
- Structured `ValidationCriteria` for consistent rule logic
