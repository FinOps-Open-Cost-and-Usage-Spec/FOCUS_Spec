# Location

## Description

FOCUS provides structured location data through region and availability zone information. By documenting geographic deployment locations, practitioners can organize and analyze costs based on where resources and services are deployed. This standardized location data helps practitioners understand the geographical distribution of infrastructure across providers.

## Directly Dependent Columns

* AvailabilityZone
* RegionId
* RegionName

## Supporting Columns

* BilledCost
* ChargePeriodEnd
* ChargePeriodStart

## Example SQL Query

```sql
SELECT
  RegionId,
  RegionName,
  AvailabilityZone,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
GROUP BY
  RegionId,
  RegionName,
  AvailabilityZone
``` 

## Introduced (Version)

1.0
