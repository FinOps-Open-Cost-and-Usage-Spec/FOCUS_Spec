# SKU Price

> **Preview:** The [SKU Price](#ds) dataset is a preview in this version of FOCUS. Its columns, requirements, and relationships may change in the next version based on implementation feedback. Its requirements are not evaluated for conformance, whether or not the dataset is provided. Two requirements outside the dataset are also excluded from conformance while it is a preview: the [Data Model](#datamodel) requirement to include [SKU Price](#ds), and the requirement that [Cost and Usage Charge Category](#col:CostAndUsage.ChargeCategory) match [SKU Price](#ds) [Charge Category](#col). The [Includes Purchases](#omc) and [Includes Quantity Tier Pricing](#omc) operating model conditions and the [SKU Price Eligibility Object Schema](#schema) are part of the preview and may change in the next version without a deprecation notice. [Issue #2768](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2768) tracks the preview.

The [SKU Price](#ds) dataset is the primary dataset for standardizing [service provider](#term) catalog rates, multipliers, and negotiated prices. This dataset enables practitioners to perform precise rate lookups, analyze commitment discounts, and understand the cost mechanics of payable and consumable prices.

The [SKU Price](#ds) dataset represents prices as of the date the dataset is captured. A [service provider](#term) might not include historical prices in their delivery; if so, practitioners can reconstruct price history by combining successive snapshots and comparing them using [SKU Price Effective Start](#col) and [SKU Price Effective End](#col). The dataset reflects the prices a [service provider](#term) offers, independent of whether a price was used, and is not derived from [Cost and Usage](#ds) data.

The dataset describes the full price list a [service provider](#term) offers, not only the SKUs that appear in [Cost and Usage](#ds). To manage the size of a complete price list, a [service provider](#term) may partition delivery, for example by region, service, or SKU category, and is encouraged to do so where publishing a complete list in a single delivery would otherwise be impractical.

The columns are presented in alphabetical order.

## Columns<!--SkipTOC-->

| Column                                                                              | Column Type | Feature Level                                                  | Allows Nulls | Data Type |
| ----------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------- | ------------ | --------- |
| [Charge Category](#datamodel.skuprice.chargecategory)                              | Dimension   | Mandatory   | False        | String    |
| [Commitment Discount Category](#datamodel.skuprice.commitmentdiscountcategory)     | Dimension   | Conditional | True         | String    |
| [Contract ID](#datamodel.skuprice.contractid)                                        | Dimension   | Mandatory                                                      | True         | String    |
| [Pricing Currency](#datamodel.skuprice.pricingcurrency)                              | Dimension   | Mandatory                                                      | False        | String    |
| [Pricing Currency Category](#datamodel.skuprice.pricingcurrencycategory)                            | Dimension   | Mandatory                                                      | False        | String    |
| [Pricing Region ID](#datamodel.skuprice.pricingregionid)                             | Dimension   | Conditional                     | True        | String    |
| [Pricing Service Name](#datamodel.skuprice.pricingservicename)                       | Dimension   | Mandatory                                                      | False        | String    |
| [Pricing Unit](#datamodel.skuprice.pricingunit)                                      | Dimension   | Mandatory                                                      | False        | String    |
| [Purchase Duration Type](#datamodel.skuprice.purchasedurationtype)                   | Dimension   | Conditional                   | True         | String    |
| [Purchase Payment Model](#datamodel.skuprice.purchasepaymentmodel)                   | Dimension   | Conditional                   | True         | String    |
| [Quantity Tier Maximum](#datamodel.skuprice.quantitytiermaximum)                     | Metric      | Conditional         | True         | Decimal   |
| [Quantity Tier Minimum](#datamodel.skuprice.quantitytierminimum)                     | Metric      | Conditional         | False        | Decimal   |
| [Service Provider Name](#datamodel.skuprice.serviceprovidername)                     | Dimension   | Mandatory                                                      | False        | String    |
| [SKU ID](#datamodel.skuprice.skuid)                                                  | Dimension   | Mandatory                                                      | False        | String    |
| [SKU Price Created](#datamodel.skuprice.skupricecreated)                             | Dimension   | Mandatory                                                      | False        | Date/Time |
| [SKU Price Description](#datamodel.skuprice.skupricedescription)                     | Dimension   | Mandatory                                                      | False        | String    |
| [SKU Price Effective End](#datamodel.skuprice.skupriceeffectiveend)                  | Dimension   | Mandatory                                                      | True         | Date/Time |
| [SKU Price Effective Start](#datamodel.skuprice.skupriceeffectivestart)              | Dimension   | Mandatory                                                      | True         | Date/Time |
| [SKU Price Eligibility](#datamodel.skuprice.skupriceeligibility)                     | Dimension   | Mandatory                                                      | False        | JSON      |
| [SKU Price ID](#datamodel.skuprice.skupriceid)                                       | Dimension   | Mandatory                                                      | False        | String    |
| [SKU Price Last Updated](#datamodel.skuprice.skupricelastupdated)                    | Dimension   | Mandatory                                                      | False        | Date/Time |
| [Unit Price](#datamodel.skuprice.unitprice)                                 | Metric      | Mandatory                                                      | False        | Decimal   |
| [Unit Price Type](#datamodel.skuprice.unitpricetype)                                 | Dimension   | Mandatory                                                      | False        | String    |

## Relationships<!--SkipTOC-->

The [SKU Price](#ds) dataset relates to the [Cost and Usage](#ds) dataset through the [SKU Price ID](#col), enabling the attribution of catalog rates to incurred usage. This is a one-to-many relationship: a single [SKU Price ID](#col) corresponds to multiple [SKU Price](#ds) records, because a SKU's price varies by effective period, contract, pricing currency, and unit price type.

Resolving the price that applies to a [Cost and Usage](#ds) charge therefore requires more than the [SKU Price ID](#col) alone. The charge must also be aligned to the [SKU Price](#ds) record using the following criteria:

* **Service Provider:** The [Cost and Usage](#ds) [Service Provider Name](#col:CostAndUsage.ServiceProviderName) matches the [SKU Price](#ds) record's [Service Provider Name](#col).
* **Effective Period:** The [Cost and Usage](#ds) [Charge Period Start](#col:CostAndUsage.ChargePeriodStart) is on or after the [SKU Price](#ds) record's [SKU Price Effective Start](#col) and before its [SKU Price Effective End](#col); for this criterion, a null [SKU Price Effective Start](#col) represents the earliest available time, and a null [SKU Price Effective End](#col) represents the latest available time.
* **Contract:** The [Contract ID](#col) matches a `ContractId` property extracted from the charge's [Contract Applied](#col:CostAndUsage.ContractApplied) array (`ContractApplied.Elements[*].ContractId`), or is null for a public list price. Note that `ContractApplied` only resolves prices associated with contract commitments.
* **[Pricing Currency](#col):** The SKU price's [Pricing Currency](#col) matches the charge's [PricingCurrency](#col:CostAndUsage.PricingCurrency), or the charge's [BillingCurrency](#col:CostAndUsage.BillingCurrency) when the [operating model](#term) does not [include pricing and billing currency differences](#omc:IncludesPricingBillingCurrencyDifferences).
* **[Unit Price Type](#col):** The [SKU Price](#ds) record's [Unit Price Type](#col) is filtered to a single value (e.g., "List"). Because one contract can carry more than one price type for the same [SKU Price ID](#col) (e.g., a "Base" rate and a "Contracted" rate), the other criteria alone can match more than one record. Comparing a billed contracted rate against its published catalog rate, for example, requires looking up the corresponding [SKU Price](#ds) record where [Unit Price Type](#col) is "List".

The resolved record carries the unit price for that combination.

> **Notes:**
>
> * Because the unit prices in the [Cost and Usage](#ds) dataset (i.e., [List Unit Price](#col:CostAndUsage.ListUnitPrice) and [Contracted Unit Price](#col:CostAndUsage.ContractedUnitPrice)) are denominated in the [Billing Currency](#col:CostAndUsage.BillingCurrency), comparing a [Cost and Usage](#ds) rate against a resolved [SKU Price](#ds) record requires currency conversion whenever the charge's [Billing Currency](#col:CostAndUsage.BillingCurrency) differs from its [Pricing Currency](#col). However, the [Pricing Currency](#col) unit prices (i.e., [Pricing Currency List Unit Price](#col:CostAndUsage.PricingCurrencyListUnitPrice) and [Pricing Currency Contracted Unit Price](#col:CostAndUsage.PricingCurrencyContractedUnitPrice)) are denominated in the [Pricing Currency](#col) and compare directly against [Unit Price](#col) without conversion.
> * Because the [SKU Price](#ds) dataset is delivered as a point-in-time snapshot, historical charges in the [Cost and Usage](#ds) dataset may reference a superseded price record that is no longer included in the current catalog. Practitioners must retain historical [SKU Price](#ds) snapshots to reliably resolve older charges.

Additionally, the [SKU Price](#ds) dataset can optionally join to the [Contract Commitment](#ds) dataset to relate a specific contracted price to an overarching contractual agreement.

| Dataset A           | Dataset A Column  | Dataset B           | Dataset B Column       |
| ------------------- | ----------------- | ------------------- | ---------------------- |
| Cost and Usage      | Service Provider Name, SKU Price ID, ContractApplied.Elements[*].ContractId, Pricing Currency (or Billing Currency), plus time (see above) | SKU Price | Service Provider Name, SKU Price ID, Contract ID, Pricing Currency, Unit Price Type (one value, see above), plus time (see above) |
| Contract Commitment | Contract ID       | SKU Price           | Contract ID            |

## Implementation Guidance<!--SkipTOC-->

Because a [SKU Price ID](#col) represents a specific price point, it inherently defines the quantity tier for that price. Service providers that natively share a single underlying identifier across multiple quantity tiers will need to generate a distinct [SKU Price ID](#col) for each tier when exporting data to FOCUS. In such a case, this can be achieved by simply concatenating the price ID with the tier start and tier end.

This ensures that each tier maintains its own distinct identifier, allowing practitioners to join [Cost and Usage](#ds) data directly to the correct tier using [SKU Price ID](#col) without needing to manually evaluate the [Quantity Tier Minimum](#col) boundaries.

The same applies to commitment terms. Service providers that price one SKU at different rates under different commitment terms (e.g., one year and three years) will need a distinct [SKU Price ID](#col) for each term, because [Purchase Duration Type](#col) is null on "Usage" records and cannot separate them. A price that differs only by contract keeps its [SKU Price ID](#col) and is separated by [Contract ID](#col).

## Requirements<!--SkipTOC-->

[SkuPrice](#ds) MUST adhere to the following requirements:

* [SkuPrice](#ds) column presence MUST adhere to the following requirements:
  * [SkuPrice](#ds) MUST include [ChargeCategory](#col).
  * [SkuPrice](#ds) MUST include [CommitmentDiscountCategory](#col) when the [operating model](#term) [includes commitment discounts](#omc).  
  * [SkuPrice](#ds) MUST include [ContractId](#col).
  * [SkuPrice](#ds) MUST include [PricingCurrency](#col).
  * [SkuPrice](#ds) MUST include [PricingCurrencyCategory](#col).
  * [SkuPrice](#ds) MUST include [PricingRegionId](#col) when the [operating model](#term) [includes regions](#omc).
  * [SkuPrice](#ds) MUST include [PricingServiceName](#col).
  * [SkuPrice](#ds) MUST include [PricingUnit](#col).
  * [SkuPrice](#ds) MUST include [PurchaseDurationType](#col) when the [operating model](#term) [includes purchases](#omc).
  * [SkuPrice](#ds) MUST include [PurchasePaymentModel](#col) when the [operating model](#term) includes purchases.
  * [SkuPrice](#ds) MUST include [QuantityTierMaximum](#col) when the [operating model](#term) [includes quantity tier pricing](#omc).
  * [SkuPrice](#ds) MUST include [QuantityTierMinimum](#col) when the [operating model](#term) includes quantity tier pricing.
  * [SkuPrice](#ds) MUST include [ServiceProviderName](#col).
  * [SkuPrice](#ds) MUST include [SkuId](#col).
  * [SkuPrice](#ds) MUST include [SkuPriceCreated](#col).
  * [SkuPrice](#ds) MUST include [SkuPriceDescription](#col).
  * [SkuPrice](#ds) MUST include [SkuPriceEffectiveEnd](#col).
  * [SkuPrice](#ds) MUST include [SkuPriceEffectiveStart](#col).
  * [SkuPrice](#ds) MUST include [SkuPriceEligibility](#col).
  * [SkuPrice](#ds) MUST include [SkuPriceId](#col).
  * [SkuPrice](#ds) MUST include [SkuPriceLastUpdated](#col).
  * [SkuPrice](#ds) MUST include [UnitPrice](#col).
  * [SkuPrice](#ds) MUST include [UnitPriceType](#col).
  * [SkuPrice](#ds) SHOULD include [custom columns](#term) needed to identify specific rate card routing logic when [FOCUS columns](#term) are not sufficient.
* [SkuPrice](#ds) MUST conform to [DatasetCompleteness](#attr) requirements.
* [SkuPrice](#ds) MUST conform to [DatasetConfiguration](#attr) requirements.
* [SkuPrice](#ds) MUST conform to [DeliveryHandling](#attr) requirements.
* [SkuPrice](#ds) MUST use the Overwrite delivery mechanism.
* [SkuPrice](#ds) SHOULD contain at least one record for every [SkuPriceId](#col) referenced in the [CostAndUsage](#ds) dataset.
* [SkuPrice](#ds) MUST NOT contain multiple records that share identical values (including nulls) across [ServiceProviderName](#col), [SkuPriceId](#col), [ContractId](#col), [SkuPriceEffectiveStart](#col), [PricingCurrency](#col), and [UnitPriceType](#col).
* [SkuPrice](#ds) MUST NOT contain records with overlapping effective periods (defined by [SkuPriceEffectiveStart](#col) and [SkuPriceEffectiveEnd](#col)) when those records share identical values (including nulls) across [ServiceProviderName](#col), [SkuPriceId](#col), [ContractId](#col), [PricingCurrency](#col), and [UnitPriceType](#col); for this constraint, a null [SkuPriceEffectiveStart](#col) represents the earliest available time, and a null [SkuPriceEffectiveEnd](#col) represents the latest available time.
* [SkuPrice](#ds) [FOCUS columns](#term) MUST conform to [FocusColumnHandling](#attr) requirements.
* [SkuPrice](#ds) [FOCUS columns](#term) MUST conform to [NullHandling](#attr) requirements.
* [SkuPrice](#ds) [custom columns](#term) MUST conform to [CustomColumnHandling](#attr) requirements.

## Dataset ID<!--SkipTOC-->

SkuPrice

## Display Name<!--SkipTOC-->

SKU Price

## Description<!--SkipTOC-->

Describes the catalog rates, internal multipliers, and negotiated unit prices for resources or services offered by a service provider.

## Version Introduced<!--SkipTOC-->

Preview: 1.5
