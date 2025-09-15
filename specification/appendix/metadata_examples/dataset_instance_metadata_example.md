# Dataset Instance Metadata

## Scenario

ACME provides two different datset instances, "Cost and Usage Daily" and "Commitments," FOCUS Cost and Usage and FOCUS Commitments respectively.  ACME provides a directory of datasets metadat with a single file including each dataet instance's metadata.

## Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/dataset_instances.json`.

The updated schema-related metadata could look like this:

```json
[
  {
    "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-246811",
    "DatasetInstanceName": "Contract Commitments Report",
    "FOCUSDataset": "ContractCommitment"
  },
  {
    "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
    "DatasetInstanceName": "COST_AND_USAGE_DAILY",
    "FOCUSDataset": "CostAndUsage"
    
  }
]
```

