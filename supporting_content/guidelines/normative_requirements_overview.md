# Column Normative Requirements Overview

## Column: Availability Zone

### **Availability Zone Cost v.1.2 (Simplified Refinement)**

The AvailabilityZone column adheres to the following requirements:

* AvailabilityZone is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within an *availability zone*.
* AvailabilityZone MUST be of type String.
* AvailabilityZone MUST conform to [String Handling](#stringhandling) requirements.
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
* BillingAccountId MUST NOT be null.
* BillingAccountId MUST be a unique identifier within a provider.

### **Billing Account ID v.1.2 (Technical Refinement)**

The BillingAccountId column adheres to the following requirements:

* BillingAccountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingAccountId MUST be of type String.
* BillingAccountId MUST conform to [String Handling](#stringhandling) requirements.
* BillingAccountId MUST NOT be null.
* BillingAccountId MUST be a unique identifier within a provider.

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
* BillingAccountName MUST NOT be null when the provider supports assigning a display name for the *billing account*.
* BillingAccountName MUST be unique within a customer.

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
  * CapacityReservationId MUST be a unique identifier within the provider.
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
  * CapacityReservationId MUST be a unique identifier within the provider.
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
  * CapacityReservationStatus MUST be null when CapacityReservationId is null.
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
    * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term* when [ChargeFrequency](#chargefrequency) is "One-Time".
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
* ListCost MUST NOT be null.
* ListCost MUST be a valid decimal value.
* ListCost MUST be denominated in the BillingCurrency.
* When [ListUnitPrice](#listunitprice) is null, ListCost adheres to the following additional requirements:
  * ListCost of a charge calculated based on other charges (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ListCost of those related charges.
  * ListCost of a charge unrelated to other charges (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#billedcost).
* The product of ListUnitPrice and PricingQuantity MUST match the ListCost when ListUnitPrice is not null, PricingQuantity is not null, and [ChargeClass](#chargeclass) is not "Correction".
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
* The product of ListUnitPrice and PricingQuantity MUST match the ListCost if ListUnitPrice is present and not null, PricingQuantity is not null, and [ChargeClass](#chargeclass) is not "Correction".
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

### **SKU Meter v.1.2 (Simplified Refinement)**

The SkuMeter column adheres to the following requirements:

* SkuMeter MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU list.
* SkuMeter MUST be of type String.
* SkuMeter MUST conform to [String Handling](#stringhandling) requirements.
* SkuMeter nullability is defined as follows:
  * SkuMeter MUST be null if SkuId is null.
  * SkuMeter SHOULD NOT be null if SkuId is not null.
* SkuMeter SHOULD remain consistent over time for a given SkuId.

### **SKU Meter v.1.2 (Technical Refinement)**

The SkuMeter column adheres to the following requirements:

* SkuMeter MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU list.
* If present, SkuMeter adheres to the following additional requirements:
  * SkuMeter MUST be of type String.
  * SkuMeter MUST conform to [String Handling](#stringhandling) requirements.
  * SkuMeter MUST be null if SkuId is null.
  * SkuMeter SHOULD NOT be null if SkuId is not null.
  * If SkuMeter is not null, SkuMeter adheres to the following additional requirement:
    * SkuMeter SHOULD remain consistent over time for a given SkuId.

### **SKU Meter v.1.1 (Original)**

The SkuMeter column adheres to the following requirements:

* SkuMeter MUST be present in a *FOCUS dataset* when when the provider includes a [SkuId](#skuid).
* SkuMeter MUST be of type String.
* SkuMeter MUST be null when SkuId is null.
* SkuMeter SHOULD NOT be null when SkuId is not null.
* SkuMeter SHOULD remain consistent over time for a given SkuId.

## Column: SKU Price Details

### **SKU Price Details v.1.2 (Simplified Refinement)**

The SkuPriceDetails column adheres to the following requirements:

* SkuPriceDetails MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU price list.
* SkuPriceDetails MUST conform to [KeyValueFormat](#key-valueformat) requirements.
* SkuPriceDetails property key SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* SkuPriceDetails nullability is defined as follows:
  * SkuPriceDetails MUST be null when SkuPriceId is null.
  * SkuPriceDetails MAY be null when SkuPriceId is not null.
* When SkuPriceDetails is not null, SkuPriceDetails adheres to the following additional requirements:
  * SkuPriceDetails MUST NOT contain properties which are not applicable to the corresponding SkuPriceId.
  * SkuPriceDetails MAY contain properties which are already captured in other dedicated columns.
  * SkuPriceDetails SHOULD remain consistent over time for a given SkuPriceId.
  * SkuPriceDetails properties for a given SkuPriceId adhere to the following additional requirements:
    * Existing properties SHOULD remain consistent over time.
    * Existing properties SHOULD NOT be removed.
    * Additional properties MAY be added over time.
  * SkuPriceDetails property key SHOULD remain consistent across comparable SKUs having that property, and the values for this key SHOULD remain in a consistent format.
  * SkuPriceDetails property value MUST represent the value for a single [PricingUnit](#pricingunit) when the property holds a numeric value.

### **SKU Price Details v.1.2 (Technical Refinement)**

The SkuPriceDetails column adheres to the following requirements:

* SkuPriceDetails MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU price list.
* If present, SkuPriceDetails adheres to the following additional requirements:
  * SkuPriceDetails MUST conform to [KeyValueFormat](#key-valueformat) requirements.
  * SkuPriceDetails property key SHOULD conform to [PascalCase](#glossary:pascalcase) format.
  * SkuPriceDetails MUST be null when SkuPriceId is null.
  * SkuPriceDetails MAY be null when SkuPriceId is not null.
  * If SkuPriceDetails is not null, SkuPriceDetails adheres to the following additional requirements:
    * SkuPriceDetails MUST NOT contain properties which are not applicable to the corresponding SkuPriceId.
    * SkuPriceDetails MAY contain properties which are already captured in other dedicated columns.
    * SkuPriceDetails SHOULD remain consistent over time for a given SkuPriceId.
    * SkuPriceDetails properties for a given SkuPriceId adhere to the following additional requirements:
      * Existing properties SHOULD remain consistent over time.
      * Existing properties SHOULD NOT be removed.
      * Additional properties MAY be added over time.
    * SkuPriceDetails property key SHOULD remain consistent across comparable SKUs having that property, and the values for this key SHOULD remain in a consistent format.
    * SkuPriceDetails property value MUST represent the value for a single [PricingUnit](#pricingunit) when the property holds a numeric value.

### **SKU Price Details v.1.1 (Original)**

The SkuPriceDetails column adheres to the following requirements:

* The SkuPriceDetails column MUST be in [KeyValueFormat](#key-valueformat).
* The key for a property SHOULD be formatted in [PascalCase](#glossary:pascalcase).
* The properties (both keys and values) contained in the SkuPriceDetails column MUST be shared across all charges having the same SkuPriceId, subject to the below provisions.
  * Additional properties (key-value pairs) MAY be added to SkuPriceDetails going forward for a given SkuPriceId.
  * Properties SHOULD NOT be removed from SkuPriceDetails for a given SkuPriceId, once they have been included.
  * Individual properties (key-value pairs) SHOULD NOT be modified for a given SkuPriceId and SHOULD remain consistent over time.
* The key for a property SHOULD remain consistent across comparable SKUs having that property and the values for this key SHOULD remain in a consistent format.
* The SkuPriceDetails column MUST NOT contain properties which are not applicable to the corresponding SkuPriceId.
* The SkuPriceDetails column MAY contain properties which are already captured in other dedicated columns.
* If a property has a numeric value, it MUST represent the value for a single [PricingUnit](#pricingunit).
* The SkuPriceDetails column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider includes a SkuPriceId.
  * The SkuPriceDetails column MAY be null when SkuPriceId is not null.
  * The SkuPriceDetails column MUST be null when SkuPriceId is null.

## Column: SKU Price ID

### **SKU Price ID v.1.2 (Simplified Refinement)**

The SkuPriceId column adheres to the following requirements:

* SkuPriceId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU price list.
* SkuPriceId MUST be of type String.
* SkuPriceId MUST conform to [String Handling](#stringhandling) requirements.
* SkuPriceId nullability is defined as follows:
  * SkuPriceId MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * SkuPriceId MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * SkuPriceId MAY be null in all other cases.
* When SkuPriceId is not null, SkuPriceId adheres to the following additional requirements:
  * SkuPriceId MUST be associated with one and only one [SkuId](#skuid), except in cases of [commitment discount flexibility](#glossary:commitment-discount-flexibility).
  * SkuPriceId MUST define a single unit price used for calculating the charge.
  * When a provider does not have a SkuPriceId and wants to include information in columns linked to SkuPriceId such as ListUnitPrice or [SkuPriceDetails](#skupricedetails), the SkuId MAY be used in the SkuPriceId column as long as it adheres to the above conditions.
  * [ListUnitPrice](#listunitprice) MUST be associated with the SkuPriceId in the provider published price list.

### **SKU Price ID v.1.2 (Technical Refinement)**

The SkuPriceId column adheres to the following requirements:

* SkuPriceId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU price list.
* If present, SkuPriceId adheres to the following additional requirements:
  * SkuPriceId MUST be of type String.
  * SkuPriceId MUST conform to [String Handling](#stringhandling) requirements.
  * SkuPriceId MUST be null if [ChargeCategory](#chargecategory) is "Tax".
  * SkuPriceId MUST NOT be null if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * SkuPriceId MAY be null in all other cases.
  * SkuPriceId MUST be associated with one and only one [SkuId](#skuid), except in cases of [commitment discount flexibility](#glossary:commitment-discount-flexibility).
  * SkuPriceId MUST define a single unit price used for calculating the charge.
  * [ListUnitPrice](#listunitprice) MUST be associated with the SkuPriceId in the provider published price list.
  * When a provider does not have a SkuPriceId and wants to include information in columns linked to SkuPriceId such as ListUnitPrice or [SkuPriceDetails](#skupricedetails), the SkuId MAY be used in the SkuPriceId column as long as it adheres to the above conditions.

### **SKU Price ID v.1.1 (Original)**

The SkuPriceId column adheres to the following requirements:

* SkuPriceId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU price list and MUST be of type String.
* SkuPriceId MUST define a single unit price used for calculating the charge.
* [ListUnitPrice](#listunitprice) MUST be associated with the SkuPriceId in the provider published price list.
* SkuPriceId MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.
* A given value of SkuPriceId MUST be associated with one and only one [SkuId](#skuid), except in cases of [commitment discount flexibility](#glossary:commitment-discount-flexibility).
* If a provider does not have a SkuPriceId and wants to include information in columns linked to SkuPriceId such as ListUnitPrice or [SkuPriceDetails](#skupricedetails), the SkuId MAY be used in the SkuPriceId column as long as it adheres to the above conditions.

## Column: Sub Account ID

### **Sub Account ID v.1.2 (Simplified Refinement)**

The SubAccountId column adheres to the following requirements:

* SubAccountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports a *sub account* construct.
* SubAccountId MUST be of type String.
* SubAccountId MUST conform to [String Handling](#stringhandling) requirements.
* SubAccountId nullability is defined as follows:
  * SubAccountId MUST be null when a charge is not related to a *sub account*.
  * SubAccountId MUST NOT be null when a charge is related to a *sub account*.

### **Sub Account ID v.1.2 (Technical Refinement)**

The SubAccountId column adheres to the following requirements:

* SubAccountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports a *sub account* construct.
* If present, SubAccountId adheres to the following additional requirements:
  * SubAccountId MUST be of type String.
  * SubAccountId MUST conform to [String Handling](#stringhandling) requirements.
  * SubAccountId MUST be null when a charge is not related to a *sub account*.
  * SubAccountId MUST NOT be null when a charge is related to a *sub account*.

### **Sub Account ID v.1.1 (Original)**

The SubAccountId column adheres to the following requirements:

* The SubAccountId column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports a *sub account* construct.
* This column MUST be of type String.
* If a charge does not apply to a *sub account*, the SubAccountId column MUST be null.

## Column: Sub Account Name

### **Sub Account Name v.1.2 (Simplified Refinement)**

The SubAccountName column adheres to the following requirements:

* SubAccountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports a *sub account* construct.
* SubAccountName MUST be of type String.
* SubAccountName MUST conform to [String Handling](#stringhandling) requirements.
* SubAccountName nullability is defined as follows:
  * SubAccountName MUST be null when [SubAccountId](#subaccountid) is null.
  * SubAccountName MUST NOT be null when SubAccountId is not null.

### **Sub Account Name v.1.2 (Technical Refinement)**

The SubAccountName column adheres to the following requirements:

* SubAccountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports a *sub account* construct.
* If present, SubAccountName adheres to the following additional requirements:
  * SubAccountName MUST be of type String.
  * SubAccountName MUST conform to [String Handling](#stringhandling) requirements.
  * SubAccountName MUST be null if [SubAccountId](#subaccountid) is null.
  * SubAccountName MUST NOT be null if SubAccountId is not null.

### **Sub Account Name v.1.1 (Original)**

The SubAccountName column adheres to the following requirements:

* The SubAccountName column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports a *sub account* construct.
* This column MUST be of type String.
* If a charge does not apply to a *sub account*, the SubAccountName column MUST be null.

## Column: Tags

### **Tags v.1.2 (Simplified Refinement)**

The Tags column adheres to the following requirements:

* Tags MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports setting user or provider-defined tags.
* Tags MUST conform to [KeyValueFormat](#key-valueformat) requirements.
* Tags MAY be null.
* When Tags is not null, Tags adheres to the following additional requirements:
  * Tags MUST contain user-defined and provider-defined tags.
  * Tags MUST only contain finalized tags.
  * Tag key with a non-null value for a given resource SHOULD be included in the Tags column.
  * Tag key with a null value for a given resource MAY be included in the Tags column depending on the provider's tag finalization process.
  * Tag key that does *not* support a corresponding value, MUST have a corresponding true (boolean) value set.
  * Providers MUST publish tag finalization methods and semantics within their respective documentation when tag finalization is supported.
  * Providers MUST NOT alter user-defined tag keys or values.
  * Provider-defined tags adhere to the following additional requirements:
    * Provider-defined tags MUST be prefixed with a provider-specified tag key prefix.
    * Providers SHOULD publish all provider-specified tag key prefixes within their respective documentation.

### **Tags v.1.2 (Technical Refinement)**

The Tags column adheres to the following requirements:

* Tags MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports setting user or provider-defined tags.
* If present, Tags adheres to the following additional requirements:
  * Tags MUST conform to [KeyValueFormat](#key-valueformat) requirements.
  * If Tags is not null, Tags adheres to the following additional requirements:
    * Tags MUST contain user-defined and provider-defined tags.
    * Tags MUST only contain finalized tags.
    * Tag key with a non-null value for a given resource SHOULD be included in the Tags column.
    * Tag key with a null value for a given resource MAY be included in the Tags column depending on the provider's tag finalization process.
    * Tag key that does *not* support a corresponding value, MUST have a corresponding true (boolean) value set.
    * Providers MUST publish tag finalization methods and semantics within their respective documentation if tag finalization is supported.
    * Providers MUST NOT alter user-defined tag keys or values.
    * Provider-defined tags adhere to the following additional requirements:
      * Provider-defined tags MUST be prefixed with a provider-specified tag key prefix.
      * Providers SHOULD publish all provider-specified tag key prefixes within their respective documentation.

### **Tags v.1.1 (Original)**

The Tags column adheres to the following requirements:

* The Tags column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports setting user or provider-defined tags.
* The Tags column MUST contain user-defined and provider-defined tags.
* The Tags column MUST only contain finalized tags.
* The Tags column MUST be in [KeyValueFormat](#key-valueformat).
* A Tag key with a non-null value for a given resource SHOULD be included in the tags column.
* A Tag key with a null value for a given resource MAY be included in the tags column depending on the provider's tag finalization process.
* A Tag key that does *not* support a corresponding value, MUST have a corresponding true (boolean) value set.
* If Tag finalization is supported, providers MUST publish tag finalization methods and semantics within their respective documentation.
* Providers MUST NOT alter user-defined Tag keys or values.

Provider-defined Tags additionally adhere to the following requirements:

* Provider-defined tags MUST be prefixed with a provider-specified tag key prefix.
* Providers SHOULD publish all provider-specified tag key prefixes within their respective documentation.
