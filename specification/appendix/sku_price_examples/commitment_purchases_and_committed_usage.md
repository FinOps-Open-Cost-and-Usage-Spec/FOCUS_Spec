# Commitment Pricing

A [*commitment discount*](#glossary:commitment-discount) appears in a [*price list*](#glossary:price-list) as two different kinds of record: the fee charged to acquire it, and the rate that consumption is priced at once it is held. [ChargeCategory](#datamodel.skuprice.chargecategory) separates them, and it governs which of the purchase-describing columns carry values.

Aura Web offers two commitment instruments over the same standard virtual machine, each under three payment models. A reservation commits to a resource and is bought as a one-year fee. A flexible spend plan commits to an amount of spend and is bought as a unit price on the committed amount. The on-demand rate for the same machine is 0.384000 per hour, and every figure below is measured against it.

## Commitment Purchases

[**CSV Example**](/specification/data/sku_price_examples/sku_price_commitment_purchases.csv)

Note the following details in the example dataset:

* All six records carry a ChargeCategory of "Purchase", which identifies them as fees to acquire something rather than rates for consuming it. [PurchaseDurationType](#datamodel.skuprice.purchasedurationtype) carries "1 Year" and [PurchasePaymentModel](#datamodel.skuprice.purchasepaymentmodel) carries the settlement structure.
* Each payment model is a separate record with its own [SkuPriceId](#datamodel.skuprice.skupriceid), not one record with a null payment model. PurchasePaymentModel is not a member of the composite key, so two variants sharing a SKU Price ID would collide on row uniqueness. The same applies to term lengths: a one-year and a three-year commitment are separate records with separate SKU Price IDs.
* The reservation fees are 1893.600000, 1998.800000, and 2104.000000 for All Upfront, Partial Upfront, and No Upfront. Each states the whole one-year obligation as a single figure, and [PurchaseDurationType](#datamodel.skuprice.purchasedurationtype) states the term that figure covers. [PricingUnit](#datamodel.skuprice.pricingunit) names the unit the reservation covers rather than the denominator of the fee: a reservation of compute hours carries "Hours", and the fee is read against the term rather than against one hour. How the figure is collected is what the payment model names, and it is not visible in the price.
* The spend plan fees are 0.900000, 0.950000, and 1.000000. A spend plan is bought by the unit of committed spend rather than as a lump sum, so its [UnitPrice](#datamodel.skuprice.unitprice) is what one unit of commitment costs: under All Upfront a customer pays 0.90 to acquire 1.00 of committed spend, and under No Upfront pays the full 1.00. PricingUnit carries "USD" because the plan commits to an amount of spend rather than to a quantity of a resource, and [PricingCurrency](#datamodel.skuprice.pricingcurrency) carries "USD" because that spend is settled in United States dollars. The two columns answer different questions on this record: what the commitment is measured in, and what it is paid in.
* The two instruments carry different [SkuId](#datamodel.skuprice.skuid) values because they are different things to buy. The reservation records share "AURAWEB-COMPUTE-RESERVATION-VM-STD" and the spend plan records share "AURAWEB-COMMITMENT-FLEXSPEND".
* Both instruments price the same underlying machine, but neither purchase record names it. A purchase fee is a price for the instrument, not for the resource, and the link between the two lives in the usage records described below.

## Committed Usage Alongside Commitment Purchases

The rate that covered consumption is priced at is a separate record from the fee. This extract carries the on-demand record, the six covered usage records, and the six purchase records, so the full comparison is visible in one place.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_committed_usage_alongside_purchases.csv)

Note the following details in the example dataset:

* The seven usage records carry a ChargeCategory of "Usage" and a null PurchaseDurationType and PurchasePaymentModel, even though six of them exist only because a commitment was purchased. The six purchase records in the same extract carry both values. The columns describe the purchase, and a rate is not a purchase.
* This is deliberate rather than an omission. A price list is published before consumption happens, so at the time a rate is published there is no way to know whether a given unit of consumption will end up covered by a commitment. Whether coverage was actually applied is visible in [EffectiveCost](#datamodel.costandusage.effectivecost) and [BilledCost](#datamodel.costandusage.billedcost) in the [Cost and Usage](#datamodel.costandusage) dataset, which record what happened, rather than in the price, which records what is on offer.
* All seven usage records carry a UnitPrice of 0.384000. The commitment does not change what an hour of this machine is priced at; it changes what the customer ultimately pays for that hour, and that is settled through the purchase rather than through the rate. A consumer that reads UnitPrice alone on a covered record reads the on-demand rate, which is the correct answer to the question UnitPrice asks.
* Because neither purchase column is populated on a usage record and UnitPrice is identical across them, a covered rate is distinguished by its SKU Price ID, which names the commitment it belongs to. Publishing all seven under one SKU Price ID would collide on row uniqueness and would leave a consumer no way to tell them apart.
* `x_EffectiveUnitPrice` is a [*custom column*](#glossary:custom-column) carrying the hourly rate a customer resolves to once the purchase is amortized across the term. It is not a FOCUS column, and it is present here because the saving a commitment produces is not expressible in the FOCUS columns of a single record. It carries zero on a purchase record, where no hourly consumption is priced, and the on-demand rate on the uncovered record. A data generator that omits the column publishes the same seven rates with the saving recoverable only by combining a usage record with its purchase record.
* The resulting one-year cost for 8,760 covered hours, against 3,363.84 at the on-demand rate:

| Commitment | Payment model | Purchase UnitPrice | Effective hourly rate | One-year total | Reduction |
| :--- | :--- | ---: | ---: | ---: | ---: |
| Reservation | All Upfront | 1893.600000 | 0.216164 | 1,893.60 | 43.7% |
| Reservation | Partial Upfront | 1998.800000 | 0.228174 | 1,998.80 | 40.6% |
| Reservation | No Upfront | 2104.000000 | 0.240183 | 2,104.00 | 37.5% |
| Flexible spend plan | All Upfront | 0.900000 | 0.259200 | 2,270.59 | 32.5% |
| Flexible spend plan | Partial Upfront | 0.950000 | 0.273600 | 2,396.74 | 28.8% |
| Flexible spend plan | No Upfront | 1.000000 | 0.288000 | 2,522.88 | 25.0% |

* The reservation totals are the purchase fees themselves, divided across 8,760 hours to reach the effective rate. A reservation is bought once and covers the term, so the fee is the whole cost.
* The spend plan reaches its totals differently. The plan prices covered consumption at 0.288000 per hour, a 25 percent reduction on the on-demand rate, which over a year commits the customer to 2,522.88 units of spend. The payment model then discounts the acquisition of those units, at 0.90, 0.95, or 1.00 each, giving 2,270.59, 2,396.74, and 2,522.88. The plan discount and the payment model discount compound, and only the second of the two is visible in the purchase record's UnitPrice.
* Across both instruments the pattern is a larger reduction the more of the obligation is settled upfront, and a larger reduction for committing to a specific resource than to an amount of spend. The least committed option, a No Upfront spend plan, still reduces the rate by a quarter.
