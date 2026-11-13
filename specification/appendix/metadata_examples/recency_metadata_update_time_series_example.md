# Recency Metadata Update (Time Series)

## Scenario

CrestNode provides recency metadata to accompany its FOCUS data export. CrestNode updates its FOCUS Cost and Usage dataset (time series) every hour; however, the data lags by two days. Here, the most recent update to the recency data indicates the previous time sectors are now TimeSectorComplete. It also indicates that previous time sectors have been updated in the dataset. New time sectors have also been added.

## Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/recency/recency-1234-abcde-12345-abcde-12345.json`.

The provided recency metadata for time series dataset could look like this:

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
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00Z"
    },
    {
      "TimeSectorStart": "2025-01-27T06:00:00Z",
      "TimeSectorEnd" : "2025-01-27T07:00:00Z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T11:15:24Z"
    },
    {
      "TimeSectorStart": "2025-01-27T07:00:00Z",
      "TimeSectorEnd" : "2025-01-27T08:00:00Z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T11:15:24Z"
    },
    {
      "TimeSectorStart": "2025-01-27T08:00:00Z",
      "TimeSectorEnd" : "2025-01-27T09:00:00Z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00Z"
    },
    {
      "TimeSectorStart": "2025-01-27T09:00:00Z",
      "TimeSectorEnd" : "2025-01-27T10:00:00Z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T10:23:10Z"
    },
    {
      "TimeSectorStart": "2025-01-27T10:00:00Z",
      "TimeSectorEnd" : "2025-01-27T11:00:00Z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T11:15:24Z"
    }
  ]
}
```
