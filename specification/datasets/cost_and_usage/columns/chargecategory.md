# Charge Category

[Charge Category](#col) represents the highest-level classification of a [charge](#term) based on the nature of how it is billed. [Charge Category](#col) is commonly used to identify and distinguish between types of [charges](#term) that may require different handling.

> **Preview:** The SKU Price dataset is a preview in this version of FOCUS. The requirement that [Charge Category](#col) match SKU Price [Charge Category](#col) is excluded from conformance while that dataset is a preview.

## Requirements

[ChargeCategory](#col) MUST adhere to the following requirements:

* [ChargeCategory](#col) MUST be of type String.
* [ChargeCategory](#col) MUST NOT be null.
* [ChargeCategory](#col) MUST be one of the allowed values.
* [ChargeCategory](#col) MUST be ["Usage"](#val:ChargeCategory) when the [charge](#term) represents consumption of a service or resource.
* [ChargeCategory](#col) MUST be ["Purchase"](#val:ChargeCategory) when the [charge](#term) represents acquisition of a service, resource, or [commitment](#term).
* [ChargeCategory](#col) MUST be ["Tax"](#val:ChargeCategory) when the [charge](#term) represents taxes levied by the relevant authorities.
* [ChargeCategory](#col) MUST be ["Credit"](#val:ChargeCategory) when the [charge](#term) represents a financial incentive or allowance unrelated to other charges.
* [ChargeCategory](#col) MUST be ["Adjustment"](#val:ChargeCategory) when the [charge](#term) represents a billing modification that does not fall into other ChargeCategories.
* [ChargeCategory](#col) for a given [SkuPriceId](#col) and [ServiceProviderName](#col) MUST match [SkuPrice.ChargeCategory](#col:SkuPrice.ChargeCategory) for the same [SkuPrice.SkuPriceId](#col:SkuPrice.SkuPriceId) and [SkuPrice.ServiceProviderName](#col:SkuPrice.ServiceProviderName) when [SkuPriceId](#col) is not null and [ChargeCategory](#col) is ["Usage"](#val:ChargeCategory) or ["Purchase"](#val:ChargeCategory).

## Allowed Values

| Value      | Description                                                                                                                                    |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------|
| Usage      | Positive or negative *charges* based on the quantity of a service or resource that was consumed over a given period of time including refunds. |
| Purchase   | Positive or negative *charges* for the acquisition of a service or resource bought upfront or on a recurring basis including refunds.          |
| Tax        | Positive or negative applicable taxes that are levied by the relevant authorities including refunds. Tax *charges* may vary depending on factors such as the location, jurisdiction, and local or federal regulations. |
| Credit     | Positive or negative *charges* granted by the service provider for various scenarios e.g., promotional credits or corrections to promotional credits.    |
| Adjustment | Positive or negative *charges* the service provider applies that do not fall into other category values.                                               |

## Column ID

ChargeCategory

## Display Name

Charge Category

## Description

Represents the highest-level classification of a [charge](#term) based on the nature of how it is billed.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | Not applicable                            |
| Column type                | Dimension                                 |
| Feature level              | Mandatory                                 |
| Allows nulls               | False                                     |
| Data type                  | String                                    |
| Value format               | Allowed values                            |

## Version Introduced

0.5
