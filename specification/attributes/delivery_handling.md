# Delivery Handling

## Overview

A [*dataset instance*](#glossary:dataset-instance) represents a specific implementation of a [*FOCUS dataset*](#glossary:FOCUS-dataset). A [*dataset instance artifact*](#glossary:dataset-instance-artifact) is the physical delivery of that instance, representing one or more records, independent of storage or transport boundaries (e.g., files, batches, or responses).

The Delivery Handling attribute defines how a data generator delivers *dataset artifacts* to a customer.

### Delivery Mechanisms

FOCUS recognizes two delivery mechanisms:

* Overwrite: Each delivery provides a complete snapshot, superseding any previously delivered *dataset artifact* for the same [*delivery scope*](#glossary:delivery-scope) (e.g., temporal grouping such as a [*billing period*](#glossary:billing-period) or non-temporal, logical grouping such as a [*contract*](#glossary:contract)).
* Append: Each delivery adds new data, while previously delivered dataset artifacts are preserved.

Overwrite and Append mechanisms are not mutually exclusive, and hybrid implementations are common in practice, allowing data generators to meet specific technical and auditability requirements.

For example, for Cost and Usage [*FOCUS dataset instances*](#glossary:FOCUS-dataset-instance), a data generator may use Overwrite mechanism for *dataset artifacts* corresponding to an [*open billing period*](#closed-billing-period), ensuring the snapshot reflects the most recent state, while using Append mechanism for [*closed billing periods*](#glossary:closed-billing-period) to preserve historical data and support auditing of corrections to previously *closed billing periods* (i.e., [*charges*](#glossary:charge) with Charge Class set to "Correction").

For more information on corrections, see the [Correction Handling attribute](*correctionhandling).

#### Overwrite Delivery

In the Overwrite delivery mechanism, each *dataset artifact* provides a complete snapshot of data for a predefined scope (e.g., a *billing period* or a logical grouping), based on the data available at the time of delivery. Subsequent *dataset artifacts* for the same scope typically reflect updates, additions, or omissions relative to the previous snapshot. This mechanism provides delivery simplicity, but it lacks inherent auditability.

Subsequent *dataset artifacts* using the Overwrite mechanism may include the following:

* Unchanged records are carried over.
* Updated records overwrite previous values.
* Additional records supplement previously delivered data.
* Omitted records are removed if no longer applicable.

#### Append Delivery

In the Append delivery mechanism, a subsequent *dataset artifact* appends new records without modifying or removing previously delivered ones. This mechanism inherently supports auditability, as all original and correction records are retained.

Subsequent *dataset artifacts* using the Append mechanism may include the following:

* Unchanged records are not included.
* Updated records are recorded as new entries, representing the net effect on aggregated quantities or costs.
* Additional records supplement previously delivered data.
* Omitted records are recorded as new entries, representing the reversal.

## Attribute ID

DeliveryHandling

## Attribute Name

Delivery Handling

## Description

Defines how a data generator delivers a *dataset artifact* to a customer.

## Requirements

Dataset Instance delivered by a data generator MUST adhere to the following Delivery Handling requirements:

* Dataset Instance MUST have its mechanism(s) for delivering *dataset artifacts* documented and accessible to practitioners (including whether Overwrite or Append is used and under which conditions).
* Dataset Instance MUST have delivered *dataset artifacts* accompanied by corresponding [FOCUS Metadata](#metadata).
* Dataset Instance MUST have its mechanism for correlating *dataset artifact* with the corresponding [FOCUS Metadata Schema object](#metadata.schema) documented and accessible to practitioners.
* Dataset Instance MUST have information contained in the delivered *dataset artifacts* accurately reflected in corresponding Metadata elements.
* When using Append delivery mechanism, Dataset instance adheres to the following additional requirements:
  * Dataset instance MUST NOT include updates to previously delivered records.
  * Dataset instance MUST NOT include omissions of previously delivered records.

## Exceptions

None

## Introduced (version)

1.4
