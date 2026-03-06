## Diff

AvailabilityZone [-adheres-]{+MUST adhere+} to the following requirements:

[-* AvailabilityZone is RECOMMENDED to be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the host provider supports deploying resources or services within an *availability zone*.-]
* AvailabilityZone MUST be of type String.
* AvailabilityZone MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* AvailabilityZone MUST be null when a [*charge*](#glossary:charge) is not specific to an *availability zone*.

