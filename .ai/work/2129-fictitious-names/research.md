# Research: #2129 Fictitious Names Across All Appendix Entries

## Issue Summary

Replace all ad-hoc placeholder and real-world vendor names across specification appendix markdown and CSV data files with the approved fictitious names defined in `specification/appendix/appendix_overview.md`.

## Critical Lesson: Substring Replacement Bug (PR #2247)

In PR #2247 (SaaS examples), a find-and-replace operation produced **"StoreStackrp"** — a mangled name caused by:

1. **Partial match**: The search pattern "AwesomeCo" matched inside "AwesomeCorp", replacing only the prefix and leaving "rp" behind.
2. **Wrong target**: The replacement used the provider name ("StoreStack") instead of the customer name ("Acme Corp").

**Root cause**: The original text had overlapping name patterns ("Acme Co" as provider, "AwesomeCorp" as customer). A naive replacement of the shorter "AwesomeCo" substring corrupted the longer "AwesomeCorp".

## Approved Fictitious Names Reference

Source: `specification/appendix/appendix_overview.md` (lines 23-68)

### Data Generators (Providers)

| Fictitious Name | Role | Replaces (Real-World) |
|:---|:---|:---|
| **Aura Web** | Cloud Service Provider (AWS-like) | Amazon Web Services, AWS |
| **CrestNode** | Cloud Service Provider (Azure-like) | Microsoft Azure, Azure |
| **LatticeScale** | Cloud Service Provider (GCP-like) | Google Cloud Platform, GCP |
| **OmniQuery** | Data Platform | Snowflake, Databricks |
| **StackLens** | SaaS Observability | Datadog, New Relic |
| **SprintCanvas** | Project Management | Jira, Asana, Trello |
| **StoreStack** | Database as a Service | MongoDB Atlas |
| **CollabChat** | Team Communications | Slack |
| **PulseMail** | Email API | SendGrid, Mailgun |
| **PipelCRM** | CRM | Salesforce, HubSpot |
| **Budget Beacon** | Cost Management | Cloudability, CloudHealth, ProsperOps |
| **SchemaWeaver** | Open Source Library | OpenCost, etc. |

### Customers

| Fictitious Name | Profile |
|:---|:---|
| **Acme Corp** | Large Enterprise |
| **AeroScale** | Cloud-Native Startup |
| **GearPeak Outdoors** | Mid-Market Retailer |

### Commitment Programs

| Fictitious Name | Category | Replaces |
|:---|:---|:---|
| **Resource Reservations (RRs)** | Usage | Reserved Instances (AWS/Azure), Resource-based CUDs (GCP) |
| **Flexible Spend Plans (FSPs)** | Spend | Savings Plans (AWS) |
| **Dynamic Compute Commitments (DCCs)** | Spend | Flexible CUDs (GCP) |
| **Enterprise Spend Agreements (ESAs)** | Spend | Enterprise Discount Programs (AWS), MACC (Azure) |
| **Interval Spend Commitments (ISCs)** | Spend | Monthly/Annual Commitments (Datadog) |
| **Bulk Capacity Credits (BCCs)** | Spend | Capacity Commitments (Snowflake) |
| **Advance Resource Commitments (ARCs)** | Usage | Capacity Reservations (AWS/Azure/GCP) |

## Known Name Variants in Source Files

### Names requiring replacement (with ALL variants found)

**"ACME" family** (used as both provider and customer across different files):
- `ACME Corp` — correction handling markdown (provider role)
- `Acme Corp` — appendix overview (customer role — this IS the approved customer name)
- `ACME` — standalone references
- `Acme Co` — SaaS spend agreements, invoice detail, contract commitments (provider role)
- `ACMECORP` — virtual currency CSVs (all-caps in identifiers)
- `ACMECORP SERVICE` — virtual currency CSVs
- `ACMECORP Licenses` — simple agreement CSVs
- `AcmeStore` — invoice detail (product/service name)
- `acme` — tag prefixes, resource IDs (e.g., `cr-arc-acme-001`, `cd-rr-acme-001`)

**"Awesome" family** (customer names in SaaS examples):
- `AwesomeCorp` — simple agreements, spend agreements (customer)
- `Awesome Corp` — virtual currency model (customer, note the space)
- `AwesomeCorpDemo` — CSV BillingAccountId values
- `AwesomeDB` — spend agreements (service name)
- `x_awesome_column1/2/3` — metadata examples (custom columns)
- `x_awesome_column_one` — metadata renaming examples

**"Serenity Corp"** — simple agreements CSV (customer)

**"TinyCloud"** — commitment discount flexibility examples (provider)

**"DataStreamer"** / **"DataStreamer Pro"** — contract commitments (third-party SaaS)

**"CyberGuard Inc"** / **"CyberGuard Endpoint Seats"** — contract commitments (security vendor)

**Real cloud provider names** (in commitment discount CSVs):
- `Amazon Web Services` — InvoiceIssuerName, ProviderName, PublisherName
- `Microsoft Azure` — same columns
- `Google Cloud` / `Google Cloud Platform` — same columns
- `AWS`, `Azure`, `GCP` — in file names, anchor IDs, SKU prefixes

