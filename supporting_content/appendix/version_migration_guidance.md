# Version Migration Guidance

This appendix provides guidance for practitioners and data generators migrating between FOCUS specification versions. Migration guidance is organized in reverse chronological order, with the most recent migration listed first.

## Document Structure

This guide serves two audiences, and each migration below is organized the same way:

| Audience | Relevant Sections |
|----------|-------------------|
| **All readers** | Overview, What's Unchanged, What's New, What Requires Migration |
| **Practitioners** | Practitioner-facing migration topics covering query and pipeline impact, including decision trees, query examples, and verification steps where applicable |
| **Data Generators** | Data generator guidance covering implementation sequencing and attribute or column changes for the transition |

Practitioners should focus on the What Requires Migration summary and the practitioner topics for their version transition. Data generators should review the data generator guidance for the same transition.

## Migrating from FOCUS 1.3 to FOCUS 1.4

### Overview

FOCUS 1.4 introduces changes across the categories defined by the [Change Impact Classification](/guidelines/contributors/spec-change-guidelines.md):

| Classification | Summary |
|----------------|---------|
| **Compatible** | Two new datasets, new columns, six new attributes, two new supported features, and revised requirements for existing cost columns. No changes required to existing queries. |
| **Migration Compatible** | Removal of the deprecated `ProviderName` and `PublisherName` columns, a revised `ContractApplied` format, and removal of three attributes whose requirements moved to successor attributes and an appendix entry. Queries or implementations referencing these require updates. |
| **Incompatible** | None |

FOCUS 1.4 is a larger release than FOCUS 1.3, but most changes are additive and compatible, with no incompatible changes. The items requiring migration are concentrated in a few areas, including the removal of columns deprecated during the 1.3 cycle. Practitioners should review the What Requires Migration summary and the Practitioner Guidance below; data generators should review the Data Generator Guidance.

### What's Unchanged

All columns, attributes, and behaviors from FOCUS 1.3 carry forward into FOCUS 1.4 except for the removed columns and attributes noted below. Existing queries that do not reference the removed columns and do not parse the revised JSON object structure continue to work without modification.

### What's New in FOCUS 1.4

The following additive changes do not require migration but may affect data pipelines expecting a fixed schema:

| Change Type | Summary |
|-------------|---------|
| **New Datasets** | [`BillingPeriod`](/specification/datasets/billing_period/dataset.md) provides invoice-issuer-aware billing period boundaries and status; [`InvoiceDetail`](/specification/datasets/invoice_detail/dataset.md) carries the financial record of charges as they appear on issued invoices (payment currency, terms, due date, purchase order number). Together they support reconciling usage to issued invoices |
| **Expanded Dataset** | The [`ContractCommitment`](/specification/datasets/contract_commitment/dataset.md) dataset grows from 13 to 30 columns, covering identification, lifecycle and periods, commitment structure, and cost and quantity |
| **New Supported Features** | [Invoice Reconciliation](/specification/supported_features/invoice_reconciliation.md) and [Commitment Program Eligibility Details](/specification/supported_features/commitment_program_eligibility_details.md) |
| **New Cost and Usage Columns** | [`CommitmentProgramEligibilityDetails`](/specification/datasets/cost_and_usage/columns/commitmentprogrameligibilitydetails.md) and [`InvoiceDetailId`](/specification/datasets/cost_and_usage/columns/invoicedetailid.md) |
| **New Attributes** | [`CorrectionHandling`](/specification/attributes/correction_handling.md), [`CustomColumnHandling`](/specification/attributes/custom_column_handling.md), [`DatasetCompleteness`](/specification/attributes/dataset_completeness.md), [`DatasetConfiguration`](/specification/attributes/dataset_configuration.md), [`DeliveryHandling`](/specification/attributes/delivery_handling.md), and [`FocusColumnHandling`](/specification/attributes/focus_column_handling.md) |
| **New Appendix Entries** | [Discount Handling](/specification/appendix/discount_handling.md), [Rounding Variance Tolerance](/specification/appendix/rounding_variance_tolerance.md), [Invoice and Billing Period Handling](/specification/appendix/invoice_and_billing_period_handling.md), and worked examples for contract commitments, correction handling, invoice detail, and JSON objects |

