## Diff

ChargeClass [-adheres-]{+MUST adhere+} to the following requirements:

[-* ChargeClass MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
-]
* ChargeClass MUST be of type String.
* ChargeClass {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ChargeClass MUST be null when the *row* does not represent a correction or when it represents a correction within the current *billing period*.
  * ChargeClass MUST NOT be null when the *row* represents a correction to a previously invoiced *billing period*.
* ChargeClass MUST be "Correction" when ChargeClass is not null.
