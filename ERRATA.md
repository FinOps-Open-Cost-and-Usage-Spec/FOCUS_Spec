# FOCUS Specification Errata

This document outlines non-material corrections, clarifications, and typographical fixes for published versions of the FinOps Open Cost and Usage Specification (FOCUS). 

These updates serve as the basis for revising FOCUS enablement artifacts, such as the Requirements Model, to ensure they remain accurate. FOCUS data generators should review these clarifications to ensure their implementations align with the working group's original intent.

---

## Version 1.5

This section outlines minor discrepancies found in the 1.5 release of the FOCUS specification and its Requirements Model.

All issues are considered clarifications to intended language and are not meant to represent material changes.

### A. Schema & Validation Logic Corrections
*The following corrections align requirement lines with the rest of their definitions.*

| Issue | Section / Location | Original | Corrected | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#1: Missing Currency Format requirement for PaymentCurrency** | `datasets/invoice_detail/columns/paymentcurrency.md`, line [9](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/datasets/invoice_detail/columns/paymentcurrency.md?plain=1#L9) | No Currency Format requirement follows the StringHandling requirement. | PaymentCurrency MUST conform to CurrencyFormat requirements. (Matches BillingCurrency and the Content Constraints table.) | Issue: [#2837](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2837) |
| **#2: Redundant ContractId not-null condition** | `datasets/contract_commitment/columns/contractid.md`, lines [12](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/datasets/contract_commitment/columns/contractid.md?plain=1#L12), [13](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/datasets/contract_commitment/columns/contractid.md?plain=1#L13) and [14](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/datasets/contract_commitment/columns/contractid.md?plain=1#L14) | When ContractId is not null, ContractId MUST adhere to the following requirements: (with two nested bullets) | The condition line is removed and its two nested bullets move up one level. ContractId MUST NOT be null (line 11), so the condition was always met. | Issue: [#2837](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2837) |
| **#3: Lowercase "must" in TimeSectorEnd requirement** | `metadata/recency/time_sectors/time_sector_end.md`, line [11](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/metadata/recency/time_sectors/time_sector_end.md?plain=1#L11) | TimeSectorEnd **must** be exclusive of the end time of the subsequent time sector. | TimeSectorEnd **MUST** be exclusive of the end time of the subsequent time sector. | Issue: [#2837](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2837) |

### B. Terminology & Reference Corrections
*The following corrections standardize casing, names, and link targets.*

| Issue | Section / Location | Original | Corrected | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#4: Inconsistent use of "ID" vs "Id" in SchemaId** | `metadata/schema/schema_id.md`, line [9](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/metadata/schema/schema_id.md?plain=1#L9) | **SchemaID** MUST NOT be null. | **SchemaId** MUST NOT be null. | Issue: [#2836](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2836) |
| **#5: Inconsistent use of "ID" vs "Id" in DatasetInstanceId** | `metadata/schema/dataset_instance_id.md`, lines [8](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/metadata/schema/dataset_instance_id.md?plain=1#L8), [9](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/metadata/schema/dataset_instance_id.md?plain=1#L9) and [10](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/metadata/schema/dataset_instance_id.md?plain=1#L10) | **DatasetInstanceID** (three times) | **DatasetInstanceId** | Issue: [#2836](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2836) |
| **#6: Incorrect InvoiceId link target** | `datasets/cost_and_usage/columns/invoicedetailid.md`, line [15](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/datasets/cost_and_usage/columns/invoicedetailid.md?plain=1#L15) | ...within a given InvoiceId, linked to `#datamodel.invoicedetail.invoiceid`. | ...within a given InvoiceId, linked to `#datamodel.costandusage.invoiceid`. | Issue: [#2836](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2836) |
| **#7: AllocationMethod used as a column name** | `datasets/cost_and_usage/columns/allocatedmethoddetails.md`, line [35](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/datasets/cost_and_usage/columns/allocatedmethoddetails.md?plain=1#L35) | ...data generator's documented **AllocationMethod** which... | ...data generator's documented **allocation method** which... (link target unchanged) | Issue: [#2836](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2836) |
| **#8: Inconsistent operating model condition name** | `operating_model_conditions/includespricingbillingcurrencydifferences.md`, line [1](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/operating_model_conditions/includespricingbillingcurrencydifferences.md?plain=1#L1) | Includes **Pricing-Billing** Currency Differences | Includes **Pricing and Billing** Currency Differences (matches Includes Billing and Payment Currency Differences) | Issue: [#2836](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2836) |

