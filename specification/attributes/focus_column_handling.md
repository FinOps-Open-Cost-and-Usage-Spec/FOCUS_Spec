# FOCUS Column Handling

Columns within FOCUS include an ID and a display name. Column IDs are used in [dataset artifacts](#term) and display names can be used in report output and other descriptive content, like documentation. Column IDs provided in a [FOCUS dataset](#term) follow consistent naming conventions for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

## Requirements

Column conforming to [FocusColumnHandling](#attr) attribute MUST adhere to the following requirements:

* [FOCUS column](#term) MUST use a Display Name consistent with the Column ID, with spaces inserted between words (e.g., Column ID `BillingAccountName` and Display Name `Billing Account Name`, Column ID `BillingAccountId` and Display Name `Billing Account ID`).
* [FOCUS column](#term) MUST use [Pascal case](#term) in the Column ID.
* [FOCUS column](#term) MUST use only alphanumeric characters in the Column ID.
* [FOCUS column](#term) MUST NOT include special characters in the Column ID.
* [FOCUS column](#term) MUST NOT use abbreviations other than `Id` in the Column ID.
* [FOCUS column](#term) SHOULD NOT use acronyms other than `Sku` in the Column ID.
* [FOCUS column](#term) SHOULD NOT exceed 50 characters in the Column ID to accommodate column length restrictions of various data repositories.
* [FOCUS column](#term) representing an identifier MUST include the `Id` suffix in the Column ID.
* [FOCUS column](#term) representing a name MUST include the `Name` suffix in the Column ID.
* [FOCUS column](#term) representing a product offering that incurred a charge MUST include `Sku` in the Column ID.
* [FOCUS column](#term) that includes the `Category` suffix in the Column ID and is not null MUST contain one of the FOCUS-defined allowed values.

## Attribute ID

FocusColumnHandling

## Attribute Name

FOCUS Column Handling

## Description

Naming conventions for [FOCUS columns](#term) appearing in a [FOCUS dataset](#term).

## Version Introduced

0.5
