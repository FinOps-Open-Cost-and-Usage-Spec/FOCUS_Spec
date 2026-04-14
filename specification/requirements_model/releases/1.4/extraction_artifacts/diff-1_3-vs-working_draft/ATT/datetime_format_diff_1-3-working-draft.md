## Diff

@@ -1,8 +1,11 @@
## Requirements

{+Column conforming to DateTimeFormat attribute MUST adhere to the following requirements:+}

* [-Date/time values-]{+*FOCUS dataset column*+} MUST be {+expressed+} in UTC (Coordinated Universal Time) to avoid ambiguity and ensure consistency across different time zones.
* [-Date/time values format-]{+*FOCUS dataset column*+} MUST [-be aligned with-]{+conform to the+} ISO 8601 standard, which provides a globally recognized format for representing dates and times (see ISO 8601-1:2019 governing document for details).
* [-Values providing information about-]{+When *FOCUS dataset column* represents+} a specific moment in [-time-]{+time, it+} MUST [-be represented in-]{+adhere to the following requirements:+}
{+  * *FOCUS dataset column* MUST use+} the extended ISO 8601 format with UTC offset [-('YYYY-MM-DDTHH:mm:ssZ') and conform to the following guidelines:-]{+(`YYYY-MM-DDTHH:mm:ssZ`).+}
  * [-Include-]{+*FOCUS dataset column* MUST include both+} the date and time components, separated with the letter [-'T'-]{+`T`.+}
  * [-Use-]{+*FOCUS dataset column* MUST use+} two-digit hours [-(HH),-]{+(`HH`),+} minutes [-(mm),-]{+(`mm`),+} and seconds [-(ss).-]{+(`ss`).+}
  * [-End-]{+*FOCUS dataset column* MUST end+} with the [-'Z' indicator to denote-]{+ISO 8601+} UTC [-(Coordinated Universal Time)-]{+designator `Z`.+}
