---
dataset: InvoiceDetail
---

# Invoice Reconciliation

## Description

FOCUS supports the reconciliation of granular cloud consumption records with the formal financial documents issued by an [invoice issuer](#term). The [Invoice Detail](#ds) dataset represents the definitive financial record of [charges](#term) as they appear on an [invoice](#term). By leveraging common identifiers, [practitioners](#term) can map usage-based costs in the [Cost and Usage](#ds) dataset back to their corresponding line items in the [Invoice Detail](#ds) dataset.

This feature also supports reconciliation across divergent currency grains. When an [invoice issuer](#term) represents billing and payment currencies at different aggregation levels, the [Payment Currency Invoice Detail ID](#col) column provides the necessary lineage to link granular usage records to the aggregate records used for financial settlement.

## Directly Dependent Columns

* [InvoiceDetail](#ds)
  * [BilledCost](#col)
  * [InvoiceId](#col)
  * [InvoiceDetailId](#col)
  * [PaymentCurrencyBilledCost](#col)
  * [PaymentCurrencyInvoiceDetailId](#col)
* [CostAndUsage](#ds)
  * [BilledCost](#col)
  * [InvoiceId](#col)
  * [InvoiceDetailId](#col)

## Supporting Columns

* [InvoiceDetail](#ds)
  * [BillingCurrency](#col)
  * [ChargeCategory](#col)
  * [InvoiceIssueStatus](#col)
  * [PaymentCurrency](#col)
* [CostAndUsage](#ds)
  * [ChargeCategory](#col)

## Example SQL Queries

Reconciliation often requires aggregating granular usage data to match the coarser grain of an [invoice](#term). The following queries demonstrate how to validate that usage records equal the billed amounts on a legal [invoice](#term).

### Reconcile Cost and Usage to Invoice Detail by Invoice ID

This query validates that the sum of costs for all service usage in the [Cost and Usage](#ds) dataset equals the total non-tax [charges](#term) in the [Invoice Detail](#ds) dataset for a specific [invoice](#term).

```sql
SELECT
  COALESCE(ID.InvoiceId, CU.InvoiceId) AS InvoiceId,
  ID.TotalBilledCost_InvoiceDetail,
  CU.TotalBilledCost_CostAndUsage,
  (COALESCE(ID.TotalBilledCost_InvoiceDetail, 0) - COALESCE(CU.TotalBilledCost_CostAndUsage, 0)) AS Variance
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
  WHERE ChargeCategory != 'Tax'
  GROUP BY InvoiceId
) CU ON ID.InvoiceId = CU.InvoiceId
WHERE COALESCE(ID.InvoiceId, CU.InvoiceId) = ?
```

### Reconcile Cost and Usage to Invoice Detail by Invoice Detail ID

This query compares each non-tax record in the [Invoice Detail](#ds) dataset for a specific [invoice](#term) with the sum of the [charges](#term) in the [Cost and Usage](#ds) dataset that reference it, identifying the [invoice](#term) line items where the two datasets differ.

```sql
SELECT
  ID.InvoiceIssuerName,
  ID.InvoiceId,
  ID.InvoiceDetailId,
  ID.InvoiceIssueStatus,
  ID.BillingCurrency,
  ID.BilledCost AS BilledCost_InvoiceDetail,
  CU.TotalBilledCost_CostAndUsage,
  (ID.BilledCost - COALESCE(CU.TotalBilledCost_CostAndUsage, 0)) AS Variance
FROM InvoiceDetail ID
LEFT JOIN (
  SELECT
    InvoiceIssuerName,
    InvoiceId,
    InvoiceDetailId,
    SUM(BilledCost) AS TotalBilledCost_CostAndUsage
  FROM CostAndUsage
  GROUP BY InvoiceIssuerName, InvoiceId, InvoiceDetailId
) CU ON ID.InvoiceIssuerName = CU.InvoiceIssuerName
  AND ID.InvoiceId = CU.InvoiceId
  AND ID.InvoiceDetailId = CU.InvoiceDetailId
WHERE ID.InvoiceIssuerName = ?
  AND ID.InvoiceId = ?
  AND ID.ChargeCategory != 'Tax'
ORDER BY ID.InvoiceDetailId
```

### Reconcile Multi-Currency Settlement Using Lineage IDs

This query demonstrates how to use [Payment Currency Invoice Detail ID](#col) to reconcile granular records (denominated in the billing currency) against the aggregate records used for payment (denominated in the payment currency). This resolves the "Divergent Grain" problem.

```sql
SELECT
  PaymentCurrencyInvoiceDetailId,
  BillingCurrency,
  PaymentCurrency,
  SUM(BilledCost) AS TotalBilled_BillingCurrency,
  SUM(PaymentCurrencyBilledCost) AS TotalBilled_PaymentCurrency,
  -- Calculate effective exchange rate for the group
  SUM(PaymentCurrencyBilledCost) / NULLIF(SUM(BilledCost), 0) AS EffectiveExchangeRate
FROM InvoiceDetail
WHERE InvoiceId = ?
GROUP BY PaymentCurrencyInvoiceDetailId, BillingCurrency, PaymentCurrency
ORDER BY PaymentCurrencyInvoiceDetailId
```

### Validate Tax Variance

This query identifies the tax component present in the [Invoice Detail](#ds) dataset that is typically excluded from the [Cost and Usage](#ds) dataset, allowing for a complete three-way match between usage, tax, and the total [invoice](#term) amount.

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

## Version Introduced

1.4
