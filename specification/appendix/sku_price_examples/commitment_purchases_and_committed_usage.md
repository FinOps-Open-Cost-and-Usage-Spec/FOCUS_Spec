# Commitment Pricing

A [*commitment discount*](#glossary:commitment-discount) appears in a [*price list*](#glossary:price-list) as two different kinds of record: the fee charged to acquire it, and the rate that consumption is priced at once it is held. [ChargeCategory](#datamodel.skuprice.chargecategory) separates them, and it governs which of the purchase-describing columns carry values.

Aura Web offers two commitment instruments, each under three payment models. A reservation commits to a specific resource, the standard virtual machine, and is bought as a one-year fee. A flexible spend plan commits to an amount of spend rather than to a resource, and is bought at face value, one unit of price for each unit of committed spend. The on-demand rate for the standard machine is 0.384000 per hour.

## Commitment Purchases

[**CSV Example**](/specification/data/sku_price_examples/sku_price_commitment_purchases.csv)

Note the following details in the example dataset:

* All six records carry a ChargeCategory of "Purchase", which identifies them as fees to acquire something rather than rates for consuming it. [PurchaseDurationType](#datamodel.skuprice.purchasedurationtype) carries "1 Year" and [PurchasePaymentModel](#datamodel.skuprice.purchasepaymentmodel) carries the settlement structure.
* Each payment model is a separate record with its own [SkuPriceId](#datamodel.skuprice.skupriceid), not one record with a null payment model. PurchasePaymentModel is not a member of the composite key, so two variants sharing a SKU Price ID would collide on row uniqueness. The same applies to term lengths: a one-year and a three-year commitment are separate records with separate SKU Price IDs.
* The reservation fees are 1893.600000, 1998.800000, and 2104.000000 for "All Upfront", "Partial Upfront", and "No Upfront". [PricingUnit](#datamodel.skuprice.pricingunit) is "Units", so each fee is the price of one reservation, and PurchaseDurationType of "1 Year" states the term that reservation runs for. The payment model names how the fee is collected, and for a reservation it also changes the fee: the more of it is paid at the start, the lower it is.
* The spend plan fees are 1.000000 under all three payment models. A spend plan is bought by the unit of committed spend rather than as a lump sum, so its [UnitPrice](#datamodel.skuprice.unitprice) is what one unit of commitment costs, and a customer pays 1.00 to acquire 1.00 of committed spend whichever payment model applies. Unlike the reservation, the payment model changes only when that amount is paid, not how much. The three records are still separate records with separate SKU Price IDs, because they are different offers even though they carry the same price. PricingUnit carries "USD" because the plan commits to an amount of spend rather than to a quantity of a resource, and [PricingCurrency](#datamodel.skuprice.pricingcurrency) carries "USD" because that spend is settled in United States dollars. The two columns answer different questions on this record: what the commitment is measured in, and what it is paid in.
* The two instruments carry different [SkuId](#datamodel.skuprice.skuid) values because they are different things to buy. The reservation records share "AURAWEB-COMPUTE-RESERVATION-VM-STD" and the spend plan records share "AURAWEB-COMMITMENT-FLEXSPEND".
* Neither purchase record names what it covers. A purchase fee is a price for the instrument, not for the resource. For the reservation, the machine appears on the covered usage records described below.

## Committed Usage Alongside Commitment Purchases

The rate that covered consumption is priced at is a separate record from the fee. This extract carries the on-demand record, the three reservation purchase records, and the three usage records covered by the reservation, so the fee and rate records for the reservation are visible in one place.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_committed_usage_alongside_purchases.csv)

Note the following details in the example dataset:

* The four usage records carry a ChargeCategory of "Usage" and a null PurchaseDurationType and PurchasePaymentModel, even though three of them exist only because a reservation was purchased. The three purchase records in the same extract carry both values. The columns describe the purchase, and a rate is not a purchase.
* This is deliberate rather than an omission. A price list is published before consumption happens, so at the time a rate is published there is no way to know whether a given unit of consumption will end up covered by a commitment. Whether coverage was actually applied is visible in [EffectiveCost](#datamodel.costandusage.effectivecost) and [BilledCost](#datamodel.costandusage.billedcost) in the [Cost and Usage](#datamodel.costandusage) dataset, which record what happened, rather than in the price, which records what is on offer.
* All four usage records carry a UnitPrice of 0.384000. The reservation does not change what an hour of this machine is priced at; it changes what the customer ultimately pays for that hour. A consumer that reads UnitPrice alone on a covered record reads the on-demand rate, which is the correct answer to the question UnitPrice asks.
* UnitPrice is identical across the four usage records, but each is a distinct price offering and therefore carries its own SKU Price ID.
* The price list does not state what a reservation saves. Both the purchase prices and the covered UnitPrice of 0.384000 are visible, but how much covered consumption one reservation absorbs is a term of the commitment, not a price, and no column in this dataset carries it. The saving becomes visible only in EffectiveCost in the Cost and Usage dataset, once consumption has been covered.
