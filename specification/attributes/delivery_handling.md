# Delivery Handling

## Overview

The Delivery Handling attribute defines how a data generator delivers a *dataset artifact* to a customer.

### Delivery Mechanisms

FOCUS supports two delivery mechanisms: 

* Overwrite. Existing rows are replaced.
* Append. Existing rows are preserved.

These mechanisms are not mutually exclusive, and hybrid implementations are common, allowing data generators to meet specific technical and auditability requirements.

For more information on corrections, see the [Correction Handling attribute](*correctionhandling).

#### Overwrite Delivery

In the Overwrite delivery mechanism, each *dataset artifact* provides a complete snapshot of data for a given [*billing period*](#glossary:billing-period), based on the data available at the time of delivery. Subsequent dataset artifacts typically reflect updates, additions, or omissions relative to the previous snapshot. This mechanism provides delivery simplicity, but it lacks inherent auditability. 

Subsequent dataset artifacts using the Overwrite mechanism may include the following:

* Unchanged records are carried over.
* Updated records overwrite previous values.
* Additional records supplement previously delivered data.
* Omitted records are removed if no longer applicable.

#### Append Delivery

In the Append delivery mechanism, a subsequent dataset artifact appends new records without modifying or removing previously delivered ones. This mechanism inherently supports auditability, as all original and correction records are retained.

Subsequent dataset artifacts using the Replace mechanism may include the following:

* Unchanged recorded are not included.
* Updated records are recorded as new entries, representing the difference.
* Additional records supplement previously delivered data.
* Ommitted records are recorded as new entries, representing the reversal.

## Attribute ID

DeliveryHandling

## Attribute Name

Delivery Handling

## Description

Defines how a data generator delivers a *dataset artifact* to a customer.

## Requirements

The delivery of a *dataset artifact* adheres to the following requirements:

* A FOCUS *dataset artifact* SHOULD be delivered using either the Overwrite or Append delivery mechanism.
* The delivery mechanism(s) used to correct FOCUS dataset artifacts MUST be documented by the data generator.

## Exceptions

None

## Introduced (version)

1.3
