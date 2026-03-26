# Appendix

*This section is non-normative.*

## Appendix Entries<!--SkipTOC-->

| Topic | Description |
| :--- | :--- |
| [Commitment Discounts](#appendix.commitmentdiscounts) | Explains the purchasing, usage, and amortization of commitment discounts in a FOCUS dataset. |
| [Examples: Commitment Discount Flexibility](#appendix.examples:commitmentdiscountflexibility) | Demonstrates scenarios for usage-based commitment discounts with and without commitment discount flexibility. |
| [Examples: Contract Commitments](#appendix.examples:contractcommitments) | Provides a structured representation and examples of commercial agreements between a customer and their service providers. |
| [Examples: JSON Object](#appendix.examples:jsonobject) | Provides examples for columns using the JSON Object Format, such as Contract Commitment Applicability. |
| [Examples: Invoice Detail](#appendix.examples:invoicedetail) | Demonstrates scenarios for issuing invoices, including typical cloud invoices, multi-currency settlements, and billing error corrections. |
| [Examples: Metadata](#appendix.examples:metadata) | Contains JSON payload examples for updating Data Generator, Dataset, Schema, and Recency metadata. |
| [Examples: Participating Entity Identification](#appendix.examples:participatingentityidentification) | Illustrates how to identify the roles of participating entities (e.g., Service Provider, Invoice Issuer, Host Provider, Data Generator) across various supply chain scenarios. |
| [Examples: SaaS](#appendix.examples:saas) | Illustrates how to model SaaS billing scenarios, including simple SaaS agreements, SaaS spend agreements, and virtual currency pricing models. |
| [Grouping Constructs for Resources or Services](#appendix.groupingconstructsforresourcesorservices) | Outlines and compares the two distinct levels of resource or service grouping mechanisms supported by FOCUS: billing accounts and sub accounts. |                                                      |

## Fictitious Data Generator Reference

To illustrate how FOCUS normalizes the presentation of data across diverse technology environments, the appendix uses a standardized set of fictitious data generators. These represent common architectural components, ranging from core cloud infrastructure to SaaS platforms. Using these examples demonstrates cross-vendor cost allocation, standardized billing schemas, and multi-cloud reporting without relying on proprietary vendor data.

Disclaimer: *The fictitious data generators referenced in this appendix are intended solely for illustrative purposes to resemble real-world services. They do not reflect, represent, or imply the actual current or future FOCUS implementations, billing schemas, or data formats of any real-world companies or equivalents listed herein.*

The table below outlines the fictitious data generators used throughout the appendix, their primary functions, and their real-world counterparts for context:

| Fictitious Data Generator | Service Offering | Quick Description | Real-World Equivalents |
| :--- | :--- | :--- | :--- |
| **Nexus Web** | Cloud Service Provider | A highly scalable, market-leading cloud infrastructure provider offering extensive compute, storage, and serverless options. | Amazon Web Services (AWS) |
| **Zenith** | Cloud Service Provider | An enterprise-focused cloud platform with deep integrations into existing corporate software ecosystems and directory services. | Microsoft Azure |
| **Meridian** | Cloud Service Provider | A cloud provider heavily optimized for machine learning, data analytics, and containerized Kubernetes workloads. | Google Cloud Platform (GCP) |
| **ClearQuery** | Data Platform | A centralized hub for storing, processing, and analyzing massive datasets to drive business intelligence. | Snowflake, Databricks |
| **WatchTower** | SaaS Observability | A monitoring tool that tracks application performance, logs, and system health in real-time to prevent downtime. | Datadog, New Relic |
| **TaskBoard** | Project Management | A collaborative workspace for planning, assigning, and tracking team tasks and agile workflows. | Jira, Asana, Trello |
| **CloudDB** | Database as a Service | A fully managed, scalable cloud database solution that handles provisioning, backups, and routine maintenance. | MongoDB Atlas |
| **TeamSpace** | Team Communications | A messaging platform offering organized chat channels, direct messaging, and secure file sharing for remote teams. | Slack |
| **QuickSend** | Email API | A developer-friendly service for reliably routing, sending, and tracking both transactional and marketing emails. | SendGrid, Mailgun |
| **GrowthCRM** | CRM | A customer relationship management platform designed to track sales pipelines, manage contacts, and optimize lead conversion. | Salesforce, HubSpot |
