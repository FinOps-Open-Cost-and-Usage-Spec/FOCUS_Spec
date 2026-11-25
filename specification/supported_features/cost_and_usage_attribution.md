# Cost and Usage Attribution

## Description

Many [*service providers*](#glossary:service-provider) have features that allow FinOps [*practitioners*](#glossary:practitioner) to enrich cost and usage data with metadata that is in addition to *service provider* defined data, in order to analyze FinOps data using organizational, deployment, or other structures. These features may take the form of directly applied metadata or inherited metadata. FOCUS facilitates the inclusion of this metadata at a row level using the [Tags](#datamodel.costandusage.tags) column.

## Directly Dependent Columns

* Tags

## Supporting Columns

* BilledCost
* ConsumedQuantity
* ConsumedUnit
* EffectiveCost

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
