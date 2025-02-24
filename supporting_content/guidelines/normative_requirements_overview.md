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
* The sum of BilledCost in a given [*billing period*](#glossary:billing-period) MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

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
* The sum of [BilledCost](#billedcost) in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

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
* The sum of [BilledCost](#billedcost) in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

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

### **Charge Class v.1.2 (Simplified Refinement)**

The ChargeClass column adheres to the following requirements:

* ChargeClass MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargeClass MUST be of type String.
* ChargeClass nullability is defined as follows:
  * ChargeClass MUST be null when the row does not represent a correction or when it represents a correction within the current *billing period*.
  * ChargeClass MUST NOT be null when the row represents a correction to a previously invoiced *billing period*.
* When ChargeClass is not null, ChargeClass adheres to the following additional requirements:
  * ChargeClass MUST be one of the allowed values.
  * ChargeClass MUST be "Correction".

### **Charge Class v.1.2 (Technical Refinement)**

The ChargeClass column adheres to the following requirements:

* ChargeClass MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargeClass MUST be of type String.
* ChargeClass MUST be null when the row does not represent a correction or when it represents a correction within the current *billing period*.
* When the row represents a correction to a previously invoiced *billing period*, ChargeClass adheres to the following additional requirements:
  * ChargeClass MUST NOT be null.
  * ChargeClass MUST be one of the allowed values.
  * ChargeClass MUST be "Correction".

### **Charge Class v.1.1 (Original)**

The ChargeClass column adheres to the following requirements:

* The ChargeClass column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type String and MUST be "Correction" when the row represents a correction to a previously invoiced *billing period*.
* ChargeClass MUST be null when it is not a correction or when it is a correction within the current *billing period*.

## Column: Charge Description

### **Charge Description v.1.2 (Simplified Refinement)**

The ChargeDescription column adheres to the following requirements:

* ChargeDescription MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargeDescription MUST be of type String.
* ChargeDescription MUST conform to [String Handling](#stringhandling) requirements.
* ChargeDescription SHOULD NOT be null.
* ChargeDescription length SHOULD be specified by providers in their publicly available documentation.

### **Charge Description v.1.2 (Technical Refinement)**

The ChargeDescription column adheres to the following requirements:

* ChargeDescription MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargeDescription MUST be of type String.
* ChargeDescription MUST conform to [String Handling](#stringhandling) requirements.
* ChargeDescription SHOULD NOT be null.
* ChargeDescription length SHOULD be specified by providers in their publicly available documentation.

### **Charge Description v.1.1 (Original)**

The ChargeDescription column adheres to the following requirements:

* The ChargeDescription column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset), MUST be of type String, and SHOULD NOT be null.
* Providers SHOULD specify the length of this column in their publicly available documentation.

## Column: Charge Frequency

### **Charge Frequency v.1.2 (Simplified Refinement)**

The ChargeFrequency column adheres to the following requirements:

* ChargeFrequency is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargeFrequency MUST be of type String.
* ChargeFrequency MUST NOT be null.
* ChargeFrequency MUST be one of the allowed values.
* ChargeFrequency MUST NOT be "Usage-Based" when [ChargeCategory](#chargecategory) is "Purchase".

### **Charge Frequency v.1.2 (Technical Refinement)**

The ChargeFrequency column adheres to the following requirements:

* ChargeFrequency is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* If present, ChargeFrequency adheres to the following additional requirements:
  * ChargeFrequency MUST be of type String.
  * ChargeFrequency MUST NOT be null.
  * ChargeFrequency MUST be one of the allowed values.
  * ChargeFrequency MUST NOT be "Usage-Based" if [ChargeCategory](#chargecategory) is "Purchase".

### **Charge Frequency v.1.1 (Original)**

The ChargeFrequency column adheres to the following requirements:

* The ChargeFrequency column is RECOMMENDED be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null.
* This column is of type String and MUST be one of the allowed values.
* When [ChargeCategory](#chargecategory) is "Purchase", ChargeFrequency MUST NOT be "Usage-Based".

## Column: Charge Period End

### **Charge Period End v.1.2 (Simplified Refinement)**

The ChargePeriodEnd column adheres to the following requirements:

* ChargePeriodEnd MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargePeriodEnd MUST be of type Date/Time.
* ChargePeriodEnd MUST conform to [Date/Time Format](#date/timeformat) requirements.
* ChargePeriodEnd MUST NOT be null.
* ChargePeriodEnd MUST be the *exclusive ending bound* of the effective period of the charge.

### **Charge Period End v.1.2 (Technical Refinement)**

The ChargePeriodEnd column adheres to the following requirements:

* ChargePeriodEnd MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargePeriodEnd MUST be of type Date/Time.
* ChargePeriodEnd MUST conform to [Date/Time Format](#date/timeformat) requirements.
* ChargePeriodEnd MUST NOT be null.
* ChargePeriodEnd MUST be the *exclusive ending bound* of the effective period of the charge.

### **Charge Period End v.1.1 (Original)**

The ChargePeriodEnd column adheres to the following requirements:

* ChargePeriodEnd MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset), MUST be of type Date/Time, MUST be an *exclusive* value, and MUST NOT contain null values.
* ChargePeriodEnd MUST match the ending date and time boundary of the effective period of the charge.

## Column: Charge Period Start

### **Charge Period Start v.1.2 (Simplified Refinement)**

The ChargePeriodStart column adheres to the following requirements:

* ChargePeriodStart MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargePeriodStart MUST be of type Date/Time.
* ChargePeriodStart MUST conform to [Date/Time Format](#date/timeformat) requirements.
* ChargePeriodStart MUST NOT be null.
* ChargePeriodStart MUST be the *inclusive beginning bound* of the effective period of the charge.

### **Charge Period Start v.1.2 (Technical Refinement)**

The ChargePeriodStart column adheres to the following requirements:

* ChargePeriodStart MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargePeriodStart MUST be of type Date/Time.
* ChargePeriodStart MUST conform to [Date/Time Format](#date/timeformat) requirements.
* ChargePeriodStart MUST NOT be null.
* ChargePeriodStart MUST be the *inclusive beginning bound* of the effective period of the charge.

### **Charge Period Start v.1.1 (Original)**

The ChargePeriodStart column adheres to the following requirements:

* ChargePeriodStart MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset), MUST be of type Date/Time, MUST be an *inclusive* value, and MUST NOT contain null values.
* ChargePeriodStart MUST match the beginning date and time boundary of the effective period of the charge.

## Column: Commitment Discount Category

### **Commitment Discount Category v.1.2 (Simplified Refinement)**

The CommitmentDiscountCategory column adheres to the following requirements:

* CommitmentDiscountCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountCategory MUST be of type String.
* CommitmentDiscountCategory MUST conform to [String Handling](#stringhandling) requirements.
* CommitmentDiscountCategory MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
* When CommitmentDiscountId is not null, CommitmentDiscountCategory adheres to the following additional requirements:
  * CommitmentDiscountCategory MUST NOT be null.
  * CommitmentDiscountCategory MUST be one of the allowed values.

### **Commitment Discount Category v.1.2 (Technical Refinement)**

The CommitmentDiscountCategory column adheres to the following requirements:

* CommitmentDiscountCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* If present, CommitmentDiscountCategory adheres to the following additional requirements:
  * CommitmentDiscountCategory MUST be of type String.
  * CommitmentDiscountCategory MUST conform to [String Handling](#stringhandling) requirements.
  * CommitmentDiscountCategory MUST be null if [CommitmentDiscountId](#commitmentdiscountid) is null.
  * If CommitmentDiscountId is not null, CommitmentDiscountCategory adheres to the following additional requirements:
    * CommitmentDiscountCategory MUST NOT be null.
    * CommitmentDiscountCategory MUST be one of the allowed values.

### **Commitment Discount Category v.1.1 (Original)**

The CommitmentDiscountCategory column adheres to the following requirements:

* The CommitmentDiscountCategory column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* This column MUST be of type String, MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null, and MUST NOT be null when CommitmentDiscountId is not null.
* The CommitmentDiscountCategory MUST be one of the allowed values.

## Column: Commitment Discount ID

### **Commitment Discount ID v.1.2 (Simplified Refinement)**

The CommitmentDiscountId column adheres to the following requirements:

* CommitmentDiscountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountId MUST be of type String.
* CommitmentDiscountId MUST conform to [String Handling](#stringhandling) requirements.
* CommitmentDiscountId nullability is defined as follows:
  * CommitmentDiscountId MUST be null when a charge is not related to a *commitment discount*.
  * CommitmentDiscountId MUST NOT be null when a charge is related to a *commitment discount*.
* When CommitmentDiscountId is not null, CommitmentDiscountId adheres to the following additional requirements:
  * CommitmentDiscountId MUST be a unique identifier within the provider.
  * CommitmentDiscountId SHOULD be a fully-qualified identifier.

### **Commitment Discount ID v.1.2 (Technical Refinement)**

The CommitmentDiscountId column adheres to the following requirements:

* CommitmentDiscountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* If present, CommitmentDiscountId adheres to the following additional requirements:
  * CommitmentDiscountId MUST be of type String.
  * CommitmentDiscountId MUST conform to [String Handling](#stringhandling) requirements.
  * CommitmentDiscountId MUST be null when a charge is not related to a *commitment discount*.
  * CommitmentDiscountId MUST NOT be null when a charge is related to a *commitment discount*.
  * CommitmentDiscountId MUST be a unique identifier within the provider.
  * CommitmentDiscountId SHOULD be a fully-qualified identifier.

### **Commitment Discount ID v.1.1 (Original)**

The CommitmentDiscountId column adheres to the following requirements:

* The CommitmentDiscountId column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* This column MUST be of type String and MUST NOT contain null values when a charge is related to a *commitment discount*.
* When a charge is not associated with a *commitment discount*, the column MUST be null.
* CommitmentDiscountId MUST ensure global uniqueness within the provider and SHOULD be a fully-qualified identifier.

## Column: Commitment Discount Name

### **Commitment Discount Name v.1.2 (Simplified Refinement)**

The CommitmentDiscountName column adheres to the following requirements:

* CommitmentDiscountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountName MUST be of type String.
* CommitmentDiscountName MUST conform to [String Handling](#stringhandling) requirements.
* CommitmentDiscountName MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
* When CommitmentDiscountId is not null, CommitmentDiscountName adheres to the following additional requirements:
  * CommitmentDiscountName MUST NOT be null when a display name can be assigned to a *commitment discount*.
  * CommitmentDiscountName MAY be null when a display name cannot be assigned to a *commitment discount*.

### **Commitment Discount Name v.1.2 (Technical Refinement)**

The CommitmentDiscountName column adheres to the following requirements:

* CommitmentDiscountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* If present, CommitmentDiscountName adheres to the following additional requirements:
  * CommitmentDiscountName MUST be of type String.
  * CommitmentDiscountName MUST conform to [String Handling](#stringhandling) requirements.
  * CommitmentDiscountName MUST be null if [CommitmentDiscountId](#commitmentdiscountid) is null.
  * If CommitmentDiscountId is not null, CommitmentDiscountName adheres to the following additional requirements:
    * CommitmentDiscountName MUST NOT be null when a display name can be assigned to a *commitment discount*.
    * CommitmentDiscountName MAY be null when a display name cannot be assigned to a *commitment discount*.

### **Commitment Discount Name v.1.1 (Original)**

The CommitmentDiscountName column adheres to the following requirements:

* The CommitmentDiscountName column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* This column MUST be of type String.
* The CommitmentDiscountName value MUST be null if the charge is not related to a *commitment discount* and MAY be null if a display name cannot be assigned to a *commitment discount*.
* CommitmentDiscountName MUST NOT be null if a display name can be assigned to a *commitment discount*.

## Column: Commitment Discount Status

### **Commitment Discount Status v.1.2 (Simplified Refinement)**

The CommitmentDiscountStatus column adheres to the following requirements:

* CommitmentDiscountStatus MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountStatus MUST be of type String.
* CommitmentDiscountStatus nullability is defined as follows:
  * CommitmentDiscountStatus MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * CommitmentDiscountStatus MUST NOT be null when CommitmentDiscountId is not null and [Charge Category](#chargecategory) is "Usage".
* CommitmentDiscountStatus MUST be one of the allowed values.

### **Commitment Discount Status v.1.2 (Technical Refinement)**

The CommitmentDiscountStatus column adheres to the following requirements:

* CommitmentDiscountStatus MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* If present, CommitmentDiscountStatus adheres to the following additional requirements:
  * CommitmentDiscountStatus MUST be of type String.
  * CommitmentDiscountStatus MUST be null if [CommitmentDiscountId](#commitmentdiscountid) is null.
  * If CommitmentDiscountId is not null and [Charge Category](#chargecategory) is "Usage", CommitmentDiscountStatus adheres to the following additional requirements:
    * CommitmentDiscountStatus MUST NOT be null.
    * CommitmentDiscountStatus MUST be one of the allowed values.

### **Commitment Discount Status v.1.1 (Original)**

The CommitmentDiscountStatus column adheres to the following requirements:

* The CommitmentDiscountStatus column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* This column MUST be of type String, MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null, and MUST NOT be null when CommitmentDiscountId is not null and [Charge Category](#chargecategory) is "Usage".
* CommitmentDiscountStatus MUST be one of the allowed values.

## Column: Commitment Discount Type

### **Commitment Discount Type v.1.2 (Simplified Refinement)**

The CommitmentDiscountType column adheres to the following requirements:

* CommitmentDiscountType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountType MUST be of type String.
* CommitmentDiscountType MUST conform to [String Handling](#stringhandling) requirements.
* CommitmentDiscountType nullability is defined as follows:
  * CommitmentDiscountType MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * CommitmentDiscountType MUST NOT be null when CommitmentDiscountId is not null.

### **Commitment Discount Type v.1.2 (Technical Refinement)**

The CommitmentDiscountType column adheres to the following requirements:

* CommitmentDiscountType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* If present, CommitmentDiscountType adheres to the following additional requirements:
  * CommitmentDiscountType MUST be of type String.
  * CommitmentDiscountType MUST conform to [String Handling](#stringhandling) requirements.
  * CommitmentDiscountType MUST be null if [CommitmentDiscountId](#commitmentdiscountid) is null.
  * CommitmentDiscountType MUST NOT be null if CommitmentDiscountId is not null.

### **Commitment Discount Type v.1.1 (Original)**

The CommitmentDiscountType column adheres to the following requirements:

* The CommitmentDiscountType column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* This column MUST be of type String, MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null, and MUST NOT be null when CommitmentDiscountId is not null.

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
    * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit that is eligible for consumption for each *charge period* that corresponds with the purchase when ChargeFrequency is "Recurring".
  * When ChargeCategory is "Usage", CommitmentDiscountQuantity adheres to the following additional requirements:
    * CommitmentDiscountQuantity MUST be the metered quantity of CommitmentDiscountUnit that is consumed over the *row's* *charge period* when [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Used".
    * CommitmentDiscountQuantity MUST be the remaining, unused quantity of CommitmentDiscountUnit for the *row's* *charge period* when CommitmentDiscountStatus is "Unused".

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

### **Commitment Discount Unit v.1.2 (Simplified Refinement)**

The CommitmentDiscountUnit column adheres to the following requirements:

* CommitmentDiscountUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountUnit MUST be of type String.
* CommitmentDiscountUnit MUST conform to [String Handling](#stringhandling) requirements.
* CommitmentDiscountUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
* CommitmentDiscountUnit nullability is defined as follows:
  * When ChargeCategory is "Usage" or "Purchase" and [CommitmentDiscountId](#commitmentdiscountid) is not null, CommitmentDiscountUnit adheres to the following additional requirements:
    * CommitmentDiscountUnit MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction".
    * CommitmentDiscountUnit MAY be null when ChargeClass is "Correction".
  * CommitmentDiscountUnit MUST be null in all other cases.
* When CommitmentDiscountUnit is not null, CommitmentDiscountUnit adheres to the following additional requirements:
  * CommitmentDiscountUnit MUST remain consistent over time for a given CommitmentDiscountId.
  * CommitmentDiscountUnit MUST represent the unit used to measure the *commitment discount*.
  * When accounting for [*commitment discount flexibility*](#glossary:commitment-discount-flexibility), the CommitmentDiscountUnit value SHOULD reflect this consideration.

### **Commitment Discount Unit v.1.2 (Technical Refinement)**

The CommitmentDiscountUnit column adheres to the following requirements:

* CommitmentDiscountUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* If present, CommitmentDiscountUnit adheres to the following additional requirements:
  * CommitmentDiscountUnit MUST be of type String.
  * CommitmentDiscountUnit MUST conform to [String Handling](#stringhandling) requirements.
  * CommitmentDiscountUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
  * If ChargeCategory is "Usage" or "Purchase" and [CommitmentDiscountId](#commitmentdiscountid) is not null, CommitmentDiscountUnit adheres to the following additional requirements:
    * CommitmentDiscountUnit MUST NOT be null if [ChargeClass](#chargeclass) is not "Correction".
    * CommitmentDiscountUnit MAY be null if ChargeClass is "Correction".
  * Else CommitmentDiscountUnit adheres to the following additional requirement:
    * CommitmentDiscountUnit MUST be null.
  * If CommitmentDiscountUnit is not null, CommitmentDiscountUnit adheres to the following additional requirements:
    * CommitmentDiscountUnit MUST remain consistent over time for a given CommitmentDiscountId.
    * CommitmentDiscountUnit MUST represent the unit used to measure the *commitment discount*.
    * When accounting for [*commitment discount flexibility*](#glossary:commitment-discount-flexibility), the CommitmentDiscountUnit value SHOULD reflect this consideration.

### **Commitment Discount Unit v.1.1 (Original)**

The CommitmentDiscountUnit column adheres to the following requirements:

* CommitmentDiscountUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports [*commitment discounts*](#glossary:commitment-discount).
* CommitmentDiscountUnit MUST be of type String, and the units of measure used in CommitmentDiscountUnit SHOULD adhere to the values and format requirements specified in the [UnitFormat](#unitformat) attribute.
* The CommitmentDiscountUnit MUST be the same across all *rows* where CommitmentDiscountQuantity has the same [CommitmentDiscountId](#commitmentdiscountid).
* CommitmentDiscountUnit MAY be null if CommitmentDiscountId is not null and [ChargeClass](#chargeclass) is "Correction".
* CommitmentDiscountUnit MUST NOT be null when CommitmentDiscountId is not null and ChargeClass is not "Correction".
* CommitmentDiscountUnit MUST be null in all other cases.

In cases where the CommitmentDiscountUnit is not null, the following applies:

* The CommitmentDiscountUnit MUST represent the unit used to measure the *commitment discount*.
* When accounting for [*commitment discount flexibility*](#glossary:commitment-discount-flexibility), the CommitmentDiscountUnit value SHOULD reflect this consideration.

## Column: Consumed Quantity

### **Consumed Quantity v.1.2 (Simplified Refinement)**

The ConsumedQuantity column adheres to the following requirements:

* ConsumedQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports the measurement of usage.
* ConsumedQuantity MUST be of type Decimal.
* ConsumedQuantity MUST conform to [Numeric Format](#numericformat) requirements.
* ConsumedQuantity nullability is defined as follows:
  * ConsumedQuantity MUST be null when [ChargeCategory](#chargecategory) is not "Usage", or when ChargeCategory is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused".
  * When ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", ConsumedQuantity adheres to the following additional requirements:
    * ConsumedQuantity MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction".
    * ConsumedQuantity MAY be null when ChargeClass is "Correction"."
* ConsumedQuantity MUST be a valid decimal value when not null.

### **Consumed Quantity v.1.2 (Technical Refinement)**

The ConsumedQuantity column adheres to the following requirements:

* ConsumedQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports the measurement of usage.
* If present, ConsumedQuantity adheres to the following additional requirements:
  * ConsumedQuantity MUST be of type Decimal.
  * ConsumedQuantity MUST conform to [Numeric Format](#numericformat) requirements.
  * ConsumedQuantity MUST be null if [ChargeCategory](#chargecategory) is not "Usage", or if ChargeCategory is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused".
  * If ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", ConsumedQuantity adheres to the following additional requirements:
    * ConsumedQuantity MUST NOT be null if [ChargeClass](#chargeclass) is not "Correction".
    * ConsumedQuantity MAY be null if ChargeClass is "Correction"."
  * If ConsumedQuantity is not null, ConsumedQuantity adheres to the following additional requirement:
    * ConsumedQuantity MUST be a valid decimal value.

### **Consumed Quantity v.1.1 (Original)**

The ConsumedQuantity column adheres to the following requirements:

* ConsumedQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports the measurement of usage.
* ConsumedQuantity MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* ConsumedQuantity MUST NOT be null and MUST be a valid positive decimal value if [ChargeCategory](#chargecategory) is "Usage", [CommitmentDiscountStatus](#commitmentdiscountstatus) is not "Unused", and [ChargeClass](#chargeclass) is not "Correction".
* ConsumedQuantity MAY be null or any valid decimal value if ChargeCategory is "Usage", CommitmentDiscountStatus is not "Unused", and ChargeClass is "Correction".
* ConsumedQuantity MUST be null in all other cases.

## Column: Consumed Unit

### **Consumed Unit v.1.2 (Simplified Refinement)**

The ConsumedUnit column adheres to the following requirements:

* ConsumedUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports the measurement of usage.
* ConsumedUnit MUST be of type String.
* ConsumedUnit MUST conform to [String Handling](#stringhandling) requirements.
* ConsumedUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
* ConsumedUnit nullability is defined as follows:
  * ConsumedUnit MUST be null when [ChargeCategory](#chargecategory) is not "Usage", or when ChargeCategory is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused".
  * When ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", ConsumedUnit adheres to the following additional requirements:
    * ConsumedUnit MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction".
    * ConsumedUnit MAY be null when ChargeClass is "Correction".

### **Consumed Unit v.1.2 (Technical Refinement)**

The ConsumedUnit column adheres to the following requirements:

* ConsumedUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports the measurement of usage.
* If present, ConsumedUnit adheres to the following additional requirements:
  * ConsumedUnit MUST be of type String.
  * ConsumedUnit MUST conform to [String Handling](#stringhandling) requirements.
  * ConsumedUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
  * ConsumedUnit MUST be null if [ChargeCategory](#chargecategory) is not "Usage", or if ChargeCategory is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused".
  * If ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", ConsumedUnit adheres to the following additional requirements:
    * ConsumedUnit MUST NOT be null if [ChargeClass](#chargeclass) is not "Correction".
    * ConsumedUnit MAY be null if ChargeClass is "Correction".

### **Consumed Unit v.1.1 (Original)**

The ConsumedUnit column adheres to the following requirements:

* ConsumedUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports the measurement of usage.
* ConsumedUnit MUST be of type String, and the units of measure used in ConsumedUnit SHOULD adhere to the values and format requirements specified in the [UnitFormat](#unitformat) attribute.
* ConsumedUnit MUST NOT be null if [ChargeCategory](#chargecategory) is "Usage", [CommitmentDiscountStatus](#commitmentdiscountstatus) is not "Unused", and [ChargeClass](#chargeclass) is not "Correction".
* ConsumedUnit MAY be null if ChargeCategory is "Usage", CommitmentDiscountStatus is not "Unused", and ChargeClass is "Correction".
* ConsumedUnit MUST be null in all other cases.

## Column: Contracted Cost

### **Contracted Cost v.1.2 (Simplified Refinement)**

The ContractedCost column adheres to the following requirements:

* ContractedCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractedCost MUST be of type Decimal.
* ContractedCost MUST conform to [Numeric Format](#numericformat) requirements.
* ContractedCost MUST NOT be null.
* ContractedCost MUST be a valid decimal value.
* ContractedCost MUST be denominated in the BillingCurrency.
* When [ContractedUnitPrice](#contractedunitprice) is null, ContractedCost adheres to the following additional requirements:
  * ContractedCost of a charge calculated based on other charges (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ContractedCost of those related charges.
  * ContractedCost of a charge unrelated to other charges (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#billedcost).
* The product of ContractedUnitPrice and PricingQuantity MUST match the ContractedCost when ContractedUnitPrice is not null, PricingQuantity is not null, and [ChargeClass](#chargeclass) is not "Correction".
* Discrepancies in ContractedCost, ContractedUnitPrice, or PricingQuantity MAY be addressed independently when ChargeClass is "Correction".

### **Contracted Cost v.1.2 (Technical Refinement)**

The ContractedCost column adheres to the following requirements:

* ContractedCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractedCost MUST be of type Decimal.
* ContractedCost MUST conform to [Numeric Format](#numericformat) requirements.
* ContractedCost MUST NOT be null.
* ContractedCost MUST be a valid decimal value.
* ContractedCost MUST be denominated in the BillingCurrency.
* If [ContractedUnitPrice](#contractedunitprice) is present and null, ContractedCost adheres to the following additional requirements:
  * ContractedCost of a charge calculated based on other charges (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ContractedCost of those related charges.
  * ContractedCost of a charge unrelated to other charges (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#billedcost).
* The product of ContractedUnitPrice and PricingQuantity MUST match the ContractedCost if ContractedUnitPrice is present and not null, PricingQuantity is not null, and [ChargeClass](#chargeclass) is not "Correction".
* Discrepancies in ContractedCost, ContractedUnitPrice, or PricingQuantity MAY be addressed independently if ChargeClass is "Correction".

### **Contracted Cost v.1.1 (Original)**

The ContractedCost column adheres to the following requirements:

* The ContractedCost column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null.
* This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency.
* When [ContractedUnitPrice](#contractedunitprice) is present and not null, multiplying the ContractedUnitPrice by PricingQuantity MUST produce the ContractedCost, except in cases of [ChargeClass](#chargeclass) "Correction", which may address PricingQuantity or any cost discrepancies independently.

In cases where the ContractedUnitPrice is present and null, the following applies:

* The ContractedCost of a charge calculated based on other charges (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ContractedCost of those related charges.
* The ContractedCost of a charge unrelated to other charges (e.g., when the [ChargeCategory](#chargecategory) is "Credit") MUST match the [BilledCost](#billedcost).

## Column: Contracted Unit Price

### **Contracted Unit Price v.1.2 (Simplified Refinement)**

The ContractedUnitPrice column adheres to the following requirements:

* ContractedUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports negotiated pricing concepts.
* ContractedUnitPrice adheres to the following additional requirements:
* ContractedUnitPrice MUST be of type Decimal.
* ContractedUnitPrice MUST conform to [Numeric Format](#numericformat) requirements.
* ContractedUnitPrice nullability is defined as follows:
  * ContractedUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * ContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* When ContractedUnitPrice is not null, ContractedUnitPrice adheres to the following additional requirements:
  * ContractedUnitPrice MUST be a non-negative decimal value.
  * ContractedUnitPrice MUST be denominated in the BillingCurrency.
  * The product of ContractedUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ContractedCost](#contractedcost) when PricingQuantity is not null and ChargeClass is not "Correction".
* Discrepancies in ContractedUnitPrice, ContractedCost, or PricingQuantity MAY be addressed independently when ChargeClass is "Correction".

### **Contracted Unit Price v.1.2 (Technical Refinement)**

The ContractedUnitPrice column adheres to the following requirements:

* ContractedUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports negotiated pricing concepts.
* If present, ContractedUnitPrice adheres to the following additional requirements:
* ContractedUnitPrice MUST be of type Decimal.
* ContractedUnitPrice MUST conform to [Numeric Format](#numericformat) requirements.
  * If [ChargeCategory](#chargecategory) is "Tax", ContractedUnitPrice adheres to the following additional requirement:
    * ContractedUnitPrice MUST be null.
  * Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", ContractedUnitPrice adheres to the following additional requirement:
    * ContractedUnitPrice MUST NOT be null.
  * Else ContractedUnitPrice adheres to the following additional requirement:
    * ContractedUnitPrice MAY be null.
  * If ContractedUnitPrice is not null, ContractedUnitPrice adheres to the following additional requirements:
    * ContractedUnitPrice MUST be a non-negative decimal value.
    * ContractedUnitPrice MUST be denominated in the BillingCurrency.
    * The product of ContractedUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ContractedCost](#contractedcost) if PricingQuantity is not null and ChargeClass is not "Correction".
  * Discrepancies in ContractedUnitPrice, ContractedCost, or PricingQuantity MAY be addressed independently if ChargeClass is "Correction".

### **Contracted Unit Price v.1.1 (Original)**

The ContractedUnitPrice column adheres to the following requirements:

* The ContractedUnitPrice column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports negotiated pricing concepts.
* This column MUST be a Decimal within the range of non-negative decimal values, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency.
* It MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.
* When ContractedUnitPrice is present and not null, multiplying ContractedUnitPrice by [PricingQuantity](#pricingquantity) MUST equal [ContractedCost](#contractedcost), except in cases of ChargeClass "Correction", which may address PricingQuantity or any cost discrepancies independently.

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
* The sum of EffectiveCost in a given *billing period* may not match the sum of the invoices received for the same *billing period* for a [*billing account*](#glossary:billing-account).
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

### **Invoice Issuer v.1.2 (Simplified Refinement)**

The InvoiceIssuerName column adheres to the following requirements:

* InvoiceIssuerName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* InvoiceIssuerName MUST be of type String.
* InvoiceIssuerName MUST conform to [String Handling](#stringhandling) requirements.
* InvoiceIssuerName MUST NOT be null.

### **Invoice Issuer v.1.2 (Technical Refinement)**

The InvoiceIssuerName column adheres to the following requirements:

* InvoiceIssuerName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* InvoiceIssuerName MUST be of type String.
* InvoiceIssuerName MUST conform to [String Handling](#stringhandling) requirements.
* InvoiceIssuerName MUST NOT be null.

### **Invoice Issuer v.1.1 (Original)**

The InvoiceIssuer column adheres to the following requirements:

* The InvoiceIssuer column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type String and MUST NOT contain null values.

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

### **Pricing Category v.1.2 (Simplified Refinement)**

The PricingCategory column adheres to the following requirements:

* PricingCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports more than one pricing category across all SKUs.
* PricingCategory MUST be of type String.
* PricingCategory nullability is defined as follows:
  * PricingCategory MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * PricingCategory MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * PricingCategory MAY be null in all other cases.
* When PricingCategory is not null, PricingCategory adheres to the following additional requirements:
  * PricingCategory MUST be one of the allowed values.
  * PricingCategory MUST be "Standard" when pricing is predetermined at the agreed upon rate for the [billing account](#glossary:billing-account).
  * PricingCategory MUST be "Committed" when the charge is subject to an existing *commitment discount* and is not the purchase of the *commitment discount*.
  * PricingCategory MUST be "Dynamic" when pricing is determined by the provider and may change over time, regardless of predetermined agreement pricing.
  * PricingCategory MUST be "Other" when there is a pricing model but none of the allowed values apply.

### **Pricing Category v.1.2 (Technical Refinement)**

The PricingCategory column adheres to the following requirements:

* PricingCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports more than one pricing category across all SKUs.
* If present, PricingCategory adheres to the following additional requirements:
  * PricingCategory MUST be of type String.
  * If [ChargeCategory](#chargecategory) is "Tax", PricingCategory adheres to the following additional requirement:
    * PricingCategory MUST be null.
  * Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", PricingCategory adheres to the following additional requirement:
    * PricingCategory MUST NOT be null.
  * Else PricingCategory adheres to the following additional requirement:
    * PricingCategory MAY be null.
  * If PricingCategory is not null, PricingCategory adheres to the following additional requirements:
    * PricingCategory MUST be one of the allowed values.
    * PricingCategory MUST be "Standard" when pricing is predetermined at the agreed upon rate for the [billing account](#glossary:billing-account).
    * PricingCategory MUST be "Committed" when the charge is subject to an existing *commitment discount* and is not the purchase of the *commitment discount*.
    * PricingCategory MUST be "Dynamic" when pricing is determined by the provider and may change over time, regardless of predetermined agreement pricing.
    * PricingCategory MUST be "Other" when there is a pricing model but none of the allowed values apply.

### **Pricing Category v.1.1 (Original)**

The PricingCategory column adheres to the following requirements:

* PricingCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports more than one pricing category across all SKUs and MUST be of type String.
* PricingCategory MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.
* PricingCategory MUST be one of the allowed values.
* PricingCategory MUST be "Standard" when pricing is predetermined at the agreed upon rate for the [billing account](#glossary:billing-account).
* PricingCategory MUST be "Committed" when the charge is subject to an existing *commitment discount* and is not the purchase of the *commitment discount*.
* PricingCategory MUST be "Dynamic" when pricing is determined by the provider and may change over time, regardless of predetermined agreement pricing.
* PricingCategory MUST be "Other" when there is a pricing model but none of the allowed values apply.

## Column: Pricing Quantity

### **PricingQuantity v.1.2 (Simplified Refinement)**

The PricingQuantity column adheres to the following requirements:

* PricingQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PricingQuantity MUST be of type Decimal.
* PricingQuantity MUST conform to [Numeric Format](#numericformat) requirements.
* PricingQuantity nullability is defined as follows:
  * PricingQuantity MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * PricingQuantity MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * PricingQuantity MAY be null in all other cases.
* When PricingQuantity is not null, PricingQuantity adheres to the following additional requirements:
  * PricingQuantity MUST be a valid decimal value.
  * The product of PricingQuantity and a unit price (e.g., [ContractedUnitPrice](#contractedunitprice)) MUST match the corresponding cost metric (e.g., [ContractedCost](#contractedcost)) when the unit price is not null and ChargeClass is not "Correction".
* Discrepancies in PricingQuantity, unit prices (e.g., ContractedUnitPrice), or costs (e.g., ContractedCost) MAY be addressed independently when ChargeClass is "Correction".

### **PricingQuantity v.1.2 (Technical Refinement)**

The PricingQuantity column adheres to the following requirements:

* PricingQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PricingQuantity MUST be of type Decimal.
* PricingQuantity MUST conform to [Numeric Format](#numericformat) requirements.
* If [ChargeCategory](#chargecategory) is "Tax", PricingQuantity adheres to the following additional requirement:
  * PricingQuantity MUST be null.
* Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", PricingQuantity adheres to the following additional requirement:
  * PricingQuantity MUST NOT be null.
* Else PricingQuantity adheres to the following additional requirement:
  * PricingQuantity MAY be null.
* If PricingQuantity is not null, PricingQuantity adheres to the following additional requirements:
  * PricingQuantity MUST be a valid decimal value.
  * The product of PricingQuantity and a unit price (e.g., [ContractedUnitPrice](#contractedunitprice)) MUST match the corresponding cost metric (e.g., [ContractedCost](#contractedcost)) when the unit price is present and not null, and ChargeClass is not "Correction".
* Discrepancies in PricingQuantity, unit prices (e.g., ContractedUnitPrice), or costs (e.g., ContractedCost) MAY be addressed independently if ChargeClass is "Correction".

### **PricingQuantity v.1.1 (Original)**

The PricingQuantity column adheres to the following requirements:

* The PricingQuantity column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* The value MAY be negative in cases where [ChargeClass](#chargeclass) is "Correction".
* This column MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.
* When unit prices (e.g. [ContractedUnitPrice](#contractedunitprice)) are not null, multiplying PricingQuantity by a unit price MUST produce a result equal to the corresponding cost metric (e.g. [ContractedCost](#contractedcost)), except in cases of ChargeClass "Correction", which may address PricingQuantity or any cost discrepancies independently.

## Column: Pricing Unit

### **Pricing Unit v.1.2 (Simplified Refinement)**

The PricingUnit column adheres to the following requirements:

* PricingUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PricingUnit MUST be of type String.
* PricingUnit MUST conform to [String Handling](#stringhandling) requirements.
* PricingUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
* PricingUnit nullability is defined as follows:
  * PricingUnit MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * PricingUnit MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * PricingUnit MAY be null in all other cases.
* When PricingUnit is not null, PricingUnit adheres to the following additional requirements:
  * PricingUnit MUST be semantically equal to the corresponding pricing measurement unit provided in provider-published [*price list*](#glossary:price-list).
  * PricingUnit MUST be semantically equal to the corresponding pricing measurement unit provided in invoice, when the invoice includes a pricing measurement unit.

### **Pricing Unit v.1.2 (Technical Refinement)**

The PricingUnit column adheres to the following requirements:

* PricingUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PricingUnit MUST be of type String.
* PricingUnit MUST conform to [String Handling](#stringhandling) requirements.
* PricingUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
* If [ChargeCategory](#chargecategory) is "Tax", PricingUnit adheres to the following additional requirement:
  * PricingUnit MUST be null.
* Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", PricingUnit adheres to the following additional requirement:
  * PricingUnit MUST NOT be null.
* Else PricingUnit adheres to the following additional requirement:
  * PricingUnit MAY be null.
* If PricingUnit is not null, PricingUnit adheres to the following additional requirements:
  * PricingUnit MUST be semantically equal to the corresponding pricing measurement unit provided in:
    * Provider-published [*price list*](#glossary:price-list)
    * Invoice, when the invoice includes a pricing measurement unit

### **Pricing Unit v.1.1 (Original)**

The PricingUnit column adheres to the following requirements:

* The PricingUnit column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type String.
* It MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.
* Units of measure used in PricingUnit SHOULD adhere to the values and format requirements specified in the [UnitFormat](#unitformat) attribute.

The PricingUnit value MUST be semantically equal to the corresponding pricing measurement unit value provided in:

* The provider-published [*price list*](#glossary:price-list)
* The invoice, when the invoice includes a pricing measurement unit

## Column: Provider

### **ProviderName v.1.2 (Simplified Refinement)**

The ProviderName column adheres to the following requirements:

* ProviderName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ProviderName MUST be of type String.
* ProviderName MUST conform to [String Handling](#stringhandling) requirements.
* ProviderName MUST NOT be null.

### **ProviderName v.1.2 (Technical Refinement)**

The ProviderName column adheres to the following requirements:

* ProviderName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ProviderName MUST be of type String.
* ProviderName MUST conform to [String Handling](#stringhandling) requirements.
* ProviderName MUST NOT be null.

### **ProviderName v.1.1 (Original)**

The Provider column adheres to the following requirements:

* The Provider column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type String and MUST NOT contain null values.

## Column: Publisher

### **Publisher v.1.2 (Simplified Refinement)**

The PublisherName column adheres to the following requirements:

* PublisherName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PublisherName MUST be of type String.
* PublisherName MUST conform to [String Handling](#stringhandling) requirements.
* PublisherName MUST NOT be null.

### **Publisher v.1.2 (Technical Refinement)**

The PublisherName column adheres to the following requirements:

* PublisherName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PublisherName MUST be of type String.
* PublisherName MUST conform to [String Handling](#stringhandling) requirements.
* PublisherName MUST NOT be null.

### **Publisher v.1.1 (Original)**

The Publisher column adheres to the following requirements:

* The Publisher column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type String and MUST NOT contain null values.

## Column: Region ID

### **Region ID v.1.2 (Simplified Refinement)**

The RegionId column adheres to the following requirements:

* RegionId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within a region.
* RegionId MUST be of type String.
* RegionId MUST conform to [String Handling](#stringhandling) requirements.
* Region ID nullability is defined as follows:
  * RegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region.
  * RegionId MAY be null when a *resource* or *service* is not operated in or managed from a distinct region.

### **Region ID v.1.2 (Technical Refinement)**

The RegionId column adheres to the following requirements:

* RegionId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within a region.
* If present, RegionId adheres to the following additional requirements:
  * RegionId MUST be of type String.
  * RegionId MUST conform to [String Handling](#stringhandling) requirements.
  * RegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region.
  * RegionId MAY be null when a *resource* or *service* is not operated in or managed from a distinct region.

### **Region ID v.1.1 (Original)**

The RegionId column adheres to the following requirements:

* The RegionId column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within a region and MUST be of type String.
* RegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region by the Provider and MAY contain null values when a *resource* or *service* is not restricted to an isolated geographic area.

## Column: Region Name

### **Region Name v.1.2 (Simplified Refinement)**

The RegionName column adheres to the following requirements:

* RegionName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within a region.
* RegionName MUST be of type String.
* RegionName MUST conform to [String Handling](#stringhandling) requirements.
* RegionName nullability is defined as follows:
  * RegionName MUST be null when [RegionId](#regionid) is null.
  * RegionName MUST NOT be null when RegionId is not null.

### **Region Name v.1.2 (Technical Refinement)**

The RegionName column adheres to the following requirements:

* RegionName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within a region.
* If present, RegionName adheres to the following additional requirements:
  * RegionName MUST be of type String.
  * RegionName MUST conform to [String Handling](#stringhandling) requirements.
  * RegionName MUST be null if [RegionId](#regionid) is null.
  * RegionName MUST NOT be null if RegionId is not null.

### **Region Name v.1.1 (Original)**

The RegionName column adheres to the following requirements:

* The RegionName column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within a region and MUST be of type String.
* RegionName MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region by the Provider and MAY contain null values when a *resource* or *service* is not restricted to an isolated geographic area.

## Column: Resource ID

### **Resource ID v.1.2 (Simplified Refinement)**

The ResourceId column adheres to the following requirements:

* ResourceId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources.
* ResourceId MUST be of type String.
* ResourceId MUST conform to [String Handling](#stringhandling) requirements.
* ResourceId nullability is defined as follows:
  * ResourceId MUST be null when a charge is not related to a *resource*.
  * ResourceId MUST NOT be null when a charge is related to a *resource*.
* When ResourceId is not null, ResourceId adheres to the following additional requirements:
  * ResourceId MUST be a unique identifier within the provider.
  * ResourceId SHOULD be a fully-qualified identifier.

### **Resource ID v.1.2 (Technical Refinement)**

The ResourceId column adheres to the following requirements:

* ResourceId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources.
* If present, ResourceId adheres to the following additional requirements:
  * ResourceId MUST be of type String.
  * ResourceId MUST conform to [String Handling](#stringhandling) requirements.
  * ResourceId MUST be null when a charge is not related to a *resource*.
  * ResourceId MUST NOT be null when a charge is related to a *resource*.
  * ResourceId MUST be a unique identifier within the provider.
  * ResourceId SHOULD be a fully-qualified identifier.

### **Resource ID v.1.1 (Original)**

The ResourceId column adheres to the following requirements:

* The ResourceId column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources.
* This column MUST be of type String.
* The ResourceId value MAY be a nullable column as some cost data [*rows*](#glossary:row) may not be associated with a *resource*.
* ResourceId MUST appear in the cost data if an identifier is assigned to a *resource* by the provider.
* ResourceId SHOULD be a fully-qualified identifier that ensures global uniqueness within the provider.

## Column: Resource Name

### **Resource Name v.1.2 (Simplified Refinement)**

The ResourceName column adheres to the following requirements:

* ResourceName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources.
* ResourceName MUST be of type String.
* ResourceName MUST conform to [String Handling](#stringhandling) requirements.
* ResourceName nullability is defined as follows:
  * ResourceName MUST be null when [ResourceId](#resourceid) is null or when the *resource* only has a system-generated ResourceId without an assigned display name.
  * ResourceName MUST NOT be null when ResourceId is not null and the *resource* has an assigned display name.
* ResourceName MUST NOT duplicate ResourceId when the *resources* is not provisioned interactively or only has a system-generated [ResourceId](#resourceid).

### **Resource Name v.1.2 (Technical Refinement)**

The ResourceName column adheres to the following requirements:

* ResourceName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources.
* If present, ResourceName adheres to the following additional requirements:
  * ResourceName MUST be of type String.
  * ResourceName MUST conform to [String Handling](#stringhandling) requirements.
  * ResourceName MUST be null if [ResourceId](#resourceid) is null or when the *resource* only has a system-generated ResourceId without an assigned display name.
  * ResourceName MUST NOT be null if ResourceId is not null and the *resource* has an assigned display name.
  * ResourceName SHOULD NOT duplicate ResourceId.

### **Resource Name v.1.1 (Original)**

The ResourceName column adheres to the following requirements:

* The ResourceName column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources.
* This column MUST be of type String.
* The ResourceName value MAY be a nullable column as some cost data [*rows*](#glossary:row) may not be associated with a *resource* or because a display name cannot be assigned to a *resource*.
* ResourceName MUST NOT be null if a display name can be assigned to a *resource*.
* *Resources* not provisioned interactively or only have a system-generated [ResourceId](#resourceid) MUST NOT duplicate the same value as the ResourceName.

## Column: Resource Type

### **Resource Type v.1.2 (Simplified Refinement)**

The ResourceType column adheres to the following requirements:

* ResourceType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources and supports assigning types to resources.
* ResourceType MUST be of type String.
* ResourceType MUST conform to [String Handling](#stringhandling) requirements.
* ResourceType nullability is defined as follows:
  * ResourceType MUST be null when [ResourceId](#resourceid) is null.
  * ResourceType MUST NOT be null when ResourceId is not null.

### **Resource Type v.1.2 (Technical Refinement)**

The ResourceType column adheres to the following requirements:

* ResourceType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources and supports assigning types to resources.
* If present, ResourceType adheres to the following additional requirements:
  * ResourceType MUST be of type String.
  * ResourceType MUST conform to [String Handling](#stringhandling) requirements.
  * ResourceType MUST be null if [ResourceId](#resourceid) is null.
  * ResourceType MUST NOT be null if ResourceId is not null.

### **Resource Type v.1.1 (Original)**

The ResourceType column adheres to the following requirements:

* The ResourceType column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources and supports assigning a type for resources.
* This column MUST be of type String and MUST NOT be null when a corresponding [ResourceId](#resourceid) is not null.
* When a corresponding ResourceId value is null, the ResourceType column value MUST also be null.

## Column: Service Category

### **Service Category v.1.2 (Simplified Refinement)**

The ServiceCategory column adheres to the following requirements:

* ServiceCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ServiceCategory MUST be of type String.
* ServiceCategory MUST NOT be null.
* ServiceCategory MUST be one of the allowed values.

### **Service Category v.1.2 (Technical Refinement)**

The ServiceCategory column adheres to the following requirements:

* ServiceCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ServiceCategory MUST be of type String.
* ServiceCategory MUST NOT be null.
* ServiceCategory MUST be one of the allowed values.

### **Service Category v.1.1 (Original)**

The ServiceCategory column adheres to the following requirements:

* The ServiceCategory column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null.
* This column is of type String and MUST be one of the allowed values.

## Column: Service Name

### **Service Name v.1.2 (Simplified Refinement)**

The ServiceName column adheres to the following requirements:

* ServiceName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ServiceName MUST be of type String.
* ServiceName MUST conform to [String Handling](#stringhandling) requirements.
* ServiceName MUST NOT be null.

### **Service Name v.1.2 (Technical Refinement)**

The ServiceName column adheres to the following requirements:

* ServiceName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ServiceName MUST be of type String.
* ServiceName MUST conform to [String Handling](#stringhandling) requirements.
* ServiceName MUST NOT be null.

### **Service Name v.1.1 (Original)**

The ServiceName column adheres to the following requirements:

* The ServiceName column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type String and MUST NOT contain null values.

## Column: Service Subcategory

### **Service Subcategory v.1.2 (Simplified Refinement)**

The ServiceSubcategory column adheres to the following requirements:

* ServiceSubcategory is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ServiceSubcategory MUST be of type String.
* ServiceSubcategory MUST NOT be null.
* ServiceSubcategory MUST be one of the allowed values.
* ServiceSubcategory MUST have one and only one parent ServiceCategory as specified in the allowed values below.
* Though a given *service* can have multiple purposes, each *service* SHOULD have one and only one ServiceSubcategory that best aligns with its primary purpose

### **Service Subcategory v.1.2 (Technical Refinement)**

The ServiceSubcategory column adheres to the following requirements:

* ServiceSubcategory is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* If present, ServiceSubcategory adheres to the following additional requirements:
  * ServiceSubcategory MUST be of type String.
  * ServiceSubcategory MUST NOT be null.
  * ServiceSubcategory MUST be one of the allowed values.
  * ServiceSubcategory MUST have one and only one parent ServiceCategory as specified in the allowed values below.
  * Though a given *service* can have multiple purposes, each *service* SHOULD have one and only one ServiceSubcategory that best aligns with its primary purpose

### **Service Subcategory v.1.1 (Original)**

The ServiceSubcategory column adheres to the following requirements:

* ServiceSubcategory is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null.
* ServiceSubcategory is of type String and MUST be one of the allowed values.
* Each ServiceSubcategory value MUST have one and only one parent ServiceCategory as specified in the allowed values below.
* Though a given *service* can have multiple purposes, each *service* SHOULD have one and only one ServiceSubcategory that best aligns with its primary purpose.

## Column: SKU ID

### **SKU ID v.1.2 (Simplified Refinement)**

The SkuId column adheres to the following requirements:

* SkuId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU list.
* SkuId MUST be of type String.
* SkuId MUST conform to [String Handling](#stringhandling) requirements.
* SkuId nullability is defined as follows:
  * SkuId MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * SkuId MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * SkuId MAY be null in all other cases.
* SkuId MUST equal SkuPriceId when a provider does not support an overarching SKU ID construct.

### **SKU ID v.1.2 (Technical Refinement)**

The SkuId column adheres to the following requirements:

* SkuId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU list.
* If present, SkuId adheres to the following additional requirements:
  * SkuId MUST be of type String.
  * SkuId MUST conform to [String Handling](#stringhandling) requirements.
  * SkuId MUST be null if [ChargeCategory](#chargecategory) is "Tax".
  * SkuId MUST NOT be null if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * SkuId MAY be null in all other cases.
  * SkuId MUST equal SkuPriceId when a provider does not support an overarching SKU ID construct.

### **SKU ID v.1.1 (Original)**

The SkuId column adheres to the following requirements:

* The SkuId column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU list.
* This column MUST be of type String.
* It MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.
* SkuId MUST equal SkuPriceId when a provider does not support an overarching SKU ID construct.

## Column: SKU Meter

### **SKU Meter v.1.2 (Simplified Refinement)**

The SkuMeter column adheres to the following requirements:

* SkuMeter MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU list.
* SkuMeter MUST be of type String.
* SkuMeter MUST conform to [String Handling](#stringhandling) requirements.
* SkuMeter nullability is defined as follows:
  * SkuMeter MUST be null when SkuId is null.
  * SkuMeter SHOULD NOT be null when SkuId is not null.
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
* SkuPriceDetails keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* SkuPriceDetails nullability is defined as follows:
  * SkuPriceDetails MUST be null when SkuPriceId is null.
  * SkuPriceDetails MAY be null when SkuPriceId is not null.
* When SkuPriceDetails is not null, SkuPriceDetails adheres to the following additional requirements:
  * SkuPriceDetails MUST NOT contain properties which are not applicable to the corresponding SkuPriceId.
  * SkuPriceDetails MAY contain properties which are already captured in other dedicated columns.
  * SkuPriceDetails SHOULD remain consistent over time for a given SkuPriceId.
  * SkuPriceDetails properties for a given SkuPriceId adhere to the following additional requirements:
      * Existing SkuPriceDetails properties SHOULD remain consistent over time.
      * Existing SkuPriceDetails properties SHOULD NOT be removed.
      * Additional SkuPriceDetails properties MAY be added over time.
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
  * Tag key with a non-null value for a given *resource* SHOULD be included in the Tags column.
  * Tag key with a null value for a given *resource* MAY be included in the Tags column depending on the provider's tag finalization process.
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
