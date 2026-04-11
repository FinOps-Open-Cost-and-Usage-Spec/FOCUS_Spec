## Diff

@@ -1,6 +1,15 @@
## Requirements

{+Column conforming to StringHandling attribute MUST adhere to the following requirements:+}

* [-String values-]{+*FOCUS dataset column* MUST preserve the original casing of string values.+}
{+* *FOCUS dataset column*+} MUST [-maintain-]{+preserve+} the original [-casing, spacing, and-]{+spacing of string values.+}
{+* *FOCUS dataset column* MUST preserve+} other relevant consistency factors as specified by {+the+} data [-generators and end-users.-]{+generator or end-user.+}
* [-*Charges* to-]{+*FOCUS dataset column* MUST remain consistent across all *billing periods* when the *FOCUS dataset column* contains immutable string values (e.g., resource identifier, region identifier).+}
{+* When *FOCUS dataset column* contains+} mutable [-entities-]{+string values+} (e.g., resource [-names)-]{+name, region name), it+} MUST [-be accurately reflected-]{+adhere to the following requirements:+}
{+  * *FOCUS dataset column* MUST reflect the altered value+} in [-corresponding *charges* incurred-]{+all records pertaining to a period+} after the [-change and-]{+change.+}
{+  * *FOCUS dataset column*+} MUST [-NOT alter *charges* incurred before-]{+reflect+} the [-change, preserving data integrity and auditability for-]{+string value as it existed prior to the change in+} all [-*charge* records.-]{+records pertaining to a period prior to the change when the record does not represent a correction to a previously closed billing period.+}
  * [-Immutable string values that refer-]{+*FOCUS dataset column* MAY reflect the altered value in records pertaining to a period prior+} to the [-same entity (e.g., resource identifiers, region identifiers, etc.)-]{+change when the record represents a correction to a previously closed billing period.+}
{+* When *FOCUS dataset column* contains not-nullable string values, it+} MUST [-remain consistent and unchanged across all *billing periods*.-]{+adhere to the following requirements:+}
  * [-Empty strings and-]{+*FOCUS dataset column* SHOULD NOT contain empty strings.+}
{+  * *FOCUS dataset column* SHOULD NOT contain+} strings consisting solely of [-spaces SHOULD NOT be used in not-nullable string columns.-]{+whitespace characters.+}
