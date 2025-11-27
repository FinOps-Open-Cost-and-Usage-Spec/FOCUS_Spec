# CommitmentDiscountQuantity

## Normative Text 1.2

The CommitmentDiscountQuantity column adheres to the following requirements:
CommitmentDiscountQuantity MUST be present in a FOCUS dataset when the provider supports commitment discounts.
CommitmentDiscountQuantity MUST be of type Decimal.
CommitmentDiscountQuantity MUST conform to NumericFormat requirements.
CommitmentDiscountQuantity nullability is defined as follows:
When ChargeCategory is "Usage" or "Purchase" and CommitmentDiscountId is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
CommitmentDiscountQuantity MUST NOT be null when ChargeClass is not "Correction".
CommitmentDiscountQuantity MAY be null when ChargeClass is "Correction".
CommitmentDiscountQuantity MUST be null in all other cases.
When CommitmentDiscountQuantity is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
CommitmentDiscountQuantity MUST be a valid decimal value.
When ChargeCategory is "Purchase":
CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit, paid fully or partially upfront, that is eligible for consumption over the commitment discount's term when ChargeFrequency is "One-Time".
CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit that is eligible for consumption for each charge period that corresponds with the purchase when ChargeFrequency is "Recurring".
When ChargeCategory is "Usage":
CommitmentDiscountQuantity MUST be the metered quantity of CommitmentDiscountUnit that is consumed in a given charge period when CommitmentDiscountStatus is "Used".
CommitmentDiscountQuantity MUST be the remaining, unused quantity of CommitmentDiscountUnit in a given charge period when CommitmentDiscountStatus is "Unused".

## Normative Text 1.3

CommitmentDiscountQuantity adheres to the following requirements:
CommitmentDiscountQuantity MUST be present in a Cost and Usage FOCUS dataset when the service provider supports commitment discounts.
CommitmentDiscountQuantity MUST be of type Decimal.
CommitmentDiscountQuantity MUST conform to NumericFormat requirements.
CommitmentDiscountQuantity nullability is defined as follows:
CommitmentDiscountQuantity MUST be null when SkuPriceId is null.
When ChargeCategory is "Usage" or "Purchase" and CommitmentDiscountId is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
CommitmentDiscountQuantity MUST NOT be null when ChargeClass is not "Correction".
CommitmentDiscountQuantity MAY be null when ChargeClass is "Correction".
CommitmentDiscountQuantity MUST be null in all other cases.
CommitmentDiscountQuantity MUST be a valid decimal value when not null.
When CommitmentDiscountQuantity is not null and ChargeCategory is "Purchase", CommitmentDiscountQuantity adheres to the following additional requirements:
CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit, paid fully or partially upfront, that is eligible for consumption over the commitment discount's term when ChargeFrequency is "One-Time".
CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit that is eligible for consumption for each charge period that corresponds with the purchase when ChargeFrequency is "Recurring".
When CommitmentDiscountQuantity is not null and ChargeCategory is "Usage", CommitmentDiscountQuantity adheres to the following additional requirements:
CommitmentDiscountQuantity MUST be the metered quantity of CommitmentDiscountUnit that is consumed in a given charge period when CommitmentDiscountStatus is "Used".
CommitmentDiscountQuantity MUST be the remaining, unused quantity of CommitmentDiscountUnit in a given charge period when CommitmentDiscountStatus is "Unused".

## Diff

-The CommitmentDiscountQuantity column adheres to the following requirements:
+## Requirements

-*CommitmentDiscountQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
+CommitmentDiscountQuantity adheres to the following requirements:
+
+* CommitmentDiscountQuantity MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.

* CommitmentDiscountQuantity MUST be of type Decimal.
* CommitmentDiscountQuantity MUST conform to [NumericFormat](#numericformat) requirements.
* CommitmentDiscountQuantity nullability is defined as follows:

* * CommitmentDiscountQuantity MUST be null when [SkuPriceId](#skupriceid) is null.
  * When ChargeCategory is "Usage" or "Purchase" and CommitmentDiscountId is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
    * CommitmentDiscountQuantity MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction".
    * CommitmentDiscountQuantity MAY be null when ChargeClass is "Correction".
  * CommitmentDiscountQuantity MUST be null in all other cases.
-* When CommitmentDiscountQuantity is not null, CommitmentDiscountQuantity adheres to the following additional requirements:

* * CommitmentDiscountQuantity MUST be a valid decimal value.

* * When ChargeCategory is "Purchase":
* * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term* when [ChargeFrequency](#chargefrequency) is "One-Time".
* * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit that is eligible for consumption for each *charge period* that corresponds with the purchase when ChargeFrequency is "Recurring".
* * When ChargeCategory is "Usage":
* * CommitmentDiscountQuantity MUST be the metered quantity of CommitmentDiscountUnit that is consumed in a given *charge period* when [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Used".
* * CommitmentDiscountQuantity MUST be the remaining, unused quantity of CommitmentDiscountUnit in a given *charge period* when CommitmentDiscountStatus is "Unused".
+*CommitmentDiscountQuantity MUST be a valid decimal value when not null.
+* When CommitmentDiscountQuantity is not null and ChargeCategory is "Purchase", CommitmentDiscountQuantity adheres to the following additional requirements:

* * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term* when [ChargeFrequency](#chargefrequency) is "One-Time".

* * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit that is eligible for consumption for each *charge period* that corresponds with the purchase when ChargeFrequency is "Recurring".
+* When CommitmentDiscountQuantity is not null and ChargeCategory is "Usage", CommitmentDiscountQuantity adheres to the following additional requirements:
* * CommitmentDiscountQuantity MUST be the metered quantity of CommitmentDiscountUnit that is consumed in a given *charge period* when [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Used".
* * CommitmentDiscountQuantity MUST be the remaining, unused quantity of CommitmentDiscountUnit in a given *charge period* when CommitmentDiscountStatus is "Unused".
