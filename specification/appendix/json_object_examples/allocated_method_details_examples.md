# Examples: Allocated Method Details

The JSON samples in the scenarios below each represent a single allocated record out of the multiple records derived from an origin record for that scenario. The sum AllocatedRatio will add up to 1 (100%) across all allocated records for an origin record, with the AllocatedRatio (or sum of AllocatedRatio) representing the allocated record's portion of the overall origin record.

## Scenario 1: Single UsageUnit value used for allocation

When only a single "UsageUnit" is used to calculate the allocation.

```json
{
  "Elements" : [ {
    "AllocatedRatio" : 0.1,
    "UsageUnit" : "Hours",
    "UsageQuantity" : 300
    }
  ]
}
```

## Scenario 2: Multiple UsageUnit values used for allocation

When multiple "UsageUnit" values are used to calculate the allocation, another object is added to the "Elements" collection.

```json
{
  "Elements": [
    {
      "AllocatedRatio": 0.05,
      "UsageUnit": "CPU",
      "UsageQuantity": 0.5
    },
    {
      "AllocatedRatio": 0.1,
      "UsageUnit": "Memory",
      "UsageQuantity": 4
    }
  ]
}
```

## Scenario 3: Data generator omits keys that are not required

This data generator does not wish to supply the "UsageUnit" or "UsageQuantity" keys but still provides cost allocation with some additional allocation method details. In this case, "UsageUnit" and "UsageQuantity" are omitted, and only the "AllocatedRatio" is supplied.

```json
{
  "Elements" : [ {
    "AllocatedRatio" : 0.45
    }
  ]
}
```

## Scenario 4: Additional non-FOCUS specified properties

A data generator can add additional properties if they feel more context is helpful or necessary to the practitioner. In this scenario, the data generator is supplying additional context that shows only 0.5 of a unit was used. However, since 1 unit was requested by the service this allocation represents, the allocation is being charged at 1 regardless.

```json
{
  "Elements": [
    {
      "AllocatedRatio": 0.6,
      "UsageUnit": "vCPU",
      "UsageQuantity": 1,
      "x_ReservedVCPU": 1,
      "x_UsedVCPU": 0.5,
      "x_AllocatedVCPU": 1
    }
  ]
}
```
