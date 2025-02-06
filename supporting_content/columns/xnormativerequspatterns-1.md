# Normative Requirements - Part 1

Technical/Actionable Requirement

## Nullability

### Nullability Pattern 1

```markdown
* (*Optional*) <ColumnId> nullability is defined as follows:
  * <ColumnId> MUST NOT be null.
```

Applies to the following columns:

* BillingAccountId
* BillingCurrency
* BillingPeriodEnd
* BillingPeriodStart
* ChargePeriodEnd
* ChargePeriodStart
* ServiceName
* EffectiveCost
* BilledCost
* ContractedCost
* ListCost
* InvoiceIssuerName
* ProviderName
* PublisherName
* ServiceCategory
* ServiceSubcategory
* ChargeCategory
* ChargeFrequency

---

* BillingAccountId MUST NOT be null.
* BillingCurrency MUST NOT be null.
* BillingPeriodEnd MUST NOT be null.
* BillingPeriodStart MUST NOT be null.
* ChargePeriodEnd MUST NOT be null.
* ChargePeriodStart MUST NOT be null.
* ServiceName MUST NOT be null.
* EffectiveCost MUST NOT be null.
* BilledCost MUST NOT be null.
* ContractedCost MUST NOT be null.
* ListCost MUST NOT be null.
* InvoiceIssuerName MUST NOT be null.
* ProviderName MUST NOT be null.
* PublisherName MUST NOT be null.
* ServiceCategory MUST NOT be null.
* ServiceSubcategory MUST NOT be null.
* ChargeCategory MUST NOT be null.
* ChargeFrequency MUST NOT be null.

### Nullability Pattern 2

```markdown
* (*Optional*) <ColumnId> nullability is defined as follows:
  * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null if/when <Condition>.
```

Applies to the following columns:

* AvailabilityZone
* BillingAccountName
* ChargeDescription

---

* AvailabilityZone MAY be null if a charge is not specific to an *availability zone*.
* BillingAccountName MUST NOT be null when the provider supports assigning a display name for the *billing account*.
* ChargeDescription SHOULD NOT be null.

### Nullability Pattern 3

```markdown
* <ColumnId> nullability is defined as follows:
  * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null if/when <Condition1>.
  * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null if/when <Condition2>.
```

Applies to the following columns:

* SubAccountId
* SubAccountName
* RegionId
* RegionName
* ResourceId
* CommitmentDiscountId
* ResourceType
* CommitmentDiscountType
* SkuMeter
* SkuPriceDetails
* CapacityReservationId
* ResourceName

---

* SubAccountId MUST be null when a charge is not related to a *sub account*.
* SubAccountId MUST NOT be null when a charge is related to a *sub account*.

* RegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region by the Provider.
* RegionId MAY be null when a *resource* or *service* is not restricted to an isolated geographic area.

* ResourceId MUST be null when a charge is not related to a *resource*.
* ResourceId MUST NOT be null when a charge is related to a *resource*.

* CommitmentDiscountId MUST be null when a charge is not related to a *commitment discount*.
* CommitmentDiscountId MUST NOT be null when a charge is related to a *commitment discount*.

* CapacityReservationId MUST be null when a charge is not related to a *capacity reservation*.
* CapacityReservationId SHOULD NOT be null when a charge is related to a capacity reservation.
* CapacityReservationId MUST NOT be null when a charge represents the unused portion of a *capacity reservation*.

