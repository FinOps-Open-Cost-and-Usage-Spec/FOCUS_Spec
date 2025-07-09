# Static Conformance Requirements (SCR)

Organizations developing technical specifications must adopt a structured, machine-readable approach to defining conformance. **Static Conformance Requirements (SCR)** offer a standardized way to define, evaluate, and enforce specification requirements before formal testing.

This repository contains modular SCR components and a Python-based build process that assembles them into a validated `scr.json` file using a corresponding JSON Schema (`scr_schema.json`).

---

## 🎯 Purpose

The SCR format is designed to help specification authors:

- Clearly define mandatory and optional requirements
- Manage dependencies between conditions and validations
- Maintain backward compatibility across versions
- Support documentation generation and validation tooling
- Enable automated testing of provider datasets against the FOCUS specification

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

## 🧾 SCR Expression Format

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

| Keyword                | Default SCR Classification | Notes                                      |
|------------------------|----------------------------|--------------------------------------------|
| **MUST / SHALL**       | Mandatory (M)               | Typically maps to MCF or MAF               |
| **SHOULD / RECOMMENDED** | Optional (O)              | May be elevated to mandatory in some contexts |
| **MAY / OPTIONAL**     | Optional (O)                | Rarely becomes mandatory                   |

---

## 📁 File & Folder Structure

### 🔄 Input Files

- `scr_details.json`: Metadata like versioning
- `preconditions.json`: Feature flags controlling rule application
- `attributes.json`: Format attribute definitions (e.g. date/time, currency)
- `check_functions.json`: Logical validation functions and their arguments
- `conformance_tables.json`: Maps datasets (e.g. FOCUS) to rule sets
- `conformance_rules/`: JSON files defining multiple `ConformanceRules`

### 📤 Output

- `scr.json`: Final merged and validated JSON document

### 📏 Schema

- `scr_schema.json`: JSON Schema (Draft 7) for validating `scr.json`

### 🛠 Build Script

- `build_scr.py`: Python script that builds and validates the final SCR file

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install jsonschema
```

### 2. Build and Validate

```bash
python build_scr.py
```

This will:

- Merge all input files into `scr.json`
- Validate the result against `scr_schema.json`
- Print success or detailed validation errors

### 3. Output Example

```bash
✅ scr.json written
✅ scr.json is valid according to scr_schema.json
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
    "Function": "Define presence in dataset",
    "Reference": "ListUnitPrice",
    "CheckType": "Static",
    "PreConditions": ["PUBLIC_PRICE_LIST_SUPPORTED"],
    "ValidationCriteria": {
      "mustSatisfy": "...",
      "Check": {
        "CheckFunction": "ColumnPresent",
        "ColumnName": "ListUnitPrice"
      },
      "Condition": null
    }
  }
}
```

---

## ✅ Schema Validation Highlights

The schema enforces:

- Required keys like `SCRDetails`, `PreConditions`, `CheckFunction`, etc.
- Proper data types (e.g., arrays, strings, objects)
- Structured `ValidationCriteria` for consistent rule logic
