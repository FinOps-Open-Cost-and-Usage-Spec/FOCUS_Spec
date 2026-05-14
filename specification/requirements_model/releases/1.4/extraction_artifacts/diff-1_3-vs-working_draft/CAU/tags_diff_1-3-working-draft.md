## Diff

@@ -1,22 +1,25 @@
## Requirements

Tags [-adheres-]{+MUST adhere+} to the following requirements:

* Tags MUST be [-present in-]{+of type JSON Object (serialized as+} a [-Cost and Usage *FOCUS dataset* when the data generator supports setting user or provider-defined tags.-]{+String where necessary).+}
{+* Tags MUST conform to StringHandling requirements.+}
* Tags MUST conform to KeyValueFormat requirements.
* Tags MAY be null.
* When Tags is not null, Tags [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * Tags MUST include all user-defined and provider-defined tags.
  * Tags MUST only include finalized tags.
  * Tags SHOULD include tag keys with corresponding non-null values for a given *resource*.
  * Tags MAY include tag keys with a null value for a given *resource* depending on the data generator's tag finalization process.
  * Tag keys that do not support corresponding values, MUST have a corresponding true (boolean) value set.
  * [-Data generator SHOULD publish tag finalization methods and semantics within their respective documentation.-]
[-  * Data generator-]{+Tag values+} MUST [-NOT alter tag-]{+match the provided+} values unless[-applying-] true (boolean) {+is applied+} to valueless tags.
* Provider-defined tags {+MUST+} adhere to the following[-additional-] requirements:
  * Provider-defined tag keys MUST be prefixed with a predetermined, provider-specified tag key prefix that is unique to each corresponding provider-specified [-tag scheme.-]{+*tag scheme*.+}
  * [-Data generator SHOULD publish all provider-specified-]{+Provider-specified+} tag key prefixes [-within their respective documentation.-]{+SHOULD be publicly documented.+}
* User-defined tags {+MUST+} adhere to the following[-additional-] requirements:
  * [-Data generator MUST prefix-]{+User-defined tag keys in+} all but one user-defined [-tag scheme with-]{+*tag scheme* MUST include+} a predetermined, provider-specified tag key prefix that is unique to each corresponding user-defined [-tag scheme-]{+*tag scheme*+} when the data generator has more than one user-defined [-tag scheme.-]{+*tag scheme*.+}
  * [-Data generator-]{+User-defined tag keys+} MUST NOT {+include a *tag scheme*-specific+} prefix[-tag keys-] when the data generator has only one user-defined [-tag scheme.-]{+*tag scheme*.+}
  * [-Data generator MUST NOT allow reserved-]{+Reserved+} tag key prefixes [-to-]{+MUST+} be {+prevented from being+} used as prefixes for any user-defined tag keys within a prefixless user-defined {+*tag scheme*.+}
{+* Tag finalization documentation MUST adhere to the following requirements:+}
{+  * Tag finalization documentation SHOULD include+} tag [-scheme.-]{+finalization methods and semantics.+}
{+  * Tag finalization documentation SHOULD be accessible to practitioners.+}