See the [CHANGELOG](/CHANGELOG.md) for complete details.

### What Requires Migration

The following changes require action. Each is detailed in the Practitioner Guidance or Data Generator Guidance below.

| Change | Audience | Action |
|--------|----------|--------|
| `ProviderName` and `PublisherName` removed | Practitioners | Migrate any remaining queries to the successor columns identified during the 1.3 cycle. |
| `ContractApplied` format revised to the JSON Object Schema format | Practitioners | Update queries that parse the `ContractApplied` JSON structure. |
| `ColumnHandling`, `DiscountHandling`, and `InvoiceHandling` attributes removed | Data Generators | Apply the requirements that moved to successor attributes and an appendix entry. |

### Practitioner Guidance

#### Provider and Publisher Column Removal

The `ProviderName` and `PublisherName` columns were deprecated in FOCUS 1.3 and are removed in FOCUS 1.4. Their use cases were redistributed to `ServiceProviderName`, `HostProviderName`, `InvoiceIssuerName`, and the `DataGenerator` metadata property during the 1.3 cycle.

Practitioners who have not yet migrated queries away from these columns should follow the [Provider and Publisher Column Changes](#provider-and-publisher-column-changes) guidance for the 1.2 to 1.3 transition below, which provides the column-by-column decision tree, the acquisition-method scenario matrix, and verification steps. The successor columns and their mapping are unchanged in FOCUS 1.4; only the removal of the deprecated columns is new.

#### ContractApplied Format Change

The [`ContractApplied`](/specification/datasets/cost_and_usage/columns/contractapplied.md) column was revised in FOCUS 1.4 to follow the JSON Object Schema format. The concepts represented by the column are unchanged; the change is to the structure of the JSON value.

Practitioners whose queries parse the `ContractApplied` value should update their parsing logic to the FOCUS 1.4 schema. Queries that test only for the presence of `ContractApplied`, or that do not inspect its internal structure, are unaffected. See the [Examples: JSON Object](/specification/appendix/json_object_examples/json_object_examples_overview.md) appendix for the JSON Object Schema format.

#### Revised Cost Column Requirements

These changes are classified as Compatible and do not require query changes, but they refine how core cost values are defined. Practitioners performing invoice reconciliation or commitment amortization analysis should review the updated definitions:

* [`BilledCost`](/specification/datasets/cost_and_usage/columns/billedcost.md) and [`EffectiveCost`](/specification/datasets/cost_and_usage/columns/effectivecost.md) requirements were revised to clarify the treatment of pricing adjustments, covered and covering charges, and cross-record sum validation. When a covering charge (a purchase that pays for other charges, such as a reserved instance prepayment) and the charges it covers are both present in the same dataset instance, `EffectiveCost` and `BilledCost` sum to the same total within the covering charge's charge period; the totals may differ when only one side of that relationship is present, or when the charges span multiple billing periods or billing accounts.
* [`InvoiceId`](/specification/datasets/cost_and_usage/columns/invoiceid.md) changed from a Recommended to a Conditional feature level. Values are populated for charges associated with an issued or pre-generated provisional invoice.

### Data Generator Guidance

#### Attribute Restructuring

Three attributes were removed in FOCUS 1.4. Their requirements moved to the successor attributes and appendix entry shown below:

| Removed Attribute | Requirements Moved To |
|-------------------|-----------------------|
| `ColumnHandling` | `FocusColumnHandling` and `CustomColumnHandling` |
| `DiscountHandling` | Discount Handling appendix entry |
| `InvoiceHandling` | `DeliveryHandling` and `DatasetCompleteness` |

Data generators applying these attributes should map their existing implementation to the successor requirements.

#### Recommended Implementation Sequence

For a release with multiple changes, data generators can reduce consumer disruption by sequencing the transition:

* Adopt additive changes first. New datasets, columns, and attributes do not affect existing consumers and can be introduced independently.
* Apply the attribute restructuring. Map `ColumnHandling`, `DiscountHandling`, and `InvoiceHandling` implementations to their successors.
* Complete the column changes last. Remove `ProviderName` and `PublisherName` once consumers have migrated, and adopt the revised `ContractApplied` format.

During staggered adoption, practitioners may receive FOCUS 1.3 and FOCUS 1.4 data from different providers during the same period. Consumers should determine the FOCUS version of each dataset they process and apply the column expectations for that version, since the removed columns are absent from FOCUS 1.4 data but may remain present in FOCUS 1.3 data during the transition.

### Affected Supported Features

The following supported features reference columns, attributes, or behaviors changed in FOCUS 1.4 and may require documentation or query updates:

* [Participating Entity Identification](/specification/supported_features/participating_entity_identification.md), for the successor columns to the removed `ProviderName` and `PublisherName`
* [Contract Commitments](/specification/supported_features/contract_commitments.md), for the revised `ContractApplied` format
* [Billed Cost and Invoice Alignment](/specification/supported_features/billed_cost_and_invoice_alignment.md) and [Effective Cost](/specification/supported_features/effective_cost.md), for the revised cost column requirements
* [Cost Comparison](/specification/supported_features/cost_comparison.md), for the expanded cash-based versus accrual-based comparison guidance

### Additional Resources

* [FOCUS 1.4 CHANGELOG](/CHANGELOG.md), the complete list of 1.4 changes by classification
* The [Migrating from FOCUS 1.2 to FOCUS 1.3](#migrating-from-focus-12-to-focus-13) section below, for the Provider and Publisher migration decision tree that remains relevant in FOCUS 1.4

---

## Migrating from FOCUS 1.2 to FOCUS 1.3

### Overview

FOCUS 1.3 introduces changes across three categories defined by the [Change Impact Classification](/guidelines/contributors/spec-change-guidelines.md):

| Classification | Summary |
|----------------|---------|
| **Compatible** | New columns, new dataset, and new metadata. No changes required to existing queries. |
| **Migration Compatible** | Deprecated `ProviderName` and `PublisherName` columns replaced by `ServiceProviderName` and `HostProviderName`. Queries referencing deprecated columns require updates. |
| **Incompatible** | None |

Most practitioners can adopt FOCUS 1.3 without changes. Only queries referencing `ProviderName` or `PublisherName` require migration.

### What's Unchanged

All columns, attributes, and behaviors from FOCUS 1.2 remain compatible in FOCUS 1.3 except for the deprecated columns noted below. Existing queries that do not reference `ProviderName` or `PublisherName` will continue to work without modification.

### What's New in FOCUS 1.3

The following additive changes do not require migration but may affect data pipelines expecting a fixed schema:

| Change Type | Summary |
|-------------|---------|
| **New Dataset** | [`ContractCommitment`](/specification/datasets/contract_commitment/dataset.md) — 13 columns tracking contract and commitment details separately from usage rows |
| **Split Cost Allocation** | 5 new columns (`AllocatedMethodId`, `AllocatedMethodDetails`, `AllocatedResourceId`, `AllocatedResourceName`, `AllocatedTags`) enabling data generator-calculated cost allocation |
| **Contract Tracking** | [`ContractApplied`](/specification/datasets/cost_and_usage/columns/contractapplied.md) column links usage rows to contract commitments via JSON object references |
| **Entity Identification** | [`ServiceProviderName`](/specification/datasets/cost_and_usage/columns/serviceprovidername.md) and [`HostProviderName`](/specification/datasets/cost_and_usage/columns/hostprovidername.md) provide explicit entity role identification |
| **New Metadata** | [Dataset Instance](/specification/metadata/dataset_instance/dataset_instance_overview.md) and [Recency](/specification/metadata/recency/recency_overview.md) metadata for tracking data identity and freshness |
| **New Attributes** | `InvoiceHandling`, `JsonObjectFormat`, and `DataGeneratorCalculatedSplitCostAllocationHandling` |

See the [CHANGELOG](/CHANGELOG.md) for complete details.

### What Requires Migration

Only the `ProviderName` and `PublisherName` columns are deprecated in FOCUS 1.3. These columns have been removed in FOCUS 1.4.

---

## Provider and Publisher Column Changes

### Before You Begin (Practitioners)

Practitioners should complete this assessment before migrating queries:

* [ ] Identify all queries, reports, and dashboards that reference `ProviderName` or `PublisherName`
* [ ] For each usage, determine what business question the column was answering
* [ ] Review [Participating Entity Identification Examples](/specification/appendix/participating_entity_identification.md) for scenarios matching your acquisition methods
* [ ] Plan migration timeline (deprecated columns will be removed in FOCUS 1.4+)

### Why This Change Was Made

The original `ProviderName` and `PublisherName` columns suffered from definitional ambiguity:

| Problem | Impact |
|---------|--------|
| `ProviderName` lacked specificity about which provider role was being described | Data generators inconsistently populated values, making cross-provider analysis unreliable |
| `PublisherName` overlapped conceptually with Provider and Invoice Issuer | The column was often null, duplicated `ProviderName`, or populated inconsistently |
| Neither column distinguished between the entity selling a service and the entity hosting the infrastructure | Practitioners couldn't determine who to contact for support vs. billing inquiries |

FOCUS 1.3 resolves this by introducing two purpose-specific columns that align with the distinct entity roles documented in [Participating Entity Identification](/specification/appendix/participating_entity_identification.md).

### Migration Decision Tree (Practitioners)

The correct mapping from deprecated columns depends on what business question your queries were answering, not a simple column rename.

#### Migrating ProviderName

| If you used ProviderName to identify... | Use this column in 1.3 | Notes |
|-----------------------------------------|------------------------|-------|
| Who sells the service you're consuming | `ServiceProviderName` | Most common case for direct CSP purchases |
| The cloud platform hosting marketplace purchases | `HostProviderName` | Marketplace scenarios where ProviderName held the CSP |
| The entity for billing inquiries | `InvoiceIssuerName` | Already existed in 1.2 |

#### Migrating PublisherName

| If you used PublisherName to identify... | Use this column in 1.3 | Notes |
|------------------------------------------|------------------------|-------|
| Who sells the service (e.g., SaaS vendor in marketplace) | `ServiceProviderName` | Primary intended use |
| Who hosts the underlying infrastructure | `HostProviderName` | Rare; usually null or duplicated ProviderName |
| Who issues the invoice | `InvoiceIssuerName` | Already existed in 1.2 |
| Who generates the billing data | `DataGenerator` (metadata) | Metadata property, not a column |

#### Key Insight: Acquisition Method Matters

The mapping varies by how resources or services were acquired. Review these common scenarios:

| Scenario | Old ProviderName | Old PublisherName | New ServiceProviderName | New HostProviderName |
|----------|------------------|-------------------|-------------------------|----------------------|
| Direct CSP purchase | CSP | CSP (or null) | CSP | CSP |
| Marketplace: SaaS on CSP infrastructure | CSP | SaaS Vendor | SaaS Vendor | CSP |
| Marketplace: SaaS on vendor infrastructure | CSP | SaaS Vendor | SaaS Vendor | SaaS Vendor |
| MSP-managed services | MSP | MSP | MSP | CSP (if visible) or MSP |
| Direct SaaS purchase | SaaS Vendor | SaaS Vendor | SaaS Vendor | CSP (if visible) or SaaS Vendor |

For the complete scenario matrix, see [Participating Entity Identification Examples](/specification/appendix/participating_entity_identification.md).

### New Column: HostProviderName

| Attribute | Value |
|-----------|-------|
| Column ID | `HostProviderName` |
| Display Name | Host Provider Name |
| Feature Level | Mandatory |
| Allows Nulls | True |
| Introduced | 1.3 |

**Purpose:** Identifies the entity providing the underlying infrastructure on which the Service Provider's resources or services are deployed.

**Nullability rules:**
* MAY be null when the service does not involve deployment on infrastructure (e.g., professional services, software licenses)
* MAY be null when the hosting provider cannot be uniquely determined (e.g., Tax or Adjustment charges)
* MUST match `ServiceProviderName` when the service provider hosts their own services and does not expose the underlying host

### Query Migration Examples (Practitioners)

#### Basic Provider Query

**FOCUS 1.2:**
```sql
SELECT ProviderName, SUM(BilledCost) AS TotalCost
FROM focus_data
GROUP BY ProviderName
```

**FOCUS 1.3:**
```sql
SELECT ServiceProviderName, SUM(BilledCost) AS TotalCost
FROM focus_data
GROUP BY ServiceProviderName
```

#### Multi-Entity Analysis

**FOCUS 1.2:**
```sql
SELECT 
    ProviderName, 
    PublisherName, 
    InvoiceIssuerName, 
    SUM(BilledCost) AS TotalCost
FROM focus_data
GROUP BY ProviderName, PublisherName, InvoiceIssuerName
```

**FOCUS 1.3:**
```sql
SELECT 
    ServiceProviderName, 
    HostProviderName, 
    InvoiceIssuerName, 
    SUM(BilledCost) AS TotalCost
FROM focus_data
GROUP BY ServiceProviderName, HostProviderName, InvoiceIssuerName
```

#### Marketplace Cost Analysis

**FOCUS 1.2** (common pattern to find marketplace purchases):
```sql
SELECT 
    ProviderName,
    PublisherName, 
    SUM(BilledCost) AS TotalCost
FROM focus_data
WHERE ProviderName != PublisherName
GROUP BY ProviderName, PublisherName
```

**FOCUS 1.3** (different semantics):
```sql
SELECT 
    ServiceProviderName,
    HostProviderName, 
    SUM(BilledCost) AS TotalCost
FROM focus_data
WHERE ServiceProviderName != HostProviderName
GROUP BY ServiceProviderName, HostProviderName
```

### Verification (Practitioners)

After migrating queries, practitioners should verify results:

1. **Direct CSP purchases:** Query results should match pre-migration outputs when grouping by `ServiceProviderName` instead of `ProviderName`
2. **Marketplace scenarios:** Results may show different groupings than before—this is intentional and reflects the corrected entity identification
3. **Null handling:** `HostProviderName` may be null for charges that don't involve infrastructure (licenses, professional services, adjustments)

---

## Guidance for Data Generators

### Dual-Column Support During Transition

Data generators SHOULD include both deprecated and new columns in FOCUS 1.3 datasets to support practitioners transitioning their queries. This allows practitioners to:
* Continue using existing queries during migration
* Validate new queries against old results
* Transition at their own pace before FOCUS 1.4

### Deprecation Metadata

FOCUS 1.2 introduced metadata properties to signal column deprecation:
* `Deprecated`: Boolean indicating whether a column is deprecated
* `PreviousColumnName`: References the column this one replaces (if applicable)

Data generators SHOULD populate these properties in their metadata schema to help practitioners identify deprecated columns programmatically.

### Deprecation Timeline

| Version | ProviderName Status | PublisherName Status |
|---------|---------------------|----------------------|
| 1.2 | Active | Active |
| 1.3 | Deprecated | Deprecated |
| 1.4+ | Removed | Removed |

---

## Affected Supported Features

The following supported features reference participating entity columns and may require documentation or query updates:

* [Charge Categorization](/specification/supported_features/charge_categorization.md)
* [Commit Usage and Under Usage](/specification/supported_features/commit_usage_and_under_usage.md)
* [Cost Comparison](/specification/supported_features/cost_comparison.md)
* [Effective Cost](/specification/supported_features/effective_cost.md)
* [Marketplace Purchases](/specification/supported_features/marketplace_purchases.md)
* [Participating Entity Identification](/specification/supported_features/participating_entity_identification.md)
* [Service Provider Services](/specification/supported_features/service_provider_services.md)
* [Resource Usage](/specification/supported_features/resource_usage.md)
* [Service Categorization](/specification/supported_features/service_categorization.md)

---

## Additional Resources

* [Participating Entity Identification Examples](/specification/appendix/participating_entity_identification.md) — Scenarios showing how entity values vary by acquisition method
* [ServiceProviderName Column Specification](/specification/datasets/cost_and_usage/columns/serviceprovidername.md)
* [HostProviderName Column Specification](/specification/datasets/cost_and_usage/columns/hostprovidername.md)
* [FOCUS 1.3 Changelog](/CHANGELOG.md)
