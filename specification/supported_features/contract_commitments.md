# Contract Commitments

## Description

FOCUS supports the tracking of [commitments](#term) made via contractual agreements between a [service provider](#term) and a customer. Each row in the [Cost and Usage](#ds) dataset is associated with one or more unique identifiers representing those [contracts](#term) and [contract commitments](#term), stored in a JSON column called [Contract Applied](#col). A richer amount of detail that describes those [commitments](#term) is carried in a separate [Contract Commitment](#ds) dataset, which can be joined to the [Cost and Usage](#ds) dataset to facilitate various queries involving filtering and aggregation.

The [Contract Applied](#col) column contains several FOCUS-defined properties. For more information, see the [Contract Applied column definition](#col:ContractApplied).

## Directly Dependent Columns

* [CostAndUsage](#ds)
  * [ContractApplied](#col)

## Supporting Columns

* [ContractCommitment](#ds)
  * [BillingCurrency](#col:ContractCommitment.BillingCurrency)
  * [ContractCommitmentCategory](#col)
  * [ContractCommitmentCost](#col)
  * [ContractCommitmentId](#col)
  * [ContractCommitmentPeriodEnd](#col)
  * [ContractCommitmentPeriodStart](#col)
  * [ContractCommitmentQuantity](#col)
  * [ContractCommitmentType](#col)
  * [ContractCommitmentUnit](#col)
  * [ContractId](#col:ContractCommitment.ContractId)

## Example SQL Queries

The FOCUS specification implements the application of [contract commitments](#term) to cost and usage via the [Contract Applied](#col) column, which is defined in [JSON object format](#attr).

Because ANSI SQL does not inherently support the parsing of JSON, the following queries leverage the JSON functions found in BigQuery Standard SQL in order to demonstrate this feature's functionality. Similar JSON functions are available in all major SQL engines; thus, the below examples can be slightly modified to accommodate any particular database instance.

### Report on Initial Contract Commitment

This query takes inputs of a time range via [Charge Period Start](#col) and [Charge Period End](#col), then presents the aggregation of initial [contract commitments](#term) from the [Cost and Usage](#ds) dataset per [Service Provider Name](#col:CostAndUsage.ServiceProviderName) and [Contract Commitment ID](#col) by filtering on the specified time range, along with [Charge Category](#col:CostAndUsage.ChargeCategory) of "Purchase".

```sql
SELECT
  MIN(CU.ChargePeriodStart) AS ChargePeriodStart,
  MAX(CU.ChargePeriodEnd) AS ChargePeriodEnd,
  CU.ServiceProviderName,
  JSON_VALUE(CA, '$.ContractCommitmentId') AS ContractCommitmentId,
  SUM(CAST(JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') AS FLOAT64)) AS ContractCommitmentAppliedCost
FROM CostAndUsage CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.ContractApplied, '$.Elements')) AS CA
WHERE JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') IS NOT NULL
  AND ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ChargeCategory = 'Purchase'
GROUP BY ServiceProviderName, ContractCommitmentId
ORDER BY ServiceProviderName, ContractCommitmentId
```

### Report on Usage Against Contract Commitment

This query takes inputs of a time range via [Charge Period Start](#col) and [Charge Period End](#col), then presents the aggregation of the application of [contract commitments](#term) from the [Cost and Usage](#ds) dataset per [Service Provider Name](#col:CostAndUsage.ServiceProviderName) and [Contract Commitment ID](#col) by filtering on the specified time range, along with [Charge Category](#col:CostAndUsage.ChargeCategory) of "Usage".

```sql
SELECT
  MIN(CU.ChargePeriodStart) AS ChargePeriodStart,
  MAX(CU.ChargePeriodEnd) AS ChargePeriodEnd,
  CU.ServiceProviderName,
  JSON_VALUE(CA, '$.ContractCommitmentId') AS ContractCommitmentId,
  SUM(CAST(JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') AS FLOAT64)) AS ContractCommitmentAppliedCost
FROM CostAndUsage CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.ContractApplied, '$.Elements')) AS CA
WHERE JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') IS NOT NULL
  AND ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ChargeCategory = 'Usage'
GROUP BY ServiceProviderName, ContractCommitmentId
ORDER BY ServiceProviderName, ContractCommitmentId
```

### Report on Usage Against Contract Commitment by Category

This query takes inputs of a time range via [Charge Period Start](#col) and [Charge Period End](#col), then presents the aggregation of the application of [contract commitments](#term) from the [Cost and Usage](#ds) dataset per [Service Provider Name](#col:CostAndUsage.ServiceProviderName) and [Contract Commitment ID](#col) by filtering on the specified time range, along with [Charge Category](#col:CostAndUsage.ChargeCategory) of "Usage". It also joins in the [Contract Commitment](#ds) dataset to provide further information about each [contract commitment](#term) (in this case, the contract, category, type, start and end date/time, committed cost, and committed quantity and unit). It reports applied cost only, so [Contract Applied](#col) entries that record an applied quantity without an applied cost are excluded.

```sql
SELECT
  MIN(CU.ChargePeriodStart) AS ChargePeriodStart,
  MAX(CU.ChargePeriodEnd) AS ChargePeriodEnd,
  CU.ServiceProviderName,
  CC.ContractId,
  JSON_VALUE(CA, '$.ContractCommitmentId') AS ContractCommitmentId,
  CC.ContractCommitmentCategory,
  CC.ContractCommitmentType,
  CC.ContractCommitmentPeriodStart,
  CC.ContractCommitmentPeriodEnd,
  CC.BillingCurrency,
  CC.ContractCommitmentCost,
  CC.ContractCommitmentQuantity,
  CC.ContractCommitmentUnit,
  SUM(CAST(JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') AS FLOAT64)) AS ContractCommitmentAppliedCost
FROM CostAndUsage CU
CROSS JOIN
  UNNEST(JSON_EXTRACT_ARRAY(CU.ContractApplied, '$.Elements')) AS CA
INNER JOIN
  ContractCommitment CC
ON
  JSON_VALUE(CA, '$.ContractCommitmentId') = CC.ContractCommitmentId
WHERE JSON_VALUE(CA, '$.ContractCommitmentAppliedCost') IS NOT NULL
  AND ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ChargeCategory = 'Usage'
GROUP BY
  CU.ServiceProviderName,
  CC.ContractId,
  ContractCommitmentId,
  CC.ContractCommitmentCategory,
  CC.ContractCommitmentType,
  CC.ContractCommitmentPeriodStart,
  CC.ContractCommitmentPeriodEnd,
  CC.BillingCurrency,
  CC.ContractCommitmentCost,
  CC.ContractCommitmentQuantity,
  CC.ContractCommitmentUnit
ORDER BY
  CU.ServiceProviderName,
  CC.ContractCommitmentCategory,
  ContractCommitmentId
```

## Version Introduced

1.3