### Compound/hyphenated identifier patterns

These are embedded in anchor IDs, resource IDs, CSV identifiers:
- `awsreservedinstance-allupfront-100%utilization` (markdown anchors)
- `awssavingsplan-noupfront-100%utilization` (markdown anchors)
- `azurereservation-allupfront-100%utilization` (markdown anchors)
- `gcpresourcecud-noupfront-100%utilization` (markdown anchors)
- `gcpflexcud-noupfront-100%utilization` (markdown anchors)
- `AWS-USEAST1-COMPUTE-*` (SKU ID patterns in CSVs)
- `cr-arc-acme-001` (commitment resource IDs)
- `cd-rr-acme-001` (commitment discount IDs)

## Authoritative ServiceCategory Assignments (from merged billing_scenario_examples CSVs)

These are the ServiceCategory values used by each fictitious provider in the already-approved CSVs on working_draft:

| Provider | ServiceCategory | Billing Model |
|:---|:---|:---|
| PipelCRM | Business Applications | Seat/license-based |
| SprintCanvas | Business Applications | Seat-based, annual upfront |
| StackLens | Management and Governance | Host/GB-based |
| StoreStack | Databases | Hours/GB (multi-unit PaaS) |
| OmniQuery | *(data platform)* | Credit-based consumption |
| CollabChat | *(team comms)* | Flat-rate subscription |
| PulseMail | *(email API)* | Tiered pricing with minimum |

## Per-Section Correct Mappings (derived from PR #2115 reference)

| Section | Original | Role | Correct Fictitious Name |
|:---|:---|:---|:---|
| SaaS: simple_agreements | ACME Corp / ACME | Provider | **PipelCRM** |
| SaaS: simple_agreements | AwesomeCorp / Serenity Corp | Customer | **Acme Corp** |
| SaaS: spend_agreements | Acme Co | Provider | **StoreStack** |
| SaaS: spend_agreements | AwesomeCorp | Customer | **Acme Corp** |
| SaaS: spend_agreements | AwesomeDB | Service | **StoreStack DB** |
| SaaS: virtual_currency | Acme Co / ACMECORP | Provider | **OmniQuery** |
| SaaS: virtual_currency | AwesomeCorp / Awesome Corp | Customer | **Acme Corp** |
| SaaS: virtual_currency | ACMECORP SERVICE | Service | **OmniQuery Platform** |
| Commitment Discounts | Amazon Web Services (AWS) | Provider | **Aura Web** |
| Commitment Discounts | Microsoft Azure | Provider | **CrestNode** |
| Commitment Discounts | Google Cloud Platform (GCP) | Provider | **LatticeScale** |
| Commitment Discounts | Reserved Instance (AWS/Azure) | Program | **Resource Reservation (RR)** |
| Commitment Discounts | Savings Plan (AWS/Azure) | Program | **Flexible Spend Plan (FSP)** |
| Commitment Discounts | Resource CUD (GCP) | Program | **Resource Reservation (RR)** |
| Commitment Discounts | Flex CUD (GCP) | Program | **Dynamic Compute Commitment (DCC)** |
| Correction Handling | ACME Corp | Data Generator | **CrestNode** |
| Invoice Detail | Acme Co | Invoice Issuer | **Aura Web** |
| Contract Commitments | Acme Co | Cloud Provider | **Aura Web** |
| Contract Commitments | DataStreamer | Marketplace SaaS | **OmniQuery** |
| Contract Commitments | CyberGuard Inc | Security Vendor (seat-based) | **SprintCanvas** *(closest fit: seat-based Business Applications)* |
| Commitment Discount Flexibility | TinyCloud | Cloud Provider | **LatticeScale** |
| Metadata Examples | ACME / Acme | Data Generator | **CrestNode** |
| Commitment Program Eligibility | *(already correct)* | — | **Aura Web**, **Acme Corp** |

## Open PRs for #2129

| PR | Branch | Scope | Status | Mapping Correct? |
|:---|:---|:---|:---|:---|
| #2247 | `2129-fictitious-saas-examples` | SaaS examples (simple/spend/virtual currency) | CHANGES_REQUESTED | Fixed: PipelCRM, Acme Corp, StoreStack |
| #2252 | `2129-fictitious-correction-handling` | Correction handling markdown (ACME Corp → CrestNode) | CHANGES_REQUESTED | Yes (CSVs confirmed clean) |
| #2253 | `2129-fictitious-commitment-discounts-v2` | Commitment discount examples (comprehensive) | CHANGES_REQUESTED | Yes: Aura Web, CrestNode, LatticeScale + programs |
| #2246 | `2129-fictitious-metadata-examples` | Metadata examples (ACME → CrestNode) | OPEN | Yes |
| #2251 | `2129-fictitious-commitment-discount-flexibility` | Commitment discount flexibility (TinyCloud → LatticeScale) | OPEN | Yes |
| #2245 | `2129-fictitious-invoice-detail` | Invoice detail (Acme Co → Aura Web) | OPEN | Yes |
| #2244 | `2129-fictitious-contract-commitments` | Contract commitments | OPEN | Partial: CyberGuard Inc has no approved equivalent |