* SubAccountName MUST be null if [SubAccountId](#subaccountid) is null.
* SubAccountName MUST NOT be null if SubAccountId is not null.

* RegionName MUST be null if [RegionId](#regionid) is null.
* RegionName MUST NOT be null if RegionId is not null.

* ResourceType MUST be null if [ResourceId](#resourceid) is null.
* ResourceType MUST NOT be null if ResourceId is not null.

* CommitmentDiscountType MUST be null if [CommitmentDiscountId](#commitmentdiscountid) is null.
* CommitmentDiscountType MUST NOT be null if CommitmentDiscountId is not null.

* SkuMeter MUST be null if SkuId is null.
* SkuMeter SHOULD NOT be null if SkuId is not null.

* SkuPriceDetails MUST be null when SkuPriceId is null.
* SkuPriceDetails MAY be null when SkuPriceId is not null.

* ResourceName MUST be null if [ResourceId](#resourceid) is null or when the *resource* only has a system-generated ResourceId without an assigned display name.
* ResourceName MUST NOT be null if ResourceId is not null and the *resource* has an assigned display name.

### Nullability Pattern 4

```markdown
* <ColumnId> nullability is defined as follows:
  * <ColumnId> MUST be null if <Condition>.
  * If <Condition>, the column adheres to the following additional requirements:
    * <ColumnId> MUST NOT be null if <Condition>.
    * <ColumnId> MAY be null if <Condition>.
```

Applies to the following columns:

* TODO

---

* CommitmentDiscountName MUST be null if [CommitmentDiscountId](#commitmentdiscountid) is null.
* If CommitmentDiscountId is not null, the column adheres to the following additional requirements:
  * CommitmentDiscountName MUST NOT be null when a display name can be assigned to a *commitment discount*.
  * CommitmentDiscountName MAY be null when a display name cannot be assigned to a *commitment discount*.

---

* ConsumedQuantity MUST be null if [ChargeCategory](#chargecategory) is not "Usage", or if ChargeCategory is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused".
* If ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", the column adheres to the following additional requirements:
  * ConsumedQuantity MUST NOT be null if [ChargeClass](#chargeclass) is not "Correction".
  * ConsumedQuantity MAY be null if ChargeClass is "Correction".

* ConsumedUnit MUST be null if [ChargeCategory](#chargecategory) is not "Usage", or if ChargeCategory is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused".
* If ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", the column adheres to the following additional requirements:
  * ConsumedUnit MUST NOT be null if [ChargeClass](#chargeclass) is not "Correction".
  * ConsumedUnit MAY be null if ChargeClass is "Correction".

---

### Nullability Pattern 5

Rplace this:

```markdown
* If <Condition>, <Column> adheres to the following additional requirements:
  * <Column> MUST NOT be null if <Condition>.
  * <Column> MAY be null if <Condition>.
* Else <Column> adheres to the following additional requirement:
  * <Column> MUST be null.
```

With this:

```markdown
* <ColumnId> nullability is defined as follows:
  * If <Condition>, <Column> adheres to the following additional requirements:
    * <Column> MUST NOT be null if <Condition>.
    * <Column> MAY be null if <Condition>.
  * <Column> MUST be null in all other cases.
```

---

* If ChargeCategory is "Usage" or "Purchase" and CommitmentDiscountId is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
  * CommitmentDiscountQuantity MUST NOT be null if [ChargeClass](#chargeclass) is not "Correction".
  * CommitmentDiscountQuantity MAY be null if ChargeClass is "Correction".
* Else CommitmentDiscountQuantity adheres to the following additional requirement:
  * CommitmentDiscountQuantity MUST be null.

* If ChargeCategory is "Usage" or "Purchase" and [CommitmentDiscountId](#commitmentdiscountid) is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
  * CommitmentDiscountUnit MUST NOT be null if [ChargeClass](#chargeclass) is not "Correction".
  * CommitmentDiscountUnit MAY be null if ChargeClass is "Correction".
* Else CommitmentDiscountQuantity adheres to the following additional requirement:
  * CommitmentDiscountUnit MUST be null.

### Nullability Pattern 6

TODO:

Replace this:

```markdown
* <ColumnId> MUST be null if <Condition>.
* If <Condition>, the column adheres to the following additional requirements:  
  * <ColumnId> MUST NOT be null.
```

With this:

```markdown
* <ColumnId> MUST be null if <Condition>.
* <ColumnId> MUST NOT be null if/when <Condition>.
```

Applies to the following columns:

* CapacityReservationStatus
* CommitmentDiscountCategory
* CommitmentDiscountStatus
* ChargeClass

---

* CapacityReservationStatus MUST be null if CapacityReservationId is null.
* If CapacityReservationId is not null and [ChargeCategory](#chargecategory) is "Usage", the column adheres to the following additional requirements:
  * CapacityReservationStatus MUST NOT be null.

* CommitmentDiscountCategory MUST be null if [CommitmentDiscountId](#commitmentdiscountid) is null.
* If CommitmentDiscountId is not null, the column adheres to the following additional requirements:
  * CommitmentDiscountCategory MUST NOT be null.

* CommitmentDiscountStatus MUST be null if [CommitmentDiscountId](#commitmentdiscountid) is null.
* If CommitmentDiscountId is not null and [Charge Category](#chargecategory) is "Usage", the column adheres to the following additional requirements:
  * CommitmentDiscountStatus MUST NOT be null.

* ChargeClass MUST be null when the row does not represent a correction or when it represents a correction within the current *billing period*.
* When the row represents a correction to a previously invoiced *billing period*, the column adheres to the following additional requirements:
  * ChargeClass MUST NOT be null.

### Nullability Pattern 7

Replace this:

```markdown
* If xxx, <ColumnId> adheres to the following additional requirement:
  * <ColumnId> MUST be null.
* Else if yyy, <ColumnId> adheres to the following additional requirement:
  * <ColumnId> MUST NOT be null.
* Else <ColumnId> adheres to the following additional requirement:
  * <ColumnId> MAY be null.
```

With this:

```markdown
* <ColumnId> nullability is defined as follows:
  * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null if/when <Condition>.
  * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null if/when <Condition>.
  * <ColumnId> MAY be null in all other cases.
```

Applies to the following columns:

* SkuPriceId
* SkuId
* PricingCategory
* PricingQuantity
* PricingUnit
* ContractedUnitPrice
* ListUnitPrice

---

* If [ChargeCategory](#chargecategory) is "Tax", SkuPriceId adheres to the following additional requirement:
  * SkuPriceId MUST be null.
* Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", SkuPriceId adheres to the following additional requirement:
  * SkuPriceId MUST NOT be null.
* Else SkuPriceId adheres to the following additional requirement:
  * SkuPriceId MAY be null.

* If [ChargeCategory](#chargecategory) is "Tax", SkuId adheres to the following additional requirement:
  * SkuId MUST be null.
* Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", SkuId adheres to the following additional requirement:
  * SkuId MUST NOT be null.
* Else SkuId adheres to the following additional requirement:
  * SkuId MAY be null.

* If [ChargeCategory](#chargecategory) is "Tax", the column adheres to the following additional requirement:
  * PricingCategory MUST be null.
* Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", the column adheres to the following additional requirement:
  * PricingCategory MUST NOT be null.
* Else the column adheres to the following additional requirement:
  * PricingCategory MAY be null.

* If [ChargeCategory](#chargecategory) is "Tax", the column adheres to the following additional requirement:
  * PricingQuantity MUST be null.
* Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", the column adheres to the following additional requirement:
  * PricingQuantity MUST NOT be null.
* Else the column adheres to the following additional requirement:
  * PricingQuantity MAY be null.

* If [ChargeCategory](#chargecategory) is "Tax", the column adheres to the following additional requirement:
  * PricingUnit MUST be null.
* Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", the column adheres to the following additional requirement:
  * PricingUnit MUST NOT be null.
* Else the column adheres to the following additional requirement:
  * PricingUnit MAY be null.

* If [ChargeCategory](#chargecategory) is "Tax", ContractedUnitPrice adheres to the following additional requirement:
  * ContractedUnitPrice MUST be null.
* Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", ContractedUnitPrice adheres to the following additional requirement:
  * ContractedUnitPrice MUST NOT be null.
* Else ContractedUnitPrice adheres to the following additional requirement:
  * ContractedUnitPrice MAY be null.

* If [ChargeCategory](#chargecategory) is "Tax", ListUnitPrice adheres to the following additional requirement:
  * ListUnitPrice MUST be null.
* Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", ListUnitPrice adheres to the following additional requirement:
  * ListUnitPrice MUST NOT be null.
* Else ListUnitPrice adheres to the following additional requirement:
  * ListUnitPrice MAY be null.

## If not null

Note! This applies to all requirements that follow the nullability - Value Format, Value Ranges, various 'Logical' requirements, ...

### If-Not-Null Pattern

```markdown
* If <ColumnId> is not null, <ColumnId> adheres to the following additional requirement(s):
```

Applies to the following columns:

* SkuPriceId  
* SkuId  
* PricingCategory  
* ConsumedQuantity  
* PricingQuantity  
* PricingUnit  
* CommitmentDiscountQuantity  
* CommitmentDiscountUnit  
* ContractedUnitPrice  
* ListUnitPrice  
* SkuMeter  
* SkuPriceDetails  
* Tags

Add for the following columns:

* CapacityReservationStatus
* CommitmentDiscountCategory
* CommitmentDiscountStatus
* ChargeClass

---

* If SkuPriceId is not null, SkuPriceId adheres to the following additional requirements:
* If SkuId is not null, SkuId adheres to the following additional requirement:
* If PricingCategory is not null, PricingCategory adheres to the following additional requirements:
* If ConsumedQuantity is not null, ConsumedQuantity adheres to the following additional requirement:
* If PricingQuantity is not null, PricingQuantity adheres to the following additional requirements:
* If PricingUnit is not null, PricingUnit adheres to the following additional requirements:
* If CommitmentDiscountQuantity is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
* If CommitmentDiscountUnit is not null, CommitmentDiscountUnit adheres to the following additional requirements:
* If ContractedUnitPrice is not null, ContractedUnitPrice adheres to the following additional requirements:
* If ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
* If SkuMeter is not null, SkuMeter adheres to the following additional requirement:
* If SkuPriceDetails is not null, SkuPriceDetails adheres to the following additional requirements:
* If Tags is not null, Tags adheres to the following additional requirements:
