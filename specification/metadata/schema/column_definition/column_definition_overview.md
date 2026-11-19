# Column Definition

The FOCUS metadata schema column definition provides a list of the columns present in the [dataset instance artifact](#term) along with metadata about the columns.

## Requirements

[ColumnDefinition](#meta) adheres to the following requirements:

* [ColumnDefinition](#meta) MUST be present in an object within the [Schema](#meta) collection.
* [ColumnDefinition](#meta) MUST be structured as a collection of objects.
* [ColumnDefinition](#meta) MUST NOT be null.
* [ColumnDefinition](#meta) collection MUST contain one and only one object for every column provided in [dataset instance artifacts](#term) that reference the parent Schema object.
* [ColumnDefinition](#meta) collection MUST NOT contain null objects.

## Metadata ID

ColumnDefinition

## Metadata Name

Column Definition

## Version Introduced

1.0
