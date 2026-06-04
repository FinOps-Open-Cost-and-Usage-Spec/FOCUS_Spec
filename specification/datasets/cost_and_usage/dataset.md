# Cost and Usage

The Cost and Usage dataset is the primary dataset for FOCUS cost and usage data.

The specification for the Cost and Usage dataset defines a group of columns that provide qualitative values (such as dates, resource, and service provider information) categorized as "dimensions" and quantitative values (numeric values) categorized as "metrics" that can be used for performing various [FinOps capabilities][FODOFC]. Metrics are commonly used for aggregations (sum, multiplication, averaging etc.) and statistical operations within the dataset. Dimensions are commonly used to categorize, filter, and reveal details in your data when combined with metrics. The columns are presented in alphabetical order.

## Columns<!--SkipTOC-->

| Column                                                                        | Column Type        | Feature Level | Allows Nulls | Data Type |
| ----------------------------------------------------------------------------- | ------------------ | ------------- | ------------ | --------- |
| [Allocated Method Details](#datasets.costandusage.allocatedmethoddetails)                           | Dimension / Metric | Recommended   | True         | JSON      |
| [Allocated Method ID](#datasets.costandusage.allocatedmethodid)                                     | Dimension          | [Conditional](#conditions.includessplitcostallocation) | True         | String    |
| [Allocated Resource ID](#datasets.costandusage.allocatedresourceid)                                 | Dimension          | [Conditional](#conditions.includessplitcostallocation) | True         | String    |
| [Allocated Resource Name](#datasets.costandusage.allocatedresourcename)                             | Dimension          | [Conditional](#conditions.includessplitcostallocation) | True         | String    |
| [Allocated Tags](#datasets.costandusage.allocatedtags)                                              | Dimension          | [Conditional](#conditions.includessplitcostallocation) | True         | JSON      |
| [Availability Zone](#datasets.costandusage.availabilityzone)                                        | Dimension          | Recommended   | True         | String    |
| [Billed Cost](#datasets.costandusage.billedcost)                                                    | Metric             | Mandatory     | False        | Decimal   |
| [Billing Account ID](#datasets.costandusage.billingaccountid)                                       | Dimension          | Mandatory     | False        | String    |
| [Billing Account Name](#datasets.costandusage.billingaccountname)                                   | Dimension          | Mandatory     | True         | String    |
| [Billing Account Type](#datasets.costandusage.billingaccounttype)                                   | Dimension          | [Conditional](#conditions.includesmultiplebillingaccounttypes) | False        | String    |
| [Billing Currency](#datasets.costandusage.billingcurrency)                                          | Dimension          | Mandatory     | False        | String    |
| [Billing Period End](#datasets.costandusage.billingperiodend)                                       | Dimension          | Mandatory     | False        | Date/Time |
| [Billing Period Start](#datasets.costandusage.billingperiodstart)                                   | Dimension          | Mandatory     | False        | Date/Time |
| [Capacity Reservation ID](#datasets.costandusage.capacityreservationid)                             | Dimension          | [Conditional](#conditions.includescapacityreservations) | True         | String    |
| [Capacity Reservation Status](#datasets.costandusage.capacityreservationstatus)                     | Dimension          | [Conditional](#conditions.includescapacityreservations) | True         | String    |
| [Charge Category](#datasets.costandusage.chargecategory)                                            | Dimension          | Mandatory     | False        | String    |
| [Charge Class](#datasets.costandusage.chargeclass)                                                  | Dimension          | Mandatory     | True         | String    |
| [Charge Description](#datasets.costandusage.chargedescription)                                      | Dimension          | Mandatory     | True         | String    |
| [Charge Frequency](#datasets.costandusage.chargefrequency)                                          | Dimension          | Recommended   | False        | String    |
| [Charge Period End](#datasets.costandusage.chargeperiodend)                                         | Dimension          | Mandatory     | False        | Date/Time |
| [Charge Period Start](#datasets.costandusage.chargeperiodstart)                                     | Dimension          | Mandatory     | False        | Date/Time |
| [Commitment Discount Category](#datasets.costandusage.commitmentdiscountcategory)                   | Dimension          | [Conditional](#conditions.includescommitmentdiscounts) | True         | String    |
| [Commitment Discount ID](#datasets.costandusage.commitmentdiscountid)                               | Dimension          | [Conditional](#conditions.includescommitmentdiscounts) | True         | String    |
| [Commitment Discount Name](#datasets.costandusage.commitmentdiscountname)                           | Dimension          | [Conditional](#conditions.includescommitmentdiscounts) | True         | String    |
| [Commitment Discount Quantity](#datasets.costandusage.commitmentdiscountquantity)                   | Metric             | [Conditional](#conditions.includescommitmentdiscounts) | True         | Decimal   |
| [Commitment Discount Status](#datasets.costandusage.commitmentdiscountstatus)                       | Dimension          | [Conditional](#conditions.includescommitmentdiscounts) | True         | String    |
| [Commitment Discount Type](#datasets.costandusage.commitmentdiscounttype)                           | Dimension          | [Conditional](#conditions.includescommitmentdiscounts) | True         | String    |
| [Commitment Discount Unit](#datasets.costandusage.commitmentdiscountunit)                           | Dimension          | [Conditional](#conditions.includescommitmentdiscounts) | True         | String    |
| [Commitment Program Eligibility Details](#datasets.costandusage.commitmentprogrameligibilitydetails)            | Dimension          | [Conditional](#conditions.includescommitmentprograms) | True         | JSON    |
| [Consumed Quantity](#datasets.costandusage.consumedquantity)                                        | Metric             | [Conditional](#conditions.includesusagemeasurement) | True         | Decimal   |
| [Consumed Unit](#datasets.costandusage.consumedunit)                                                | Dimension          | [Conditional](#conditions.includesusagemeasurement) | True         | String    |
| [Consumer ID](#datasets.costandusage.consumerid)                                                    | Dimension          | Conditional   | True         | String    |
| [Contract Applied](#datasets.costandusage.contractapplied)                                          | Dimension / Metric | [Conditional](#conditions.includescontractcommitments) | True         | JSON      |
| [Contracted Cost](#datasets.costandusage.contractedcost)                                            | Metric             | Mandatory     | False        | Decimal   |
| [Contracted Unit Price](#datasets.costandusage.contractedunitprice)                                 | Metric             | [Conditional](#conditions.includesnegotiatedpricing) | True         | Decimal   |
| [Effective Cost](#datasets.costandusage.effectivecost)                                              | Metric             | Mandatory     | False        | Decimal   |
| [Host Provider Name](#datasets.costandusage.hostprovidername)                                       | Dimension          | Mandatory     | False        | String    |
| [Invoice Detail ID](#datasets.costandusage.invoicedetailid)                                         | Dimension          | [Conditional](#conditions.includespayableinvoices) | True         | String    |
| [Invoice ID](#datasets.costandusage.invoiceid)                                                      | Dimension          | [Conditional](#conditions.includespayableinvoices) | True         | String    |
| [Invoice Issuer Name](#datasets.costandusage.invoiceissuername)                                     | Dimension          | Mandatory     | False        | String    |
| [List Cost](#datasets.costandusage.listcost)                                                        | Metric             | Mandatory     | False        | Decimal   |
| [List Unit Price](#datasets.costandusage.listunitprice)                                             | Metric             | [Conditional](#conditions.includeslistunitprices) | True         | Decimal   |
| [Pricing Category](#datasets.costandusage.pricingcategory)                                          | Dimension          | [Conditional](#conditions.includesmultiplepricingcategories) | True         | String    |
| [Pricing Currency](#datasets.costandusage.pricingcurrency)                                          | Dimension          | [Conditional](#conditions.includespricingbillingcurrencydifferences) | False        | String    |
| [Pricing Currency Contracted Unit Price](#datasets.costandusage.pricingcurrencycontractedunitprice) | Metric             | [Conditional](#conditions.includespricingbillingcurrencydifferences) | True         | Decimal   |
| [Pricing Currency Effective Cost](#datasets.costandusage.pricingcurrencyeffectivecost)              | Metric             | [Conditional](#conditions.includespricingbillingcurrencydifferences) | False        | Decimal   |
| [Pricing Currency List Unit Price](#datasets.costandusage.pricingcurrencylistunitprice)             | Metric             | [Conditional](#conditions.includespricingbillingcurrencydifferences) | True         | Decimal   |
| [Pricing Quantity](#datasets.costandusage.pricingquantity)                                          | Metric             | Mandatory     | True         | Decimal   |
| [Pricing Unit](#datasets.costandusage.pricingunit)                                                  | Dimension          | Mandatory     | True         | String    |
| [Principal ID](#datasets.costandusage.principalid)                                                  | Dimension          | Conditional   | True         | String    |
| [Region ID](#datasets.costandusage.regionid)                                                        | Dimension          | [Conditional](#conditions.includesregions) | True         | String    |
| [Region Name](#datasets.costandusage.regionname)                                                    | Dimension          | [Conditional](#conditions.includesregions) | True         | String    |
| [Resource ID](#datasets.costandusage.resourceid)                                                    | Dimension          | [Conditional](#conditions.includesprovisionedresources) | True         | String    |
| [Resource Name](#datasets.costandusage.resourcename)                                                | Dimension          | [Conditional](#conditions.includesprovisionedresources) | True         | String    |
| [Resource Type](#datasets.costandusage.resourcetype)                                                | Dimension          | [Conditional](#conditions.includesprovisionedresources) | True         | String    |
| [Service Category](#datasets.costandusage.servicecategory)                                          | Dimension          | Mandatory     | False        | String    |
| [Service Name](#datasets.costandusage.servicename)                                                  | Dimension          | Mandatory     | False        | String    |
| [Service Provider Name](#datasets.costandusage.serviceprovidername)                                 | Dimension          | Mandatory     | False        | String    |
| [Service Subcategory](#datasets.costandusage.servicesubcategory)                                    | Dimension          | Recommended   | False        | String    |
| [SKU ID](#datasets.costandusage.skuid)                                                              | Dimension          | [Conditional](#conditions.includesunitpricing) | True         | String    |
| [SKU Meter](#datasets.costandusage.skumeter)                                                        | Dimension          | [Conditional](#conditions.includesunitpricing) | True         | String    |
| [SKU Price Details](#datasets.costandusage.skupricedetails)                                         | Dimension          | [Conditional](#conditions.includesunitpricing) | True         | JSON      |
| [SKU Price ID](#datasets.costandusage.skupriceid)                                                   | Dimension          | [Conditional](#conditions.includesunitpricing) | True         | String    |
| [Sub Account ID](#datasets.costandusage.subaccountid)                                               | Dimension          | [Conditional](#conditions.includessubaccounts) | True         | String    |
| [Sub Account Name](#datasets.costandusage.subaccountname)                                           | Dimension          | [Conditional](#conditions.includessubaccounts) | True         | String    |
| [Sub Account Type](#datasets.costandusage.subaccounttype)                                           | Dimension          | [Conditional](#conditions.includesmultiplesubaccounttypes) | True         | String    |
| [Tags](#datasets.costandusage.tags)                                                                 | Dimension          | [Conditional](#conditions.includestags) | True         | JSON      |

## Relationships<!--SkipTOC-->

The Cost and Usage dataset can be joined to the Contract Commitment dataset through the use of the Contract Commitment ID.

* In the Cost and Usage dataset, Contract Commitment ID is a property within a JSON object array provided in Contract Applied column.
* In the Contract Commitment dataset, Contract Commitment ID is a column.

| Dataset A           | Dataset A Column  | Dataset B           | Dataset B Column       |
| ------------------- | ----------------- | ------------------- | ---------------------- |
| Cost and Usage      | Contract Applied  | Contract Commitment | Contract Commitment ID |

## Requirements<!--SkipTOC-->

CostAndUsage MUST adhere to the following requirements:

* CostAndUsage column presence MUST adhere to the following requirements:
  * CostAndUsage SHOULD include [AllocatedMethodDetails](#datasets.costandusage.allocatedmethoddetails) when the [*operating model*](#glossary:operating-model) [includes split cost allocation](#conditions.includessplitcostallocation).
  * CostAndUsage MUST include [AllocatedMethodId](#datasets.costandusage.allocatedmethodid) when the *operating model* [includes split cost allocation](#conditions.includessplitcostallocation).
  * CostAndUsage MUST include [AllocatedResourceId](#datasets.costandusage.allocatedresourceid) when the *operating model* [includes split cost allocation](#conditions.includessplitcostallocation).
  * CostAndUsage MUST include [AllocatedResourceName](#datasets.costandusage.allocatedresourcename) when the *operating model* [includes split cost allocation](#conditions.includessplitcostallocation).
  * CostAndUsage MUST include [AllocatedTags](#datasets.costandusage.allocatedtags) when the *operating model* [includes split cost allocation](#conditions.includessplitcostallocation).
  * CostAndUsage SHOULD include [AvailabilityZone](#datasets.costandusage.availabilityzone) when the *operating model* [includes availability zones](#conditions.includesavailabilityzones).
  * CostAndUsage MUST include [BilledCost](#datasets.costandusage.billedcost).
  * CostAndUsage MUST include [BillingAccountId](#datasets.costandusage.billingaccountid).
  * CostAndUsage MUST include [BillingAccountName](#datasets.costandusage.billingaccountname).
  * CostAndUsage MUST include [BillingAccountType](#datasets.costandusage.billingaccounttype) when the *operating model* [includes multiple billing account types](#conditions.includesmultiplebillingaccounttypes).
  * CostAndUsage MUST include [BillingCurrency](#datasets.costandusage.billingcurrency).
  * CostAndUsage MUST include [BillingPeriodEnd](#datasets.costandusage.billingperiodend).
  * CostAndUsage MUST include [BillingPeriodStart](#datasets.costandusage.billingperiodstart).
  * CostAndUsage MUST include [CapacityReservationId](#datasets.costandusage.capacityreservationid) when the *operating model* [includes capacity reservations](#conditions.includescapacityreservations).
  * CostAndUsage MUST include [CapacityReservationStatus](#datasets.costandusage.capacityreservationstatus) when the *operating model* [includes capacity reservations](#conditions.includescapacityreservations).
  * CostAndUsage MUST include [ChargeCategory](#datasets.costandusage.chargecategory).
  * CostAndUsage MUST include [ChargeClass](#datasets.costandusage.chargeclass).
  * CostAndUsage MUST include [ChargeDescription](#datasets.costandusage.chargedescription).
  * CostAndUsage SHOULD include [ChargeFrequency](#datasets.costandusage.chargefrequency).
  * CostAndUsage MUST include [ChargePeriodEnd](#datasets.costandusage.chargeperiodend).
  * CostAndUsage MUST include [ChargePeriodStart](#datasets.costandusage.chargeperiodstart).
  * CostAndUsage MUST include [CommitmentDiscountCategory](#datasets.costandusage.commitmentdiscountcategory) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentDiscountName](#datasets.costandusage.commitmentdiscountname) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentDiscountQuantity](#datasets.costandusage.commitmentdiscountquantity) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentDiscountUnit](#datasets.costandusage.commitmentdiscountunit) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentProgramEligibilityDetails](#datasets.costandusage.commitmentprogrameligibilitydetails) when the *operating model* [includes commitment programs](#conditions.includescommitmentprograms).
  * CostAndUsage MUST include [ConsumedQuantity](#datasets.costandusage.consumedquantity) when the *operating model* [includes usage measurement](#conditions.includesusagemeasurement).
  * CostAndUsage MUST include [ConsumedUnit](#datasets.costandusage.consumedunit) when the *operating model* [includes usage measurement](#conditions.includesusagemeasurement).
  * CostAndUsage MUST include [ConsumerId](#datasets.costandusage.consumerid) in at least one [*dataset instance*](#glossary:dataset-instance) when the *operating model* [includes consumers](#conditions.includesconsumers) and the customer has opted in to receive data at the consumer grain.
  * CostAndUsage MUST include [ContractApplied](#datasets.costandusage.contractapplied) when the *operating model* [includes contract commitments](#conditions.includescontractcommitments).
  * CostAndUsage MUST include [ContractedCost](#datasets.costandusage.contractedcost).
  * CostAndUsage MUST include [ContractedUnitPrice](#datasets.costandusage.contractedunitprice) when the *operating model* [includes negotiated pricing](#conditions.includesnegotiatedpricing).
  * CostAndUsage MUST include [EffectiveCost](#datasets.costandusage.effectivecost).
  * CostAndUsage MUST include [HostProviderName](#datasets.costandusage.hostprovidername).
  * CostAndUsage MUST include [InvoiceDetailId](#datasets.costandusage.invoicedetailid) when the *operating model* [includes payable invoices](#conditions.includespayableinvoices).
  * CostAndUsage MUST include [InvoiceId](#datasets.costandusage.invoiceid) when the *operating model* [includes payable invoices](#conditions.includespayableinvoices).
  * CostAndUsage MUST include [InvoiceIssuerName](#datasets.costandusage.invoiceissuername).
  * CostAndUsage MUST include [ListCost](#datasets.costandusage.listcost).
  * CostAndUsage MUST include [ListUnitPrice](#datasets.costandusage.listunitprice) when the *operating model* [includes list unit prices](#conditions.includeslistunitprices).
  * CostAndUsage MUST include [PricingCategory](#datasets.costandusage.pricingcategory) when the *operating model* [includes multiple pricing categories](#conditions.includesmultiplepricingcategories).
  * CostAndUsage MUST include [PricingCurrency](#datasets.costandusage.pricingcurrency) when the *operating model* [includes pricing and billing currency differences](#conditions.includespricingbillingcurrencydifferences).
  * CostAndUsage MUST adhere to the following [PricingCurrencyContractedUnitPrice](#datasets.costandusage.pricingcurrencycontractedunitprice) requirements:
    * CostAndUsage MUST include PricingCurrencyContractedUnitPrice when the *operating model* [includes virtual currency](#conditions.includesvirtualcurrency) and [includes list unit prices](#conditions.includeslistunitprices).
    * CostAndUsage SHOULD include PricingCurrencyContractedUnitPrice when the *operating model* [includes pricing and billing currency differences](#conditions.includespricingbillingcurrencydifferences) and [includes list unit prices](#conditions.includeslistunitprices).
    * CostAndUsage MAY include PricingCurrencyContractedUnitPrice in all other cases.
  * CostAndUsage MUST adhere to the following [PricingCurrencyEffectiveCost](#datasets.costandusage.pricingcurrencyeffectivecost) requirements:
    * CostAndUsage MUST include PricingCurrencyEffectiveCost when the *operating model* [includes virtual currency](#conditions.includesvirtualcurrency) and [includes list unit prices](#conditions.includeslistunitprices).
    * CostAndUsage SHOULD include PricingCurrencyEffectiveCost when the *operating model* [includes pricing and billing currency differences](#conditions.includespricingbillingcurrencydifferences) and [includes list unit prices](#conditions.includeslistunitprices).
    * CostAndUsage MAY include PricingCurrencyEffectiveCost in all other cases.
  * CostAndUsage MUST adhere to the following [PricingCurrencyListUnitPrice](#datasets.costandusage.pricingcurrencylistunitprice) requirements:
    * CostAndUsage MUST include PricingCurrencyListUnitPrice when the *operating model* [includes virtual currency](#conditions.includesvirtualcurrency) and [includes list unit prices](#conditions.includeslistunitprices).
    * CostAndUsage SHOULD include PricingCurrencyListUnitPrice when the *operating model* [includes pricing and billing currency differences](#conditions.includespricingbillingcurrencydifferences) and [includes list unit prices](#conditions.includeslistunitprices).
    * CostAndUsage MAY include PricingCurrencyListUnitPrice in all other cases.
  * CostAndUsage MUST include [PricingQuantity](#datasets.costandusage.pricingquantity).
  * CostAndUsage MUST include [PricingUnit](#datasets.costandusage.pricingunit).
  * CostAndUsage MUST include [PrincipalId](#datasets.costandusage.principalid) in at least one [*dataset instance*](#glossary:dataset-instance) when the *operating model* [includes principals](#conditions.includesprincipals) and the customer has opted in to receive data at the principal grain.
  * CostAndUsage MUST include [RegionId](#datasets.costandusage.regionid) when the *operating model* [includes regions](#conditions.includesregions).
  * CostAndUsage MUST include [RegionName](#datasets.costandusage.regionname) when the *operating model* [includes regions](#conditions.includesregions).
  * CostAndUsage MUST include [ResourceId](#datasets.costandusage.resourceid) when the *operating model* [includes provisioned resources](#conditions.includesprovisionedresources).
  * CostAndUsage MUST include [ResourceName](#datasets.costandusage.resourcename) when the *operating model* [includes provisioned resources](#conditions.includesprovisionedresources).
  * CostAndUsage MUST include [ResourceType](#datasets.costandusage.resourcetype) when the *operating model* [includes provisioned resources](#conditions.includesprovisionedresources) and [includes resource type assignment](#conditions.includesresourcetypeassignment).
  * CostAndUsage MUST include [ServiceCategory](#datasets.costandusage.servicecategory).
  * CostAndUsage MUST include [ServiceName](#datasets.costandusage.servicename).
  * CostAndUsage MUST include [ServiceProviderName](#datasets.costandusage.serviceprovidername).
  * CostAndUsage SHOULD include [ServiceSubcategory](#datasets.costandusage.servicesubcategory).
  * CostAndUsage MUST include [SkuId](#datasets.costandusage.skuid) when the *operating model* [includes unit pricing](#conditions.includesunitpricing).
  * CostAndUsage MUST include [SkuMeter](#datasets.costandusage.skumeter) when the *operating model* [includes unit pricing](#conditions.includesunitpricing).
  * CostAndUsage MUST include [SkuPriceDetails](#datasets.costandusage.skupricedetails) when the *operating model* [includes unit pricing](#conditions.includesunitpricing).
  * CostAndUsage MUST include [SkuPriceId](#datasets.costandusage.skupriceid) when the *operating model* [includes unit pricing](#conditions.includesunitpricing).
  * CostAndUsage MUST include [SubAccountId](#datasets.costandusage.subaccountid) when the *operating model* [includes sub accounts](#conditions.includessubaccounts).
  * CostAndUsage MUST include [SubAccountName](#datasets.costandusage.subaccountname) when the *operating model* [includes sub accounts](#conditions.includessubaccounts).
  * CostAndUsage MUST include [SubAccountType](#datasets.costandusage.subaccounttype) when the *operating model* [includes multiple sub account types](#conditions.includesmultiplesubaccounttypes).
  * CostAndUsage MUST include [Tags](#datasets.costandusage.tags) when the *operating model* [includes tags](#conditions.includestags).
  * CostAndUsage SHOULD include [*custom columns*](#glossary:custom-column) needed to identify all applied discounts when [*FOCUS columns*](#glossary:FOCUS-column) are not sufficient.
* CostAndUsage MUST conform to [CorrectionHandling](#attributes.correctionhandling) requirements.
* CostAndUsage MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.
* CostAndUsage MUST conform to [DatasetConfiguration](#attributes.datasetconfiguration) requirements.
* CostAndUsage MUST conform to [DeliveryHandling](#attributes.deliveryhandling) requirements.
* CostAndUsage MUST include *charges* representing unused portions of a [*commitment*](#glossary:commitment) when the *commitment* is not fully utilized.
* CostAndUsage MUST include separate *charges* representing discounted and non-discounted portions when a discount applies to only a portion of the originally incurred *charge*.
* When the *operating model* [includes split cost allocation](#conditions.includessplitcostallocation), CostAndUsage MUST adhere to the following requirements:
  * CostAndUsage MUST have its split cost allocation method documented and accessible to practitioners.
  * CostAndUsage SHOULD offer split cost allocation on an opt-in basis.
  * CostAndUsage MAY contain records for concepts not related to resource usage, when it aligns with the documented split cost allocation method.
  * CostAndUsage MAY contain records for unused or unallocated usage from the *origin charge* as separate *allocated charges*, when it aligns with the documented split cost allocation method.
  * CostAndUsage MAY contain *allocated charges* with apportioned costs for unused or unallocated usage, when it aligns with the documented split cost allocation method.
* CostAndUsage SHOULD reflect all applied discounts in *charges* they pertain to.
* CostAndUsage SHOULD NOT represent applied discounts as separate negating or offsetting *charges*.
* CostAndUsage *FOCUS columns* MUST conform to [DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling) requirements when the *operating model* [includes split cost allocation](#conditions.includessplitcostallocation).
* CostAndUsage *FOCUS columns* MUST conform to [FocusColumnHandling](#attributes.focuscolumnhandling) requirements.
* CostAndUsage *FOCUS columns* MUST conform to [NullHandling](#attributes.nullhandling) requirements.
* CostAndUsage *custom columns* MUST conform to [CustomColumnHandling](#attributes.customcolumnhandling) requirements.

## Dataset ID<!--SkipTOC-->

CostAndUsage

## Display Name<!--SkipTOC-->

Cost and Usage

## Description<!--SkipTOC-->

Describes the cost and usage incurred through using or purchasing a service provider's [*resources*](#glossary:resource) or [*services*](#glossary:service).

## Version Introduced<!--SkipTOC-->

0.5
