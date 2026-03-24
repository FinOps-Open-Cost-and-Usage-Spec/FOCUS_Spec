## Diff

[-The-]AllocatedMethodDetails [-column adheres-]{+MUST adhere+} to the following requirements:

* AllocatedMethodDetails[-SHOULD be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the data generator supports [Data Generator-Calculated Split Cost Allocation](#datagenerator-calculatedsplitcostallocationhandling).-]
[-* AllocatedMethodDetails-] MUST be of type [-String.-]{+JSON Object (serialized as a String where necessary).+}
* AllocatedMethodDetails MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* AllocatedMethodDetails MUST conform to [-[JsonObjectFormat](#jsonobjectformat)-]{+[JsonObjectFormat](#attributes.jsonobjectformat)+} requirements.
* AllocatedMethodDetails {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * AllocatedMethodDetails MUST be null when a charge is not related to a data generator-calculated split cost allocation.
  * AllocatedMethodDetails SHOULD NOT be null when a charge is related to a data generator-calculated split cost allocation.
{+* AllocatedMethodDetails MUST conform to [AllocatedMethodDetailsObject](#datasets.costandusage.allocatedmethoddetails.allocatedmethoddetailsobject) requirements when AllocatedMethodDetails is not null.+}

[-### Object Schema Requirements-]{+##+} Allocated Method Details [-consists of a valid JSON object which contains an array of key-value objects describing the one or more factors (allocation properties) that determined the split cost allocation. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the allocation.-]

[-When AllocatedMethodDetails is not null, the JsonObjectFormat for AllocatedMethodDetails adheres to the following requirements:-]
[-* AllocatedMethodDetails MUST have a top-level key "Elements" which contains an array.-]
[-* Each item in "Elements" MUST be an object.-]
[-  * Objects inside "Elements" MUST conform to [KeyValueFormat](#key-valueformat) requirements.-]
[-    * FOCUS-defined allocation properties adhere to the following additional requirements:-]
[-      * Allocation property key MUST match the spelling and casing specified for the FOCUS-defined property.-]
[-      * Allocation property value MUST be of the type specified for that property.-]
[-      * Allocation properties MUST adhere to additional normative requirements specific to that property.-]
[-    * Data generator-defined allocation properties MAY be included in "Elements".-]
[-      * Allocation property keys MUST begin with the string "x_" unless it is a FOCUS-defined allocation property.-]
[-* AllocatedMethodDetails root object MAY contain additional data generator-defined items, in addition to "Elements".-]

[-### Content Requirements-]

[-The following keys are used for allocation properties to facilitate querying data across allocations and across data generators. Focus-defined keys will appear in the list below and data generator-defined keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.-]

[-<b>Allocated Ratio</b>-]

[-Allocated Ratio communicates the percentage of the [*Origin Charge*](#glossary:origin-charge) that this [*Allocated Charge*](#glossary:allocated-charge) derived from the corresponding [Allocated Method Id](#allocatedmethodid) and Usage Unit property.-]

[-The "AllocatedRatio" property adheres to the following requirements:-]

[-* "AllocatedRatio" MUST be included inside each "Elements" object.-]
[-* Values for "AllocatedRatio" MUST be a decimal value compatible with [NumericFormat](#numericformat) representing the allocated charge's percentage of the origin charge.-]
[-* Values for all "AllocatedRatio" properties across all allocated charges related to a single origin charge MUST sum up to 1 (100%).-]{+Object+}

[-<b>Usage Unit</b>-]{+Allocated Method Details consists of a valid JSON object with a top level key of Elements containing an Array of entry objects. Each entry object consists of FOCUS-defined property keys but can be extended to provide additional details about the allocation.+}

[-Usage Unit communicates-]{+The following section details+} the [-aspect-]{+normative requirements for the AllocatedMethodDetailsObject and its nested properties. For a logical overview+} of the [-documented Allocation Method Id being used to calculate-]{+expected content, see+} the [-Allocated Ratio property-]{+[Schema Structure](#datasets.costandusage.allocatedmethoddetails.schemastructure)+} and [-what is being measured by Usage Quantity property.-]{+[Object Example](#datasets.costandusage.allocatedmethoddetails.objectexample) sections.+}

[-The "UsageUnit" property adheres to the following requirements:-]{+### Object Requirements+}

[-* "UsageUnit"-]{+The AllocatedMethodDetailsObject+} MUST [-be included inside an "Elements" object if "UsageQuantity" allocation property is included in that "Elements" object, otherwise "UsageUnit" MAY be included in each "Elements" object.-]
[-* Values for "UsageUnit" MUST capture the unit or component of data generator's documented [AllocationMethod](#allocationmethodid) that was used-]{+adhere+} to[-determine-] the [-"AllocatedRatio" value.-]
[-* Values for "UsageUnit" SHOULD conform to [UnitFormat](#unitformat) requirements.-]{+following requirements:+}

[-<b>Usage Quantity</b>-]{+* AllocatedMethodDetailsObject MUST conform to the [AllocatedMethodDetailsObjectSchema](#schemas.datasets.costandusage.allocatedmethoddetailsobjectschema) JSON Schema.+}
{+* AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio MUST represent the allocated charge's percentage of the origin charge.+}
{+* Values for all AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio properties across all allocated charges related to a single origin charge MUST sum up to 1 (100%).+}
{+* AllocatedMethodDetailsObject.Elements[\*].UsageUnit SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.+}
{+* AllocatedMethodDetailsObject.Elements[\*].UsageUnit MUST represent the unit or component of data generator's documented [AllocationMethod](#datasets.costandusage.allocatedmethodid) which was used to determine the AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio value.+}
{+* AllocatedMethodDetailsObject.Elements[\*].UsageQuantity SHOULD capture the quantity or volume of the AllocatedMethodDetailsObject.Elements[\*].UsageUnit measured by the data generator that was used to determine the AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio value.+}

