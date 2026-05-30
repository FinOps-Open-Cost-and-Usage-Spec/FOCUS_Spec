# SKU Price

The SKU Price dataset is the primary dataset for standardizing [*service provider*](#glossary:service-provider) catalog rates, multipliers, and negotiated prices. This dataset enables practitioners to perform precise rate lookups, analyze commitment discounts, and understand the cost mechanics of payable vs consumable prices.

The columns are presented in alphabetical order.

## Columns

| Column                                                                              | Column Type | Feature Level                                                  | Allows Nulls | Data Type |
| ----------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------- | ------------ | --------- |
| [Charge Frequency](#datasets.skuprice.chargefrequency)                              | Dimension   | [Conditional](#conditions.includesmultiplechargefrequencies)   | False        | String    |
| [Contract Commitment Duration Type](#datasets.skuprice.contractcommitmentdurationtype) | Dimension   | [Conditional](#conditions.includescontractcommitments)         | True         | String    |
| [Contract Commitment Payment Model](#datasets.skuprice.contractcommitmentpaymentmodel) | Dimension   | [Conditional](#conditions.includescontractcommitments)         | True         | String    |
| [Contract ID](#datasets.skuprice.contractid)                                        | Dimension   | [Conditional](#conditions.includescontractcommitments)         | True         | String    |
| [Pricing Category](#datasets.skuprice.pricingcategory)                              | Dimension   | Mandatory                                                      | False        | String    |
| [Pricing Currency](#datasets.skuprice.pricingcurrency)                              | Dimension   | Mandatory                                                      | False        | String    |
| [Pricing Currency Category](#datasets.skuprice.pricingcurrencycategory)                            | Dimension   | Mandatory                                                      | False        | String    |
| [Pricing Region ID](#datasets.skuprice.pricingregionid)                             | Dimension   | [Conditional](#conditions.includesregions)                     | True        | String    |
| [Pricing Service Name](#datasets.skuprice.pricingservicename)                       | Dimension   | Mandatory                                                      | False        | String    |
| [Pricing Unit](#datasets.skuprice.pricingunit)                                      | Dimension   | Mandatory                                                      | False        | String    |
| [Service Provider Name](#datasets.skuprice.serviceprovidername)                     | Dimension   | Mandatory                                                      | False        | String    |
| [SKU ID](#datasets.skuprice.skuid)                                                  | Dimension   | Mandatory                                                      | False        | String    |
| [SKU Price Created](#datasets.skuprice.skupricecreated)                             | Dimension   | Mandatory                                                      | False        | Date/Time |
| [SKU Price Description](#datasets.skuprice.skupricedescription)                     | Dimension   | Mandatory                                                      | False        | String    |
| [SKU Price Details](#datasets.skuprice.skupricedetails)                             | Dimension   | Mandatory                                                      | True         | JSON      |
| [SKU Price Effective End](#datasets.skuprice.skupriceeffectiveend)                  | Dimension   | Mandatory                                                      | True         | Date/Time |
| [SKU Price Effective Start](#datasets.skuprice.skupriceeffectivestart)              | Dimension   | Mandatory                                                      | False        | Date/Time |
| [SKU Price Eligibility](#datasets.skuprice.skupriceeligibility)                     | Dimension   | Mandatory                                                      | True         | JSON      |
| [SKU Price ID](#datasets.skuprice.skupriceid)                                       | Dimension   | Mandatory                                                      | False        | String    |
| [SKU Price Last Updated](#datasets.skuprice.skupricelastupdated)                    | Dimension   | Mandatory                                                      | False        | Date/Time |
| [SKU Price Lifecycle Status](#datasets.skuprice.skupricelifecyclestatus)            | Dimension   | Mandatory                                                      | False        | String    |
| [Unit Price](#datasets.skuprice.unitprice)                                          | Metric      | Mandatory                                                      | False        | Decimal   |
| [Unit Price Category](#datasets.skuprice.unitpricecategory)                         | Dimension   | Mandatory                                                      | False        | String    |
| [Volume Tier Maximum](#datasets.skuprice.volumetiermaximum)                         | Metric      | [Conditional](#conditions.includesvolumetierpricing)           | True         | Decimal   |
| [Volume Tier Minimum](#datasets.skuprice.volumetierminimum)                         | Metric      | [Conditional](#conditions.includesvolumetierpricing)           | False        | Decimal   |
| [Volume Tier Name](#datasets.skuprice.volumetiername)                               | Dimension   | [Conditional](#conditions.includesvolumetierpricing)           | True         | String    |

## Relationships

The SKU Price dataset can be joined to the Cost and Usage dataset through the use of the SKU Price ID, enabling the attribution of catalog rates directly to incurred usage. It can also optionally join to the Contract Commitment dataset to relate a specific contracted price to an overarching negotiated agreement.

| Dataset A           | Dataset A Column  | Dataset B           | Dataset B Column       |
| ------------------- | ----------------- | ------------------- | ---------------------- |
| Cost and Usage      | SKU Price ID      | SKU Price           | SKU Price ID           |
| Contract Commitment | Contract ID       | SKU Price           | Contract ID            |

## Requirements

SkuPrice MUST adhere to the following requirements:

* SkuPrice column presence MUST adhere to the following requirements:
  * SkuPrice MUST include [ChargeFrequency](#datasets.skuprice.chargefrequency) when the *operating model* [includes multiple charge frequencies](#conditions.includesmultiplechargefrequencies).
  * SkuPrice MUST include [ContractCommitmentDurationType](#datasets.skuprice.contractcommitmentdurationtype) when the *operating model* [includes contract commitments](#conditions.includescontractcommitments).
  * SkuPrice MUST include [ContractCommitmentPaymentModel](#datasets.skuprice.contractcommitmentpaymentmodel) when the *operating model* [includes contract commitments](#conditions.includescontractcommitments).
  * SkuPrice MUST include [ContractId](#datasets.skuprice.contractid) when the *operating model* [includes contract commitments](#conditions.includescontractcommitments).
  * SkuPrice MUST include [PricingCategory](#datasets.skuprice.pricingcategory).
  * SkuPrice MUST include [PricingCurrency](#datasets.skuprice.pricingcurrency).
  * SkuPrice MUST include [PricingCurrencyCategory](#datasets.skuprice.pricingcurrencycategory).
  * SkuPrice MUST include [PricingRegionId](#datasets.skuprice.pricingregionid) when the *operating model* [includes regions](#conditions.includesregions).
  * SkuPrice MUST include [PricingServiceName](#datasets.skuprice.pricingservicename).
  * SkuPrice MUST include [PricingUnit](#datasets.skuprice.pricingunit).
  * SkuPrice MUST include [ServiceProviderName](#datasets.skuprice.serviceprovidername).
  * SkuPrice MUST include [SkuId](#datasets.skuprice.skuid).
  * SkuPrice MUST include [SkuPriceCreated](#datasets.skuprice.skupricecreated).
  * SkuPrice MUST include [SkuPriceDescription](#datasets.skuprice.skupricedescription).
  * SkuPrice MUST include [SkuPriceDetails](#datasets.skuprice.skupricedetails).
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
* SkuPrice MUST maintain row uniqueness across the composite key of SkuPriceId, ContractId, VolumeTierMinimum, SkuPriceEffectiveStart, PricingCurrency, and UnitPriceCategory.
* SkuPrice *FOCUS columns* MUST conform to [FocusColumnHandling](#attributes.focuscolumnhandling) requirements.
* SkuPrice *FOCUS columns* MUST conform to [NullHandling](#attributes.nullhandling) requirements.
* SkuPrice *custom columns* MUST conform to [CustomColumnHandling](#attributes.customcolumnhandling) requirements.

## Dataset ID

SkuPrice

## Display Name

SKU Price

## Description

Describes the catalog rates, internal multipliers, and negotiated unit prices for resources or services offered by a service provider.

## Version Introduced

1.5
