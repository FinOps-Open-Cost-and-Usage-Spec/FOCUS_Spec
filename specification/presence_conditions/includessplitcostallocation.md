# Includes Split Cost Allocation

The Includes Split Cost Allocation presence condition represents a verifiable state where the source operating model includes logic for distributing the cost or usage of a single origin charge across multiple entities.

## Requirements

IncludesSplitCostAllocation MUST adhere to the following requirements:

* IncludesSplitCostAllocation MUST evaluate to true when the source operating model contains a mechanism to distribute shared costs across distinct resources, tags, or accounts.
* IncludesSplitCostAllocation MUST evaluate to false when the source operating model lacks any native mechanism for cost or usage apportionment.

## Presence Condition ID

IncludesSplitCostAllocation

## Display Name

Includes Split Cost Allocation

## Description

A verifiable state indicating whether the source operating model includes split cost allocation.

## Version Introduced

1.5
