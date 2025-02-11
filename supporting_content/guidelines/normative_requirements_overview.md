# Column Normative Requirements Overview

## Column: Availability Zone

### **Availability Zone Cost v.1.2 (Simplified Refinement)**

The AvailabilityZone column adheres to the following requirements:

* AvailabilityZone is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within an *availability zone*.
* AvailabilityZone MUST be of type String.
* AvailabilityZone MUST conform to [String Handling](#stringhandling) requirements.
* AvailabilityZone nullability is defined as follows:
  * AvailabilityZone MAY be null when a charge is not specific to an *availability zone*.

### **Availability Zone v.1.2 (Technical Refinement)**

The AvailabilityZone column adheres to the following requirements:

* AvailabilityZone is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within an *availability zone*.
* If present, AvailabilityZone adheres to the following additional requirements:
  * AvailabilityZone MUST be of type String.
  * AvailabilityZone MUST conform to [String Handling](#stringhandling) requirements.
  * AvailabilityZone MAY be null if a charge is not specific to an *availability zone*.

### **Availability Zone v.1.1 (Original)**

The AvailabilityZone column adheres to the following requirements:

* The AvailabilityZone column is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within an *availability zone*.
* This column MUST be of type String and MAY contain null values when a charge is not specific to an *availability zone*.

## Column: Billed Cost

### **Billed Cost v.1.2 (Simplified Refinement)**

The BilledCost column adheres to the following requirements:

* BilledCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BilledCost MUST be of type Decimal.
* BilledCost MUST conform to [Numeric Format](#numericformat) requirements.
* BilledCost nullability is defined as follows:
  * BilledCost MUST NOT be null.
* BilledCost MUST be a valid decimal value.
* BilledCost MUST be denominated in the BillingCurrency.
* The sum of the BilledCost for [*rows*](#glossary:row) in a given [*billing period*](#glossary:billing-period) MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

### **Billed Cost v.1.2 (Technical Refinement)**

The BilledCost column adheres to the following requirements:

* BilledCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BilledCost MUST be of type Decimal.
* BilledCost MUST conform to [Numeric Format](#numericformat) requirements.
* BilledCost MUST NOT be null.
* BilledCost MUST be a valid decimal value.
* BilledCost MUST be denominated in the BillingCurrency.
* The sum of the BilledCost for [*rows*](#glossary:row) in a given [*billing period*](#glossary:billing-period) MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

### **Billed Cost v.1.1 (Original)**

The BilledCost column adheres to the following requirements:

* The BilledCost column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null.
* This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat), and be denominated in the BillingCurrency.
* The sum of the BilledCost for [*rows*](#glossary:row) in a given [*billing period*](#glossary:billing-period) MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

## Column: Billing Account ID

### **Billing Account ID v.1.2 (Simplified Refinement)**

The BillingAccountId column adheres to the following requirements:

* BillingAccountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingAccountId MUST be of type String.
* BillingAccountId MUST conform to [String Handling](#stringhandling) requirements.
* BillingAccountId nullability is defined as follows:
  * BillingAccountId MUST NOT be null.
* BillingAccountId MUST ensure global uniqueness within a provider.

### **Billing Account ID v.1.2 (Technical Refinement)**

The BillingAccountId column adheres to the following requirements:

* BillingAccountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingAccountId MUST be of type String.
* BillingAccountId MUST conform to [String Handling](#stringhandling) requirements.
* BillingAccountId MUST NOT be null.
* BillingAccountId MUST be a globally unique identifier within a provider.

### **Billing Account ID v.1.1 (Original)**

The BillingAccountId column adheres to the following requirements:

* The BillingAccountId column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type String and MUST NOT contain null values.
* BillingAccountId MUST be a globally unique identifier within a provider.

## Column: Billing Account Name

### **Billing Account Name v.1.2 (Simplified Refinement)**

The BillingAccountName column adheres to the following requirements:

* BillingAccountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingAccountName MUST be of type String.
* BillingAccountName MUST conform to [String Handling](#stringhandling) requirements.
* BillingAccountName nullability is defined as follows:
  * BillingAccountName MUST NOT be null when the provider supports assigning a display name for the *billing account*.
* When BillingAccountName is not null, BillingAccountName adheres to the following additional requirement:
  * BillingAccountName MUST ensure uniqueness within a customer.

### **Billing Account Name v.1.2 (Technical Refinement)**

The BillingAccountName column adheres to the following requirements:

* BillingAccountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingAccountName MUST be of type String.
* BillingAccountName MUST conform to [String Handling](#stringhandling) requirements.
* BillingAccountName MUST NOT be null when the provider supports assigning a display name for the *billing account*.
* BillingAccountName MUST be unique within a customer.

### **Billing Account Name v.1.1 (Original)**

The BillingAccountName column adheres to the following requirements:

* The BillingAccountName column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null when the provider supports assigning a display name for the *billing account*.
* This column MUST be of type String.
* BillingAccountName MUST be unique within a customer when a customer has more than one *billing account*.

## Column: Billing Currency

### **Billing Currency v.1.2 (Simplified Refinement)**

The BillingCurrency column adheres to the following requirements:

* BillingCurrency MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingCurrency MUST be of type String.
* BillingCurrency MUST conform to [Currency Code Format](#currencycodeformat) requirements.
* BillingCurrency nullability is defined as follows:
  * BillingCurrency MUST NOT be null.
* BillingCurrency MUST match the currency used in the invoice generated by the invoice issuer.

### **Billing Currency v.1.2 (Technical Refinement)**

The BillingCurrency column adheres to the following requirements:

* BillingCurrency MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingCurrency MUST be of type String.
* BillingCurrency MUST conform to [Currency Code Format](#currencycodeformat) requirements.
* BillingCurrency MUST NOT be null.
* BillingCurrency MUST match the currency used in the invoice generated by the invoice issuer.

### **Billing Currency v.1.1 (Original)**

The BillingCurrency column adheres to the following requirements:

* The BillingCurrency column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingCurrency MUST match the currency used in the invoice generated by the invoice issuer.
* This column MUST be of type String and MUST NOT contain null values.
* BillingCurrency MUST conform to [Currency Code Format](#currencycodeformat) requirements.

## Column: Billing Period End

### **Billing Period End v.1.2 (Simplified Refinement)**

The BillingPeriodEnd column adheres to the following requirements:

* BillingPeriodEnd MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingPeriodEnd MUST be of type Date/Time.
* BillingPeriodEnd MUST conform to [Date/Time Format](#date/timeformat) requirements.
* BillingPeriodEnd nullability is defined as follows:
  * BillingPeriodEnd MUST NOT be null.
* BillingPeriodEnd MUST be the *exclusive ending bound* of the *billing period*.
* The sum of the [BilledCost](#billedcost) for [*rows*](#glossary:row) in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

### **Billing Period End v.1.2 (Technical Refinement)**

The BillingPeriodEnd column adheres to the following requirements:

* BillingPeriodEnd MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingPeriodEnd MUST be of type Date/Time.
* BillingPeriodEnd MUST conform to [Date/Time Format](#date/timeformat) requirements.
* BillingPeriodEnd MUST NOT be null.
* BillingPeriodEnd MUST be the *exclusive ending bound* of the *billing period*.
* The sum of the [BilledCost](#billedcost) for [*rows*](#glossary:row) in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

### **Billing Period End v.1.1 (Original)**

The BillingPeriodEnd column adheres to the following requirements:

* The BillingPeriodEnd column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type [Date/Time Format](#date/timeformat), MUST be an *exclusive* value, and MUST NOT contain null values.
* The sum of the [BilledCost](#billedcost) column for [*rows*](#glossary:row) in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

## Column: Billing Period Start

### **Billing Period Start v.1.2 (Simplified Refinement)**

The BillingPeriodStart column adheres to the following requirements:

* BillingPeriodStart MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingPeriodStart MUST be of type Date/Time.
* BillingPeriodStart MUST conform to [Date/Time Format](#date/timeformat) requirements.
* BillingPeriodStart nullability is defined as follows:
  * BillingPeriodStart MUST NOT be null.
* BillingPeriodStart MUST be the *inclusive beginning bound* of the *billing period*.
* The sum of the [BilledCost](#billedcost) for [*rows*](#glossary:row) in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

### **Billing Period Start v.1.2 (Technical Refinement)**

The BillingPeriodStart column adheres to the following requirements:

* BillingPeriodStart MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingPeriodStart MUST be of type Date/Time.
* BillingPeriodStart MUST conform to [Date/Time Format](#date/timeformat) requirements.
* BillingPeriodStart MUST NOT be null.
* BillingPeriodStart MUST be the *inclusive beginning bound* of the *billing period*.
* The sum of the [BilledCost](#billedcost) for [*rows*](#glossary:row) in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

### **Billing Period Start v.1.1 (Original)**

The BillingPeriodStart column adheres to the following requirements:

* The BillingPeriodStart column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset), MUST be of type [Date/Time Format](#date/timeformat), MUST be an *inclusive* value, and MUST NOT contain null values.
* The sum of the [BilledCost](#billedcost) metric for [*rows*](#glossary:row) in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

## Column: Capacity Reservation ID

### **Capacity Reservation ID v.1.2 (Simplified Refinement)**

The CapacityReservationId column adheres to the following requirements:

* CapacityReservationId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *capacity reservations*.
* CapacityReservationId MUST be of type String.
* CapacityReservationId MUST conform to [String Handling](#stringhandling) requirements.
* CapacityReservationId nullability is defined as follows:
  * CapacityReservationId MUST be null when a charge is not related to a *capacity reservation*.
  * CapacityReservationId MUST NOT be null when a charge represents the unused portion of a *capacity reservation*.
  * CapacityReservationId SHOULD NOT be null when a charge is related to a capacity reservation.
* When CapacityReservationId is not null, CapacityReservationId adheres to the following additional requirements:
  * CapacityReservationId MUST ensure global uniqueness within the provider.
  * CapacityReservationId SHOULD be a fully-qualified identifier.

### **Capacity Reservation ID v.1.2 (Technical Refinement)**

The CapacityReservationId column adheres to the following requirements:

* CapacityReservationId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *capacity reservations*.
* If present, CapacityReservationId adheres to the following additional requirements:
  * CapacityReservationId MUST be of type String.
  * CapacityReservationId MUST conform to [String Handling](#stringhandling) requirements.
  * CapacityReservationId MUST be null when a charge is not related to a *capacity reservation*.
  * CapacityReservationId SHOULD NOT be null when a charge is related to a capacity reservation.
  * CapacityReservationId MUST NOT be null when a charge represents the unused portion of a *capacity reservation*.
  * CapacityReservationId MUST ensure global uniqueness within the provider.
  * CapacityReservationId SHOULD be a fully-qualified identifier.

### **Capacity Reservation ID v.1.1 (Original)**

The CapacityReservationId column adheres to the following requirements:

* CapacityReservationId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *capacity reservations* and MUST be of type String.
* CapacityReservationId SHOULD NOT be null when a charge is related to a capacity reservation.
* CapacityReservationId MUST NOT be null when a charge represents the unused portion of a *capacity reservation*.
* CapacityReservationId MUST be null when a charge is not related to a *capacity reservation*.
* CapacityReservationId MUST ensure global uniqueness within the provider and SHOULD be a fully-qualified identifier.

## Column: Capacity Reservation Status

### **Capacity Reservation Status v.1.2 (Simplified Refinement)**

The CapacityReservationStatus column adheres to the following requirements:

* CapacityReservationStatus MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *capacity reservations*.
* CapacityReservationStatus MUST be of type String.
* CapacityReservationStatus nullability is defined as follows:
  * CapacityReservationStatus MUST be null if CapacityReservationId is null.
  * CapacityReservationStatus MUST NOT be null when CapacityReservationId is not null and [ChargeCategory](#chargecategory) is "Usage".
* When CapacityReservationStatus is not null, CapacityReservationStatus adheres to the following additional requirements:
  * CapacityReservationStatus MUST be one of the allowed values.
  * CapacityReservationStatus MUST be "Unused" when the charge represents the unused portion of a *capacity reservation*.
  * CapacityReservationStatus MUST be "Used" when the charge represents the used portion of a *capacity reservation*.

### **Capacity Reservation Status v.1.2 (Technical Refinement)**

The CapacityReservationStatus column adheres to the following requirements:

* CapacityReservationStatus MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *capacity reservations*.
* If present, CapacityReservationStatus adheres to the following additional requirements:
  * CapacityReservationStatus MUST be of type String.
  * CapacityReservationStatus MUST be null if CapacityReservationId is null.
  * If CapacityReservationId is not null and [ChargeCategory](#chargecategory) is "Usage", CapacityReservationStatus adheres to the following additional requirements:
    * CapacityReservationStatus MUST NOT be null.
    * CapacityReservationStatus MUST be one of the allowed values.
    * CapacityReservationStatus MUST be "Unused" when the charge represents the unused portion of a *capacity reservation*.
    * CapacityReservationStatus MUST be "Used" when the charge represents the used portion of a *capacity reservation*.

### **Capacity Reservation Status v.1.1 (Original)**

The CapacityReservationStatus column adheres to the following requirements:

* CapacityReservationStatus MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *capacity reservations* and MUST be of type String.
* CapacityReservationStatus MUST be null when CapacityReservationId is null.
* CapacityReservationStatus MUST NOT be null when CapacityReservationId is not null and [ChargeCategory](#chargecategory) is "Usage".
* CapacityReservationStatus MUST be one of the allowed values.
* CapacityReservationStatus MUST label all unused *capacity reservation* charges and MUST label used *capacity reservation* charges if the provider supports it.

## Column: Charge Category

### **Charge Category v.1.2 (Simplified Refinement)**

The ChargeCategory column adheres to the following requirements:

* ChargeCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargeCategory MUST be of type String.
* ChargeCategory nullability is defined as follows:
  * ChargeCategory MUST NOT be null.
* ChargeCategory MUST be one of the allowed values.

### **Charge Category v.1.2 (Technical Refinement)**

The ChargeCategory column adheres to the following requirements:

* ChargeCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargeCategory MUST be of type String.
* ChargeCategory MUST NOT be null.
* ChargeCategory MUST be one of the allowed values.

### **Charge Category v.1.1 (Original)**

The ChargeCategory column adheres to the following requirements:

* The ChargeCategory column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null.
* This column is of type String and MUST be one of the allowed values.

## Column: Charge Class

## Column: Charge Description

## Column: Charge Frequency

## Column: Charge Period End

## Column: Charge Period Start

## Column: Commitment Discount Category

## Column: Commitment Discount ID

## Column: Commitment Discount Name

## Column: Commitment Discount Status

## Column: Commitment Discount Type

## Column: Commitment Discount Quantity

### **CommitmentDiscountQuantity v.1.2 (Simplified Refinement)**

The CommitmentDiscountQuantity column adheres to the following requirements:

* CommitmentDiscountQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountQuantity MUST be of type Decimal.
* CommitmentDiscountQuantity MUST conform to [Numeric Format](#numericformat) requirements.
* CommitmentDiscountQuantity nullability is defined as follows:
  * When ChargeCategory is "Usage" or "Purchase" and CommitmentDiscountId is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
    * CommitmentDiscountQuantity MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction".
    * CommitmentDiscountQuantity MAY be null when ChargeClass is "Correction".
  * CommitmentDiscountQuantity MUST be null in all other cases.
* When CommitmentDiscountQuantity is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
  * CommitmentDiscountQuantity MUST be a valid decimal value.
  * When ChargeCategory is "Purchase", CommitmentDiscountQuantity adheres to the following additional requirements:
    * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnits, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term* when [ChargeFrequency](#chargefrequency) is "One-Time".
    * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnits that is eligible for consumption for each *charge period* that corresponds with the purchase when ChargeFrequency is "Recurring".
  * When ChargeCategory is "Usage", CommitmentDiscountQuantity adheres to the following additional requirements:
    * CommitmentDiscountQuantity MUST be the metered quantity of CommitmentDiscountUnits that is consumed over the *row's* *charge period* when [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Used".
    * CommitmentDiscountQuantity MUST be the remaining, unused quantity of CommitmentDiscountUnits for the *row's* *charge period* when CommitmentDiscountStatus is "Unused".

### **CommitmentDiscountQuantity v.1.2 (Technical Refinement)**

The CommitmentDiscountQuantity column adheres to the following requirements:

* CommitmentDiscountQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* If present, CommitmentDiscountQuantity adheres to the following additional requirements:
  * CommitmentDiscountQuantity MUST be of type Decimal.
  * CommitmentDiscountQuantity MUST conform to [Numeric Format](#numericformat) requirements.
  * If ChargeCategory is "Usage" or "Purchase" and CommitmentDiscountId is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
    * CommitmentDiscountQuantity MUST NOT be null if [ChargeClass](#chargeclass) is not "Correction".
    * CommitmentDiscountQuantity MAY be null if ChargeClass is "Correction".
  * Else CommitmentDiscountQuantity adheres to the following additional requirement:
    * CommitmentDiscountQuantity MUST be null.
  * If CommitmentDiscountQuantity is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
    * CommitmentDiscountQuantity MUST be a valid decimal value.
    * If ChargeCategory is "Purchase", CommitmentDiscountQuantity adheres to the following additional requirements:
      * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnits, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term* if [ChargeFrequency](#chargefrequency) is "One-Time".
      * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnits that is eligible for consumption for each *charge period* that corresponds with the purchase if ChargeFrequency is "Recurring".
    * If ChargeCategory is "Usage", CommitmentDiscountQuantity adheres to the following additional requirements:
      * CommitmentDiscountQuantity MUST be the metered quantity of CommitmentDiscountUnits that is consumed over the *row's* *charge period* if [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Used".
      * CommitmentDiscountQuantity MUST be the remaining, unused quantity of CommitmentDiscountUnits for the *row's* *charge period* if CommitmentDiscountStatus is "Unused".

### **CommitmentDiscountQuantity v.1.1 (Original)**

The CommitmentDiscountQuantity column adheres to the following requirements:

* CommitmentDiscountQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountQuantity MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* CommitmentDiscountQuantity MAY be null or any valid decimal value if [*CommitmentDiscountId*](#commitmentdiscountid) is not null and [*ChargeClass*](#chargeclass) is "Correction".

In cases where the ChargeCategory is "Purchase", CommitmentDiscountId is not null, and ChargeClass is not "Correction", the following applies:

* When [ChargeFrequency](#chargefrequency) is "One-Time", and CommitmentDiscountId is not null, CommitmentDiscountQuantity MUST be the positive quantity of CommitmentDiscountUnits, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term*.
* When ChargeFrequency is "Recurring", and CommitmentDiscountId is not null, CommitmentDiscountQuantity MUST be the positive quantity of CommitmentDiscountUnits that is eligible for consumption for each *charge period* that corresponds with the purchase.

In cases where the ChargeCategory is "Usage", CommitmentDiscountId is not null, and ChargeClass is not "Correction", the following applies:

* When [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Used", CommitmentDiscountQuantity MUST be the positive, metered quantity of CommitmentDiscountUnits that is consumed over the *row's* *charge period*.
* When CommitmentDiscountStatus is "Unused", CommitmentDiscountQuantity MUST be the remaining, positive, unused quantity of CommitmentDiscountUnits for the *row's* *charge period*.

CommitmentDiscountQuantity MUST be null in all other cases.

## Column: Commitment Discount Unit

## Column: Consumed Quantity

## Column: Consumed Unit

## Column: Contracted Cost

## Column: Contracted Unit Price

## Column: Effective Cost

### **Effective Cost v.1.2 (Simplified Refinement)**

The EffectiveCost column adheres to the following requirements:

* EffectiveCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* EffectiveCost MUST be of type Decimal.
* EffectiveCost MUST conform to [Numeric Format](#numericformat) requirements.
* EffectiveCost nullability is defined as follows:
  * EffectiveCost MUST NOT be null.
* EffectiveCost MUST be a valid decimal value.
* EffectiveCost MUST be 0 when [ChargeCategory](#chargecategory) is "Purchase" and the purchase is intended to cover future eligible charges.
* EffectiveCost MUST be denominated in the BillingCurrency.
* The sum of EffectiveCost for *rows* in a given *billing period* may not match the sum of the invoices received for the same *billing period* for a [*billing account*](#glossary:billing-account).
* When ChargeCategory is not "Usage" or "Purchase", EffectiveCost adheres to the following additional requirements:
  * EffectiveCost of a charge calculated based on other charges (e.g., when the ChargeCategory is "Tax") MUST be calculated based on the EffectiveCost of those related charges.
  * EffectiveCost of a charge unrelated to other charges (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#billedcost).
* When CommitmentDiscountStatus is "Unused", the EffectiveCost MUST be the total committed cost consumed for the given charge period minus related usage charges.

### **Effective Cost v.1.2 (Technical Refinement)**

The EffectiveCost column adheres to the following requirements:

* EffectiveCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* EffectiveCost MUST be of type Decimal.
* EffectiveCost MUST conform to [Numeric Format](#numericformat) requirements.
* EffectiveCost MUST NOT be null.
* EffectiveCost MUST be a valid decimal value.
* EffectiveCost MUST be 0 if [ChargeCategory](#chargecategory) is "Purchase" and the purchase is intended to cover future eligible charges.
* EffectiveCost MUST be denominated in the BillingCurrency.
* The sum of EffectiveCost for *rows* in a given *billing period* may not match the sum of the invoices received for the same *billing period* for a [*billing account*](#glossary:billing-account).
* If ChargeCategory is not "Usage" or "Purchase", EffectiveCost adheres to the following additional requirements:
  * EffectiveCost of a charge calculated based on other charges (e.g., when the ChargeCategory is "Tax") MUST be calculated based on the EffectiveCost of those related charges.
  * EffectiveCost of a charge unrelated to other charges (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#billedcost).
* When CommitmentDiscountStatus is "Unused", the EffectiveCost MUST be the total committed cost consumed for the given charge period minus related usage charges.

### **Effective Cost v.1.1 (Original)**

The EffectiveCost column adheres to the following requirements:

* The EffectiveCost column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null.
* This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency.
* EffectiveCost MUST be 0 when ChargeCategory is "Purchase" and the purchase is intended to cover future eligible charges.
* The aggregated EffectiveCost for a billing period may not match the charge received on the invoice for the same *billing period*.

In cases where the [ChargeCategory](#chargecategory) is not "Usage" or "Purchase", the following applies:

* The EffectiveCost MUST be calculated based on the EffectiveCost of the related charges if the charge is calculated based on other charges (e.g. [ChargeCategory](#chargecategory) is "Tax").
* The EffectiveCost MUST match the [BilledCost](#billedcost) if the charge is unrelated to other charges (e.g. [ChargeCategory](#chargecategory) is "Credit").
* When CommitmentDiscountStatus is "Unused", the EffectiveCost MUST be the total committed cost consumed for the given charge period minus related usage charges.

## Column: Invoice Issuer

## Column: List Cost

### **List Cost v.1.2 (Simplified Refinement)**

The ListCost column adheres to the following requirements:

* ListCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ListCost MUST be of type Decimal.
* ListCost MUST conform to [Numeric Format](#numericformat) requirements.
* ListCost nullability is defined as follows:
  * ListCost MUST NOT be null.
* ListCost MUST be a valid decimal value.
* ListCost MUST be denominated in the BillingCurrency.
* When [ListUnitPrice](#listunitprice) is null, ListCost adheres to the following additional requirements:
  * ListCost of a charge calculated based on other charges (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ListCost of those related charges.
  * ListCost of a charge unrelated to other charges (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#billedcost).
* The product of ListUnitPrice and PricingQuantity and MUST match the ListCost when ListUnitPrice is present and not null, PricingQuantity is not null, and [ChargeClass](#chargeclass) is not "Correction".
* Discrepancies in ListCost, ListUnitPrice, or PricingQuantity MAY be addressed independently when ChargeClass is "Correction".

### **List Cost v.1.2 (Technical Refinement)**

The ListCost column adheres to the following requirements:

* ListCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ListCost MUST be of type Decimal.
* ListCost MUST conform to [Numeric Format](#numericformat) requirements.
* ListCost MUST NOT be null.
* ListCost MUST be a valid decimal value.
* ListCost MUST be denominated in the BillingCurrency.
* If [ListUnitPrice](#listunitprice) is present and null, ListCost adheres to the following additional requirements:
  * ListCost of a charge calculated based on other charges (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ListCost of those related charges.
  * ListCost of a charge unrelated to other charges (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#billedcost).
* The product of ListUnitPrice and PricingQuantity and MUST match the ListCost if ListUnitPrice is present and not null, PricingQuantity is not null, and [ChargeClass](#chargeclass) is not "Correction".
* Discrepancies in ListCost, ListUnitPrice, or PricingQuantity MAY be addressed independently if ChargeClass is "Correction".

### **List Cost v.1.1 (Original)**

The ListCost column adheres to the following requirements:

* The ListCost column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null.
* This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency.
* When [ListUnitPrice](#listunitprice) is present and not null, multiplying the ListUnitPrice by PricingQuantity MUST produce the ListCost, except in cases of [ChargeClass](#chargeclass) "Correction", which may address PricingQuantity or any cost discrepancies independently.

In cases where the ListUnitPrice is present and is null, the following applies:

* The ListCost of a charge calculated based on other charges (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ListCost of those related charges.
* The ListCost of a charge unrelated to other charges (e.g., when the [ChargeCategory](#chargecategory) is "Credit") MUST match the [BilledCost](#billedcost).

## Column: List Unit Price

### **List Unit Price v.1.2 (Simplified Refinement)**

The ListUnitPrice column adheres to the following requirements:

* ListUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes unit prices exclusive of discounts.
* ListUnitPrice MUST be of type Decimal.
* ListUnitPrice MUST conform to [Numeric Format](#numericformat) requirements.
* ListUnitPrice nullability is defined as follows:
  * ListUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* When ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the BillingCurrency.
  * The product of ListUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ListCost](#listcost) when PricingQuantity is not null and ChargeClass is not "Correction".
  * Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY be addressed independently when ChargeClass is "Correction".

### **List Unit Price v.1.2 (Technical Refinement)**

The ListUnitPrice column adheres to the following requirements:

* ListUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes unit prices exclusive of discounts.
* If present, ListUnitPrice adheres to the following additional requirements:
  * ListUnitPrice MUST be of type Decimal.
  * ListUnitPrice MUST conform to [Numeric Format](#numericformat) requirements.
  * If [ChargeCategory](#chargecategory) is "Tax", ListUnitPrice adheres to the following additional requirement:
    * ListUnitPrice MUST be null.
  * Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", ListUnitPrice adheres to the following additional requirement:
    * ListUnitPrice MUST NOT be null.
  * Else ListUnitPrice adheres to the following additional requirement:
    * ListUnitPrice MAY be null.
  * If ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
    * ListUnitPrice MUST be a non-negative decimal value.
    * ListUnitPrice MUST be denominated in the BillingCurrency.
    * The product of ListUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ListCost](#listcost) if PricingQuantity is not null and ChargeClass is not "Correction".
  * Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY be addressed independently if ChargeClass is "Correction".

### **List Unit Price v.1.1 (Original)**

The ListUnitPrice column adheres to the following requirements:

* The ListUnitPrice column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes unit prices exclusive of discounts.
* This column MUST be a Decimal within the range of non-negative decimal values, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency.
* It MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.
* When ListUnitPrice is present and is not null, multiplying ListUnitPrice by [PricingQuantity](#pricingquantity) MUST equal [ListCost](#listcost), except in cases of ChargeClass "Correction", which may address PricingQuantity or any cost discrepancies independently.

## Column: Pricing Category
## Column: Pricing Quantity
## Column: Pricing Unit
## Column: Provider
## Column: Publisher
## Column: Region ID
## Column: Region Name
## Column: Resource ID
## Column: Resource Name
## Column: Resource Type
## Column: Service Category
## Column: Service Name
## Column: Service Subcategory
## Column: SKU ID
## Column: SKU Meter
## Column: SKU Price Details
## Column: SKU Price ID
## Column: Sub Account ID
## Column: Sub Account Name
## Column: Tags
