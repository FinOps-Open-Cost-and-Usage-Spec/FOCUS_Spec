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
* When BillingAccountName is not null, BillingAccountName adheres to the following additional requirements:
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

## Column: Billing Period End

## Column: Billing Period Start

## Column: Capacity Reservation ID

## Column: Capacity Reservation Status

## Column: Charge Category

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

## Column: Invoice Issuer

## Column: List Cost

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
