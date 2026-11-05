# Unit Price

The [Unit Price](#col) represents the service-provider-published unit price for a single [Pricing Unit](#col) of the associated [SKU Price](#term). This price is denominated in the [Pricing Currency](#col).

When [Contract ID](#col) is null, the [Unit Price](#col) represents the standard public price. When [Contract ID](#col) is populated, the [Unit Price](#col) represents a price specific to that contract, and [Unit Price Type](#col) indicates which kind (e.g., a "Base" list price fixed for the contract, or a "Contracted" rate).

## Requirements

[UnitPrice](#col) MUST adhere to the following requirements:

* [UnitPrice](#col) MUST be of type Decimal.
* [UnitPrice](#col) MUST conform to [NumericFormat](#attr) requirements.
* [UnitPrice](#col) MUST NOT be null.
* [UnitPrice](#col) MUST be a non-negative decimal value.
* [UnitPrice](#col) MUST be denominated in the [PricingCurrency](#col).

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

UnitPrice

## Display Name

Unit Price

## Description

The service-provider-published unit price for a single *[Pricing Unit](#col)* of the associated [SKU Price](#term).

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#ds)                                     |
| Operating Model Conditions | Not applicable                                       |
| Column type                | Metric                                               |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | Decimal                                              |
| Value format               | [Numeric Format](#attr)                              |
| Number range               | Any valid non-negative decimal value                 |

## Version Introduced

Preview: 1.5
