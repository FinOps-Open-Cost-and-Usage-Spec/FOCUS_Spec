## Diff

@@ -1,6 +1,8 @@
## Requirements

{+Column conforming to KeyValueFormat attribute MUST adhere to the following requirements:+}

* [-Key-Value Format columns-]{+*FOCUS dataset column*+} MUST [-contain-]{+be+} a serialized JSON string, consistent with the ECMA 404 definition of an object.
* Keys in [-a key-value pair-]{+*FOCUS dataset column*+} MUST be unique within [-an-]{+the+} object.
* [-Values-]{+Key values+} in [-a key-value pair-]{+*FOCUS dataset column*+} MUST be[-one-] of [-the following types:-]{+type+} number, string, [-`true`, `false`,-]{+boolean (`true` or `false`),+} or `null`.
* [-Values-]{+Key values+} in [-a key-value pair-]{+*FOCUS dataset column*+} MUST NOT be [-an object-]{+objects+} or [-an array.-]{+arrays.+}
