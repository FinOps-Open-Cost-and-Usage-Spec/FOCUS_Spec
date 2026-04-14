## Diff

@@ -1,13 +1,13 @@
## Requirements

[-*-]{+Column conforming to+} JsonObjectFormat [-columns-]{+attribute MUST adhere to the following requirements:+}

{+* *FOCUS dataset column*+} MUST contain a serialized JSON string, consistent with the ECMA 404 definition of an object.
* [-Objects used within JsonObjectFormat adhere-]{+*FOCUS dataset column* MUST conform+} to {+all requirements of+} the [-following additional requirements:-]{+corresponding column definition, which may specify or restrict the shape or contents of the object.+}
{+* Object in *FOCUS dataset column* SHOULD NOT exceed 3 levels of nesting.+}
* {+Key in+} Object [-keys-]{+in *FOCUS dataset column*+} MUST be [-unique within an object.-]{+unique.+}
* {+Key value in+} Object [-values-]{+in *FOCUS dataset column*+} MUST be[-one-] of [-the following types:-]{+type+} number, string, [-`true`, `false`,-]{+boolean (`true` or `false`),+} array, object, or `null`.
* [-Arrays used within JsonObjectFormat-]{+Object in array in *FOCUS dataset column* MUST+} adhere to the following[-additional-] requirements:
  * [-Array elements-]{+Object in array in *FOCUS dataset column*+} MUST [-all use the same,-]{+be of a+} consistent type.
  * [-Array elements-]{+Object in array in *FOCUS dataset column*+} MUST NOT be repeated.
  * [-Array elements-]{+Object in array in *FOCUS dataset column*+} MUST NOT be null.[-* JsonObjectFormat columns MUST conform to all requirements of the corresponding column definition, which may specify or restrict the shape or contents of the Object.-]
[-* Data Generator-defined custom columns whose contents contain a JSON object MUST have their object schema documented by the data generator.-]
[-* JsonObjectFormat objects SHOULD NOT exceed 3 levels of nesting.-]
