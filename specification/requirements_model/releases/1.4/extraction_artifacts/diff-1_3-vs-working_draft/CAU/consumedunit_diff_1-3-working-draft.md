## Diff

ConsumedUnit [-adheres-]{+MUST adhere+} to the following requirements:

[-* ConsumedUnit MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports the measurement of usage.-]
* ConsumedUnit MUST be of type String.
* ConsumedUnit MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ConsumedUnit SHOULD conform to [-[UnitFormat](#unitformat)-]{+[UnitFormat](#attributes.unitformat)+} requirements.
* ConsumedUnit {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ConsumedUnit MUST be null when ConsumedQuantity is null.
  * ConsumedUnit MUST NOT be null when ConsumedQuantity is not null.

