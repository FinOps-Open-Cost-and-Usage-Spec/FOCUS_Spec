# Recency Metadata

## Scenario

ACME provides recency metadata to accompany their FOCUS data export. Acme updates their FOCUS Cost and Usage, data time series dataset, every hour, the data lags by 2 days. In this case the most recent update to the recency data indicates the previously incomplete time sectors are now complete. It also indicates that previous time sectors have been updated in the dataset. New time sectors have also been added.

## Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/recency/recency-1234-abcde-12345-abcde-12345.json`.

The provided recency metadata for time series dataset could look like this:

```json
{
  "Dataset": "1234-abcde-12345-abcde-12345",
  "RecencyLastUpdateDate": "2025-01-291T12:01:03.083z",
  "TimeSectors": [
    {
      "start_time": "2025-01-27T0:00:00z",
      "end_time" : "2025-01-27T1:00:00z",
      "complete" : true,
      "last_updated" : "2025-01-29T04:00:00z"
    },
    {
      "start_time": "2025-01-27T1:00:00z",
      "end_time" : "2025-01-27T2:00:00z",
      "complete" : true,
      "last_updated" : "2025-01-29T04:00:00z"
    },
    {
      "start_time": "2025-01-27T2:00:00z",
      "end_time" : "2025-01-27T3:00:00z",
      "complete" : true,
      "last_updated" : "2025-01-29T04:00:00z"
    },
    {
      "start_time": "2025-01-27T3:00:00z",
      "end_time" : "2025-01-27T4:00:00z",
      "complete" : true,
      "last_updated" : "2025-01-29T04:00:00z"
    },
    {
      "start_time": "2025-01-27T4:00:00z",
      "end_time" : "2025-01-27T5:00:00z",
      "complete" : true,
      "last_updated" : "2025-01-29T04:00:00z"
    },
    {
      "start_time": "2025-01-27T5:00:00z",
      "end_time" : "2025-01-27T6:00:00z",
      "complete" : true,
      "last_updated" : "2025-01-29T04:00:00z"
    },
    {
      "start_time": "2025-01-27T6:00:00z",
      "end_time" : "2025-01-27T7:00:00z",
      "complete" : true,
      "last_updated" : "2025-01-29T11:15:24z"
    },
    {
      "start_time": "2025-01-27T7:00:00z",
      "end_time" : "2025-01-27T8:00:00z",
      "complete" : true,
      "last_updated" : "2025-01-29T11:15:24z"
    },
    {
      "start_time": "2025-01-27T8:00:00z",
      "end_time" : "2025-01-27T9:00:00z",
      "complete" : false,
      "last_updated" : "2025-01-29T04:00:00z"
    },
    {
      "start_time": "2025-01-27T9:00:00z",
      "end_time" : "2025-01-27T10:00:00z",
      "complete" : false,
      "last_updated" : "2025-01-29T10:23:10z"
    },
    {
      "start_time": "2025-01-27T10:00:00z",
      "end_time" : "2025-01-27T11:00:00z",
      "complete" : false,
      "last_updated" : "2025-01-29T11:15:24z"
    }
  ]
}
```

The provided recency metadata for non-time series dataset could look like this:

```json
{
  "Dataset": "1234-abcde-12345-abcde-12345",
  "RecencyLastUpdateDate": "2025-01-291T12:01:03.083z",
  "last_updated" : "2025-01-29T04:00:00z",
  "complete" : true
}
```
