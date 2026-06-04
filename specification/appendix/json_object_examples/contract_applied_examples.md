# Examples: Contract Applied

## Scenario 1: Initial Contract Commitment

A single Cost and Usage charge represents the values stated on a contract and its three contract commitments agreed between a service provider and a customer:

1) 12345: Spend $500k overall. (This is the value of the contract, and thus ContractId = ContractCommitmentId.)
2) 23456: Spend $25k on a particular service.
3) 34567: Consume 100k compute hours on a particular resource type.

The Charge Category is denoted as Purchase, and the Contract ID, Resource ID, and Contract Commitment ID are all denoted as 12345.

```json
{
  "ResourceId": "12345",
  "ChargeCategory": "Purchase",
  "BilledCost": 500000.00,
  "EffectiveCost": 0.00,
  "ContractApplied":
    {
      "Elements": [ {
        "ContractId": "12345",
        "ContractCommitmentId": "12345",
        "ContractCommitmentAppliedCost": 500000.00
      }, {
        "ContractId": "12345",
        "ContractCommitmentId": "23456",
        "ContractCommitmentAppliedCost": 25000.00
      }, {
        "ContractId": "12345",
        "ContractCommitmentId": "34567",
        "ContractCommitmentAppliedQuantity": 100000.00,
        "ContractCommitmentAppliedUnit": "compute_hours"
      } ]
    }
}
```

## Scenario 2: Contract Commitment Usage with No Custom Columns

Assume the contract commitment as described in Scenario 1. Assume that only 50% of cost and usage gets applied to the contract commitments, per the contract terms.

A single Cost and Usage charge for `myResource1` carries Effective Cost of 30 (denominated in USD) and Consumed Quantity of 1 (denominated in compute hours). The Charge Category is denoted as Usage.

This applies to the contract commitments in the following manner:

```json
{
  "ResourceId": "myResource1",
  "ChargeCategory": "Usage",
  "BilledCost": 0.00,
  "EffectiveCost": 30.00,
  "ConsumedQuantity": 1,
  "ContractApplied":
    {
      "Elements": [ {
        "ContractId": "12345",
        "ContractCommitmentId": "12345",
        "ContractCommitmentAppliedCost": 15.00
      }, {
        "ContractId": "12345",
        "ContractCommitmentId": "23456",
        "ContractCommitmentAppliedCost": 15.00
      }, {
        "ContractId": "12345",
        "ContractCommitmentId": "34567",
        "ContractCommitmentAppliedQuantity": 0.50,
        "ContractCommitmentAppliedUnit": "compute_hours"
      } ]
    }
}
```

## Scenario 3: Contract Commitment Usage with Custom Columns

The same as Scenario 2, except a custom key-value pair `x_ContractCommitmentCostBalance` is provided by the data generator. This datapoint represents the value remaining on a given contract commitment.

```json
{
  "ResourceId": "myResource1",
  "ChargeCategory": "Usage",
  "BilledCost": 0.00,
  "EffectiveCost": 30.00,
  "ConsumedQuantity": 1,
  "ContractApplied":
    {
      "Elements": [ {
        "ContractId": "12345",
        "ContractCommitmentId": "12345",
        "ContractCommitmentAppliedCost": 15.00,
        "x_ContractCommitmentCostBalance": 499985.00
      }, {
        "ContractId": "12345",
        "ContractCommitmentId": "23456",
        "ContractCommitmentAppliedCost": 15.00,
        "x_ContractCommitmentCostBalance": 24985.00
      }, {
        "ContractId": "12345",
        "ContractCommitmentId": "34567",
        "ContractCommitmentAppliedQuantity": 0.50,
        "ContractCommitmentAppliedUnit": "compute_hours"
      } ]
    }
}
```
