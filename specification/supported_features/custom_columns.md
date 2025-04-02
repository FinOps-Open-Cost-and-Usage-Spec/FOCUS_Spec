# Custom Columns

## Introduced Version

0.5

## Description

The FOCUS spec supports the inclusion of custom columns to facilitate reporting capability that is not covered by the columns included in the specification.

## Directly Dependent Columns
* x_CustomColumn

## Example SQL Query

```sql
SELECT
  BillingPeriodStart,
  x_CustomColumn,
  SUM(BilledCost) AS TotalBilledCost,
FROM focus_data_table
WHERE ServiceName = ?
  AND BillingPeriodStart >= ? AND BillingPeriodStart < ?
GROUP BY
  BillingPeriodStart,
  x_CustomColumn
ORDER BY MonthlyCost DESC
```
