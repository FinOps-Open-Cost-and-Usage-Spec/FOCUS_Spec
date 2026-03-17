## Diff

ConsumedQuantity [-adheres-]{+MUST adhere+} to the following requirements:

[-* ConsumedQuantity MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports the measurement of usage.-]
* ConsumedQuantity MUST be of type Decimal.
* ConsumedQuantity MUST conform to NumericFormat requirements.
* ConsumedQuantity {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ConsumedQuantity MUST be null when SkuPriceId is null.
  * ConsumedQuantity MUST be null when ChargeCategory is not "Usage", or when ChargeCategory is "Usage" and CommitmentDiscountStatus is "Unused".
  * When ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", ConsumedQuantity [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
    * ConsumedQuantity MUST NOT be null when ChargeClass is not "Correction".
    * ConsumedQuantity MAY be null when ChargeClass is "Correction".
* ConsumedQuantity MUST be a valid decimal value when not null.

