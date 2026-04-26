## Diff

@@ -1,17 +1,16 @@
## Requirements

PricingCategory [-adheres-]{+MUST adhere+} to the following requirements:

[-* PricingCategory MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports more than one pricing category across all *SKUs*.-]
* PricingCategory MUST be of type String.
* PricingCategory {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * PricingCategory MUST be null when SkuPriceId is null.
  * PricingCategory MUST be null when ChargeCategory is "Tax".
  * PricingCategory MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  * PricingCategory MAY be null in all other cases.
* When PricingCategory is not null, PricingCategory [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * PricingCategory MUST be one of the allowed values.
  * PricingCategory MUST be "Standard" when pricing is predetermined at the agreed upon rate for the billing account.
  * PricingCategory MUST be "Committed" when the *charge* is subject to an existing *commitment discount* and is not the purchase of the *commitment discount*.
  * PricingCategory MUST be "Dynamic" when pricing is determined by the service provider and may change over time, regardless of predetermined agreement pricing.
  * PricingCategory MUST be "Other" when there is a pricing model but none of the allowed values apply.
