## Diff

Tags [-adheres-]{+MUST adhere+} to the following requirements:

* Tags MUST[-be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the data generator supports setting user or provider-defined tags.-]
[-* Tags MUST-] conform to KeyValueFormat requirements.
* Tags MAY be null.
* When Tags is not null, Tags [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * Tags MUST include all user-defined and provider-defined tags.
  * Tags MUST only include finalized tags.
  * Tags SHOULD include tag keys with corresponding non-null values for a given [*resource*](#glossary:resource).
@@ -19,10 +18,10 @@ Tags adheres to the following requirements:
  * Tag keys that do not support corresponding values, MUST have a corresponding true (boolean) value set.
  * Data generator SHOULD publish tag finalization methods and semantics within their respective documentation.
  * Data generator MUST NOT alter tag values unless applying true (boolean) to valueless tags.
* Provider-defined tags {+MUST+} adhere to the following[-additional-] requirements:
  * Provider-defined tag keys MUST be prefixed with a predetermined, provider-specified tag key prefix that is unique to each corresponding provider-specified tag scheme.
  * Data generator SHOULD publish all provider-specified tag key prefixes within their respective documentation.
* User-defined tags {+MUST+} adhere to the following[-additional-] requirements:
  * Data generator MUST prefix all but one user-defined tag scheme with a predetermined, provider-specified tag key prefix that is unique to each corresponding user-defined tag scheme when the data generator has more than one user-defined tag scheme.
  * Data generator MUST NOT prefix tag keys when the data generator has only one user-defined tag scheme.
  * Data generator MUST NOT allow reserved tag key prefixes to be used as prefixes for any user-defined tag keys within a prefixless user-defined tag scheme.