### C. Typographical Errors
*The following corrections fix minor textual discrepancies that do not impact the intended technical implementation.*

| Issue | Section / Location | Original | Corrected | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#9: "MUST not" in TimeSectorComplete requirement** | `metadata/recency/time_sectors/time_sector_complete.md`, line [9](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/metadata/recency/time_sectors/time_sector_complete.md?plain=1#L9) | TimeSectorComplete MUST **not** be null. | TimeSectorComplete MUST **NOT** be null. | Issue: [#2836](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2836) |
| **#10: "MUST not" in PreviousColumnName requirement** | `metadata/schema/column_definition/previouscolumnname.md`, line [10](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/metadata/schema/column_definition/previouscolumnname.md?plain=1#L10) | PreviousColumnName MUST **not** be null. | PreviousColumnName MUST **NOT** be null. | Issue: [#2836](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2836) |
| **#11: "NULL" in HostProviderName requirements** | `datasets/cost_and_usage/columns/hostprovidername.md`, lines [14](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/datasets/cost_and_usage/columns/hostprovidername.md?plain=1#L14) and [15](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/datasets/cost_and_usage/columns/hostprovidername.md?plain=1#L15) | HostProviderName MAY be **NULL** when... | HostProviderName MAY be **null** when... | Issue: [#2836](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2836) |
| **#12: Duplicate requirement in Time Sector End description** | `metadata/recency/time_sectors/time_sector_end.md`, line [3](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/e9cdcc7cbb9bfec2f6d6f6b6a8d872bc0b6b9cc0/specification/metadata/recency/time_sectors/time_sector_end.md?plain=1#L3) | The Time Sector End **MUST be** later than the Time Sector Start. | The Time Sector End **is** later than the Time Sector Start. (Line 12 states the requirement.) | Issue: [#2836](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2836) |

### D. Requirements Model Corrections
*The following corrections address the FOCUS 1.5 Requirements Model validation rules.*

| Issue | File | Original | Corrected | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#13: Missing PaymentCurrency Currency Format check** | `paymentcurrency.json` | The Invoice Detail PaymentCurrency rules have no Currency Format check. | A Currency Format rule is added, matching the BillingCurrency rules. (Follows erratum #1.) | Issue: [#2837](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2837) |
| **#14: ContractId not-null composite** | `contractid.json` | `CCT-ContractId-C-004-C` models the "When ContractId is not null" condition removed by erratum #2. | The rule matches the corrected requirement text. (Follows erratum #2.) | Issue: [#2837](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2837) |
| **#15: Allowed-values rules fail on null<br><br>*(Defect also present in the 1.2 to 1.4 Requirements Models)*** | `commitmentdiscountstatus.json`, `commitmentdiscountcategory.json` | `CAU-CommitmentDiscountStatus-C-005-M` and `CAU-CommitmentDiscountCategory-C-005-M` have an empty `Condition`, so a null value fails the allowed-values check, contradicting each column's `C-003-C` (MUST be null when CommitmentDiscountId is null). | Each rule gets a `CheckNotValue` condition on its own column with `"Value": null`, matching the sibling `CapacityReservationStatus` and `PricingCategory` rules. | Issue: [#2783](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2783) |

---

## Version 1.4

This section outlines discrepancies found in the enablement artifacts (Requirements Model) for the 1.4 release of the FOCUS specification. The underlying specification text for version 1.4 remains accurate and unchanged.

### A. Schema & Validation Logic Corrections
*No errata reported for this release.*

### B. Terminology & Reference Corrections
*No errata reported for this release.*

### C. Typographical Errors
*No errata reported for this release.*

### D. Requirements Model Corrections
*The following corrections address bugs found strictly within the FOCUS 1.4 Requirements Model validation rules.*

| Issue | File | Original | Corrected | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#1: Circular rule dependency**<br><br>*(Defect also present in the 1.2 and 1.3 Requirements Models)* | `commitmentdiscountunit.json` | `CAU-CommitmentDiscountUnit-C-005-C` and `CAU-CommitmentDiscountUnit-C-006-C` declared a dependency on the composite rule `CAU-CommitmentDiscountQuantity-C-000-C`, which itself resolved back through the `CommitmentDiscountUnit` rules and closed a dependency cycle. Neither rule referenced `CAU-CommitmentDiscountQuantity-C-000-C` in its logic, which is a `CheckValue` on the column only. | The dependency was narrowed to `CAU-CommitmentDiscountQuantity-C-003-C`, the nullability requirement the two rules actually rely on, breaking the cycle. | Issue: [#2536](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2536)<br>PR: [#2609](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2609) |

