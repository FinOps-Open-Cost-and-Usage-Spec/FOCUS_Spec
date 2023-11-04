# Column: ChargeSubcategory

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                | Column                                                                                                                                                                                                                                                        |
| --------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS       | CUR                     | `bill/BillType` (Refund)<br>`lineItem/LineItemType` (Tax, Credit, Discount, DiscountedUsage, Fee, Refund, RIFee, SavingsPlanUpfrontFee, SavingsPlanRecurringFee, SavingsPlanCoveredUsage, SavingsPlanNegation) |
| GCP       | BigQuery Billing Export | `Cost type` (tax, adjustment, or rounding error)                                                                                                                                                                                                     |
| Microsoft | Cost details            | `ChargeType` (Refund)<br><br>Related:<br>`PricingModel` (OnDemand, Reservation, SavingsPlan, Spot)<br>`Frequency` (OneTime, Recurring)  
| Microsoft | Cost Details            |`RoundingAdjustment` (RoundingAdjustment) |

## Example usage scenarios

Current values observed in billing data for various scenarios:

| Provider  | Current value                      | ChargeType | Scenario                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------- | ---------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |                                                                    
| AWS       | Refund                             | Adjustment |                                                                                                                                                                                                                                                              |
| GCP       | adjustment                         | Adjustment | ![Screenshot of GCP cost details with type and mode columns.](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/assets/399533/af90e4cd-f3c0-448a-bb0f-0249bcf7135c)<br>Example 1:<br>Description: "Billing correction - Adjustment for project X for incorrect Flexible CUD charge"<br>Mode: "MANUAL_ADJUSTMENT"<br>Type: "GENERAL_ADJUSTMENT" |
| GCP       | rounding_error                     | Adjustment | These show up as monthly rows without a project as a credit                                                                                                                                                                                                                                                                                                |
| GCP       | credit                             | Adjustment | Fields: type, name, amount, full_name, id<br>![Screenshot of a table with a type column and 5 rows of example values](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/assets/399533/15bcc210-5a36-473b-aeac-c1d2682dfdc8)                                                                                                                    |                                                                                                                                                                                                                                                                                                           |
| Microsoft | Refund                             | Adjustment | Refund for exchange of commited use such as exchanging or refunding a reservation                                                                                                                                                                                                                                                                                                                               |
| Microsoft | Adjustment                         | Billing Correction | Credit provided back by the provider for incorrect billing.                                                                                                                                                                                                                                                                                                                                           |
| Microsoft | Credit                             | Adjustment | Credit applied for good will or promotional credit or service level violation credits                                                                                                                                                                                                                                                                                                                                       |

## Discussion / Scratch space

- What adjustment categories do we need to group?
- Do we need to normalize adjustment categories?
- Refunds - $s coming back after the original charge
- Credits are typically based on agreements for migration of workloads, or promotional items negotiated with the provider
- Balance transfers - how do you show what a balance transfer is if in the unliely event you close an account with a positive value and open a new account

### Example mappings for normalized values

| Provider  | Usage                                                                                                | Purchase                                                         | Adjustment               | Tax |
| --------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------ | --- |
