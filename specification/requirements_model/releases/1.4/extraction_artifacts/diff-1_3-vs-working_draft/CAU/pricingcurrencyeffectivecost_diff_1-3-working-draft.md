## Diff

PricingCurrencyEffectiveCost [-adheres-]{+MUST adhere+} to the following requirements:

* PricingCurrencyEffectiveCost presence in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset)[-is defined as follows:-]
[-  * PricingCurrencyEffectiveCost-] MUST [-be present in a Cost and Usage *FOCUS dataset* when-]{+adhere to+} the [-service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.-]{+following presence requirements:+}
  * PricingCurrencyEffectiveCost [-is RECOMMENDED to-]{+SHOULD+} be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
  * PricingCurrencyEffectiveCost MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.
* PricingCurrencyEffectiveCost MUST be of type Decimal.
* PricingCurrencyEffectiveCost MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* PricingCurrencyEffectiveCost MUST NOT be null.
* PricingCurrencyEffectiveCost MUST be [-a valid decimal value.-]
[-* PricingCurrencyEffectiveCost MUST be 0-]{+denominated+} in the [-event of prepaid purchases or purchases that are applicable to previous usage.-]{+[PricingCurrency](#datasets.costandusage.pricingcurrency).+}
* PricingCurrencyEffectiveCost MUST be[-denominated in-] the [-[PricingCurrency](#pricingcurrency).-]{+PricingCurrency-denominated equivalent of [EffectiveCost](#datasets.costandusage.effectivecost).+}

