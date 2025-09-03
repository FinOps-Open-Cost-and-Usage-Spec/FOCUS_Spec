# Cost and Usage

The Cost and Usage dataset is the primary dataset for FOCUS cost and usage data.

The specification for the Cost and Usage dataset defines a group of columns that provide qualitative values (such as dates, resource, and provider information) categorized as "dimensions" and quantitative values (numeric values) categorized as "metrics" that can be used for performing various [FinOps capabilities][FODOFC]. Metrics are commonly used for aggregations (sum, multiplication, averaging etc.) and statistical operations within the dataset. Dimensions are commonly used to categorize, filter, and reveal details in your data when combined with metrics. The columns are presented in alphabetical order.

<div class='h4-nonindex'>Columns</div>

<<column list TBD>>

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
