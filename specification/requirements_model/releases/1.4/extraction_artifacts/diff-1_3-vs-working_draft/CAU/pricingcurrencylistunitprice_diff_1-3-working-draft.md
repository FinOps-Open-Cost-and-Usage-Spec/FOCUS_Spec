## Diff

PricingCurrencyListUnitPrice [-adheres-]{+MUST adhere+} to the following requirements:

* PricingCurrencyListUnitPrice presence in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset)[-is defined as follows:-]
[-  * PricingCurrencyListUnitPrice-] MUST [-be present in a Cost and Usage *FOCUS dataset* when-]{+adhere to+} the [-service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.-]{+following presence requirements:+}
  * PricingCurrencyListUnitPrice [-is RECOMMENDED to-]{+SHOULD+} be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
  * PricingCurrencyListUnitPrice MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.
* PricingCurrencyListUnitPrice MUST be of type Decimal.
* PricingCurrencyListUnitPrice MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* PricingCurrencyListUnitPrice {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * PricingCurrencyListUnitPrice MUST be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is null.
  * PricingCurrencyListUnitPrice MUST be null when [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is "Tax".
  * PricingCurrencyListUnitPrice MUST NOT be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is not null.
  * PricingCurrencyListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [-[ChargeClass](#chargeclass)-]{+[ChargeClass](#datasets.costandusage.chargeclass)+} is not "Correction".
  * PricingCurrencyListUnitPrice MAY be null in all other cases.
* When PricingCurrencyListUnitPrice is not null, PricingCurrencyListUnitPrice [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * PricingCurrencyListUnitPrice MUST be a non-negative decimal value.
  * PricingCurrencyListUnitPrice MUST be denominated in the PricingCurrency.

