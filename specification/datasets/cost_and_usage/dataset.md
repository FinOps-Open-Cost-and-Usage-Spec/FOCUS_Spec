# Cost and Usage

The Cost and Usage dataset is the primary dataset for FOCUS cost and usage data.

The specification for the Cost and Usage dataset defines a group of columns that provide qualitative values (such as dates, resource, and provider information) categorized as "dimensions" and quantitative values (numeric values) categorized as "metrics" that can be used for performing various [FinOps capabilities][FODOFC]. Metrics are commonly used for aggregations (sum, multiplication, averaging etc.) and statistical operations within the dataset. Dimensions are commonly used to categorize, filter, and reveal details in your data when combined with metrics. The columns are presented in alphabetical order.

<div class='h4-nonindex'>Columns</div>

| Column                                                                        | Column Type | Feature Level | Allows Nulls | Data Type |
| ----------------------------------------------------------------------------- | ----------- | ------------- | ------------ | --------- |
| [Availability Zone](#availabilityzone)                                        | Dimension   | Recommended   | True         | String    |
| [Billed Cost](#billedcost)                                                    | Metric      | Mandatory     | False        | Decimal   |
| [Billing Account ID](#billingaccountid)                                       | Dimension   | Mandatory     | False        | String    |
| [Billing Account Name](#billingaccountname)                                   | Dimension   | Mandatory     | True         | String    |
| [Billing Account Type](#billingaccounttype)                                   | Dimension   | Conditional   | False        | String    |
| [Billing Currency](#billingcurrency)                                          | Dimension   | Mandatory     | False        | String    |
| [Billing Period End](#billingperiodend)                                       | Dimension   | Mandatory     | False        | Date/Time |
| [Billing Period Start](#billingperiodstart)                                   | Dimension   | Mandatory     | False        | Date/Time |
| [Capacity Reservation ID](#capacityreservationid)                             | Dimension   | Conditional   | True         | String    |
| [Capacity Reservation Status](#capacityreservationstatus)                     | Dimension   | Conditional   | True         | String    |
| [Charge Category](#chargecategory)                                            | Dimension   | Mandatory     | False        | String    |
| [Charge Class](#chargeclass)                                                  | Dimension   | Mandatory     | True         | String    |
| [Charge Description](#chargedescription)                                      | Dimension   | Mandatory     | True         | String    |
| [Charge Frequency](#chargefrequency)                                          | Dimension   | Recommended   | False        | String    |
| [Charge Period End](#chargeperiodend)                                         | Dimension   | Mandatory     | False        | Date/Time |
| [Charge Period Start](#chargeperiodstart)                                     | Dimension   | Mandatory     | False        | Date/Time |
| [Commitment Discount Category](#commitmentdiscountcategory)                   | Dimension   | Conditional   | True         | String    |
| [Commitment Discount ID](#commitmentdiscountid)                               | Dimension   | Conditional   | True         | String    |
| [Commitment Discount Name](#commitmentdiscountname)                           | Dimension   | Conditional   | True         | String    |
| [Commitment Discount Quantity](#commitmentdiscountquantity)                   | Metric      | Conditional   | True         | Decimal   |
| [Commitment Discount Status](#commitmentdiscountstatus)                       | Dimension   | Conditional   | True         | String    |
| [Commitment Discount Type](#commitmentdiscounttype)                           | Dimension   | Conditional   | True         | String    |
| [Commitment Discount Unit](#commitmentdiscountunit)                           | Dimension   | Conditional   | True         | String    |
| [Consumed Quantity](#consumedquantity)                                        | Metric      | Conditional   | True         | Decimal   |
| [Consumed Unit](#consumedunit)                                                | Dimension   | Conditional   | True         | String    |
| [Contracted Cost](#contractedcost)                                            | Metric      | Mandatory     | False        | Decimal   |
| [Contracted Unit Price](#contractedunitprice)                                 | Metric      | Conditional   | True         | Decimal   |
| [Effective Cost](#effectivecost)                                              | Metric      | Mandatory     | False        | Decimal   |
| [Invoice ID](#invoiceid)                                                      | Dimension   | Recommended   | True         | String    |
| [Invoice Issuer](#invoiceissuername)                                          | Dimension   | Mandatory     | False        | String    |
| [List Cost](#listcost)                                                        | Metric      | Mandatory     | False        | Decimal   |
| [List Unit Price](#listunitprice)                                             | Metric      | Conditional   | True         | Decimal   |
| [Pricing Category](#pricingcategory)                                          | Dimension   | Conditional   | True         | String    |
| [Pricing Currency Contracted Unit Price](#pricingcurrencycontractedunitprice) | Metric      | Conditional   | True         | Decimal   |
| [Pricing Currency Effective Cost](#pricingcurrencyeffectivecost)              | Metric      | Conditional   | True         | Decimal   |
| [Pricing Currency List Unit Price](#pricingcurrencylistunitprice)             | Metric      | Conditional   | True         | Decimal   |
| [Pricing Currency](#pricingcurrency)                                          | Dimension   | Conditional   | True         | String    |
| [Pricing Quantity](#pricingquantity)                                          | Metric      | Mandatory     | True         | Decimal   |
| [Pricing Unit](#pricingunit)                                                  | Dimension   | Mandatory     | True         | String    |
| [Provider](#providername)                                                     | Dimension   | Mandatory     | False        | String    |
| [Publisher](#publishername)                                                   | Dimension   | Mandatory     | False        | String    |
| [Region ID](#regionid)                                                        | Dimension   | Conditional   | True         | String    |
| [Region Name](#regionname)                                                    | Dimension   | Conditional   | True         | String    |
| [Resource ID](#resourceid)                                                    | Dimension   | Conditional   | True         | String    |
| [Resource Name](#resourcename)                                                | Dimension   | Conditional   | True         | String    |
| [Resource Type](#resourcetype)                                                | Dimension   | Conditional   | True         | String    |
| [Service Category](#servicecategory)                                          | Dimension   | Mandatory     | False        | String    |
| [Service Name](#servicename)                                                  | Dimension   | Mandatory     | False        | String    |
| [Service Subcategory](#servicesubcategory)                                    | Dimension   | Recommended   | False        | String    |
| [SKU ID](#skuid)                                                              | Dimension   | Conditional   | True         | String    |
| [SKU Meter](#skumeter)                                                        | Dimension   | Conditional   | True         | String    |
| [SKU Price Details](#skupricedetails)                                         | Dimension   | Conditional   | True         | JSON      |
| [SKU Price ID](#skupriceid)                                                   | Dimension   | Conditional   | True         | String    |
| [Sub Account ID](#subaccountid)                                               | Dimension   | Conditional   | True         | String    |
| [Sub Account Name](#subaccountname)                                           | Dimension   | Conditional   | True         | String    |
| [Sub Account Type](#subaccounttype)                                           | Dimension   | Conditional   | True         | String    |
| [Tags](#tags)                                                                 | Dimension   | Conditional   | True         | JSON      |

<div class='h4-nonindex'>Relationships</div>

None

<div class='h4-nonindex'>Requirements</div>

The CostAndUsage dataset adheres to the following requirements:

* CostAndUsage MUST conform to [ColumnHandling](#columnhandling) requirements.
* CostAndUsage MUST conform to [DiscountHandling](#discounthandling) requirements.
* CostAndUsage MUST conform to [NullHandling](#nullhandling) requirements.

<div class='h4-nonindex'>Dataset ID</div>

CostAndUsage

<div class='h4-nonindex'>Display Name</div>

Cost and Usage

<div class='h4-nonindex'>Description</div>

Describes the cost and usage incurred through using or purchasing a provider's [*resources*](#glossary:resource) or [*services*](#glossary:service).

<div class='h4-nonindex'>Introduced (version)</div>

0.5
