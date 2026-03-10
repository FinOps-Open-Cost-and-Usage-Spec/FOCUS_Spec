## Diff

RegionId [-adheres-]{+MUST adhere+} to the following requirements:

[-* RegionId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the host provider supports deploying resources or services within a region.-]
* RegionId MUST be of type String.
* RegionId MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* RegionId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * RegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region.
  * RegionId MAY be null when a *resource* or *service* is not operated in or managed from a distinct region.

