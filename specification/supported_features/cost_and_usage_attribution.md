# Cost and Usage Attribution

## Introduced Version
1.0

## Description

Many providers have features that allow Finops practitioners to enrich cost and usage data with metadata, that is addition to provider defined data, in order to analyze Finops data using organizational, deployment, or other structures. These features may take the form of directly applied metadata or inherited metadata. The FOCUS spec faciliates the inclusion of this metadata at a row level.  

## Directly Dependent Columns
* Tags


## Indirectly Dependent Columns


## Example SQL Query
```
SELECT
  tags,
  SUM(BilledCost)
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  tags
```


