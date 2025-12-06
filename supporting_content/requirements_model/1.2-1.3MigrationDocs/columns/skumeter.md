## SKUMeter

### Normative Text v1.2

The SkuMeter column adheres to the following requirements:

* SkuMeter MUST be present in a *FOCUS dataset* when the provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.
* SkuMeter MUST be of type String.
* SkuMeter MUST conform to [StringHandling](#stringhandling) requirements.
* SkuMeter nullability is defined as follows:
  * SkuMeter MUST be null when [SkuId](#skuid) is null.
  * SkuMeter SHOULD NOT be null when SkuId is not null.
* SkuMeter SHOULD remain consistent over time for a given SkuId.

### Normative Text v1.3

## Requirements

SkuMeter adheres to the following requirements:

* SkuMeter MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.
* SkuMeter MUST be of type String.
* SkuMeter MUST conform to [StringHandling](#stringhandling) requirements.
* SkuMeter nullability is defined as follows:
  * SkuMeter MUST be null when [SkuId](#skuid) is null.
  * SkuMeter SHOULD NOT be null when SkuId is not null.
* SkuMeter SHOULD remain consistent over time for a given SkuId.

### Diff

-The SkuMeter column adheres to the following requirements:
+## Requirements
 
-* SkuMeter MUST be present in a *FOCUS dataset* when the provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.
+SkuMeter adheres to the following requirements:
+
+* SkuMeter MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.
 * SkuMeter MUST be of type String.
 * SkuMeter MUST conform to [StringHandling](#stringhandling) requirements.
 * SkuMeter nullability is defined as follows: