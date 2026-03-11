# Marketplace Multi-Provider Scenario Guidance

This section is non-normative.

## Overview

In multi-provider marketplace scenarios, billing data may originate from different data generators. For example, a Cloud Service Provider (CSP) might handle the purchase transaction, while a Software-as-a-Service (SaaS) provider generates usage records. This guidance clarifies how FOCUS columns, particularly EffectiveCost, should be populated in such cases.

This guidance addresses the data accuracy concerns outlined in the parent issue [FR] Clarify definitions of EffectiveCost vs BilledCost across providers [#982](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/982), which reframes the problem from "double counting" to providers populating inaccurate EffectiveCost values when lacking actual usage information. It provides scenario-based guidance for marketplace purchases as specified in Milestone 3 of #982.
## Provider Responsibility Matrix

| Scenario | Purchase Provider | Usage Provider | EffectiveCost Population |
|----------|-------------------|----------------|--------------------------|
| CSP Marketplace (CSP as invoice issuer) | CSP | CSP | CSP populates based on actual usage |
| Third-party SaaS via Marketplace (SaaS as usage provider) | CSP | SaaS | SaaS populates based on actual usage; CSP does not estimate |
| Cross-provider | CSP | SaaS | Only provider with actual usage data populates EffectiveCost |

## Key Principles

### CSP Responsibilities
- **Purchase Record Without Usage Details**: When a CSP handles the purchase but not the usage, EffectiveCost on the purchase row is 0. Per the EffectiveCost column definition, EffectiveCost is 0 when ChargeCategory is "Purchase" and the purchase covers future eligible charges.

### SaaS Provider Responsibilities
- **Usage Details Without Purchase Record**: EffectiveCost reflects actual usage.
  - Rationale: SaaS providers have direct access to consumption metrics.
  - Usage: Populate EffectiveCost based on service-specific data like API calls or data ingested.

### Aggregation Behavior
- **Cross-Provider Aggregations Will NOT Match**: This is expected behavior, not an error.
  - Rationale: Supports #982's cross-cutting criteria for when aggregations will NOT match in cross-provider marketplace scenarios.
  - Usage: Practitioners should account for this in reporting and analysis.

### General Rule
- **EffectiveCost Population**: Only the provider with actual usage data should populate EffectiveCost.
  - Rationale: Ensures data accuracy and prevents double-counting or estimation errors.

## Examples

### AWS Marketplace Example

In [AWS Marketplace](https://aws.amazon.com/marketplace/), customers can browse and purchase third-party software solutions directly integrated with AWS services. AWS facilitates the entire purchase process, from discovery to invoicing, and consolidates charges into the customer's AWS bill. However, for SaaS offerings, AWS does not track or report on the actual usage of the software; that responsibility falls to the SaaS provider (e.g., Datadog, Grafana, New Relic).

AWS Marketplace supports various pricing models, including upfront payments, hourly rates, and annual contracts, but usage data is always sourced from the SaaS vendor. This separation ensures AWS focuses on infrastructure billing, while SaaS providers handle service-specific metrics.

#### Scenario Description
A customer purchases monitoring subscriptions (Datadog or Grafana) through AWS Marketplace. AWS handles the billing and invoicing, appearing as a line item in the AWS Cost and Usage Report (CUR). The SaaS providers (Datadog/Grafana) provide the actual usage data separately, reflecting metrics like log ingestion, API calls, or active series.

#### FOCUS Dataset Population
- **BilledCost**: Populated by AWS with the total marketplace purchase amount (e.g., $10,000.00), including any fees or taxes.
- **EffectiveCost**: Not populated by AWS (empty in AWS dataset); populated by Datadog in their separate dataset with actual usage-based costs.
- **ResourceId**: Unique marketplace identifier (e.g., marketplace-123) for correlation.
- **ChargeCategory**: "Purchase" for the marketplace transaction.
- **ServiceName**: "AWS Marketplace" for the billing entry.
- **InvoiceIssuerName**: "AWS Marketplace" indicating AWS as the invoice issuer.

Detailed considerations include:
- AWS (Purchase Provider): Handles the marketplace transaction, populates BilledCost in AWS Cost and Usage Reports (CUR), and includes any AWS marketplace fees or taxes. EffectiveCost is not populated, as AWS lacks access to SaaS usage details.
- SaaS Provider (e.g., Datadog): Delivers usage reports through their own dashboards or APIs, populating EffectiveCost with actual consumption data like ingested logs, API requests, or active users.
- Integration Features: AWS Marketplace integrates with AWS Organizations, Service Catalog, and Cost Allocation Tags for governance. Correlation can use AWS Resource Tags or Account IDs shared between providers.
- Billing Mechanics: Charges appear in the AWS invoice under "Marketplace" line items, with usage potentially reported separately by the SaaS provider.

For comprehensive guidance, see [AWS Marketplace billing and invoicing](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-paying-for-products.html) and [AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html). For FOCUS dataset examples, see the [Marketplace Multi-Provider Examples](/specification/appendix/marketplace_multiprovider_examples/marketplace_multiprovider_examples.mdpp), including CSV samples like [AWS Purchase Data](/specification/data/marketplace_multiprovider_examples/marketplace_m1_aws.csv).

### Azure Marketplace Example

In [Azure Marketplace](https://azure.microsoft.com/en-us/marketplace/), customers can procure third-party software solutions directly through the Azure portal. Azure acts as the intermediary for purchases, handling transactions, invoicing, and payment processing. However, the actual SaaS providers (e.g., Datadog, Grafana) are responsible for delivering usage metrics and performance data.

Azure's marketplace billing integrates with Azure Cost Management, but usage details are sourced from the SaaS vendor's systems. This separation ensures that Azure focuses on infrastructure and billing consolidation, while SaaS providers maintain control over their service-specific data.

#### Scenario Description
A customer subscribes to Datadog through Azure Marketplace. Azure processes the purchase and includes it in the Azure billing export. Datadog separately reports usage metrics, such as monitored hosts or ingested data volumes.

#### FOCUS Dataset Population
- **BilledCost**: Populated by Azure with the marketplace purchase cost, reflecting the invoiced amount.
- **EffectiveCost**: Not populated by Azure (empty in Azure dataset); populated by Datadog with usage-based effective costs.
- **ResourceId**: Azure-specific resource identifier for the marketplace item.
- **ChargeCategory**: "Purchase" for the transaction.
- **ServiceName**: "Azure Marketplace" in billing exports.
- **InvoiceIssuerName**: "Microsoft" or "Azure" as the invoice issuer.

Key aspects include:
- Azure (Purchase Provider): Manages the marketplace transaction, populates BilledCost in Azure billing exports, and may include marketplace fees. EffectiveCost is not populated as Azure lacks granular usage insights.
- SaaS Provider (e.g., Datadog): Provides detailed usage reports via their own APIs or exports, populating EffectiveCost based on actual consumption metrics like API calls, data ingested, or user activity.
- Integration Points: Azure Resource Manager (ARM) templates often facilitate deployment, and Azure Monitor can correlate with SaaS telemetry, but FOCUS datasets require manual correlation using fields like SubscriptionId or ResourceGroup.

For more on Azure Marketplace billing, see [Azure Marketplace purchasing](https://learn.microsoft.com/en-us/marketplace/azure-purchasing-invoicing) and [Azure Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/). For FOCUS dataset examples illustrating multi-provider scenarios, see the [Marketplace Multi-Provider Examples](/specification/appendix/marketplace_multiprovider_examples/marketplace_multiprovider_examples.mdpp), including CSV samples like [Azure Purchase Data](/specification/data/marketplace_multiprovider_examples/marketplace_m1_azure.csv).

### GCP Marketplace Example

[Google Cloud Marketplace](https://cloud.google.com/marketplace/docs/overview) allows customers to discover, purchase, and deploy third-party software on Google Cloud. GCP handles the commercial aspects, including pricing, invoicing, and billing integration with Google Cloud Billing. SaaS providers (e.g., Datadog, Grafana) manage the operational delivery, including usage tracking and reporting.

GCP's marketplace emphasizes seamless integration with Google Cloud services, but usage data remains with the SaaS provider. This model supports complex deployments where GCP provides the underlying infrastructure, and SaaS adds value through specialized tools.

#### Scenario Description
A customer deploys Datadog via Google Cloud Marketplace. GCP bills for the marketplace purchase in Cloud Billing exports. Datadog reports actual usage, such as data processing volumes or API usage.

#### FOCUS Dataset Population
- **BilledCost**: Populated by GCP with the marketplace cost, including surcharges.
- **EffectiveCost**: Not populated by GCP (empty in GCP dataset); populated by Datadog with effective usage costs.
- **ResourceId**: GCP project or resource identifier.
- **ChargeCategory**: "Purchase" for the transaction.
- **ServiceName**: "Google Cloud Marketplace" in billing.
- **InvoiceIssuerName**: "Google" as the issuer.

Detailed considerations:
- GCP (Purchase Provider): Records the marketplace purchase in Cloud Billing exports, populating BilledCost with any applicable marketplace surcharges or discounts. EffectiveCost is not included, as GCP does not monitor SaaS-specific usage.
- SaaS Provider (e.g., Datadog, Grafana): Supplies usage data through their platforms, populating EffectiveCost with metrics tailored to their service (e.g., log volume, query counts). Billing may be separate or integrated via GCP's billing APIs.
- Advanced Features: GCP Marketplace supports private offers and custom pricing, which can complicate FOCUS population. Correlation can leverage Google Cloud Project IDs or BigQuery exports for unified views.
- Documentation: Refer to [GCP Marketplace billing](https://cloud.google.com/marketplace/docs/billing) and [Cloud Billing reports](https://cloud.google.com/billing/docs/how-to/reports) for integration details. For detailed FOCUS dataset examples, see the [Marketplace Multi-Provider Examples](/specification/appendix/marketplace_multiprovider_examples/marketplace_multiprovider_examples.mdpp), including CSV samples like [GCP Purchase Data](/specification/data/marketplace_multiprovider_examples/marketplace_m1_gcp.csv).

These examples highlight provider-specific nuances in marketplace transactions, ensuring accurate FOCUS dataset handling.

For detailed FOCUS dataset examples illustrating these scenarios, see the [Marketplace Multi-Provider Examples](/specification/appendix/marketplace_multiprovider_examples/marketplace_multiprovider_examples.mdpp).

## Correlation Approach for Practitioners

Practitioners can correlate data using common identifiers such as:

- **ResourceId**: Links resources across providers (e.g., AWS instance ID or Azure resource ID).
- **ChargeId**: Unique identifier for charges, useful for matching line items.
- **InvoiceId** (where available): Ties back to billing documents.

For examples, refer to the CSV datasets in [Marketplace Multi-Provider Examples](/specification/appendix/marketplace_multiprovider_examples/marketplace_multiprovider_examples.mdpp), where ResourceId and ChargeId are populated to demonstrate correlation in multi-provider scenarios.

Note: Correlation may require additional metadata or external systems. For more details on FOCUS columns, see the [FOCUS Column Library](https://focus.finops.org/focus-columns/). Reference the parent issue for this guidance: [FR] Clarify definitions of EffectiveCost vs BilledCost across providers [#982](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/982).

## Cross-Provider Aggregation Mismatch

When aggregating data from multiple providers, totals may not match due to different data sources. This is expected behavior, not an error, as confirmed by provider documentation (e.g., [AWS Marketplace Billing](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-paying-for-products.html), [Azure Marketplace](https://azure.microsoft.com/en-us/marketplace/), [GCP Marketplace](https://cloud.google.com/marketplace/docs/overview)).

### Addressing Aggregation Mismatches

Practitioners can address mismatches through the following approaches:

1. **Correlation and Matching**: Use shared identifiers (e.g., ResourceId, ChargeId) to link purchase records from CSPs with usage records from SaaS providers. This may require custom ETL processes or third-party tools.
2. **Separate Reporting**: Report CSP and SaaS data separately, with clear labels indicating the source, to avoid misleading aggregations.
3. **Reconciliation Processes**: Implement manual or automated reconciliation workflows to account for discrepancies, such as comparing invoice totals against usage-based calculations.
4. **Provider Communication**: Contact providers for additional metadata or clarification on how their billing data relates.
5. **Documentation and Disclaimers**: Include disclaimers in reports noting that cross-provider totals may not match due to data source differences.

This guidance is supported by provider practices where CSPs handle transactions but SaaS providers deliver usage data, leading to potential mismatches in unified views.
This guidance is supported by provider practices where CSPs handle transactions but SaaS providers deliver usage data, leading to potential mismatches in unified views.

## Validation

This guidance has been validated with implementations from Datadog, Grafana, and Neos using the [FOCUS Validator](https://github.com/finopsfoundation/focus_validator). The CSV examples in the [Marketplace Multi-Provider Examples](/specification/appendix/marketplace_multiprovider_examples/marketplace_multiprovider_examples.mdpp) have been tested against the FOCUS specification to ensure compliance.

For the full FOCUS specification and column definitions, see [focus.finops.org](https://focus.finops.org).

