# Cost and Usage

The Cost and Usage dataset is the primary dataset for FOCUS cost and usage data.

The specification for the Cost and Usage dataset defines a group of columns that provide qualitative values (such as dates, resource, and provider information) categorized as "dimensions" and quantitative values (numeric values) categorized as "metrics" that can be used for performing various [FinOps capabilities][FODOFC]. Metrics are commonly used for aggregations (sum, multiplication, averaging etc.) and statistical operations within the dataset. Dimensions are commonly used to categorize, filter, and reveal details in your data when combined with metrics. The columns are presented in alphabetical order.

<div class='h4-nonindex'>Columns</div>

| Column                                                                        | Column Type | Feature Level | Allows Nulls | Data Type | Required |
| ----------------------------------------------------------------------------- | ----------- | ------------- | ------------ | --------- | -------- |
| [Billed Cost](#billedcost)                                                    | Metric      | Mandatory     | False        | Decimal   | TRUE     |
| [Billing Account ID](#billingaccountid)                                       | Dimension   | Mandatory     | False        | String    | TRUE     |
| [Billing Account Type](#billingaccounttype)                                   | Dimension   | Conditional   | False        | String    | FALSE    |
| [Billing Currency](#billingcurrency)                                          | Dimension   | Mandatory     | False        | String    | TRUE     |
| [Billing Period End](#billingperiodend)                                       | Dimension   | Mandatory     | False        | Date/Time | TRUE     |
| [Billing Period Start](#billingperiodstart)                                   | Dimension   | Mandatory     | False        | Date/Time | TRUE     |
| [Charge Category](#charge category)                                           | Dimension   | Mandatory     | False        | String    | TRUE     |
| [Charge Frequency](#chargefrequency)                                          | Dimension   | Recommended   | False        | String    | TRUE     |
| [Charge Period End](#chargeperiodend)                                         | Dimension   | Mandatory     | False        | Date/Time | TRUE     |
| [Charge Period Start](#chargeperiodstart)                                     | Dimension   | Mandatory     | False        | Date/Time | TRUE     |
| [Contracted Cost](#contractedcost)                                            | Metric      | Mandatory     | False        | Decimal   | TRUE     |
| [Effective Cost](#effectivecost)                                              | Metric      | Mandatory     | False        | Decimal   | TRUE     |
| [Invoice Issuer](#invoiceissuername)                                          | Dimension   | Mandatory     | False        | String    | TRUE     |
| [List Cost](#listcost)                                                        | Metric      | Mandatory     | False        | Decimal   | TRUE     |
| [Provider](#providername)                                                     | Dimension   | Mandatory     | False        | String    | TRUE     |
| [Publisher](#publishername)                                                   | Dimension   | Mandatory     | False        | String    | TRUE     |
| [Service Category](#servicecategory)                                          | Dimension   | Mandatory     | False        | String    | TRUE     |
| [Service Name](#servicename)                                                  | Dimension   | Mandatory     | False        | String    | TRUE     |
| [Service Subcategory](#servicesubcategory)                                    | Dimension   | Recommended   | False        | String    | FALSE    |
| [Availability Zone](#availabilityzone)                                        | Dimension   | Recommended   | True         | String    | FALSE    |
| [Billing Account Name](#billingaccountname)                                   | Dimension   | Mandatory     | True         | String    | TRUE     |
| [Capacity Reservation ID](#capacityreservationid)                             | Dimension   | Conditional   | True         | String    | TRUE     |
| [Capacity Reservation Status](#capacityreservationstatus)                     | Dimension   | Conditional   | True         | String    | TRUE     |
| [Charge Class](#charge class)                                                 | Dimension   | Mandatory     | True         | String    | TRUE     |
| [Charge Description](#chargedescription)                                      | Dimension   | Mandatory     | True         | String    | TRUE     |
| [Commitment Discount Category](#commitmentdiscountcategory)                   | Dimension   | Conditional   | True         | String    | TRUE     |
| [Commitment Discount ID](#commitmentdiscountid)                               | Dimension   | Conditional   | True         | String    | TRUE     |
| [Commitment Discount Name](#commitmentdiscountname)                           | Dimension   | Conditional   | True         | String    | TRUE     |
| [Commitment Discount Quantity](#commitmentdiscountquantity)                   | Metric      | Conditional   | True         | Decimal   | TRUE     |
| [Commitment Discount Status](#commitmentdiscountstatus)                       | Dimension   | Conditional   | True         | String    | FALSE    |
| [Commitment Discount Type](#commitmentdiscounttype)                           | Dimension   | Conditional   | True         | String    | TRUE     |
| [Commitment Discount Unit](#commitmentdiscountunit)                           | Dimension   | Conditional   | True         | String    | TRUE     |
| [Consumed Quantity](#consumedquantity)                                        | Metric      | Conditional   | True         | Decimal   | TRUE     |
| [Consumed Unit](#consumedunit)                                                | Dimension   | Conditional   | True         | String    | TRUE     |
| [Contracted Unit Price](#contractedunitprice)                                 | Metric      | Conditional   | True         | Decimal   | FALSE    |
| [Invoice ID](#invoiceid)                                                      | Dimension   | Recommended   | True         | String    | FALSE    |
| [List Unit Price](#listunitprice)                                             | Metric      | Conditional   | True         | Decimal   | TRUE     |
| [Pricing Category](#pricingcategory)                                          | Dimension   | Conditional   | True         | String    | TRUE     |
| [Pricing Currency](#pricingcurrency)                                          | Dimension   | Conditional   | True         | String    | TRUE     |
| [Pricing Currency Contracted Unit Price](#pricingcurrencycontractedunitprice) | Metric      | Conditional   | True         | Decimal   | TRUE     |
| [Pricing Currency Effective Cost](#pricingcurrencyeffectivecost)              | Metric      | Conditional   | True         | Decimal   | TRUE     |
| [Pricing Currency List Unit Price](#pricingcurrencylistunitprice)             | Metric      | Conditional   | True         | Decimal   | TRUE     |
| [Pricing Quantity](#pricingquantity)                                          | Metric      | Mandatory     | True         | Decimal   | TRUE     |
| [Pricing Unit](#pricingunit)                                                  | Dimension   | Mandatory     | True         | String    | TRUE     |
| [Region ID](#regionid)                                                        | Dimension   | Conditional   | True         | String    | TRUE     |
| [Region Name](#regionname)                                                    | Dimension   | Conditional   | True         | String    | FALSE    |
| [Resource ID](#resourceid)                                                    | Dimension   | Conditional   | True         | String    | TRUE     |
| [Resource Name](#resourcename)                                                | Dimension   | Conditional   | True         | String    | TRUE     |
| [Resource Type](#resourcetype)                                                | Dimension   | Conditional   | True         | String    | TRUE     |
| [SKU ID](#skuid)                                                              | Dimension   | Conditional   | True         | String    | TRUE     |
| [SKU Meter](#skumeter)                                                        | Dimension   | Conditional   | True         | String    | TRUE     |
| [SKU Price Details](#skupricedetails)                                         | Dimension   | Conditional   | True         | JSON      | TRUE     |
| [SKU Price ID](#skupriceid)                                                   | Dimension   | Conditional   | True         | String    | TRUE     |
| [Sub Account ID](#subaccountid)                                               | Dimension   | Conditional   | True         | String    | TRUE     |
| [Sub Account Name](#subaccountname)                                           | Dimension   | Conditional   | True         | String    | TRUE     |
| [Sub Account Type](#subaccounttype)                                           | Dimension   | Conditional   | True         | String    | TRUE     |
| [Tags](#tags)                                                                 | Dimension   | Conditional   | True         | JSON      | TRUE     |

<div class='h4-nonindex'>Relationships</div>

The Cost and Usage dataset can be joined to the Contract Commitment dataset through the use of the Contract Commitment ID field.

| Dataset A           | Dataset A Column       | Dataset B           | Dataset B Column       |
| ------------------- | ---------------------- | ------------------- | ---------------------- |
| Cost and Usage      | Contract Commitment ID | Contract Commitment | Contract Commitment ID |

<div class='h4-nonindex'>Requirements</div>

The CostAndUsage dataset adheres to the following requirements:

* CostAndUsage MUST be present.
* CostAndUsage MUST conform to [ColumnHandling](#columnhandling) requirements.
* CostAndUsage MUST conform to [CurrencyFormat](#currencyformat) requirements.
* CostAndUsage MUST conform to [DateTimeFormat](#datetimeformat) requirements.
* CostAndUsage MUST conform to [DiscountHandling](#discounthandling) requirements.
* CostAndUsage MUST conform to [KeyValueFormat](#keyvalueformat) requirements.
* CostAndUsage MUST conform to [NullHandling](#nullhandling) requirements.
* CostAndUsage MUST conform to [NumericFormat](#numericformat) requirements.
* CostAndUsage MUST conform to [StringHandling](#stringhandling) requirements.
* CostAndUsage MUST conform to [UnitFormat](#unitformat) requirements.

<div class='h4-nonindex'>Dataset ID</div>

CostAndUsage

<div class='h4-nonindex'>Display Name</div>

Cost and Usage

<div class='h4-nonindex'>Description</div>

Describes the cost and usage incurred by consuming a provider's resources and services.

<div class='h4-nonindex'>Introduced (version)</div>

0.5
