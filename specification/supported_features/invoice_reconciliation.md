# Invoice Reconciliation

## Description

FOCUS supports the reconciliation of granular cloud consumption records with the formal financial documents issued by an invoice issuer. The [Invoice Detail](#datasets.invoicedetail) dataset represents the definitive financial record of [*charges*](#glossary:charges) as they appear on an invoice. By leveraging common identifiers, practitioners can map usage-based costs in the [Cost and Usage](#datasets.costandusage) dataset back to their corresponding line items in the [Invoice Detail](#datasets.invoicedetail) dataset.

This feature also supports reconciliation across divergent currency grains. When an invoice issuer represents billing and payment currencies at different aggregation levels, the `PaymentCurrencyInvoiceDetailId` provides the necessary lineage to link granular usage records to the aggregate records used for financial settlement.

## Directly Dependent Columns

* [InvoiceDetail](#datasets.invoicedetail)
  * BilledCost
  * InvoiceId
  * InvoiceDetailId
  * PaymentCurrencyBilledCost
  * PaymentCurrencyInvoiceDetailId
* [CostAndUsage](#datasets.costandusage)
  * BilledCost
  * InvoiceId
  * InvoiceDetailId

## Supporting Columns

* [InvoiceDetail](#datasets.invoicedetail)
  * BillingCurrency
  * ChargeCategory
  * InvoiceIssueStatus
  * PaymentCurrency
* [CostAndUsage](#datasets.costandusage)
  * ChargeCategory
  * ServiceCategory

## Example SQL Queries

Reconciliation often requires aggregating granular usage data to match the coarser grain of an invoice. The following queries demonstrate how to validate that usage records match the billed amounts on a legal invoice.

### Reconcile Cost and Usage to Invoice Detail by Invoice ID

This query validates that the sum of costs for all service usage in the [CostAndUsage](#datasets.costandusage) dataset matches the total non-tax charges in the [InvoiceDetail](#datasets.invoicedetail) dataset for a specific invoice.

```sql
SELECT
  COALESCE(ID.InvoiceId, CU.InvoiceId) AS InvoiceId,
  ID.TotalBilledCost_InvoiceDetail,
  CU.TotalBilledCost_CostAndUsage,
  (ID.TotalBilledCost_InvoiceDetail - CU.TotalBilledCost_CostAndUsage) AS Variance
FROM (
  SELECT
    InvoiceId,
    SUM(BilledCost) AS TotalBilledCost_InvoiceDetail
  FROM InvoiceDetail
  WHERE ChargeCategory != 'Tax'
  GROUP BY InvoiceId
) ID
FULL OUTER JOIN (
  SELECT
    InvoiceId,
    SUM(BilledCost) AS TotalBilledCost_CostAndUsage
  FROM CostAndUsage
) CU ON ID.InvoiceId = CU.InvoiceId
WHERE ID.InvoiceId = ?
```

### Reconcile Multi-Currency Settlement using Lineage IDs

This query demonstrates how to use the `PaymentCurrencyInvoiceDetailId` to reconcile granular records (denominated in the billing currency) against the aggregate records used for payment (denominated in the payment currency). This resolves the "Divergent Grain" problem.

```sql
SELECT
  PaymentCurrencyInvoiceDetailId,
  SUM(BilledCost) AS TotalBilled_BillingCurrency,
  SUM(PaymentCurrencyBilledCost) AS TotalBilled_PaymentCurrency,
  -- Calculate effective exchange rate for the group
  SAFE_DIVIDE(SUM(PaymentCurrencyBilledCost), SUM(BilledCost)) AS EffectiveExchangeRate
FROM InvoiceDetail
WHERE InvoiceId = ?
GROUP BY PaymentCurrencyInvoiceDetailId
ORDER BY PaymentCurrencyInvoiceDetailId
```

### Validate Tax Variance

This query identifies the tax component present in the [InvoiceDetail](#datasets.invoicedetail) dataset that is typically excluded from the [CostAndUsage](#datasets.costandusage) dataset, allowing for a complete three-way match between usage, tax, and the total invoice amount.

```sql
SELECT
  InvoiceId,
  SUM(CASE WHEN ChargeCategory = 'Tax' THEN BilledCost ELSE 0 END) AS TotalTaxAmount,
  SUM(CASE WHEN ChargeCategory != 'Tax' THEN BilledCost ELSE 0 END) AS TotalServiceAmount,
  SUM(BilledCost) AS GrandTotalPayable
FROM InvoiceDetail
WHERE InvoiceId = ?
GROUP BY InvoiceId
```

## Introduced (Version)

1.4