---

## Version 1.3

This section outlines minor discrepancies found in the 1.3 release of the FOCUS specification. 

All issues are considered clarifications to intended language and are not meant to represent material changes. The working group has implemented checks going forward that will prevent the introduction of similar issues. These issues have been addressed in version 1.4.

### A. Schema & Validation Logic Corrections
*The following corrections address schema definitions and validation rules to ensure automated tooling and JSON parsers function correctly.*

| Issue | Section / Location | Original | Corrected | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **#1: Missing property presence scope**<br><br>*(Incorrectly copied the presence requirement pattern for top-level columns instead of JSON properties)* | Section 3.1.31.1.3, lines [58](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L58), [74](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L74), [93](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L93), [108](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L108), and [123](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L123C1-L124C1) | `<<PropertyId>>` MUST be present **in a Cost and Usage FOCUS dataset** when... | `<<PropertyId>>` MUST be present **in an Elements object within ContractApplied** when... | Issue: [#2048](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2048)<br>PR: [#2052](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2052) |
| **#2: Incorrect ContractCommitmentAppliedUnit type** | Section 3.1.31.2.4, line [184](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/contractapplied.md?plain=1#L184) | Declares `ContractCommitmentAppliedUnit` to be **float64** in the JSON Type Definition (JTD). | This should be **string**. | Issue: [#2048](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2048)<br>PR: [#2052](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2052) |
| **#9: Incorrect "Allows nulls" for PricingCurrency** | Section 3.1.41.5, line [33](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/pricingcurrency.md?plain=1#L33) | Content Constraints declares PricingCurrency to allow nulls. | PricingCurrency does not allow nulls, per normative requirement. | Issue: [#2079](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2079)<br>PR: [#2052](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2052) |
| **#10: Incorrect "Allows nulls" for PricingCurrencyEffectiveCost** | Section 3.1.43.5, line [38](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/c67b95bd40e6fb43a57f74a53a615c4d6d3c118f/specification/datasets/cost_and_usage/columns/pricingcurrencyeffectivecost.md?plain=1#L38) | Content Constraints declares PricingCurrencyEffectiveCost to allow nulls. | PricingCurrencyEffectiveCost does not allow nulls, per normative requirement. | Issue: [#2079](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2079)<br>PR: [#2052](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2052) |

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
| **#11: Incorrect CommitmentDiscountStatus allowed values**<br><br>*(Defect carried over from the 1.2 Requirements Model)* | `commitmentdiscountstatus.json` | `CAU-CommitmentDiscountStatus-C-005-M` listed the allowed values as `Active`, `Expired`, and `Pending`, none of which appear in the specification. | Corrected to the spec-defined values `Used` and `Unused` (matching the column's Allowed Values table and the sibling `CapacityReservationStatus` rule). | Issue: [#2418](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2418)<br>PR: [#2422](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2422) |
| **#12: Over-broad rule dependency**<br><br>*(Defect carried over from the 1.2 Requirements Model)* | `commitmentdiscountunit.json` | `CAU-CommitmentDiscountUnit-C-005-C` and `CAU-CommitmentDiscountUnit-C-006-C` declared a dependency on `CAU-CommitmentDiscountQuantity-C-000-C`, the composite covering every `CommitmentDiscountQuantity` requirement. Both rules condition only on whether `CommitmentDiscountQuantity` is null, so the declared dependency was broader than the logic required. This model contains no dependency cycle. | The dependency was narrowed to `CAU-CommitmentDiscountQuantity-C-003-C`, the nullability composite the two rules actually rely on. | Issue: [#2536](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2536)<br>PR: [#2609](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2609) |
| **#13: Malformed condition on CapacityReservationStatus nullability**<br><br>*(Defect carried over from the 1.2 Requirements Model)* | `capacityreservationstatus.json` | The `Condition` on `CAU-CapacityReservationStatus-C-003-C` wrapped its single `CheckValue` clause in an `"AND"` key, and the `Condition` on `CAU-CapacityReservationStatus-C-004-C` used `{"AND": [...]}`. Neither form matches the `{"CheckFunction": "AND", "Items": [...]}` shape the model defines, so both conditions parsed as absent and the rules fired on every row. | `CAU-CapacityReservationStatus-C-003-C` now carries the bare `CheckValue` clause, and `CAU-CapacityReservationStatus-C-004-C` uses the standard `CheckFunction`/`Items` composite form. | Issue: [#2369](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2369)<br>PR: [#2622](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2622) |
| **#14: Inverted CommitmentDiscountStatus null requirement** | `commitmentdiscountstatus.json` | `CAU-CommitmentDiscountStatus-C-003-C` used `CheckNotValue` with `"Value": null`, which asserts the opposite of its stated requirement that `CommitmentDiscountStatus` MUST be null when `CommitmentDiscountId` is null. Rows the rule treats as valid raised a violation. | The function was corrected to `CheckValue`, matching the equivalent 1.2 correction and the 1.4 model. | Issue: [#2369](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2369)<br>PR: [#2622](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2622) |
| **#15: Inverted and incomplete CommitmentDiscountStatus condition**<br><br>*(Defect carried over from the 1.2 Requirements Model)* | `commitmentdiscountstatus.json` | The `Condition` on `CAU-CommitmentDiscountStatus-C-004-C` used `CheckValue` with `"Value": null`, firing the rule when `CommitmentDiscountId` is null rather than when it is not null, and omitted the `ChargeCategory` is `"Usage"` clause present in the stated requirement. | The condition was replaced with a `{"CheckFunction": "AND", "Items": [...]}` composite combining `CheckNotValue` on `CommitmentDiscountId` and `CheckValue` of `"Usage"` on `ChargeCategory`. | Issue: [#2369](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2369)<br>PR: [#2622](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2622) |

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
| **#3: Incorrect CommitmentDiscountStatus allowed values** | `commitmentdiscountstatus.json` | `CommitmentDiscountStatus-C-005-M` listed the allowed values as `Active`, `Expired`, and `Pending`, none of which appear in the specification. | Corrected to the spec-defined values `Used` and `Unused` (matching the column's Allowed Values table and the sibling `CapacityReservationStatus` rule). | Issue: [#2418](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2418)<br>PR: [#2422](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2422) |
| **#4: Over-broad rule dependency** | `commitmentdiscountunit.json` | `CommitmentDiscountUnit-C-005-C` and `CommitmentDiscountUnit-C-006-C` declared a dependency on `CommitmentDiscountQuantity-C-000-C`, the composite covering every `CommitmentDiscountQuantity` requirement. Both rules condition only on whether `CommitmentDiscountQuantity` is null, so the declared dependency was broader than the logic required. This model contains no dependency cycle. | The dependency was narrowed to `CommitmentDiscountQuantity-C-003-C`, the nullability composite the two rules actually rely on. | Issue: [#2536](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2536)<br>PR: [#2609](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2609) |
| **#5: Malformed condition on CapacityReservationStatus nullability** | `capacityreservationstatus.json` | The `Condition` on `CapacityReservationStatus-C-003-C` wrapped its single `CheckValue` clause in an `"AND"` key, and the `Condition` on `CapacityReservationStatus-C-004-C` used `{"AND": [...]}`. Neither form matches the `{"CheckFunction": "AND", "Items": [...]}` shape the model defines, so both conditions parsed as absent and the rules fired on every row. | `CapacityReservationStatus-C-003-C` now carries the bare `CheckValue` clause, and `CapacityReservationStatus-C-004-C` uses the standard `CheckFunction`/`Items` composite form. | Issue: [#2369](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2369)<br>PR: [#2622](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2622) |
| **#6: Inverted and incomplete CommitmentDiscountStatus condition** | `commitmentdiscountstatus.json` | The `Condition` on `CommitmentDiscountStatus-C-004-C` used `CheckValue` with `"Value": null`, firing the rule when `CommitmentDiscountId` is null rather than when it is not null, and omitted the `ChargeCategory` is `"Usage"` clause present in the stated requirement. | The condition was replaced with a `{"CheckFunction": "AND", "Items": [...]}` composite combining `CheckNotValue` on `CommitmentDiscountId` and `CheckValue` of `"Usage"` on `ChargeCategory`. | Issue: [#2369](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2369)<br>PR: [#2622](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2622) |
