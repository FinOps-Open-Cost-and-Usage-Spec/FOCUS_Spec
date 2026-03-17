## Diff

SkuPriceId [-adheres-]{+MUST adhere+} to the following requirements:

[-* SkuPriceId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports unit pricing concepts and publishes *price lists*, publicly or as part of contracting.-]
* SkuPriceId MUST be of type String.
* SkuPriceId MUST conform to [String [-Handling](#stringhandling)-]{+Handling](#attributes.stringhandling)+} requirements.
* SkuPriceId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * SkuPriceId MUST be null when ChargeCategory is "Tax".
  * SkuPriceId MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  * SkuPriceId MAY be null in all other cases.
* When SkuPriceId is not null, SkuPriceId [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * SkuPriceId MUST have one and only one parent [-[SkuId](#skuid).-]{+[SkuId](#datasets.costandusage.skuid).+}
  * SkuPriceId MUST remain consistent over time.
  * SkuPriceId MUST remain consistent across [*billing accounts*](#glossary:billing-account) or contracts.
  * SkuPriceId MAY equal SkuId.
  * SkuPriceId MUST be associated with a given [*resource*](#glossary:resource) or [*service*](#glossary:service) when ChargeCategory is "Usage" or "Purchase".
  * SkuPriceId MUST reference a *SKU Price* in a service-provider-supplied *price list*, enabling the lookup of detailed information about the *SKU Price*.
  * SkuPriceId MUST support the lookup of the ListUnitPrice when the service provider publishes unit prices exclusive of discounts.
  * SkuPriceId MUST support the verification of the given ContractedUnitPrice when the service provider supports negotiated pricing concepts.
