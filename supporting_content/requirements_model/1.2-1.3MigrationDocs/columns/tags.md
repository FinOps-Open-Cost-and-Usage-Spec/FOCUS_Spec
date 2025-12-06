## Tags

### Normative Text v1.2

The Tags column adheres to the following requirements:

* Tags MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports setting user or provider-defined tags.
* Tags MUST conform to [KeyValueFormat](#key-valueformat) requirements.
* Tags MAY be null.
* When Tags is not null, Tags adheres to the following additional requirements:
  * Tags MUST include all user-defined and provider-defined tags.
  * Tags MUST only include finalized tags.
  * Tags SHOULD include tag keys with corresponding non-null values for a given [*resource*](#glossary:resource).
  * Tags MAY include tag keys with a null value for a given *resource* depending on the provider's tag finalization process.
  * Tag keys that do not support corresponding values, MUST have a corresponding true (boolean) value set.
  * Provider SHOULD publish tag finalization methods and semantics within their respective documentation.
  * Provider MUST NOT alter tag values unless applying true (boolean) to valueless tags.
* Provider-defined tags adhere to the following additional requirements:
  * Provider-defined tag keys MUST be prefixed with a predetermined, provider-specified tag key prefix that is unique to each corresponding provider-specified tag scheme.
  * Provider SHOULD publish all provider-specified tag key prefixes within their respective documentation.
* User-defined tags adhere to the following additional requirements:
  * Provider MUST prefix all but one user-defined tag scheme with a predetermined, provider-specified tag key prefix that is unique to each corresponding user-defined tag scheme when the provider has more than one user-defined tag scheme.
  * Provider MUST NOT prefix tag keys when the provider has only one user-defined tag scheme.
  * Provider MUST NOT allow reserved tag key prefixes to be used as prefixes for any user-defined tag keys within a prefixless user-defined tag scheme.

### Normative Text v1.3

## Requirements

Tags adheres to the following requirements:

* Tags MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the data generator supports setting user or provider-defined tags.
* Tags MUST conform to [KeyValueFormat](#key-valueformat) requirements.
* Tags MAY be null.
* When Tags is not null, Tags adheres to the following additional requirements:
  * Tags MUST include all user-defined and provider-defined tags.
  * Tags MUST only include finalized tags.
  * Tags SHOULD include tag keys with corresponding non-null values for a given [*resource*](#glossary:resource).
  * Tags MAY include tag keys with a null value for a given *resource* depending on the data generator's tag finalization process.
  * Tag keys that do not support corresponding values, MUST have a corresponding true (boolean) value set.
  * Data generator SHOULD publish tag finalization methods and semantics within their respective documentation.
  * Data generator MUST NOT alter tag values unless applying true (boolean) to valueless tags.
* Provider-defined tags adhere to the following additional requirements:
  * Provider-defined tag keys MUST be prefixed with a predetermined, provider-specified tag key prefix that is unique to each corresponding provider-specified tag scheme.
  * Data generator SHOULD publish all provider-specified tag key prefixes within their respective documentation.
* User-defined tags adhere to the following additional requirements:
  * Data generator MUST prefix all but one user-defined tag scheme with a predetermined, provider-specified tag key prefix that is unique to each corresponding user-defined tag scheme when the data generator has more than one user-defined tag scheme.
  * Data generator MUST NOT prefix tag keys when the data generator has only one user-defined tag scheme.
  * Data generator MUST NOT allow reserved tag key prefixes to be used as prefixes for any user-defined tag keys within a prefixless user-defined tag scheme.

### Diff

-The Tags column adheres to the following requirements:
+## Requirements
 
-* Tags MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports setting user or provider-defined tags.
+Tags adheres to the following requirements:
+
+* Tags MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the data generator supports setting user or provider-defined tags.
 * Tags MUST conform to [KeyValueFormat](#key-valueformat) requirements.
 * Tags MAY be null.
 * When Tags is not null, Tags adheres to the following additional requirements:
   * Tags MUST include all user-defined and provider-defined tags.
   * Tags MUST only include finalized tags.
   * Tags SHOULD include tag keys with corresponding non-null values for a given [*resource*](#glossary:resource).
-  * Tags MAY include tag keys with a null value for a given *resource* depending on the provider's tag finalization process.
+  * Tags MAY include tag keys with a null value for a given *resource* depending on the data generator's tag finalization process.
   * Tag keys that do not support corresponding values, MUST have a corresponding true (boolean) value set.
-  * Provider SHOULD publish tag finalization methods and semantics within their respective documentation.
-  * Provider MUST NOT alter tag values unless applying true (boolean) to valueless tags.
+  * Data generator SHOULD publish tag finalization methods and semantics within their respective documentation.
+  * Data generator MUST NOT alter tag values unless applying true (boolean) to valueless tags.
 * Provider-defined tags adhere to the following additional requirements:
   * Provider-defined tag keys MUST be prefixed with a predetermined, provider-specified tag key prefix that is unique to each corresponding provider-specified tag scheme.
-  * Provider SHOULD publish all provider-specified tag key prefixes within their respective documentation.
+  * Data generator SHOULD publish all provider-specified tag key prefixes within their respective documentation.
 * User-defined tags adhere to the following additional requirements:
-  * Provider MUST prefix all but one user-defined tag scheme with a predetermined, provider-specified tag key prefix that is unique to each corresponding user-defined tag scheme when the provider has more than one user-defined tag scheme.
-  * Provider MUST NOT prefix tag keys when the provider has only one user-defined tag scheme.
-  * Provider MUST NOT allow reserved tag key prefixes to be used as prefixes for any user-defined tag keys within a prefixless user-defined tag scheme.
+  * Data generator MUST prefix all but one user-defined tag scheme with a predetermined, provider-specified tag key prefix that is unique to each corresponding user-defined tag scheme when the data generator has more than one user-defined tag scheme.
+  * Data generator MUST NOT prefix tag keys when the data generator has only one user-defined tag scheme.
+  * Data generator MUST NOT allow reserved tag key prefixes to be used as prefixes for any user-defined tag keys within a prefixless user-defined tag scheme.