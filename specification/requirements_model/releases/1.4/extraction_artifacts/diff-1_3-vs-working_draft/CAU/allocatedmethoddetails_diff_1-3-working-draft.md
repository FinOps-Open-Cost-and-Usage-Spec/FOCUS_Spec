## Diff 

diff --git a/tmp/allocatedmethoddetails_v13.md b/tmp/allocatedmethoddetails_working.md
index d18e594b..83860680 100644
--- a/tmp/allocatedmethoddetails_v13.md
+++ b/tmp/allocatedmethoddetails_working.md
@@ -2,101 +2,71 @@

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
{+* AllocatedMethodDetails MUST conform to AllocatedMethodDetailsObject requirements when AllocatedMethodDetails is not null.+}

[-### Object Schema Requirements-]{+##+} Allocated Method Details [-consists of a valid JSON object which contains an array of key-value objects describing the one or more factors (allocation properties) that determined the split cost allocation. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the allocation.-]

[-When AllocatedMethodDetails is not null, the JsonObjectFormat for AllocatedMethodDetails adheres to the following requirements:-]
[-* AllocatedMethodDetails MUST have a top-level key "Elements" which contains an array.-]
[-* Each item in "Elements" MUST be an object.-]
[-  * Objects inside "Elements" MUST conform to KeyValueFormat requirements.-]
[-    * FOCUS-defined allocation properties adhere to the following additional requirements:-]
[-      * Allocation property key MUST match the spelling and casing specified for the FOCUS-defined property.-]
[-      * Allocation property value MUST be of the type specified for that property.-]
[-      * Allocation properties MUST adhere to additional normative requirements specific to that property.-]
[-    * Data generator-defined allocation properties MAY be included in "Elements".-]
[-      * Allocation property keys MUST begin with the string "x_" unless it is a FOCUS-defined allocation property.-]
[-* AllocatedMethodDetails root object MAY contain additional data generator-defined items, in addition to "Elements".-]

[-### Content Requirements-]{+Object+}

[-The following keys are used for allocation properties to facilitate querying data across allocations and across data generators. Focus-defined keys will appear in the list below and data generator-defined-]{+Allocated Method Details consists of a valid JSON object with a top level key of Elements containing an Array of entry objects. Each entry object consists of FOCUS-defined property+} keys [-will-]{+but can+} be [-prefixed with "x_"-]{+extended+} to [-make them easy to identify as well as prevent collisions.-]{+provide additional details about the allocation.+}

[-<b>Allocated Ratio</b>-]{+The following section details the normative requirements for the AllocatedMethodDetailsObject and its nested properties. For a logical overview of the expected content, see the Schema Structure and Object Example sections.+}

[-Allocated Ratio communicates the percentage of the *Origin Charge* that this *Allocated Charge* derived from the corresponding Allocated Method Id and Usage Unit property.-]{+### Object Requirements+}

The [-"AllocatedRatio" property adheres-]{+AllocatedMethodDetailsObject MUST adhere+} to the following requirements:

* [-"AllocatedRatio"-]{+AllocatedMethodDetailsObject+} MUST [-be included inside each "Elements" object.-]{+conform to the AllocatedMethodDetailsObjectSchema JSON Schema.+}
* [-Values for "AllocatedRatio"-]{+AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio+} MUST [-be a decimal value compatible with NumericFormat representing-]{+represent+} the allocated charge's percentage of the origin charge.
* [-Values for all "AllocatedRatio" properties-]{+The sum of AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio+} across all allocated charges related to a single origin charge MUST [-sum up-]{+be equal+} to 1 (100%).
{+* AllocatedMethodDetailsObject.Elements[\*].UsageUnit SHOULD conform to UnitFormat requirements.+}
{+* AllocatedMethodDetailsObject.Elements[\*].UsageUnit MUST represent the unit or component of data generator's documented AllocationMethod which was used to determine the AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio value.+}
{+* AllocatedMethodDetailsObject.Elements[\*].UsageQuantity SHOULD capture the quantity or volume of the AllocatedMethodDetailsObject.Elements[\*].UsageUnit measured by the data generator that was used to determine the AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio value.+}

[-<b>Usage Unit</b>-]{+### Object Schema Structure+}

[-Usage Unit communicates-]{+AllocatedMethodDetails contains a structured JSON object defining+} the [-aspect of the documented Allocation Method Id being-]{+allocation properties+} used to calculate [-the Allocated Ratio property and what is being measured by Usage Quantity property.-]{+a split cost allocation.+}

[-The "UsageUnit" property adheres to the following requirements:-]{+<div class="h7-nonindex">Top-Level Properties</div>+}

[-* "UsageUnit" MUST be included inside an "Elements" object if "UsageQuantity" allocation property is included in that "Elements" object, otherwise "UsageUnit" MAY be included in each "Elements" object.-]
[-* Values for "UsageUnit" MUST capture the unit-]{+| Property | Type | Required | Description |+}
{+| :--- | :--- | :--- | :--- |+}
{+| `Elements` | Array | True | The parent array containing one+} or [-component of data generator's documented AllocationMethod that-]{+more objects which communicate information about how an allocated record+} was [-used to determine the "AllocatedRatio" value.-]
[-* Values for "UsageUnit" SHOULD conform to UnitFormat requirements.-]{+calculated. |+}

[-<b>Usage Quantity</b>-]{+<div class="h7-nonindex">Elements Object</div>+}

[-Usage Quantity communicates the volume that was consumed or used, denominated in the Usage Unit property value.-]The [-"UsageQuantity" property adheres to the following requirements:-]

[-* "UsageQuantity" MAY be included inside an "Elements" object when that "Elements" object-]{+`Elements` array+} contains [-a "UsageUnit" allocation property.-]
[-* Values for "UsageQuantity" MUST be compatible with NumericFormat.-]
[-* Values for "UsageQuantity" SHOULD capture the quantity-]{+one+} or [-volume-]{+more objects, each+} of {+which contains+} the [-"UsageUnit" measured by the data generator that was used to determine the "AllocatedRatio" value.-]