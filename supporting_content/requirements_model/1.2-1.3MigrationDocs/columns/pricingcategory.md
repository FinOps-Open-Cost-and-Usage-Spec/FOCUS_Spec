## PricingCategory

### Normative Text v1.2

The PricingCategory column adheres to the following requirements:

* PricingCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports more than one pricing category across all [*SKUs*](#glossary:sku).
* PricingCategory MUST be of type String.
* PricingCategory nullability is defined as follows:
  * PricingCategory MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * PricingCategory MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * PricingCategory MAY be null in all other cases.
* When PricingCategory is not null, PricingCategory adheres to the following additional requirements:
  * PricingCategory MUST be one of the allowed values.
  * PricingCategory MUST be "Standard" when pricing is predetermined at the agreed upon rate for the [billing account](#glossary:billing-account).
  * PricingCategory MUST be "Committed" when the *charge* is subject to an existing *commitment discount* and is not the purchase of the *commitment discount*.
  * PricingCategory MUST be "Dynamic" when pricing is determined by the provider and may change over time, regardless of predetermined agreement pricing.
  * PricingCategory MUST be "Other" when there is a pricing model but none of the allowed values apply.


### Normative Text v1.3

## Requirements

PricingCategory adheres to the following requirements:

* PricingCategory MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports more than one pricing category across all [*SKUs*](#glossary:sku).
* PricingCategory MUST be of type String.
* PricingCategory nullability is defined as follows:
  * PricingCategory MUST be null when [SkuPriceId](#skupriceid) is null.
  * PricingCategory MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * PricingCategory MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * PricingCategory MAY be null in all other cases.
* When PricingCategory is not null, PricingCategory adheres to the following additional requirements:
  * PricingCategory MUST be one of the allowed values.
  * PricingCategory MUST be "Standard" when pricing is predetermined at the agreed upon rate for the [billing account](#glossary:billing-account).
  * PricingCategory MUST be "Committed" when the *charge* is subject to an existing *commitment discount* and is not the purchase of the *commitment discount*.
  * PricingCategory MUST be "Dynamic" when pricing is determined by the service provider and may change over time, regardless of predetermined agreement pricing.
  * PricingCategory MUST be "Other" when there is a pricing model but none of the allowed values apply.

### Diff

-The PricingCategory column adheres to the following requirements:
+## Requirements
 
-* PricingCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports more than one pricing category across all [*SKUs*](#glossary:sku).
+PricingCategory adheres to the following requirements:
+
+* PricingCategory MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports more than one pricing category across all [*SKUs*](#glossary:sku).
 * PricingCategory MUST be of type String.
 * PricingCategory nullability is defined as follows:
+  * PricingCategory MUST be null when [SkuPriceId](#skupriceid) is null.
   * PricingCategory MUST be null when [ChargeCategory](#chargecategory) is "Tax".
   * PricingCategory MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
   * PricingCategory MAY be null in all other cases.
@@ -14,7 +17,7 @@ The PricingCategory column adheres to the following requirements:
   * PricingCategory MUST be one of the allowed values.
   * PricingCategory MUST be "Standard" when pricing is predetermined at the agreed upon rate for the [billing account](#glossary:billing-account).
   * PricingCategory MUST be "Committed" when the *charge* is subject to an existing *commitment discount* and is not the purchase of the *commitment discount*.
-  * PricingCategory MUST be "Dynamic" when pricing is determined by the provider and may change over time, regardless of predetermined agreement pricing.
+  * PricingCategory MUST be "Dynamic" when pricing is determined by the service provider and may change over time, regardless of predetermined agreement pricing.
   * PricingCategory MUST be "Other" when there is a pricing model but none of the allowed values apply.