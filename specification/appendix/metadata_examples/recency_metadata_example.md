# Recency Metadata

## Scenario

CrestNode has elected to add recency metadata to its FOCUS data export. CrestNode provides a directory of recency metadata for each dataset they provide and each recency object is a single file.

## Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/recency/recency-1234-abcde-12345-abcde-12345.json`.

The provided recency metadata for a time series dataset could look like this:

```json
{
  "DatasetInstanceId": "1234-abcde-12345-abcde-12345",
  "RecencyLastUpdated": "2025-01-29T12:01:03Z",
  "TimeSectors": [
    {
      "TimeSectorStart": "2025-01-27T00:00:00Z",
      "TimeSectorEnd" : "2025-01-27T01:00:00Z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00Z"
    },
    {
      "TimeSectorStart": "2025-01-27T01:00:00Z",
      "TimeSectorEnd" : "2025-01-27T02:00:00Z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00Z"
    },
    {
      "TimeSectorStart": "2025-01-27T02:00:00Z",
      "TimeSectorEnd" : "2025-01-27T03:00:00Z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00Z"
    },
    {
      "TimeSectorStart": "2025-01-27T03:00:00Z",
      "TimeSectorEnd" : "2025-01-27T04:00:00Z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00Z"
    },
    {
      "TimeSectorStart": "2025-01-27T04:00:00Z",
      "TimeSectorEnd" : "2025-01-27T05:00:00Z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00Z"
    },
    {
      "TimeSectorStart": "2025-01-27T05:00:00Z",
      "TimeSectorEnd" : "2025-01-27T06:00:00Z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00Z"
    },
    {
      "TimeSectorStart": "2025-01-27T06:00:00Z",
      "TimeSectorEnd" : "2025-01-27T07:00:00Z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00Z"
    }
  ]
}
```

The provided recency metadata for non-time series dataset could look like this:

```json
{
  "DatasetInstanceId": "54321-abcde-12345-abcde-12345",
  "RecencyLastUpdated": "2025-01-29T12:01:03Z",
  "DatasetInstanceLastUpdated" : "2025-01-29T04:00:00Z",
  "DatasetInstanceComplete" : true
}
```
