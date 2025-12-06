## ServiceName

### Normative Text v1.2

The ServiceName column adheres to the following requirements:

* ServiceName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ServiceName MUST be of type String.
* ServiceName MUST conform to [StringHandling](#stringhandling) requirements.
* ServiceName MUST NOT be null.
* The relationship between ServiceName and [ServiceCategory](#servicecategory) is defined as follows:
  * ServiceName MUST have one and only one ServiceCategory that best aligns with its primary purpose, except when no suitable ServiceCategory is available.
  * ServiceName MUST be associated with the ServiceCategory "Other" when no suitable ServiceCategory is available.
* The relationship between ServiceName and [ServiceSubcategory](#servicesubcategory) is defined as follows:
  * ServiceName SHOULD have one and only one ServiceSubcategory that best aligns with its primary purpose, except when no suitable ServiceSubcategory is available.
  * ServiceName SHOULD be associated with the ServiceSubcategory "Other" when no suitable ServiceSubcategory is available.

### Normative Text v1.3

ServiceName adheres to the following requirements:

* ServiceName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ServiceName MUST be of type String.
* ServiceName MUST conform to [StringHandling](#stringhandling) requirements.
* ServiceName MUST NOT be null.
* The relationship between ServiceName and [ServiceCategory](#servicecategory) is defined as follows:
  * ServiceName MUST have one and only one ServiceCategory that best aligns with its primary purpose, except when no suitable ServiceCategory is available.
  * ServiceName MUST be associated with the ServiceCategory "Other" when no suitable ServiceCategory is available.
* The relationship between ServiceName and [ServiceSubcategory](#servicesubcategory) is defined as follows:
  * ServiceName SHOULD have one and only one ServiceSubcategory that best aligns with its primary purpose, except when no suitable ServiceSubcategory is available.
  * ServiceName SHOULD be associated with the ServiceSubcategory "Other" when no suitable ServiceSubcategory is available.

### Diff

-The ServiceName column adheres to the following requirements:
+## Requirements
 
-* ServiceName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
+ServiceName adheres to the following requirements:
+
+* ServiceName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
 * ServiceName MUST be of type String.
 * ServiceName MUST conform to [StringHandling](#stringhandling) requirements.
 * ServiceName MUST NOT be null.