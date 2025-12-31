# Scenario Completeness

## Design Rationale

The Scenario Completeness attribute ensures that FOCUS datasets enable practitioners to achieve the same analysis and reporting scenarios available in native datasets. This attribute complements Column Handling by addressing *what* custom columns should be included, while Column Handling addresses *how* custom columns should be named and formatted.

Without this attribute, practitioners adopting FOCUS datasets may lose access to provider-specific information needed for critical analyses, forcing them to maintain parallel native dataset workflows. This attribute establishes clear expectations for data completeness while maintaining data quality and avoiding duplication.

## How Concerns Are Addressed

### AWS Column Stability Concern

**Concern:** AWS believes columns should NEVER change. If they add non-FOCUS columns (e.g., `x_ColumnName`) that later become FOCUS columns, those columns would need to change names, breaking customers who built workflows around the custom column names.

**Solution:** The attribute includes a MAY requirement allowing data generators to preserve non-FOCUS versions of custom columns even after FOCUS equivalents are introduced. This enables migration on practitioners' own terms without breaking changes, addressing AWS's column stability policy.

### GCP "Junk Drawer" Concern

**Concern:** Requiring providers to include all native dataset information as custom columns could cause FOCUS to become a "junk drawer" - accumulating unnecessary, low-quality, or unfocused data.

**Solution:** Since FOCUS only asks providers to include data they already have in their native datasets, data quality depends on provider data quality, not FOCUS requirements. Providers maintain control over what they include and can curate their data appropriately. The requirements emphasize maintaining granularity and accuracy, and explicitly prohibit duplication, ensuring quality standards are preserved.

## When to Include Custom Columns

Data generators SHOULD include custom columns in the following scenarios:

1. **Provider-Specific Attributes:** When native datasets contain attributes not represented in FOCUS columns (e.g., Azure Resource Group, GCP project hierarchy, AWS account organizational units).

2. **Marketplace Metadata:** When charges include marketplace or publisher information needed for attribution or analysis (e.g., marketplace product identifiers, seller information).

3. **Service-Specific Configuration:** When provider services include configuration details needed for optimization or cost attribution (e.g., capacity types, instance families, storage classes).

4. **Correlation Identifiers:** When native datasets include identifiers that enable reliable correlation between FOCUS and native datasets (e.g., native charge identifiers, line item IDs).

## When NOT to Include Custom Columns

Data generators MUST NOT include custom columns in the following scenarios:

1. **Duplication:** When information is already captured in FOCUS standard columns. Custom columns MUST NOT duplicate data already represented in FOCUS columns.

2. **Transformed Data:** When native data is transformed or aggregated into FOCUS columns, data generators MUST NOT add custom columns for the original native representation. The transformation should be documented, but the original format should not be duplicated.

3. **Violates Data Integrity:** When including custom columns would violate FOCUS metrics integrity (e.g., would break cost summation or quantity aggregation).

## Correlation Guidance

To enable reliable correlation between FOCUS and native datasets:

* **Providers with existing unique identifiers:** Include them as custom columns (e.g., `x_ChargeId`, `x_LineItemId`).
* **Providers without existing identifiers:** Document correlation guidance and include minimal custom columns required for dataset joins.
* **Correlation columns serve as linking mechanisms:** Uniqueness within FOCUS datasets is not required, as correlation is typically done at the dataset level.

## Aggregation and Splitting Examples

When rows are split or aggregated to conform to FOCUS requirements (e.g., Discount Handling), custom column values MUST be handled consistently:

### Example: Row Splitting

**Native Dataset:**
- Single row with `ResourceId = "vm-123"`, `Cost = $100`, `x_ResourceGroup = "production"`

**FOCUS Dataset (after discount handling split):**
- Row 1: `ResourceId = "vm-123"`, `BilledCost = $90`, `x_ResourceGroup = "production"`
- Row 2: `ResourceId = "vm-123"`, `BilledCost = $10`, `x_ResourceGroup = "production"` (discount row)

**Note:** `x_ResourceGroup` is preserved on both rows to maintain correlation.

### Example: Row Aggregation

**Native Dataset:**
- Multiple rows with different `x_Tags` values but same `ResourceId`

**FOCUS Dataset (after aggregation):**
- Single row with `ResourceId`, aggregated costs, and `x_Tags` containing all tag values (as JSON or delimited string)

**Note:** Custom column values are aggregated appropriately to preserve data integrity.

## Provider-Specific Examples

### AWS

**Custom columns to include:**

- `x_LineItemId` (for correlation with CUR)
- `x_ReservationArn` (for Reserved Instance tracking)
- `x_SavingsPlanArn` (for Savings Plan tracking)
- `x_LegalEntity` (billing entity information)

**Example:** AWS CUR includes `lineItem/LineItemId` which should be included as `x_LineItemId` to enable correlation.

### Microsoft Azure

**Custom columns to include:**

- `x_ResourceGroup` (for resource group attribution)
- `x_BillingProfileId` (for billing profile hierarchy)
- `x_InvoiceSectionId` (for invoice section attribution)

**Example:** Azure Cost Details include `ResourceGroup` which should be included as `x_ResourceGroup` to enable resource group analysis.

### GCP

**Custom columns to include:**

- `x_ProjectNumber` (if different from SubAccountId)
- `x_BillingAccountId` (GCP's native billing account identifier)

**Example:** GCP BigQuery Billing Export includes project-level identifiers which should be included to enable correlation.

### OCI

**Custom columns to include:**

- `x_CompartmentId` (for compartment hierarchy)
- `x_CompartmentName` (for compartment display names)

**Example:** OCI Cost Reports include compartment information which should be included as custom columns to enable compartment-based analysis.
