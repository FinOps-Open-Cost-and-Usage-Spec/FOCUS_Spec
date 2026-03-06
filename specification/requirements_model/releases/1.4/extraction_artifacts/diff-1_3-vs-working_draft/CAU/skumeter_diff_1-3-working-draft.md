## Diff

SkuMeter [-adheres-]{+MUST adhere+} to the following requirements:

[-* SkuMeter MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.-]
* SkuMeter MUST be of type String.
* SkuMeter MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* SkuMeter {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * SkuMeter MUST be null when [-[SkuId](#skuid)-]{+[SkuId](#datasets.costandusage.skuid)+} is null.
  * SkuMeter SHOULD NOT be null when SkuId is not null.
* SkuMeter SHOULD remain consistent over time for a given SkuId.

