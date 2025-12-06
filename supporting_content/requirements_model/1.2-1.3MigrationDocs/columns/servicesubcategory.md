## ServiceSubcategory

### Normative Text v1.2

The ServiceSubcategory column adheres to the following requirements:

* ServiceSubcategory is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ServiceSubcategory MUST be of type String.
* ServiceSubcategory MUST NOT be null.
* ServiceSubcategory MUST be one of the allowed values.
* ServiceSubcategory MUST have one and only one parent ServiceCategory as specified in the allowed values below.

### Normative Text v1.3

## Requirements

ServiceSubcategory adheres to the following requirements:

* ServiceSubcategory is RECOMMENDED to be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ServiceSubcategory MUST be of type String.
* ServiceSubcategory MUST NOT be null.
* ServiceSubcategory MUST be one of the allowed values.
* ServiceSubcategory MUST have one and only one parent ServiceCategory as specified in the allowed values below.

### Diff

-The Service Subcategory is a secondary classification of the [Service Category](#servicecategory) for a [*service*](#glossary:service) based on its core function. The Service Subcategory (in conjunction with the Service Category) is commonly used for scenarios like analyzing spend and usage for specific workload types across providers and tracking the migration of workloads across fundamentally different architectures.  
+The Service Subcategory is a secondary classification of the [Service Category](#servicecategory) for a [*service*](#glossary:service) based on its core function. The Service Subcategory (in conjunction with the Service Category) is commonly used for scenarios like analyzing spend and usage for specific workload types across service providers and tracking the migration of workloads across fundamentally different architectures.  
 
-The ServiceSubcategory column adheres to the following requirements:
+## Requirements
 
-* ServiceSubcategory is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
+ServiceSubcategory adheres to the following requirements:
+
+* ServiceSubcategory is RECOMMENDED to be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).