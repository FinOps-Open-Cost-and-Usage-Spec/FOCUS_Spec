# Column Definition

The FOCUS metadata schema column definition provides a list of the columns present in the [*dataset instance artifact*](#glossary:dataset-instance-artifact) along with metadata about the columns.

## Requirements

ColumnDefinition adheres to the following requirements:

* ColumnDefinition MUST be present in an object within the [Schema](#schema) collection.
* ColumnDefinition MUST be structured as a collection of objects.
* ColumnDefinition MUST NOT be null.
* ColumnDefinition collection MUST contain one and only one object for every column provided in *dataset instance artifacts* that reference the parent Schema object.
* ColumnDefinition collection MUST NOT contain null objects.

## Metadata ID

ColumnDefinition

## Metadata Name

Column Definition

## Introduced (version)

1.0
