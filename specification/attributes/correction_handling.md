# Correction Handling

Corrections are line items that appear in the FOCUS data set to support any scenarios where providers need to adjust a charge to a consumer. These scenarios include:

* [*Refund*](#glossary:refund) - experiencing a billing technical error (i.e. charging the incorrect rate/volume for a service line item)
* [*Credit*](#glossary:credit) - providing a promotional benefit (i.e. migration incentives or new service incentives)
* Metadata Corrections
* Late Arriving Charges

Refunds are applied to retrospective charge records where the usage has already been incurred whereas credits are applied in a forward looking perspective and are consumed ('burned-down') by future usage.

include original summary linking out to correction or refund attributes as appropriate

DO NOT INCLUDE REQUIREMENTS IN THIS SECTION

correction to non cost and non usage columns i.e. metadata MAY be applied retrospectively

do example for late arriving costs

Matrix of different scenarios:

* Correction curent period
* Correction previous period
* Refund current period
* Refund previous period
* Credit current period
* Credit previous period
* Late arriving costs

## Attribute ID

CorrectionHandling

## Attribute Name

Correction Handling

## Description

Indicates how to include and apply discounts to usage charges or rows in a FOCUS dataset.

## Requirements

* TODO

## Exceptions

None

## Introduced (version)

1.3
