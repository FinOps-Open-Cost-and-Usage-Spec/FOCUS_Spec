## Diff

@@ -1,9 +1,8 @@
## Requirements

ServiceSubcategory [-adheres-]{+MUST adhere+} to the following requirements:

[-* ServiceSubcategory is RECOMMENDED to be present in a Cost and Usage *FOCUS dataset*.-]
* ServiceSubcategory MUST be of type String.
* ServiceSubcategory MUST NOT be null.
* ServiceSubcategory MUST be one of the allowed values.
* ServiceSubcategory MUST have one and only one parent ServiceCategory as specified in the allowed values below.
