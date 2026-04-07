# Delivery Handling

## Overview

The Delivery Handling attribute defines how a [*data generator*](#metadata.datagenerator) delivers a [*FOCUS dataset*](#glossary:FOCUS-dataset) to a customer.

A [*dataset instance*](#glossary:dataset-instance) represents a specific implementation of a [*FOCUS dataset*](#glossary:FOCUS-dataset). A [*dataset instance artifact*](#glossary:dataset-instance-artifact) is the physical delivery of that instance, representing one or more records, independent of storage or transport boundaries (e.g., files, batches, or responses).

### Delivery Mechanisms

FOCUS recognizes two *FOCUS dataset* delivery mechanisms:

* Overwrite: Each delivery provides a complete snapshot, superseding any previously delivered *dataset artifact* for the same [*delivery scope*](#glossary:delivery-scope) (e.g., temporal grouping such as a [*billing period*](#glossary:billing-period) or non-temporal, logical grouping such as a [*contract*](#glossary:contract)).
* Append: Each delivery adds new data, while previously delivered *dataset artifacts* are preserved.

Overwrite and Append mechanisms are not mutually exclusive, and hybrid implementations are common in practice, allowing data generators to meet specific technical and auditability requirements.

For example, for Cost and Usage *FOCUS datasets*, a data generator may use Overwrite mechanism for *dataset artifacts* corresponding to an [*open billing period*](#glossary:open-billing-period), ensuring the snapshot reflects the most recent state, while using Append mechanism for [*closed billing periods*](#glossary:closed-billing-period) to preserve historical data and support auditing of corrections to previously *closed billing periods* (i.e., [*charges*](#glossary:charge) with Charge Class set to "Correction").

For more information on corrections, see the [Correction Handling attribute](#attributes.correctionhandling).

#### Overwrite Delivery

In the Overwrite delivery mechanism, each *dataset artifact* provides a complete snapshot of data for a predefined scope (e.g., a *billing period* or a logical grouping), based on the data available at the time of delivery. Subsequent *dataset artifacts* for the same scope typically reflect updates, additions, or omissions relative to the previous snapshot. This mechanism provides delivery simplicity, but it lacks inherent auditability. Dataset artifact size typically increases within a delivery scope as underlying data accumulates, but total data volume remains the lowest compared to Append delivery as each dataset artifact supersedes previously delivered ones for the same delivery scope.

Subsequent *dataset artifacts* using the Overwrite mechanism may include the following:

* Unchanged records are carried over.
* Updated records overwrite previous values.
* Additional records supplement previously delivered data.
* Omitted records are removed if no longer applicable.

#### Append Delivery

In the Append delivery mechanism, a subsequent *dataset artifact* appends new records without modifying or removing previously delivered ones. This mechanism inherently supports auditability, as all original and correction records are retained. Total data volume increases over time as all delivered dataset artifacts are preserved, and is typically higher compared to Overwrite delivery.

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

Defines how a [*data generator*](#metadata.datagenerator) delivers a *FOCUS dataset* to a customer.

## Requirements

DeliveryHandling MUST adhere to the following requirements:

* *FOCUS dataset* MUST have its mechanism(s) for delivering *dataset artifacts* documented and accessible to practitioners (including whether Overwrite or Append is used and under which conditions).
* *FOCUS dataset* MUST NOT require practitioners to deduplicate records within or across delivered dataset artifacts.
* When using Overwrite delivery mechanism, *FOCUS dataset* MUST adhere to the following additional requirements:
  * *FOCUS dataset* MUST represent a complete snapshot for a given [*delivery scope*](#glossary:delivery-scope).
  * *FOCUS dataset* MUST supersede all previously delivered *dataset artifacts* for the same *delivery scope*.
* *FOCUS dataset* MUST preserve all previously delivered *dataset artifacts* when using Append delivery mechanism.
* *FOCUS dataset* SHOULD have delivered *dataset artifacts* accompanied by corresponding [FOCUS Metadata](#metadata).
* *FOCUS dataset* MUST have its mechanism for correlating *dataset artifact* with the [FOCUS Metadata Schema object](#metadata.schema) documented and accessible to practitioners when the Metadata is delivered.

## Exceptions

None

## Introduced (version)

1.4
