# Contract Commitments

## Overview

The **Contract Commitment** dataset provides a structured representation of the commercial agreements between a customer and their service providers. While the [Cost and Usage](#datasets.costandusage) dataset tracks the results of consumption, the Contract Commitment dataset tracks the intent and constraints of the relationship.

### Core Logical Pillars

To ensure interoperability across different data generators, the dataset relies on three core logical pillars:

1. **Commitment Categorization:** Distinguishes between obligations based on **Spend** (e.g., "I will spend 1M") vs. **Usage** (e.g., "I will use 500 vCPUs"). This determines which metrics —- Cost or Quantity —- are used to measure fulfillment.
2. **Fulfillment Modeling:** Defines the operational behavior and consumption flexibility of a commitment.
   * **Continuous** models (like Reserved Instances) are "use-it-or-lose-it", typically within short windows (e.g., Hourly).
   * **Discontinuous** models (like Enterprise Agreements) allow consumption to be aggregated over a longer duration (e.g., Total Term).
3. **Eligibility Boundaries:** Using a structured JSON format, the dataset defines the logical perimeter of a commitment, specifying exactly which accounts, regions, or services are eligible to receive the negotiated benefit.

### Expected Value Taxonomy

The following table defines the high-level expectations for key categorical columns in this dataset:

| Attribute | Expected Value Logic | Example Values |
| :--- | :--- | :--- |
| **Benefit Category** | The primary economic advantage provided. | `Discount`, `Monetary Pool`, `Availability`, `Other` |
| **Model** | How the commitment is consumed. | `Continuous`, `Discontinuous` |
| **Fulfillment Interval** | The "Use-it-or-lose-it" or "Goal" window for reset. | `Hourly`, `Monthly`, `Annual`, `Total Term` |
| **Lifecycle Status** | The current lifecycle state of the record. | `Active`, `Exhausted`, `Pending`, `Expired`, `Canceled` |
| **Offer Category** | The "privacy" or source level of the pricing. | `Public`, `Negotiated` |
| **Payment Model** | The cash-flow timing for the commitment. | `No Upfront`, `Partial Upfront`, `All Upfront` |

### Why the Values Matter

By standardizing these values, organizations can move from manual spreadsheet tracking to **Automated FinOps Governance**.

For example, in a Discontinuous model with an Annual Fulfillment Interval, a reporting engine does not evaluate the commitment hour-by-hour. Instead, it accumulates usage across the full year and waits until the end of that annual interval to determine whether the contractual threshold has been met. At that point, it looks for a "True-up" event — the reconciliation step that settles any difference between the committed amount and actual consumption.

By contrast, in a Continuous model with an Hourly Fulfillment Interval, an engine evaluates the commitment during every hour of the billing period. For each individual hour, it compares committed capacity to actual usage. If usage falls short during a given interval, the engine calculates "Waste", representing the unused portion of the commitment for that specific hour. That unused capacity is measured and reported as it occurs rather than deferred for end-of-term reconciliation.

## Examples

### Common Offering Examples

The following table provides a reference for how common cloud and SaaS commercial offerings theoretically map to the Contract Commitment schema. (This table is provided for demonstration purposes only.  Actual value assignments are left to the data generators upon the creation of dataset artifacts.)

In the below table, CC represents Contract Commitment.

| Offering Example | CC Category | CC Model | CC Offer Category | CC Benefit Category | CC Fulfillment Interval | CC Duration Type | CC Payment Model | CC Payment Interval |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **AWS Savings Plan** | Spend | Continuous | Public | Discount | Hourly | 1 Year | Partial Upfront | Monthly |
| **Azure Reservation** | Usage | Continuous | Public | Discount | Hourly | 3 Years | All Upfront | One-Time |
| **GCP Flex CUD** | Spend | Continuous | Public | Discount | Hourly | 3 Years | No Upfront | Monthly |
| **Azure ODCR** | Usage | Continuous | Public | Availability | Hourly | 1 Month | No Upfront | Monthly |
| **AWS EDP / MACC** | Spend | Discontinuous | Negotiated | Discount | Annual | 3 Years | No Upfront | Monthly |
| **Snowflake (EA)** | Spend | Discontinuous | Negotiated | Monetary Pool | Annual | 1 Year | All Upfront | Annual |
| **Datadog (Public)** | Spend | Discontinuous | Public | Monetary Pool | Annual | 1 Year | No Upfront | Monthly |
| **SaaS Seats (CRM)** | Usage | Continuous | Negotiated | Discount | Monthly | 1 Year | No Upfront | Monthly |
| **Multi-Year Pool** | Spend | Discontinuous | Negotiated | Monetary Pool | Total Term | 3 Years | All Upfront | One-Time |
| **Growth Rebate** | Spend | Discontinuous | Negotiated | Monetary Pool | Annual | 2 Years | No Upfront | Annual |
| **API Credit Pack** | Usage | Discontinuous | Public | Monetary Pool | Transactional | 2 Years | All Upfront | One-Time |
| **Marketplace SaaS** | Spend | Discontinuous | Negotiated | Monetary Pool | Annual | 1 Year | All Upfront | One-Time |
| **90-Day POC** | Spend | Discontinuous | Negotiated | Monetary Pool | Custom | 90 Days | No Upfront | Custom |
| **Enterprise Support** | Usage | Continuous | Negotiated | Other | Monthly | 1 Year | No Upfront | Monthly |

### Scenario 1: Strategic Cloud Transformation Agreement

This example demonstrates a complex, multi-faceted agreement between a customer and a primary cloud provider, **Acme Co**. While governed by a single master contract (`AGR-99-BETA`), it contains three distinct commercial levers:

#### Commitment 1: The Global Spend Pool

* **Context:** A high-level Enterprise Agreement (EA) where the customer commits to spending **1M USD** over three years.
* **Commercial Logic:** A **Spend-based**, **Discontinuous** model. Every dollar spent within the three-year window fulfills the commitment.
* **Eligibility:** **Global**. Applies to any service or region.

#### Commitment 2: Regional Compute Reservations

* **Context:** Fixed capacity of virtual machines in a specific data center for stable production workloads.
* **Commercial Logic:** A **Usage-based**, **Continuous** model. This benefit is "use it or lose it" on an **Hourly** basis.
* **Eligibility:** Restricted to specific resource types running in the `us-east-1` region.

#### Commitment 3: Marketplace SaaS Add-on

* **Context:** A specialized analytics tool, **DataStreamer**, purchased through the Acme marketplace.
* **Commercial Logic:** A **Spend-based** "pass-through" for financial tracking with an **Annual Fulfillment Interval**.
* **The Issuer/Provider Split:** The **Service Provider** is **DataStreamer**, but the **Invoice Issuer** remains **Acme Co**, showing how the model tracks third-party spend in a unified ecosystem.

### Data Example: AGR-99-BETA

| Column | Commitment 1: Spend Pool | Commitment 2: Compute RI | Commitment 3: Marketplace SaaS |
| :--- | :--- | :--- | :--- |
| **Billing Currency** | `EUR` | `EUR` | `EUR` |
| **CC Benefit Category** | `Monetary Pool` | `Discount` | `Monetary Pool` |
| **CC Category** | `Spend` | `Usage` | `Spend` |
| **CC Cost** | `925000.00` | `46250.00` | `111000.00` |
| **CC Created** | `2025-12-01T09:00:00Z` | `2025-12-01T09:00:00Z` | `2026-01-15T14:30:00Z` |
| **CC Description** | `3yr Enterprise Spend Goal` | `us-east-1 m5 Reservations` | `DataStreamer Pro via Marketplace` |
| **CC Discount %** | `0.15` | `0.40` | `0.10` |
| **CC Duration Type** | `3 Years` | `1 Year` | `1 Year` |
| **CC Applicability** | `{"IsGlobalScope": true}` | `{"InclusionOperator": "Or", "Inclusions": [{"Dimension": "RegionId", "Operator": "In", "Values": ["us-east-1"]}]}` | `{"InclusionOperator": "Or", "Inclusions": [{"Dimension": "ServiceCategory", "Operator": "In", "Values": ["Analytics"]}]}` |
| **CC Fulfillment Interval** | `Total Term` | `Hourly` | `Annual` |
| **CC ID** | `CMT-SPEND-001` | `CMT-RI-002` | `CMT-SaaS-003` |
| **CC Last Updated** | `2026-02-01T10:00:00Z` | `2025-12-01T09:00:00Z` | `2026-01-15T14:30:00Z` |
| **CC Model** | `Discontinuous` | `Continuous` | `Discontinuous` |
| **CC Offer Category** | `Negotiated` | `Public` | `Negotiated` |
| **CC Payment Interval** | `Monthly` | `One-Time` | `Monthly` |
| **CC Payment Model** | `No Upfront` | `All Upfront` | `Partial Upfront` |
| **CC Payment Upfront %** | `0.00` | `1.00` | `0.50` |
| **CC Period End** | `2028-12-01` | `2026-12-01` | `2027-01-15` |
| **CC Period Start** | `2025-12-01` | `2025-12-01` | `2026-01-15` |
| **CC Quantity** | `1000000.00` | `10.00` | `120000.00` |
| **CC Lifecycle Status** | `Active` | `Active` | `Pending` |
| **CC Type** | `Enterprise Agreement` | `Reserved Instance` | `SaaS Subscription` |
| **CC Unit** | `USD` | `Instance-Hours` | `Credits` |
| **Contract ID** | `AGR-99-BETA` | `AGR-99-BETA` | `AGR-99-BETA` |
| **Contract Period End** | `2028-12-01` | `2028-12-01` | `2028-12-01` |
| **Contract Period Start** | `2025-12-01` | `2025-12-01` | `2025-12-01` |
| **Invoice Issuer Name** | `Acme Co` | `Acme Co` | `Acme Co` |
| **Pricing Currency** | `USD` | `USD` | `USD` |
| **Pricing Currency CC Cost** | `1000000.00` | `50000.00` | `120000.00` |
| **Service Provider Name** | `Acme Co` | `Acme Co` | `DataStreamer` |

[CSV Example](../../data/contract_commitments/contract_commitment_scenario_1.csv)

### Scenario 2: SaaS Expansion & Hybrid Connector

In this scenario, an enterprise with an existing master agreement with **Acme Co** (`AGR-44-GAMMA`) expands its footprint to include specialized AI training and security licensing. This example highlights how the model handles non-financial units (Seats) and project-based burst windows.

#### Commitment 1: AI Model Training (Usage-based Burst)

* **Context:** A short-term, intensive commitment to a specific number of GPU-Hours for a specialized AI training run.
* **Commercial Logic:** A **Usage-based**, **Continuous** model with a short **3-Month** duration. It is paid **All Upfront** to secure priority capacity.
* **Eligibility:** Restricted to the `AI/ML` service category.

#### Commitment 2: Security Seat License (Quantity-based)

* **Context:** A commitment to **500 Seats** of an endpoint security platform.
* **Commercial Logic:** A **Quantity-based**, **Discontinuous** model. The unit of measure is **Seats** rather than a currency value.
* **Invoice/Provider Alignment:** Unlike the Marketplace example, this is billed directly by the vendor (**CyberGuard Inc**), yet remains logically associated with the broader Cloud Transformation contract.

#### Commitment 3: Cross-Cloud Data Connector (Tiered Usage)

* **Context:** A commitment based on **Data Volume (TB)** specifically for egress traffic between cloud providers.
* **Commercial Logic:** A **Usage-based**, **Continuous** model tracked on a **Monthly Fulfillment Interval**.
* **Eligibility:** Targeted specifically at `Egress` usage types via string-match logic in the Eligibility JSON.

### Data Example: AGR-44-GAMMA

| Column | Commitment 1: AI Training | Commitment 2: Security Seats | Commitment 3: Data Connector |
| :--- | :--- | :--- | :--- |
| **Billing Currency** | `USD` | `USD` | `USD` |
| **CC Benefit Category** | `Discount` | `Availability` | `Discount` |
| **CC Category** | `Usage` | `Usage` | `Usage` |
| **CC Cost** | `250000.00` | `120000.00` | `15000.00` |
| **CC Created** | `2026-02-01T08:00:00Z` | `2026-02-01T08:00:00Z` | `2026-02-01T08:00:00Z` |
| **CC Description** | `H100 GPU Reservation - Q1` | `CyberGuard Endpoint Seats` | `Inter-Cloud Egress Tier` |
| **CC Discount %** | `0.30` | `null` | `0.50` |
| **CC Duration Type** | `3 Months` | `1 Year` | `1 Year` |
| **CC Applicability** | `{"InclusionOperator": "Or", "Inclusions": [{"Dimension": "ServiceCategory", "Operator": "In", "Values": ["AI/ML"]}]}` | `{"IsGlobalScope": true}` | `{"InclusionOperator": "Or", "Inclusions": [{"Dimension": "UsageType", "Operator": "Contains", "Values": ["Egress"]}]}` |
| **CC Fulfillment Interval** | `Monthly` | `Annual` | `Monthly` |
| **CC ID** | `CMT-AI-888` | `CMT-SEC-999` | `CMT-DATA-111` |
| **CC Last Updated** | `2026-02-01T08:00:00Z` | `2026-02-01T08:00:00Z` | `2026-02-01T08:00:00Z` |
| **CC Model** | `Continuous` | `Discontinuous` | `Continuous` |
| **CC Offer Category** | `Negotiated` | `Negotiated` | `Public` |
| **CC Payment Interval** | `One-Time` | `Monthly` | `Monthly` |
| **CC Payment Model** | `All Upfront` | `No Upfront` | `No Upfront` |
| **CC Payment Upfront %** | `1.00` | `0.00` | `0.00` |
| **CC Period End** | `2026-05-01` | `2027-02-01` | `2027-02-01` |
| **CC Period Start** | `2026-02-01` | `2026-02-01` | `2026-02-01` |
| **CC Quantity** | `5000.00` | `500.00` | `100.00` |
| **CC Lifecycle Status** | `Active` | `Active` | `Active` |
| **CC Type** | `Capacity Reservation` | `SaaS Subscription` | `Usage Tier` |
| **CC Unit** | `GPU-Hours` | `Seats` | `Terabytes` |
| **Contract ID** | `AGR-44-GAMMA` | `AGR-44-GAMMA` | `AGR-44-GAMMA` |
| **Contract Period End** | `2029-02-01` | `2029-02-01` | `2029-02-01` |
| **Contract Period Start** | `2026-02-01` | `2026-02-01` | `2026-02-01` |
| **Invoice Issuer Name** | `Acme Co` | `CyberGuard Inc` | `Acme Co` |
| **Pricing Currency** | `USD` | `USD` | `USD` |
| **Pricing Currency CC Cost** | `250000.00` | `120000.00` | `15000.00` |
| **Service Provider Name** | `Acme Co` | `CyberGuard Inc` | `Acme Co` |

[CSV Example](../../data/contract_commitments/contract_commitment_scenario_2.csv)

### Scenario 3: Scale-Out & Overage

This scenario focuses on how the model handles growth beyond initial estimates. In the master agreement `AGR-11-DELTA`, the customer has established "safety nets" and tiered pricing to ensure that scale-out events are still covered by negotiated rates, even after a primary pool is exhausted.

#### Commitment 1 & 2: Database Storage Tiers (Base + Overage)

* **Context:** The customer commits to a base of 100TB of Database storage. To avoid "sticker shock" if they grow to 150TB, they have a pre-negotiated **Overage Tier**.
* **Commercial Logic:** Commitment 1 is the paid floor (`CC Cost: 50000.00`). Commitment 2 is a "Zero-Cost" commitment that exists solely to define the **CC Discount %** (10%) applied to any usage exceeding the first 100TB.
* **Eligibility:** Both rows target the same `Database` service category.

#### Commitment 3: CDN Annual (Volume Exhaustion)

* **Context:** An annual volume commitment of 1PB (1,000TB) for Content Delivery Network services.
* **Commercial Logic:** This is a **Discontinuous** model with an **Annual Fulfillment Interval**.
* **Overage Status:** Because the customer has already consumed their allotted volume before the `CC Period End`, the **CC Lifecycle Status** has shifted to `Exhausted`. This signals that the pool is empty and subsequent usage will be handled according to the contract's true-up or on-demand terms.

### Data Example: AGR-11-DELTA

| Column | Commitment 1: Base Storage | Commitment 2: Storage Overage | Commitment 3: CDN Annual |
| :--- | :--- | :--- | :--- |
| **Billing Currency** | `USD` | `USD` | `USD` |
| **CC Benefit Category** | `Discount` | `Discount` | `Monetary Pool` |
| **CC Category** | `Usage` | `Usage` | `Usage` |
| **CC Cost** | `50000.00` | `0.00` | `100000.00` |
| **CC Created** | `2026-02-01T08:00:00Z` | `2026-02-01T08:00:00Z` | `2026-02-01T08:00:00Z` |
| **CC Description** | `Base 100TB DB Storage` | `Tier 2 Storage Overage` | `1PB Annual CDN Volume` |
| **CC Discount %** | `0.20` | `0.10` | `0.25` |
| **CC Duration Type** | `1 Year` | `1 Year` | `1 Year` |
| **CC Applicability** | `{"InclusionOperator": "Or", "Inclusions": [{"Dimension": "ServiceCategory", "Operator": "In", "Values": ["Database"]}]}` | `{"InclusionOperator": "Or", "Inclusions": [{"Dimension": "ServiceCategory", "Operator": "In", "Values": ["Database"]}]}` | `{"InclusionOperator": "Or", "Inclusions": [{"Dimension": "ServiceCategory", "Operator": "In", "Values": ["CDN"]}]}` |
| **CC Fulfillment Interval** | `Monthly` | `Monthly` | `Annual` |
| **CC ID** | `CMT-STR-BASE` | `CMT-STR-OVER` | `CMT-CDN-VOL` |
| **CC Last Updated** | `2026-02-01T08:00:00Z` | `2026-02-01T08:00:00Z` | `2026-02-01T08:00:00Z` |
| **CC Model** | `Continuous` | `Continuous` | `Discontinuous` |
| **CC Offer Category** | `Negotiated` | `Negotiated` | `Negotiated` |
| **CC Payment Interval** | `Monthly` | `Monthly` | `One-Time` |
| **CC Payment Model** | `No Upfront` | `No Upfront` | `All Upfront` |
| **CC Payment Upfront %** | `0.00` | `0.00` | `1.00` |
| **CC Period End** | `2027-02-01` | `2027-02-01` | `2027-02-01` |
| **CC Period Start** | `2026-02-01` | `2026-02-01` | `2026-02-01` |
| **CC Quantity** | `100.00` | `0.00` | `1000.00` |
| **CC Lifecycle Status** | `Active` | `Active` | `Exhausted` |
| **CC Type** | `Usage Tier` | `Usage Tier` | `Volume Commitment` |
| **CC Unit** | `Terabytes` | `Terabytes` | `Terabytes` |
| **Contract ID** | `AGR-11-DELTA` | `AGR-11-DELTA` | `AGR-11-DELTA` |
| **Contract Period End** | `2029-02-01` | `2029-02-01` | `2029-02-01` |
| **Contract Period Start** | `2026-02-01` | `2026-02-01` | `2026-02-01` |
| **Invoice Issuer Name** | `Acme Co` | `Acme Co` | `Acme Co` |
| **Pricing Currency** | `USD` | `USD` | `USD` |
| **Pricing Currency CC Cost** | `50000.00` | `0.00` | `100000.00` |
| **Service Provider Name** | `Acme Co` | `Acme Co` | `Acme Co` |

[CSV Example](../../data/contract_commitments/contract_commitment_scenario_3.csv)
