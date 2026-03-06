## Diff

ListUnitPrice [-adheres-]{+MUST adhere+} to the following requirements:

[-* ListUnitPrice MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider publishes unit prices exclusive of discounts.-]
* ListUnitPrice MUST be of type Decimal.
* ListUnitPrice MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* ListUnitPrice {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ListUnitPrice MUST be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is null.
  * ListUnitPrice MUST be null when [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is "Tax".
  * ListUnitPrice MUST NOT be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is not null.
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [-[ChargeClass](#chargeclass)-]{+[ChargeClass](#datasets.costandusage.chargeclass)+} is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* When ListUnitPrice is not null, ListUnitPrice [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the BillingCurrency.
* [-[ListCost](#listcost)-]{+[ListCost](#datasets.costandusage.listcost)+} MUST equal the product of ListUnitPrice and [-[PricingQuantity](#pricingquantity)-]{+[PricingQuantity](#datasets.costandusage.pricingquantity)+} when ListUnitPrice is not null and PricingQuantity is not null.

