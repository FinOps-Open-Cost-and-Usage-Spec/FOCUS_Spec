# Discount Types

Providers offer various discounting schemes for their service offerings. These discounts typically fall into common types such as:

- Commitment-based discounts
- Tier-based discounts
- Negotiated discounts
- Promotional discounts
- Usage-based discounts
- Partner discounts

## Commitment-based discounts

Notes:

- Usage-based commitment discounts
- Spend-based commitment discounts

## Tier-based discounts

- RI Volume Discounts?

## Negotiated discounts

TBD

## Promotional discounts

- Free Trial
- Promotion discounts given by sales representatives to onboard customers.

## Usage-based discounts

- An example of this is GCP's [Sustained use discounts](https://cloud.google.com/compute/docs/sustained-use-discounts) which are still usage-based but not associated to any commitments.

## Partner discounts

- Private Rate Discounts
- Enterprise Discount Program
- Solution Provider Program
- RESELLER_MARGIN

# Links to documentation

- AWS
  - Reserved Instances - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html
  - Savings Plans - https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html
  - Bundled discounts - https://aws.amazon.com/blogs/aws-cloud-financial-management/bundled-discounts-in-aws-cost-and-usage-report/

- GCP
  - Committed use discounts - https://cloud.google.com/compute/docs/instances/committed-use-discounts-overview
  - Resource-based CUDs - https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts
  - Spend-based CUDs - https://cloud.google.com/docs/cuds-spend-based
  - Sustained use discounts - https://cloud.google.com/compute/docs/sustained-use-discounts
  - Credit types - https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#standard-usage-cost-data-schema

- Microsoft
  - Reservations - https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations
  - Savings Plans - https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/savings-plan-compute-overview
  - Azure Hybrid Benefit - https://azure.microsoft.com/en-us/pricing/hybrid-benefit/#overview
  - Azure Dev/Test Pricing - https://azure.microsoft.com/en-us/pricing/offers/dev-test/

# Discussion / Scratch space

- AWS discount types include:
  - DiscountedUsage - discounts covered by Reserved Instances
  - SavingsPlanCoveredUsage - discounts covered by SavingsPlans
  - EdpDiscount - Enterprise Discount Program
  - SppDiscount - Solutions Provider Program
  - RiVolumeDiscount
  - BundledDiscount - discounted usage on a specific product/service based on the usage of another product/service.

- GCP discount types include:
  - DISCOUNT - credits earned after a contractual spending threshold is reached.
  - COMMITTED_USAGE_DISCOUNT - resource-based commitment discounts.
  - COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE - Spend-based commitment discounts.
  - SUSTAINED_USAGE_DISCOUNT - automatic discount earned for prolonged usage.
  - FREE_TIER - free resource usage up to specified limits.
  - PROMOTION - includes free tial, marketing campaign credits, or other grants to use GCP.
  - RESELLER_MARGIN - indicates the Reseller Program Discounts earned on every eligible line item.
  - SUBSCRIPTION_BENEFIT - credits earned by purchasing long-term subscriptions to services in exchange for discounts.

- Where does spot instance usage-based discount fall under? Should there be a **Usage-based discounts** type?

- Where does GCP's sustained usage discount fall under? Maybe the same as spot instance, in which case, **Usage-based discounts**?

- Microsoft discounts include:
  - Azure consumption discounts
  - Reservations and Savings Plans
  - CSP software subscriptions
  - Office 365, Dynamics 365, Microsoft 365 discounts
  - Azure Hybrid Benefit
  - Azure Dev/Test Pricing
