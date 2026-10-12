# Data Generator-Calculated Split Cost Allocation

## Description

FOCUS enables tracking of resources split by some internal consumption metrics. This is most common for resources supporting shared usage like compute nodes in a shared cluster (Kubernetes, databases) or storage engines that can share capacity between workloads.

## Directly Dependent Columns

* ResourceId
* EffectiveCost
* BilledCost
* AllocatedResourceId
* AllocatedResourceName
* AllocatedServiceName
* AllocatedMethodDetails
* AllocatedMethodId

## Supporting Columns

* ChargeCategory
* ChargePeriodEnd
* ChargePeriodStart
* ServiceCategory
* ServiceName
* ServiceProviderName

## Example SQL Queries

### Find Resources with a Shared Cost

```sql
SELECT
  DISTINCT ResourceId
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND AllocatedMethodId IS NOT NULL
```

### Get Total Effective Cost by Resource ID (Ignore Shared Cost)

```sql
SELECT
  ResourceId,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND AllocatedMethodId IS NOT NULL
GROUP BY
  ResourceId
```

### Get Total Effective Cost by Allocated Resource ID

```sql
SELECT
  AllocatedResourceId,
  AllocatedResourceName,
  ServiceName,
  ServiceCategory,
  ServiceProviderName,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND AllocatedMethodId IS NOT NULL
GROUP BY
  AllocatedResourceId,
  AllocatedResourceName,
  ServiceName,
  ServiceCategory,
  ServiceProviderName
```

### Get Total Effective Cost by Allocated Service Name

```sql
SELECT
  AllocatedServiceName,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND AllocatedMethodId IS NOT NULL
  AND AllocatedServiceName IS NOT NULL
GROUP BY
  AllocatedServiceName
```

### Find Total Unallocated Split Costs by Resource ID

```sql
SELECT
  ResourceId,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND AllocatedMethodId IS NOT NULL AND AllocatedResourceId IS NULL
GROUP BY
  ResourceId
```

### Find How a Single Resource Has Been Split

```sql
SELECT
  ResourceId,
  COALESCE(AllocatedResourceId, 'Unallocated') AS AllocatedResourceId,
  SUM(BilledCost) AS TotalBilledCost,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND ResourceId = ?
GROUP BY
  ResourceId,
  COALESCE(AllocatedResourceId, 'Unallocated')
```

### Extract JSON from Allocated Method Details

```sql
SELECT
  ResourceId,
  elements.allocated_ratio,
  elements.usage_unit,
  elements.usage_quantity
FROM
  focus_data_table,
  JSON_TABLE(
    AllocatedMethodDetails,
    '$.Elements[*]' COLUMNS (
      allocated_ratio DECIMAL(10, 2) PATH '$.AllocatedRatio',
      usage_unit VARCHAR(50) PATH '$.UsageUnit',
      usage_quantity DECIMAL(10, 2) PATH '$.UsageQuantity'
    )
  ) AS elements
```

## Version Introduced

1.3
