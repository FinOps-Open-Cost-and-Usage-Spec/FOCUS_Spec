# Column: ChargeType

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                | Column                                                                                                                                                                                     |
| --------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AWS       | CUR                     | `bill/InvoicingEntity` (Amazon Web Services, Inc.)<br>`bill/BillingEntity` (AWS, AWS Marketplace)<br>bill/BillType (Anniversary, Purchase, Refund)<br>`lineItem/LineItemType` (Usage, Tax) |
| GCP       | BigQuery Billing Export | `Cost type` (regular, tax, adjustment, or rounding error)                                                                                                                                  |
| Microsoft | Cost details            | `ChargeType` (Purchase, Usage, Refund, Adjustment, Tax?)<br><br>Related:<br>`PricingModel` (OnDemand, Reservation, SavingsPlan, Spot)<br>`Frequency` (OneTime, Recurring)                  |

## Example usage scenarios

Current values observed in billing data for various scenarios:

- AWS

  | lineItem/LineItemType | lineItem/ProductCode | lineItem/UsageType          | lineItem/Operation       | lineItemType/ResourceId |
  | --------------------- | -------------------- | --------------------------- | ------------------------ | ----------------------- |
  | Usage                 | AmazonCloudWatch     | USW2-CW:GMD-Metrics         | GetMetricData            | No resource id          |
  | Usage                 | AmazonRDS            | USW2-RDS:ChargedBackupUsage | CreateDBInstance         | No resource id          |
  | Usage                 | AmazonS3             | Requests-Tier2              | ​​​​GetLensConfiguration | No resource id          |
  | Usage                 | AmazonSES            | USW2-DataTransfer-In-Bytes  | SendRawEmail             | No resource id          |
  | Usage                 | AWSCloudTrail        | APN3-FreeEventsRecorded     | None                     | No resource id          |
  | Usage                 | AWSCostExplorer      | USE1-CostDataStorage        | CostDataStorage          | No resource id          |
  | Usage                 | awskms               | us-west-2-KMS-Requests      | ListKeys                 | No resource id          |
  | Usage                 | AWSLambda            | USW2-USE1-AWS-In-Bytes      | Invoke                   | No resource id          |
  | Usage                 | AWSSupportBusiness   | Dollar                      | None                     | No resource id          |
  | Usage                 | AmazonEC2            | USW2-ElasticIP:IdleAddress  | AssociateAddressVPC      | No resource id          |
  | Tax                   | AmazonEC2            | USW2-BoxUsage:c5.large      | RunInstances             | No resource id          |

  | lineItem/LineItemType                               | Usage Type             | Operation      | Product Code |
  | --------------------------------------------------- | ---------------------- | -------------- | ------------ |
  | BundledDiscount                                     | BoxUsage:c5.large      | RunInstances   | AmazonEC2    |
  | Credit                                              | TimedStorage-ByteHrs   | CreateSnapshot | AmazonEBS    |
  | Discount                                            | DataTransfer-Out-Bytes | AmazonS3       | AmazonS3     |
  | DiscountedUsage                                     | BoxUsage:m5.xlarge     | RunInstances   | AmazonEC2    |
  | Fee (paid for All Upfront RI or Partial Upfront RI) | HeavyUsage:r5.large    | RunInstances   | AmazonEC2    |
  | Refund                                              | DataTransfer-In-Bytes  | AmazonS3       | AmazonS3     |
  | RIFee                                               | BoxUsage:m5.large      | RunInstances   | AmazonEC2    |
  | Tax (US sales tax or VAT)                           | DataTransfer-Out-Bytes | AmazonS3       | AmazonS3     |
  | Usage                                               | BoxUsage:t2.micro      | RunInstances   | AmazonEC2    |
  | SavingsPlanUpfrontFee                               | BoxUsage:c5.xlarge     | RunInstances   | AmazonEC2    |
  | SavingsPlanRecurringFee                             | BoxUsage:m5.large      | RunInstances   | AmazonEC2    |
  | SavingsPlanCoveredUsage                             | BoxUsage:r5.large      | RunInstances   | AmazonEC2    |
  | SavingsPlanNegation                                 | BoxUsage:m5.2xlarge    | RunInstances   | AmazonEC2    |

## Discussion / Scratch space

