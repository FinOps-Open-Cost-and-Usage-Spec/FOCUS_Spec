## Diff

SkuId [-adheres-]{+MUST adhere+} to the following requirements:

[-* SkuId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports unit pricing concepts and publishes price lists, publicly or as part of contracting.-]
* SkuId MUST be of type String.
* SkuId MUST conform to StringHandling requirements.
* SkuId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * SkuId MUST be null when ChargeCategory is "Tax".
  * SkuId MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  * SkuId MAY be null in all other cases.
* SkuId for a given *SKU* [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * SkuId MUST remain consistent across [*billing accounts*](#glossary:billing-account) or contracts.
  * SkuId MUST remain consistent across PricingCategory values.
  * SkuId MUST remain consistent regardless of any other factors that might impact the price but do not affect the functionality of the *SKU*.
* SkuId MUST be associated with a given [*resource*](#glossary:resource) or [*service*](#glossary:service) when ChargeCategory is "Usage" or "Purchase".
* SkuId MAY equal [-[SkuPriceId](#skupriceid).-]{+[SkuPriceId](#datasets.costandusage.skupriceid).+}

