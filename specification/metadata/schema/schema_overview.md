# Schema

The schema metadata object and its content provide information about the structure of the data provided.

## Requirements

[Schema](#meta) adheres to the following requirements:

* [Schema](#meta) MUST be present in the [Metadata](#metadata).
* [Schema](#meta) MUST be structured as a collection of objects.
* [Schema](#meta) MUST NOT be null.
* [Schema](#meta) collection MUST contain at least one object for every [DatasetInstance](#meta) object.
* [Schema](#meta) collection MUST NOT contain null objects.
* [Schema](#meta) collection object MUST be associated with one and only one [DatasetInstance](#meta) object.
* [Schema](#meta) collection object MUST be added to the collection whenever the structure of the [dataset instance artifacts](#term) changes (including, but not limited to, additions or removals of columns, modifications to any [ColumnDefinition](#meta), or updates to the FOCUSVersion or [DataGeneratorVersion](#meta)).
* [Schema](#meta) collection object MUST be referenced by [dataset instance artifacts](#term) that conform to the structure defined by that [Schema](#meta) collection object.
* [Schema](#meta) collection object MUST define the exact structure of the [dataset instance artifacts](#term) that reference it.
* [Schema](#meta) collection object MUST be retrievable independently from the [dataset instance artifacts](#term) that conform to the structure defined by that [Schema](#meta) collection object.
* [Schema](#meta) collection object SHOULD be provided separately from the [dataset instance artifacts](#term) that conform to the structure defined by that [Schema](#meta) collection object.
* [Schema](#meta) collection object MAY be provided through the structure and/or schema of the delivery mechanism (e.g., database tables).

## Examples

There are many scenarios that would result in an update to the [Schema](#meta) metadata. These scenarios include but are not limited to:

* [Adding a new column](#appendix.examples:metadata.addingnewcolumns)
* [Removing a column](#appendix.examples:metadata.removingcolumns)
* [Changing column metadata](#appendix.examples:metadata.changingcolumnmetadata)
* [FOCUS Version has changed](#appendix.examples:metadata.focusversionchanged)
* [Data Generator Version has changed](#appendix.examples:metadata.schemametadatatofocusdatareference)
* [Correcting schema metadata errors](#appendix.examples:metadata.datageneratormetadataerrorcorrection)

For an example of the FOCUS schema metadata, please refer to: [Schema Metadata Example](#supportedfeatures.schemametadata).

## Metadata ID

Schema

## Metadata Name

Schema

## Version Introduced

1.0
