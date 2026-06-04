# Schema

The schema metadata object and its content provide information about the structure of the data provided.

## Requirements

Schema adheres to the following requirements:

* Schema MUST be present in the [Metadata](#metadata).
* Schema MUST be structured as a collection of objects.
* Schema MUST NOT be null.
* Schema collection MUST contain at least one object for every [DatasetInstance](#datasetinstance) object.
* Schema collection MUST NOT contain null objects.
* Schema collection object MUST be associated with one and only one DatasetInstance object.
* Schema collection object MUST be added to the collection whenever the structure of the [*dataset instance artifacts*](#glossary:dataset-instance-artifact) changes (including, but not limited to, additions or removals of columns, modifications to any ColumnDefinition, or updates to the FOCUSVersion or DataGeneratorVersion).
* Schema collection object MUST be referenced by *dataset instance artifacts* that conform to the structure defined by that Schema collection object.
* Schema collection object MUST define the exact structure of the *dataset instance artifacts* that reference it.
* Schema collection object MUST be retrievable independently from the *dataset instance artifacts* that conform to the structure defined by that Schema collection object.
* Schema collection object SHOULD be provided separately from the *dataset instance artifacts* that conform to the structure defined by that Schema collection object.
* Schema collection object MAY be provided through the structure and/or schema of the delivery mechanism (e.g., database tables).

## Examples

There are many scenarios that would result in an update to the Schema metadata.  These scenarios include but are not limited to:

* [Adding a new column](#addingnewcolumns)
* [Removing a column](#removingcolumns)
* [Changing column metadata](#changingcolumnmetadata)
* [FOCUS Version has changed](#focusversionchanged)
* [Data Generator Version has changed](#schemametadatatofocusdatareference)
* [Correcting schema metadata errors](#providermetadataerrorcorrection)

For an example of the FOCUS schema metadata, please refer to: [Schema Metadata Example](#schemametadata).

## Metadata ID

Schema

## Metadata Name

Schema

## Introduced (version)

1.0
