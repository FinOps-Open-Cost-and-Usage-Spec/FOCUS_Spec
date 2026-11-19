# Delivery Handling

## Overview

The [Delivery Handling](#attr) attribute defines how a [*data generator*](#metadata.datagenerator) delivers a [FOCUS dataset](#term) to a customer.

A [dataset instance](#term) represents a specific implementation of a [FOCUS dataset](#term). A [dataset instance artifact](#term) is the physical delivery of that instance, representing one or more records, independent of storage or transport boundaries (e.g., files, batches, or responses).

### Delivery Mechanisms

FOCUS recognizes two [FOCUS dataset](#term) delivery mechanisms:

* Overwrite: Each delivery provides a complete snapshot, superseding any previously delivered [dataset artifact](#term) for the same [delivery scope](#term) (e.g., temporal grouping such as a [billing period](#term) or non-temporal, logical grouping such as a [contract](#term)).
* Append: Each delivery adds new data, while previously delivered [dataset artifacts](#term) are preserved.

Overwrite and Append mechanisms are not mutually exclusive, and hybrid implementations are common in practice, allowing data generators to meet specific technical and auditability requirements.

For example, for [Cost and Usage](#ds) [FOCUS datasets](#term), a data generator may use Overwrite mechanism for [dataset artifacts](#term) corresponding to an [open billing period](#term), ensuring the snapshot reflects the most recent state, while using Append mechanism for [closed billing periods](#term) to preserve historical data and support auditing of corrections to previously [closed billing periods](#term) (i.e., [charges](#term) with [Charge Class](#col) set to "Correction").

For more information on corrections, see the [Correction Handling attribute](#attr:CorrectionHandling).

#### Overwrite Delivery

In the Overwrite delivery mechanism, each [dataset artifact](#term) provides a complete snapshot of data for a predefined scope (e.g., a [billing period](#term) or a logical grouping), based on the data available at the time of delivery. Subsequent [dataset artifacts](#term) for the same scope typically reflect updates, additions, or omissions relative to the previous snapshot. This mechanism provides delivery simplicity, but it lacks inherent auditability. Dataset artifact size typically increases within a delivery scope as underlying data accumulates, but total data volume remains the lowest compared to Append delivery as each dataset artifact supersedes previously delivered ones for the same delivery scope.

Subsequent [dataset artifacts](#term) using the Overwrite mechanism may include the following:

* Unchanged records are carried over.
* Updated records overwrite previous values.
* Additional records supplement previously delivered data.
* Omitted records are removed if no longer applicable.

#### Append Delivery

In the Append delivery mechanism, a subsequent [dataset artifact](#term) appends new records without modifying or removing previously delivered ones. This mechanism inherently supports auditability, as all original and correction records are retained. Total data volume increases over time as all delivered dataset artifacts are preserved, and is typically higher compared to Overwrite delivery.

Subsequent [dataset artifacts](#term) using the Append mechanism may include the following:

* Unchanged records are not included.
* Updated records are recorded as new entries, representing the net effect on aggregated quantities or costs.
* Additional records supplement previously delivered data.
* Omitted records are recorded as new entries, representing the reversal.

## Requirements

Dataset conforming to [DeliveryHandling](#attr) attribute MUST adhere to the following requirements:

* [FOCUS dataset](#term) MUST NOT require practitioners to deduplicate records within or across delivered dataset artifacts.
* When using Overwrite delivery mechanism, [FOCUS dataset](#term) MUST adhere to the following additional requirements:
  * [FOCUS dataset](#term) MUST represent a complete snapshot for a given [delivery scope](#term).
  * [FOCUS dataset](#term) MUST supersede all previously delivered [dataset artifacts](#term) for the same [delivery scope](#term).
* [FOCUS dataset](#term) MUST preserve all previously delivered [dataset artifacts](#term) when using Append delivery mechanism.
* [FOCUS dataset](#term) SHOULD have delivered [dataset artifacts](#term) accompanied by corresponding [FOCUS Metadata](#metadata).
* [FOCUS dataset](#term) delivery mechanism documentation MUST adhere to the following requirements:
  * [FOCUS dataset](#term) delivery mechanism documentation MUST include the delivery mechanism used (Overwrite or Append).
  * [FOCUS dataset](#term) delivery mechanism documentation MUST include the conditions under which each delivery mechanism applies when more than one delivery mechanism is used.
  * [FOCUS dataset](#term) delivery mechanism documentation MUST include the mechanism for correlating [dataset artifacts](#term) with the [FOCUS Metadata Schema object](#meta:Schema) when the Metadata is delivered.
  * [FOCUS dataset](#term) delivery mechanism documentation MUST be accessible to practitioners.

## Attribute ID

DeliveryHandling

## Attribute Name

Delivery Handling

## Description

Defines how a *data generator* delivers a [FOCUS dataset](#term) to a customer.

## Version Introduced

1.4
