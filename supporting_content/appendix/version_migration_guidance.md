# Version Migration Guidance 

## Migrating from FOCUS 1.2 to FOCUS 1.3: Provider and Publisher Column Changes

### Overview

FOCUS 1.3 introduces a **migration compatible change** affecting how participating entities are identified in the Cost and Usage dataset. This change deprecates the `ProviderName` and `PublisherName` columns and replaces them with `ServiceProviderName` and `HostProviderName`.

Practitioners and data generators consuming or producing FOCUS 1.2 data will need to update queries and mappings when adopting FOCUS 1.3.

### Why This Change Was Made

The original `ProviderName` and `PublisherName` columns suffered from definitional ambiguity:

| Problem | Impact |
|---------|--------|
| **ProviderName** lacked specificity about *which* provider role was being described | Data generators inconsistently populated values, making cross-provider analysis unreliable |
| **PublisherName** overlapped conceptually with Provider and Invoice Issuer | The column was often left null, duplicated ProviderName, or populated inconsistently across data generators |
| Neither column distinguished between the entity selling a service and the entity hosting the underlying infrastructure | Practitioners couldn't determine who to contact for support vs. billing inquiries |

FOCUS 1.3 resolves this by introducing two purpose-specific columns that align with the distinct entity roles documented in [Participating Entity Identification](participating_entity_identification.md).

### Column Mapping

#### ProviderName → ServiceProviderName

| Attribute | FOCUS 1.2 | FOCUS 1.3 |
|-----------|-----------|-----------|
| Column ID | `ProviderName` | `ServiceProviderName` |
| Display Name | Provider Name | Service Provider Name |
| Feature Level | Mandatory | Mandatory |
| Allows Nulls | False | False |
| Status in 1.3 | Deprecated | Active |

**Migration action:** Replace all references to `ProviderName` with `ServiceProviderName` in queries and ingestion logic. The semantic intent is preserved: both columns identify the entity that makes resources or services available for purchase.

#### PublisherName → No Direct Replacement

| Attribute | FOCUS 1.2 | FOCUS 1.3 |
|-----------|-----------|-----------|
| Column ID | `PublisherName` | *Deprecated, no replacement* |
| Display Name | Publisher Name | — |
| Feature Level | Mandatory | — |
| Status in 1.3 | Deprecated | — |

**Migration action:** Evaluate what business question your `PublisherName` queries were answering, then select the appropriate 1.3 column:

| If you used PublisherName to identify... | Use this column in 1.3 |
|------------------------------------------|------------------------|
| Who sells the service | `ServiceProviderName` |
| Who hosts the underlying infrastructure | `HostProviderName` |
| Who issues the invoice | `InvoiceIssuerName` |
| Who generates the billing data | `DataGenerator` (metadata) |

The ambiguity that `PublisherName` attempted to address is now resolved by the explicit separation of these four entity roles.

#### New Column: HostProviderName

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

## Query Migration Examples

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
SELECT ProviderName, PublisherName, InvoiceIssuerName, SUM(BilledCost)
FROM focus_data
GROUP BY ProviderName, PublisherName, InvoiceIssuerName
```

**FOCUS 1.3:**
```sql
SELECT ServiceProviderName, HostProviderName, InvoiceIssuerName, SUM(BilledCost)
FROM focus_data
GROUP BY ServiceProviderName, HostProviderName, InvoiceIssuerName
```

### Affected Supported Features

The following supported features reference the deprecated columns and should be reviewed when migrating:

- Charge Categorization
- Commit Usage and Under Usage
- Cost Comparison
- Effective Cost
- Marketplace Purchases
- Participating Entity Identification
- Provider Services
- Resource Usage
- Service Categorization

### Deprecation Timeline

| Version | ProviderName Status | PublisherName Status |
|---------|---------------------|----------------------|
| 1.2 | Active | Active |
| 1.3 | Deprecated | Deprecated |
| 1.4+ | Removed | Removed |

Data generators should include both deprecated and new columns in FOCUS 1.3 datasets to support practitioners transitioning their queries.

### Additional Resources

- [Participating Entity Identification Examples](participating_entity_identification.md) — Scenarios showing how Service Provider, Host Provider, Invoice Issuer, and Data Generator values vary by acquisition method
- [ServiceProviderName Column Specification](columns/serviceprovidername.md)
- [HostProviderName Column Specification](columns/hostprovidername.md)
- [FOCUS 1.3 Changelog](../CHANGELOG.md)