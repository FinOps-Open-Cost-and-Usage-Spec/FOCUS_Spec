# Cost and Usage

The Cost and Usage dataset is the primary dataset for FOCUS cost and usage data.

The specification for the Cost and Usage dataset defines a group of columns that provide qualitative values (such as dates, resource, and service provider information) categorized as "dimensions" and quantitative values (numeric values) categorized as "metrics" that can be used for performing various [FinOps capabilities][FODOFC]. Metrics are commonly used for aggregations (sum, multiplication, averaging etc.) and statistical operations within the dataset. Dimensions are commonly used to categorize, filter, and reveal details in your data when combined with metrics. The columns are presented in alphabetical order.

## Columns<!--SkipTOC-->

| Column                                                                        | Column Type        | Feature Level | Allows Nulls | Data Type |
| ----------------------------------------------------------------------------- | ------------------ | ------------- | ------------ | --------- |
| [Allocated Method Details](#datasets.costandusage.allocatedmethoddetails)                           | Dimension          | Recommended   | True         | JSON      |
| [Allocated Method ID](#datasets.costandusage.allocatedmethodid)                                     | Dimension          | Conditional   | True         | String    |
| [Allocated Resource ID](#datasets.costandusage.allocatedresourceid)                                 | Dimension          | Conditional   | True         | String    |
| [Allocated Resource Name](#datasets.costandusage.allocatedresourcename)                             | Dimension          | Conditional   | True         | String    |
| [Allocated Tags](#datasets.costandusage.allocatedtags)                                              | Dimension          | Conditional   | True         | JSON      |
| [Availability Zone](#datasets.costandusage.availabilityzone)                                        | Dimension          | Recommended   | True         | String    |
| [Billed Cost](#datasets.costandusage.billedcost)                                                    | Metric             | Mandatory     | False        | Decimal   |
| [Billing Account ID](#datasets.costandusage.billingaccountid)                                       | Dimension          | Mandatory     | False        | String    |
| [Billing Account Name](#datasets.costandusage.billingaccountname)                                   | Dimension          | Mandatory     | True         | String    |
| [Billing Account Type](#datasets.costandusage.billingaccounttype)                                   | Dimension          | Conditional   | False        | String    |
| [Billing Currency](#datasets.costandusage.billingcurrency)                                          | Dimension          | Mandatory     | False        | String    |
| [Billing Period End](#datasets.costandusage.billingperiodend)                                       | Dimension          | Mandatory     | False        | Date/Time |
| [Billing Period Start](#datasets.costandusage.billingperiodstart)                                   | Dimension          | Mandatory     | False        | Date/Time |
| [Capacity Reservation ID](#datasets.costandusage.capacityreservationid)                             | Dimension          | Conditional   | True         | String    |
| [Capacity Reservation Status](#datasets.costandusage.capacityreservationstatus)                     | Dimension          | Conditional   | True         | String    |
| [Charge Category](#datasets.costandusage.chargecategory)                                            | Dimension          | Mandatory     | False        | String    |
| [Charge Class](#datasets.costandusage.chargeclass)                                                  | Dimension          | Mandatory     | True         | String    |
| [Charge Description](#datasets.costandusage.chargedescription)                                      | Dimension          | Mandatory     | True         | String    |
| [Charge Frequency](#datasets.costandusage.chargefrequency)                                          | Dimension          | Recommended   | False        | String    |
| [Charge Period End](#datasets.costandusage.chargeperiodend)                                         | Dimension          | Mandatory     | False        | Date/Time |
| [Charge Period Start](#datasets.costandusage.chargeperiodstart)                                     | Dimension          | Mandatory     | False        | Date/Time |
| [Commitment Discount Category](#datasets.costandusage.commitmentdiscountcategory)                   | Dimension          | Conditional   | True         | String    |
| [Commitment Discount ID](#datasets.costandusage.commitmentdiscountid)                               | Dimension          | Conditional   | True         | String    |
| [Commitment Discount Name](#datasets.costandusage.commitmentdiscountname)                           | Dimension          | Conditional   | True         | String    |
| [Commitment Discount Quantity](#datasets.costandusage.commitmentdiscountquantity)                   | Metric             | Conditional   | True         | Decimal   |
| [Commitment Discount Status](#datasets.costandusage.commitmentdiscountstatus)                       | Dimension          | Conditional   | True         | String    |
| [Commitment Discount Type](#datasets.costandusage.commitmentdiscounttype)                           | Dimension          | Conditional   | True         | String    |
| [Commitment Discount Unit](#datasets.costandusage.commitmentdiscountunit)                           | Dimension          | Conditional   | True         | String    |
| [Consumed Quantity](#datasets.costandusage.consumedquantity)                                        | Metric             | Conditional   | True         | Decimal   |
| [Consumed Unit](#datasets.costandusage.consumedunit)                                                | Dimension          | Conditional   | True         | String    |
| [Contract Applied](#datasets.costandusage.contractapplied)                                          | Dimension / Metric | Conditional   | True         | JSON      |
| [Contracted Cost](#datasets.costandusage.contractedcost)                                            | Metric             | Mandatory     | False        | Decimal   |
| [Contracted Unit Price](#datasets.costandusage.contractedunitprice)                                 | Metric             | Conditional   | True         | Decimal   |
| [Effective Cost](#datasets.costandusage.effectivecost)                                              | Metric             | Mandatory     | False        | Decimal   |
| [Host Provider Name](#datasets.costandusage.hostprovidername)                                       | Dimension          | Mandatory     | False        | String    |
| [Invoice ID](#datasets.costandusage.invoiceid)                                                      | Dimension          | Recommended   | True         | String    |
| [Invoice Issuer Name](#datasets.costandusage.invoiceissuername)                                     | Dimension          | Mandatory     | False        | String    |
| [List Cost](#datasets.costandusage.listcost)                                                        | Metric             | Mandatory     | False        | Decimal   |
| [List Unit Price](#datasets.costandusage.listunitprice)                                             | Metric             | Conditional   | True         | Decimal   |
| [Pricing Category](#datasets.costandusage.pricingcategory)                                          | Dimension          | Conditional   | True         | String    |
| [Pricing Currency](#datasets.costandusage.pricingcurrency)                                          | Dimension          | Conditional   | True         | String    |
| [Pricing Currency Contracted Unit Price](#datasets.costandusage.pricingcurrencycontractedunitprice) | Metric             | Conditional   | True         | Decimal   |
| [Pricing Currency Effective Cost](#datasets.costandusage.pricingcurrencyeffectivecost)              | Metric             | Conditional   | True         | Decimal   |
| [Pricing Currency List Unit Price](#datasets.costandusage.pricingcurrencylistunitprice)             | Metric             | Conditional   | True         | Decimal   |
| [Pricing Quantity](#datasets.costandusage.pricingquantity)                                          | Metric             | Mandatory     | True         | Decimal   |
| [Pricing Unit](#datasets.costandusage.pricingunit)                                                  | Dimension          | Mandatory     | True         | String    |
| [Provider - DEPRECATED](#datasets.costandusage.provider-deprecated)                                        | Dimension          | Mandatory     | False        | String    |
| [Publisher - DEPRECATED](#datasets.costandusage.publisher-deprecated)                                      | Dimension          | Mandatory     | False        | String    |
| [Region ID](#datasets.costandusage.regionid)                                                        | Dimension          | Conditional   | True         | String    |
| [Region Name](#datasets.costandusage.regionname)                                                    | Dimension          | Conditional   | True         | String    |
| [Resource ID](#datasets.costandusage.resourceid)                                                    | Dimension          | Conditional   | True         | String    |
| [Resource Name](#datasets.costandusage.resourcename)                                                | Dimension          | Conditional   | True         | String    |
| [Resource Type](#datasets.costandusage.resourcetype)                                                | Dimension          | Conditional   | True         | String    |
| [Service Category](#datasets.costandusage.servicecategory)                                          | Dimension          | Mandatory     | False        | String    |
| [Service Name](#datasets.costandusage.servicename)                                                  | Dimension          | Mandatory     | False        | String    |
| [Service Provider Name](#datasets.costandusage.serviceprovidername)                                 | Dimension          | Mandatory     | False        | String    |
| [Service Subcategory](#datasets.costandusage.servicesubcategory)                                    | Dimension          | Recommended   | False        | String    |
| [SKU ID](#datasets.costandusage.skuid)                                                              | Dimension          | Conditional   | True         | String    |
| [SKU Meter](#datasets.costandusage.skumeter)                                                        | Dimension          | Conditional   | True         | String    |
| [SKU Price Details](#datasets.costandusage.skupricedetails)                                         | Dimension          | Conditional   | True         | JSON      |
| [SKU Price ID](#datasets.costandusage.skupriceid)                                                   | Dimension          | Conditional   | True         | String    |
| [Sub Account ID](#datasets.costandusage.subaccountid)                                               | Dimension          | Conditional   | True         | String    |
| [Sub Account Name](#datasets.costandusage.subaccountname)                                           | Dimension          | Conditional   | True         | String    |
| [Sub Account Type](#datasets.costandusage.subaccounttype)                                           | Dimension          | Conditional   | True         | String    |
| [Tags](#datasets.costandusage.tags)                                                                 | Dimension          | Conditional   | True         | JSON      |

## Relationships<!--SkipTOC-->

The Cost and Usage dataset can be joined to the Contract Commitment dataset through the use of the Contract Commitment ID.

* In the Cost and Usage dataset, Contract Commitment ID is a property within a JSON object array provided in Contract Applied column.
* In the Contract Commitment dataset, Contract Commitment ID is a column.

| Dataset A           | Dataset A Column  | Dataset B           | Dataset B Column       |
| ------------------- | ----------------- | ------------------- | ---------------------- |
| Cost and Usage      | Contract Applied  | Contract Commitment | Contract Commitment ID |

## Requirements<!--SkipTOC-->

CostAndUsage adheres to the following requirements:

* CostAndUsage MUST be present.
* CostAndUsage MUST conform to [ColumnHandling](#attributes.columnhandling) requirements.
* CostAndUsage MUST conform to [NullHandling](#attributes.nullhandling) requirements.
* CostAndUsage MUST conform to [DiscountHandling](#attributes.discounthandling) requirements.
* CostAndUsage MUST conform to [InvoiceHandling](#attributes.invoicehandling) requirements.
* CostAndUsage MUST conform to [DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling) requirements.
* The schema of the CostAndUsage FOCUS dataset MUST adhere to the following requirements:
  * CostAndUsage FOCUS dataset SHOULD contain the AllocatedMethodDetails column when the data generator supports [Data Generator-Calculated Split Cost Allocation](#datagenerator-calculatedsplitcostallocationhandling).
  * CostAndUsage FOCUS dataset MUST contain the AllocatedMethodId column when the data generator supports [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling).
  * CostAndUsage FOCUS dataset MUST contain the AllocatedResourceId column when the data generator supports [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling).
  * CostAndUsage FOCUS dataset MUST contain the AllocatedResourceName column when the data generator supports [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling).
  * CostAndUsage FOCUS dataset MUST contain the AllocatedTags column when the service provider supports [Data Generator-Calculated Split Cost Allocation](#datagenerator-calculatedsplitcostallocationhandling).
  * CostAndUsage FOCUS dataset SHOULD contain the AvailabilityZone column when the host provider supports deploying resources or services within an *availability zone*.
  * CostAndUsage FOCUS dataset MUST contain the BilledCost column.
  * CostAndUsage FOCUS dataset MUST contain the BillingAccountId column.
  * CostAndUsage FOCUS dataset MUST contain the BillingAccountName column.
  * CostAndUsage FOCUS dataset MUST contain the BillingAccountType column when the invoice issuer supports more than one possible BillingAccountType value.
  * CostAndUsage FOCUS dataset MUST contain the BillingCurrency column.
  * CostAndUsage FOCUS dataset MUST contain the BillingPeriodEnd column.
  * CostAndUsage FOCUS dataset MUST contain the BillingPeriodStart column.
  * CostAndUsage FOCUS dataset MUST contain the CapacityReservationId column when the service provider supports *capacity reservations*.
  * CostAndUsage FOCUS dataset MUST contain the CapacityReservationStatus column when the service provider supports *capacity reservations*.
  * CostAndUsage FOCUS dataset MUST contain the ChargeCategory column.
  * CostAndUsage FOCUS dataset MUST contain the ChargeClass column.
  * CostAndUsage FOCUS dataset MUST contain the ChargeDescription column.
  * CostAndUsage FOCUS dataset SHOULD contain the ChargeFrequency column.
  * CostAndUsage FOCUS dataset MUST contain the ChargePeriodEnd column.
  * CostAndUsage FOCUS dataset MUST contain the ChargePeriodStart column.
  * CostAndUsage FOCUS dataset MUST contain the CommitmentDiscountCategory column when the service provider supports *commitment discounts*.
  * CostAndUsage FOCUS dataset MUST contain the CommitmentDiscountId column when the service provider supports *commitment discounts*.
  * CostAndUsage FOCUS dataset MUST contain the CommitmentDiscountName column when the service provider supports *commitment discounts*.
  * CostAndUsage FOCUS dataset MUST contain the CommitmentDiscountQuantity column when the service provider supports *commitment discounts*.
  * CostAndUsage FOCUS dataset MUST contain the CommitmentDiscountStatus column when the service provider supports *commitment discounts*.
  * CostAndUsage FOCUS dataset MUST contain the CommitmentDiscountType column when the service provider supports *commitment discounts*.
  * CostAndUsage FOCUS dataset MUST contain the CommitmentDiscountUnit column when the service provider supports *commitment discounts*.
  * CostAndUsage FOCUS dataset MUST contain the ConsumedQuantity column when the service provider supports the measurement of usage.
  * CostAndUsage FOCUS dataset MUST contain the ConsumedUnit column when the service provider supports the measurement of usage.
  * CostAndUsage FOCUS dataset MUST contain the ContractApplied column when the service provider supports *contract commitments*.
  * CostAndUsage FOCUS dataset MUST contain the ContractedCost column.
  * CostAndUsage FOCUS dataset MUST contain the ContractedUnitPrice column when the service provider supports negotiated pricing concepts.
  * CostAndUsage FOCUS dataset MUST contain the EffectiveCost column.
  * CostAndUsage FOCUS dataset MUST contain the HostProviderName column.
  * CostAndUsage FOCUS dataset SHOULD contain the InvoiceId column.
  * CostAndUsage FOCUS dataset MUST contain the InvoiceIssuerName column.
  * CostAndUsage FOCUS dataset MUST contain the ListCost column.
  * CostAndUsage FOCUS dataset MUST contain the ListUnitPrice column when the service provider publishes unit prices exclusive of discounts.
  * CostAndUsage FOCUS dataset MUST contain the PricingCategory column when the service provider supports more than one pricing category across all [*SKUs*](#glossary:sku).
  * CostAndUsage FOCUS dataset MUST contain the PricingCurrency column when the service provider supports pricing and billing in different currencies.
  * CostAndUsage FOCUS dataset MUST contain the PricingCurrencyContractedUnitPrice column when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
  * CostAndUsage FOCUS dataset MUST contain the PricingCurrencyEffectiveCost column when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
  * CostAndUsage FOCUS dataset MUST contain the PricingCurrencyListUnitPrice column when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
  * CostAndUsage FOCUS dataset MUST contain the PricingQuantity column.
  * CostAndUsage FOCUS dataset MUST contain the PricingUnit column.
  * CostAndUsage FOCUS dataset MUST contain the ProviderName column.
  * CostAndUsage FOCUS dataset MUST contain the PublisherName column.
  * CostAndUsage FOCUS dataset MUST contain the RegionId column when the host provider supports deploying resources or services within a region.
  * CostAndUsage FOCUS dataset MUST contain the RegionName column when the host provider supports deploying resources or services within a region.
  * CostAndUsage FOCUS dataset MUST contain the ResourceId column when the service provider supports billing based on provisioned *resources*.
  * CostAndUsage FOCUS dataset MUST contain the ResourceName column when the service provider supports billing based on provisioned resources.
  * CostAndUsage FOCUS dataset MUST contain the ResourceType column when the service provider supports billing based on provisioned *resources* and supports assigning types to *resources*.
  * CostAndUsage FOCUS dataset MUST contain the ServiceCategory column.
  * CostAndUsage FOCUS dataset MUST contain the ServiceName column.
  * CostAndUsage FOCUS dataset MUST contain the ServiceProviderName column.
  * CostAndUsage FOCUS dataset SHOULD contain the ServiceSubcategory column.
  * CostAndUsage FOCUS dataset MUST contain the SkuId column when the service provider supports unit pricing concepts and publishes price lists, publicly or as part of contracting.
  * CostAndUsage FOCUS dataset MUST contain the SkuMeter column when the service provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.
  * CostAndUsage FOCUS dataset MUST contain the SkuPriceDetails column when the service provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.
  * CostAndUsage FOCUS dataset MUST contain the SkuPriceId column when the service provider supports unit pricing concepts and publishes *price lists*, publicly or as part of contracting.
  * CostAndUsage FOCUS dataset MUST contain the SubAccountId column when the service provider supports a *sub account* construct.
  * CostAndUsage FOCUS dataset MUST contain the SubAccountName column when the service provider supports a *sub account* construct.
  * CostAndUsage FOCUS dataset MUST contain the SubAccountType column when the service provider supports more than one possible SubAccountType value.
  * CostAndUsage FOCUS dataset MUST contain the Tags column when the data generator supports setting user or provider-defined tags.

## Dataset ID<!--SkipTOC-->

CostAndUsage

## Display Name<!--SkipTOC-->

Cost and Usage

## Description<!--SkipTOC-->

Describes the cost and usage incurred through using or purchasing a service provider's [*resources*](#glossary:resource) or [*services*](#glossary:service).

## Introduced (version)<!--SkipTOC-->

0.5
