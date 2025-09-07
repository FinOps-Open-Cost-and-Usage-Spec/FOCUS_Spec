# Split Cost Allocation

## Description

FOCUS enables tracking of resources split by some internal consumption metrics. This is most common for resources supporting shared usage like compute nodes in a shared cluster (Kubernetes, databases) or storage engines that can share capacity between workloads.

## Directly Dependent Columns

* ResourceId
* EffectiveCost
* BilledCost
* allocated_resource_id
* allocated_resource_name
* allocated_resource_details
* allocated_method_id

## Supporting Columns

* ChargeCategory
* ChargePeriodEnd
* ChargePeriodStart
* ProviderName
* ServiceName

## Example SQL Query (Find resources with a shared cost)

```sql
SELECT
  DISTINCT ResourceId
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND allocated_method_id IS NOT NULL
```

## Example SQL Query (Get total effective cost by ResourceId (ignore shared cost))

```sql
SELECT
  ResourceId
  SUM(EffectiveCost) as TotalEffectiveCost
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND allocated_method_id IS NOT NULL
GROUP BY
  ResourceId
```

## Example SQL Query (Get total effective cost by allocated_resource_id)

```sql
SELECT
  allocated_resource_id
  SUM(EffectiveCost) as TotalEffectiveCost
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND allocated_method_id IS NOT NULL
GROUP BY
  allocated_resource_id
```

## Example SQL Query (Find total unallocated split costs by resourceId)

```sql
SELECT
  ResourceId,
  SUM(EffectiveCost) as TotalEffectiveCost
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND allocated_method_id IS NOT NULL AND allocated_resource_id IS NULL
GROUP BY
  ResourceId
```

## Example SQL Query (Find how a single resource has been split)

```sql
SELECT
  ResourceId,
  COALESCE(allocated_resource_id, 'Unallocated') AS allocated_resource_id,
  SUM(EffectiveCost) as TotalEffectiveCost
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
  AND allocated_resource_id = ?
GROUP BY
  ResourceId,
  COALESCE(allocated_resource_id, 'Unallocated')
```

## Example SQL Query (Extract JSON from allocated_method_details)

```sql
SELECT
  resource_id,
  elements.allocated_ratio,
  elements.usage_unit,
  elements.usage_quantity
FROM
  focus_data_table,
  JSON_TABLE(
    allocated_method_details,
    '$.Elements[*]' COLUMNS (
      allocated_ratio DECIMAL(10, 2) PATH '$.AllocatedRatio',
      usage_unit VARCHAR(50) PATH '$.UsageUnit',
      usage_quantity DECIMAL(10, 2) PATH '$.UsageQuantity'
    )
  ) AS elements;
  ```

## Introduced (Version)

1.3
