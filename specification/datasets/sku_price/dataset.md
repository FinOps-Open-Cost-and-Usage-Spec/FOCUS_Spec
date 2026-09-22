# SKU Price

The SKU Price dataset is the primary dataset for standardizing [*service provider*](#glossary:service-provider) catalog rates, multipliers, and negotiated prices. This dataset enables practitioners to perform precise rate lookups, analyze commitment discounts, and understand the cost mechanics of payable and consumable prices.

The SKU Price dataset represents prices as of the date the dataset is captured. A *service provider* might not include historical prices in their delivery; if so, practitioners can reconstruct price history by combining successive snapshots and comparing them using [SKU Price Effective Start](#datamodel.skuprice.skupriceeffectivestart) and [SKU Price Effective End](#datamodel.skuprice.skupriceeffectiveend). The dataset reflects the prices a *service provider* offers, independent of whether a price was used, and is not derived from [Cost and Usage](#datamodel.costandusage) data.

The dataset describes the full price list a *service provider* offers, not only the SKUs that appear in Cost and Usage. To manage the size of a complete price list, a *service provider* may partition delivery, for example by region, service, or SKU category, and is encouraged to do so where publishing a complete list in a single delivery would otherwise be impractical.

The columns are presented in alphabetical order.

## Columns<!--SkipTOC-->

| Column                                                                              | Column Type | Feature Level                                                  | Allows Nulls | Data Type |
| ----------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------- | ------------ | --------- |
| [Charge Category](#datamodel.skuprice.chargecategory)                              | Dimension   | Mandatory   | False        | String    |
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

## Relationships<!--SkipTOC-->

The [SKU Price](#datamodel.skuprice) dataset relates to the [Cost and Usage](#datamodel.costandusage) dataset through the SKU Price ID, enabling the attribution of catalog rates to incurred usage. This is a one-to-many relationship: a single SKU Price ID corresponds to multiple SKU Price records, because a SKU's price varies by effective period, contract, quantity tier, and pricing currency.

Resolving the price that applies to a Cost and Usage charge therefore requires more than the SKU Price ID alone. The charge must also be aligned to the SKU Price record using the following criteria:

* **Effective Period:** The SKU Price record's effective period (defined by [SKU Price Effective Start](#datamodel.skuprice.skupriceeffectivestart) and [SKU Price Effective End](#datamodel.skuprice.skupriceeffectiveend)) contains the Cost and Usage charge period (defined by [Charge Period Start](#datamodel.costandusage.chargeperiodstart) and [Charge Period End](#datamodel.costandusage.chargeperiodend)).
* **Contract:** The Contract ID matches the agreement under which the charge was incurred (or is null for a public list price).
* **Quantity Tier:** The quantity tier (defined by [Quantity Tier Minimum](#datamodel.skuprice.quantitytierminimum) and [Quantity Tier Maximum](#datamodel.skuprice.quantitytiermaximum)) contains the cumulative or evaluated quantity that determines the price for the charge.
* **Pricing Currency:** The SKU price's [Pricing Currency](#datamodel.skuprice.pricingcurrency) matches the charge's [PricingCurrency](#datamodel.costandusage.pricingcurrency).

The resolved record carries the unit price for that combination. If Contract ID is populated, the Unit Price represents the contractually agreed rate; if null, it represents the public list price. Comparing a billed contracted rate against its published catalog rate therefore requires looking up the corresponding SKU Price record where Contract ID is null.

> **Notes:**
>
> * Because the base unit prices in the Cost and Usage dataset (i.e., [List Unit Price](#datamodel.costandusage.listunitprice) and [Contracted Unit Price](#datamodel.costandusage.contractedunitprice)) are denominated in the Billing Currency, comparing a Cost and Usage rate against a resolved SKU Price record requires currency conversion whenever the charge's Billing Currency differs from its Pricing Currency. However, the Pricing Currency unit prices (i.e., [Pricing Currency List Unit Price](#datamodel.costandusage.pricingcurrencylistunitprice) and [Pricing Currency Contracted Unit Price](#datamodel.costandusage.pricingcurrencycontractedunitprice)) are denominated in the Pricing Currency and compare directly against Unit Price without conversion.
> * Because the SKU Price dataset is delivered as a point-in-time snapshot, historical charges in the Cost and Usage dataset may reference a superseded price record that is no longer included in the current catalog. Practitioners must retain historical SKU Price snapshots to reliably resolve older charges.

Additionally, the SKU Price dataset can optionally join to the [Contract Commitment](#datamodel.contractcommitment) dataset to relate a specific contracted price to an overarching contractual agreement.

| Dataset A           | Dataset A Column  | Dataset B           | Dataset B Column       |
| ------------------- | ----------------- | ------------------- | ---------------------- |
| Cost and Usage      | SKU Price ID, Contract ID, Pricing Currency, plus time and tier (see above) | SKU Price | SKU Price ID, Contract ID, Pricing Currency, plus time and tier (see above) |
| Contract Commitment | Contract ID       | SKU Price           | Contract ID            |

## Requirements<!--SkipTOC-->

SkuPrice MUST adhere to the following requirements:

* SkuPrice column presence MUST adhere to the following requirements:
  * SkuPrice MUST include [ChargeCategory](#datamodel.skuprice.chargecategory).
  * SkuPrice MUST include [ContractId](#datamodel.skuprice.contractid).
  * SkuPrice MUST include [PricingCurrency](#datamodel.skuprice.pricingcurrency).
  * SkuPrice MUST include [PricingCurrencyCategory](#datamodel.skuprice.pricingcurrencycategory).
  * SkuPrice MUST include [PricingRegionId](#datamodel.skuprice.pricingregionid) when the *operating model* [includes regions](#operatingmodelconditions.includesregions).
  * SkuPrice MUST include [PricingServiceName](#datamodel.skuprice.pricingservicename).
  * SkuPrice MUST include [PricingUnit](#datamodel.skuprice.pricingunit).
  * SkuPrice MUST include [PurchaseDurationType](#datamodel.skuprice.purchasedurationtype) when the *operating model* [includes purchases](#operatingmodelconditions.includespurchases).
  * SkuPrice MUST include [PurchasePaymentModel](#datamodel.skuprice.purchasepaymentmodel) when the *operating model* includes purchases.
  * SkuPrice MUST include [QuantityTierMaximum](#datamodel.skuprice.quantitytiermaximum) when the *operating model* [includes quantity tier pricing](#operatingmodelconditions.includesquantitytierpricing).
  * SkuPrice MUST include [QuantityTierMinimum](#datamodel.skuprice.quantitytierminimum) when the *operating model* includes quantity tier pricing.
  * SkuPrice MUST include [ServiceProviderName](#datamodel.skuprice.serviceprovidername).
  * SkuPrice MUST include [SkuId](#datamodel.skuprice.skuid).
  * SkuPrice MUST include [SkuPriceCreated](#datamodel.skuprice.skupricecreated).
  * SkuPrice MUST include [SkuPriceDescription](#datamodel.skuprice.skupricedescription).
  * SkuPrice MUST include [SkuPriceEffectiveEnd](#datamodel.skuprice.skupriceeffectiveend).
  * SkuPrice MUST include [SkuPriceEffectiveStart](#datamodel.skuprice.skupriceeffectivestart).
  * SkuPrice MUST include [SkuPriceEligibility](#datamodel.skuprice.skupriceeligibility).
  * SkuPrice MUST include [SkuPriceId](#datamodel.skuprice.skupriceid).
  * SkuPrice MUST include [SkuPriceLastUpdated](#datamodel.skuprice.skupricelastupdated).
  * SkuPrice MUST include [UnitPrice](#datamodel.skuprice.unitprice).
  * SkuPrice SHOULD include [*custom columns*](#glossary:custom-column) needed to identify specific rate card routing logic when [*FOCUS columns*](#glossary:FOCUS-column) are not sufficient.
* SkuPrice MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.
* SkuPrice MUST conform to [DatasetConfiguration](#attributes.datasetconfiguration) requirements.
* SkuPrice MUST conform to [DeliveryHandling](#attributes.deliveryhandling) requirements.
* SkuPrice MUST leverage the Overwrite *DeliveryHandling* mechanism (i.e., data cannot be delivered as append-only).
* SkuPrice MUST contain at least one record for every [SkuPriceId](#datamodel.skuprice.skupriceid) referenced in the [CostAndUsage](#datamodel.costandusage) dataset.
* SkuPrice MUST NOT contain multiple records that share identical values (including nulls) across ServiceProviderName, SkuPriceId, ContractId, SkuPriceEffectiveStart, and PricingCurrency.
* SkuPrice MUST NOT contain records with overlapping effective periods (defined by SkuPriceEffectiveStart and SkuPriceEffectiveEnd) when those records share identical values (including nulls) across ServiceProviderName, SkuPriceId, ContractId, and PricingCurrency; for this constraint, a null SkuPriceEffectiveStart represents the earliest available time, and a null SkuPriceEffectiveEnd represents the latest available time.
* SkuPrice *FOCUS columns* MUST conform to [FocusColumnHandling](#attributes.focuscolumnhandling) requirements.
* SkuPrice *FOCUS columns* MUST conform to [NullHandling](#attributes.nullhandling) requirements.
* SkuPrice *custom columns* MUST conform to [CustomColumnHandling](#attributes.customcolumnhandling) requirements.

## Dataset ID<!--SkipTOC-->

SkuPrice

## Display Name<!--SkipTOC-->

SKU Price

## Description<!--SkipTOC-->

Describes the catalog rates, internal multipliers, and negotiated unit prices for resources or services offered by a service provider.

## Version Introduced<!--SkipTOC-->

1.5
