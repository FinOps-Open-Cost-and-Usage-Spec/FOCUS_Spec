# Commitment Discounts

## Examples: Commitment Discount Scenarios

A [_commitment discount_](#glossary:commitment-discount) is a billing discount model that offers reduced rates on preselected [_SKUs_](#glossary:sku) in exchange for an obligated usage or spend amount over a specified [_period_](#glossary:period). _Commitment discounts_ typically consist of purchase and usage records within cost and usage datasets.

Usage-based _commitment discounts_ obligate a customer to a predetermined amount of usage over a specified [_period_](#glossary:period). In some cases, usage-based _commitment discounts_ also feature [_commitment discount flexibility_](#glossary:commitment-discount-flexibility) which may expand the types of [_resources_](#glossary:resource) that a _commitment discount_ can cover. It is important to note when mixing _commitment discounts_ with and without _commitment discount flexibility_, the [CommitmentDiscountUnit](#datasets.costandusage.commitmentdiscountunit) should reflect this difference.

Spend-based commitment discounts obligate a customer to a predetermined amount of spend over a specified [_period_](#glossary:period). In the usage examples below, each [_row_](#glossary:row) measures the monetary amount of the hourly commit consumed by the _commitment discount_, so the CommitmentDiscountUnit chosen is "USD", or the [_billing currency_](#glossary:billing-currency).

## Purchasing

While customers are bound to the [_period_](#glossary:period) of a _commitment discount_, service providers offer some or all of the following payment options before and/or during the _period_:

* _All Upfront_ - The _commitment discount_ is paid in full before the _period_ begins.
* _No Upfront_ - The _commitment discount_ is paid on a repeated basis, typically over each [_billing period_](#glossary:billing-period) of the _period_.
* _Partial Upfront_ - Some of the _commitment discount_ is paid before the _period_ begins, and the rest is paid repeatedly over the _period_.

For example, if a customer buys a 1-year, spend-based _commitment discount_ with a &dollar;1.00 hourly commit and pays with the partial option, the _commitment discount's_ payment consists of a one-time purchase in the beginning of the _period_ _and_ monthly recurring purchases with the following totals:

1. _One-Time_ - &dollar;4,380 (`24 hours * 365 days * &dollar;1.00 * 0.5`)
2. _Recurring_ - &dollar;182.50 (`24 hours * 365 days * &dollar;1.00 / 12 months`)

## Usage

Commitment discounts follow a "use-it-or-lose-it" model where the [_amortization_](#glossary:amortization) of a _commitment discount's_ purchase applies evenly to eligible _resources_ over each [_charge period_](#glossary:charge-period) of the _period_.

For example, if a customer buys a spend-based _commitment discount_ with a &dollar;1.00 hourly commit in January (31 days), only &dollar;1.00 is eligible for consumption for each hourly _charge period_. If a customer has eligible _resources_ running during this _charge period_, an amount of up to &dollar;1.00 will be allocated to these _resources_. Conversely, if a customer does not have eligible _resources_ running that fully take advantage of this &dollar;1.00 during this _charge period_, then some or all of this amount will go to waste.

## Commitment Discounts in FOCUS

Within the FOCUS specification, the following examples demonstrate how a _commitment discount_ appears across various payment and usage scenarios.

### Purchase _Rows_

All _commitment discount_ purchases appear with a positive [BilledCost](#datasets.costandusage.billedcost), [PricingCategory](#datasets.costandusage.pricingcategory) as "Standard", and with the _commitment discount's_ id populating both the [ResourceId](#datasets.costandusage.resourceid) and [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) value. One-time purchases appear as a single record with [ChargeCategory](#datasets.costandusage.chargecategory) as "Purchase", [ChargeFrequency](#datasets.costandusage.chargefrequency) as "One-Time", and the total quantity and units for _commitment discount's_ _period_ reflected as [CommitmentDiscountQuantity](#datasets.costandusage.commitmentdiscountquantity) and CommitmentDiscountUnit, respectively.

Recurring purchases are allocated across all corresponding _charge periods_ of the _period_ when ChargeCategory is "Purchase", ChargeFrequency is "Recurring", and CommitmentDiscountQuantity and CommitmentDiscountUnit are reflected only for that _charge period_.

Using the same _commitment discount_ example as above with a one-year, spend-based _commitment discount_ with a &dollar;1.00 hourly commit purchased on Jan 1, 2023, various purchase options are available:

#### Scenario #1: All Upfront

The entire _commitment discount_ is billed _once_ during the first _charge period_ of the _period_ for &dollar;8,670 (derived as `24 hours * 365 days * &dollar;1.00`).

[CSV Example](/specification/data/commitment_discount_scenarios/commitment_discount_purchase_scenario_1.csv)

#### Scenario #2: No Upfront

The _commitment discount_ is billed across all 8,760 (`24 hours * 365 days`) _charge periods_ of the _period_ with &dollar;1.00 allocated to each _charge period_ over the _period_.

[CSV Example](/specification/data/commitment_discount_scenarios/commitment_discount_purchase_scenario_2.csv)

This example shows the first three hourly rows of 8,760 total rows that are all the same except for the incrementing monthly and hourly timeframes denoted in the Billing Period and Charge Period columns, respectively.

#### Scenario #3: Partial Upfront

With a 50/50 split, half of the commitment is billed _once_ during the first _charge period_ of the _period_ for &dollar;4,380 (derived as `24 hours * 182.5 days * &dollar;1.00`), and the other half is billed across each _charge period_ over the commitment _period_, derived as (`&dollar;1.00 * 8,760 hours * 0.5`). Amortized costs incur half of the amount (i.e., &dollar;0.50) from the one-time purchase and the other half from the recurring purchase.

[CSV Example](/specification/data/commitment_discount_scenarios/commitment_discount_purchase_scenario_3.csv)

This example shows the first three hourly rows of 8,760 total rows that are all the same except for the incrementing monthly and hourly timeframes denoted in the Billing Period and Charge Period columns, respectively.

### Usage _Rows_

_Amortization_ of _commitment discounts_ occur similarly regardless of how _commitment discount_ purchases are made. The same usage-based or spend-based amount is applied evenly across all _charge periods_ and potentially allocated to eligible _resources_. Continuing with the same _commitment discount_ example, a one-year, spend-based _commitment discount_ with a &dollar;1.00 hourly commit and 1 _resource_ (for simplicity) yields 4 types of scenarios that can occur during a _charge period_:

* Scenario #1: An eligible _resource_ fully consumes the allocated amount (100% utilization)
* Scenario #2: No eligible _resource_ consumes the allocated amount (0% utilization)
* Scenario #3: An eligible _resource_ partially consumes the allocated amount (75% utilization)
* Scenario #4: An eligible _resource_ fully consumes the &dollar;1.00 hourly commit with an overage (100% utilization + overage)

#### Scenario #1: An eligible _resource_ fully consumes the allocated amount (100% utilization)

In this scenario, one eligible _resource_ runs for the full hour and consumes &dollar;1.00, so one _row_ allocated to the _resource_ is produced.

[CSV Example](/specification/data/commitment_discount_scenarios/commitment_discount_usage_scenario_1.csv)

#### Scenario #2: No eligible _resource_ consumes the allocated amount (0% utilization)

In this situation, the full eligible, &dollar;1.00 amount remained unutilized and results in 1 unused _row_. In this scenario, it is important to note that while CommitmentDiscountQuantity is not because &dollar;1 was still drawn down by the _commitment discount_ even though, no _resource_ was allocated, so [ConsumedQuantity](#datasets.costandusage.consumedquantity) and [ConsumedUnit](#datasets.costandusage.consumedunit) are null.

[CSV Example](/specification/data/commitment_discount_scenarios/commitment_discount_usage_scenario_2.csv)

#### Scenario #3: An eligible _resource_ partially consumes the allocated amount (75% utilization)

In this scenario, one eligible _resource_ runs for the full hour and consumes &dollar;0.75 of the &dollar;1.00 allocation. One _row_ shows &dollar;0.75 to a _resource_, and the other _row_ shows that &dollar;0.25 was unused.

[CSV Example](/specification/data/commitment_discount_scenarios/commitment_discount_usage_scenario_3.csv)

#### Scenario #4: An eligible _resource_ fully consumes the &dollar;1.00 hourly commit with an overage (100% utilization + overage)

In this scenario, one eligible _resource_ runs for the full hour and is charged &dollar;1.50. One _row_ shows that &dollar;1.00 was _amortized_ from the _commitment discount_, and the other shows that &dollar;0.50 was charged as standard, on-demand spend.

[CSV Example](/specification/data/commitment_discount_scenarios/commitment_discount_usage_scenario_4.csv)
