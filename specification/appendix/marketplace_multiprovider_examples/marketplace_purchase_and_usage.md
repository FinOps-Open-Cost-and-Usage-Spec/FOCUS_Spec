# Marketplace Purchase and Usage Example

This section is non-normative.

## Scenario

A customer purchases an annual Datadog Pro subscription through AWS Marketplace. This generates two separate FOCUS billing records: a purchase record from AWS and a usage record from Datadog. This example illustrates how `BilledCost` and `EffectiveCost` are populated by each provider, and how the two records can be correlated using `ResourceId` and `InvoiceId`.

## Purchase Provider (AWS Marketplace)

AWS records the marketplace transaction as a purchase charge. Because AWS does not have access to Datadog's consumption data, `EffectiveCost` is 0 on this row. Per the `EffectiveCost` column definition, `EffectiveCost` is 0 when `ChargeCategory` is `Purchase` and the purchase is intended to cover future eligible charges. `BilledCost` reflects the full contracted amount invoiced to the customer.

## Usage Provider (Datadog)

Datadog records the actual usage consumed against the subscription. Because the customer's payment flows through AWS Marketplace rather than directly to Datadog, `BilledCost` is 0 on this row. Per the `BilledCost` column definition, `BilledCost` is 0 for charges where payment is received by a third party. `EffectiveCost` reflects actual consumption for the billing period. Because the invoice is issued by AWS, `InvoiceIssuerName` is "Amazon Web Services" on the Datadog record, and `InvoiceId` matches the AWS invoice.

## Dataset Notes

Note the following details in the example datasets:

- **Charge Period and Billing Period Alignment:** The AWS purchase record has `ChargePeriodStart` of April 1, 2025 and `ChargePeriodEnd` of April 1, 2026, representing the full annual subscription term. `BillingPeriodStart` and `BillingPeriodEnd` cover April 2025, reflecting when the purchase was invoiced. The Datadog usage record has a `ChargePeriodEnd` of May 1, 2025, reflecting a single month of consumption within the subscription term. This distinction enables time-based correlation between the two records.
- **ResourceId for Correlation:** Both records carry the same `ResourceId` value (`mp-sub-dd-pro-2025-04`). This shared identifier is the primary mechanism for linking the CSP purchase record to the SaaS usage record. Practitioners should ensure this value is consistently applied at subscription onboarding time.
- **Shared InvoiceIssuerName and InvoiceId:** Because the customer's payment flows through AWS, both records carry `InvoiceIssuerName` = "Amazon Web Services" and the same `InvoiceId`. This reflects the FOCUS entity identification pattern for marketplace scenarios where the SaaS provider does not issue a separate invoice to the customer.
- **BilledCost and EffectiveCost are not additive across providers:** The AWS `BilledCost` of $10,000 represents a cash-basis recording of the annual contract. The Datadog `EffectiveCost` of $8,245 represents an accrual-basis recording of actual April consumption. These figures describe different accounting perspectives on the same subscription and should not be summed in a unified view without additional reconciliation logic.

## Example Data

See the full datasets:

- [AWS purchase record](../../data/marketplace_multiprovider_examples/marketplace_m1_aws.csv)
- [Datadog usage record](../../data/marketplace_multiprovider_examples/marketplace_m1_datadog.csv)
- [Combined view across all providers](../../data/marketplace_multiprovider_examples/marketplace_m2_combined.csv)
