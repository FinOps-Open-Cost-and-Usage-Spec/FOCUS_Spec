# Data Generator-Calculated Split Cost Allocation Handling

The data generator-calculated split cost allocation for data generator-defined services is a capability that can be offered by data generators which allocates (or in some cases provides more granular detail about) a charge to a more granular level. This is accomplished by taking a charge record present in a FOCUS dataset ([*origin charge*](#glossary:origin-charge)) and splitting it into multiple charge records ([*allocated charges*](#glossary:allocated-charge)) to reflect the more granular detail, while ensuring the origin charge can be derived from the combination of *allocated charges*. This feature is used by practitioners to conduct chargebacks and better understand the usage of resources.

## Attribute ID

DataGeneratorCalculatedSplitCostAllocationHandling

## Attribute Name

Data Generator-Calculated Split Cost Allocation Handling

## Description

An attribute that allows data generators to offer more detailed cost and usage information based on a method defined and documented by the data generator, including support for allocating costs in cases where the usage of a resource might not match the units the resource is measured in.

## Requirements

When the data generator supports data generator-calculated split cost allocation, column conforming to DataGeneratorCalculatedSplitCostAllocationHandling attribute MUST adhere to the following requirements:

* [*FOCUS dataset column*](#glossary:FOCUS-dataset-column) values in *allocated charges* MUST match the corresponding value in the *origin charge* when the *FOCUS dataset column* represents a dimension.
* *FOCUS dataset column* values in *allocated charges* MUST match the corresponding value in the *origin charge* when the *FOCUS dataset column* represents a non-summable [*metric*](#glossary:metric) (e.g., unit prices).
* The sum of *FOCUS dataset column* values in *allocated charges* MUST match the corresponding value in the *origin charge* when the *FOCUS dataset column* represents a summable *metric* (e.g., costs and quantities).

## Introduced (version)

1.3
