## Diff

ChargeClass [-adheres-]{+MUST adhere+} to the following requirements:

[-* ChargeClass MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
-]
* ChargeClass MUST be of type String.
* ChargeClass {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ChargeClass MUST be null when the [-*row*-]{+*charge*+} does not represent a correction [-or when it represents-]{+to+} a [-correction within the current *billing-]{+previously *closed billing+} period*.
  * ChargeClass MUST NOT be null when the [-*row*-]{+*charge*+} represents a correction to a previously [-invoiced *billing-]{+*closed billing+} period*.
* ChargeClass MUST be "Correction" when ChargeClass is not null.