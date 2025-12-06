## ConsumedQuantity

### Normative Text v1.2

The ConsumedQuantity column adheres to the following requirements:

* ConsumedQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports the measurement of usage.
* ConsumedQuantity MUST be of type Decimal.
* ConsumedQuantity MUST conform to [NumericFormat](#numericformat) requirements.
* ConsumedQuantity nullability is defined as follows:
  * ConsumedQuantity MUST be null when [ChargeCategory](#chargecategory) is not "Usage", or when ChargeCategory is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused".
  * When ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", ConsumedQuantity adheres to the following additional requirements:
    * ConsumedQuantity MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction".
    * ConsumedQuantity MAY be null when ChargeClass is "Correction".
* ConsumedQuantity MUST be a valid decimal value when not null.

### Normative Text v1.3

## Requirements

ConsumedQuantity adheres to the following requirements:

* ConsumedQuantity MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports the measurement of usage.
* ConsumedQuantity MUST be of type Decimal.
* ConsumedQuantity MUST conform to [NumericFormat](#numericformat) requirements.
* ConsumedQuantity nullability is defined as follows:
  * ConsumedQuantity MUST be null when [SkuPriceId](#skupriceid) is null.
  * ConsumedQuantity MUST be null when [ChargeCategory](#chargecategory) is not "Usage", or when ChargeCategory is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused".
  * When ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", ConsumedQuantity adheres to the following additional requirements:
    * ConsumedQuantity MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction".
    * ConsumedQuantity MAY be null when ChargeClass is "Correction".
* ConsumedQuantity MUST be a valid decimal value when not null.

### Diff

-The ConsumedQuantity column adheres to the following requirements:
+## Requirements
 
-* ConsumedQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports the measurement of usage.
+ConsumedQuantity adheres to the following requirements:
+
+* ConsumedQuantity MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports the measurement of usage.
 * ConsumedQuantity MUST be of type Decimal.
 * ConsumedQuantity MUST conform to [NumericFormat](#numericformat) requirements.
 * ConsumedQuantity nullability is defined as follows:
+  * ConsumedQuantity MUST be null when [SkuPriceId](#skupriceid) is null.
   * ConsumedQuantity MUST be null when [ChargeCategory](#chargecategory) is not "Usage", or when ChargeCategory is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused".
   * When ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", ConsumedQuantity adheres to the following additional requirements:
     * ConsumedQuantity MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction".


