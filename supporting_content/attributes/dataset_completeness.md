# Dataset Completeness

## Design Rationale

The Dataset Completeness attribute ensures that FOCUS datasets include custom columns for native dataset columns not represented in FOCUS columns. This attribute complements Column Handling by addressing *what* custom columns should be included, while Column Handling addresses *how* custom columns should be named and formatted.

Without this attribute, practitioners adopting FOCUS datasets may lose access to provider-specific information needed for critical analyses, forcing them to maintain parallel native dataset workflows. This attribute establishes clear expectations for data completeness while maintaining data quality.

## How Concerns Are Addressed

### AWS Column Stability Concern

**Concern:** AWS believes columns should NEVER change. If they add non-FOCUS columns (e.g., `x_ColumnName`) that later become FOCUS columns, those columns would need to change names, breaking customers who built workflows around the custom column names.

**Solution:** The attribute includes a MAY requirement allowing data generators to preserve non-FOCUS versions of custom columns even after FOCUS equivalents are introduced. This enables migration on practitioners' own terms without breaking changes, addressing AWS's column stability policy.

### GCP "Junk Drawer" Concern

**Concern:** Requiring providers to include all native dataset information as custom columns could cause FOCUS to become a "junk drawer" - accumulating unnecessary, low-quality, or unfocused data.

**Solution:** Since FOCUS only asks providers to include data they already have in their native datasets, data quality depends on provider data quality, not FOCUS requirements. Providers maintain control over what they include and can curate their data appropriately. The MAY requirement allowing exclusion of columns that don't support scenarios enables providers to avoid including low-value data, ensuring quality standards are preserved.

## When to Include Custom Columns

Custom columns should be included in the following scenarios:

1. **Provider-Specific Attributes:** When native datasets contain attributes not represented in FOCUS columns (e.g., Azure Resource Group, GCP project hierarchy, AWS account organizational units).

2. **Marketplace Metadata:** When charges include marketplace or publisher information needed for attribution or analysis (e.g., marketplace product identifiers, seller information).

3. **Service-Specific Configuration:** When provider services include configuration details needed for optimization or cost attribution (e.g., capacity types, instance families, storage classes).

4. **Correlation Identifiers:** When native datasets include identifiers that enable reliable correlation between FOCUS and native datasets (e.g., native charge identifiers, line item IDs).

## When NOT to Include Custom Columns

Custom columns should be avoided in the following scenarios:

1. **Duplication:** When information is already captured in FOCUS standard columns. Custom columns should not duplicate data already represented in FOCUS columns.

2. **Transformed Data:** When native data is transformed or aggregated into FOCUS columns, data generators should generally not add custom columns for the original native representation. The transformation should be documented instead. However, data generators MAY preserve non-FOCUS versions of columns when FOCUS equivalents are introduced to enable migration without breaking changes.

3. **Violates Data Integrity:** When including custom columns would violate FOCUS metrics integrity (e.g., would break cost summation or quantity aggregation).

## Correlation Guidance

To enable reliable correlation between FOCUS and native datasets:

* **Providers with existing unique identifiers:** Include them as custom columns (e.g., `x_ChargeId`, `x_LineItemId`).
* **Providers without existing identifiers:** Document correlation guidance and include minimal custom columns required for dataset joins.
* **Correlation columns serve as linking mechanisms:** Uniqueness within FOCUS datasets is not required, as correlation is typically done at the dataset level.

## Aggregation and Splitting Examples

Custom column values must be handled consistently when rows are split or aggregated to conform to other FOCUS requirements (e.g., Discount Handling):

### Example: Row Splitting

**Native Dataset:**

* Single row with `ResourceId = "vm-123"`, `Cost = $100`, `x_ResourceGroup = "production"`

**FOCUS Dataset (after discount handling split):**

* Row 1: `ResourceId = "vm-123"`, `BilledCost = $90`, `x_ResourceGroup = "production"`
* Row 2: `ResourceId = "vm-123"`, `BilledCost = $10`, `x_ResourceGroup = "production"` (discount row)

**Note:** `x_ResourceGroup` is preserved on both rows to maintain correlation.

### Example: Row Aggregation

**Native Dataset:**

* Multiple rows with different `x_Tags` values but same `ResourceId`

**FOCUS Dataset (after aggregation):**

* Single row with `ResourceId`, aggregated costs, and `x_Tags` containing all tag values (as JSON or delimited string)

**Note:** Custom column values are aggregated appropriately to preserve data integrity.

## Provider-Specific Examples

### AWS

**Custom columns to include:**

* `x_LineItemId` (for correlation with CUR)
* `x_ReservationArn` (for Reserved Instance tracking)
* `x_SavingsPlanArn` (for Savings Plan tracking)
* `x_LegalEntity` (billing entity information)

