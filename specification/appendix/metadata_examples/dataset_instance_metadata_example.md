# Dataset Instance Metadata

## Scenario

ACME provides three dataset instances: "Cost and Usage Daily," "Cost and Usage Hourly," and "Contract Commitments," corresponding to the FOCUS datasets Cost and Usage and Contract Commitment. ACME also provides a metadata directory containing a single file with metadata for each dataset instance.

## Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/dataset_instances.json`.

The updated schema-related metadata could look like this:

```json
[
  {
    "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-246811",
    "DatasetInstanceName": "Contract Commitments Report",
    "FocusDatasetId": "ContractCommitment"
  },
  {
    "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
    "DatasetInstanceName": "Cost and Usage Daily",
    "FocusDatasetId": "CostAndUsage"
  },
  {
    "DatasetInstanceId": "178151-ja23h1287-387151-dbad145e-134657",
    "DatasetInstanceName": "Cost and Usage Hourly",
    "FocusDatasetId": "CostAndUsage"
  }
]
```

