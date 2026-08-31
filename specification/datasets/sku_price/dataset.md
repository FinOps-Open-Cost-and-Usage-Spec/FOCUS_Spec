# SKU Price

The SKU Price dataset is the primary dataset for standardizing [*price lists*](#glossary:price-list) offered by a [*service provider*](#glossary:service-provider). This dataset enables practitioners to perform precise [*SKU Price*](#glossary:sku-price) lookups, analyze commitment discounts, and understand the cost mechanics of payable and consumable prices.

The SKU Price dataset represents prices as of the date the dataset is captured. Providing a historical record of prior prices is the practitioner's responsibility rather than a guaranteed delivery; practitioners can reconstruct price history by retaining successive snapshots and comparing them using [SKU Price Effective Start](#datamodel.skuprice.skupriceeffectivestart) and [SKU Price Effective End](#datamodel.skuprice.skupriceeffectiveend). The dataset reflects the prices a *service provider* offers, independent of whether a price was used, and is not derived from Cost and Usage data.

The dataset describes the full price list a *service provider* offers, not only the SKUs that appear in Cost and Usage. To manage the size of a complete price list, a *service provider* may partition delivery, for example by region, service, or SKU category, and is encouraged to do so where publishing a complete list in a single delivery would otherwise be impractical.

The columns are presented in alphabetical order.

## Columns<!--SkipTOC-->

| Column                                                                              | Column Type | Feature Level                                                  | Allows Nulls | Data Type |
| ----------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------- | ------------ | --------- |
| [Charge Category](#datamodel.skuprice.chargecategory)                              | Dimension   | Mandatory   | False        | String    |
| [Contract ID](#datamodel.skuprice.contractid)                                        | Dimension   | Mandatory                                                      | True         | String    |
| [Contracted Unit Price](#datamodel.skuprice.contractedunitprice)                     | Metric      | Mandatory                                                      | False        | Decimal   |
| [List Unit Price](#datamodel.skuprice.listunitprice)                                 | Metric      | Mandatory                                                      | False        | Decimal   |
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

## Relationships<!--SkipTOC-->

The SKU Price dataset relates to the Cost and Usage dataset through the SKU Price ID, enabling the attribution of catalog unit prices to incurred usage. This is a one-to-many relationship: a single SKU Price ID corresponds to multiple SKU Price records, because a SKU's price varies by effective period, contract, and pricing currency. Resolving the price that applies to a Cost and Usage charge therefore requires more than the SKU Price ID alone. The charge must also be aligned to the SKU Price record whose effective period contains the charge period, whose Contract ID matches the agreement under which the charge was incurred (or is null for a public list price), and whose pricing currency matches the currency in which the charge is denominated. The resolved record carries both the List Unit Price and the Contracted Unit Price for that combination, so no further join is needed to compare the public unit price against the negotiated unit price. Contracted Unit Price resolves the same way in both datasets. Where no negotiation applies, a Cost and Usage charge reports a Contracted Unit Price equal to its List Unit Price, and the SKU Price record it resolves to, whose Contract ID is null, carries that same equality. Comparing a billed contracted unit price against its published catalog unit price therefore requires no allowance for a null on either side. The SKU Price dataset can also optionally join to the Contract Commitment dataset to relate a specific contracted price to an overarching negotiated agreement.

| Dataset A           | Dataset A Column  | Dataset B           | Dataset B Column       |
| ------------------- | ----------------- | ------------------- | ---------------------- |
| Cost and Usage      | SKU Price ID      | SKU Price           | SKU Price ID           |
| Contract Commitment | Contract ID       | SKU Price           | Contract ID            |

## Requirements<!--SkipTOC-->

SkuPrice MUST adhere to the following requirements:

* SkuPrice column presence MUST adhere to the following requirements:
  * SkuPrice MUST include [ChargeCategory](#datamodel.skuprice.chargecategory).
  * SkuPrice MUST include [ContractId](#datamodel.skuprice.contractid).
  * SkuPrice MUST include [ContractedUnitPrice](#datamodel.skuprice.contractedunitprice).
  * SkuPrice MUST include [ListUnitPrice](#datamodel.skuprice.listunitprice).
  * SkuPrice MUST include [PricingCurrency](#datamodel.skuprice.pricingcurrency).
  * SkuPrice MUST include [PricingCurrencyCategory](#datamodel.skuprice.pricingcurrencycategory).
  * SkuPrice MUST include [PricingRegionId](#datamodel.skuprice.pricingregionid) when the *operating model* [includes regions](#conditions.includesregions).
  * SkuPrice MUST include [PricingServiceName](#datamodel.skuprice.pricingservicename).
  * SkuPrice MUST include [PricingUnit](#datamodel.skuprice.pricingunit).
  * SkuPrice MUST include [PurchaseDurationType](#datamodel.skuprice.purchasedurationtype) when the *operating model* [includes purchases](#conditions.includespurchases).
  * SkuPrice MUST include [PurchasePaymentModel](#datamodel.skuprice.purchasepaymentmodel) when the *operating model* includes purchases.
  * SkuPrice MUST include [QuantityTierMaximum](#datamodel.skuprice.quantitytiermaximum) when the *operating model* [includes quantity tier pricing](#conditions.includesquantitytierpricing).
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
  * SkuPrice SHOULD include [*custom columns*](#glossary:custom-column) needed to identify specific price list routing logic when [*FOCUS columns*](#glossary:FOCUS-column) are not sufficient.
* SkuPrice MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.
* SkuPrice MUST conform to [DatasetConfiguration](#attributes.datasetconfiguration) requirements.
* SkuPrice MUST contain at least one record for every [SkuPriceId](#datamodel.skuprice.skupriceid) referenced in the [CostAndUsage](#datamodel.costandusage) dataset.
* SkuPrice MUST NOT contain more than one record for a given ServiceProviderName, SkuPriceId, ContractId, SkuPriceEffectiveStart, and PricingCurrency, with two null values in the same column considered equal.
* SkuPrice validity periods, defined by SkuPriceEffectiveStart and SkuPriceEffectiveEnd, MUST NOT overlap for a given ServiceProviderName, SkuPriceId, ContractId, and PricingCurrency, with two null values in the same column considered equal.
* SkuPrice *FOCUS columns* MUST conform to [FocusColumnHandling](#attributes.focuscolumnhandling) requirements.
* SkuPrice *FOCUS columns* MUST conform to [NullHandling](#attributes.nullhandling) requirements.
* SkuPrice *custom columns* MUST conform to [CustomColumnHandling](#attributes.customcolumnhandling) requirements.

## Dataset ID<!--SkipTOC-->

SkuPrice

## Display Name<!--SkipTOC-->

SKU Price

## Description<!--SkipTOC-->

Describes *price lists* for *resources* or *services* offered by a *service provider*.

## Version Introduced<!--SkipTOC-->

1.5
