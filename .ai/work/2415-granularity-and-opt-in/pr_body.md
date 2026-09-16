## Summary

This PR extends the Dataset Configuration attribute with scoped detail configuration for FOCUS 1.5.

Data generators can make optional, higher-cardinality detail available for documented areas of a FOCUS dataset. Practitioners can select the detail needed for those areas without FOCUS defining a request payload, property name, or transport mechanism. A provider can expose the selection through an API parameter, export setting, query interface, or another access mechanism.

The glossary gains four entries: Companion Artifact, Detail Representation, Detail Scope, and Detail Variant. A detail scope is a subset of records, identified by values of FOCUS columns representing dimensions (e.g., ServiceName, ResourceType), for which more than one detail variant is offered. The records delivered when no additional detail is selected count as a detail variant.

The normative requirements establish:

* When a detail scope is offered, a FOCUS dataset is configurable to select each offered detail variant and includes only one detail variant for each detail scope.
* The columns documented for a selected detail variant are included regardless of the user-defined column selection, and the column-selection requirement carries a matching exception for those columns.
* A FOCUS dataset is configurable to select one detail representation when more than one is offered for a selected detail variant. Whether that selection applies to the complete dataset or to each detail scope is left to the data generator.
* Detail scope documentation includes the column values that identify each detail scope, the offered detail variants and the columns each populates (FOCUS or custom), and whether each variant uses Data Generator-Calculated Split Cost Allocation Handling.
* Detail scope documentation includes the offered detail representations, their relationship to other records representing the same data, and the columns that relate companion artifact records to dataset artifact records. The documentation is accessible to practitioners.
* The sum of each summable metric column for the records in a detail scope is preserved across all offered detail variants, so variants of the same scope reconcile to the same totals.
* Records with identical values in all delivered columns other than summable metrics, including custom columns, should be represented as a single record while preserving the aggregate value of each summable metric column.

The supporting content describes illustrative detail representations:

* Inline: additional populated columns on the same records
* Expanded: more detailed records replace the less detailed records in the same dataset artifact
* Companion artifact: detail delivered in a separate file or table whose structure FOCUS does not define

It also explains that Data Generator-Calculated Split Cost Allocation Handling is a defined subset of scoped detail configuration, and that record-minimization guidance does not replace column-specific aggregation guidance, including the guidance for `PricingQuantity`, `ListCost`, and `ContractedCost`.

### Open Questions for TF-2

* **Term names.** This PR uses detail variant and detail representation, as @ijurica proposed, in place of detail level and delivery method. "Level" implies an ordinal scale and collides with "Feature level" in Content Constraints tables. "Delivery method" sits next to DeliveryHandling's delivery mechanism. The Replacement representation is renamed Expanded because Replacement is a CorrectionHandling correction style. Data coverage is folded into the Detail Scope definition rather than defined separately. These names are the author's proposal; TF-2 can confirm them or choose others.
* **Default output as a detail variant.** The Detail Variant entry counts the default output as a variant. Without that, a detail scope with only one optional variant would not trigger the configurability requirement, and the opt-in would not be guaranteed. TF-2 can confirm or revise this.
* **Column selection and detail variant columns.** The column-selection requirement, introduced in 1.4, says a FOCUS dataset is configurable to include only a user-defined selection of columns, while the columns documented for a selected detail variant are included regardless of that selection. Read independently, which is how the requirements model resolves them into atomic rules, the two conflict: `ATT-DatasetConfiguration-A-001-M` makes no reference to detail variants, so a validator would flag a dataset carrying a variant column the user did not select. This PR resolves it by adding `except when a column is documented for a selected detail variant` to the column-selection requirement. That amends text introduced in 1.4, so the change would be recorded in the 1.5 changelog while Version Introduced stays 1.4. Alternatives: leave the 1.4 requirement untouched and instead state that the user-defined selection of columns includes the columns documented for a selected detail variant, mirroring the `default column set` form; or leave both requirements unqualified and rely on the detail variant requirement taking precedence implicitly. Which resolution does TF-2 prefer?
* **Detail scopes and delivery scopes.** The Delivery Scope entry allows non-temporal, logical groupings, so a detail scope could be read as one kind of delivery scope. This PR keeps them separate because the delivery scope requirements would misapply. DeliveryHandling requires a complete snapshot for each delivery scope under Overwrite, and CorrectionHandling places Delta and Ledger corrections within a delivery scope. Treating each detail scope as a delivery scope would make it a separate unit of supersession and correction. Records in a companion artifact are also outside any dataset artifact delivery. A detail scope instead determines which records have selectable detail variants. Should the two stay separate, and should Detail Scope be renamed to avoid confusion with Delivery Scope?
* **Changing a detail variant within a delivery scope.** Under Overwrite, the next dataset artifact supersedes earlier ones, so a new variant selection takes effect cleanly. Under Append (Delta or Ledger), dataset artifacts delivered at the previous variant remain alongside records at the new variant within the same delivery scope, so the combined artifacts include more than one detail variant for a detail scope. Restating earlier records at the new variant would also count summable metrics twice unless the earlier records are reversed. Should a variant change take effect only at a delivery scope boundary (e.g., the next billing period), require reversal records, or be left to documentation?
* **Companion artifacts and native datasets.** A companion artifact's structure is not defined by FOCUS, which makes it close to a native dataset artifact. DatasetCompleteness requires custom columns for all native dataset columns unless an exclusion is documented. If companion artifact columns count as native dataset columns, the detail they hold (e.g., `x_UserId`) would be required in the FOCUS dataset, which undoes the opt-in. Should the glossary state that companion artifact columns are not native dataset columns for this purpose, or define a companion artifact as native data?
* **Detail variants and dataset instances.** The Dataset Instance entry already covers instances that differ by custom column inclusions. Does selecting a detail variant produce a distinct dataset instance, or is it configuration of one instance? The answer determines when a new Schema metadata entry is required and whether the dataset-instance merge rules in BilledCost and EffectiveCost apply.
* **PrincipalId and the default column set.** PrincipalId (#2360) is required when IncludesRequesterAttribution applies, and a default column set must include all applicable FOCUS columns. Together, high-cardinality actor detail is in every offered default column set. Options: exempt columns populated only by a non-default detail variant, tie PrincipalId to a selected detail variant, or accept PrincipalId in the default column set.
* **Record minimization and Ledger corrections.** In the Ledger correction style, a reversal and its corrected record can share every non-summable value. The record-minimization SHOULD would merge them into a net record and lose the audit trail. Should the requirement carry an exception, or is a supporting content note enough?

### Type of Change

* [ ] Bug fix
* [x] New feature / Specification update
* [ ] Editorial / Formatting

### Author Checklist

* [x] **AI Usage Guidelines:** I have read the [FOCUS AI Usage Guidelines](/guidelines/contributors/ai-usage-guidelines.md).
* [x] **Self Review Attestation:** I have performed a self-review of my own contribution.
* [x] **AI-Generated Examples:** If this PR includes examples generated by AI, I have manually verified that the data is mathematically accurate, logically consistent, and compliant with the FOCUS schema.
