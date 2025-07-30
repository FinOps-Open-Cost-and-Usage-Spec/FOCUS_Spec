# Conformance Requirements (CR)

Organizations developing technical specifications must adopt a structured, machine-readable approach to defining conformance. **Conformance Requirements (CR)** offer a standardized way to define, evaluate, and enforce specification requirements before formal testing.

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

| Segment         | Meaning                      |
|-----------------|------------------------------|
| `ArtifactName`  | Logical name (e.g. ListUnitPrice) |
| `ArtifactType`  | `C` (Column) or `A` (Attribute) |
| `NumericId`     | Sequence ID (e.g. 001)        |
| `ArtifactStatus`| `M`, `O`, or `C`              |

### Group Reference Formats

- `ArtifactName:FeatureType` — e.g. `ListUnitPrice:MCF`
- `GroupName:FeatureType` — e.g. `GRP-1:MCF`
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

To accommodate these changes without altering the core FOCUS Specification version, the `Version` field of an CR may differ slightly from the associated FOCUS Specification version. This allows us to make targeted corrections while preserving compatibility and traceability.

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
