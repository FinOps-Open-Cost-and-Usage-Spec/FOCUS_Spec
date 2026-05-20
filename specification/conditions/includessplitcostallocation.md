# Includes Split Cost Allocation

The Includes Split Cost Allocation condition represents a verifiable state where the [*operating model*](#glossary:operating-model) includes logic for distributing the cost or usage of a single origin charge across multiple entities.

## Requirements

IncludesSplitCostAllocation MUST adhere to the following requirements:

* IncludesSplitCostAllocation MUST evaluate to true when the operating model contains a mechanism to distribute shared costs across distinct resources, tags, or accounts.
* IncludesSplitCostAllocation MUST evaluate to false when the operating model lacks any native mechanism for cost or usage apportionment.

## Condition ID

IncludesSplitCostAllocation

## Display Name

Includes Split Cost Allocation

## Description

A verifiable state indicating whether the operating model includes split cost allocation.

## Version Introduced

1.5
