# AvailabilityZone

## Normative Text 1.2

The AvailabilityZone column adheres to the following requirements:
AvailabilityZone is RECOMMENDED to be present in a FOCUS dataset when the provider supports deploying resources or services within an availability zone.
AvailabilityZone MUST be of type String.
AvailabilityZone MUST conform to StringHandling requirements.
AvailabilityZone MUST be null when a charge is not specific to an availability zone.

## Normative Text 1.3

AvailabilityZone adheres to the following requirements:
AvailabilityZone is RECOMMENDED to be present in a Cost and Usage FOCUS dataset when the host provider supports deploying resources or services within an availability zone.
AvailabilityZone MUST be of type String.
AvailabilityZone MUST conform to StringHandling requirements.
AvailabilityZone MUST be null when a charge is not specific to an availability zone.

## Diff

-The AvailabilityZone column adheres to the following requirements:
+## Requirements

-*AvailabilityZone is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within an *availability zone*.
+AvailabilityZone adheres to the following requirements:
+
+* AvailabilityZone is RECOMMENDED to be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the host provider supports deploying resources or services within an *availability zone*.

* AvailabilityZone MUST be of type String.
* AvailabilityZone MUST conform to [StringHandling](#stringhandling) requirements.
* AvailabilityZone MUST be null when a [*charge*](#glossary:charge) is not specific to an *availability zone*.
