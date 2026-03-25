# Billing Scenario Examples

The following examples illustrate how [BilledCost](#datasets.costandusage.billedcost) and [EffectiveCost](#datasets.costandusage.effectivecost) behave across common software as a service (SaaS) and platform as a service (PaaS) billing models. Each scenario uses a fictional [*service provider*](#glossary:service%20provider) with illustrative pricing and demonstrates a distinct billing pattern that SaaS or PaaS data generators may implement via the FOCUS specification.

Each example targets a specific billing pattern. All examples share a consistent column set; columns not applicable to a given scenario contain null values.

| Scenario | Service Provider | What You'll Learn |
| :--- | :--- | :--- |
| [Credit-Based Consumption](#credit-based-consumption-on-demand-data-platform-usage) | ClearQuery | Custom consumption units (Credits) with `ChargeFrequency` split between "Usage-Based" (compute) and "Recurring" (storage). No [*commitment discount*](#glossary:commitment-discount); BilledCost = EffectiveCost on all rows. |
| [Host-Based SaaS Monitoring](#host-based-saas-monitoring-monthly-on-demand-usage) | WatchTower | Multiple [*services*](#glossary:service) billed on independent metrics (hosts vs. GB). "Recurring" for host-based charges, "Usage-Based" for log ingestion. No regional billing. |
| [Seat-Based SaaS Subscription](#seat-based-saas-subscription-annual-upfront-with-commitment-discount) | TaskBoard Co | Upfront annual purchase amortized to monthly Usage rows. BilledCost vs. EffectiveCost divergence. Spend-based `CommitmentDiscountCategory`, One-Time `ChargeFrequency`. |
| [Multi-Unit PaaS Database](#multi-unit-usage-based-paas-database-as-a-service) | CloudDB | Three heterogeneous PricingUnit values (Hours, GB, GB) within one *service provider*. Region-specific billing with RegionId/RegionName populated. |
| [Flat-Rate SaaS Licensing](#flat-rate-saas-licensing-fixed-monthly-subscription) | TeamSpace | Fixed monthly subscription where PricingUnit is "Subscriptions" and PricingQuantity is 1, decoupled from underlying user count. |
| [Annual Commitment Billed Monthly](#annual-commitment-billed-monthly-seat-based-crm) | GrowthCRM | Annual term contract with monthly billing where the billed rate equals list price. No *commitment discount* despite the annual obligation. |
| [Tiered Pricing with Committed Minimum](#tiered-pricing-with-committed-minimum-email-api-platform) | QuickSend | Plan fee as a usage-denominated *commitment discount* with Used/Unused split and overage pricing. `CommitmentDiscountCategory` = "Usage". Two billing periods showing under- and over-minimum scenarios. |

## Credit-Based Consumption: On-Demand Data Platform Usage

A data platform [*service provider*](#glossary:service%20provider), ClearQuery, uses a credit-based consumption model. Customers consume credits based on warehouse compute activity and pay a fixed per-credit rate determined by their service edition. Storage is billed separately on a per-terabyte basis.

The *service provider*'s on-demand pricing for this example:

| Service | SKU | Unit Price | Pricing Unit | Credits/Hour |
| :------ | :-- | ---------: | :----------- | -----------: |
| Virtual Warehouse Compute | XS Warehouse | &dollar;3.00 | Credits | 1 |
| Virtual Warehouse Compute | Medium Warehouse | &dollar;3.00 | Credits | 4 |
| Storage | Active Storage | &dollar;23.00 | TB | n/a |

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

Here is how these charges appear in the data (relevant columns only):

| FOCUS Column | XS Warehouse | Medium Warehouse | Active Storage |
| :--- | :--- | :--- | :--- |
| ChargeCategory | Usage | Usage | Usage |
| ChargeFrequency | Usage-Based | Usage-Based | Recurring |
| ConsumedQuantity | 200 | 320 | 5 |
| ConsumedUnit | Credits | Credits | TB |
| BilledCost | &dollar;600.00 | &dollar;960.00 | &dollar;115.00 |
| EffectiveCost | &dollar;600.00 | &dollar;960.00 | &dollar;115.00 |
| ListCost | &dollar;600.00 | &dollar;960.00 | &dollar;115.00 |
| ContractedCost | &dollar;600.00 | &dollar;960.00 | &dollar;115.00 |
| PricingUnit | Credits | Credits | TB |
| PricingCategory | Standard | Standard | Standard |

Key observations:

* Both warehouses share the same [ListUnitPrice](#datasets.costandusage.listunitprice) of &dollar;3.00 per credit. The credit price is determined by the service edition, not warehouse size.
* [ConsumedUnit](#datasets.costandusage.consumedunit) is "Credits" for compute and "TB" for storage. The credit is the *service provider*'s unit of compute consumption.
* [ChargeFrequency](#datasets.costandusage.chargefrequency) is "Usage-Based" for compute (metered by credit consumption) and "Recurring" for storage (billed per TB per month).
* Storage has no [ResourceId](#datasets.costandusage.resourceid) or [ResourceName](#datasets.costandusage.resourcename) because it is an account-level charge, not tied to a specific [*resource*](#glossary:resource).
* [BilledCost](#datasets.costandusage.billedcost) and [EffectiveCost](#datasets.costandusage.effectivecost) are equal on all rows. These two columns diverge when a purchase [*charge*](#glossary:charge) covers future usage (as with a [*commitment discount*](#glossary:commitment-discount)), because the [*cash-based*](#glossary:cash-based-accounting) outflow is invoiced upfront while cost is recognized on an [*accrual basis*](#glossary:accrual-based-accounting) over time. With no such purchase [*charges*](#glossary:charge) here, the two views produce the same cost per row.

[**CSV Example**](/specification/data/saas_examples/credit_based_consumption_a.csv)

## Host-Based SaaS Monitoring: Monthly On-Demand Usage

A SaaS observability [*service provider*](#glossary:service%20provider), WatchTower, offers multiple monitoring [*services*](#glossary:service) billed on different units: host-based pricing for infrastructure and application performance monitoring, and volume-based pricing for log ingestion.

The *service provider*'s on-demand pricing for this example:

| Service | SKU | Unit Price | Pricing Unit |
| :------ | :-- | ---------: | :----------- |
| Infrastructure Monitoring | Infra Pro | &dollar;18.00 | Hosts |
| APM | APM Standard | &dollar;36.00 | Hosts |
| Log Management | Log Ingestion | &dollar;0.10 | GB |

A customer uses the *service provider*'s monitoring platform on a month-to-month basis with no annual commitment. During January 2025, the customer's usage is:

* 25 infrastructure hosts monitored
* 10 APM hosts monitored (a subset of the infrastructure hosts, billed independently)
* 150 GB of logs ingested

Three usage charges appear on the January invoice:

* Infrastructure Monitoring: `25 Hosts x &dollar;18.00` = &dollar;450.00
* APM: `10 Hosts x &dollar;36.00` = &dollar;360.00
* Log Management: `150 GB x &dollar;0.10` = &dollar;15.00

Total [BilledCost](#datasets.costandusage.billedcost): &dollar;825.00

Here is how these charges appear in the data (relevant columns only):

| FOCUS Column | Infra Monitoring | APM | Log Management |
| :--- | :--- | :--- | :--- |
| ChargeCategory | Usage | Usage | Usage |
| ChargeFrequency | Recurring | Recurring | Usage-Based |
| ConsumedQuantity | 25 | 10 | 150 |
| ConsumedUnit | Hosts | Hosts | GB |
| BilledCost | &dollar;450.00 | &dollar;360.00 | &dollar;15.00 |
| EffectiveCost | &dollar;450.00 | &dollar;360.00 | &dollar;15.00 |
| ListCost | &dollar;450.00 | &dollar;360.00 | &dollar;15.00 |
| ContractedCost | &dollar;450.00 | &dollar;360.00 | &dollar;15.00 |
| PricingUnit | Hosts | Hosts | GB |
| PricingCategory | Standard | Standard | Standard |

Key observations:

* [ChargeFrequency](#datasets.costandusage.chargefrequency) is "Recurring" for the host-based *services* (billed per host per month regardless of utilization within the month) and "Usage-Based" for log ingestion (billed on actual volume consumed).
* APM hosts are a subset of infrastructure hosts but each *service* is billed independently. The 10 APM hosts also appear in the 25 infrastructure host count.
* [RegionId](#datasets.costandusage.regionid) and [RegionName](#datasets.costandusage.regionname) are null. This *service provider* does not expose region in its billing. Some SaaS and PaaS *service providers* do bill by region, in which case these columns would be populated (see the Multi-Unit PaaS example below).
* [ResourceId](#datasets.costandusage.resourceid) and [ResourceName](#datasets.costandusage.resourcename) are null. The *service provider* bills at the *service* level (per host or per GB), not per individual monitored [*resource*](#glossary:resource).
* All three *services* share the [ServiceCategory](#datasets.costandusage.servicecategory) "Management and Governance" per the FOCUS allowed values for logging, monitoring, and observability *services*.
* [BilledCost](#datasets.costandusage.billedcost) and [EffectiveCost](#datasets.costandusage.effectivecost) are equal on all rows because there are no purchase [*charges*](#glossary:charge) covering future usage (see the Credit-Based Consumption example for a full explanation of when these columns diverge).

[**CSV Example**](/specification/data/saas_examples/host_based_saas_monitoring_a.csv)

## Seat-Based SaaS Subscription: Annual Upfront with Commitment Discount

This example illustrates an annual upfront SaaS subscription where the customer receives a discounted per-user rate by committing to a 12-month term. The discounted rate is only available with the annual commitment, making this a [*commitment discount*](#glossary:commitment-discount).

The [*service provider*](#glossary:service%20provider), TaskBoard Co, offers a project management platform with the following pricing for 50 users on the Standard plan:

| Billing Option | Unit Price | Monthly Cost (50 users) | Annual Cost |
| :------------- | ---------: | ----------------------: | ----------: |
| Monthly | &dollar;9.05/user/month | &dollar;452.50 | &dollar;5,430.00 |
| Annual | &dollar;7.58/user/month | &dollar;379.00 | &dollar;4,550.00 |

The annual option represents a ~16% discount versus monthly billing.

A customer subscribes to the Standard plan for 50 users on April 1, 2025. They choose the annual billing option, paying &dollar;4,550.00 upfront for a 12-month term ending April 1, 2026. All 50 seats are occupied in the first month.

Two charges appear in the April 2025 [*billing period*](#glossary:billing-period):

Here is how these charges appear in the data (relevant columns only):

| FOCUS Column | Purchase | Usage (April) |
| :--- | :--- | :--- |
| ChargeCategory | Purchase | Usage |
| ChargeFrequency | One-Time | Recurring |
| CommitmentDiscountCategory | Spend | Spend |
| CommitmentDiscountStatus | *(null)* | Used |
| CommitmentDiscountQuantity | 4,550.00 | 379.00 |
| CommitmentDiscountUnit | USD | USD |
| ConsumedQuantity | *(null)* | 50 |
| ConsumedUnit | *(null)* | Users |
| BilledCost | &dollar;4,550.00 | &dollar;0.00 |
| EffectiveCost | &dollar;0.00 | &dollar;379.00 |
| ListCost | &dollar;5,430.00 | &dollar;452.50 |
| ContractedCost | &dollar;5,430.00 | &dollar;452.50 |
| PricingUnit | Count | Users |
| PricingCategory | Standard | Committed |

**Purchase Charge:** [ChargeCategory](#datasets.costandusage.chargecategory) is "Purchase" with [ChargeFrequency](#datasets.costandusage.chargefrequency) "One-Time". The full annual amount is invoiced in a single payment.
* The [*charge period*](#glossary:chargeperiod) spans the entire commitment term: April 1, 2025 through April 1, 2026.
* [BilledCost](#datasets.costandusage.billedcost) is &dollar;4,550.00. This is the [*cash-based*](#glossary:cash-based-accounting) invoiced amount for the annual subscription.
* [EffectiveCost](#datasets.costandusage.effectivecost) is &dollar;0.00. The purchase covers future usage. Cost is recognized on an [*accrual basis*](#glossary:accrual-based-accounting) as usage occurs.
* [ListCost](#datasets.costandusage.listcost) is &dollar;5,430.00 (`50 users x &dollar;9.05/user/month x 12 months`). This represents the cost without the annual discount.
* [ContractedCost](#datasets.costandusage.contractedcost) is &dollar;5,430.00, equal to [ListCost](#datasets.costandusage.listcost). Because no [*negotiated discounts*](#glossary:negotiated-discount) apply (the annual rate is a published [*commitment discount*](#glossary:commitment-discount), not a bilateral negotiation), [ContractedUnitPrice](#datasets.costandusage.contractedunitprice) defaults to [ListUnitPrice](#datasets.costandusage.listunitprice) per the spec. The difference between [ContractedCost](#datasets.costandusage.contractedcost) (&dollar;5,430.00) and [BilledCost](#datasets.costandusage.billedcost) (&dollar;4,550.00) represents the &dollar;880.00 in [*commitment discount*](#glossary:commitment-discount) savings at the point of purchase.
* [ResourceId](#datasets.costandusage.resourceid) equals [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid). The [*commitment discount*](#glossary:commitment-discount) itself is the [*resource*](#glossary:resource) being purchased.
* [CommitmentDiscountCategory](#datasets.costandusage.commitmentdiscountcategory) is "Spend" because the commitment is denominated in dollars, not usage units.
* [CommitmentDiscountQuantity](#datasets.costandusage.commitmentdiscountquantity) is 4,550.00 [CommitmentDiscountUnit](#datasets.costandusage.commitmentdiscountunit) (USD). This is the total spend eligible for consumption over the term.
* [PricingCategory](#datasets.costandusage.pricingcategory) is "Standard". The purchase of the [*commitment discount*](#glossary:commitment-discount) is at the agreed-upon rate.

**Usage Charge (April 2025):** [ChargeCategory](#datasets.costandusage.chargecategory) is "Usage" with [PricingCategory](#datasets.costandusage.pricingcategory) "Committed". The usage is covered by the annual purchase.
* [BilledCost](#datasets.costandusage.billedcost) is &dollar;0.00. No additional invoiced amount. The usage is covered by the purchase charge.
* [EffectiveCost](#datasets.costandusage.effectivecost) is &dollar;379.00. This is the [*accrual-based*](#glossary:accrual-based-accounting) recognized portion of the annual commitment: `&dollar;7.58/user x 50 users`.
* [ListCost](#datasets.costandusage.listcost) is &dollar;452.50 (`50 users x &dollar;9.05/user`). The monthly list cost without the annual discount.
* [ContractedCost](#datasets.costandusage.contractedcost) is &dollar;452.50, equal to [ListCost](#datasets.costandusage.listcost). No [*negotiated discounts*](#glossary:negotiated-discount) apply, so [ContractedUnitPrice](#datasets.costandusage.contractedunitprice) defaults to [ListUnitPrice](#datasets.costandusage.listunitprice).
* The [*commitment discount*](#glossary:commitment-discount) savings appear in the difference between [ContractedCost](#datasets.costandusage.contractedcost) (&dollar;452.50) and [EffectiveCost](#datasets.costandusage.effectivecost) (&dollar;379.00): &dollar;73.50 per month.
* [CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus) is "Used". All 50 seats are occupied.
* [CommitmentDiscountQuantity](#datasets.costandusage.commitmentdiscountquantity) is 379.00 USD. This is the amount of spend consumed from the commitment in this [*charge period*](#glossary:chargeperiod).
* [ResourceId](#datasets.costandusage.resourceid) is the actual [*resource*](#glossary:resource) (the customer's project management site), not the [*commitment discount*](#glossary:commitment-discount).

**Rounding Note:** The per-user rate of &dollar;7.58 is derived from `&dollar;4,550 / 12 months / 50 users` = &dollar;7.5833, rounded to two decimal places. This means `&dollar;7.58 x 50 users x 12 months` = &dollar;4,548.00, which is &dollar;2.00 less than the &dollar;4,550.00 purchase. In a full 12-month dataset, the final month's charge would include a true-up to ensure the sum of [EffectiveCost](#datasets.costandusage.effectivecost) across all usage rows equals the [BilledCost](#datasets.costandusage.billedcost) of the purchase row.

[**CSV Example**](/specification/data/saas_examples/seat_based_saas_annual_a.csv)

## Multi-Unit Usage-Based PaaS: Database-as-a-Service

A PaaS database [*service provider*](#glossary:service%20provider), CloudDB, bills different resource types on different units. The *service provider* offers dedicated database clusters with separate charges for compute, storage, and data transfer.

The *service provider*'s on-demand pricing for this example:

| Service | SKU | Unit Price | Pricing Unit |
| :------ | :-- | ---------: | :----------- |
| CloudDB Clusters | M10 Cluster | &dollar;0.08 | Hours |
| CloudDB Clusters | M30 Cluster | &dollar;0.54 | Hours |
| CloudDB Storage | SSD Storage | &dollar;0.25 | GB |
| CloudDB Data Transfer | Data Transfer Out | &dollar;0.01 | GB |

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

Here is how these charges appear in the data (relevant columns only):

| FOCUS Column | M10 Cluster | M30 Cluster | SSD Storage | Data Transfer Out |
| :--- | :--- | :--- | :--- | :--- |
| ChargeCategory | Usage | Usage | Usage | Usage |
| ChargeFrequency | Usage-Based | Usage-Based | Recurring | Usage-Based |
| ConsumedQuantity | 744 | 744 | 100 | 50 |
| ConsumedUnit | Hours | Hours | GB | GB |
| BilledCost | &dollar;59.52 | &dollar;401.76 | &dollar;25.00 | &dollar;0.50 |
| EffectiveCost | &dollar;59.52 | &dollar;401.76 | &dollar;25.00 | &dollar;0.50 |
| ListCost | &dollar;59.52 | &dollar;401.76 | &dollar;25.00 | &dollar;0.50 |
| ContractedCost | &dollar;59.52 | &dollar;401.76 | &dollar;25.00 | &dollar;0.50 |
| PricingUnit | Hours | Hours | GB | GB |
| PricingCategory | Standard | Standard | Standard | Standard |
| RegionId | us-east-1 | us-east-1 | us-east-1 | us-east-1 |

Key observations:

* Three different [PricingUnit](#datasets.costandusage.pricingunit) values appear within a single *service provider*: Hours (compute), GB (storage), and GB (data transfer). This heterogeneity is typical for PaaS database [*services*](#glossary:service).
* [ChargeFrequency](#datasets.costandusage.chargefrequency) varies by resource type. Compute clusters are "Usage-Based" (metered hourly). Storage is "Recurring" (billed per GB provisioned per month regardless of access patterns). Data transfer is "Usage-Based" (billed on actual volume transferred).
* Compute clusters have [ResourceId](#datasets.costandusage.resourceid) and [ResourceName](#datasets.costandusage.resourcename) values because each cluster is a distinct [*resource*](#glossary:resource). Storage and data transfer are account-level charges with no specific [*resource*](#glossary:resource), so these columns are null.
* All four charges share the [ServiceCategory](#datasets.costandusage.servicecategory) "Databases" but are split across three distinct [ServiceName](#datasets.costandusage.servicename) values: CloudDB Clusters, CloudDB Storage, and CloudDB Data Transfer.
* [RegionId](#datasets.costandusage.regionid) and [RegionName](#datasets.costandusage.regionname) are populated. This *service provider* deploys database clusters to specific regions, and pricing varies by region.
* [BilledCost](#datasets.costandusage.billedcost) and [EffectiveCost](#datasets.costandusage.effectivecost) are equal on all rows because there are no purchase [*charges*](#glossary:charge) covering future usage (see the Credit-Based Consumption example for a full explanation of when these columns diverge).

[**CSV Example**](/specification/data/saas_examples/multi_unit_paas_database_a.csv)

## Flat-Rate SaaS Licensing: Fixed Monthly Subscription

A project management and team communication [*service provider*](#glossary:service%20provider), TeamSpace, offers a single flat-rate subscription. All features and unlimited users are included for a fixed monthly fee with no per-user pricing.

The *service provider*'s pricing for this example:

| Service | SKU | Unit Price | Pricing Unit |
| :------ | :-- | ---------: | :----------- |
| TeamSpace | Pro Unlimited | &dollar;349.00 | Subscriptions |

The *service provider* also offers an annual billing option at &dollar;299.00 per month (billed annually). This example uses the month-to-month option with no annual commitment.

A customer subscribes to the Pro Unlimited plan on a month-to-month basis. During January 2025, the customer's team of 35 people uses the platform.

One charge appears on the January invoice:

* Pro Unlimited: `1 Subscription x &dollar;349.00` = &dollar;349.00

Total [BilledCost](#datasets.costandusage.billedcost): &dollar;349.00

Here is how this charge appears in the data (relevant columns only):

| FOCUS Column | Pro Unlimited |
| :--- | :--- |
| ChargeCategory | Usage |
| ChargeFrequency | Recurring |
| ConsumedQuantity | 1 |
| ConsumedUnit | Subscriptions |
| BilledCost | &dollar;349.00 |
| EffectiveCost | &dollar;349.00 |
| ListCost | &dollar;349.00 |
| ContractedCost | &dollar;349.00 |
| PricingUnit | Subscriptions |
| PricingQuantity | 1 |
| PricingCategory | Standard |

Key observations:

* [ChargeFrequency](#datasets.costandusage.chargefrequency) is "Recurring". The subscription is a fixed monthly fee regardless of usage activity or user count within the [*billing period*](#glossary:billing-period).
* [PricingUnit](#datasets.costandusage.pricingunit) is "Subscriptions" and [PricingQuantity](#datasets.costandusage.pricingquantity) is 1. Unlike per-seat or per-unit models, the entire platform is a single billable unit.
* There is no relationship between [ConsumedQuantity](#datasets.costandusage.consumedquantity) and the number of users. The 35-person team does not affect the charge.
* If the customer chose the annual billing option (&dollar;299.00/month billed annually), this would follow a [*commitment discount*](#glossary:commitment-discount) pattern similar to the Seat-Based SaaS Subscription example above, with a Purchase row for the annual payment and monthly Usage rows for amortized [EffectiveCost](#datasets.costandusage.effectivecost).
* [BilledCost](#datasets.costandusage.billedcost) and [EffectiveCost](#datasets.costandusage.effectivecost) are equal because there are no purchase [*charges*](#glossary:charge) covering future usage (see the Credit-Based Consumption example for a full explanation of when these columns diverge).

[**CSV Example**](/specification/data/saas_examples/flat_rate_saas_licensing_a.csv)

## Annual Commitment Billed Monthly: Seat-Based CRM

A CRM [*service provider*](#glossary:service%20provider), GrowthCRM, offers a seat-based sales platform requiring an annual commitment. Unlike prepaid annual subscriptions, one billing option charges monthly throughout the contract term. The monthly billed rate equals the list price, so no [*commitment discount*](#glossary:commitment-discount) is applied in FOCUS terms.

The *service provider*'s pricing for this example (Professional plan, 10 users):

| Billing Option | Unit Price | Monthly Cost (10 users) | Annual Cost |
| :------------- | ---------: | ----------------------: | ----------: |
| Annual (pay upfront) | &dollar;90.00/user/month | &dollar;900.00 | &dollar;10,800.00 |
| Annual (billed monthly) | &dollar;100.00/user/month | &dollar;1,000.00 | &dollar;12,000.00 |

A customer subscribes to the Professional plan for 10 users, choosing the annual commitment with monthly billing. They pay &dollar;100.00 per user per month with no upfront payment.

One charge appears on the January 2025 invoice:

* Sales Platform Professional: `10 Users x &dollar;100.00` = &dollar;1,000.00

Total [BilledCost](#datasets.costandusage.billedcost): &dollar;1,000.00

Here is how this charge appears in the data (relevant columns only):

| FOCUS Column | Sales Platform Professional |
| :--- | :--- |
| ChargeCategory | Usage |
| ChargeFrequency | Recurring |
| ConsumedQuantity | 10 |
| ConsumedUnit | Users |
| BilledCost | &dollar;1,000.00 |
| EffectiveCost | &dollar;1,000.00 |
| ListCost | &dollar;1,000.00 |
| ContractedCost | &dollar;1,000.00 |
| PricingUnit | Users |
| PricingCategory | Standard |

Key observations:

* [BilledCost](#datasets.costandusage.billedcost), [EffectiveCost](#datasets.costandusage.effectivecost), [ListCost](#datasets.costandusage.listcost), and [ContractedCost](#datasets.costandusage.contractedcost) are all equal at &dollar;1,000.00. Monthly billing on an annual contract produces no divergence between [*cash-based*](#glossary:cash-based-accounting) and [*accrual-based*](#glossary:accrual-based-accounting) costs because there is no upfront payment to amortize.
* [PricingCategory](#datasets.costandusage.pricingcategory) is "Standard" because the billed rate equals the [ListUnitPrice](#datasets.costandusage.listunitprice). The annual contract is a term commitment, not a pricing discount. No [*commitment discount*](#glossary:commitment-discount) columns are populated.
* [ChargeFrequency](#datasets.costandusage.chargefrequency) is "Recurring" because the charge recurs monthly at a fixed per-seat rate regardless of usage activity within the [*billing period*](#glossary:billing-period).
* If the customer chose the annual pay-upfront option (&dollar;90.00/user/month), the &dollar;10.00 per-seat discount would qualify as a [*commitment discount*](#glossary:commitment-discount), following the pattern in the Seat-Based SaaS Subscription example with a Purchase row and amortized [EffectiveCost](#datasets.costandusage.effectivecost).
* This scenario demonstrates that an annual contract does not automatically produce a [*commitment discount*](#glossary:commitment-discount) in FOCUS. The distinguishing factor is whether the commitment provides a price reduction from the standard rate.

[**CSV Example**](/specification/data/saas_examples/annual_commitment_billed_monthly_a.csv)

## Tiered Pricing with Committed Minimum: Email API Platform

A SaaS email API [*service provider*](#glossary:service%20provider), QuickSend, offers tiered plans that include a monthly email allowance. Emails sent within the allowance are covered by the plan fee. Emails exceeding the allowance are billed at a per-email overage rate. The plan minimum functions as a usage-denominated [*commitment discount*](#glossary:commitment-discount) because the customer pays a fixed fee for a quantity of usage units.

The *service provider*'s pricing for this example (Essentials 50K plan):

| Component | Rate | Unit |
| :-------- | ---: | :--- |
| Plan fee (includes 50,000 emails) | &dollar;19.95 | Count |
| Overage | &dollar;0.00133 | Emails |

This example covers two billing periods to show both under-minimum and over-minimum scenarios:

* **January 2025:** The customer sends 30,000 emails, below the 50,000 email allowance. 20,000 emails go unused.
* **February 2025:** The customer sends 65,000 emails, exceeding the allowance by 15,000.

**January charges (under minimum):**

The monthly plan fee of &dollar;19.95 appears as a Purchase charge. Two Usage charges split the commitment between used and unused portions:

* Purchase: &dollar;19.95 (plan fee covering 50,000 emails)
* Used: 30,000 emails, [EffectiveCost](#datasets.costandusage.effectivecost) = &dollar;11.97 (`30,000 / 50,000 x &dollar;19.95`)
* Unused: 20,000 emails, [EffectiveCost](#datasets.costandusage.effectivecost) = &dollar;7.98 (`20,000 / 50,000 x &dollar;19.95`)

Total [BilledCost](#datasets.costandusage.billedcost): &dollar;19.95

Here is how the January charges appear in the data (relevant columns only):

| FOCUS Column | Purchase | Usage (Used) | Usage (Unused) |
| :--- | :--- | :--- | :--- |
| ChargeCategory | Purchase | Usage | Usage |
| ChargeFrequency | Recurring | Usage-Based | Usage-Based |
| CommitmentDiscountCategory | Usage | Usage | Usage |
| CommitmentDiscountStatus | *(null)* | Used | Unused |
| CommitmentDiscountQuantity | 50,000 | 30,000 | 20,000 |
| CommitmentDiscountUnit | Emails | Emails | Emails |
| ConsumedQuantity | *(null)* | 30,000 | *(null)* |
| ConsumedUnit | *(null)* | Emails | *(null)* |
| BilledCost | &dollar;19.95 | &dollar;0.00 | &dollar;0.00 |
| EffectiveCost | &dollar;0.00 | &dollar;11.97 | &dollar;7.98 |
| ListCost | &dollar;19.95 | &dollar;39.90 | &dollar;26.60 |
| ContractedCost | &dollar;19.95 | &dollar;39.90 | &dollar;26.60 |
| PricingUnit | Count | Emails | Emails |
| PricingCategory | Standard | Committed | Committed |

**February charges (over minimum):**

The customer uses all 50,000 plan emails plus 15,000 overage emails:

* Purchase: &dollar;19.95 (plan fee covering 50,000 emails)
* Used: 50,000 emails, [EffectiveCost](#datasets.costandusage.effectivecost) = &dollar;19.95 (full allowance consumed)
* Overage: 15,000 emails at &dollar;0.00133 = &dollar;19.95 (standard pricing, not part of commitment)

Total [BilledCost](#datasets.costandusage.billedcost): &dollar;39.90

Here is how the February charges appear in the data (relevant columns only):

| FOCUS Column | Purchase | Usage (Used) | Usage (Overage) |
| :--- | :--- | :--- | :--- |
| ChargeCategory | Purchase | Usage | Usage |
| ChargeFrequency | Recurring | Usage-Based | Usage-Based |
| CommitmentDiscountCategory | Usage | Usage | *(null)* |
| CommitmentDiscountStatus | *(null)* | Used | *(null)* |
| CommitmentDiscountQuantity | 50,000 | 50,000 | *(null)* |
| CommitmentDiscountUnit | Emails | Emails | *(null)* |
| ConsumedQuantity | *(null)* | 50,000 | 15,000 |
| ConsumedUnit | *(null)* | Emails | Emails |
| BilledCost | &dollar;19.95 | &dollar;0.00 | &dollar;19.95 |
| EffectiveCost | &dollar;0.00 | &dollar;19.95 | &dollar;19.95 |
| ListCost | &dollar;19.95 | &dollar;66.50 | &dollar;19.95 |
| ContractedCost | &dollar;19.95 | &dollar;66.50 | &dollar;19.95 |
| PricingUnit | Count | Emails | Emails |
| PricingCategory | Standard | Committed | Standard |

Key observations:

* [CommitmentDiscountCategory](#datasets.costandusage.commitmentdiscountcategory) is "Usage" on all commitment-related rows. The plan minimum is denominated in email quantity (50,000 emails), not a dollar amount. This distinguishes it from the "Spend" category in the Seat-Based SaaS Subscription example.
* [CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus) shows "Used" and "Unused" on Usage rows. In January, the customer only consumed 30,000 of 50,000 emails, so the remaining 20,000 generate an "Unused" row. The Unused row has [BilledCost](#datasets.costandusage.billedcost) of &dollar;0.00 but [EffectiveCost](#datasets.costandusage.effectivecost) of &dollar;7.98, representing waste from the commitment.
* The Purchase row has [BilledCost](#datasets.costandusage.billedcost) of &dollar;19.95 and [EffectiveCost](#datasets.costandusage.effectivecost) of &dollar;0.00. This follows the same pattern as the Seat-Based SaaS Subscription: the purchase captures the [*cash-based*](#glossary:cash-based-accounting) cost, while [*accrual-based*](#glossary:accrual-based-accounting) cost is recognized on the Usage rows.
* The overage row in February has no [*commitment discount*](#glossary:commitment-discount) columns populated. Overage emails are billed at the standard per-email rate and are not part of the commitment.
* [ContractedUnitPrice](#datasets.costandusage.contractedunitprice) and [ListUnitPrice](#datasets.costandusage.listunitprice) are both &dollar;0.00133 on all Usage rows. Because no [*negotiated discounts*](#glossary:negotiated-discount) apply, [ContractedUnitPrice](#datasets.costandusage.contractedunitprice) defaults to [ListUnitPrice](#datasets.costandusage.listunitprice) per the spec. The [*commitment discount*](#glossary:commitment-discount) savings are reflected in the difference between [ContractedCost](#datasets.costandusage.contractedcost) and [EffectiveCost](#datasets.costandusage.effectivecost), not in [ContractedUnitPrice](#datasets.costandusage.contractedunitprice).
* [ListCost](#datasets.costandusage.listcost) and [ContractedCost](#datasets.costandusage.contractedcost) on Usage rows represent the market value of those emails at the per-email rate: `&dollar;0.00133 x 30,000` = &dollar;39.90 for the January Used row. These values exceed [BilledCost](#datasets.costandusage.billedcost) (&dollar;0.00) because the usage is covered by the plan fee, not billed individually. The gap between [ListCost](#datasets.costandusage.listcost) and [EffectiveCost](#datasets.costandusage.effectivecost) shows the [*commitment discount*](#glossary:commitment-discount) benefit per row.
* [PricingUnit](#datasets.costandusage.pricingunit) is "Count" on the Purchase row because the plan fee is a single monthly purchase, not denominated in the usage unit (emails). On Usage rows, [PricingUnit](#datasets.costandusage.pricingunit) is "Emails" because those rows are priced per email.
* [ChargeFrequency](#datasets.costandusage.chargefrequency) is "Recurring" on the Purchase rows (the plan fee recurs monthly). On the Usage rows, [ChargeFrequency](#datasets.costandusage.chargefrequency) is "Usage-Based" for both Used and Unused rows because the amounts vary based on actual email consumption each period.

[**CSV Example**](/specification/data/saas_examples/tiered_pricing_committed_minimum_a.csv)