**Example:** AWS CUR includes `lineItem/LineItemId` which should be included as `x_LineItemId` to enable correlation.

### Microsoft Azure

**Custom columns to include:**

* `x_ResourceGroup` (for resource group attribution)
* `x_BillingProfileId` (for billing profile hierarchy)
* `x_InvoiceSectionId` (for invoice section attribution)

**Example:** Azure Cost Details include `ResourceGroup` which should be included as `x_ResourceGroup` to enable resource group analysis.

### GCP

**Custom columns to include:**

* `x_ProjectNumber` (if different from SubAccountId)
* `x_BillingAccountId` (GCP's native billing account identifier)

**Example:** GCP BigQuery Billing Export includes project-level identifiers which should be included to enable correlation.

### OCI

**Custom columns to include:**

* `x_CompartmentId` (for compartment hierarchy)
* `x_CompartmentName` (for compartment display names)

**Example:** OCI Cost Reports include compartment information which should be included as custom columns to enable compartment-based analysis.

## Related Requirements

### Column Handling

The Column Handling attribute defines *how* custom columns should be named (using the `x_` prefix convention), formatted, and documented. Dataset Completeness defines *what* custom columns should be included to ensure complete coverage of native dataset columns. These attributes work together to ensure custom columns are both properly handled and comprehensively included.

### Provider Column Mappings (FR #1098)

For comprehensive documentation of how native columns map to FOCUS columns (both standard and custom), see the provider column mappings feature request (#1098). While Column Handling requires documentation of custom columns, #1098 addresses the broader need for complete native-to-FOCUS column mapping documentation across all column types.

## Design Decisions

* **Separate attribute from Column Handling**
  * Concern: Why not add these requirements to Column Handling?
  * Decision: Column Handling applies requirements to columns already in the dataset (naming, ordering). Dataset Completeness defines which additional columns the dataset should include. These are different scopes — column-level formatting vs dataset-level coverage.
* **Scenario-based vs column-based framing**
  * Concern: Should the MUST requirement reference analysis/reporting *scenarios* or native dataset *columns*?
  * Options: Scenario-based (flexible but subjective) vs column-based (concrete, enforceable against native dataset documentation)
  * Decision: Column-based. The MAY exclusion for columns that don't support scenarios preserves scenario thinking within a verifiable framework.
* **No aggregation or granularity requirements**
  * Concern: Does this overlap with FR #1091 (column selection) or FR #1093 (data granularity)?
  * Decision: No. Fidelity means "don't degrade data you already have." Row split/aggregation handling only applies when *other* FOCUS requirements (e.g., Discount Handling) cause splits.
* **"Native dataset" terminology**
  * Concern: Need a formal term for provider-specific, non-FOCUS datasets.
  * Options: Native dataset, non-FOCUS dataset, proprietary dataset, source/provider dataset
  * Decision: "Native dataset" — intuitive, not overly broad (unlike "non-FOCUS") or adversarial (unlike "proprietary"). Glossary entry added.
* **"Materially" qualifier on MUST include requirement**
  * Concern: Providers could be forced to include 60+ native columns (Mike, pydi-aws)
  * Decision: Added "materially support analysis or reporting" to scope the requirement.
* **Integrity requirement made verifiable**
  * Concern: "Preserve the integrity of all columns" too vague to test (Shawn)
  * Decision: Changed to "MUST NOT alter the aggregated values of summable metrics."
* **Default column set moved to Dataset Configuration**
  * Concern: Column selection belongs with Dataset Configuration, not here (Shawn, Matt)
  * Decision: Moved MAY requirement to Dataset Configuration.
* **SHOULD NOT duplicate vs MAY preserve**
  * Concern: Appear contradictory (Shawn)
  * Decision: Complementary — SHOULD NOT prevents new duplication; MAY preserve allows temporary overlap during migration when FOCUS adds equivalent columns.
* **Custom column documentation requirement moved to Column Handling**
  * Concern: Documentation is a column-level requirement — it applies to all custom columns regardless of why they were added (Shawn)
  * Decision: Moved to Column Handling. Documentation applies to every custom column (whether added for Dataset Completeness, Invoice Handling, or Discount Handling), making it a column-level rule alongside naming and ordering, not a dataset coverage policy.

## Future Considerations

The following items were identified during development but deferred for future work:

1. **Clarify "data generator" scope:** The glossary should explicitly note that data generators include both providers (cloud, SaaS) and FinOps tool vendors who aggregate or transform billing data.

2. **GA dataset qualifier (potential):** Consider whether to limit requirements to generally available (GA) native datasets only, excluding preview/beta datasets. This could address provider concerns about matching experimental features.
