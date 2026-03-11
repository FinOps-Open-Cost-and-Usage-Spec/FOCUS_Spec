# FOCUS Specification Errata

This document outlines non-material corrections, clarifications, and typographical fixes for published versions of the FinOps Open Cost and Usage Specification (FOCUS). 

These updates serve as the basis for revising FOCUS enablement artifacts, such as the Requirements Model, to ensure they remain accurate. FOCUS data generators should review these clarifications to ensure their implementations align with the working group's original intent.

---

## Version 1.3

This section outlines minor discrepancies found in the 1.3 release of the FOCUS specification. 

All issues are considered clarifications to intended language and are not meant to represent material changes. The working group has implemented checks going forward that will prevent the introduction of similar issues. All issues were introduced in version 1.3 of the specification and have been addressed in version 1.4.

### A. Schema & Validation Logic Corrections
*The following corrections address schema definitions and validation rules to ensure automated tooling and JSON parsers function correctly.*

| Issue | Section / Location | Original | Corrected | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#1: Missing property presence scope**<br><br>*(Incorrectly copied the presence requirement pattern for top-level columns instead of JSON properties)* | Section 3.1.31.1.3, lines [58](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L58), [74](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L74), [93](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L93), [108](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L108), and [123](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L123C1-L124C1) | `<<PropertyId>>` MUST be present **in a Cost and Usage FOCUS dataset** when... | `<<PropertyId>>` MUST be present **in an Elements object within ContractApplied** when... | Issue: [#2048](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2048)<br>PR: [#2052](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2052) |
| **#2: Incorrect ContractCommitmentAppliedUnit type** | Section 3.1.31.2.4, line [184](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L184) | Declares `ContractCommitmentAppliedUnit` to be **float64** in the JSON Type Definition (JTD). | This should be **string**. | Issue: [#2048](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2048)<br>PR: [#2052](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2052) |

### B. Terminology & Reference Corrections
*The following corrections standardize casing and fix broken column cross-references to prevent mapping errors.*

| Issue | Section / Location | Original | Corrected | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#3: Inconsistent use of "ID" vs "Id"** | Section 3.1.31, various lines (e.g., [74](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L74)) | **ContractID**, **ContractCommitmentID**, and **ResourceID** | **ContractId**, **ContractCommitmentId**, and **ResourceId** | Issue: [#2048](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2048)<br>PR: [#2052](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2052) |
| **#4: Incorrect AllocatedTags reference** | Section 4.3.4, line [23](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/attributes/data_generator_calculated_split_cost_allocation_handling.md?plain=1#L23) | References column **AllocatedResourceTags** | References column **AllocatedTags**. | Issue: [#2048](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2048)<br>PR: [#2052](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2052) |

### C. Typographical Errors
*The following corrections fix minor textual discrepancies that clarify the text but do not impact the intended technical implementation.*

| Issue | Section / Location | Original | Corrected | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#5: Five vs four key-value pairs** | Section 3.1.31.1.2, line [36](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L36) | "Elements" objects MUST contain **four** key-value pairs... (`ContractId` excluded) | "Elements" objects MUST contain **five** key-value pairs... (`ContractId` included) | Issue: [#2048](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2048)<br>PR: [#2052](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2052) |
| **#6: Property typo** | Section 3.1.31.1.2, line [46](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L46C8-L46C9) | ...unless it is a FOCUS-defined **allocation** property. | ...unless it is a FOCUS-defined **application** property. | Issue: [#2048](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2048)<br>PR: [#2052](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2052) |

### D. Requirements Model Corrections
*The following corrections address bugs found strictly within the FOCUS Requirements Model (the JSON validation rules). In these instances, the underlying specification text is correct, but the programmatic model contained implementation errors.*

| Issue | File | Original | Corrected | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#7: Missing Ignored Key** | `contractappliedobject.json` | The `IgnoreKeys` array omitted `"ContractId"`, causing valid custom key checks to fail. | `"ContractId"` was added to the `IgnoreKeys` array. | Issue: [#2048](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2048)<br>PR: [#2052](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2052) |
| **#8: Incorrect JSON Path targets** | `contractappliedobject.json` | The `Path` targeted `"$.Elements[*].ContractCommitmentId"` for all three metric presence checks. | The `Path` was corrected to target the respective `Cost`, `Quantity`, and `Unit` JSON properties. | Issue: [#2048](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2048)<br>PR: [#2052](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2052) |

---

## Version 1.2

This section outlines discrepancies found in the enablement artifacts (Requirements Model) for the 1.2 release of the FOCUS specification. The underlying specification text for version 1.2 remains accurate and unchanged.

### A. Schema & Validation Logic Corrections
*No errata reported for this release.*

### B. Terminology & Reference Corrections
*No errata reported for this release.*

### C. Typographical Errors
*No errata reported for this release.*

### D. Requirements Model Corrections
*The following corrections address bugs found strictly within the FOCUS 1.2 Requirements Model validation rules.*

| Issue | File | Original | Corrected | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#1: Incorrect argument name** | `resourcetype.json` | The condition function incorrectly used the argument `"CheckCondition": "ResourceId"`. | The argument was corrected to the standard `"ColumnName": "ResourceId"`. | Issue: [#1824](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/1824)<br>PR: [#1956](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/1956) |
| **#2: Incorrect nullability function** | `commitmentdiscountstatus.json` | The requirement used `CheckNotValue` to ensure the status was null, which caused valid nulls to fail. | The function was corrected to `CheckValue` to properly enforce the `MUST be null` requirement. | Issue: [#1825](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/1825)<br>PR: [#1956](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/1956) |
