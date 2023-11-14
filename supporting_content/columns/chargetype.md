# Column: ChargeType

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                | Column                                                                                                                                                                                                                                                        |
| --------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS       | CUR                     | `bill/BillType` (Anniversary, Purchase, Refund)<br>`lineItem/LineItemType` (Usage, Tax, BundledDiscount, Credit, Discount, DiscountedUsage, Fee, Refund, RIFee, SavingsPlanUpfrontFee, SavingsPlanRecurringFee, SavingsPlanCoveredUsage, SavingsPlanNegation) |
| GCP       | BigQuery Billing Export | `Cost type` (regular, tax, adjustment, or rounding error)                                                                                                                                                                                                     |
| Microsoft | Cost details            | `ChargeType` (Purchase, Usage, Refund, Adjustment, Tax?)<br><br>Related:<br>`PricingModel` (OnDemand, Reservation, SavingsPlan, Spot)<br>`Frequency` (OneTime, Recurring)                                                                                     |

## Example usage scenarios

Current values observed in billing data for various scenarios:

| Provider  | Current value                      | ChargeType | Scenario                                                                                                                                                                                                                                                                                                                                                   |
| --------- | ---------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS       | Anniversary / Usage                | Usage      | Usage charged at on-demand rate for resources with resource id (EC2, EBS, RDS, RedShift)                                                                                                                                                                                                                                                                   |
| AWS       | Anniversary / Usage                | Usage      | Usage charged at on-demand rate for resources with "no resource id" (Support, CloudWatch, DataTransfer)                                                                                                                                                                                                                                                    |
| AWS       | Anniversary / Tax                  | Tax        | US sales tax or VAT with "no resource id"                                                                                                                                                                                                                                                                                                                  |
| AWS       | Purchase / Fee                     | Purchase   | All upfront and partial upfront fees for RI purchase                                                                                                                                                                                                                                                                                                       |
| AWS       | Purchase / RIFee                   | Purchase   | Monthly recurring RI amount for partial upfront and no upfront                                                                                                                                                                                                                                                                                             |
| AWS       | Purchase / SavingsPlanUpfrontFee   | Purchase   | All upfront and partial upfront fees for SP purchase                                                                                                                                                                                                                                                                                                       |
| AWS       | Purchase / SavingsPlanRecurringFee | Purchase   | Monthly recurring SP amount for partial upfront and no upfront                                                                                                                                                                                                                                                                                             |
| AWS       | Adjustments / SavingsPlanNegation  | Usage      | Used to negate the on-demand cost covered by SP                                                                                                                                                                                                                                                                                                            |
| AWS       | Anniversary / BundledDiscount      | Usage      | Usage based discount for free or discounted price. If a customer uses X units of product/service A, this customer gets Y units of product/service B at a discounted price (with a discount Z%).                                                                                                                                                            |
| AWS       | Refund                             | Adjustment |
| GCP       | regular                            | Usage      | These show up as rows that contain data of usage and costs                                                                                                                                                                                                                                                                                                 |
| GCP       | tax                                | Tax        | These show up as monthly rows without a project as a credit and with a project with a debit.                                                                                                                                                                                                                                                               |
| GCP       | adjustment                         | Adjustment | ![Screenshot of GCP cost details with type and mode columns.](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/assets/399533/af90e4cd-f3c0-448a-bb0f-0249bcf7135c)<br>Example 1:<br>Description: "Billing correction - Adjustment for project X for incorrect Flexible CUD charge"<br>Mode: "MANUAL_ADJUSTMENT"<br>Type: "GENERAL_ADJUSTMENT" |
| GCP       | rounding_error                     | Adjustment | These show up as monthly rows without a project as a credit                                                                                                                                                                                                                                                                                                |
| GCP       | credit                             | Adjustment | Fields: type, name, amount, full_name, id<br>![Screenshot of a table with a type column and 5 rows of example values](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/assets/399533/15bcc210-5a36-473b-aeac-c1d2682dfdc8)                                                                                                                    |
| Microsoft | Purchase                           | Purchase   | Upfront or recurring fee for Marketplace offers or commitment-based discounts.                                                                                                                                                                                                                                                                             |
| Microsoft | Usage                              | Usage      | Consumption-based usage of deployed resources.                                                                                                                                                                                                                                                                                                             |
| Microsoft | Refund                             | Adjustment | Refund provided by support.                                                                                                                                                                                                                                                                                                                                |
| Microsoft | Adjustment                         | Adjustment | Rounding errors.                                                                                                                                                                                                                                                                                                                                           |
| Microsoft | Tax                                | Tax        | US sales tax or VAT.                                                                                                                                                                                                                                                                                                                                       |

## Discussion / Scratch space

- What are the different types of spend that we want to group?
- This work is to group the different values providers use to differentiate the spend. The plan is to introduce a ‘normalized’ dimension for this in v1.0
  - Should this be prefixed with ‘Provider’ since we want to normalize this as well? If not, we have to come up with another name for the normalized column
    - Decided that this should be a normalized column from v0.5.
    - Given the mis-alignment of current vendor data, its not going to be much value to create a dimension where we put different vendor values in a single column so practitioners can use the vendor provided value using a single column rather than doing n different where clauses when looking for the vendor native value (not our normalized value).
- This dimension may be referred to in other contexts - e.g. data granularity requirements (attribute) may change based on if its usage data vs tax or fees. For example, Should ResourceId be required based on if something is a ‘usage’ cost vs a ‘purchase’?
- Use cases:
  - Usage for cost reporting use cases / driving accountability
  - Tax needs to be filterable for special accounting treatments within companies
  - Fees are important for cost allocation / amortization - needs to be isolated from other cost
  - Refunds - $s coming back after the original charge
  - Credits are typically based on agreements for migration of workloads
  - AWS handling for SPs: Anniversary charge (BillType) Savings Plan for $1 and a negation for UsageType (for -0.50)
- Is it Recurring or not? (Attribute about the Purchase?)
- What Charge Types can BE recurring?
- What Charge Types for "Free Tier" with usage limits and "Free Trial" offers?

### Example mappings for normalized values

| Provider  | Usage                                                                                                | Purchase                                                         | Adjustment               | Tax |
| --------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------ | --- |
| AWS       | DiscountedUsage<br>Discount<br>SavingsPlanCoveredUsage<br>BundledDiscount<br>SavingsPlanNegation (?) | SavingsPlanRecurringFee<br>SavingsPlanUpfrontFee<br>RIFee<br>Fee | Refund<br>Credits        | Tax |
| GCP       | regular                                                                                              |                                                                  | rounding_error<br>credit | tax |
| Microsoft | Usage                                                                                                | Purchase                                                         | Refund<br>Adjustment     | Tax |

### Examples of how Charge Type relates to Pricing Category / Charge Frequency columns

| Scenario| ChargeType | ChargeSubcategory | PricingCategory  | Charge Frequency |
|-|-|-|-|-|
| Upfront discount purchase | Purchase| NULL  | On-Demand  | One-time |
| Partial Upfront discount monthly fee | Purchase    | NULL  | On-Demand  | Recurring  |
| Usage covered by upfront portion of partial upfront discount | Usage   | Used Commitment   | Commitment-based | Usage-based  |
| Unused commitment of partial upfront discount    | Usage   | Unused Commitment | Commitment-based | Usage-based      |
| Usage not covered by discount | Usage | On-Demand  | On-Demand   | Usage-based|
| Refund | Adjustment   | Refund | NULL | One-time  |
| Usage invoice tax charge   | Tax   |  NULL |  NULL | Recurring        |
