# Charge Category

Charge Category represents the highest-level classification of a [*charge*](#glossary:charge) based on the nature of how it is billed. Charge Category is commonly used to identify and distinguish between types of [*charges*](#glossary:charge) that may require different handling.

## Requirements

ChargeCategory MUST adhere to the following requirements:

* ChargeCategory MUST be of type String.
* ChargeCategory MUST NOT be null.
* ChargeCategory MUST be one of the allowed values.
* When the *charge* does not aggregate multiple classifications, ChargeCategory MUST adhere to the following requirements:
  * ChargeCategory MUST be "Usage" when the *charge* represents consumption of a service or resource.
  * ChargeCategory MUST be "Purchase" when the *charge* represents acquisition of a service, resource, or *commitment*.
  * ChargeCategory MUST be "Tax" when the *charge* represents taxes levied by the relevant authorities.
  * ChargeCategory MUST be "Credit" when the *charge* represents a financial incentive or allowance unrelated to other *charges*.
  * ChargeCategory MUST be "Adjustment" when the *charge* represents a billing modification that does not fall into other ChargeCategories.
* When the *charge* aggregates multiple classifications, ChargeCategory MUST adhere to the following requirements:
  * ChargeCategory MAY be "Usage" when the record aggregates *charges* across multiple allowed values other than "Tax" (for example, aggregation of "Usage" and "Credit" is allowed, but not "Usage" and "Tax").

## Implementation Context

Unlike the [CostAndUsage](#datasets.costandusage) dataset, which requires strict categorization per row, [InvoiceDetail](#datasets.invoicedetail) records are designed to align with physical or electronic invoice line items. Invoice issuers frequently aggregate different types of transactions (e.g., combining base usage and promotional credits) into a single billed line item. To accurately reflect the issued invoice without breaking schema validation, the `InvoiceDetail` dataset permits the `"Usage"` category to represent an aggregate of multiple charge types, provided that `"Tax"` charges are kept distinctly separate.

## Column ID

ChargeCategory

## Display Name

Charge Category

## Description

Represents the highest-level classification of a *charge* based on the nature of how it is billed.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

## Allowed Values

| Value      | Description                                                                                                                                    |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------|
| Usage      | Positive or negative *charges* based on the quantity of a service or resource that was consumed over a given period of time including refunds. |
| Purchase   | Positive or negative *charges* for the acquisition of a service or resource bought upfront or on a recurring basis including refunds. |
| Tax        | Positive or negative applicable taxes that are levied by the relevant authorities including refunds. Tax *charges* may vary depending on factors such as the location, jurisdiction, and local or federal regulations. |
| Credit     | Positive or negative *charges* granted by the service provider for various scenarios (e.g., promotional credits, corrections to promotional credits). |
| Adjustment | Positive or negative *charges* the service provider applies that do not fall into other category values. |

## Introduced (version)

1.4
