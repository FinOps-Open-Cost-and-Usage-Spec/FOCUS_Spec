# Column: CommitmentTerm

## Example provider mappings

| Provider  | Data set                 | Column                      | Example Value |
|:----------|:-------------------------|:----------------------------| :----------------------------|
| AWS       | CUR                      | N/A. AWS uses reservation/ReservationStartTime<br>and reservation/ReservationEndTime to describe<br> term of a reservation commitment.AWS uses <br> savingsplan/Starttime and savingsplan/Endtime to describe <br> term of a savings plan commitment. | N/A |
| GCP       | Committed use discounts (CUD) dashboard  | term | 3 Years |
| Microsoft | [Reservation Charges API](https://learn.microsoft.com/en-us/rest/api/billing/enterprise/billing-enterprise-api-reserved-instance-charges)  | term      | P1Y/P3Y |

## Documentation

- AWS:
  - [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html)
  - [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)
- GCP:
  - [Structure of Standard data export](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage)
  - [Structure of Detailed data export](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)
  - [Committed Use Discounts](https://cloud.google.com/docs/cuds)
- Microsoft:
  - [Azure Savings Plans](https://learn.microsoft.com/azure/cost-management-billing/savings-plan/savings-plan-compute-overview)
  - [Azure Reservations](https://learn.microsoft.com/azure/cost-management-billing/reservations/save-compute-costs-reservations)
  - [Azure billing detail schema](https://learn.microsoft.com/en-us/rest/api/billing/enterprise/billing-enterprise-api-usage-detail)


## Discussion Items:
- Should commitment data appear in the main billing data, or appear in a separate commitment data set? Cloud Providers differ a lot here.
