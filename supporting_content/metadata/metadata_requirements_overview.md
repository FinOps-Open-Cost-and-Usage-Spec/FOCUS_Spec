# Metadata Requirements Overview

## Metadata structure overview

- Metadata - **object**
  - DataGenerator - **object**
    - DataGenerator - *property*
  - DatasetInstance - **collection of objects**
    - FocusDatasetId - *property*
    - DatasetInstanceId - *property*
    - DatasetInstanceName - *property*
  - Schema - **collection of objects**
    - SchemaId - *property*
    - CreationDate - *property*
    - FocusVersion - *property*
    - DataGeneratorVersion - *property*
    - DatasetInstanceId - *property*
    - ColumnDefinition - **collection of objects**
      - ColumnName - *property*
      - DataType - *property*
      - Deprecated - *property*
      - NumericPrecision - *property*
      - NumberScale - *property*
      - PreviousColumnName - *property*
      - ProviderTagPrefixes - *property*
      - StringEncoding - *property*
      - StringMaxLength - *property*
  - Recency - **collection of objects**
    - DatasetInstanceId - *property*
    - DatasetInstanceComplete - *property*
    - DatasetInstanceLastUpdated - *property*
    - RecencyLastUpdated - *property*
    - TimeSectors - **collection of objects**
      - TimeSectorComplete - *property*
      - TimeSectorLast Updated - *property*
      - TimeSectorStart - *property*
      - TimeSectorEnd - *property*

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

* DataGenerator MUST be present in the [Metadata](#metadata).
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

### Dataset Instance - Refinement

DatasetInstance adheres to the following requirements:

* DatasetInstance MUST be present in the [Metadata](#metadata).
* DatasetInstance MUST be structured as a collection of objects.
* DatasetInstance MUST NOT be null.
* DatasetInstance collection MUST contain at least one object for every [*FOCUS dataset*](#glossary:FOCUS-dataset) supported by the data generator.
* DatasetInstance object MUST NOT be null.
* DatasetInstance object MUST be associated with one and only one *FOCUS dataset*.

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

### Recency - Refinement

Recency adheres to the following requirements:

* Recency MAY be present in the [Metadata](#metadata).
* Recency MUST be structured as a collection of objects.
* Recency MUST NOT be null.
* Recency collection MUST NOT contain null objects.
* Recency collection MAY contain one and only one object for every [DatasetInstance](#datasetinstance) object.
* Recency collection object MUST be associated with one and only one DatasetInstance object.
* Recency collection object MUST be retrievable without inspection of the contents of [*dataset instance artifacts*](#glossary:dataset-instance-artifact).
* Recency collection object SHOULD be updated when the data generator updates the corresponding *dataset instance artifact*.

## Time Sectors

### Time Sectors - Orig

* This metadata MUST be present in the FOCUS metadata recency when the dataset represents data over time.
* This metadata MUST be of type array and MUST NOT contain null values.
* When datasets are updated the corresponding time sector MUST be created/updated.

### Time Sectors - Refinement

TimeSectors adheres to the following requirements:

* TimeSectors MUST be present in an object within the [Recency](#recency) collection when the the associated *FOCUS dataset* is defined as a time series dataset.
* TimeSectors MUST be structured as a collection of objects.
* TimeSectors MUST NOT be null.
* TimeSectors collection MUST contain at least one object.
* TimeSectors collection MUST NOT contain null objects.
* TimeSectors collection object MUST be updated, if already present, or added to the collection whenever the data generator updates or provides new dataset artifacts.

## Schema

### Schema - Orig

* Reference to FOCUS Data
  * FOCUS [*dataset instance artifacts*](#glossary:dataset-instance-artifacts), whether they are data files, data streams, or data tables, MUST provide a clear reference to the schema of the data.
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

### Schema - Refinement

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

## Column Definition

### Column Definition - Orig

* This metadata MUST be present in the FOCUS metadata schema.
* This metadata MUST be of type Object and MUST NOT contain null values.

### Column Definition - Refinement

ColumnDefinition adheres to the following requirements:

* ColumnDefinition MUST be present in an object within the [Schema](#schema) collection.
* ColumnDefinition MUST be structured as a collection of objects.
* ColumnDefinition MUST NOT be null.
* ColumnDefinition collection MUST contain one and only one object for every column provided in *dataset instance artifacts* that reference the parent Schema object.
* ColumnDefinition collection MUST NOT contain null objects.
