# Includes Regions

The Includes Regions condition represents a verifiable state where the [operating model](#glossary:operating-model) includes deploying resources or services within a region.

## Requirements

IncludesRegions MUST adhere to the following requirements:

* IncludesRegions MUST evaluate to true when the operating model supports deploying resources or services within distinct geographic regions.
* IncludesRegions MUST evaluate to false when the operating model does not support region-based deployment.

## Condition ID

IncludesRegions

## Display Name

Includes Regions

## Description

A verifiable state indicating whether the operating model includes deploying resources or services within a region.

## Version Introduced

1.5
