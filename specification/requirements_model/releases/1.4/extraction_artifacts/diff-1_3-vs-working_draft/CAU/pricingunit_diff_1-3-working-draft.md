## Diff

@@ -1,14 +1,13 @@
## Requirements

PricingUnit [-adheres-]{+MUST adhere+} to the following requirements:

[-* PricingUnit MUST be present in a Cost and Usage *FOCUS dataset*.-]
* PricingUnit MUST be of type String.
* PricingUnit MUST conform to StringHandling requirements.
* PricingUnit SHOULD conform to UnitFormat requirements.
* PricingUnit {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * PricingUnit MUST be null when PricingQuantity is null.
  * PricingUnit MUST NOT be null when PricingQuantity is not null.
* When PricingUnit is not null, PricingUnit [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * PricingUnit MUST be semantically equal to the corresponding pricing measurement unit provided in service-provider-published *price list*.
  * PricingUnit MUST be semantically equal to the corresponding pricing measurement unit provided in invoice, when the invoice includes a pricing measurement unit.
