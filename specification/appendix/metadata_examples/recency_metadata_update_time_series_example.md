# Recency Metadata Update (Time Series)

## Scenario

ACME provides recency metadata to accompany its FOCUS data export. ACME updates its FOCUS Cost and Usage dataset (time series) every hour; however, the data lags by two days. Here, the most recent update to the recency data indicates the previous time sectors are now TimeSectorComplete. It also indicates that previous time sectors have been updated in the dataset. New time sectors have also been added.

## Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/recency/recency-1234-abcde-12345-abcde-12345.json`.

The provided recency metadata for time series dataset could look like this:

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
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T6:00:00z",
      "TimeSectorEnd" : "2025-01-27T7:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T11:15:24z"
    },
    {
      "TimeSectorStart": "2025-01-27T7:00:00z",
      "TimeSectorEnd" : "2025-01-27T8:00:00z",
      "TimeSectorComplete" : true,
      "TimeSectorLastUpdated" : "2025-01-29T11:15:24z"
    },
    {
      "TimeSectorStart": "2025-01-27T8:00:00z",
      "TimeSectorEnd" : "2025-01-27T9:00:00z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T04:00:00z"
    },
    {
      "TimeSectorStart": "2025-01-27T9:00:00z",
      "TimeSectorEnd" : "2025-01-27T10:00:00z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T10:23:10z"
    },
    {
      "TimeSectorStart": "2025-01-27T10:00:00z",
      "TimeSectorEnd" : "2025-01-27T11:00:00z",
      "TimeSectorComplete" : false,
      "TimeSectorLastUpdated" : "2025-01-29T11:15:24z"
    }
  ]
}
```

The provided recency metadata for non-time series dataset could look like this:

```json
{
  "Dataset": "1234-abcde-12345-abcde-12345",
  "RecencyLastUpdateDate": "2025-01-291T12:01:03.083z",
  "DatasetInstanceLastUpdated" : "2025-01-29T04:00:00z",
  "DatasetInstanceComplete" : true
}
```
