# FOCUS Specification Errata

This document outlines non-material corrections, clarifications, and typographical fixes for published versions of the FinOps Open Cost and Usage Specification (FOCUS). 

---

## Version 1.3

This section outlines minor discrepancies found in the 1.3 release of the FOCUS specification. These issues have been resolved within FOCUS enablement artifacts such as the Requirements Model and Validator, and FOCUS data generators should review these clarifications to ensure their implementations align with the working group's original intent.

All issues are considered clarifications to intended language and are not meant to represent material changes. The working group has implemented checks going forward that will prevent the introduction of similar issues. All issues were introduced in version 1.3 of the specification and have been addressed in version 1.4.

### A. Schema & Validation Logic Corrections
*The following corrections address schema definitions and validation rules to ensure automated tooling and JSON parsers function correctly.*

| Issue | Section / Location | Original | Corrected | PR Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#1: Missing property presence scope**<br><br>*(Incorrectly copied the presence requirement pattern for top-level columns instead of JSON properties)* | Section 3.1.31.1.3, lines [58](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L58), [74](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L74), [93](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L93), [108](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L108), and [123](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L123C1-L124C1) | `<<PropertyId>>` MUST be present **in a Cost and Usage FOCUS dataset** when... | `<<PropertyId>>` MUST be present **in an Elements object within ContractApplied** when... | TBD |
| **#2: Incorrect ContractCommitmentAppliedUnit type** | Section 3.1.31.2.4, line [184](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L184) | Declares `ContractCommitmentAppliedUnit` to be **float64** in the JSON Type Definition (JTD). | This should be **string**. | TBD |

### B. Terminology & Reference Corrections
*The following corrections standardize casing and fix broken column cross-references to prevent mapping errors.*

| Issue | Section / Location | Original | Corrected | PR Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#3: Inconsistent use of "ID" vs "Id"** | Section 3.1.31, various lines | **ContractID**, **ContractCommitmentID**, and **ResourceID** | **ContractId**, **ContractCommitmentId**, and **ResourceId** | TBD |
| **#4: Incorrect AllocatedTags reference** | Section 4.3.4, line [23](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/attributes/data_generator_calculated_split_cost_allocation_handling.md?plain=1#L23) | References column **AllocatedResourceTags** | References column **AllocatedTags**. | TBD |

### C. Typographical Errors
*The following corrections fix minor textual discrepancies that clarify the text but do not impact the intended technical implementation.*

| Issue | Section / Location | Original | Corrected | PR Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#5: Five vs four key-value pairs** | Section 3.1.31.1.2, line [36](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L36) | "Elements" objects MUST contain **four** key-value pairs... (`ContractId` excluded) | "Elements" objects MUST contain **five** key-value pairs... (`ContractId` included) | TBD |
| **#6: Property typo** | Section 3.1.31.1.2, line [46](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L46C8-L46C9) | ...unless it is a FOCUS-defined **allocation** property. | ...unless it is a FOCUS-defined **application** property. | TBD |