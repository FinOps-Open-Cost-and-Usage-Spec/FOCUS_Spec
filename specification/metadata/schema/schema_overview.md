# Schema

The schema metadata object and its content provide information about the structure of the data provided.

## Requirements

* Schema metadata MUST be provided for every FOCUS dataset provided by the data generator.
* Schema metadata MUST provide a reference to the FOCUS dataset of the dataset artifact.
* Schema metadata MUST be retrievable independently from the dataset it describes.
* Schema metadata MAY be provided through the structure and/or schema of the delivery mechanism (e.g., database tables).
* Schema metadata SHOULD be provided separately from the dataset artifact it describes.
* Schema metadata MUST be updated via a new metadata object when a data generator changes the structure of a FOCUS dataset.

## Examples

There are many scenarios that would result in an update to the Schema metadata.  These scenarios include but are not limited to:

* [Adding a new column](#addingnewcolumns)
* [Removing a column](#removingcolumns)
* [Changing column metadata](#changingcolumnmetadata)
* [FOCUS Version has changed](#focusversionchanged)
* [Data Generator Version has changed](#schemametadatatofocusdatareference)
* [Correcting schema metadata errors](#providermetadataerrorcorrection)

For an example of the FOCUS schema metadata, please refer to: [Schema Metadata Example](#schemametadata).
