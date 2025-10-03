# Recency Metadata

## Scenario

ACME has elected to add recency metadata to its FOCUS data export. ACME provides a directory of recency metadata for each dataset they provide and each recency object is a single file.

## Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/recency/recency-1234-abcde-12345-abcde-12345.json`.

The provided recency metadata for a time series dataset could look like this:

```json
{
  "DatasetInstanceId": "1234-abcde-12345-abcde-12345",
  "RecencyLastUpdateDate": "2025-01-291T12:01:03.083z",
  "TimeSectors": [
    {
      "TimeSectorStart": "2025-01-27T0:00:00z",
      "TimeSectorEnd" : "2025-01-27T1:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T1:00:00z",
      "TimeSectorEnd" : "2025-01-27T2:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T2:00:00z",
      "TimeSectorEnd" : "2025-01-27T3:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T3:00:00z",
      "TimeSectorEnd" : "2025-01-27T4:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T4:00:00z",
      "TimeSectorEnd" : "2025-01-27T5:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T5:00:00z",
      "TimeSectorEnd" : "2025-01-27T6:00:00z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T6:00:00z",
      "TimeSectorEnd" : "2025-01-27T7:00:00z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    }
  ]
}
```

The provided recency metadata for non-time series dataset could look like this:

```json
{
  "DatasetInstanceId": "54321-abcde-12345-abcde-12345",
  "RecencyLastUpdateDate": "2025-01-291T12:01:03.083z",
  "DatasetInstanceLastUpdated" : "2025-01-29T04:00:00z",
  "DatasetInstanceComplete" : true
}
```
