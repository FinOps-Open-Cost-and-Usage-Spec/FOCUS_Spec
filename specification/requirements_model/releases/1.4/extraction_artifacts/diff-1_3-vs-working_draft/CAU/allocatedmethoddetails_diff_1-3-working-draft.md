## Diff

@@ -1,63 +1,13 @@
## Requirements

### Column Requirements

[-The-]AllocatedMethodDetails [-column adheres-]{+MUST adhere+} to the following requirements:

* AllocatedMethodDetails[-SHOULD be present in a Cost and Usage *FOCUS dataset* when the data generator supports Data Generator-Calculated Split Cost Allocation.-]
[-* AllocatedMethodDetails-] MUST be of type [-String.-]{+JSON Object (serialized as a String where necessary).+}
* AllocatedMethodDetails MUST conform to StringHandling requirements.
* AllocatedMethodDetails MUST conform to JsonObjectFormat requirements.
* AllocatedMethodDetails {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * AllocatedMethodDetails MUST be null when a charge is not related to a data generator-calculated split cost allocation.
  * AllocatedMethodDetails SHOULD NOT be null when a charge is related to a data generator-calculated split cost allocation.
[-### Object Schema Requirements-]

[-Allocated Method Details consists of a valid JSON object which contains an array of key-value objects describing the one or more factors (allocation properties) that determined the split cost allocation. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the allocation.-]

[-When AllocatedMethodDetails is not null, the JsonObjectFormat for AllocatedMethodDetails adheres to the following requirements:-]* AllocatedMethodDetails MUST[-have a top-level key "Elements" which contains an array.-]
[-* Each item in "Elements" MUST be an object.-]
[-  * Objects inside "Elements" MUST-] conform to [-KeyValueFormat requirements.-]
[-    * FOCUS-defined allocation properties adhere to the following additional requirements:-]
[-      * Allocation property key MUST match the spelling and casing specified for the FOCUS-defined property.-]
[-      * Allocation property value MUST be of the type specified for that property.-]
[-      * Allocation properties MUST adhere to additional normative-]{+AllocatedMethodDetailsObject+} requirements [-specific to that property.-]
[-    * Data generator-defined allocation properties MAY be included in "Elements".-]
[-      * Allocation property keys MUST begin with the string "x_" unless it is a FOCUS-defined allocation property.-]
[-*-]{+when+} AllocatedMethodDetails[-root object MAY contain additional data generator-defined items, in addition to "Elements".-]

[-### Content Requirements-]

[-The following keys are used for allocation properties to facilitate querying data across allocations and across data generators. Focus-defined keys will appear in the list below and data generator-defined keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.-]

[-<b>Allocated Ratio</b>-]

[-Allocated Ratio communicates the percentage of the *Origin Charge* that this *Allocated Charge* derived from the corresponding Allocated Method Id and Usage Unit property.-]

[-The "AllocatedRatio" property adheres to the following requirements:-]

[-* "AllocatedRatio" MUST be included inside each "Elements" object.-]
[-* Values for "AllocatedRatio" MUST be a decimal value compatible with NumericFormat representing the allocated charge's percentage of the origin charge.-]
[-* Values for all "AllocatedRatio" properties across all allocated charges related to a single origin charge MUST sum up to 1 (100%).-]

[-<b>Usage Unit</b>-]

[-Usage Unit communicates the aspect of the documented Allocation Method Id being used to calculate the Allocated Ratio property and what is being measured by Usage Quantity property.-]

[-The "UsageUnit" property adheres to the following requirements:-]

[-* "UsageUnit" MUST be included inside an "Elements" object if "UsageQuantity" allocation property-] is [-included in that "Elements" object, otherwise "UsageUnit" MAY be included in each "Elements" object.-]
[-* Values for "UsageUnit" MUST capture the unit or component of data generator's documented AllocationMethod that was used to determine the "AllocatedRatio" value.-]
[-* Values for "UsageUnit" SHOULD conform to UnitFormat requirements.-]

[-<b>Usage Quantity</b>-]

[-Usage Quantity communicates the volume that was consumed or used, denominated in the Usage Unit property value.-]

[-The "UsageQuantity" property adheres to the following requirements:-]

[-* "UsageQuantity" MAY be included inside an "Elements" object when that "Elements" object contains a "UsageUnit" allocation property.-]
[-* Values for "UsageQuantity" MUST be compatible with NumericFormat.-]
[-* Values for "UsageQuantity" SHOULD capture the quantity or volume of the "UsageUnit" measured by the data generator that was used to determine the "AllocatedRatio" value.-]{+not null.+}
