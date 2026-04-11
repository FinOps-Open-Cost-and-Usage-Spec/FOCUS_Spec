## Diff

@@ -1,8 +1,12 @@
## Requirements

ChargeCategory [-adheres-]{+MUST adhere+} to the following requirements:

[-* ChargeCategory MUST be present in a Cost and Usage *FOCUS dataset*.-]
* ChargeCategory MUST be of type String.
* ChargeCategory MUST NOT be null.
* ChargeCategory MUST be one of the allowed values.
{+* ChargeCategory MUST be "Usage" when the *charge* represents consumption of a service or resource.+}
{+* ChargeCategory MUST be "Purchase" when the *charge* represents acquisition of a service, resource, or *commitment*.+}
{+* ChargeCategory MUST be "Tax" when the *charge* represents taxes levied by the relevant authorities.+}
{+* ChargeCategory MUST be "Credit" when the *charge* represents a financial incentive or allowance unrelated to other charges.+}
{+* ChargeCategory MUST be "Adjustment" when the *charge* represents a billing modification that does not fall into other ChargeCategories.+}
