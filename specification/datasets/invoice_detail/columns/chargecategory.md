# Charge Category

[Charge Category](#col) represents the highest-level classification of a [charge](#term) based on the nature of how it is billed. [Charge Category](#col) is commonly used to identify and distinguish between types of [charges](#term) that may require different handling.

## Requirements

[ChargeCategory](#col) MUST adhere to the following requirements:

* [ChargeCategory](#col) MUST be of type String.
* [ChargeCategory](#col) MUST NOT be null.
* [ChargeCategory](#col) MUST be one of the allowed values.
* When the [charge](#term) does not aggregate multiple classifications, [ChargeCategory](#col) MUST adhere to the following requirements:
  * [ChargeCategory](#col) MUST be ["Usage"](#val:ChargeCategory) when the [charge](#term) represents consumption of a service or resource.
  * [ChargeCategory](#col) MUST be ["Purchase"](#val:ChargeCategory) when the [charge](#term) represents acquisition of a service, resource, or [commitment](#term).
  * [ChargeCategory](#col) MUST be ["Tax"](#val:ChargeCategory) when the [charge](#term) represents taxes levied by the relevant authorities.
  * [ChargeCategory](#col) MUST be ["Credit"](#val:ChargeCategory) when the [charge](#term) represents a financial incentive or allowance unrelated to other [charges](#term).
  * [ChargeCategory](#col) MUST be ["Adjustment"](#val:ChargeCategory) when the [charge](#term) represents a billing modification that does not fall into other ChargeCategories.
* When the [charge](#term) aggregates multiple classifications, [ChargeCategory](#col) MUST adhere to the following requirements:
  * [ChargeCategory](#col) MAY be ["Usage"](#val:ChargeCategory) when the record aggregates [charges](#term) across multiple allowed values other than ["Tax"](#val:ChargeCategory) (e.g., aggregation of ["Usage"](#val:ChargeCategory) and ["Credit"](#val:ChargeCategory) is allowed, but not ["Usage"](#val:ChargeCategory) and ["Tax"](#val:ChargeCategory)).

## Allowed Values

| Value      | Description                                                                                                                                    |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------|
| Usage      | Positive or negative *charges* based on the quantity of a service or resource that was consumed over a given period of time including refunds. |
| Purchase   | Positive or negative *charges* for the acquisition of a service or resource bought upfront or on a recurring basis including refunds. |
| Tax        | Positive or negative applicable taxes that are levied by the relevant authorities including refunds. Tax *charges* may vary depending on factors such as the location, jurisdiction, and local or federal regulations. |
| Credit     | Positive or negative *charges* granted by the service provider for various scenarios (e.g., promotional credits, corrections to promotional credits). |
| Adjustment | Positive or negative *charges* the service provider applies that do not fall into other category values. |

## Implementation Guidance

Unlike the [CostAndUsage](#ds) dataset, which requires strict categorization per row, [InvoiceDetail](#ds) records are designed to align with physical or electronic invoice line items. When the invoice does not provide an explicit charge category for a line item, a single line item may inherently represent a mix of charge categories (e.g., combining base usage and promotional credits). To accurately reflect the issued invoice without breaking schema validation, the `InvoiceDetail` dataset permits the ["Usage"](#val:ChargeCategory) category to represent an aggregate of multiple charge categories, provided that ["Tax"](#val:ChargeCategory) charges are kept distinctly separate.

## Column ID

ChargeCategory

## Display Name

Charge Category

## Description

Represents the highest-level classification of a [charge](#term) based on the nature of how it is billed.

## Content Constraints

| Constraint                 | Value                                      |
| :------------------------- | :----------------------------------------- |
| Dataset                    | [Invoice Detail](#ds)                      |
| Operating model conditions | Not applicable                             |
| Column type                | Dimension                                  |
| Feature level              | Mandatory                                  |
| Allows nulls               | False                                      |
| Data type                  | String                                     |
| Value format               | Allowed values                             |

## Version Introduced

1.4
