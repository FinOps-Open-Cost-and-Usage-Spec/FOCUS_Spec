## Diff

@@ -1,4 +1,6 @@
## Requirements

{+Column conforming to CurrencyFormat attribute MUST adhere to the following requirements:+}

* [-Currency-related columns-]{+*FOCUS dataset column*+} MUST [-be represented as a-]{+conform to ISO 4217:2015 standard.+}
{+* *FOCUS dataset column* MUST use the+} three-letter alphabetic code [-as dictated-]{+defined+} in[-the governing document-] ISO 4217:2015[-when the value is presented in national currency-] (e.g., USD, EUR).[-* Currency-related columns MUST conform to StringHandling requirements when the value is presented in virtual currency (e.g., credits, tokens).-]
