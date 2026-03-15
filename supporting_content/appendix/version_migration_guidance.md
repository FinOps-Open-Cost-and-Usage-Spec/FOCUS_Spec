# Version Migration Guidance

This appendix provides guidance for practitioners and data generators migrating between FOCUS specification versions. Migration guidance is organized in reverse chronological order, with the most recent migration listed first.

### Document Structure

This guide serves two audiences:

| Audience | Relevant Sections |
|----------|-------------------|
| **All readers** | Overview, What's Unchanged, What's New, What Requires Migration |
| **Practitioners** | Provider and Publisher Column Changes, including migration decision tree, query examples, and verification checklist |
| **Data Generators** | Guidance for Data Generators, including dual-column support, deprecation metadata, and deprecation timeline |

Practitioners updating queries should focus on the migration decision tree and query examples. Data generators implementing FOCUS 1.3 should review the dual-column support recommendations.

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

- [ ] Identify all queries, reports, and dashboards that reference `ProviderName` or `PublisherName`
- [ ] For each usage, determine what business question the column was answering
- [ ] Review [Participating Entity Identification Examples](/specification/appendix/participating_entity_identification.md) for scenarios matching your acquisition methods
- [ ] Plan migration timeline (deprecated columns will be removed in FOCUS 1.4+)

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
- MAY be null when the service does not involve deployment on infrastructure (e.g., professional services, software licenses)
- MAY be null when the hosting provider cannot be uniquely determined (e.g., Tax or Adjustment charges)
- MUST equal `ServiceProviderName` when the service provider hosts their own services and does not expose the underlying host

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
- Continue using existing queries during migration
- Validate new queries against old results
- Transition at their own pace before FOCUS 1.4

### Deprecation Metadata

FOCUS 1.2 introduced metadata properties to signal column deprecation:
- `Deprecated`: Boolean indicating whether a column is deprecated
- `PreviousColumnName`: References the column this one replaces (if applicable)

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

- [Charge Categorization](/specification/supported_features/charge_categorization.md)
- [Commit Usage and Under Usage](/specification/supported_features/commit_usage_and_under_usage.md)
- [Cost Comparison](/specification/supported_features/cost_comparison.md)
- [Effective Cost](/specification/supported_features/effective_cost.md)
- [Marketplace Purchases](/specification/supported_features/marketplace_purchases.md)
- [Participating Entity Identification](/specification/supported_features/participating_entity_identification.md)
- [Service Provider Services](/specification/supported_features/service_provider_services.md)
- [Resource Usage](/specification/supported_features/resource_usage.md)
- [Service Categorization](/specification/supported_features/service_categorization.md)

---

## Additional Resources

- [Participating Entity Identification Examples](/specification/appendix/participating_entity_identification.md) — Scenarios showing how entity values vary by acquisition method
- [ServiceProviderName Column Specification](/specification/datasets/cost_and_usage/columns/serviceprovidername.md)
- [HostProviderName Column Specification](/specification/datasets/cost_and_usage/columns/hostprovidername.md)
- [FOCUS 1.3 Changelog](/CHANGELOG.md)