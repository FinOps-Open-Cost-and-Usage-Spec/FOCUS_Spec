## SKUId

### Normative Text v1.2

### Normative Text v1.2

The SkuId column adheres to the following requirements:

* SkuId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports unit pricing concepts and publishes price lists, publicly or as part of contracting.
* SkuId MUST be of type String.
* SkuId MUST conform to [StringHandling](#stringhandling) requirements.
* SkuId nullability is defined as follows:
  * SkuId MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * SkuId MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * SkuId MAY be null in all other cases.
* SkuId for a given *SKU* adheres to the following additional requirements:
  * SkuId MUST remain consistent across [*billing accounts*](#glossary:billing-account) or contracts.
  * SkuId MUST remain consistent across [PricingCategory](#pricingcategory) values.
  * SkuId MUST remain consistent regardless of any other factors that might impact the price but do not affect the functionality of the *SKU*.
* SkuId MUST be associated with a given [*resource*](#glossary:resource) or [*service*](#glossary:service) when ChargeCategory is "Usage" or "Purchase".
* SkuId MAY equal [SkuPriceId](#SkuPriceId).

### Normative Text v1.3

## Requirements

SkuId adheres to the following requirements:

* SkuId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports unit pricing concepts and publishes price lists, publicly or as part of contracting.
* SkuId MUST be of type String.
* SkuId MUST conform to [StringHandling](#stringhandling) requirements.
* SkuId nullability is defined as follows:
  * SkuId MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * SkuId MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * SkuId MAY be null in all other cases.
* SkuId for a given *SKU* adheres to the following additional requirements:
  * SkuId MUST remain consistent across [*billing accounts*](#glossary:billing-account) or contracts.
  * SkuId MUST remain consistent across [PricingCategory](#pricingcategory) values.
  * SkuId MUST remain consistent regardless of any other factors that might impact the price but do not affect the functionality of the *SKU*.
* SkuId MUST be associated with a given [*resource*](#glossary:resource) or [*service*](#glossary:service) when ChargeCategory is "Usage" or "Purchase".
* SkuId MAY equal [SkuPriceId](#skupriceid).

### Diff

-The SkuId column adheres to the following requirements:
+## Requirements
 
-* SkuId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports unit pricing concepts and publishes price lists, publicly or as part of contracting.
+SkuId adheres to the following requirements:
+
+* SkuId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports unit pricing concepts and publishes price lists, publicly or as part of contracting.
 * SkuId MUST be of type String.
 * SkuId MUST conform to [StringHandling](#stringhandling) requirements.
 * SkuId nullability is defined as follows:
@@ -29,7 +31,7 @@ The SkuId column adheres to the following requirements:
   * SkuId MUST remain consistent across [PricingCategory](#pricingcategory) values.
   * SkuId MUST remain consistent regardless of any other factors that might impact the price but do not affect the functionality of the *SKU*.
 * SkuId MUST be associated with a given [*resource*](#glossary:resource) or [*service*](#glossary:service) when ChargeCategory is "Usage" or "Purchase".
-* SkuId MAY equal [SkuPriceId](#SkuPriceId).
+* SkuId MAY equal [SkuPriceId](#skupriceid).
