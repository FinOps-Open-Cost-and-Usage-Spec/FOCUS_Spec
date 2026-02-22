# Marketplace Purchase and Usage Examples

Many marketplace transactions involve multiple providers, where Cloud Service Providers (CSPs) handle purchases and invoicing, while Software-as-a-Service (SaaS) providers supply usage data. This leads to scenarios where FOCUS datasets from different providers must be correlated and combined for accurate cost analysis.

The scenarios described below illustrate how a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) should be populated in marketplace multi-provider scenarios. These examples highlight the separation of responsibilities and provide guidance on handling data from disparate sources.

## Scenario M1: CSP Marketplace Purchase with SaaS Usage (Upfront Purchase Model)

CloudTech Solutions decides to purchase a SaaS monitoring tool (Datadog) through AWS Marketplace for a 12-month term starting April 1st, 2025. AWS Marketplace facilitates the transaction, consolidates billing, and issues the invoice for $10,000. However, AWS does not track or provide detailed usage metrics for Datadog's service. Datadog separately provides usage-based reports to CloudTech Solutions, reflecting actual consumption.

In this upfront purchase model, the entire cost is billed at the start, but usage is realized over time. Practitioners need to correlate AWS's purchase record with Datadog's usage data to understand true cost allocation.

- **Purchase Provider (AWS):** Records the marketplace transaction as a one-time charge, populating BilledCost and related purchase fields.
- **Usage Provider (Datadog):** Records ongoing usage, populating EffectiveCost and consumption metrics.

[**CSV Example - AWS Purchase**](/specification/data/marketplace_multiprovider_examples/marketplace_m1_aws.csv)  
[**CSV Example - Datadog Usage**](/specification/data/marketplace_multiprovider_examples/marketplace_m1_datadog.csv)  
[**CSV Example - Grafana Usage**](/specification/data/marketplace_multiprovider_examples/marketplace_m1_grafana.csv)

Note the following details in the example datasets:

* **Charge Period and Billing Period Alignment:** Both records share the same ChargePeriodStart (April 1st, 2025) and ChargePeriodEnd (April 1st, 2026), representing the service term. The BillingPeriodStart/End (April 2025) reflects when the purchase was invoiced. This alignment enables time-based correlation.
* **BilledCost Population:** In the AWS dataset, BilledCost is $10,000, representing the full invoiced amount. ListCost and ContractedCost are also $10,000, as there are no discounts. EffectiveCost is empty because AWS lacks usage details.
* **EffectiveCost Population:** In the Datadog/Grafana datasets, EffectiveCost is $10,000, reflecting the actual cost based on usage (1000 GB for Datadog, 5000 active series for Grafana). BilledCost is empty since the SaaS providers do not issue the invoice. This separation prevents double-counting in aggregated views.
* **ChargeCategory and ChargeClass:** AWS uses "Purchase" and "Standard" to indicate a marketplace acquisition. Datadog/Grafana use "Usage" and "Standard" for consumption-based charges.
* **Consumption Metrics:** Datadog populates ConsumedQuantity (1000) and ConsumedUnit (GB), along with PricingQuantity (1000) and PricingUnit (GB), showing how usage drives the cost. Grafana uses Active Series as the consumption metric, reflecting their billing model based on time series data. AWS leaves these empty as it doesn't track usage.
* **Provider Identification:** ServiceProviderName is "AWS" for the purchase record and "Datadog"/"Grafana" for the usage record. InvoiceIssuerName is "AWS Marketplace" for the billed record, highlighting the invoicing entity.
* **Correlation Fields:** ResourceId ("marketplace-123" in AWS, "resource-456" in Datadog, "resource-789" in Grafana) serves as a key identifier. In practice, providers might use shared marketplace transaction IDs (if available) or external mapping.
* **Practitioner Implications:** When combining these datasets, sum BilledCost from AWS and EffectiveCost from Datadog/Grafana for total spend. Discrepancies may arise if usage exceeds the purchased amount or if there are adjustments.

## Scenario M2: Cross-Provider Aggregation Mismatch (Combined Reporting Challenge)

Building on Scenario M1, CloudTech Solutions attempts to create a unified cost report by aggregating data from AWS Marketplace and Datadog usage data. While the totals match in this simple example, real-world scenarios often show mismatches due to timing differences, partial data, or provider-specific calculations.

The combined dataset demonstrates how records from multiple providers appear together, emphasizing the need for careful correlation to avoid erroneous aggregations.

[**CSV Example - Combined View**](/specification/data/marketplace_multiprovider_examples/marketplace_m2_combined.csv)

Note the following details in the example dataset:

* **Record Separation:** The dataset includes two distinct records—one from AWS (BillingAccountId: 12345) and one from Grafana (BillingAccountId: 67890)—reflecting separate provider accounts. BillingAccountName ("CloudTechDemo") is consistent for organizational correlation.
* **Cost Fields:** BilledCost ($10,000 from AWS) represents the invoiced amount, while EffectiveCost ($10,000 from Grafana) represents the realized cost. In mismatched scenarios, these might differ (e.g., BilledCost could be $10,000, but EffectiveCost $9,500 due to unused credits).
* **Charge Descriptions:** AWS describes it as "Marketplace purchase for SaaS service," while Grafana uses "Usage-based charges for Grafana Cloud metrics monitoring," providing context for each record's origin.
* **Aggregation Challenges:** Summing BilledCost across providers gives the total invoiced ($10,000), but summing EffectiveCost shows actual consumption. Practitioners should reconcile using ResourceId or ChargePeriod to identify related records.
* **Common Mismatch Causes:** Delays in usage reporting, currency conversions, or provider-specific tax handling can lead to discrepancies. For example, if Grafana reports usage a month late, EffectiveCost might not align with BilledCost periods.
* **Best Practices:** Use tools for cross-provider matching, include disclaimers in reports about potential mismatches, and validate totals against invoices. This scenario underscores that multi-provider data is not always additive without reconciliation.