# SKU Price

The SKU Price dataset is the primary dataset for standardizing [*service provider*](#glossary:service-provider) catalog rates, multipliers, and negotiated prices. This dataset enables practitioners to perform precise rate lookups, analyze commitment discounts, and understand the cost mechanics of payable vs consumable prices.

The SKU Price dataset represents prices as of the date the dataset is captured. Providing a historical record of prior prices is the practitioner's responsibility rather than a guaranteed delivery; practitioners can reconstruct price history by retaining successive snapshots and comparing them using [SKU Price Effective Start](#datasets.skuprice.skupriceeffectivestart) and [SKU Price Effective End](#datasets.skuprice.skupriceeffectiveend). The dataset reflects the prices a *service provider* offers, independent of whether a price was used, and is not derived from Cost and Usage data.

The dataset describes the full price list a *service provider* offers, not only the SKUs that appear in Cost and Usage. To manage the size of a complete price list, a *service provider* may partition delivery, for example by region, service, or SKU category, and is encouraged to do so where publishing a complete list in a single delivery would otherwise be impractical.

The columns are presented in alphabetical order.

## Columns<!--SkipTOC-->

| Column                                                                              | Column Type | Feature Level                                                  | Allows Nulls | Data Type |
| ----------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------- | ------------ | --------- |
| [Charge Category](#datasets.skuprice.chargecategory)                              | Dimension   | Mandatory   | False        | String    |
| [Contract ID](#datasets.skuprice.contractid)                                        | Dimension   | [Conditional](#conditions.includescontractcommitments)         | True         | String    |
| [Pricing Currency](#datasets.skuprice.pricingcurrency)                              | Dimension   | Mandatory                                                      | False        | String    |
| [Pricing Currency Category](#datasets.skuprice.pricingcurrencycategory)                            | Dimension   | Mandatory                                                      | False        | String    |
| [Pricing Region ID](#datasets.skuprice.pricingregionid)                             | Dimension   | [Conditional](#conditions.includesregions)                     | True        | String    |
| [Pricing Service Name](#datasets.skuprice.pricingservicename)                       | Dimension   | Mandatory                                                      | False        | String    |
| [Pricing Unit](#datasets.skuprice.pricingunit)                                      | Dimension   | Mandatory                                                      | False        | String    |
| [Purchase Duration Type](#datasets.skuprice.purchasedurationtype)                   | Dimension   | [Conditional](#conditions.includespurchases)                   | True         | String    |
| [Purchase Payment Model](#datasets.skuprice.purchasepaymentmodel)                   | Dimension   | [Conditional](#conditions.includespurchases)                   | True         | String    |
| [Service Provider Name](#datasets.skuprice.serviceprovidername)                     | Dimension   | Mandatory                                                      | False        | String    |
| [SKU ID](#datasets.skuprice.skuid)                                                  | Dimension   | Mandatory                                                      | False        | String    |
| [SKU Price Created](#datasets.skuprice.skupricecreated)                             | Dimension   | Mandatory                                                      | False        | Date/Time |
| [SKU Price Description](#datasets.skuprice.skupricedescription)                     | Dimension   | Mandatory                                                      | False        | String    |
| [SKU Price Effective End](#datasets.skuprice.skupriceeffectiveend)                  | Dimension   | Mandatory                                                      | True         | Date/Time |
| [SKU Price Effective Start](#datasets.skuprice.skupriceeffectivestart)              | Dimension   | Mandatory                                                      | True         | Date/Time |
| [SKU Price Eligibility](#datasets.skuprice.skupriceeligibility)                     | Dimension   | Mandatory                                                      | False        | JSON      |
| [SKU Price ID](#datasets.skuprice.skupriceid)                                       | Dimension   | Mandatory                                                      | False        | String    |
| [SKU Price Last Updated](#datasets.skuprice.skupricelastupdated)                    | Dimension   | Mandatory                                                      | False        | Date/Time |
| [SKU Price Lifecycle Status](#datasets.skuprice.skupricelifecyclestatus)            | Dimension   | Mandatory                                                      | False        | String    |
| [Unit Price](#datasets.skuprice.unitprice)                                          | Metric      | Mandatory                                                      | False        | Decimal   |
| [Unit Price Category](#datasets.skuprice.unitpricecategory)                         | Dimension   | Mandatory                                                      | False        | String    |
| [Volume Tier Maximum](#datasets.skuprice.volumetiermaximum)                         | Metric      | [Conditional](#conditions.includesvolumetierpricing)           | True         | Decimal   |
| [Volume Tier Minimum](#datasets.skuprice.volumetierminimum)                         | Metric      | [Conditional](#conditions.includesvolumetierpricing)           | False        | Decimal   |
| [Volume Tier Name](#datasets.skuprice.volumetiername)                               | Dimension   | [Conditional](#conditions.includesvolumetierpricing)           | True         | String    |

## Relationships<!--SkipTOC-->

The SKU Price dataset relates to the Cost and Usage dataset through the SKU Price ID, enabling the attribution of catalog rates to incurred usage. This is a one-to-many relationship: a single SKU Price ID corresponds to multiple SKU Price records, because a SKU's price varies by effective period, contract, volume tier, pricing currency, and unit price category. Resolving the price that applies to a Cost and Usage charge therefore requires more than the SKU Price ID alone. The charge must also be aligned to the SKU Price record whose effective period contains the charge period, whose Contract ID matches the agreement under which the charge was incurred (or is null for a public list price), whose volume tier contains the charged quantity, whose pricing currency matches the currency in which the charge is denominated, and whose unit price category matches the price type applied to the charge. The SKU Price dataset can also optionally join to the Contract Commitment dataset to relate a specific contracted price to an overarching negotiated agreement.

| Dataset A           | Dataset A Column  | Dataset B           | Dataset B Column       |
| ------------------- | ----------------- | ------------------- | ---------------------- |
| Cost and Usage      | SKU Price ID      | SKU Price           | SKU Price ID           |
| Contract Commitment | Contract ID       | SKU Price           | Contract ID            |

## Requirements<!--SkipTOC-->

SkuPrice MUST adhere to the following requirements:

* SkuPrice column presence MUST adhere to the following requirements:
  * SkuPrice MUST include [ChargeCategory](#datasets.skuprice.chargecategory).
  * SkuPrice MUST include [ContractId](#datasets.skuprice.contractid) when the *operating model* [includes contract commitments](#conditions.includescontractcommitments).
  * SkuPrice MUST include [PricingCurrency](#datasets.skuprice.pricingcurrency).
  * SkuPrice MUST include [PricingCurrencyCategory](#datasets.skuprice.pricingcurrencycategory).
  * SkuPrice MUST include [PricingRegionId](#datasets.skuprice.pricingregionid) when the *operating model* [includes regions](#conditions.includesregions).
  * SkuPrice MUST include [PricingServiceName](#datasets.skuprice.pricingservicename).
  * SkuPrice MUST include [PricingUnit](#datasets.skuprice.pricingunit).
  * SkuPrice MUST include [PurchaseDurationType](#datasets.skuprice.purchasedurationtype) when the *operating model* [includes purchases](#conditions.includespurchases).
  * SkuPrice MUST include [PurchasePaymentModel](#datasets.skuprice.purchasepaymentmodel) when the *operating model* [includes purchases](#conditions.includespurchases).
  * SkuPrice MUST include [ServiceProviderName](#datasets.skuprice.serviceprovidername).
  * SkuPrice MUST include [SkuId](#datasets.skuprice.skuid).
  * SkuPrice MUST include [SkuPriceCreated](#datasets.skuprice.skupricecreated).
  * SkuPrice MUST include [SkuPriceDescription](#datasets.skuprice.skupricedescription).
  * SkuPrice MUST include [SkuPriceEffectiveEnd](#datasets.skuprice.skupriceeffectiveend).
  * SkuPrice MUST include [SkuPriceEffectiveStart](#datasets.skuprice.skupriceeffectivestart).
  * SkuPrice MUST include [SkuPriceEligibility](#datasets.skuprice.skupriceeligibility).
  * SkuPrice MUST include [SkuPriceId](#datasets.skuprice.skupriceid).
  * SkuPrice MUST include [SkuPriceLastUpdated](#datasets.skuprice.skupricelastupdated).
  * SkuPrice MUST include [SkuPriceLifecycleStatus](#datasets.skuprice.skupricelifecyclestatus).
  * SkuPrice MUST include [UnitPrice](#datasets.skuprice.unitprice).
  * SkuPrice MUST include [UnitPriceCategory](#datasets.skuprice.unitpricecategory).
  * SkuPrice MUST include [VolumeTierMaximum](#datasets.skuprice.volumetiermaximum) when the *operating model* [includes volume tier pricing](#conditions.includesvolumetierpricing).
  * SkuPrice MUST include [VolumeTierMinimum](#datasets.skuprice.volumetierminimum) when the *operating model* [includes volume tier pricing](#conditions.includesvolumetierpricing).
  * SkuPrice MUST include [VolumeTierName](#datasets.skuprice.volumetiername) when the *operating model* [includes volume tier pricing](#conditions.includesvolumetierpricing).
  * SkuPrice SHOULD include [*custom columns*](#glossary:custom-column) needed to identify specific rate card routing logic when [*FOCUS columns*](#glossary:FOCUS-column) are not sufficient.
* SkuPrice MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.
* SkuPrice MUST conform to [DatasetConfiguration](#attributes.datasetconfiguration) requirements.
* SkuPrice MUST maintain row uniqueness across the composite key of ServiceProviderName, SkuPriceId, ContractId, VolumeTierMinimum, SkuPriceEffectiveStart, PricingCurrency, and UnitPriceCategory.
* SkuPrice MUST treat two records with a null value in the same composite-key member as equal in that member when evaluating row uniqueness.
* SkuPrice MUST NOT contain records whose validity periods, defined by SkuPriceEffectiveStart and SkuPriceEffectiveEnd, overlap for the same combination of ServiceProviderName, SkuPriceId, ContractId, VolumeTierMinimum, PricingCurrency, and UnitPriceCategory.
* SkuPrice MUST contain at least one record for every [SkuPriceId](#datasets.skuprice.skupriceid) referenced in the [CostAndUsage](#datasets.costandusage) dataset.
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
