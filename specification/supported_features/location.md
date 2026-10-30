---
dataset: CostAndUsage
---

# Location

## Description

FOCUS provides structured location data through region and availability zone information. By documenting geographic deployment locations, practitioners can organize and analyze costs based on where resources and services are deployed. This standardized location data helps practitioners understand the geographical distribution of infrastructure across host providers.

## Directly Dependent Columns

* [AvailabilityZone](#col)
* [RegionId](#col)
* [RegionName](#col)

## Supporting Columns

* [BilledCost](#col)
* [ChargePeriodEnd](#col)
* [ChargePeriodStart](#col)

## Example SQL Query

```sql
SELECT
  RegionId,
  RegionName,
  AvailabilityZone,
  SUM(BilledCost) AS TotalBilledCost
FROM CostAndUsage
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
GROUP BY
  RegionId,
  RegionName,
  AvailabilityZone
```

## Version Introduced

1.0
