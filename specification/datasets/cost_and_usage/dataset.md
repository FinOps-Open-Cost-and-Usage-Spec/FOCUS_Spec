# Cost and Usage

The Cost and Usage dataset is the primary dataset for FOCUS cost and usage data.

The specification for the Cost and Usage dataset defines a group of columns that provide qualitative values (such as dates, resource, and service provider information) categorized as "dimensions" and quantitative values (numeric values) categorized as "metrics" that can be used for performing various [FinOps capabilities][FODOFC]. Metrics are commonly used for aggregations (sum, multiplication, averaging etc.) and statistical operations within the dataset. Dimensions are commonly used to categorize, filter, and reveal details in your data when combined with metrics. The columns are presented in alphabetical order.

## Columns<!--SkipTOC-->

| Column                                                                        | Column Type        | Feature Level | Allows Nulls | Data Type |
| ----------------------------------------------------------------------------- | ------------------ | ------------- | ------------ | --------- |
| [Allocated Method Details](#datamodel.costandusage.allocatedmethoddetails)                           | Dimension / Metric | Recommended   | True         | JSON      |
| [Allocated Method ID](#datamodel.costandusage.allocatedmethodid)                                     | Dimension          | [Conditional](#conditions.includessplitcostallocation) | True         | String    |
| [Allocated Resource ID](#datamodel.costandusage.allocatedresourceid)                                 | Dimension          | [Conditional](#conditions.includessplitcostallocation) | True         | String    |
| [Allocated Resource Name](#datamodel.costandusage.allocatedresourcename)                             | Dimension          | [Conditional](#conditions.includessplitcostallocation) | True         | String    |
| [Allocated Tags](#datamodel.costandusage.allocatedtags)                                              | Dimension          | [Conditional](#conditions.includessplitcostallocation) | True         | JSON      |
| [Availability Zone](#datamodel.costandusage.availabilityzone)                                        | Dimension          | Recommended   | True         | String    |
| [Billed Cost](#datamodel.costandusage.billedcost)                                                    | Metric             | Mandatory     | False        | Decimal   |
| [Billing Account ID](#datamodel.costandusage.billingaccountid)                                       | Dimension          | Mandatory     | False        | String    |
| [Billing Account Name](#datamodel.costandusage.billingaccountname)                                   | Dimension          | Mandatory     | True         | String    |
| [Billing Account Type](#datamodel.costandusage.billingaccounttype)                                   | Dimension          | [Conditional](#conditions.includesmultiplebillingaccounttypes) | False        | String    |
| [Billing Currency](#datamodel.costandusage.billingcurrency)                                          | Dimension          | Mandatory     | False        | String    |
| [Billing Period End](#datamodel.costandusage.billingperiodend)                                       | Dimension          | Mandatory     | False        | Date/Time |
| [Billing Period Start](#datamodel.costandusage.billingperiodstart)                                   | Dimension          | Mandatory     | False        | Date/Time |
| [Capacity Reservation ID](#datamodel.costandusage.capacityreservationid)                             | Dimension          | [Conditional](#conditions.includescapacityreservations) | True         | String    |
| [Capacity Reservation Status](#datamodel.costandusage.capacityreservationstatus)                     | Dimension          | [Conditional](#conditions.includescapacityreservations) | True         | String    |
| [Charge Category](#datamodel.costandusage.chargecategory)                                            | Dimension          | Mandatory     | False        | String    |
| [Charge Class](#datamodel.costandusage.chargeclass)                                                  | Dimension          | Mandatory     | True         | String    |
| [Charge Description](#datamodel.costandusage.chargedescription)                                      | Dimension          | Mandatory     | True         | String    |
| [Charge Frequency](#datamodel.costandusage.chargefrequency)                                          | Dimension          | Recommended   | False        | String    |
| [Charge Period End](#datamodel.costandusage.chargeperiodend)                                         | Dimension          | Mandatory     | False        | Date/Time |
| [Charge Period Start](#datamodel.costandusage.chargeperiodstart)                                     | Dimension          | Mandatory     | False        | Date/Time |
| [Commitment Discount Category](#datamodel.costandusage.commitmentdiscountcategory)                   | Dimension          | [Conditional](#conditions.includescommitmentdiscounts) | True         | String    |
| [Commitment Discount ID](#datamodel.costandusage.commitmentdiscountid)                               | Dimension          | [Conditional](#conditions.includescommitmentdiscounts) | True         | String    |
| [Commitment Discount Name](#datamodel.costandusage.commitmentdiscountname)                           | Dimension          | [Conditional](#conditions.includescommitmentdiscounts) | True         | String    |
| [Commitment Discount Quantity](#datamodel.costandusage.commitmentdiscountquantity)                   | Metric             | [Conditional](#conditions.includescommitmentdiscounts) | True         | Decimal   |
| [Commitment Discount Status](#datamodel.costandusage.commitmentdiscountstatus)                       | Dimension          | [Conditional](#conditions.includescommitmentdiscounts) | True         | String    |
| [Commitment Discount Type](#datamodel.costandusage.commitmentdiscounttype)                           | Dimension          | [Conditional](#conditions.includescommitmentdiscounts) | True         | String    |
| [Commitment Discount Unit](#datamodel.costandusage.commitmentdiscountunit)                           | Dimension          | [Conditional](#conditions.includescommitmentdiscounts) | True         | String    |
| [Commitment Program Eligibility Details](#datamodel.costandusage.commitmentprogrameligibilitydetails)            | Dimension          | [Conditional](#conditions.includescommitmentprograms) | True         | JSON    |
| [Consumed Quantity](#datamodel.costandusage.consumedquantity)                                        | Metric             | [Conditional](#conditions.includesusagemeasurement) | True         | Decimal   |
| [Consumed Unit](#datamodel.costandusage.consumedunit)                                                | Dimension          | [Conditional](#conditions.includesusagemeasurement) | True         | String    |
| [Contract Applied](#datamodel.costandusage.contractapplied)                                          | Dimension / Metric | [Conditional](#conditions.includescontractcommitments) | True         | JSON      |
| [Contracted Cost](#datamodel.costandusage.contractedcost)                                            | Metric             | Mandatory     | False        | Decimal   |
| [Contracted Unit Price](#datamodel.costandusage.contractedunitprice)                                 | Metric             | [Conditional](#conditions.includesnegotiatedpricing) | True         | Decimal   |
| [Effective Cost](#datamodel.costandusage.effectivecost)                                              | Metric             | Mandatory     | False        | Decimal   |
| [Host Provider Name](#datamodel.costandusage.hostprovidername)                                       | Dimension          | Mandatory     | False        | String    |
| [Invoice Detail ID](#datamodel.costandusage.invoicedetailid)                                         | Dimension          | [Conditional](#conditions.includespayableinvoices) | True         | String    |
| [Invoice ID](#datamodel.costandusage.invoiceid)                                                      | Dimension          | [Conditional](#conditions.includespayableinvoices) | True         | String    |
| [Invoice Issuer Name](#datamodel.costandusage.invoiceissuername)                                     | Dimension          | Mandatory     | False        | String    |
| [List Cost](#datamodel.costandusage.listcost)                                                        | Metric             | Mandatory     | False        | Decimal   |
| [List Unit Price](#datamodel.costandusage.listunitprice)                                             | Metric             | [Conditional](#conditions.includeslistunitprices) | True         | Decimal   |
| [Pricing Category](#datamodel.costandusage.pricingcategory)                                          | Dimension          | [Conditional](#conditions.includesmultiplepricingcategories) | True         | String    |
| [Pricing Currency](#datamodel.costandusage.pricingcurrency)                                          | Dimension          | [Conditional](#conditions.includespricing-billingcurrencydifferences) | False        | String    |
| [Pricing Currency Contracted Unit Price](#datamodel.costandusage.pricingcurrencycontractedunitprice) | Metric             | [Conditional](#conditions.includespricing-billingcurrencydifferences) | True         | Decimal   |
| [Pricing Currency Effective Cost](#datamodel.costandusage.pricingcurrencyeffectivecost)              | Metric             | [Conditional](#conditions.includespricing-billingcurrencydifferences) | False        | Decimal   |
| [Pricing Currency List Unit Price](#datamodel.costandusage.pricingcurrencylistunitprice)             | Metric             | [Conditional](#conditions.includespricing-billingcurrencydifferences) | True         | Decimal   |
| [Pricing Quantity](#datamodel.costandusage.pricingquantity)                                          | Metric             | Mandatory     | True         | Decimal   |
| [Pricing Unit](#datamodel.costandusage.pricingunit)                                                  | Dimension          | Mandatory     | True         | String    |
| [Principal ID](#datamodel.costandusage.principalid)                                                  | Dimension          | [Conditional](#conditions.includesrequesterattribution) | True         | String    |
| [Region ID](#datamodel.costandusage.regionid)                                                        | Dimension          | [Conditional](#conditions.includesregions) | True         | String    |
| [Region Name](#datamodel.costandusage.regionname)                                                    | Dimension          | [Conditional](#conditions.includesregions) | True         | String    |
| [Resource ID](#datamodel.costandusage.resourceid)                                                    | Dimension          | [Conditional](#conditions.includesprovisionedresources) | True         | String    |
| [Resource Name](#datamodel.costandusage.resourcename)                                                | Dimension          | [Conditional](#conditions.includesprovisionedresources) | True         | String    |
| [Resource Type](#datamodel.costandusage.resourcetype)                                                | Dimension          | [Conditional](#conditions.includesprovisionedresources) | True         | String    |
| [Service Category](#datamodel.costandusage.servicecategory)                                          | Dimension          | Mandatory     | False        | String    |
| [Service Name](#datamodel.costandusage.servicename)                                                  | Dimension          | Mandatory     | False        | String    |
| [Service Provider Name](#datamodel.costandusage.serviceprovidername)                                 | Dimension          | Mandatory     | False        | String    |
| [Service Subcategory](#datamodel.costandusage.servicesubcategory)                                    | Dimension          | Recommended   | False        | String    |
| [SKU ID](#datamodel.costandusage.skuid)                                                              | Dimension          | [Conditional](#conditions.includesunitpricing) | True         | String    |
| [SKU Meter](#datamodel.costandusage.skumeter)                                                        | Dimension          | [Conditional](#conditions.includesunitpricing) | True         | String    |
| [SKU Price Details](#datamodel.costandusage.skupricedetails)                                         | Dimension          | [Conditional](#conditions.includesunitpricing) | True         | JSON      |
| [SKU Price ID](#datamodel.costandusage.skupriceid)                                                   | Dimension          | [Conditional](#conditions.includesunitpricing) | True         | String    |
| [Sub Account ID](#datamodel.costandusage.subaccountid)                                               | Dimension          | [Conditional](#conditions.includessubaccounts) | True         | String    |
| [Sub Account Name](#datamodel.costandusage.subaccountname)                                           | Dimension          | [Conditional](#conditions.includessubaccounts) | True         | String    |
| [Sub Account Type](#datamodel.costandusage.subaccounttype)                                           | Dimension          | [Conditional](#conditions.includesmultiplesubaccounttypes) | True         | String    |
| [Tags](#datamodel.costandusage.tags)                                                                 | Dimension          | [Conditional](#conditions.includestags) | True         | JSON      |

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
  * CostAndUsage SHOULD include [AllocatedMethodDetails](#datamodel.costandusage.allocatedmethoddetails) when the [*operating model*](#glossary:operating-model) [includes split cost allocation](#conditions.includessplitcostallocation).
  * CostAndUsage MUST include [AllocatedMethodId](#datamodel.costandusage.allocatedmethodid) when the *operating model* [includes split cost allocation](#conditions.includessplitcostallocation).
  * CostAndUsage MUST include [AllocatedResourceId](#datamodel.costandusage.allocatedresourceid) when the *operating model* [includes split cost allocation](#conditions.includessplitcostallocation).
  * CostAndUsage MUST include [AllocatedResourceName](#datamodel.costandusage.allocatedresourcename) when the *operating model* [includes split cost allocation](#conditions.includessplitcostallocation).
  * CostAndUsage MUST include [AllocatedTags](#datamodel.costandusage.allocatedtags) when the *operating model* [includes split cost allocation](#conditions.includessplitcostallocation).
  * CostAndUsage SHOULD include [AvailabilityZone](#datamodel.costandusage.availabilityzone) when the *operating model* [includes availability zones](#conditions.includesavailabilityzones).
  * CostAndUsage MUST include [BilledCost](#datamodel.costandusage.billedcost).
  * CostAndUsage MUST include [BillingAccountId](#datamodel.costandusage.billingaccountid).
  * CostAndUsage MUST include [BillingAccountName](#datamodel.costandusage.billingaccountname).
  * CostAndUsage MUST include [BillingAccountType](#datamodel.costandusage.billingaccounttype) when the *operating model* [includes multiple billing account types](#conditions.includesmultiplebillingaccounttypes).
  * CostAndUsage MUST include [BillingCurrency](#datamodel.costandusage.billingcurrency).
  * CostAndUsage MUST include [BillingPeriodEnd](#datamodel.costandusage.billingperiodend).
  * CostAndUsage MUST include [BillingPeriodStart](#datamodel.costandusage.billingperiodstart).
  * CostAndUsage MUST include [CapacityReservationId](#datamodel.costandusage.capacityreservationid) when the *operating model* [includes capacity reservations](#conditions.includescapacityreservations).
  * CostAndUsage MUST include [CapacityReservationStatus](#datamodel.costandusage.capacityreservationstatus) when the *operating model* [includes capacity reservations](#conditions.includescapacityreservations).
  * CostAndUsage MUST include [ChargeCategory](#datamodel.costandusage.chargecategory).
  * CostAndUsage MUST include [ChargeClass](#datamodel.costandusage.chargeclass).
  * CostAndUsage MUST include [ChargeDescription](#datamodel.costandusage.chargedescription).
  * CostAndUsage SHOULD include [ChargeFrequency](#datamodel.costandusage.chargefrequency).
  * CostAndUsage MUST include [ChargePeriodEnd](#datamodel.costandusage.chargeperiodend).
  * CostAndUsage MUST include [ChargePeriodStart](#datamodel.costandusage.chargeperiodstart).
  * CostAndUsage MUST include [CommitmentDiscountCategory](#datamodel.costandusage.commitmentdiscountcategory) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentDiscountId](#datamodel.costandusage.commitmentdiscountid) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentDiscountName](#datamodel.costandusage.commitmentdiscountname) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentDiscountQuantity](#datamodel.costandusage.commitmentdiscountquantity) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentDiscountStatus](#datamodel.costandusage.commitmentdiscountstatus) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentDiscountType](#datamodel.costandusage.commitmentdiscounttype) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentDiscountUnit](#datamodel.costandusage.commitmentdiscountunit) when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts).
  * CostAndUsage MUST include [CommitmentProgramEligibilityDetails](#datamodel.costandusage.commitmentprogrameligibilitydetails) when the *operating model* [includes commitment programs](#conditions.includescommitmentprograms).
  * CostAndUsage MUST include [ConsumedQuantity](#datamodel.costandusage.consumedquantity) when the *operating model* [includes usage measurement](#conditions.includesusagemeasurement).
  * CostAndUsage MUST include [ConsumedUnit](#datamodel.costandusage.consumedunit) when the *operating model* [includes usage measurement](#conditions.includesusagemeasurement).
  * CostAndUsage MUST include [ContractApplied](#datamodel.costandusage.contractapplied) when the *operating model* [includes contract commitments](#conditions.includescontractcommitments).
  * CostAndUsage MUST include [ContractedCost](#datamodel.costandusage.contractedcost).
  * CostAndUsage MUST include [ContractedUnitPrice](#datamodel.costandusage.contractedunitprice) when the *operating model* [includes negotiated pricing](#conditions.includesnegotiatedpricing).
  * CostAndUsage MUST include [EffectiveCost](#datamodel.costandusage.effectivecost).
  * CostAndUsage MUST include [HostProviderName](#datamodel.costandusage.hostprovidername).
  * CostAndUsage MUST include [InvoiceDetailId](#datamodel.costandusage.invoicedetailid) when the *operating model* [includes payable invoices](#conditions.includespayableinvoices).
  * CostAndUsage MUST include [InvoiceId](#datamodel.costandusage.invoiceid) when the *operating model* [includes payable invoices](#conditions.includespayableinvoices).
  * CostAndUsage MUST include [InvoiceIssuerName](#datamodel.costandusage.invoiceissuername).
  * CostAndUsage MUST include [ListCost](#datamodel.costandusage.listcost).
  * CostAndUsage MUST include [ListUnitPrice](#datamodel.costandusage.listunitprice) when the *operating model* [includes list unit prices](#conditions.includeslistunitprices).
  * CostAndUsage MUST include [PricingCategory](#datamodel.costandusage.pricingcategory) when the *operating model* [includes multiple pricing categories](#conditions.includesmultiplepricingcategories).
  * CostAndUsage MUST include [PricingCurrency](#datamodel.costandusage.pricingcurrency) when the *operating model* [includes pricing and billing currency differences](#conditions.includespricing-billingcurrencydifferences).
  * CostAndUsage MUST adhere to the following [PricingCurrencyContractedUnitPrice](#datamodel.costandusage.pricingcurrencycontractedunitprice) requirements:
    * CostAndUsage MUST include PricingCurrencyContractedUnitPrice when the *operating model* [includes virtual currency](#conditions.includesvirtualcurrency) and [includes list unit prices](#conditions.includeslistunitprices).
    * CostAndUsage SHOULD include PricingCurrencyContractedUnitPrice when the *operating model* [includes pricing and billing currency differences](#conditions.includespricing-billingcurrencydifferences) and [includes list unit prices](#conditions.includeslistunitprices).
    * CostAndUsage MAY include PricingCurrencyContractedUnitPrice in all other cases.
  * CostAndUsage MUST adhere to the following [PricingCurrencyEffectiveCost](#datamodel.costandusage.pricingcurrencyeffectivecost) requirements:
    * CostAndUsage MUST include PricingCurrencyEffectiveCost when the *operating model* [includes virtual currency](#conditions.includesvirtualcurrency) and [includes list unit prices](#conditions.includeslistunitprices).
    * CostAndUsage SHOULD include PricingCurrencyEffectiveCost when the *operating model* [includes pricing and billing currency differences](#conditions.includespricing-billingcurrencydifferences) and [includes list unit prices](#conditions.includeslistunitprices).
    * CostAndUsage MAY include PricingCurrencyEffectiveCost in all other cases.
  * CostAndUsage MUST adhere to the following [PricingCurrencyListUnitPrice](#datamodel.costandusage.pricingcurrencylistunitprice) requirements:
    * CostAndUsage MUST include PricingCurrencyListUnitPrice when the *operating model* [includes virtual currency](#conditions.includesvirtualcurrency) and [includes list unit prices](#conditions.includeslistunitprices).
    * CostAndUsage SHOULD include PricingCurrencyListUnitPrice when the *operating model* [includes pricing and billing currency differences](#conditions.includespricing-billingcurrencydifferences) and [includes list unit prices](#conditions.includeslistunitprices).
    * CostAndUsage MAY include PricingCurrencyListUnitPrice in all other cases.
  * CostAndUsage MUST include [PricingQuantity](#datamodel.costandusage.pricingquantity).
  * CostAndUsage MUST include [PricingUnit](#datamodel.costandusage.pricingunit).
  * CostAndUsage MUST include [PrincipalId](#datamodel.costandusage.principalid) when the *operating model* [includes requester attribution](#conditions.includesrequesterattribution).
  * CostAndUsage MUST include [RegionId](#datamodel.costandusage.regionid) when the *operating model* [includes regions](#conditions.includesregions).
  * CostAndUsage MUST include [RegionName](#datamodel.costandusage.regionname) when the *operating model* [includes regions](#conditions.includesregions).
  * CostAndUsage MUST include [ResourceId](#datamodel.costandusage.resourceid) when the *operating model* [includes provisioned resources](#conditions.includesprovisionedresources).
  * CostAndUsage MUST include [ResourceName](#datamodel.costandusage.resourcename) when the *operating model* [includes provisioned resources](#conditions.includesprovisionedresources).
  * CostAndUsage MUST include [ResourceType](#datamodel.costandusage.resourcetype) when the *operating model* [includes provisioned resources](#conditions.includesprovisionedresources) and [includes resource type assignment](#conditions.includesresourcetypeassignment).
  * CostAndUsage MUST include [ServiceCategory](#datamodel.costandusage.servicecategory).
  * CostAndUsage MUST include [ServiceName](#datamodel.costandusage.servicename).
  * CostAndUsage MUST include [ServiceProviderName](#datamodel.costandusage.serviceprovidername).
  * CostAndUsage SHOULD include [ServiceSubcategory](#datamodel.costandusage.servicesubcategory).
  * CostAndUsage MUST include [SkuId](#datamodel.costandusage.skuid) when the *operating model* [includes unit pricing](#conditions.includesunitpricing).
  * CostAndUsage MUST include [SkuMeter](#datamodel.costandusage.skumeter) when the *operating model* [includes unit pricing](#conditions.includesunitpricing).
  * CostAndUsage MUST include [SkuPriceDetails](#datamodel.costandusage.skupricedetails) when the *operating model* [includes unit pricing](#conditions.includesunitpricing).
  * CostAndUsage MUST include [SkuPriceId](#datamodel.costandusage.skupriceid) when the *operating model* [includes unit pricing](#conditions.includesunitpricing).
  * CostAndUsage MUST include [SubAccountId](#datamodel.costandusage.subaccountid) when the *operating model* [includes sub accounts](#conditions.includessubaccounts).
  * CostAndUsage MUST include [SubAccountName](#datamodel.costandusage.subaccountname) when the *operating model* [includes sub accounts](#conditions.includessubaccounts).
  * CostAndUsage MUST include [SubAccountType](#datamodel.costandusage.subaccounttype) when the *operating model* [includes multiple sub account types](#conditions.includesmultiplesubaccounttypes).
  * CostAndUsage MUST include [Tags](#datamodel.costandusage.tags) when the *operating model* [includes tags](#conditions.includestags).
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
