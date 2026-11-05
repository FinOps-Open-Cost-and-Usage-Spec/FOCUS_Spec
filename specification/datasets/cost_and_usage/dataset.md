# Cost and Usage

The [Cost and Usage](#ds) dataset is the primary dataset for FOCUS cost and usage data.

The specification for the [Cost and Usage](#ds) dataset defines a group of columns that provide qualitative values (such as dates, resource, and service provider information) categorized as "dimensions" and quantitative values (numeric values) categorized as "metrics" that can be used for performing various [FinOps capabilities][FODOFC]. Metrics are commonly used for aggregations (sum, multiplication, averaging etc.) and statistical operations within the dataset. Dimensions are commonly used to categorize, filter, and reveal details in your data when combined with metrics. The columns are presented in alphabetical order.

> **Note:** A [Cost and Usage](#ds) dataset may carry values that are classified as Personal Data or Personally Identifiable Information (PII) under privacy regulations such as GDPR or CCPA, including values that are pseudonymized rather than plain-text. Identity attributes, carried in columns such as [Requester Details](#col), and customer-defined values, carried in columns such as [Tags](#col), are the most common sources. Which of these values a dataset carries is a matter for the [*data generator*](#metadata.datagenerator) and the data consumer to settle between them. Organizations need to separately ensure that the ingestion, storage, and processing of a dataset comply with the privacy regulations applicable to them and with their internal data privacy, security, and retention policies. Cost and usage data is commonly retained for multi-year trend analysis, which extends the period over which those obligations apply.

## Columns<!--SkipTOC-->

| Column                                                                        | Column Type        | Feature Level | Allows Nulls | Data Type |
| ----------------------------------------------------------------------------- | ------------------ | ------------- | ------------ | --------- |
| [Allocated Method Details](#datamodel.costandusage.allocatedmethoddetails)                           | Dimension / Metric | Recommended   | True         | JSON      |
| [Allocated Method ID](#datamodel.costandusage.allocatedmethodid)                                     | Dimension          | Conditional | True         | String    |
| [Allocated Resource ID](#datamodel.costandusage.allocatedresourceid)                                 | Dimension          | Conditional | True         | String    |
| [Allocated Resource Name](#datamodel.costandusage.allocatedresourcename)                             | Dimension          | Conditional | True         | String    |
| [Allocated Service Name](#datamodel.costandusage.allocatedservicename)                               | Dimension          | Conditional | True         | String    |
| [Allocated Tags](#datamodel.costandusage.allocatedtags)                                              | Dimension          | Conditional | True         | JSON      |
| [Availability Zone](#datamodel.costandusage.availabilityzone)                                        | Dimension          | Recommended   | True         | String    |
| [Billed Cost](#datamodel.costandusage.billedcost)                                                    | Metric             | Mandatory     | False        | Decimal   |
| [Billing Account ID](#datamodel.costandusage.billingaccountid)                                       | Dimension          | Mandatory     | False        | String    |
| [Billing Account Name](#datamodel.costandusage.billingaccountname)                                   | Dimension          | Mandatory     | True         | String    |
| [Billing Account Type](#datamodel.costandusage.billingaccounttype)                                   | Dimension          | Conditional | False        | String    |
| [Billing Currency](#datamodel.costandusage.billingcurrency)                                          | Dimension          | Mandatory     | False        | String    |
| [Billing Period End](#datamodel.costandusage.billingperiodend)                                       | Dimension          | Mandatory     | False        | Date/Time |
| [Billing Period Start](#datamodel.costandusage.billingperiodstart)                                   | Dimension          | Mandatory     | False        | Date/Time |
| [Capacity Reservation ID](#datamodel.costandusage.capacityreservationid)                             | Dimension          | Conditional | True         | String    |
| [Capacity Reservation Status](#datamodel.costandusage.capacityreservationstatus)                     | Dimension          | Conditional | True         | String    |
| [Charge Category](#datamodel.costandusage.chargecategory)                                            | Dimension          | Mandatory     | False        | String    |
| [Charge Class](#datamodel.costandusage.chargeclass)                                                  | Dimension          | Mandatory     | True         | String    |
| [Charge Description](#datamodel.costandusage.chargedescription)                                      | Dimension          | Mandatory     | True         | String    |
| [Charge Frequency](#datamodel.costandusage.chargefrequency)                                          | Dimension          | Recommended   | False        | String    |
| [Charge Period End](#datamodel.costandusage.chargeperiodend)                                         | Dimension          | Mandatory     | False        | Date/Time |
| [Charge Period Start](#datamodel.costandusage.chargeperiodstart)                                     | Dimension          | Mandatory     | False        | Date/Time |
| [Commitment Discount Category](#datamodel.costandusage.commitmentdiscountcategory)                   | Dimension          | Conditional | True         | String    |
| [Commitment Discount ID](#datamodel.costandusage.commitmentdiscountid)                               | Dimension          | Conditional | True         | String    |
| [Commitment Discount Name](#datamodel.costandusage.commitmentdiscountname)                           | Dimension          | Conditional | True         | String    |
| [Commitment Discount Quantity](#datamodel.costandusage.commitmentdiscountquantity)                   | Metric             | Conditional | True         | Decimal   |
| [Commitment Discount Status](#datamodel.costandusage.commitmentdiscountstatus)                       | Dimension          | Conditional | True         | String    |
| [Commitment Discount Type](#datamodel.costandusage.commitmentdiscounttype)                           | Dimension          | Conditional | True         | String    |
| [Commitment Discount Unit](#datamodel.costandusage.commitmentdiscountunit)                           | Dimension          | Conditional | True         | String    |
| [Commitment Program Eligibility Details](#datamodel.costandusage.commitmentprogrameligibilitydetails)            | Dimension          | Conditional | True         | JSON    |
| [Consumed Quantity](#datamodel.costandusage.consumedquantity)                                        | Metric             | Conditional | True         | Decimal   |
| [Consumed Unit](#datamodel.costandusage.consumedunit)                                                | Dimension          | Conditional | True         | String    |
| [Contract Applied](#datamodel.costandusage.contractapplied)                                          | Dimension / Metric | Conditional | True         | JSON      |
| [Contracted Cost](#datamodel.costandusage.contractedcost)                                            | Metric             | Mandatory     | False        | Decimal   |
| [Contracted Unit Price](#datamodel.costandusage.contractedunitprice)                                 | Metric             | Conditional | True         | Decimal   |
| [Credential ID](#datamodel.costandusage.credentialid)                                                | Dimension          | Conditional | True         | String    |
| [Effective Cost](#datamodel.costandusage.effectivecost)                                              | Metric             | Mandatory     | False        | Decimal   |
| [Host Provider Name](#datamodel.costandusage.hostprovidername)                                       | Dimension          | Mandatory     | False        | String    |
| [Invoice Detail ID](#datamodel.costandusage.invoicedetailid)                                         | Dimension          | Conditional | True         | String    |
| [Invoice ID](#datamodel.costandusage.invoiceid)                                                      | Dimension          | Conditional | True         | String    |
| [Invoice Issuer Name](#datamodel.costandusage.invoiceissuername)                                     | Dimension          | Mandatory     | False        | String    |
| [List Cost](#datamodel.costandusage.listcost)                                                        | Metric             | Mandatory     | False        | Decimal   |
| [List Unit Price](#datamodel.costandusage.listunitprice)                                             | Metric             | Conditional | True         | Decimal   |
| [Pricing Category](#datamodel.costandusage.pricingcategory)                                          | Dimension          | Conditional | True         | String    |
| [Pricing Currency](#datamodel.costandusage.pricingcurrency)                                          | Dimension          | Conditional | False        | String    |
| [Pricing Currency Contracted Unit Price](#datamodel.costandusage.pricingcurrencycontractedunitprice) | Metric             | Conditional | True         | Decimal   |
| [Pricing Currency Effective Cost](#datamodel.costandusage.pricingcurrencyeffectivecost)              | Metric             | Conditional | False        | Decimal   |
| [Pricing Currency List Unit Price](#datamodel.costandusage.pricingcurrencylistunitprice)             | Metric             | Conditional | True         | Decimal   |
| [Pricing Quantity](#datamodel.costandusage.pricingquantity)                                          | Metric             | Mandatory     | True         | Decimal   |
| [Pricing Unit](#datamodel.costandusage.pricingunit)                                                  | Dimension          | Mandatory     | True         | String    |
| [Principal ID](#datamodel.costandusage.principalid)                                                  | Dimension          | Conditional | True         | String    |
| [Region ID](#datamodel.costandusage.regionid)                                                        | Dimension          | Conditional | True         | String    |
| [Region Name](#datamodel.costandusage.regionname)                                                    | Dimension          | Conditional | True         | String    |
| [Requester Details](#datamodel.costandusage.requesterdetails)                                        | Dimension          | Conditional | True         | JSON      |
| [Resource ID](#datamodel.costandusage.resourceid)                                                    | Dimension          | Conditional | True         | String    |
| [Resource Name](#datamodel.costandusage.resourcename)                                                | Dimension          | Conditional | True         | String    |
| [Resource Type](#datamodel.costandusage.resourcetype)                                                | Dimension          | Conditional | True         | String    |
| [Service Category](#datamodel.costandusage.servicecategory)                                          | Dimension          | Mandatory     | False        | String    |
| [Service Name](#datamodel.costandusage.servicename)                                                  | Dimension          | Mandatory     | False        | String    |
| [Service Provider Name](#datamodel.costandusage.serviceprovidername)                                 | Dimension          | Mandatory     | False        | String    |
| [Service Subcategory](#datamodel.costandusage.servicesubcategory)                                    | Dimension          | Recommended   | False        | String    |
| [SKU ID](#datamodel.costandusage.skuid)                                                              | Dimension          | Conditional | True         | String    |
| [SKU Meter](#datamodel.costandusage.skumeter)                                                        | Dimension          | Conditional | True         | String    |
| [SKU Price Details](#datamodel.costandusage.skupricedetails)                                         | Dimension          | Conditional | True         | JSON      |
| [SKU Price ID](#datamodel.costandusage.skupriceid)                                                   | Dimension          | Conditional | True         | String    |
| [Sub Account ID](#datamodel.costandusage.subaccountid)                                               | Dimension          | Conditional | True         | String    |
| [Sub Account Name](#datamodel.costandusage.subaccountname)                                           | Dimension          | Conditional | True         | String    |
| [Sub Account Type](#datamodel.costandusage.subaccounttype)                                           | Dimension          | Conditional | True         | String    |
| [Tags](#datamodel.costandusage.tags)                                                                 | Dimension          | Conditional | True         | JSON      |

## Relationships<!--SkipTOC-->

The [Cost and Usage](#ds) dataset can be joined to the [Contract Commitment](#ds) dataset through the use of the [Contract Commitment ID](#col:ContractCommitment.ContractCommitmentId).

* In the [Cost and Usage](#ds) dataset, Contract Commitment ID is a property within a JSON object array provided in [Contract Applied](#col) column.
* In the [Contract Commitment](#ds) dataset, [Contract Commitment ID](#col:ContractCommitment.ContractCommitmentId) is a column.

| Dataset A           | Dataset A Column  | Dataset B           | Dataset B Column       |
| ------------------- | ----------------- | ------------------- | ---------------------- |
| Cost and Usage      | Contract Applied  | Contract Commitment | Contract Commitment ID |

## Requirements<!--SkipTOC-->

[CostAndUsage](#ds) MUST adhere to the following requirements:

* [CostAndUsage](#ds) column presence MUST adhere to the following requirements:
  * [CostAndUsage](#ds) SHOULD include [AllocatedMethodDetails](#col) when the [operating model](#term) [includes split cost allocation](#omc).
  * [CostAndUsage](#ds) MUST include [AllocatedMethodId](#col) when the [operating model](#term) includes split cost allocation.
  * [CostAndUsage](#ds) MUST include [AllocatedResourceId](#col) when the [operating model](#term) includes split cost allocation.
  * [CostAndUsage](#ds) MUST include [AllocatedResourceName](#col) when the [operating model](#term) includes split cost allocation.
  * [CostAndUsage](#ds) MUST include [AllocatedServiceName](#col) when the [operating model](#term) includes split cost allocation.
  * [CostAndUsage](#ds) MUST include [AllocatedTags](#col) when the [operating model](#term) includes split cost allocation.
  * [CostAndUsage](#ds) SHOULD include [AvailabilityZone](#col) when the [operating model](#term) [includes availability zones](#omc).
  * [CostAndUsage](#ds) MUST include [BilledCost](#col).
  * [CostAndUsage](#ds) MUST include [BillingAccountId](#col).
  * [CostAndUsage](#ds) MUST include [BillingAccountName](#col).
  * [CostAndUsage](#ds) MUST include [BillingAccountType](#col) when the [operating model](#term) [includes multiple billing account types](#omc).
  * [CostAndUsage](#ds) MUST include [BillingCurrency](#col).
  * [CostAndUsage](#ds) MUST include [BillingPeriodEnd](#col).
  * [CostAndUsage](#ds) MUST include [BillingPeriodStart](#col).
  * [CostAndUsage](#ds) MUST include [CapacityReservationId](#col) when the [operating model](#term) [includes capacity reservations](#omc).
  * [CostAndUsage](#ds) MUST include [CapacityReservationStatus](#col) when the [operating model](#term) includes capacity reservations.
  * [CostAndUsage](#ds) MUST include [ChargeCategory](#col).
  * [CostAndUsage](#ds) MUST include [ChargeClass](#col).
  * [CostAndUsage](#ds) MUST include [ChargeDescription](#col).
  * [CostAndUsage](#ds) SHOULD include [ChargeFrequency](#col).
  * [CostAndUsage](#ds) MUST include [ChargePeriodEnd](#col).
  * [CostAndUsage](#ds) MUST include [ChargePeriodStart](#col).
  * [CostAndUsage](#ds) MUST include [CommitmentDiscountCategory](#col) when the [operating model](#term) [includes commitment discounts](#omc).
  * [CostAndUsage](#ds) MUST include [CommitmentDiscountId](#col) when the [operating model](#term) includes commitment discounts.
  * [CostAndUsage](#ds) MUST include [CommitmentDiscountName](#col) when the [operating model](#term) includes commitment discounts.
  * [CostAndUsage](#ds) MUST include [CommitmentDiscountQuantity](#col) when the [operating model](#term) includes commitment discounts.
  * [CostAndUsage](#ds) MUST include [CommitmentDiscountStatus](#col) when the [operating model](#term) includes commitment discounts.
  * [CostAndUsage](#ds) MUST include [CommitmentDiscountType](#col) when the [operating model](#term) includes commitment discounts.
  * [CostAndUsage](#ds) MUST include [CommitmentDiscountUnit](#col) when the [operating model](#term) includes commitment discounts.
  * [CostAndUsage](#ds) MUST include [CommitmentProgramEligibilityDetails](#col) when the [operating model](#term) [includes commitment programs](#omc).
  * [CostAndUsage](#ds) MUST include [ConsumedQuantity](#col) when the [operating model](#term) [includes usage measurement](#omc).
  * [CostAndUsage](#ds) MUST include [ConsumedUnit](#col) when the [operating model](#term) includes usage measurement.
  * [CostAndUsage](#ds) MUST include [ContractApplied](#col) when the [operating model](#term) [includes contract commitments](#omc).
  * [CostAndUsage](#ds) MUST include [ContractedCost](#col).
  * [CostAndUsage](#ds) MUST include [ContractedUnitPrice](#col) when the [operating model](#term) [includes unit pricing](#omc).
  * [CostAndUsage](#ds) MUST include [CredentialId](#col) when the [operating model](#term) [includes requester attribution](#omc).
  * [CostAndUsage](#ds) MUST include [EffectiveCost](#col).
  * [CostAndUsage](#ds) MUST include [HostProviderName](#col).
  * [CostAndUsage](#ds) MUST include [InvoiceDetailId](#col) when the [operating model](#term) [includes payable invoices](#omc).
  * [CostAndUsage](#ds) MUST include [InvoiceId](#col) when the [operating model](#term) includes payable invoices.
  * [CostAndUsage](#ds) MUST include [InvoiceIssuerName](#col).
  * [CostAndUsage](#ds) MUST include [ListCost](#col).
  * [CostAndUsage](#ds) MUST include [ListUnitPrice](#col) when the [operating model](#term) includes unit pricing.
  * [CostAndUsage](#ds) MUST include [PricingCategory](#col) when the [operating model](#term) [includes multiple pricing categories](#omc).
  * [CostAndUsage](#ds) MUST include [PricingCurrency](#col) when the [operating model](#term) [includes pricing and billing currency differences](#omc:IncludesPricingBillingCurrencyDifferences).
  * [CostAndUsage](#ds) MUST adhere to the following [PricingCurrencyContractedUnitPrice](#col) requirements:
    * [CostAndUsage](#ds) MUST include [PricingCurrencyContractedUnitPrice](#col) when the [operating model](#term) [includes consumption currency](#omc) and includes unit pricing.
    * [CostAndUsage](#ds) SHOULD include [PricingCurrencyContractedUnitPrice](#col) when the [operating model](#term) includes pricing and billing currency differences and includes unit pricing.
    * [CostAndUsage](#ds) MAY include [PricingCurrencyContractedUnitPrice](#col) in all other cases.
  * [CostAndUsage](#ds) MUST adhere to the following [PricingCurrencyEffectiveCost](#col) requirements:
    * [CostAndUsage](#ds) MUST include [PricingCurrencyEffectiveCost](#col) when the [operating model](#term) includes consumption currency.
    * [CostAndUsage](#ds) SHOULD include [PricingCurrencyEffectiveCost](#col) when the [operating model](#term) includes pricing and billing currency differences.
    * [CostAndUsage](#ds) MAY include [PricingCurrencyEffectiveCost](#col) in all other cases.
  * [CostAndUsage](#ds) MUST adhere to the following [PricingCurrencyListUnitPrice](#col) requirements:
    * [CostAndUsage](#ds) MUST include [PricingCurrencyListUnitPrice](#col) when the [operating model](#term) includes consumption currency and includes unit pricing.
    * [CostAndUsage](#ds) SHOULD include [PricingCurrencyListUnitPrice](#col) when the [operating model](#term) includes pricing and billing currency differences and includes unit pricing.
    * [CostAndUsage](#ds) MAY include [PricingCurrencyListUnitPrice](#col) in all other cases.
  * [CostAndUsage](#ds) MUST include [PricingQuantity](#col).
  * [CostAndUsage](#ds) MUST include [PricingUnit](#col).
  * [CostAndUsage](#ds) MUST include [PrincipalId](#col) when the [operating model](#term) includes requester attribution.
  * [CostAndUsage](#ds) MUST include [RegionId](#col) when the [operating model](#term) [includes regions](#omc).
  * [CostAndUsage](#ds) MUST include [RegionName](#col) when the [operating model](#term) includes regions.
  * [CostAndUsage](#ds) MUST include [RequesterDetails](#col) when the [operating model](#term) includes requester attribution.
  * [CostAndUsage](#ds) MUST include [ResourceId](#col) when the [operating model](#term) [includes provisioned resources](#omc).
  * [CostAndUsage](#ds) MUST include [ResourceName](#col) when the [operating model](#term) includes provisioned resources.
  * [CostAndUsage](#ds) MUST include [ResourceType](#col) when the [operating model](#term) includes provisioned resources and [includes resource type assignment](#omc).
  * [CostAndUsage](#ds) MUST include [ServiceCategory](#col).
  * [CostAndUsage](#ds) MUST include [ServiceName](#col).
  * [CostAndUsage](#ds) MUST include [ServiceProviderName](#col).
  * [CostAndUsage](#ds) SHOULD include [ServiceSubcategory](#col).
  * [CostAndUsage](#ds) MUST include [SkuId](#col) when the [operating model](#term) includes unit pricing.
  * [CostAndUsage](#ds) MUST include [SkuMeter](#col) when the [operating model](#term) includes unit pricing.
  * [CostAndUsage](#ds) MUST include [SkuPriceDetails](#col) when the [operating model](#term) includes unit pricing.
  * [CostAndUsage](#ds) MUST include [SkuPriceId](#col) when the [operating model](#term) includes unit pricing.
  * [CostAndUsage](#ds) MUST include [SubAccountId](#col) when the [operating model](#term) [includes sub accounts](#omc).
  * [CostAndUsage](#ds) MUST include [SubAccountName](#col) when the [operating model](#term) includes sub accounts.
  * [CostAndUsage](#ds) MUST include [SubAccountType](#col) when the [operating model](#term) [includes multiple sub account types](#omc).
  * [CostAndUsage](#ds) MUST include [Tags](#col) when the [operating model](#term) [includes tags](#omc).
  * [CostAndUsage](#ds) SHOULD include [custom columns](#term) needed to identify all applied discounts when [FOCUS columns](#term) are not sufficient.
* [CostAndUsage](#ds) MUST conform to [CorrectionHandling](#attr) requirements.
* [CostAndUsage](#ds) MUST conform to [DatasetCompleteness](#attr) requirements.
* [CostAndUsage](#ds) MUST conform to [DatasetConfiguration](#attr) requirements.
* [CostAndUsage](#ds) MUST conform to [DeliveryHandling](#attr) requirements.
* [CostAndUsage](#ds) MUST include [charges](#term) representing unused portions of a [commitment](#term) when the [commitment](#term) is not fully utilized.
* [CostAndUsage](#ds) MUST include separate [charges](#term) representing discounted and non-discounted portions when a discount applies to only a portion of the originally incurred [charge](#term).
* When the [operating model](#term) includes split cost allocation, [CostAndUsage](#ds) MUST adhere to the following requirements:
  * [CostAndUsage](#ds) MUST have its split cost allocation method documented and accessible to practitioners.
  * [CostAndUsage](#ds) SHOULD offer split cost allocation on an opt-in basis.
  * [CostAndUsage](#ds) MAY contain records for concepts not related to resource usage, when it aligns with the documented split cost allocation method.
  * [CostAndUsage](#ds) MAY contain records for unused or unallocated usage from the [origin charge](#term) as separate [allocated charges](#term), when it aligns with the documented split cost allocation method.
  * [CostAndUsage](#ds) MAY contain [allocated charges](#term) with apportioned costs for unused or unallocated usage, when it aligns with the documented split cost allocation method.
* [CostAndUsage](#ds) SHOULD reflect all applied discounts in [charges](#term) they pertain to.
* [CostAndUsage](#ds) SHOULD NOT represent applied discounts as separate negating or offsetting [charges](#term).
* [CostAndUsage](#ds) [FOCUS columns](#term) MUST conform to [DataGeneratorCalculatedSplitCostAllocationHandling](#attr) requirements when the [operating model](#term) includes split cost allocation.
* [CostAndUsage](#ds) [FOCUS columns](#term) MUST conform to [FocusColumnHandling](#attr) requirements.
* [CostAndUsage](#ds) [FOCUS columns](#term) MUST conform to [NullHandling](#attr) requirements.
* [CostAndUsage](#ds) [custom columns](#term) MUST conform to [CustomColumnHandling](#attr) requirements.
* When the [operating model](#term) includes requester attribution, [CostAndUsage](#ds) documentation MUST adhere to the following requirements:
  * [CostAndUsage](#ds) documentation MUST include the use cases in which [CredentialId](#col) is not null.
  * [CostAndUsage](#ds) documentation MUST include the use cases in which [PrincipalId](#col) is not null.
  * [CostAndUsage](#ds) documentation MUST include the use cases in which [RequesterDetails](#col) is not null.

## Dataset ID<!--SkipTOC-->

CostAndUsage

## Display Name<!--SkipTOC-->

Cost and Usage

## Description<!--SkipTOC-->

Describes the cost and usage incurred through using or purchasing a service provider's [resources](#term) or [services](#term).

## Version Introduced<!--SkipTOC-->

0.5
