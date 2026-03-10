# Billing Scenario Examples

The following examples illustrate how BilledCost and EffectiveCost behave across common SaaS and PaaS billing models. Each scenario uses publicly available pricing and demonstrates a distinct billing pattern that SaaS or PaaS data generators may encounter when implementing the FOCUS specification.

These examples complement the existing SaaS examples by covering credit-based consumption, host-based monitoring, seat-based annual subscriptions, multi-unit PaaS usage, flat-rate licensing, annual commitment billed monthly, and tiered pricing with committed minimums.

## Credit-Based Consumption: On-Demand Data Platform Usage

A data platform provider uses a credit-based consumption model. Customers consume credits based on warehouse compute activity and pay a fixed per-credit rate determined by their service edition. Storage is billed separately on a per-terabyte basis.

The provider's on-demand pricing for this example (Enterprise edition):

| Service | SKU | Unit Price | Pricing Unit |
| :------ | :-- | ---------: | :----------- |
| Virtual Warehouse Compute | XS Warehouse | &dollar;3.00 | Credit |
| Virtual Warehouse Compute | Medium Warehouse | &dollar;3.00 | Credit |
| Storage | Active Storage | &dollar;23.00 | TB |

Credit consumption varies by warehouse size. An XS warehouse consumes 1 credit per hour. A Medium warehouse consumes 4 credits per hour.

A customer runs two warehouses in the US East region during January 2025:

* XS warehouse (analyst workload): 200 hours of runtime = 200 credits consumed
* Medium warehouse (ETL workload): 80 hours of runtime = 320 credits consumed (4 credits/hour)
* 5 TB of active storage

Three usage charges appear on the January invoice:

* XS Warehouse: `200 Credits x &dollar;3.00` = &dollar;600.00
* Medium Warehouse: `320 Credits x &dollar;3.00` = &dollar;960.00
* Active Storage: `5 TB x &dollar;23.00` = &dollar;115.00

