## Diff

CommitmentDiscountQuantity [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountQuantity MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.-]
* CommitmentDiscountQuantity MUST be of type Decimal.
* CommitmentDiscountQuantity MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* CommitmentDiscountQuantity {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountQuantity MUST be null when [-[SkuPriceId](#skupriceid)-]{+[SkuPriceId](#datasets.costandusage.skupriceid)+} is null.
  * When ChargeCategory is "Usage" or "Purchase" and CommitmentDiscountId is not null, CommitmentDiscountQuantity [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
    * CommitmentDiscountQuantity MUST NOT be null when [-[ChargeClass](#chargeclass)-]{+[ChargeClass](#datasets.costandusage.chargeclass)+} is not "Correction".
    * CommitmentDiscountQuantity MAY be null when ChargeClass is "Correction".
  * CommitmentDiscountQuantity MUST be null in all other cases.
* CommitmentDiscountQuantity MUST be a valid decimal value when not null.
* When CommitmentDiscountQuantity is not null and ChargeCategory is "Purchase", CommitmentDiscountQuantity [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term* when [-[ChargeFrequency](#chargefrequency)-]{+[ChargeFrequency](#datasets.costandusage.chargefrequency)+} is "One-Time".
  * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit that is eligible for consumption for each *charge period* that corresponds with the purchase when ChargeFrequency is "Recurring".
* When CommitmentDiscountQuantity is not null and ChargeCategory is "Usage", CommitmentDiscountQuantity [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * CommitmentDiscountQuantity MUST be the metered quantity of CommitmentDiscountUnit that is consumed in a given *charge period* when [-[CommitmentDiscountStatus](#commitmentdiscountstatus)-]{+[CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus)+} is "Used".
  * CommitmentDiscountQuantity MUST be the remaining, unused quantity of CommitmentDiscountUnit in a given *charge period* when CommitmentDiscountStatus is "Unused".

