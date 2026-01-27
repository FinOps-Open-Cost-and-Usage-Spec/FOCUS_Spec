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
* CostAndUsage MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.

## Dataset ID<!--SkipTOC-->

CostAndUsage

## Display Name<!--SkipTOC-->

Cost and Usage

## Description<!--SkipTOC-->

Describes the cost and usage incurred through using or purchasing a service provider's [*resources*](#glossary:resource) or [*services*](#glossary:service).

## Introduced (version)<!--SkipTOC-->

0.5
