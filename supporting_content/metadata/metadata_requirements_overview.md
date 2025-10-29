# Metadata Requirements Overview

## Metadata structure overview

Metadata

Metadata -> DataGenerator
Metadata -> DataGenerator -> DataGenerator

Metadata -> DatasetInstance
Metadata -> DatasetInstance -> FocusDatasetId
Metadata -> DatasetInstance -> DatasetInstanceId
Metadata -> DatasetInstance -> DatasetInstanceName

Metadata -> Schema
Metadata -> Schema -> SchemaId
Metadata -> Schema -> CreationDate
Metadata -> Schema -> FocusVersion
Metadata -> Schema -> DataGeneratorVersion
Metadata -> Schema -> DatasetInstanceId

Metadata -> Schema -> ColumnDefinition
Metadata -> Schema -> ColumnDefinition -> ColumnName
Metadata -> Schema -> ColumnDefinition -> DataType
Metadata -> Schema -> ColumnDefinition -> Deprecated
Metadata -> Schema -> ColumnDefinition -> NumericPrecision
Metadata -> Schema -> ColumnDefinition -> NumberScale
Metadata -> Schema -> ColumnDefinition -> PreviousColumnName
Metadata -> Schema -> ColumnDefinition -> ProviderTagPrefixes
Metadata -> Schema -> ColumnDefinition -> StringEncoding
Metadata -> Schema -> ColumnDefinition -> StringMaxLength

Metadata -> Recency
Metadata -> Recency -> DatasetInstanceId
Metadata -> Recency -> DatasetInstanceComplete
Metadata -> Recency -> DatasetInstanceLastUpdated
Metadata -> Recency -> RecencyLastUpdated

Metadata -> Recency -> TimeSectors
Metadata -> Recency -> TimeSectors -> TimeSectorComplete
Metadata -> Recency -> TimeSectors -> TimeSectorLast Updated
Metadata -> Recency -> TimeSectors -> TimeSectorStart
Metadata -> Recency -> TimeSectors -> TimeSectorEnd

## Metadata

### Metadata - Orig

* FOCUS Metadata SHOULD be provided in a format that is accessible programmatically, such as a file, website, API, or table.
* Providers SHOULD provide documentation on their implementation of the FOCUS metadata.

### Metadata - Refinement

Metadata adheres to the following requirements:

* Data generators SHOULD provide FOCUS metadata in a format that is accessible programmatically, such as a file, website, API, or table.
* Data generators SHOULD provide documentation on their implementation of the FOCUS metadata.

## Data Generator

### Data Generator - Orig

* The FOCUS Data Generator metadata MUST be provided.
* This metadata MUST be of type Object and MUST NOT contain null values.

### Data Generator - Refinement

DataGenerator adheres to the following requirements:

* DataGenerator MUST be present in Metadata.
* DataGenerator MUST be of type Object.
* DataGenerator MUST NOT be null.

## Dataset Instance

### Dataset Instance - Orig

* Reference to FOCUS Data:
  * FOCUS data artifacts, whether they are data files, data streams, or data tables, MUST provide a clear reference to the dataset instance of the data.
  * This reference MUST be retrievable without inspection of the contents of the FOCUS data within the data artifact.
  * For some delivery mechanisms such as database tables, the provider may rely on the schema functionality of the providing system.
* Dataset Instance Metadata Creation:
  * For every dataset instance provided by the Data Generator, a dataset instance metadata object MUST be supplied.
* Dataset Instance Metadata Updates:
  * Should a property of the dataset instance be updated, the expectation is that the dataset instance metadata object is updated to reflect the change. This ensures that the dataset instance metadata object is always accurate.

### Dataset Instance - Refinement V2

DatasetInstance adheres to the following requirements:

* DatasetInstance MUST be present in Metadata.
* DatasetInstance MUST be structured as a collection of objects.
* DatasetInstance MUST NOT be null.
* DatasetInstance collection MUST contain at least one object for every FOCUS dataset supported by the Data Generator.
* DatasetInstance object MUST NOT be null.
* DatasetInstance object MUST be associated with one and only one FOCUS dataset.

### Dataset Instance - Refinement V1

DatasetInstance adheres to the following requirements:

* DatasetInstance MUST be provided for every dataset instance provided by the data generator.
* DatasetInstance MUST provide a reference to the dataset instance of the dataset artifact.
* DatasetInstance MUST be retrievable independently from the dataset artifact it describes.
* DatasetInstance MAY be provided through the structure and/or schema of the delivery mechanism (e.g., database tables).
* DatasetInstance SHOULD be updated when a data generator updates the corresponding dataset artifact.

## Recency

### Recency - Orig

* FOCUS Datasets:
  * FOCUS datasets, regardless of delivery mechanism, MAY provide metadata indicating the recency of the data.
  * This metadata MUST be retrievable without inspection of the contents of the FOCUS data within the data artifact.
