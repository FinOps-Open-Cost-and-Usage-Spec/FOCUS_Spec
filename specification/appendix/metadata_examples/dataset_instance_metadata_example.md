# Dataset Instance Metadata

## Scenario

ACME provides two dataset instances, "Cost and Usage Daily" and "Commitments", each corresponding to the respective FOCUS datasets: Cost and Usage and Contract Commitment. ACME also provides a directory of datasets metadata containing a single file with metadata for each dataset instance.

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

