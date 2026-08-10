# Purchase Fees and Commitment Rates

A [*commitment discount*](#glossary:commitment-discount) appears in a [*price list*](#glossary:price-list) as two different kinds of record: the fee charged to acquire it, and the rate that consumption is priced at once it is held. [ChargeCategory](#datamodel.skuprice.chargecategory) separates them, and it governs which of the purchase-describing columns carry values.

## Purchase Fees

Aura Web offers a one-year reservation for its standard virtual machine under two payment models, and a one-year flexible spend plan under two more.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_purchase_fees.csv)

Note the following details in the example dataset:

* All four records carry a ChargeCategory of "Purchase", which identifies them as fees to acquire something rather than rates for consuming it. [PurchaseDurationType](#datamodel.skuprice.purchasedurationtype) carries "1 Year" and [PurchasePaymentModel](#datamodel.skuprice.purchasepaymentmodel) carries the settlement structure.
* The reservation is offered as two records, one for each payment model. Under "All Upfront" the whole obligation is settled by a single fee of 2354.690000. Under "Partial Upfront" an initial fee of 1244.160000 settles part of it, and the rest is recovered through the hourly rate described in the next section.
* A payment model variant is a separate record with its own [SkuPriceId](#datamodel.skuprice.skupriceid), not one record with a null payment model. PurchasePaymentModel is not a member of the composite key, so two variants sharing a SKU Price ID would collide on row uniqueness. The same applies to term lengths: a one-year and a three-year reservation are separate records with separate SKU Price IDs.
* The flexible spend plan shows the same pattern for a spend commitment rather than a resource reservation. Its "Partial Upfront" record is the recurring installment that follows an initial payment, and its "No Upfront" record is the monthly fee charged when nothing is paid at the start. Both carry a [PricingUnit](#datamodel.skuprice.pricingunit) of "Units" and are denominated in the [PricingCurrency](#datamodel.skuprice.pricingcurrency) of "USD".
* The two plans carry different [SkuId](#datamodel.skuprice.skuid) values because they are different things to buy. The reservation records share "AURAWEB-COMPUTE-RESERVATION-VM-STD-1YR" and the spend plan records share "AURAWEB-COMMITMENT-FLEXSPEND-1YR".

## Commitment Rates

The rate that covered consumption is priced at is a separate record from the fee.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_commitment_rates.csv)

The extract carries the three reservation rates alongside the two reservation fees, so the difference between them is visible in one place.

Note the following details in the example dataset:

* The three rate records carry a ChargeCategory of "Usage" and a null PurchaseDurationType and PurchasePaymentModel, even though each rate exists only because a one-year reservation was purchased. The two fee records in the same extract carry both values. The columns describe the purchase, and a rate is not a purchase.
* This is deliberate rather than an omission. A price list is published before consumption happens, so at the time a rate is published there is no way to know whether a given unit of consumption will end up covered by a commitment. Whether coverage was actually applied is visible in [EffectiveCost](#datamodel.costandusage.effectivecost) and [BilledCost](#datamodel.costandusage.billedcost) in the [Cost and Usage](#datamodel.costandusage) dataset, which record what happened, rather than in the price, which records what is on offer.
* Because neither column is populated on a rate record, a rate that varies by payment model is distinguished by its SKU Price ID. The three records here are "AURAWEB-USEAST1-COMPUTE-USAGE-COMMITTED", "AURAWEB-USEAST1-COMPUTE-USAGE-COMMITTED-PARTIAL-UPFRONT", and "AURAWEB-USEAST1-COMPUTE-USAGE-COMMITTED-ALL-UPFRONT". Publishing them under one SKU Price ID would collide on row uniqueness and would leave a consumer no way to tell them apart.
* The rates and fees together produce the same one-year cost from three different cash-flow shapes. Against an on-demand [ListUnitPrice](#datamodel.skuprice.listunitprice) of 0.384000 per hour, or 3,363.84 over 8,760 hours:

| Payment model | Upfront fee | Hourly rate | One-year total | Reduction |
| :--- | ---: | ---: | ---: | ---: |
| All Upfront | 2354.690000 | 0.000000 | 2,354.69 | 30% |
| Partial Upfront | 1244.160000 | 0.142000 | 2,488.08 | 26% |
| No Upfront | *none* | 0.299200 | 2,620.99 | 22% |

* The "All Upfront" rate is 0.000000 rather than null. The obligation was settled in full by the fee, so covered consumption carries no further per-hour charge, and zero is the price. ListUnitPrice does not accept nulls in this dataset.
* The "No Upfront" plan has no fee record at all, because nothing is charged to acquire it. Its whole obligation is recovered through the hourly rate.

> **Note:** A purchase that carries no term at all leaves PurchaseDurationType null on a record whose ChargeCategory is "Purchase". A non-expiring balance of credits is the common shape, and is shown in the consumption currency scenario.