* Dataset Updates:
  * When a dataset is updated by the [Data Generator](#datagenerator) the supplied recency metadata corresponding to the dataset should be updated to indicate that the dataset has been updated.
  * Example scenarios include but are not limited to:
    * [Updating an overtime dataset recency metadata](#addingnewcolumns)
    * [Updating a non over-time dataset recency metadata](#changingcolumnmetadata)

### Recency - Refinement V2

Recency adheres to the following requirements:

* Recency MAY be present in Metadata.
* Recency MUST be structured as a collection of objects.
* Recency MUST NOT be null.
* Recency collection MAY contain one and only one object for every DatasetInstance.
* Recency object MUST NOT be null.
* Recency object MUST be associated with one and only one FOCUS DatasetInstance.
* Recency object MUST be retrievable without inspection of the contents of FOCUS dataset instance artifacts.
* Recency object SHOULD be updated when a data generator updates the corresponding dataset instance artifact.

### Recency - Refinement V1

Recency adheres to the following requirements:

* Recency MAY be present in Metadata.
* Recency MUST be retrievable without inspection of the contents of the FOCUS data within the data artifact.
* Recency SHOULD be updated when a data generator updates the corresponding dataset artifact.

## Time Sectors

### Time Sectors Orig

* This metadata MUST be present in the FOCUS metadata recency when the dataset represents data over time.
* This metadata MUST be of type array and MUST NOT contain null values.
* When datasets are updated the corresponding time sector MUST be created/updated.

### Time Sectors Current

TimeSectors adheres to the following requirements:

* TimeSectors MUST be present in Recency when the the associated FOCUS dataset is defined as a time series dataset.
* TimeSectors MUST be structured as a collection of objects.
* TimeSectors MUST NOT be null.
* TimeSectors collection MUST contain at least one object.
* TimeSectors object MUST NOT be null.
* TimeSectors objects MUST be updated, if already present, or added to the collection whenever Data Generator updates or provides new dataset artifacts.

## Schema

### Schema - Orig

* Reference to FOCUS Data
  * FOCUS [*dataset-instance-artifacts*](#glossary:dataset-instance-artifacts), whether they are data files, data streams, or data tables, MUST provide a clear reference to the schema of the data.
  * This reference MUST be retrievable without inspection of the contents of the FOCUS data within the data artifact. 
  * For some delivery mechanisms such as database tables, the provider may rely on the schema functionality of the providing system.
  * It is recommended that the schema reference be provided as an external reference rather than included in full as metadata accompanying the data artifact. This allows for easier understanding of when changes to the schema of the [*FOCUS datasets*](#glossary:FOCUS-dataset) occurs.
* Schema Metadata Creation
  * Should the provider change the structure of the supplied FOCUS dataset instance artifact, a new schema metadata object MUST be supplied. These scenarios include but are not limited to:
  * [Adding a new column](#addingnewcolumns)
  * [Removing a column](#removingcolumns)
  * [Changing column metadata](#changingcolumnmetadata)
  * [FOCUS Version has changed](#focusversionchanged)
  * [Data Generator Version has changed](#schemametadatatofocusdatareference)
  * [Correcting schema metadata errors](#providermetadataerrorcorrection)
* Schema Metadata Updates:
  * Should there be an error where the schema metadata object does not match the schema of the FOCUS dataset instance artifact, the provider MUST update the schema metadata object to match the schema of the FOCUS dataset instance artifact. This is to ensure that the schema metadata object is always accurate.

### Schema - Refinement V2

Schema adheres to the following requirements:

* Schema MUST be present in Metadata.
* Schema MUST be structured as a collection of objects.
* Schema MUST NOT be null.
* Schema collection MUST contain at least one object for every FOCUS dataset instance provided by the data generator.
* Schema object MUST NOT be null.
* Schema object MUST be added to the collection whenever the structure of the FOCUS dataset instance artifacts changes (including, but not limited to, additions or removals of columns, modifications to any ColumnDefinition, or updates to the FOCUSVersion or DataGeneratorVersion).
* Schema object MUST be referenced by FOCUS dataset instance artifacts that conform to the structure defined by that Schema object.
* Schema object MUST define the exact structure of the FOCUS dataset instance artifacts that reference it.
* Schema object MUST be retrievable independently from the FOCUS dataset instance artifacts that conform to the structure defined by that Schema object.
* Schema object SHOULD be provided separately from the FOCUS dataset instance artifacts that conform to the structure defined by that Schema object.
* Schema object MAY be provided through the structure and/or schema of the delivery mechanism (e.g., database tables).

### Schema - Refinement V1

Schema adheres to the following requirements:

* Schema MUST be provided for every FOCUS dataset provided by the data generator.
* Schema MUST provide a reference to the FOCUS dataset of the dataset artifact.
* Schema MUST be retrievable independently from the dataset it describes.
* Schema MAY be provided through the structure and/or schema of the delivery mechanism (e.g., database tables).
* Schema SHOULD be provided separately from the dataset artifact it describes.
* Schema MUST be updated via a new metadata object when a data generator changes the structure of a FOCUS dataset.

## Column definition

### Column Definition - Orig

TODO

### Column Definition - Refinement V2

TODO

### Column Definition - Refinement V1

ColumnDefinition adheres to the following requirements:

* ColumnDefinition MUST be present in Schema.
* ColumnDefinition MUST be of type Object.
* ColumnDefinition MUST NOT contain null values.
