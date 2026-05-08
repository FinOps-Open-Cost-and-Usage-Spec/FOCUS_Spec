## Diff

@@ -1,11 +1,10 @@
## Requirements

AllocatedMethodId [-adheres-]{+MUST adhere+} to the following requirements:

[-* AllocatedMethodId MUST be present in a Cost and Usage *FOCUS dataset* when the data generator supports data generator-calculated split cost allocation.-]
* AllocatedMethodId MUST be of type String.
* AllocatedMethodId MUST conform to StringHandling requirements.
* AllocatedMethodId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * AllocatedMethodId MUST be null when a *charge* is not related to a data generator-calculated split cost allocation.
  * AllocatedMethodId MUST NOT be null when a *charge* is related to a data generator-calculated split cost allocation.
* Data [-generator documentation of a-]{+generator-calculated+} split cost allocation method {+documentation+} MUST[-make-] reference[-to-] a single AllocatedMethodId value.
