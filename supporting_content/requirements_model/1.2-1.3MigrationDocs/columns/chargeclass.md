## ChargeClass

### Normative Text v1.2

The ChargeClass column adheres to the following requirements:

* ChargeClass MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargeClass MUST be of type String.
* ChargeClass nullability is defined as follows:
  * ChargeClass MUST be null when the *row* does not represent a correction or when it represents a correction within the current *billing period*.
  * ChargeClass MUST NOT be null when the *row* represents a correction to a previously invoiced *billing period*.
* ChargeClass MUST be "Correction" when ChargeClass is not null.

### Normative Text v1.3

## Requirements

ChargeClass adheres to the following requirements:

* ChargeClass MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargeClass MUST be of type String.
* ChargeClass nullability is defined as follows:
  * ChargeClass MUST be null when the *row* does not represent a correction or when it represents a correction within the current *billing period*.
  * ChargeClass MUST NOT be null when the *row* represents a correction to a previously invoiced *billing period*.
* ChargeClass MUST be "Correction" when ChargeClass is not null.

### Diff

-The ChargeClass column adheres to the following requirements:
+## Requirements^M
 
-* ChargeClass MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
+ChargeClass adheres to the following requirements:^M
+^M
+* ChargeClass MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).^M
 * ChargeClass MUST be of type String.
 * ChargeClass nullability is defined as follows:
   * ChargeClass MUST be null when the *row* does not represent a correction or when it represents a correction within the current *billing period*.