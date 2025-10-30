# Recency Metadata Update (Non Time Series)

## Scenario

ACME provides recency metadata to accompany their FOCUS data export. ACME updates their FOCUS Contracts dataset, a non time-series dataset, every day. In this case, the most recent update to the recency data indicates the dataset and associated data artifact has been updated and is considered complete.

## Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/recency/recency-54321-abcde-12345-abcde-12345.json`.

The provided recency metadata for non-time series dataset could look like this:

```json
{
  "DatasetInstanceId": "54321-abcde-12345-abcde-12345",
  "RecencyLastUpdate": "2025-01-291T15:01:03.083z",
  "DatasetInstanceLastUpdated" : "2025-01-29T010:00:00z",
  "DatasetInstanceComplete" : true
}
```