- What different types of line items do we want to group?
- This work is to group the different values providers use to differentiate cost line items. The plan is to introduce a "normalized" dimension for this in v1.0
  - Should this be prefixed with "Provider" since we want to normalize this as well? If not, we have to come up with another name for the same thing.
  - This may be referred to in other contexts (e.g., data granularity requirements may change if its usage data vs tax or fees). ResourceId should be required based on if something is a "usage" cost?
- Need to add more details about what each of the values means and how/when they should be used.
- Are we making any statements about taxes being required?
- Use cases:
  - Usage for cost reporting use cases / driving accountability
  - Tax needs to be filterable for special accounting treatments within companies
  - Fees are important for cost allocation / amortization - needs to be isolated from other cost
  - Refunds - $s coming back after the original charge
  - Credits are typically based on agreements for migration of workloads
  - AWS: Anniversary charge (BillType) Savings Plan Negations for UsageType (for -0.50)
- Question for AWS practitioners:
  - For the "Usage" `lineItem/LineItemType`, the `lineItenType/ResourceId` is empty for many AWS services depending on the `lineItem/UsageType` and `lineItem/Operation`.
  - For the "Tax" `lineItem/LineItemType`, the `lineItenType/ResourceId` is always empty for all AWS services.
- Discussion about possible ChargeType values

  - Purchase (prepayment)
    - SavingsPlanRecurringFee
    - SavingsPlanUpfrontFee
    - RIFee
    - Fee
  - Usage (postpayment)
    - DiscountedUsage
    - Discount
    - SavingsPlanCoveredUsage
    - BundledDiscount
    - SavingsPlanNegation (?)
  - Adjustment
    - Rounding Errors (computers don't do numbers well)
    - Refund (Correcting a charge)
    - Credits (Mystery Money)
  - Tax

  | Charge Type | Frequency | PricingModel |
  | ----------- | --------- | ------------ |
  | Purchase    | Monthly   | SavingsPlan  |
  | Purchase    | OneTime   | SavingsPlan  |
  | Usage       | Hourly    | OnDemand     |
  | Usage       |           | SavingsPlan  |
  | Usage       |           | Reservation  |
  | Usage       |           |              |

  | Line Item Type       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Usage                | The most common type and the default. The line item represents a charge for the use of some cloud resource. "Real Cost" includes only Usage line items and uses the first available cost type provided from: amortized_cost, discounted_cost, or cost                                                                                                                                                                                                                                       |
  | Tax                  | This line item represents any tax charges. Columns in the time, resource, and action categories should only be populated if the tax is associated with applicable Usage changes. Otherwise these columns should be left blank.                                                                                                                                                                                                                                                              |
  | Support              | Charges for support or other human services. Columns in the time category should specify the start and end of the support contract.                                                                                                                                                                                                                                                                                                                                                         |
  | Purchase             | Charge for a one-time purchase or non-usage based subscription; for example, software bought from the AWS Marketplace. The time category columns should represent the span of time over which the purchase applies (for subscriptions with renewal) or the time of the purchase (for one-time charges).                                                                                                                                                                                     |
  | CommittedUsePurchase | Charges for a "committed use" (RI, savings plan, etc.) purchase. "Committed use" includes any instrument for which payment is made to receive a reduced rate on future usage. This may include one-time upfront purchases or recurring monthly charges. The time category columns should represent the span of time over which the charge applies (for example, one month for monthly recurring charges.) The amortized_cost cost column of this line item should always be zero (if used). |
  | Discount             | A negative value cost associated with some Usage line item. Columns in the time, resource, and action categories of this line item should match those of the applicable Usage line item and the cost should be negative. The discounted_cost for this line item should be zero if this discount is fully accounted for in the discounted_cost of other Usage line items. (Please note: you must still include discounted_cost if it should be zero)                                         |
  | Credit               | A negative value cost not associated with any specific Usage line items. May represent a refund, special sales deal, or other similar circumstance.                                                                                                                                                                                                                                                                                                                                         |
  | Fee                  | A positive value charge for which no other line item type applies.                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | Adjustment           | An alteration made to the bill to correct for some error or rounding issue.                                                                                                                                                                                                                                                                                                                                                                                                                 |

- Additional questions:
  - Is it Recurring or not? (Attribute about the Purchase?)
  - What Charge Types can BE recurring?
  - What Charge Types for "Free Tier" with usage limits and "Free Trial" offers?
