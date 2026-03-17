## Diff

HostProviderName [-adheres-]{+MUST adhere+} to the following requirements:

[-* HostProviderName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* HostProviderName MUST be of type String.
* HostProviderName MUST conform to StringHandling requirements.
* HostProviderName {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * HostProviderName MAY be NULL when the associated ServiceName does not involve deployment on any underlying infrastructure (e.g., professional services, software licenses).
  * HostProviderName MAY be NULL when the information about the entity providing the underlying infrastructure cannot be uniquely determined (e.g., when the ChargeCategory is "Tax" or "Adjustment").
  * HostProviderName MUST NOT be null in all other cases.
* When HostProviderName is not null, HostProviderName values [-are defined as follows:-]{+MUST adhere to the following requirements:+}
  * HostProviderName MUST reflect the name of the host provider when explicitly selected by the customer.
  * HostProviderName MUST reflect the name of the host provider when the service provider exposes the underlying hosting provider.
  * HostProviderName MUST equal ServiceProviderName in all other cases.