Total [BilledCost](#datasets.costandusage.billedcost): &dollar;1,675.00

Key observations:

* [BilledCost](#datasets.costandusage.billedcost) and [EffectiveCost](#datasets.costandusage.effectivecost) are equal on all rows. With no related purchase charges, the [*cash-based*](#glossary:cash-based-accounting) and [*accrual-based*](#glossary:accrual-based-accounting) costs align.
* Both warehouses share the same [ListUnitPrice](#datasets.costandusage.listunitprice) of &dollar;3.00 per credit. The credit price is determined by the service edition, not warehouse size.
* [ConsumedUnit](#datasets.costandusage.consumedunit) is "Credits" for compute and "TB" for storage. The credit is the provider's unit of compute consumption.
* [ChargeFrequency](#datasets.costandusage.chargefrequency) is "Usage-Based" for compute (metered by credit consumption) and "Recurring" for storage (billed per TB per month).
* Storage has no [ResourceId](#datasets.costandusage.resourceid) or [ResourceName](#datasets.costandusage.resourcename) because it is an account-level charge, not tied to a specific [*resource*](#glossary:resource).

[**CSV Example**](/specification/data/saas_examples/credit_based_consumption_a.csv)

## Host-Based SaaS Monitoring: Monthly On-Demand Usage

A SaaS observability provider offers multiple monitoring [*services*](#glossary:service) billed on different units: host-based pricing for infrastructure and application performance monitoring, and volume-based pricing for log ingestion.

The provider's on-demand pricing for this example:

| Service | SKU | Unit Price | Pricing Unit |
| :------ | :-- | ---------: | :----------- |
| Infrastructure Monitoring | Infra Pro | &dollar;18.00 | Host |
| APM | APM Standard | &dollar;36.00 | Host |
| Log Management | Log Ingestion | &dollar;0.10 | GB |

A customer uses the provider's monitoring platform on a month-to-month basis with no annual commitment. During January 2025, the customer's usage is:

* 25 infrastructure hosts monitored
* 10 APM hosts monitored (a subset of the infrastructure hosts, billed independently)
* 150 GB of logs ingested

Three usage charges appear on the January invoice:

* Infrastructure Monitoring: `25 Hosts x &dollar;18.00` = &dollar;450.00
* APM: `10 Hosts x &dollar;36.00` = &dollar;360.00
* Log Management: `150 GB x &dollar;0.10` = &dollar;15.00

Total [BilledCost](#datasets.costandusage.billedcost): &dollar;825.00

Key observations:

* [BilledCost](#datasets.costandusage.billedcost) and [EffectiveCost](#datasets.costandusage.effectivecost) are equal on all rows. With no related purchase charges, the [*cash-based*](#glossary:cash-based-accounting) and [*accrual-based*](#glossary:accrual-based-accounting) costs align.
* [ChargeFrequency](#datasets.costandusage.chargefrequency) is "Recurring" for the host-based *services* (billed per host per month regardless of utilization within the month) and "Usage-Based" for log ingestion (billed on actual volume consumed).
* APM hosts are a subset of infrastructure hosts but each *service* is billed independently. The 10 APM hosts also appear in the 25 infrastructure host count.
* No [RegionId](#datasets.costandusage.regionid) or [RegionName](#datasets.costandusage.regionname) values are present. As a SaaS platform, billing is not region-specific.
* All three *services* share the [ServiceCategory](#datasets.costandusage.servicecategory) "Management and Governance" per the FOCUS allowed values for logging, monitoring, and observability *services*.

[**CSV Example**](/specification/data/saas_examples/host_based_saas_monitoring_a.csv)

## Seat-Based SaaS Subscription: Annual Upfront with Commitment Discount

This example illustrates an annual upfront SaaS subscription where the customer receives a discounted per-user rate by committing to a 12-month term. The discounted rate is only available with the annual commitment, making this a [*commitment discount*](#glossary:commitment-discount).

The provider offers a project management platform with the following pricing for 50 users on the Standard plan:

| Billing Option | Unit Price | Monthly Cost (50 users) | Annual Cost |
| :------------- | ---------: | ----------------------: | ----------: |
| Monthly | &dollar;9.05/user/month | &dollar;452.50 | &dollar;5,430.00 |
| Annual | &dollar;7.58/user/month | &dollar;379.00 | &dollar;4,550.00 |

The annual option represents a ~16% discount versus monthly billing.

A customer subscribes to the Standard plan for 50 users on April 1, 2025. They choose the annual billing option, paying &dollar;4,550.00 upfront for a 12-month term ending April 1, 2026. All 50 seats are occupied in the first month.

Two charges appear in the April 2025 [*billing period*](#glossary:billing-period):

**Purchase Charge:** [ChargeCategory](#datasets.costandusage.chargecategory) is "Purchase" with [ChargeFrequency](#datasets.costandusage.chargefrequency) "One-Time". The full annual amount is invoiced in a single payment.
* The [*charge period*](#glossary:chargeperiod) spans the entire commitment term: April 1, 2025 through April 1, 2026.
* [BilledCost](#datasets.costandusage.billedcost) is &dollar;4,550.00. This is the [*cash-based*](#glossary:cash-based-accounting) invoiced amount for the annual subscription.
* [EffectiveCost](#datasets.costandusage.effectivecost) is &dollar;0.00. The purchase covers future usage. Cost is recognized on an [*accrual basis*](#glossary:accrual-based-accounting) as usage occurs.
* [ListCost](#datasets.costandusage.listcost) is &dollar;5,430.00 (`50 users x &dollar;9.05/user/month x 12 months`). This represents the cost without the annual discount.
* [ContractedCost](#datasets.costandusage.contractedcost) is &dollar;4,550.00. This equals BilledCost since the customer pays the contracted annual price.
* [ResourceId](#datasets.costandusage.resourceid) equals [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid). The *commitment discount* itself is the [*resource*](#glossary:resource) being purchased.
* [CommitmentDiscountCategory](#datasets.costandusage.commitmentdiscountcategory) is "Spend" because the commitment is denominated in dollars, not usage units.
* [CommitmentDiscountQuantity](#datasets.costandusage.commitmentdiscountquantity) is 4,550.00 [CommitmentDiscountUnit](#datasets.costandusage.commitmentdiscountunit) (USD). This is the total spend eligible for consumption over the term.
* [PricingCategory](#datasets.costandusage.pricingcategory) is "Standard". The purchase of the *commitment discount* is at the agreed-upon rate.

**Usage Charge (April 2025):** [ChargeCategory](#datasets.costandusage.chargecategory) is "Usage" with [PricingCategory](#datasets.costandusage.pricingcategory) "Committed". The usage is covered by the annual purchase.
* [BilledCost](#datasets.costandusage.billedcost) is &dollar;0.00. No additional invoiced amount. The usage is covered by the purchase charge.
* [EffectiveCost](#datasets.costandusage.effectivecost) is &dollar;379.00. This is the [*accrual-based*](#glossary:accrual-based-accounting) recognized portion of the annual commitment: `&dollar;4,550 / 12 months`.
* [ListCost](#datasets.costandusage.listcost) is &dollar;452.50 (`50 users x &dollar;9.05/user`). The monthly list cost without the annual discount.
* [ContractedCost](#datasets.costandusage.contractedcost) is &dollar;452.50, equal to ListCost. Because no [*negotiated discounts*](#glossary:negotiated-discount) apply (the annual rate is a published *commitment discount*, not a bilateral negotiation), [ContractedUnitPrice](#datasets.costandusage.contractedunitprice) defaults to ListUnitPrice per the spec. The commitment discount savings appear in the difference between ContractedCost and EffectiveCost.
* [CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus) is "Used". All 50 seats are occupied.
* [CommitmentDiscountQuantity](#datasets.costandusage.commitmentdiscountquantity) is 379.00 USD. This is the amount of spend consumed from the commitment in this [*charge period*](#glossary:chargeperiod).
* [ResourceId](#datasets.costandusage.resourceid) is the actual *resource* (the customer's project management site), not the *commitment discount*.

**Rounding Note:** The EffectiveCost of &dollar;379.00 is derived from `&dollar;4,550 / 12 months` = &dollar;379.1667 per month. In this example the monthly amount is rounded. In a full 12-month dataset, the final month's charge would include a true-up to ensure the sum of EffectiveCost across all usage rows equals the BilledCost of the purchase row.

[**CSV Example**](/specification/data/saas_examples/seat_based_saas_annual_a.csv)

## Multi-Unit Usage-Based PaaS: Database-as-a-Service

A PaaS database [*service*](#glossary:service) provider bills different resource types on different units. The provider offers dedicated database clusters with separate charges for compute, storage, and data transfer.

The provider's on-demand pricing for this example:

| Service | SKU | Unit Price | Pricing Unit |
| :------ | :-- | ---------: | :----------- |
| Atlas Dedicated Clusters | M10 Cluster | &dollar;0.08 | Hour |
| Atlas Dedicated Clusters | M30 Cluster | &dollar;0.54 | Hour |
| Atlas Storage | SSD Storage | &dollar;0.25 | GB |
| Atlas Data Transfer | Data Transfer Out | &dollar;0.01 | GB |

A customer runs two dedicated database clusters in the US East region for the full month of January 2025 (744 hours). They also consume 100 GB of SSD storage and 50 GB of outbound data transfer.

* 1x M10 cluster (analytics workload): 744 hours at &dollar;0.08/hour
* 1x M30 cluster (production workload): 744 hours at &dollar;0.54/hour
* 100 GB of SSD storage
* 50 GB of outbound data transfer

Four usage charges appear on the January invoice:

* M10 Cluster: `744 Hours x &dollar;0.08` = &dollar;59.52
* M30 Cluster: `744 Hours x &dollar;0.54` = &dollar;401.76
* SSD Storage: `100 GB x &dollar;0.25` = &dollar;25.00
* Data Transfer Out: `50 GB x &dollar;0.01` = &dollar;0.50

Total [BilledCost](#datasets.costandusage.billedcost): &dollar;486.78

Key observations:

* [BilledCost](#datasets.costandusage.billedcost) and [EffectiveCost](#datasets.costandusage.effectivecost) are equal on all rows. With no related purchase charges, the [*cash-based*](#glossary:cash-based-accounting) and [*accrual-based*](#glossary:accrual-based-accounting) costs align.
* Three different [PricingUnit](#datasets.costandusage.pricingunit) values appear within a single provider: Hours (compute), GB (storage), and GB (data transfer). This heterogeneity is typical for PaaS database *services*.
* [ChargeFrequency](#datasets.costandusage.chargefrequency) varies by resource type. Compute clusters are "Usage-Based" (metered hourly). Storage is "Recurring" (billed per GB provisioned per month regardless of access patterns). Data transfer is "Usage-Based" (billed on actual volume transferred).
* Compute clusters have [ResourceId](#datasets.costandusage.resourceid) and [ResourceName](#datasets.costandusage.resourcename) values because each cluster is a distinct [*resource*](#glossary:resource). Storage and data transfer are account-level charges with no specific *resource*, so these columns are null.
* All four charges share the [ServiceCategory](#datasets.costandusage.servicecategory) "Databases" but are split across three distinct [ServiceName](#datasets.costandusage.servicename) values: Atlas Dedicated Clusters, Atlas Storage, and Atlas Data Transfer.
* [RegionId](#datasets.costandusage.regionid) and [RegionName](#datasets.costandusage.regionname) are populated. Unlike SaaS *services*, PaaS database clusters are deployed to specific regions and pricing may vary by region.

[**CSV Example**](/specification/data/saas_examples/multi_unit_paas_database_a.csv)

## Flat-Rate SaaS Licensing: Fixed Monthly Subscription

A project management and team communication provider offers a single flat-rate subscription. All features and unlimited users are included for a fixed monthly fee with no per-user pricing.

The provider's pricing for this example:

| Service | SKU | Unit Price | Pricing Unit |
| :------ | :-- | ---------: | :----------- |
| Basecamp | Pro Unlimited | &dollar;349.00 | Subscription |

The provider also offers an annual billing option at &dollar;299.00 per month (billed annually). This example uses the month-to-month option with no annual commitment.

A customer subscribes to the Pro Unlimited plan on a month-to-month basis. During January 2025, the customer's team of 35 people uses the platform.

One charge appears on the January invoice:

* Pro Unlimited: `1 Subscription x &dollar;349.00` = &dollar;349.00

Total [BilledCost](#datasets.costandusage.billedcost): &dollar;349.00

Key observations:

* [BilledCost](#datasets.costandusage.billedcost) and [EffectiveCost](#datasets.costandusage.effectivecost) are equal. With no related purchase charges, the [*cash-based*](#glossary:cash-based-accounting) and [*accrual-based*](#glossary:accrual-based-accounting) costs align.
* [ChargeFrequency](#datasets.costandusage.chargefrequency) is "Recurring". The subscription is a fixed monthly fee regardless of usage activity or user count within the [*billing period*](#glossary:billing-period).
* [PricingUnit](#datasets.costandusage.pricingunit) is "Subscriptions" and [PricingQuantity](#datasets.costandusage.pricingquantity) is 1. Unlike per-seat or per-unit models, the entire platform is a single billable unit.
* There is no relationship between [ConsumedQuantity](#datasets.costandusage.consumedquantity) and the number of users. The 35-person team does not affect the charge.
* If the customer chose the annual billing option (&dollar;299.00/month billed annually), this would follow a [*commitment discount*](#glossary:commitment-discount) pattern similar to the Seat-Based SaaS Subscription example above, with a Purchase row for the annual payment and monthly Usage rows for amortized [EffectiveCost](#datasets.costandusage.effectivecost).

[**CSV Example**](/specification/data/saas_examples/flat_rate_saas_licensing_a.csv)

## Annual Commitment Billed Monthly: Seat-Based CRM

A CRM provider offers a seat-based sales platform requiring an annual commitment. Unlike prepaid annual subscriptions, one billing option charges monthly throughout the contract term. The monthly billed rate equals the list price, so no [*commitment discount*](#glossary:commitment-discount) is applied in FOCUS terms.

The provider's pricing for this example (Professional plan, 10 users):

| Billing Option | Unit Price | Monthly Cost (10 users) | Annual Cost |
| :------------- | ---------: | ----------------------: | ----------: |
| Annual (pay upfront) | &dollar;90.00/user/month | &dollar;900.00 | &dollar;10,800.00 |
| Annual (billed monthly) | &dollar;100.00/user/month | &dollar;1,000.00 | &dollar;12,000.00 |

A customer subscribes to the Professional plan for 10 users, choosing the annual commitment with monthly billing. They pay &dollar;100.00 per user per month with no upfront payment.

One charge appears on the January 2025 invoice:

* Sales Hub Professional: `10 Users x &dollar;100.00` = &dollar;1,000.00

Total [BilledCost](#datasets.costandusage.billedcost): &dollar;1,000.00

Key observations:

* [BilledCost](#datasets.costandusage.billedcost), [EffectiveCost](#datasets.costandusage.effectivecost), [ListCost](#datasets.costandusage.listcost), and [ContractedCost](#datasets.costandusage.contractedcost) are all equal at &dollar;1,000.00. Monthly billing on an annual contract produces no divergence between [*cash-based*](#glossary:cash-based-accounting) and [*accrual-based*](#glossary:accrual-based-accounting) costs because there is no upfront payment to amortize.
* [PricingCategory](#datasets.costandusage.pricingcategory) is "Standard" because the billed rate equals the [ListUnitPrice](#datasets.costandusage.listunitprice). The annual contract is a term commitment, not a pricing discount. No [*commitment discount*](#glossary:commitment-discount) columns are populated.
* [ChargeFrequency](#datasets.costandusage.chargefrequency) is "Recurring" because the charge recurs monthly at a fixed per-seat rate regardless of usage activity within the [*billing period*](#glossary:billing-period).
* If the customer chose the annual pay-upfront option (&dollar;90.00/user/month), the &dollar;10.00 per-seat discount would qualify as a [*commitment discount*](#glossary:commitment-discount), following the pattern in the Seat-Based SaaS Subscription example with a Purchase row and amortized [EffectiveCost](#datasets.costandusage.effectivecost).
* This scenario demonstrates that an annual contract does not automatically produce a [*commitment discount*](#glossary:commitment-discount) in FOCUS. The distinguishing factor is whether the commitment provides a price reduction from the standard rate.

[**CSV Example**](/specification/data/saas_examples/annual_commitment_billed_monthly_a.csv)

## Tiered Pricing with Committed Minimum: Email API Platform

A SaaS email API provider offers tiered plans that include a monthly email allowance. Emails sent within the allowance are covered by the plan fee. Emails exceeding the allowance are billed at a per-email overage rate. The plan minimum functions as a usage-denominated [*commitment discount*](#glossary:commitment-discount) because the customer pays a fixed fee for a quantity of usage units.

The provider's pricing for this example (Essentials 50K plan):

| Component | Rate | Unit |
| :-------- | ---: | :--- |
| Plan fee (includes 50,000 emails) | &dollar;19.95 | Month |
| Overage | &dollar;0.00133 | Email |

This example covers two billing periods to show both under-minimum and over-minimum scenarios:

* **January 2025:** The customer sends 30,000 emails, below the 50,000 email allowance. 20,000 emails go unused.
* **February 2025:** The customer sends 65,000 emails, exceeding the allowance by 15,000.

**January charges (under minimum):**

The monthly plan fee of &dollar;19.95 appears as a Purchase charge. Two Usage charges split the commitment between used and unused portions:

* Purchase: &dollar;19.95 (plan fee covering 50,000 emails)
* Used: 30,000 emails, [EffectiveCost](#datasets.costandusage.effectivecost) = &dollar;11.97 (`30,000 / 50,000 x &dollar;19.95`)
* Unused: 20,000 emails, [EffectiveCost](#datasets.costandusage.effectivecost) = &dollar;7.98 (`20,000 / 50,000 x &dollar;19.95`)

Total [BilledCost](#datasets.costandusage.billedcost): &dollar;19.95

**February charges (over minimum):**

The customer uses all 50,000 plan emails plus 15,000 overage emails:

* Purchase: &dollar;19.95 (plan fee covering 50,000 emails)
* Used: 50,000 emails, [EffectiveCost](#datasets.costandusage.effectivecost) = &dollar;19.95 (full allowance consumed)
* Overage: 15,000 emails at &dollar;0.00133 = &dollar;19.95 (standard pricing, not part of commitment)

Total [BilledCost](#datasets.costandusage.billedcost): &dollar;39.90

Key observations:

* [CommitmentDiscountCategory](#datasets.costandusage.commitmentdiscountcategory) is "Usage" on all commitment-related rows. The plan minimum is denominated in email quantity (50,000 emails), not a dollar amount. This distinguishes it from the "Spend" category in the Seat-Based SaaS Subscription example.
* [CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus) shows "Used" and "Unused" on Usage rows. In January, the customer only consumed 30,000 of 50,000 emails, so the remaining 20,000 generate an "Unused" row. The Unused row has [BilledCost](#datasets.costandusage.billedcost) of &dollar;0.00 but [EffectiveCost](#datasets.costandusage.effectivecost) of &dollar;7.98, representing waste from the commitment.
* The Purchase row has [BilledCost](#datasets.costandusage.billedcost) of &dollar;19.95 and [EffectiveCost](#datasets.costandusage.effectivecost) of &dollar;0.00. This follows the same pattern as the Seat-Based SaaS Subscription: the purchase captures the [*cash-based*](#glossary:cash-based-accounting) cost, while [*accrual-based*](#glossary:accrual-based-accounting) cost is recognized on the Usage rows.
* The overage row in February has no [*commitment discount*](#glossary:commitment-discount) columns populated. Overage emails are billed at the standard per-email rate and are not part of the commitment.
* [ContractedUnitPrice](#datasets.costandusage.contractedunitprice) and [ListUnitPrice](#datasets.costandusage.listunitprice) are both &dollar;0.00133 on all Usage rows. Because no [*negotiated discounts*](#glossary:negotiated-discount) apply, ContractedUnitPrice defaults to ListUnitPrice per the spec. The *commitment discount* savings are reflected in the difference between [ContractedCost](#datasets.costandusage.contractedcost) and [EffectiveCost](#datasets.costandusage.effectivecost), not in ContractedUnitPrice.
* [ChargeFrequency](#datasets.costandusage.chargefrequency) is "Recurring" on the Purchase rows (the plan fee recurs monthly) and "Usage-Based" on the Usage rows (charges vary based on email volume consumed).

[**CSV Example**](/specification/data/saas_examples/tiered_pricing_committed_minimum_a.csv)
