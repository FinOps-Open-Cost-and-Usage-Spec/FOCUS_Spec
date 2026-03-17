## Diff

RegionName [-adheres-]{+MUST adhere+} to the following requirements:

[-* RegionName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the host provider supports deploying resources or services within a region.-]
* RegionName MUST be of type String.
* RegionName MUST conform to StringHandling requirements.
* RegionName {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * RegionName MUST be null when RegionId is null.
  * RegionName MUST NOT be null when RegionId is not null.

