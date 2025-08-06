# Conformance Requirements (CR)

Conformance Requirements are structured, testable rules that define how each column in a dataset must behave in order to comply with the FOCUS specification. These rules are extracted from **verbose normative text** and translated into precise **logic statements** that can be programmatically validated. Each requirement includes elements such as _applicability conditions_, _expected behavior_, and _dependencies_ on other rules—enabling both human-readable documentation and automated conformance checking.

## Introduction

This document outlines a structured approach to converting verbose technical requirements from the FOCUS v1.2 specification into precise, programmatically testable conformance requirements. The goal is to enable consistent validation, documentation, and visualization of rules across all dataset columns using structured JSON representations.

The project is divided into three main stages, each with a defined scope and estimated effort:

### Stage 1 – Extract Conformance Requirements from FOCUS v1.2  
**Estimated Effort: 40% of total project time**

This foundational stage involves analyzing the **FOCUS v1.2** Technical Specification to extract **atomic** and **composite** conformance rules for each dataset column. These are captured in standardized Markdown tables that define logic, applicability, conditions, and dependencies.

The current output for **Stage 1** is **AI-assisted**, with over 85% of rules estimated to be valid. However, member review is critical, as the text of some requirements are complex to formalize in a prompt. The quality and accuracy of this stage directly impact the success of subsequent stages, especially JSON generation and dependency modeling.

### Stage 2 – Convert Extracted Rules into JSON Format  
**Estimated Effort: 35% of total project time**

This stage translates the structured conformance tables from **Stage 1** into a machine-readable JSON format. Each rule is converted into a defined JSON structure, validated against a shared schema. The conversion process can be largely automated by copying and adapting predefined JSON templates, which are repeated per column.

The JSON output enables programmatic validation and integration into testing workflows, making it a crucial bridge between human-readable requirements and conformance tooling.

### Stage 3 – Model Dependencies Between CRIDs  
**Estimated Effort: 25% of total project time**

This stage focuses on interpreting the `Requirement` field of each **CRID** to explicitly map dependencies to other **CRIDs** using logical structures such as `AND`, `OR`, and `NOT`. The output is used to construct a dependency graph for each column, enabling accurate validation of composite rules.

**Stage 3** can only be properly completed once both **Stage 1** and **Stage 2** are finalized, as it depends on having both accurate CRID identifiers and their JSON representations available for analysis.

These three stages form the foundation of the conformance modeling workflow. Once complete, additional outputs will be generated from the JSON representations, including:

- A standardized Markdown table of conformance requirements for each column
- A visual **DAG** _(Directed Acyclic Graph)_ diagram that maps CRID dependencies

This process enables reliable validation, clearer documentation, and easier integration with conformance tooling.

This repository contains modular CR components and a Python-based build process that assembles them into a validated `cr-<version>.json` file using a corresponding JSON Schema (`cr_schema.json`).

---

## 🎯 Purpose

The CR format is designed to help specification authors:

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

---

## 🧾 CR Expression Format

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

### Group Reference Formats

- `ArtifactName:FeatureType` — e.g. `ListUnitPrice:MCF`
- `FOCUS:FeatureType` — e.g. `FOCUS:OCF`

---

## 📐 RFC 2119 Keyword Mapping

| Keyword                | Default CR Classification | Notes                                      |
|------------------------|----------------------------|--------------------------------------------|
| **MUST / SHALL**       | Mandatory (M)               | Typically maps to MCF or MAF               |
| **SHOULD / RECOMMENDED** | Optional (O)              | May be elevated to mandatory in some contexts |
| **MAY / OPTIONAL**     | Optional (O)                | Rarely becomes mandatory                   |

---

## Versioning

In general, the version of each Conformance Requirement (CR) is aligned with the version of the FOCUS Specification to which it applies. However, there may be occasions where a correction or clarification is required due to an error or bug in a previously published CR definition.

To accommodate these changes without altering the core FOCUS Specification version, the `Version` field of a CR may differ slightly from the associated FOCUS Specification version. This allows us to make targeted corrections while preserving compatibility and traceability.

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
- An optional -Bugfix# suffix identifies a correction to the original CR version

Example:
If the CR originally aligned with FOCUS Specification version `1.2`, but a correction is later made, the updated CR version would be `1.2-Bugfix1`, a further correction would end up being `1.2-Bugfix2`

This approach ensures clear linkage to the original specification version while allowing for transparent and controlled updates to individual CR definitions.

## 📁 File & Folder Structure

### 🔄 Input Files

- `cr_details.json`: Metadata like versioning
- `applicability_criteria.json`: Feature flags controlling rule application
- `check_functions.json`: Logical validation functions and their arguments
- `conformance_datasets.json`: Maps datasets (e.g. FOCUS) to rule sets
- `conformance_rules/`: JSON files defining multiple `ConformanceRules`

### 📤 Output

- `cr-<version>.json`: Final merged and validated JSON document

### 📏 Schema

- `cr_schema.json`: JSON Schema (Draft 7) for validating `cr-<version>.json`

### 🛠 Build Script

- `build_cr_json.py`: Python script that builds and validates the final CR file

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install jsonschema
```

### 2. Build and Validate

```bash
python build_cr_json.py
```

This will:

- Merge all input files into `cr_json.json`
- Validate the result against `cr_schema.json`
- Print success or detailed validation errors

### 3. Output Example

```bash
✅ cr-<version>.json written
✅ cr-<version>.json is valid according to cr_schema.json
```

Or on error:

```bash
❌ Validation failed:
- [ConformanceRules.0.ListUnitPrice-C-004-C.ValidationCriteria.Check.Value] None is not of type 'string', 'number', 'boolean'
- [CheckFunction.ColumnByColumnEqualsColumnValue.Arguments.2] 'ResultColumnName' is a required property
```

---

## 📘 Conformance Rule Format

Each JSON file in `conformance_rules/` contains one or more rules structured as:

```json
{
  "ListUnitPrice-C-001-C": {
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
}
```

---

## ✅ Schema Validation Highlights

The schema enforces:

- Required keys like `Details`, `ApplicabilityCriteria`, `CheckFunction`, etc.
- Proper data types (e.g., arrays, strings, objects)
- Structured `ValidationCriteria` for consistent rule logic
