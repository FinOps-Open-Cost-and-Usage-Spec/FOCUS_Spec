# FOCUS Column Handling

Columns within FOCUS include an ID and a display name. Column IDs are used in [*dataset artifacts*](#glossary:dataset-artifact) and display names can be used in report output and other descriptive content, like documentation. Column IDs provided in a [*FOCUS dataset*](#glossary:FOCUS-dataset) follow consistent naming conventions for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

## Attribute ID

FocusColumnHandling

## Attribute Name

FOCUS Column Handling

## Description

Naming conventions for columns appearing in a *FOCUS dataset*.

## Requirements

Column conforming to FocusColumnHandling attribute MUST adhere to the following requirements:

* [*FOCUS column*](#glossary:FOCUS-column) MUST use a Display Name consistent with the Column ID, with spaces inserted between words (e.g., Column ID "BillingAccountName" and Display Name "Billing Account Name").
* *FOCUS column* MUST use [*Pascal case*](#glossary:pascalcase) in the Column ID.
* *FOCUS column* MUST use only alphanumeric characters in the Column ID.
* *FOCUS column* MUST NOT include special characters in the Column ID.
* *FOCUS column* MUST NOT use abbreviations other than `Id` in the Column ID.
* *FOCUS column* SHOULD NOT use acronyms other than `Sku` in the Column ID.
* *FOCUS column* SHOULD NOT exceed 50 characters in the Column ID to accommodate column length restrictions of various data repositories.
* *FOCUS column* MUST include the `Id` suffix in the Column ID when the *FOCUS column* represents an identifier.
* *FOCUS column* MUST include the `Name` suffix in the Column ID when the *FOCUS column* represents a name.
* *FOCUS column* MUST include `Sku` in the Column ID when the *FOCUS column* represents a product offering that incurred a charge.
* *FOCUS column* MUST contain one of the FOCUS-defined allowed values when the *FOCUS column* includes `Category` suffix in the Column ID and is not null.

## Introduced (version)

0.5
