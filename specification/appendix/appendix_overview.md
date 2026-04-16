# Appendix

*This section is informative. It illustrates the application of normative rules defined elsewhere in this specification and does not introduce additional requirements.*

## Appendix Entries<!--SkipTOC-->

| Topic | Description |
| :--- | :--- |
| [Commitment Discounts](#appendix.commitmentdiscounts) | Explains the purchasing, usage, and amortization of commitment discounts in a FOCUS dataset. |
| [Discount Handling](#appendix.discounthandling) | Explains how discounts are represented and applied to charges in a FOCUS dataset. |
| [Examples: Commitment Discount Flexibility](#appendix.examples:commitmentdiscountflexibility) | Demonstrates scenarios for usage-based commitment discounts with and without commitment discount flexibility. |
| [Examples: Commitment Program Eligibility Details](#appendix.examples:commitmentprogrameligibilitydetails) | Demonstrates how commitment program eligibility details interact with capacity reservation columns for capacity reservation programs. |
| [Examples: Contract Commitments](#appendix.examples:contractcommitments) | Provides a structured representation and examples of commercial agreements between a customer and their service providers. |
| [Examples: Invoice Detail](#appendix.examples:invoicedetail) | Demonstrates scenarios for issuing invoices, including typical cloud invoices, multi-currency settlements, and billing error corrections. |
| [Examples: JSON Object](#appendix.examples:jsonobject) | Provides examples for columns using the JSON Object Format, such as Contract Commitment Applicability. |
| [Examples: Metadata](#appendix.examples:metadata) | Contains JSON payload examples for updating Data Generator, Dataset, Schema, and Recency metadata. |
| [Examples: Participating Entity Identification](#appendix.examples:participatingentityidentification) | Illustrates how to identify the roles of participating entities (e.g., Service Provider, Invoice Issuer, Host Provider, Data Generator) across various supply chain scenarios. |
| [Examples: SaaS](#appendix.examples:saas) | Illustrates how to model SaaS billing scenarios, including simple SaaS agreements, SaaS spend agreements, and virtual currency pricing models. |
| [Grouping Constructs for Resources or Services](#appendix.groupingconstructsforresourcesorservices) | Outlines and compares the two distinct levels of resource or service grouping mechanisms supported by FOCUS: billing accounts and sub accounts. |
| [Invoice and Billing Period Handling](#appendix.invoiceandbillingperiodhandling) | Outlines invoice reconciliation, invoice issuance, and open vs. closed billing periods across FOCUS datasets, including correction handling. |
| [Rounding Variance Tolerance](#appendix.roundingvariancetolerance) | Defines the statistical tolerance formula and provides scenarios for handling precision differences during invoice reconciliation between detailed cost data and invoices. |

## Fictitious Data Generator Reference

To illustrate how FOCUS normalizes the presentation of data across diverse technology environments, the appendix uses a standardized set of fictitious [*data generators*](#metadata.datagenerator). These represent common architectural components, ranging from core cloud infrastructure to SaaS platforms. Using these examples demonstrates cross-vendor cost allocation, standardized billing schemas, and multi-cloud reporting without relying on proprietary vendor data.

Disclaimer: *The fictitious entities (data generators, customers, and commitment programs) referenced in this appendix are intended solely for illustrative purposes to resemble real-world services and organizations. They do not reflect, represent, or imply the actual current or future FOCUS implementations, billing schemas, or data formats of any real-world companies or equivalents listed herein.*

The table below outlines the fictitious *data generators* used throughout the appendix, their primary functions, and their real-world counterparts for context:

| Fictitious Data Generator | Service Offering | Fictitious Data Generator Description | Similar Real-World Examples |
| :--- | :--- | :--- | :--- |
| **Aura Web** | Cloud Service Provider | A highly scalable, market-leading cloud infrastructure provider offering extensive compute, storage, and serverless options. | Amazon Web Services (AWS) |
| **CrestNode** | Cloud Service Provider | An enterprise-focused cloud platform with deep integrations into existing corporate software ecosystems and directory services. | Microsoft Azure |
| **LatticeScale** | Cloud Service Provider | A cloud provider heavily optimized for machine learning, data analytics, and containerized Kubernetes workloads. | Google Cloud Platform (GCP) |
| **OmniQuery** | Data Platform | A centralized hub for storing, processing, and analyzing massive datasets to drive business intelligence. | Snowflake, Databricks |
| **StackLens** | SaaS Observability | A monitoring tool that tracks application performance, logs, and system health in real-time to prevent downtime. | Datadog, New Relic |
| **SprintCanvas** | Project Management | A collaborative workspace for planning, assigning, and tracking team tasks and agile workflows. | Jira, Asana, Trello |
| **StoreStack** | Database as a Service | A fully managed, scalable cloud database solution that handles provisioning, backups, and routine maintenance. | MongoDB Atlas |
| **CollabChat** | Team Communications | A messaging platform offering organized chat channels, direct messaging, and secure file sharing for remote teams. | Slack |
| **PulseMail** | Email API | A developer-friendly service for reliably routing, sending, and tracking both transactional and marketing emails. | SendGrid, Mailgun |
| **PipelCRM** | CRM | A customer relationship management platform designed to track sales pipelines, manage contacts, and optimize lead conversion. | Salesforce, HubSpot |
| **Budget Beacon** | Cost Management | A cloud cost-optimization platform that shines a spotlight on overspending, waste, and savings opportunities across multi-cloud environments. | Cloudability, CloudHealth, ProsperOps |
| **SchemaWeaver** | Open Source Library | An open-source tool that refines raw cloud cost and usage data, normalizing it into FOCUS-compliant schemas for downstream analytics and reporting. Not a public service. | OpenCost, Cloud Intelligence Dashboards, FinOps toolkit |

## Fictitious Customer Reference

To contextualize the billing and cost allocation examples, this appendix utilizes fictitious customer profiles. These profiles represent common organizational structures and cloud adoption patterns.

| Fictitious Customer | Company Profile | Customer Description |
| :--- | :--- | :--- |
| **Acme Corp** | Large Enterprise | A traditional multinational corporation undergoing a major cloud transformation. They manage a complex, hybrid multi-cloud environment with strict regulatory and compliance requirements. |
| **AeroScale** | Cloud-Native Startup | A fast-growing tech startup operating entirely in the cloud. They heavily utilize serverless architectures, managed databases, and agile deployment pipelines. |
| **GearPeak Outdoors** | Mid-Market Retailer | An outdoor apparel and equipment brand with massive seasonal traffic spikes. They leverage auto-scaling infrastructure for their e-commerce storefront and a heavy mix of SaaS for supply chain and CRM. |

## Fictitious Commitment Program Reference

To illustrate commitment program application and amortization without relying on vendor-specific terminology, the examples in this appendix use standardized fictitious commitment instruments. These constructs abstract the common commitment mechanisms used by major cloud and SaaS providers.

| Fictitious Commitment Program | Abbr. | Category | Fictitious Commitment Program Description | Similar Real-World Programs |
| :--- | :--- | :--- | :--- | :--- |
| **Resource Reservations** | RR | Usage | An upfront commitment to use a specific resource type, family, and region for a set term (e.g., 1 or 3 years) in exchange for a significantly reduced hourly rate. | Reserved Instances (AWS/Azure), Resource-based CUDs (GCP) |
| **Flexible Spend Plans** | FSP | Spend | A commitment to spend a specific monetary amount per hour across a broad category of compute or service offerings, providing high flexibility as workloads shift. | Savings Plans (AWS) |
| **Dynamic Compute Commitments** | DCC | Spend | A spend-based commitment covering aggregate compute resources (such as vCPU and memory) across multiple regions and machine families, converting the hourly spend into a usage discount. | Flexible CUDs (GCP) |
| **Enterprise Spend Agreements** | ESA | Spend | An overarching, contractual agreement where an organization commits to a minimum aggregate spend across a provider's portfolio over a set term (e.g., 1-3 years) in exchange for a blanket percentage discount. | Enterprise Discount Programs (AWS), MACC (Azure) |
| **Interval Spend Commitments** | ISC | Spend | A recurring minimum-spend or minimum-usage agreement at fixed intervals (e.g., monthly, annual), common among SaaS observability and infrastructure monitoring providers. Program names inherently include the period reference. | Monthly/Annual Commitments (Datadog) |
| **Bulk Capacity Credits** | BCC | Spend | A pre-purchased pool of platform-specific credits or capacity units, consumed against usage over a contract period. Common among data and analytics platforms. | Capacity Commitments (Snowflake), Committed Use Discounts (Databricks) |
| **Advance Resource Commitments** | ARC | Usage | An advance reservation of specific compute capacity in a region or availability zone, guaranteeing resource availability without necessarily providing a unit discount. Distinct from Resource Reservations, which are commitment discounts. | Capacity Reservations (AWS), On-demand Capacity Reservations (Azure), Zonal reservations (GCP) |
