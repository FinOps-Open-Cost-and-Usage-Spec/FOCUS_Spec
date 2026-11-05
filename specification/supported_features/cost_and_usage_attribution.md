---
dataset: CostAndUsage
---

# Cost and Usage Attribution

## Description

Many [service providers](#term) have features that allow FinOps [practitioners](#term) to enrich cost and usage data with metadata that is in addition to [service provider](#term) defined data, in order to analyze FinOps data using organizational, deployment, or other structures. These features may take the form of directly applied metadata or inherited metadata. FOCUS facilitates the inclusion of this metadata at a row level using the [Tags](#col) column.

## Directly Dependent Columns

* [Tags](#col)

## Supporting Columns

* [BilledCost](#col)
* [ConsumedQuantity](#col)
* [ConsumedUnit](#col)
* [EffectiveCost](#col)

## Example SQL Query

```sql
SELECT
  Tags,
  ConsumedUnit,
  SUM(BilledCost),
  SUM(EffectiveCost),
  SUM(ConsumedQuantity)
FROM CostAndUsage
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  Tags,
  ConsumedUnit
```

## Version Introduced

1.0
