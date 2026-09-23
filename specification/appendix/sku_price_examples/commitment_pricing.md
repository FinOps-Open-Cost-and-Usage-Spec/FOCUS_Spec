# Commitment Pricing

[*Commitment discount*](#glossary:commitment-discount) appear in a [*price list*](#glossary:price-list) as two different kinds of records: commitment purchase SKU Price records, and usage SKU Price records for usage covered by those commitments. [ChargeCategory](#datamodel.skuprice.chargecategory) separates them, and it governs which of the purchase-describing columns carry values.

Aura Web offers two commitment instruments, each under three payment models. A reservation commits to a specific resource, the standard virtual machine, and is bought as a one-year fee. A flexible spend plan commits to an amount of spend rather than to a resource, and is bought at face value, one unit of price for each unit of committed spend. The on-demand rate for the standard machine is 0.384000 per hour.

## Commitment Purchases

[**CSV Example**](/specification/data/sku_price_examples/sku_price_commitment_purchases.csv)

Note the following details in the example dataset:

* All six records carry a ChargeCategory of "Purchase", which identifies them as fees to acquire something rather than rates for consuming it. [PurchaseDurationType](#datamodel.skuprice.purchasedurationtype) carries "1 Year" and [PurchasePaymentModel](#datamodel.skuprice.purchasepaymentmodel) carries the settlement structure.
* Each payment model is a separate record with its own [SkuPriceId](#datamodel.skuprice.skupriceid).
* The reservation fees are 1893.600000, 1998.800000, and 2104.000000 for "All Upfront", "Partial Upfront", and "No Upfront". [PricingUnit](#datamodel.skuprice.pricingunit) is "Units", so each fee is the price of one reservation, and PurchaseDurationType of "1 Year" states the term that reservation runs for. The payment model names how the fee is collected, and for a reservation it also changes the fee: the more of it is paid at the start, the lower it is.
* The spend plan fees are 1.000000 under all three payment models. A spend plan is bought by the unit of committed spend rather than as a lump sum, so its [UnitPrice](#datamodel.skuprice.unitprice) is what one unit of commitment costs, and a customer pays 1.00 to acquire 1.00 of committed spend whichever payment model applies. Unlike the reservation, the payment model changes only when that amount is paid, not how much. The three records are still separate records with separate SKU Price IDs, because they are different offers even though they carry the same price. PricingUnit carries "USD" because the plan commits to an amount of spend rather than to a quantity of a resource, and [PricingCurrency](#datamodel.skuprice.pricingcurrency) carries "USD" because that spend is settled in United States dollars. The two columns answer different questions on this record: what the commitment is measured in, and what it is paid in.
* The two instruments carry different [SkuId](#datamodel.skuprice.skuid) values because they are different things to buy. The reservation records share "AURAWEB-COMPUTE-RESERVATION-VM-STD" and the spend plan records share "AURAWEB-COMMITMENT-FLEXSPEND".

## Committed Usage Alongside Commitment Purchases

The rate that covered consumption is priced at is a separate record from the fee. This extract carries the on-demand record, the three reservation purchase records, and the three usage records covered by the reservation, so the fee and rate records for the reservation are visible in one place.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_committed_usage_alongside_purchases.csv)

Note the following details in the example dataset:

* The four usage records carry a ChargeCategory of "Usage" and a null PurchaseDurationType and PurchasePaymentModel, even though three of them exist only because a reservation was purchased. The three purchase records in the same extract carry both values. The columns describe the purchase, and a rate is not a purchase.
* This is deliberate rather than an omission. A price list is published before consumption happens, so at the time a rate is published there is no way to know whether a given unit of consumption will end up covered by a commitment. Whether coverage was actually applied is visible in [EffectiveCost](#datamodel.costandusage.effectivecost) and [BilledCost](#datamodel.costandusage.billedcost) in the [Cost and Usage](#datamodel.costandusage) dataset, which record what happened, rather than in the price, which records what is on offer.
* All four usage records carry a UnitPrice of 0.384000. The reservation does not change what an hour of this machine is priced at; it changes what the customer ultimately pays for that hour. A consumer that reads UnitPrice alone on a covered record reads the on-demand rate, which is the correct answer to the question UnitPrice asks.
* UnitPrice is identical across the four usage records, but each is a distinct price offering and therefore carries its own SKU Price ID.
* The price list does not state what a reservation saves. Both the purchase prices and the covered UnitPrice of 0.384000 are visible, but how much covered consumption one reservation absorbs is a term of the commitment, not a price, and no column in this dataset carries it. The saving becomes visible only in EffectiveCost in the Cost and Usage dataset, once consumption has been covered.

---

**# Commitment Pricing**

A [**commitment discount**](#glossary:commitment-discount) appears in a [**price list**](#glossary:price-list) as two different kinds of record: the fee charged to acquire the commitment, and the rate at which consumption associated with the commitment is priced. [ChargeCategory](#datamodel.skuprice.chargecategory) separates them, and it governs which of the purchase-describing columns carry values.

Aura Web offers two commitment instruments, each under three payment models. A reservation commits to a specific resource, the standard virtual machine, and is bought for a one-year term. A flexible spend plan commits to an amount of spend rather than to a resource, and is bought at face value, one unit of price for each unit of committed spend. The on-demand rate for the standard machine is 0.384000 per hour.

**## Commitment Purchases**

[****CSV Example****](/specification/data/sku_price_examples/sku_price_commitment_purchases.csv)

Note the following details in the example dataset:

* All six records have a ChargeCategory of "Purchase", identifying them as commitment purchase records. [PurchaseDurationType](#datamodel.skuprice.purchasedurationtype) is "1 Year", and [PurchasePaymentModel](#datamodel.skuprice.purchasepaymentmodel) identifies the payment model.

* Each payment model is represented by a separate record with its own [SkuPriceId](#datamodel.skuprice.skupriceid). The records therefore represent distinct price offerings even when other attributes, including UnitPrice, are the same.

* The reservation purchase prices are 1893.600000, 1998.800000, and 2104.000000 for "All Upfront", "Partial Upfront", and "No Upfront", respectively. [PricingUnit](#datamodel.skuprice.pricingunit) is "Units", so [UnitPrice](#datamodel.skuprice.unitprice) represents the price of one reservation. [PurchaseDurationType](#datamodel.skuprice.purchasedurationtype) specifies the one-year term, while [PurchasePaymentModel](#datamodel.skuprice.purchasepaymentmodel) specifies the payment model. In this example, the payment model affects the UnitPrice of the reservation purchase.

* The spend plan purchase price is 1.000000 for all three payment models. The plan is purchased per unit of committed spend, so [UnitPrice](#datamodel.skuprice.unitprice) represents the price of one unit of commitment. In this example, the payment model does not affect the UnitPrice, so all three payment models have the same UnitPrice while remaining separate price offerings with distinct SkuPriceId values. [PricingUnit](#datamodel.skuprice.pricingunit) is "USD", representing the unit in which the commitment is measured, and [PricingCurrency](#datamodel.skuprice.pricingcurrency) is also "USD", representing the currency in which the purchase is priced. These attributes describe different aspects of the price: the unit of the commitment and the currency of the price.

* The two commitment instruments have different [SkuId](#datamodel.skuprice.skuid) values because they represent different products. The reservation records share "AURAWEB-COMPUTE-RESERVATION-VM-STD", while the spend plan records share "AURAWEB-COMMITMENT-FLEXSPEND".

**## Committed Usage Alongside Commitment Purchases**

The rate for consumption covered by a commitment is represented by a separate record from the commitment purchase fee. This extract includes the on-demand usage record, the three reservation purchase records, and the three usage records associated with those reservations, allowing the purchase and usage records for the reservation to be viewed together.

[****CSV Example****](/specification/data/sku_price_examples/sku_price_committed_usage_alongside_purchases.csv)

Note the following details in the example dataset:

* The four usage records have a ChargeCategory of "Usage" and null PurchaseDurationType and PurchasePaymentModel. The purchase records in the same extract have values for both attributes. PurchaseDurationType and PurchasePaymentModel describe the commitment purchase and therefore do not apply to usage records.

* This separation reflects the distinction between pricing information and the application of a commitment to consumption. A price list describes available rates and purchase offers before consumption occurs. Whether a particular consumption record is covered by a commitment is reflected in the [EffectiveCost](#datamodel.costandusage.effectivecost) and [BilledCost](#datamodel.costandusage.billedcost) attributes in the [Cost and Usage](#datamodel.costandusage) dataset, rather than in the price record.

* All four usage records have a UnitPrice of 0.384000. For the three records representing usage covered by a reservation, ContractId is null, so UnitPrice represents the standard public list price for the resource. The commitment does not reduce this UnitPrice; the effect of applying the commitment is reflected in the resulting cost, including [EffectiveCost](#datamodel.costandusage.effectivecost), rather than in UnitPrice.

* Although the UnitPrice is identical across the four usage records, each record represents a distinct price offering and therefore has its own [SkuPriceId](#datamodel.skuprice.skupriceid). The distinct SkuPriceId values associate each usage record with the commitment that covers it.

* The price list does not specify the amount of consumption covered by a reservation or the resulting savings. Those are terms of the commitment rather than attributes of the usage price. The purchase price and UnitPrice are available in the price list, while the resulting cost of covered consumption is reflected in EffectiveCost in the Cost and Usage dataset.
