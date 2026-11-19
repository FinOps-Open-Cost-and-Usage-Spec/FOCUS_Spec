# Recency Metadata Update (Non Time Series)

## Scenario

CrestNode provides recency metadata to accompany their FOCUS data export. CrestNode updates their FOCUS Contract Commitment dataset, a non time-series dataset, every day. In this case, the most recent update to the recency data indicates the dataset and associated data artifact has been updated and is considered complete.

## Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/recency/recency-178151-dbad145e-178151-dbad145e-246811.json`.

The provided recency metadata for non-time series dataset could look like this:

```json
{
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-246811",
  "RecencyLastUpdated": "2025-01-29T15:01:03Z",
  "DatasetInstanceLastUpdated" : "2025-01-29T10:00:00Z",
  "DatasetInstanceComplete" : true
}
```
