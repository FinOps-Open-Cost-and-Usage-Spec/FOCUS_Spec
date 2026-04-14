## Diff

@@ -1,4 +1,7 @@
## Requirements

{+Column conforming to NullHandling attribute MUST adhere to the following requirements:+}

* [-Columns-]{+*FOCUS dataset column*+} MUST use [-NULL when there isn't a value that can be specified-]{+`null`+} for [-a nullable column.-]{+absent values when the *FOCUS dataset column* is defined as nullable.+}
* [-Columns-]{+*FOCUS dataset column*+} MUST NOT [-use-]{+contain+} empty strings or placeholder [-values such as 0-]{+strings (e.g., `Not Applicable`)+} for {+absent values when the *FOCUS dataset column* contains string values.+}
{+* *FOCUS dataset column* MUST NOT contain placeholder+} numeric [-columns or "Not Applicable"-]{+values (e.g., `0`)+} for [-string columns to represent a null or not having a value, regardless of whether-]{+absent values when+} the [-column allows nulls or not.-]{+*FOCUS dataset column* contains numeric values.+}
