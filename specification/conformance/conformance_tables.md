# Conformance Dataset: CostAndUsage

| ConformanceRuleId | Function | Reference | ApplicabilityCriteria | MustSatisfy | KeyWord | Requirement | Condition | Type | CRVersionIntroduced | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AvailabilityZone-C-000-C | Composite | AvailabilityZone | AVAILABILITY_ZONE_SUPPORTED |  |  | AND of [Check AvailabilityZone-C-001-M, Check AvailabilityZone-C-002-M, Check AvailabilityZone-C-003-C] |  | Static | 1.2 | Active |
| AvailabilityZone-C-001-M | Type | AvailabilityZone |  |  |  | TypeString(AvailabilityZone) |  | Static | 1.2 | Active |
| AvailabilityZone-C-002-M | Type | AvailabilityZone |  |  |  | FormatString(AvailabilityZone) |  | Static | 1.2 | Active |
| AvailabilityZone-C-003-C | Nullability | AvailabilityZone |  |  |  |  |  | Dynamic | 1.2 | Active |
| BilledCost-C-000-M | Composite | BilledCost |  |  |  | AND of [Check BilledCost-C-001-M, Check BilledCost-C-002-M, Check BilledCost-C-003-M, Check BilledCost-C-004-C, Check BilledCost-C-005-M, Check BilledCost-C-006-M] |  | Static | 1.2 | Active |
| BilledCost-C-001-M | Nullability | BilledCost |  |  |  | CheckNotValue(BilledCost, null) |  | Static | 1.2 | Active |
| BilledCost-C-002-M | Type | BilledCost |  |  |  | TypeDecimal(BilledCost) |  | Static | 1.2 | Active |
| BilledCost-C-003-M | Format | BilledCost |  |  |  | FormatNumeric(BilledCost) |  | Static | 1.2 | Active |
| BilledCost-C-004-C | Validation | BilledCost |  |  |  | CheckValue(BilledCost, 0) | CheckNotSameValue(ProviderName, InvoiceIssuerName) | Static | 1.2 | Active |
| BilledCost-C-005-M | Validation | BilledCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| BilledCost-C-006-M | Validation | BilledCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| BillingAccountId-C-000-M | Composite | BillingAccountId |  |  |  | AND of [Check BillingAccountId-C-001-M, Check BillingAccountId-C-002-M, Check BillingAccountId-C-003-M, Check BillingAccountId-C-004-M, Check BillingAccountId-C-005-O] |  | Static | 1.2 | Active |
| BillingAccountId-C-001-M | Nullability | BillingAccountId |  |  |  | CheckNotValue(BillingAccountId, null) |  | Static | 1.2 | Active |
| BillingAccountId-C-002-M | Type | BillingAccountId |  |  |  | TypeString(BillingAccountId) |  | Static | 1.2 | Active |
| BillingAccountId-C-003-M | Format | BillingAccountId |  |  |  | FormatString(BillingAccountId) |  | Static | 1.2 | Active |
| BillingAccountId-C-004-M | Validation | BillingAccountId |  |  |  |  |  | Dynamic | 1.2 | Active |
| BillingAccountId-C-005-O | Validation | BillingAccountId |  |  |  |  |  | Dynamic | 1.2 | Active |
| BillingAccountName-C-000-M | Composite | BillingAccountName |  |  |  | AND of [Check BillingAccountName-C-001-M, Check BillingAccountName-C-002-M, Check BillingAccountName-C-003-C] |  | Static | 1.2 | Active |
| BillingAccountName-C-001-M | Type | BillingAccountName |  |  |  | TypeString(BillingAccountName) |  | Static | 1.2 | Active |
| BillingAccountName-C-002-M | Type | BillingAccountName |  |  |  | FormatString(BillingAccountName) |  | Static | 1.2 | Active |
| BillingAccountName-C-003-C | Nullability | BillingAccountName | ACCOUNT_NAMING_SUPPORTED |  |  | CheckNotValue(BillingAccountName, null) |  | Static | 1.2 | Active |
| BillingAccountType-C-000-M | Composite | BillingAccountType |  |  |  | AND of [Check BillingAccountType-C-001-M, Check BillingAccountType-C-002-M, Check BillingAccountType-C-003-C, Check BillingAccountType-C-006-M] |  | Static | 1.2 | Active |
| BillingAccountType-C-001-M | Type | BillingAccountType |  |  |  | TypeString(BillingAccountType) |  | Static | 1.2 | Active |
| BillingAccountType-C-002-M | Format | BillingAccountType |  |  |  | FormatString(BillingAccountType) |  | Static | 1.2 | Active |
| BillingAccountType-C-003-C | Composite | BillingAccountType |  |  |  | AND of [Check BillingAccountType-C-004-C, Check BillingAccountType-C-005-C] |  | Static | 1.2 | Active |
| BillingAccountType-C-004-C | Nullability | BillingAccountType |  |  |  | CheckValue(BillingAccountType, null) | CheckValue(BillingAccountId, null) | Static | 1.2 | Active |
| BillingAccountType-C-005-C | Nullability | BillingAccountType |  |  |  | CheckNotValue(BillingAccountType, null) | CheckNotValue(BillingAccountId, null) | Static | 1.2 | Active |
| BillingAccountType-C-006-M | Validation | BillingAccountType |  |  |  |  |  | Dynamic | 1.2 | Active |
| BillingCurrency-C-000-M | Composite | BillingCurrency |  |  |  | AND of [Check BillingCurrency-C-001-M, Check BillingCurrency-C-002-M, Check BillingCurrency-C-003-M, Check BillingCurrency-C-004-M, Check BillingCurrency-C-005-M, Check BillingCurrency-C-006-M] |  | Static | 1.2 | Active |
| BillingCurrency-C-001-M | Type | BillingCurrency |  |  |  | TypeString(BillingCurrency) |  | Static | 1.2 | Active |
| BillingCurrency-C-002-M | Validation | BillingCurrency |  |  |  | FormatString(BillingCurrency) |  | Static | 1.2 | Active |
| BillingCurrency-C-003-M | Format | BillingCurrency |  |  |  | FormatCurrency(BillingCurrency) |  | Static | 1.2 | Active |
| BillingCurrency-C-004-M | Nullability | BillingCurrency |  |  |  | CheckNotValue(BillingCurrency, null) |  | Static | 1.2 | Active |
| BillingCurrency-C-005-M | Validation | BillingCurrency |  |  |  |  |  | Dynamic | 1.2 | Active |
| BillingCurrency-C-006-M | Validation | BillingCurrency |  |  |  | CheckNationalCurrency(BillingCurrency) |  | Static | 1.2 | Active |
| BillingPeriodEnd-C-000-M | Composite | BillingPeriodEnd |  |  |  | AND of [Check BillingPeriodEnd-C-001-M, Check BillingPeriodEnd-C-002-M, Check BillingPeriodEnd-C-003-M, Check BillingPeriodEnd-C-004-M] |  | Static | 1.2 | Active |
| BillingPeriodEnd-C-001-M | Type | BillingPeriodEnd |  |  |  | TypeDateTime(BillingPeriodEnd) |  | Static | 1.2 | Active |
| BillingPeriodEnd-C-002-M | Format | BillingPeriodEnd |  |  |  | FormatDateTime(BillingPeriodEnd) |  | Static | 1.2 | Active |
| BillingPeriodEnd-C-003-M | Nullability | BillingPeriodEnd |  |  |  | CheckNotValue(BillingPeriodEnd, null) |  | Static | 1.2 | Active |
| BillingPeriodEnd-C-004-M | Validation | BillingPeriodEnd |  |  |  |  |  | Dynamic | 1.2 | Active |
| BillingPeriodStart-C-000-M | Composite | BillingPeriodStart |  |  |  | AND of [Check BillingPeriodStart-C-001-M, Check BillingPeriodStart-C-002-M, Check BillingPeriodStart-C-003-M, Check BillingPeriodStart-C-004-M] |  | Static | 1.2 | Active |
| BillingPeriodStart-C-001-M | Type | BillingPeriodStart |  |  |  | TypeDateTime(BillingPeriodStart) |  | Static | 1.2 | Active |
| BillingPeriodStart-C-002-M | Format | BillingPeriodStart |  |  |  | FormatDateTime(BillingPeriodStart) |  | Static | 1.2 | Active |
| BillingPeriodStart-C-003-M | Nullability | BillingPeriodStart |  |  |  | CheckNotValue(BillingPeriodStart, null) |  | Static | 1.2 | Active |
| BillingPeriodStart-C-004-M | Validation | BillingPeriodStart |  |  |  |  |  | Dynamic | 1.2 | Active |
| CapacityReservationId-C-000-C | Composite | CapacityReservationId | CAPACITY_RESERVATION_SUPPORTED |  |  | AND of [Check CapacityReservationId-C-001-M, Check CapacityReservationId-C-002-M, Check CapacityReservationId-C-003-C, Check CapacityReservationId-C-007-C] |  | Static | 1.2 | Active |
| CapacityReservationId-C-001-M | Type | CapacityReservationId |  |  |  | TypeString(CapacityReservationId) |  | Static | 1.2 | Active |
| CapacityReservationId-C-002-M | Format | CapacityReservationId |  |  |  | FormatString(CapacityReservationId) |  | Static | 1.2 | Active |
| CapacityReservationId-C-003-C | Composite | CapacityReservationId |  |  |  | AND of [Check CapacityReservationId-C-004-C, Check CapacityReservationId-C-005-C, Check CapacityReservationId-C-006-C] |  | Static | 1.2 | Active |
| CapacityReservationId-C-004-C | Nullability | CapacityReservationId |  |  |  |  |  | Dynamic | 1.2 | Active |
| CapacityReservationId-C-005-C | Nullability | CapacityReservationId |  |  |  | CheckNotValue(CapacityReservationId, null) | CheckValue(CapacityReservationStatus, Unused) | Static | 1.2 | Active |
| CapacityReservationId-C-006-C | Nullability | CapacityReservationId |  |  |  |  |  | Dynamic | 1.2 | Active |
| CapacityReservationId-C-007-C | Composite | CapacityReservationId |  |  |  | AND of [Check CapacityReservationId-C-008-M, Check CapacityReservationId-C-009-O] | CheckNotValue(CapacityReservationId, null) | Static | 1.2 | Active |
| CapacityReservationId-C-008-M | Validation | CapacityReservationId |  |  |  |  |  | Dynamic | 1.2 | Active |
| CapacityReservationId-C-009-O | Validation | CapacityReservationId |  |  |  |  |  | Dynamic | 1.2 | Active |
| CapacityReservationStatus-C-000-C | Composite | CapacityReservationStatus | CAPACITY_RESERVATION_SUPPORTED |  |  | AND of [Check CapacityReservationStatus-C-001-M, Check CapacityReservationStatus-C-002-C, Check CapacityReservationStatus-C-005-C] |  | Static | 1.2 | Active |
| CapacityReservationStatus-C-001-M | Type | CapacityReservationStatus |  |  |  | TypeString(CapacityReservationStatus) |  | Static | 1.2 | Active |
| CapacityReservationStatus-C-002-C | Composite | CapacityReservationStatus |  |  |  | AND of [Check CapacityReservationStatus-C-003-C, Check CapacityReservationStatus-C-004-C] |  | Static | 1.2 | Active |
| CapacityReservationStatus-C-003-C | Nullability | CapacityReservationStatus |  |  |  | CheckValue(CapacityReservationStatus, null) |  | Static | 1.2 | Active |
| CapacityReservationStatus-C-004-C | Nullability | CapacityReservationStatus |  |  |  | CheckNotValue(CapacityReservationStatus, null) |  | Static | 1.2 | Active |
| CapacityReservationStatus-C-005-C | Composite | CapacityReservationStatus |  |  |  | AND of [Check CapacityReservationStatus-C-006-M, Check CapacityReservationStatus-C-007-C, Check CapacityReservationStatus-C-008-C] | CheckNotValue(CapacityReservationStatus, null) | Static | 1.2 | Active |
| CapacityReservationStatus-C-006-M | Validation | CapacityReservationStatus |  |  |  | OR of [CheckValue(CapacityReservationStatus, Used), CheckValue(CapacityReservationStatus, Unused)] |  | Static | 1.2 | Active |
| CapacityReservationStatus-C-007-C | Validation | CapacityReservationStatus |  |  |  |  |  | Dynamic | 1.2 | Active |
| CapacityReservationStatus-C-008-C | Validation | CapacityReservationStatus |  |  |  |  |  | Dynamic | 1.2 | Active |
| ChargeCategory-C-000-M | Composite | ChargeCategory |  |  |  | AND of [Check ChargeCategory-C-001-M, Check ChargeCategory-C-002-M, Check ChargeCategory-C-003-M] |  | Static | 1.2 | Active |
| ChargeCategory-C-001-M | Type | ChargeCategory |  |  |  | TypeString(ChargeCategory) |  | Static | 1.2 | Active |
| ChargeCategory-C-002-M | Nullability | ChargeCategory |  |  |  | CheckNotValue(ChargeCategory, null) |  | Static | 1.2 | Active |
| ChargeCategory-C-003-M | Validation | ChargeCategory |  |  |  | OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase), CheckValue(ChargeCategory, Tax), CheckValue(ChargeCategory, Credit), CheckValue(ChargeCategory, Adjustment)] |  | Static | 1.2 | Active |
| ChargeClass-C-000-M | Composite | ChargeClass |  |  |  | AND of [Check ChargeClass-C-001-M, Check ChargeClass-C-002-C, Check ChargeClass-C-005-C] |  | Static | 1.2 | Active |
| ChargeClass-C-001-M | Type | ChargeClass |  |  |  | TypeString(ChargeClass) |  | Static | 1.2 | Active |
| ChargeClass-C-002-C | Composite | ChargeClass |  |  |  | AND of [Check ChargeClass-C-003-C, Check ChargeClass-C-004-C] |  | Static | 1.2 | Active |
| ChargeClass-C-003-C | Nullability | ChargeClass |  |  |  |  |  | Dynamic | 1.2 | Active |
| ChargeClass-C-004-C | Nullability | ChargeClass |  |  |  |  |  | Dynamic | 1.2 | Active |
| ChargeClass-C-005-C | Validation | ChargeClass |  |  |  | CheckValue(ChargeClass, Correction) | CheckNotValue(ChargeClass, null) | Static | 1.2 | Active |
| ChargeDescription-C-000-M | Composite | ChargeDescription |  |  |  | AND of [Check ChargeDescription-C-001-M, Check ChargeDescription-C-002-M, Check ChargeDescription-C-003-O, Check ChargeDescription-C-004-O] |  | Static | 1.2 | Active |
| ChargeDescription-C-001-M | Type | ChargeDescription |  |  |  | TypeString(ChargeDescription) |  | Static | 1.2 | Active |
| ChargeDescription-C-002-M | Format | ChargeDescription |  |  |  | FormatString(ChargeDescription) |  | Static | 1.2 | Active |
| ChargeDescription-C-003-O | Nullability | ChargeDescription |  |  |  | CheckNotValue(ChargeDescription, null) |  | Static | 1.2 | Active |
| ChargeDescription-C-004-O | Validation | ChargeDescription |  |  |  |  |  | Dynamic | 1.2 | Active |
| ChargeFrequency-C-000-O | Composite | ChargeFrequency |  |  |  | AND of [Check ChargeFrequency-C-001-M, Check ChargeFrequency-C-002-M, Check ChargeFrequency-C-003-M, Check ChargeFrequency-C-004-C] |  | Static | 1.2 | Active |
| ChargeFrequency-C-001-M | Type | ChargeFrequency |  |  |  | TypeString(ChargeFrequency) |  | Static | 1.2 | Active |
| ChargeFrequency-C-002-M | Nullability | ChargeFrequency |  |  |  | CheckNotValue(ChargeFrequency, null) |  | Static | 1.2 | Active |
| ChargeFrequency-C-003-M | Validation | ChargeFrequency |  |  |  | OR of [CheckValue(ChargeFrequency, One-Time), CheckValue(ChargeFrequency, Recurring), CheckValue(ChargeFrequency, Usage-Based)] |  | Static | 1.2 | Active |
| ChargeFrequency-C-004-C | Validation | ChargeFrequency |  |  |  | CheckNotValue(ChargeFrequency, Usage-Based) | CheckValue(ChargeCategory, Purchase) | Static | 1.2 | Active |
| ChargePeriodEnd-C-000-M | Composite | ChargePeriodEnd |  |  |  | AND of [Check ChargePeriodEnd-C-001-M, Check ChargePeriodEnd-C-002-M, Check ChargePeriodEnd-C-003-M, Check ChargePeriodEnd-C-004-M] |  | Static | 1.2 | Active |
| ChargePeriodEnd-C-001-M | Type | ChargePeriodEnd |  |  |  | TypeDateTime(ChargePeriodEnd) |  | Static | 1.2 | Active |
| ChargePeriodEnd-C-002-M | Format | ChargePeriodEnd |  |  |  | FormatDateTime(ChargePeriodEnd) |  | Static | 1.2 | Active |
| ChargePeriodEnd-C-003-M | Nullability | ChargePeriodEnd |  |  |  | CheckNotValue(ChargePeriodEnd, null) |  | Static | 1.2 | Active |
| ChargePeriodEnd-C-004-M | Validation | ChargePeriodEnd |  |  |  |  |  | Dynamic | 1.2 | Active |
| ChargePeriodStart-C-000-M | Composite | ChargePeriodStart |  |  |  | AND of [Check ChargePeriodStart-C-001-M, Check ChargePeriodStart-C-002-M, Check ChargePeriodStart-C-003-M, Check ChargePeriodStart-C-004-M] |  | Static | 1.2 | Active |
| ChargePeriodStart-C-001-M | Type | ChargePeriodStart |  |  |  | TypeDateTime(ChargePeriodStart) |  | Static | 1.2 | Active |
| ChargePeriodStart-C-002-M | Format | ChargePeriodStart |  |  |  | FormatDateTime(ChargePeriodStart) |  | Static | 1.2 | Active |
| ChargePeriodStart-C-003-M | Nullability | ChargePeriodStart |  |  |  | CheckNotValue(ChargePeriodStart) |  | Static | 1.2 | Active |
| ChargePeriodStart-C-004-M | Validation | ChargePeriodStart |  |  |  |  |  | Dynamic | 1.2 | Active |
| CommitmentDiscountCategory-C-000-C | Composite | CommitmentDiscountCategory | COMMITMENT_DISCOUNT_SUPPORTED |  |  | AND of [Check CommitmentDiscountCategory-C-001-M, Check CommitmentDiscountCategory-C-002-C, Check CommitmentDiscountCategory-C-005-M] |  | Static | 1.2 | Active |
| CommitmentDiscountCategory-C-001-M | Type | CommitmentDiscountCategory |  |  |  | TypeString(CommitmentDiscountCategory) |  | Static | 1.2 | Active |
| CommitmentDiscountCategory-C-002-C | Composite | CommitmentDiscountCategory |  |  |  | AND of [Check CommitmentDiscountCategory-C-003-C, Check CommitmentDiscountCategory-C-004-C] |  | Static | 1.2 | Active |
| CommitmentDiscountCategory-C-003-C | Nullability | CommitmentDiscountCategory |  |  |  | CheckValue(CommitmentDiscountCategory, null) | CheckValue(CommitmentDiscountId, null) | Static | 1.2 | Active |
| CommitmentDiscountCategory-C-004-C | Nullability | CommitmentDiscountCategory |  |  |  | CheckNotValue(CommitmentDiscountCategory, null) | CheckNotValue(CommitmentDiscountId, null) | Static | 1.2 | Active |
| CommitmentDiscountCategory-C-005-M | Validation | CommitmentDiscountCategory |  |  |  | OR of [CheckValue(CommitmentDiscountCategory, Spend), CheckValue(CommitmentDiscountCategory, Usage)] |  | Static | 1.2 | Active |
| CommitmentDiscountId-C-000-C | Composite | CommitmentDiscountId | COMMITMENT_DISCOUNT_SUPPORTED |  |  | AND of [Check CommitmentDiscountId-C-001-M, Check CommitmentDiscountId-C-002-M, Check CommitmentDiscountId-C-003-C, Check CommitmentDiscountId-C-006-C] |  | Static | 1.2 | Active |
| CommitmentDiscountId-C-001-M | Type | CommitmentDiscountId |  |  |  | TypeString(CommitmentDiscountId) |  | Static | 1.2 | Active |
| CommitmentDiscountId-C-002-M | Format | CommitmentDiscountId |  |  |  | FormatString(CommitmentDiscountId) |  | Static | 1.2 | Active |
| CommitmentDiscountId-C-003-C | Composite | CommitmentDiscountId |  |  |  | AND of [Check CommitmentDiscountId-C-004-C, Check CommitmentDiscountId-C-005-C] |  | Static | 1.2 | Active |
| CommitmentDiscountId-C-004-C | Nullability | CommitmentDiscountId |  |  |  |  |  | Dynamic | 1.2 | Active |
| CommitmentDiscountId-C-005-C | Nullability | CommitmentDiscountId |  |  |  |  |  | Dynamic | 1.2 | Active |
| CommitmentDiscountId-C-006-C | Composite | CommitmentDiscountId |  |  |  | AND of [Check CommitmentDiscountId-C-007-M, Check CommitmentDiscountId-C-008-C] | CheckNotValue(CommitmentDiscountId, null) | Static | 1.2 | Active |
| CommitmentDiscountId-C-007-M | Validation | CommitmentDiscountId |  |  |  |  |  | Dynamic | 1.2 | Active |
| CommitmentDiscountId-C-008-C | Validation | CommitmentDiscountId |  |  |  |  |  | Dynamic | 1.2 | Active |
| CommitmentDiscountName-C-000-C | Composite | CommitmentDiscountName | COMMITMENT_DISCOUNT_SUPPORTED |  |  | AND of [Check CommitmentDiscountName-C-001-M, Check CommitmentDiscountName-C-002-M, Check CommitmentDiscountName-C-003-C, Check CommitmentDiscountName-C-004-C] |  | Static | 1.2 | Active |
| CommitmentDiscountName-C-001-M | Type | CommitmentDiscountName |  |  |  | TypeString(CommitmentDiscountName) |  | Static | 1.2 | Active |
| CommitmentDiscountName-C-002-M | Validation | CommitmentDiscountName |  |  |  | FormatString(CommitmentDiscountName) |  | Static | 1.2 | Active |
| CommitmentDiscountName-C-003-C | Composite | CommitmentDiscountName |  |  |  | AND of [Check CommitmentDiscountName-C-004-C, Check CommitmentDiscountName-C-005-C] |  | Static | 1.2 | Active |
| CommitmentDiscountName-C-004-C | Nullability | CommitmentDiscountName |  |  |  | CheckValue(CommitmentDiscountName, null) | CheckValue(CommitmentDiscountId, null) | Static | 1.2 | Active |
| CommitmentDiscountName-C-005-C | Composite | CommitmentDiscountName |  |  |  | AND of [Check CommitmentDiscountName-C-006-C, Check CommitmentDiscountName-C-007-C] | CheckNotValue(CommitmentDiscountId, null) | Static | 1.2 | Active |
| CommitmentDiscountName-C-006-C | Nullability | CommitmentDiscountName |  |  |  |  |  | Dynamic | 1.2 | Active |
| CommitmentDiscountName-C-007-C | Nullability | CommitmentDiscountName |  |  |  |  |  | Dynamic | 1.2 | Active |
| CommitmentDiscountQuantity-C-000-C | Composite | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  | AND of [Check CommitmentDiscountQuantity-C-001-M, Check CommitmentDiscountQuantity-C-002-M, Check CommitmentDiscountQuantity-C-003-M, Check CommitmentDiscountQuantity-C-004-C, Check CommitmentDiscountQuantity-C-009-C] |  | Static | 1.2 | Active |
| CommitmentDiscountQuantity-C-001-M | Type | CommitmentDiscountQuantity |  |  |  | TypeDecimal(CommitmentDiscountQuantity) |  | Static | 1.2 | Active |
| CommitmentDiscountQuantity-C-002-M | Format | CommitmentDiscountQuantity |  |  |  | FormatNumeric(CommitmentDiscountQuantity) |  | Static | 1.2 | Active |
| CommitmentDiscountQuantity-C-003-M | Validation | CommitmentDiscountQuantity |  |  |  |  |  | Dynamic | 1.2 | Active |
| CommitmentDiscountQuantity-C-004-C | Composite | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  | AND of [Check CommitmentDiscountQuantity-C-005-C, Check CommitmentDiscountQuantity-C-008-C] |  | Static | 1.2 | Active |
| CommitmentDiscountQuantity-C-005-C | Composite | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  | AND of [Check CommitmentDiscountQuantity-C-006-C, Check CommitmentDiscountQuantity-C-007-C] | AND of [OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)], CheckNotValue(CommitmentDiscountId, null)] | Static | 1.2 | Active |
| CommitmentDiscountQuantity-C-006-C | Nullability | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  | CheckNotValue(CommitmentDiscountQuantity, null) | AND of [OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)], CheckNotValue(CommitmentDiscountId, null), CheckNotValue(ChargeClass, Correction)] | Static | 1.2 | Active |
| CommitmentDiscountQuantity-C-007-C | Nullability | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  | CheckValue(CommitmentDiscountQuantity, null) | CheckValue(ChargeClass, Correction) | Static | 1.2 | Active |
| CommitmentDiscountQuantity-C-008-C | Nullability | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  | CheckValue(CommitmentDiscountQuantity, null) | OR of [AND of [CheckNotValue(ChargeCategory, Usage), CheckNotValue(ChargeCategory, Purchase)], CheckValue(CommitmentDiscountId, null), CheckValue(ChargeClass, Correction)] | Static | 1.2 | Active |
| CommitmentDiscountQuantity-C-009-C | Composite | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  | AND of [Check CommitmentDiscountQuantity-C-010-C, Check CommitmentDiscountQuantity-C-013-C] | CheckNotValue(CommitmentDiscountQuantity, null) | Static | 1.2 | Active |
| CommitmentDiscountQuantity-C-010-C | Composite | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  | AND of [Check CommitmentDiscountQuantity-C-011-C, Check CommitmentDiscountQuantity-C-012-C] | CheckValue(ChargeCategory, Purchase) | Static | 1.2 | Active |
| CommitmentDiscountQuantity-C-011-C | Validation | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  |  | AND of [CheckValue(ChargeCategory, Purchase), CheckValue(ChargeFrequency, One-Time)] | Dynamic | 1.2 | Active |
| CommitmentDiscountQuantity-C-012-C | Validation | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  |  | AND of [CheckValue(ChargeCategory, Purchase), CheckValue(ChargeFrequency, Recurring)] | Dynamic | 1.2 | Active |
| CommitmentDiscountQuantity-C-013-C | Composite | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  | AND of [Check CommitmentDiscountQuantity-C-014-C, Check CommitmentDiscountQuantity-C-015-C] | CheckValue(ChargeCategory, Usage) | Static | 1.2 | Active |
| CommitmentDiscountQuantity-C-014-C | Validation | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  |  | AND of [CheckValue(ChargeCategory, Usage), CheckValue(CommitmentDiscountStatus, Used)] | Dynamic | 1.2 | Active |
| CommitmentDiscountQuantity-C-015-C | Validation | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  |  | AND of [CheckValue(ChargeCategory, Usage), CheckValue(CommitmentDiscountStatus, Unused)] | Dynamic | 1.2 | Active |
| CommitmentDiscountStatus-C-000-C | Composite | CommitmentDiscountStatus | COMMITMENT_DISCOUNT_SUPPORTED |  |  | AND of [Check CommitmentDiscountStatus-C-001-M, Check CommitmentDiscountStatus-C-002-M, Check CommitmentDiscountStatus-C-003-M] |  | Static | 1.2 | Active |
| CommitmentDiscountStatus-C-001-M | Type | CommitmentDiscountStatus |  |  |  | TypeString(CommitmentDiscountStatus) |  | Static | 1.2 | Active |
| CommitmentDiscountStatus-C-002-M | Nullability | CommitmentDiscountStatus |  |  |  | CheckNotValue(CommitmentDiscountStatus, null) |  | Static | 1.2 | Active |
| CommitmentDiscountStatus-C-003-M | Validation | CommitmentDiscountStatus |  |  |  | OR of [CheckValue(CommitmentDiscountStatus, Active), CheckValue(CommitmentDiscountStatus, Expired), CheckValue(CommitmentDiscountStatus, Pending)] |  | Static | 1.2 | Active |
| CommitmentDiscountType-C-000-C | Composite | CommitmentDiscountType | COMMITMENT_DISCOUNT_SUPPORTED |  |  | AND of [Check CommitmentDiscountType-C-001-M, Check CommitmentDiscountType-C-002-M, Check CommitmentDiscountType-C-003-C] |  | Static | 1.2 | Active |
| CommitmentDiscountType-C-001-M | Type | CommitmentDiscountType |  |  |  | TypeString(CommitmentDiscountType) |  | Static | 1.2 | Active |
| CommitmentDiscountType-C-002-M | Format | CommitmentDiscountType |  |  |  | FormatString(CommitmentDiscountType) |  | Static | 1.2 | Active |
| CommitmentDiscountType-C-003-C | Composite | CommitmentDiscountType |  |  |  | AND of [Check CommitmentDiscountType-C-004-C, Check CommitmentDiscountType-C-005-C] |  | Static | 1.2 | Active |
| CommitmentDiscountType-C-004-C | Nullability | CommitmentDiscountType |  |  |  | CheckValue(CommitmentDiscountType, null) | CheckValue(CommitmentDiscountId, null) | Static | 1.2 | Active |
| CommitmentDiscountType-C-005-C | Nullability | CommitmentDiscountType |  |  |  | CheckNotValue(CommitmentDiscountType, null) | CheckNotValue(CommitmentDiscountId, null) | Static | 1.2 | Active |
| CommitmentDiscountUnit-C-000-C | Composite | CommitmentDiscountUnit | COMMITMENT_DISCOUNT_SUPPORTED |  |  | AND of [Check CommitmentDiscountUnit-C-001-M, Check CommitmentDiscountUnit-C-002-M, Check CommitmentDiscountUnit-C-003-M, Check CommitmentDiscountUnit-C-004-C, Check CommitmentDiscountUnit-C-007-C] |  | Static | 1.2 | Active |
| CommitmentDiscountUnit-C-001-M | Type | CommitmentDiscountUnit |  |  |  | TypeString(CommitmentDiscountUnit) |  | Static | 1.2 | Active |
| CommitmentDiscountUnit-C-002-M | Format | CommitmentDiscountUnit |  |  |  | FormatString(CommitmentDiscountUnit) |  | Static | 1.2 | Active |
| CommitmentDiscountUnit-C-003-M | Format | CommitmentDiscountUnit |  |  |  | FormatUnit(CommitmentDiscountUnit) |  | Static | 1.2 | Active |
| CommitmentDiscountUnit-C-004-C | Composite | CommitmentDiscountUnit |  |  |  | AND of [Check CommitmentDiscountUnit-C-005-C, Check CommitmentDiscountUnit-C-006-C] |  | Static | 1.2 | Active |
| CommitmentDiscountUnit-C-005-C | Nullability | CommitmentDiscountUnit |  |  |  | CheckValue(CommitmentDiscountUnit, null) | CheckValue(CommitmentDiscountQuantity, null) | Static | 1.2 | Active |
| CommitmentDiscountUnit-C-006-C | Nullability | CommitmentDiscountUnit |  |  |  | CheckNotValue(CommitmentDiscountUnit, null) | CheckNotValue(CommitmentDiscountQuantity, null) | Static | 1.2 | Active |
| CommitmentDiscountUnit-C-007-C | Composite | CommitmentDiscountUnit |  |  |  | AND of [Check CommitmentDiscountUnit-C-008-M, Check CommitmentDiscountUnit-C-009-M, Check CommitmentDiscountUnit-C-010-C] | CheckNotValue(CommitmentDiscountUnit, null) | Static | 1.2 | Active |
| CommitmentDiscountUnit-C-008-M | Validation | CommitmentDiscountUnit |  |  |  |  |  | Dynamic | 1.2 | Active |
| CommitmentDiscountUnit-C-009-M | Validation | CommitmentDiscountUnit |  |  |  |  |  | Dynamic | 1.2 | Active |
| CommitmentDiscountUnit-C-010-C | Validation | CommitmentDiscountUnit |  |  |  |  |  | Dynamic | 1.2 | Active |
| ConsumedQuantity-C-000-C | Composite | ConsumedQuantity | USAGE_MEASUREMENT_SUPPORTED |  |  | AND of [Check ConsumedQuantity-C-001-M, Check ConsumedQuantity-C-002-M, Check ConsumedQuantity-C-003-C, Check ConsumedQuantity-C-008-C] |  | Static | 1.2 | Active |
| ConsumedQuantity-C-001-M | Type | ConsumedQuantity |  |  |  | TypeDecimal(ConsumedQuantity) |  | Static | 1.2 | Active |
| ConsumedQuantity-C-002-M | Format | ConsumedQuantity |  |  |  | FormatNumeric(ConsumedQuantity) |  | Static | 1.2 | Active |
| ConsumedQuantity-C-003-C | Composite | ConsumedQuantity |  |  |  | AND of [Check ConsumedQuantity-C-004-C, Check ConsumedQuantity-C-005-C] |  | Static | 1.2 | Active |
| ConsumedQuantity-C-004-C | Nullability | ConsumedQuantity |  |  |  | CheckValue(ConsumedQuantity, null) | OR of [CheckNotValue(ChargeCategory, Usage), AND of [CheckValue(ChargeCategory, Usage), CheckValue(CommitmentDiscountStatus, Unused)]] | Static | 1.2 | Active |
| ConsumedQuantity-C-005-C | Composite | ConsumedQuantity |  |  |  | AND of [Check ConsumedQuantity-C-006-C, Check ConsumedQuantity-C-007-C] | AND of [CheckValue(ChargeCategory, Usage), CheckNotValue(CommitmentDiscountStatus, Unused)] | Static | 1.2 | Active |
| ConsumedQuantity-C-006-C | Nullability | ConsumedQuantity |  |  |  | CheckNotValue(ConsumedQuantity, null) | CheckValue(ChargeClass, Correction) | Static | 1.2 | Active |
| ConsumedQuantity-C-007-C | Nullability | ConsumedQuantity |  |  |  | CheckValue(ConsumedQuantity, null) | CheckValue(ChargeClass, Correction) | Static | 1.2 | Active |
| ConsumedQuantity-C-008-C | Validation | ConsumedQuantity |  |  |  |  | CheckNotValue(ConsumedQuantity, null) | Dynamic | 1.2 | Active |
| ConsumedUnit-C-000-C | Composite | ConsumedUnit | USAGE_MEASUREMENT_SUPPORTED |  |  | AND of [Check ConsumedUnit-C-001-M, Check ConsumedUnit-C-002-M, Check ConsumedUnit-C-003-O, Check ConsumedUnit-C-004-C, Check ConsumedUnit-C-005-C] |  | Static | 1.2 | Active |
| ConsumedUnit-C-001-M | Type | ConsumedUnit |  |  |  | TypeString(ConsumedUnit) |  | Static | 1.2 | Active |
| ConsumedUnit-C-002-M | Format | ConsumedUnit |  |  |  | FormatString(ConsumedUnit) |  | Static | 1.2 | Active |
| ConsumedUnit-C-003-O | Format | ConsumedUnit |  |  |  | FormatUnit(ConsumedUnit) |  | Static | 1.2 | Active |
| ConsumedUnit-C-004-C | Nullability | ConsumedUnit |  |  |  | CheckValue(ConsumedUnit, null) | CheckValue(ConsumedQuantity, null) | Static | 1.2 | Active |
| ConsumedUnit-C-005-C | Nullability | ConsumedUnit |  |  |  | CheckNotValue(ConsumedUnit, null) | CheckNotValue(ConsumedQuantity, null) | Static | 1.2 | Active |
| ContractedCost-C-000-M | Composite | ContractedCost |  |  |  | AND of [Check ContractedCost-C-001-M, Check ContractedCost-C-002-M, Check ContractedCost-C-003-M, Check ContractedCost-C-004-M, Check ContractedCost-C-005-M, Check ContractedCost-C-006-C, Check ContractedCost-C-009-C, Check ContractedCost-C-010-C] |  | Static | 1.2 | Active |
| ContractedCost-C-001-M | Type | ContractedCost |  |  |  | TypeDecimal(ContractedCost) |  | Static | 1.2 | Active |
| ContractedCost-C-002-M | Format | ContractedCost |  |  |  | FormatNumeric(ContractedCost) |  | Static | 1.2 | Active |
| ContractedCost-C-003-M | Nullability | ContractedCost |  |  |  | CheckNotValue(ContractedCost, null) |  | Static | 1.2 | Active |
| ContractedCost-C-004-M | Validation | ContractedCost |  |  |  | CheckNotValue(ContractedCost, null) |  | Static | 1.2 | Active |
| ContractedCost-C-005-M | Validation | ContractedCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| ContractedCost-C-006-C | Composite | ContractedCost |  |  |  | AND of [Check ContractedCost-C-007-C, Check ContractedCost-C-008-C] | CheckValue(ContractedUnitPrice, null) | Static | 1.2 | Active |
| ContractedCost-C-007-C | Validation | ContractedCost |  |  |  |  | AND of [CheckValue(ContractedUnitPrice, null), CheckValue(ChargeCategory, Tax)] | Dynamic | 1.2 | Active |
| ContractedCost-C-008-C | Validation | ContractedCost |  |  |  |  | AND of [CheckValue(ContractedUnitPrice, null), CheckValue(ChargeCategory, Credit)] | Dynamic | 1.2 | Active |
| ContractedCost-C-009-C | Validation | ContractedCost |  |  |  |  | AND of [CheckNotValue(ContractedUnitPrice, null), CheckNotValue(PricingQuantity, null), CheckNotValue(ChargeClass, Correction)] | Dynamic | 1.2 | Active |
| ContractedCost-C-010-C | Validation | ContractedCost |  |  |  |  | CheckValue(ChargeClass, Correction) | Dynamic | 1.2 | Active |
| ContractedUnitPrice-C-000-C | Composite | ContractedUnitPrice | NEGOTIATED_PRICING_SUPPORTED |  |  | AND of [Check ContractedUnitPrice-C-001-M, Check ContractedUnitPrice-C-004-M, Check ContractedUnitPrice-C-008-C, Check ContractedUnitPrice-C-012-C] |  | Static | 1.2 | Active |
| ContractedUnitPrice-C-001-M | Composite | ContractedUnitPrice |  |  |  | AND of [Check ContractedUnitPrice-C-002-M, Check ContractedUnitPrice-C-003-M] |  | Static | 1.2 | Active |
| ContractedUnitPrice-C-002-M | Type | ContractedUnitPrice |  |  |  | TypeDecimal(ContractedUnitPrice) |  | Static | 1.2 | Active |
| ContractedUnitPrice-C-003-M | Format | ContractedUnitPrice |  |  |  | FormatNumeric(ContractedUnitPrice) |  | Static | 1.2 | Active |
| ContractedUnitPrice-C-004-M | Composite | ContractedUnitPrice |  |  |  | AND of [Check ContractedUnitPrice-C-005-C, Check ContractedUnitPrice-C-006-C, Check ContractedUnitPrice-C-007-O] |  | Static | 1.2 | Active |
| ContractedUnitPrice-C-005-C | Nullability | ContractedUnitPrice |  |  |  | CheckValue(ContractedUnitPrice, null) | CheckValue(ChargeCategory, Tax) | Static | 1.2 | Active |
| ContractedUnitPrice-C-006-C | Nullability | ContractedUnitPrice |  |  |  | CheckNotValue(ContractedUnitPrice, null) | AND of [OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)], CheckNotValue(ChargeClass, Correction)] | Static | 1.2 | Active |
| ContractedUnitPrice-C-007-O | Nullability | ContractedUnitPrice |  |  |  |  |  | Dynamic | 1.2 | Active |
| ContractedUnitPrice-C-008-C | Composite | ContractedUnitPrice |  |  |  | AND of [Check ContractedUnitPrice-C-009-C, Check ContractedUnitPrice-C-010-C, Check ContractedUnitPrice-C-011-C] | CheckNotValue(ContractedUnitPrice, null) | Static | 1.2 | Active |
| ContractedUnitPrice-C-009-C | Validation | ContractedUnitPrice |  |  |  | CheckGreaterOrEqualThanValue(ContractedUnitPrice, 0) | CheckNotValue(ContractedUnitPrice, null) | Static | 1.2 | Active |
| ContractedUnitPrice-C-010-C | Validation | ContractedUnitPrice |  |  |  |  | CheckNotValue(ContractedUnitPrice, null) | Dynamic | 1.2 | Active |
| ContractedUnitPrice-C-011-C | Validation | ContractedUnitPrice |  |  |  | ColumnByColumnEqualsColumnValue | AND of [CheckNotValue(ContractedUnitPrice, null), CheckNotValue(PricingQuantity, null), CheckNotValue(ChargeClass, Correction)] | Static | 1.2 | Active |
| ContractedUnitPrice-C-012-C | Validation | ContractedUnitPrice |  |  |  |  | CheckValue(ChargeClass, Correction) | Dynamic | 1.2 | Active |
| CostAndUsage-D-000-M | Composite | CostAndUsage |  |  |  | AND of [Check CostAndUsage-D-001-M, Check CostAndUsage-D-002-M] |  | Static | 1.2 | Active |
| CostAndUsage-D-001-M | Composite | CostAndUsage |  |  |  | AND of [Check CostAndUsage-D-003-C, Check CostAndUsage-D-004-C, Check CostAndUsage-D-005-M, Check CostAndUsage-D-006-M, Check CostAndUsage-D-007-M, Check CostAndUsage-D-008-M, Check CostAndUsage-D-009-M, Check CostAndUsage-D-010-M, Check CostAndUsage-D-011-C, Check CostAndUsage-D-012-C, Check CostAndUsage-D-013-C, Check CostAndUsage-D-014-C, Check CostAndUsage-D-015-C, Check CostAndUsage-D-016-C, Check CostAndUsage-D-017-C, Check CostAndUsage-D-018-C, Check CostAndUsage-D-019-C, Check CostAndUsage-D-020-C, Check CostAndUsage-D-021-M, Check CostAndUsage-D-022-C, Check CostAndUsage-D-023-M, Check CostAndUsage-D-024-M, Check CostAndUsage-D-025-M, Check CostAndUsage-D-026-M, Check CostAndUsage-D-027-O, Check CostAndUsage-D-028-M, Check CostAndUsage-D-029-C, Check CostAndUsage-D-030-M, Check CostAndUsage-D-031-M, Check CostAndUsage-D-032-M, Check CostAndUsage-D-033-O, Check CostAndUsage-D-034-C, Check CostAndUsage-D-035-M, Check CostAndUsage-D-036-M, Check CostAndUsage-D-037-M, Check CostAndUsage-D-038-M, Check CostAndUsage-D-039-C, Check CostAndUsage-D-040-M, Check CostAndUsage-D-041-M, Check CostAndUsage-D-042-O, Check CostAndUsage-D-043-C, Check CostAndUsage-D-044-C, Check CostAndUsage-D-045-C, Check CostAndUsage-D-046-C, Check CostAndUsage-D-049-C, Check CostAndUsage-D-052-C, Check CostAndUsage-D-055-C, Check CostAndUsage-D-056-C, Check CostAndUsage-D-057-C, Check CostAndUsage-D-058-C, Check CostAndUsage-D-059-C, Check CostAndUsage-D-060-C, Check CostAndUsage-D-061-C, Check CostAndUsage-D-062-C, Check CostAndUsage-D-063-C, Check CostAndUsage-D-064-C, Check CostAndUsage-D-065-M] |  | Static | 1.2 | Active |
| CostAndUsage-D-002-M | Composite | CostAndUsage |  |  |  | AND of [Check AvailabilityZone-C-000-C, Check BilledCost-C-000-M, Check BillingAccountId-C-000-M, Check BillingAccountName-C-000-M, Check BillingAccountType-C-000-M, Check BillingCurrency-C-000-M, Check BillingPeriodEnd-C-000-M, Check BillingPeriodStart-C-000-M, Check CapacityReservationId-C-000-C, Check CapacityReservationStatus-C-000-C, Check ChargeCategory-C-000-M, Check ChargeClass-C-000-M, Check ChargeFrequency-C-000-O, Check ChargeDescription-C-000-M, Check ChargePeriodEnd-C-000-M, Check ChargePeriodStart-C-000-M, Check CommitmentDiscountCategory-C-000-C, Check CommitmentDiscountId-C-000-C, Check CommitmentDiscountName-C-000-C, Check CommitmentDiscountStatus-C-000-C, Check CommitmentDiscountType-C-000-C, Check CommitmentDiscountUnit-C-000-C, Check CommitmentDiscountQuantity-C-000-C, Check ConsumedUnit-C-000-C, Check ConsumedQuantity-C-000-C, Check ContractedCost-C-000-M, Check ContractedUnitPrice-C-000-C, Check EffectiveCost-C-000-M, Check InvoiceId-C-000-O, Check InvoiceIssuerName-C-000-M, Check ListCost-C-000-M, Check ListUnitPrice-C-000-C, Check PricingCategory-C-000-M, Check PricingCurrency-C-000-C, Check PricingCurrencyContractedUnitPrice-C-000-C, Check PricingCurrencyEffectiveCost-C-000-C, Check PricingCurrencyListUnitPrice-C-000-C, Check PricingQuantity-C-000-M, Check PricingUnit-C-000-M, Check ProviderName-C-000-M, Check PublisherName-C-000-M, Check RegionId-C-000-C, Check RegionName-C-000-C, Check ResourceId-C-000-C, Check ResourceName-C-000-C, Check ResourceType-C-000-C, Check SubAccountId-C-000-C, Check SubAccountName-C-000-C, Check ServiceCategory-C-000-M, Check ServiceName-C-000-M, Check ServiceSubcategory-C-000-O, Check SkuId-C-000-C, Check SkuMeter-C-000-C, Check SkuPriceDetails-C-000-C, Check SkuPriceId-C-000-C, Check SubAccountType-C-000-C, Check Tags-C-000-C] |  | Static | 1.2 | Active |
| CostAndUsage-D-003-C | Presence | AvailabilityZone | AVAILABILITY_ZONE_SUPPORTED |  |  | ColumnPresent(AvailabilityZone) |  | Static | 1.2 | Active |
| CostAndUsage-D-004-C | Presence | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | ColumnPresent(ListUnitPrice) |  | Static | 1.2 | Active |
| CostAndUsage-D-005-M | Presence | BillingAccountName |  |  |  | ColumnPresent(BillingAccountName) |  | Static | 1.2 | Active |
| CostAndUsage-D-006-M | Presence | BilledCost |  |  |  | ColumnPresent(BilledCost) |  | Static | 1.2 | Active |
| CostAndUsage-D-007-M | Presence | BillingAccountType |  |  |  | ColumnPresent(BillingAccountType) |  | Static | 1.2 | Active |
| CostAndUsage-D-008-M | Presence | ChargeCategory |  |  |  | ColumnPresent(ChargeCategory) |  | Static | 1.2 | Active |
| CostAndUsage-D-009-M | Presence | BillingPeriodStart |  |  |  | ColumnPresent(BillingPeriodStart) |  | Static | 1.2 | Active |
| CostAndUsage-D-010-M | Presence | BillingPeriodEnd |  |  |  | ColumnPresent(BillingPeriodEnd) |  | Static | 1.2 | Active |
| CostAndUsage-D-011-C | Presence | ConsumedQuantity | USAGE_MEASUREMENT_SUPPORTED |  |  | ColumnPresent(ConsumedQuantity) |  | Static | 1.2 | Active |
| CostAndUsage-D-012-C | Presence | CommitmentDiscountName | COMMITMENT_DISCOUNT_SUPPORTED |  |  | ColumnPresent(CommitmentDiscountName) |  | Static | 1.2 | Active |
| CostAndUsage-D-013-C | Presence | CommitmentDiscountId | COMMITMENT_DISCOUNT_SUPPORTED |  |  | ColumnPresent(CommitmentDiscountId) |  | Static | 1.2 | Active |
| CostAndUsage-D-014-C | Presence | CommitmentDiscountType | COMMITMENT_DISCOUNT_SUPPORTED |  |  | ColumnPresent(CommitmentDiscountType) |  | Static | 1.2 | Active |
| CostAndUsage-D-015-C | Presence | CommitmentDiscountUnit | COMMITMENT_DISCOUNT_SUPPORTED |  |  | ColumnPresent(CommitmentDiscountUnit) |  | Static | 1.2 | Active |
| CostAndUsage-D-016-C | Presence | CommitmentDiscountCategory | COMMITMENT_DISCOUNT_SUPPORTED |  |  | ColumnPresent(CommitmentDiscountCategory) |  | Static | 1.2 | Active |
| CostAndUsage-D-017-C | Presence | CommitmentDiscountStatus | COMMITMENT_DISCOUNT_SUPPORTED |  |  | ColumnPresent(CommitmentDiscountStatus) |  | Static | 1.2 | Active |
| CostAndUsage-D-018-C | Presence | CommitmentDiscountQuantity | COMMITMENT_DISCOUNT_SUPPORTED |  |  | ColumnPresent(CommitmentDiscountQuantity) |  | Static | 1.2 | Active |
| CostAndUsage-D-019-C | Presence | SubAccountId | SUB_ACCOUNT_SUPPORTED |  |  | ColumnPresent(SubAccountId) |  | Static | 1.2 | Active |
| CostAndUsage-D-020-C | Presence | CapacityReservationStatus | CAPACITY_RESERVATION_SUPPORTED |  |  | ColumnPresent(CapacityReservationStatus) |  | Static | 1.2 | Active |
| CostAndUsage-D-021-M | Presence | PublisherName |  |  |  | ColumnPresent(PublisherName) |  | Static | 1.2 | Active |
| CostAndUsage-D-022-C | Presence | PricingCategory | MULTIPLE_PRICING_CATEGORIES_SUPPORTED |  |  | ColumnPresent(PricingCategory) |  | Static | 1.2 | Active |
| CostAndUsage-D-023-M | Presence | InvoiceIssuerName |  |  |  | ColumnPresent(PublisherName) |  | Static | 1.2 | Active |
| CostAndUsage-D-024-M | Presence | BillingAccountId |  |  |  | ColumnPresent(BillingAccountId) |  | Static | 1.2 | Active |
| CostAndUsage-D-025-M | Presence | ChargeDescription |  |  |  | ColumnPresent(ChargeDescription) |  | Static | 1.2 | Active |
| CostAndUsage-D-026-M | Presence | ChargeClass |  |  |  | ColumnPresent(ChargeClass) |  | Static | 1.2 | Active |
| CostAndUsage-D-027-O | Presence | ChargeFrequency |  |  |  | ColumnPresent(ChargeFrequency) |  | Static | 1.2 | Active |
| CostAndUsage-D-028-M | Presence | ChargePeriodEnd |  |  |  | ColumnPresent(ChargePeriodEnd) |  | Static | 1.2 | Active |
| CostAndUsage-D-029-C | Presence | SubAccountName | SUB_ACCOUNT_SUPPORTED |  |  | ColumnPresent(SubAccountName) |  | Static | 1.2 | Active |
| CostAndUsage-D-030-M | Presence | ContractedCost |  |  |  | ColumnPresent(ContractedCost) |  | Static | 1.2 | Active |
| CostAndUsage-D-031-M | Presence | EffectiveCost |  |  |  | ColumnPresent(EffectiveCost) |  | Static | 1.2 | Active |
| CostAndUsage-D-032-M | Presence | ListCost |  |  |  | ColumnPresent(ListCost) |  | Static | 1.2 | Active |
| CostAndUsage-D-033-O | Presence | InvoiceId |  |  |  | ColumnPresent(InvoiceId) |  | Static | 1.2 | Active |
| CostAndUsage-D-034-C | Presence | ContractedUnitPrice | NEGOTIATED_PRICING_SUPPORTED |  |  | ColumnPresent(ContractedUnitPrice) |  | Static | 1.2 | Active |
| CostAndUsage-D-035-M | Presence | BillingCurrency |  |  |  | ColumnPresent(BillingCurrency) |  | Static | 1.2 | Active |
| CostAndUsage-D-036-M | Presence | PricingQuantity |  |  |  | ColumnPresent(PricingQuantity) |  | Static | 1.2 | Active |
| CostAndUsage-D-037-M | Presence | ChargePeriodStart |  |  |  | ColumnPresent(ChargePeriodStart) |  | Static | 1.2 | Active |
| CostAndUsage-D-038-M | Presence | ProviderName |  |  |  | ColumnPresent(ProviderName) |  | Static | 1.2 | Active |
| CostAndUsage-D-039-C | Presence | ResourceType | BILLING_BASED_ON_PROVISIONED_RESOURCES_SUPPORTED, RESOURCE_TYPE_ASSIGNMENT_SUPPORTED |  |  | ColumnPresent(ResourceType) |  | Static | 1.2 | Active |
| CostAndUsage-D-040-M | Presence | ServiceCategory |  |  |  | ColumnPresent(ServiceCategory) |  | Static | 1.2 | Active |
| CostAndUsage-D-041-M | Presence | ServiceName |  |  |  | ColumnPresent(ServiceName) |  | Static | 1.2 | Active |
| CostAndUsage-D-042-O | Presence | ServiceSubcategory |  |  |  | ColumnPresent(ServiceSubcategory) |  | Static | 1.2 | Active |
| CostAndUsage-D-043-C | Presence | ResourceId | BILLING_BASED_ON_PROVISIONED_RESOURCES_SUPPORTED, RESOURCE_TYPE_ASSIGNMENT_SUPPORTED |  |  | ColumnPresent(ResourceId) |  | Static | 1.2 | Active |
| CostAndUsage-D-044-C | Presence | ResourceName | BILLING_BASED_ON_PROVISIONED_RESOURCES_SUPPORTED, RESOURCE_TYPE_ASSIGNMENT_SUPPORTED |  |  | ColumnPresent(ResourceName) |  | Static | 1.2 | Active |
| CostAndUsage-D-045-C | Presence | PricingCurrency | PRICING_BILLING_CURRENCY_DIFFERENCES_SUPPORTED |  |  | ColumnPresent(PricingCurrency) |  | Static | 1.2 | Active |
| CostAndUsage-D-046-C | Composite | PricingCurrencyContractedUnitPrice |  |  |  | AND of [Check CostAndUsage-D-047-C, Check CostAndUsage-D-048-C] |  | Static | 1.2 | Active |
| CostAndUsage-D-047-C | Presence | PricingCurrencyContractedUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED, VIRTUAL_CURRENCY_SUPPORTED |  |  | ColumnPresent(PricingCurrencyContractedUnitPrice) |  | Static | 1.2 | Active |
| CostAndUsage-D-048-C | Presence | PricingCurrencyContractedUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED, PRICING_BILLING_CURRENCY_DIFFERENCES_SUPPORTED |  |  | ColumnPresent(PricingCurrencyContractedUnitPrice) |  | Static | 1.2 | Active |
| CostAndUsage-D-049-C | Composite | PricingCurrencyEffectiveCost |  |  |  | AND of [Check CostAndUsage-D-050-C, Check CostAndUsage-D-051-C] |  | Static | 1.2 | Active |
| CostAndUsage-D-050-C | Presence | PricingCurrencyEffectiveCost | PUBLIC_PRICE_LIST_SUPPORTED, VIRTUAL_CURRENCY_SUPPORTED |  |  | ColumnPresent(PricingCurrencyEffectiveCost) |  | Static | 1.2 | Active |
| CostAndUsage-D-051-C | Presence | PricingCurrencyEffectiveCost | PUBLIC_PRICE_LIST_SUPPORTED, PRICING_BILLING_CURRENCY_DIFFERENCES_SUPPORTED |  |  | ColumnPresent(PricingCurrencyEffectiveCost) |  | Static | 1.2 | Active |
| CostAndUsage-D-052-C | Composite | PricingCurrencyListUnitPrice |  |  |  | AND of [Check CostAndUsage-D-053-C, Check CostAndUsage-D-054-C] |  | Static | 1.2 | Active |
| CostAndUsage-D-053-C | Presence | PricingCurrencyListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED, VIRTUAL_CURRENCY_SUPPORTED |  |  | ColumnPresent(PricingCurrencyListUnitPrice) |  | Static | 1.2 | Active |
| CostAndUsage-D-054-C | Presence | PricingCurrencyListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED, PRICING_BILLING_CURRENCY_DIFFERENCES_SUPPORTED |  |  | ColumnPresent(PricingCurrencyListUnitPrice) |  | Static | 1.2 | Active |
| CostAndUsage-D-055-C | Presence | SkuPriceId | PUBLIC_PRICE_LIST_SUPPORTED, UNIT_PRICING_SUPPORTED |  |  | ColumnPresent(SkuPriceId) |  | Static | 1.2 | Active |
| CostAndUsage-D-056-C | Presence | SkuMeter | PUBLIC_PRICE_LIST_SUPPORTED, UNIT_PRICING_SUPPORTED |  |  | ColumnPresent(SkuMeter) |  | Static | 1.2 | Active |
| CostAndUsage-D-057-C | Presence | SkuId | PUBLIC_PRICE_LIST_SUPPORTED, UNIT_PRICING_SUPPORTED |  |  | ColumnPresent(SkuId) |  | Static | 1.2 | Active |
| CostAndUsage-D-058-C | Presence | SkuPriceDetails | PUBLIC_PRICE_LIST_SUPPORTED, UNIT_PRICING_SUPPORTED |  |  | ColumnPresent(SkuPriceDetails) |  | Static | 1.2 | Active |
| CostAndUsage-D-059-C | Presence | RegionName | REGION_SUPPORTED |  |  | ColumnPresent(RegionName) |  | Static | 1.2 | Active |
| CostAndUsage-D-060-C | Presence | RegionId | REGION_SUPPORTED |  |  | ColumnPresent(RegionId) |  | Static | 1.2 | Active |
| CostAndUsage-D-061-C | Presence | Tags | TAGGING_SUPPORTED |  |  | ColumnPresent(Tags) |  | Static | 1.2 | Active |
| CostAndUsage-D-062-C | Presence | CapacityReservationId | CAPACITY_RESERVATION_SUPPORTED |  |  | ColumnPresent(CapacityReservationId) |  | Static | 1.2 | Active |
| CostAndUsage-D-063-C | Presence | ConsumedUnit | USAGE_MEASUREMENT_SUPPORTED |  |  | ColumnPresent(ConsumedUnit) |  | Static | 1.2 | Active |
| CostAndUsage-D-064-C | Presence | SubAccountType | USAGE_MEASUREMENT_SUPPORTED |  |  | ColumnPresent(SubAccountType) |  | Static | 1.2 | Active |
| CostAndUsage-D-065-M | Presence | PricingUnit |  |  |  | ColumnPresent(PricingUnit) |  | Static | 1.2 | Active |
| EffectiveCost-C-000-M | Composite | EffectiveCost |  |  |  | AND of [Check EffectiveCost-C-001-M, Check EffectiveCost-C-002-M, Check EffectiveCost-C-003-M, Check EffectiveCost-C-004-M, Check EffectiveCost-C-005-C, Check EffectiveCost-C-006-M, Check EffectiveCost-C-007-O, Check EffectiveCost-C-008-C, Check EffectiveCost-C-011-C] |  | Static | 1.2 | Active |
| EffectiveCost-C-001-M | Type | EffectiveCost |  |  |  | TypeDecimal(EffectiveCost) |  | Static | 1.2 | Active |
| EffectiveCost-C-002-M | Format | EffectiveCost |  |  |  | FormatNumeric(EffectiveCost) |  | Static | 1.2 | Active |
| EffectiveCost-C-003-M | Nullability | EffectiveCost |  |  |  | CheckNotValue(EffectiveCost, null) |  | Static | 1.2 | Active |
| EffectiveCost-C-004-M | Validation | EffectiveCost |  |  |  | CheckNotValue(ConsumedQuantity, null) |  | Static | 1.2 | Active |
| EffectiveCost-C-005-C | Validation | EffectiveCost |  |  |  | CheckValue(EffectiveCost, 0) | CheckValue(ChargeCategory, Purchase) | Static | 1.2 | Active |
| EffectiveCost-C-006-M | Validation | EffectiveCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| EffectiveCost-C-007-O | Validation | EffectiveCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| EffectiveCost-C-008-C | Composite | EffectiveCost |  |  |  | AND of [Check EffectiveCost-C-009-C, Check EffectiveCost-C-010-C] | AND of [CheckNotValue(ChargeCategory, Usage), CheckNotValue(ChargeCategory, Purchase)] | Static | 1.2 | Active |
| EffectiveCost-C-009-C | Validation | EffectiveCost |  |  |  |  | CheckValue(ChargeCategory, Tax) | Dynamic | 1.2 | Active |
| EffectiveCost-C-010-C | Validation | EffectiveCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| EffectiveCost-C-011-C | Composite | EffectiveCost |  |  |  | AND of [Check EffectiveCost-C-012-C, Check EffectiveCost-C-013-C] | CheckNotValue(CommitmentDiscountId, null) | Static | 1.2 | Active |
| EffectiveCost-C-012-C | Validation | EffectiveCost |  |  |  |  | AND of [CheckValue(ChargeCategory, Usage), CheckNotValue(CommitmentDiscountId, null)] | Dynamic | 1.2 | Active |
| EffectiveCost-C-013-C | Validation | EffectiveCost |  |  |  |  | AND of [CheckValue(ChargeCategory, Usage), CheckNotValue(CommitmentDiscountId, null)] | Dynamic | 1.2 | Active |
| InvoiceId-C-000-O | Composite | InvoiceId |  |  |  | AND of [Check InvoiceId-C-001-M, Check InvoiceId-C-002-M, Check InvoiceId-C-003-C, Check InvoiceId-C-006-O, Check InvoiceId-C-007-C] |  | Static | 1.2 | Active |
| InvoiceId-C-001-M | Type | InvoiceId |  |  |  | TypeString(InvoiceId) |  | Static | 1.2 | Active |
| InvoiceId-C-002-M | Format | InvoiceId |  |  |  | FormatString(InvoiceId) |  | Static | 1.2 | Active |
| InvoiceId-C-003-C | Composite | InvoiceId |  |  |  | OR of [Check InvoiceId-C-004-C, Check InvoiceId-C-005-C] |  | Static | 1.2 | Active |
| InvoiceId-C-006-O | Validation | InvoiceId |  |  |  |  |  | Dynamic | 1.2 | Active |
| InvoiceId-C-007-C | Validation | InvoiceId |  |  |  |  |  | Dynamic | 1.2 | Active |
| InvoiceIssuerName-C-000-M | Composite | InvoiceIssuerName |  |  |  | AND of [Check InvoiceIssuerName-C-001-M, Check InvoiceIssuerName-C-002-M, Check InvoiceIssuerName-C-003-M] |  | Static | 1.2 | Active |
| InvoiceIssuerName-C-001-M | Type | InvoiceIssuerName |  |  |  | TypeString(InvoiceIssuerName) |  | Static | 1.2 | Active |
| InvoiceIssuerName-C-002-M | Format | InvoiceIssuerName |  |  |  | FormatString(InvoiceIssuerName) |  | Static | 1.2 | Active |
| InvoiceIssuerName-C-003-M | Nullability | InvoiceIssuerName |  |  |  | CheckNotValue(InvoiceIssuerName, null) |  | Static | 1.2 | Active |
| ListCost-C-000-M | Composite | ListCost |  |  |  | AND of [Check ListCost-C-001-M, Check ListCost-C-002-M, Check ListCost-C-003-M, Check ListCost-C-004-M, Check ListCost-C-005-M, Check ListCost-C-006-C, Check ListCost-C-009-C, Check ListCost-C-010-C] |  | Static | 1.2 | Active |
| ListCost-C-001-M | Type | ListCost |  |  |  | TypeDecimal(ListCost) |  | Static | 1.2 | Active |
| ListCost-C-002-M | Format | ListCost |  |  |  | FormatNumeric(ListCost) |  | Static | 1.2 | Active |
| ListCost-C-003-M | Nullability | ListCost |  |  |  | CheckNotValue(ListCost, null) |  | Static | 1.2 | Active |
| ListCost-C-004-M | Validation | ListCost |  |  |  | CheckNotValue(ListCost, null) |  | Static | 1.2 | Active |
| ListCost-C-005-M | Validation | ListCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| ListCost-C-006-C | Composite | ListCost |  |  |  | AND of [Check ListCost-C-007-C, Check ListCost-C-008-C] | CheckValue(ListUnitPrice, null) | Static | 1.2 | Active |
| ListCost-C-007-C | Validation | ListCost |  |  |  |  | AND of [CheckValue(ListUnitPrice, null), CheckValue(ChargeCategory, Tax)] | Dynamic | 1.2 | Active |
| ListCost-C-008-C | Validation | ListCost |  |  |  |  | AND of [CheckValue(ListUnitPrice, null), CheckValue(ChargeCategory, Credit)] | Dynamic | 1.2 | Active |
| ListCost-C-009-C | Validation | ListCost |  |  |  | ColumnByColumnEqualsColumnValue(ListUnitPrice, PricingQuantity) | AND of [CheckNotValue(ListUnitPrice, null), CheckNotValue(PricingQuantity, null), CheckNotValue(ChargeClass, Correction)] | Static | 1.2 | Active |
| ListCost-C-010-C | Validation | ListCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| ListUnitPrice-C-000-C | Composite | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | AND of [Check ListUnitPrice-C-001-M, Check ListUnitPrice-C-002-M, Check ListUnitPrice-C-003-M, Check ListUnitPrice-C-007-C] |  | Static | 1.2 | Active |
| ListUnitPrice-C-001-M | Type | ListUnitPrice |  |  |  | TypeDecimal(ListUnitPrice) |  | Static | 1.2 | Active |
| ListUnitPrice-C-002-M | Format | ListUnitPrice |  |  |  | FormatNumeric(ListUnitPrice) |  | Static | 1.2 | Active |
| ListUnitPrice-C-003-M | Composite | ListUnitPrice |  |  |  | AND of [Check ListUnitPrice-C-004-C, Check ListUnitPrice-C-005-C, Check ListUnitPrice-C-006-O] |  | Static | 1.2 | Active |
| ListUnitPrice-C-004-C | Nullability | ListUnitPrice |  |  |  | CheckValue(ListUnitPrice, null) | CheckValue(ChargeCategory, Tax) | Static | 1.2 | Active |
| ListUnitPrice-C-005-C | Nullability | ListUnitPrice |  |  |  | CheckNotValue(ListUnitPrice, null) | AND of [CheckNotValue(ChargeClass, Correction), OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)]] | Static | 1.2 | Active |
| ListUnitPrice-C-006-O | Nullability | ListUnitPrice |  |  |  | CheckValue(ListUnitPrice, null) |  | Static | 1.2 | Active |
| ListUnitPrice-C-007-C | Composite | ListUnitPrice |  |  |  | AND of [Check ListUnitPrice-C-008-M, Check ListUnitPrice-C-009-M, Check ListUnitPrice-C-010-C, Check ListUnitPrice-C-011-C] | CheckNotValue(ListUnitPrice, null) | Static | 1.2 | Active |
| ListUnitPrice-C-008-M | Validation | ListUnitPrice |  |  |  | CheckGreaterOrEqualThanValue(ListUnitPrice, 0) |  | Static | 1.2 | Active |
| ListUnitPrice-C-009-M | Validation | ListUnitPrice |  |  |  |  |  | Dynamic | 1.2 | Active |
| ListUnitPrice-C-010-C | Format | ListUnitPrice |  |  |  | ColumnByColumnEqualsColumnValue(ListUnitPrice, PricingQuantity) -> ListCost | AND of [CheckNotValue(ListUnitPrice, null), CheckNotValue(ChargeClass, Correction)] | Static | 1.2 | Active |
| ListUnitPrice-C-011-C | Validation | ListUnitPrice |  |  |  |  | CheckValue(ChargeClass, Correction) | Dynamic | 1.2 | Active |
| PricingCategory-C-000-M | Composite | PricingCategory |  |  |  | AND of [Check PricingCategory-C-001-M, Check PricingCategory-C-002-M, Check PricingCategory-C-006-C] |  | Static | 1.2 | Active |
| PricingCategory-C-001-M | Type | PricingCategory |  |  |  | TypeString(PricingCategory) |  | Static | 1.2 | Active |
| PricingCategory-C-002-M | Composite | PricingCategory |  |  |  | AND of [Check PricingCategory-C-003-C, Check PricingCategory-C-004-C, Check PricingCategory-C-005-O] |  | Static | 1.2 | Active |
| PricingCategory-C-003-C | Nullability | PricingCategory |  |  |  | CheckValue(PricingCategory, null) | CheckValue(ChargeCategory, Tax) | Static | 1.2 | Active |
| PricingCategory-C-004-C | Nullability | PricingCategory |  |  |  | CheckNotValue(PricingCategory, null) | AND of [OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)], CheckNotValue(ChargeClass, Correction)] | Static | 1.2 | Active |
| PricingCategory-C-005-O | Nullability | PricingCategory |  |  |  |  |  | Dynamic | 1.2 | Active |
| PricingCategory-C-006-C | Composite | PricingCategory |  |  |  | AND of [Check PricingCategory-C-007-M, Check PricingCategory-C-008-C, Check PricingCategory-C-009-C, Check PricingCategory-C-010-C, Check PricingCategory-C-011-C] | CheckNotValue(PricingCategory, null) | Static | 1.2 | Active |
| PricingCategory-C-007-M | Validation | PricingCategory |  |  |  | OR of [CheckValue(PricingCategory, Standard), CheckValue(PricingCategory, Committed), CheckValue(PricingCategory, Dynamic), CheckValue(PricingCategory, Other)] |  | Static | 1.2 | Active |
| PricingCategory-C-008-C | Validation | PricingCategory |  |  |  |  | CheckNotValue(PricingCategory, null) | Dynamic | 1.2 | Active |
| PricingCategory-C-009-C | Validation | PricingCategory |  |  |  |  |  | Dynamic | 1.2 | Active |
| PricingCategory-C-010-C | Validation | PricingCategory |  |  |  |  |  | Dynamic | 1.2 | Active |
| PricingCategory-C-011-C | Validation | PricingCategory |  |  |  |  |  | Dynamic | 1.2 | Active |
| PricingCurrency-C-000-C | Composite | PricingCurrency | PRICING_BILLING_CURRENCY_DIFFERENCES_SUPPORTED |  |  | AND of [Check PricingCurrency-C-001-M, Check PricingCurrency-C-002-M, Check PricingCurrency-C-003-M, Check PricingCurrency-C-004-M] |  | Static | 1.2 | Active |
| PricingCurrency-C-001-M | Type | PricingCurrency |  |  |  | TypeString(PricingCurrency) |  | Static | 1.2 | Active |
| PricingCurrency-C-002-M | Format | PricingCurrency |  |  |  | FormatString(PricingCurrency) |  | Static | 1.2 | Active |
| PricingCurrency-C-003-M | Format | PricingCurrency |  |  |  | CheckNationalCurrency(PricingCurrency) |  | Static | 1.2 | Active |
| PricingCurrency-C-004-M | Nullability | PricingCurrency |  |  |  | CheckNotValue(PricingCurrency, null) |  | Static | 1.2 | Active |
| PricingCurrencyContractedUnitPrice-C-000-C | Composite | PricingCurrencyContractedUnitPrice | PRICING_BILLING_CURRENCY_DIFFERENCES_SUPPORTED |  |  | AND of [Check PricingCurrencyContractedUnitPrice-C-001-M, Check PricingCurrencyContractedUnitPrice-C-002-M, Check PricingCurrencyContractedUnitPrice-C-003-M, Check PricingCurrencyContractedUnitPrice-C-007-C] |  | Static | 1.2 | Active |
| PricingCurrencyContractedUnitPrice-C-001-M | Type | PricingCurrencyContractedUnitPrice |  |  |  | TypeDecimal(PricingCurrencyContractedUnitPrice) |  | Static | 1.2 | Active |
| PricingCurrencyContractedUnitPrice-C-002-M | Format | PricingCurrencyContractedUnitPrice |  |  |  | FormatNumeric(PricingCurrencyContractedUnitPrice) |  | Static | 1.2 | Active |
| PricingCurrencyContractedUnitPrice-C-003-M | Composite | PricingCurrencyContractedUnitPrice |  |  |  | AND of [Check PricingCurrencyContractedUnitPrice-C-004-C, Check PricingCurrencyContractedUnitPrice-C-005-C, Check PricingCurrencyContractedUnitPrice-C-006-O] |  | Static | 1.2 | Active |
| PricingCurrencyContractedUnitPrice-C-004-C | Nullability | PricingCurrencyContractedUnitPrice |  |  |  |  | CheckValue(ChargeCategory, Tax) | Dynamic | 1.2 | Active |
| PricingCurrencyContractedUnitPrice-C-005-C | Nullability | PricingCurrencyContractedUnitPrice |  |  |  |  | AND of [OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)], CheckNotValue(ChargeClass, Correction)] | Dynamic | 1.2 | Active |
| PricingCurrencyContractedUnitPrice-C-006-O | Nullability | PricingCurrencyContractedUnitPrice |  |  |  |  |  | Dynamic | 1.2 | Active |
| PricingCurrencyContractedUnitPrice-C-007-C | Composite | PricingCurrencyContractedUnitPrice |  |  |  | AND of [Check PricingCurrencyContractedUnitPrice-C-008-C, Check PricingCurrencyContractedUnitPrice-C-009-C, Check PricingCurrencyContractedUnitPrice-C-010-C] | CheckNotValue(PricingCurrencyContractedUnitPrice, null) | Static | 1.2 | Active |
| PricingCurrencyContractedUnitPrice-C-008-C | Validation | PricingCurrencyContractedUnitPrice |  |  |  |  | CheckNotValue(PricingCurrencyContractedUnitPrice, null) | Dynamic | 1.2 | Active |
| PricingCurrencyContractedUnitPrice-C-009-C | Validation | PricingCurrencyContractedUnitPrice |  |  |  |  | CheckNotValue(PricingCurrencyContractedUnitPrice, null) | Dynamic | 1.2 | Active |
| PricingCurrencyContractedUnitPrice-C-010-C | Validation | PricingCurrencyContractedUnitPrice |  |  |  |  | CheckValue(ChargeClass, Correction) | Dynamic | 1.2 | Active |
| PricingCurrencyEffectiveCost-C-000-C | Composite | PricingCurrencyEffectiveCost | PRICING_BILLING_CURRENCY_DIFFERENCES_SUPPORTED |  |  | AND of [Check PricingCurrencyEffectiveCost-C-001-M, Check PricingCurrencyEffectiveCost-C-002-M, Check PricingCurrencyEffectiveCost-C-003-M, Check PricingCurrencyEffectiveCost-C-004-M, Check PricingCurrencyEffectiveCost-C-005-M, Check PricingCurrencyEffectiveCost-C-006-M] |  | Static | 1.2 | Active |
| PricingCurrencyEffectiveCost-C-001-M | Type | PricingCurrencyEffectiveCost |  |  |  | TypeDecimal(PricingCurrencyEffectiveCost) |  | Static | 1.2 | Active |
| PricingCurrencyEffectiveCost-C-002-M | Format | PricingCurrencyEffectiveCost |  |  |  | FormatNumeric(PricingCurrencyEffectiveCost) |  | Static | 1.2 | Active |
| PricingCurrencyEffectiveCost-C-003-M | Nullability | PricingCurrencyEffectiveCost |  |  |  | CheckNotValue(PricingCurrencyEffectiveCost, null) |  | Static | 1.2 | Active |
| PricingCurrencyEffectiveCost-C-004-M | Validation | PricingCurrencyEffectiveCost |  |  |  | CheckGreaterOrEqualThanValue(PricingCurrencyListUnitPrice, 0) |  | Static | 1.2 | Active |
| PricingCurrencyEffectiveCost-C-005-M | Validation | PricingCurrencyEffectiveCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| PricingCurrencyEffectiveCost-C-006-M | Validation | PricingCurrencyEffectiveCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| PricingCurrencyListUnitPrice-C-000-C | Composite | PricingCurrencyListUnitPrice | PRICING_BILLING_CURRENCY_DIFFERENCES_SUPPORTED |  |  | AND of [Check PricingCurrencyListUnitPrice-C-001-M, Check PricingCurrencyListUnitPrice-C-002-M, Check PricingCurrencyListUnitPrice-C-003-M, Check PricingCurrencyListUnitPrice-C-007-C] |  | Static | 1.2 | Active |
| PricingCurrencyListUnitPrice-C-001-M | Type | PricingCurrencyListUnitPrice |  |  |  | TypeDecimal(PricingCurrencyListUnitPrice) |  | Static | 1.2 | Active |
| PricingCurrencyListUnitPrice-C-002-M | Format | PricingCurrencyListUnitPrice |  |  |  | FormatNumeric(PricingCurrencyListUnitPrice) |  | Static | 1.2 | Active |
| PricingCurrencyListUnitPrice-C-003-M | Composite | PricingCurrencyListUnitPrice |  |  |  | AND of [Check PricingCurrencyListUnitPrice-C-004-C, Check PricingCurrencyListUnitPrice-C-005-C, Check PricingCurrencyListUnitPrice-C-006-O] |  | Static | 1.2 | Active |
| PricingCurrencyListUnitPrice-C-004-C | Nullability | PricingCurrencyListUnitPrice |  |  |  | CheckValue(PricingCurrencyListUnitPrice, null) | CheckValue(ChargeCategory, Tax) | Static | 1.2 | Active |
| PricingCurrencyListUnitPrice-C-005-C | Nullability | PricingCurrencyListUnitPrice |  |  |  | CheckNotValue(PricingCurrencyListUnitPrice, null) | AND of [OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)], CheckNotValue(ChargeClass, Correction)] | Static | 1.2 | Active |
| PricingCurrencyListUnitPrice-C-006-O | Nullability | PricingCurrencyListUnitPrice |  |  |  |  |  | Dynamic | 1.2 | Active |
| PricingCurrencyListUnitPrice-C-007-C | Composite | PricingCurrencyListUnitPrice |  |  |  | AND of [Check PricingCurrencyListUnitPrice-C-008-M, Check PricingCurrencyListUnitPrice-C-009-M, Check PricingCurrencyListUnitPrice-C-010-C] | CheckNotValue(PricingCurrencyListUnitPrice, null) | Static | 1.2 | Active |
| PricingCurrencyListUnitPrice-C-008-M | Validation | PricingCurrencyListUnitPrice |  |  |  | CheckGreaterOrEqualThanValue(PricingCurrencyListUnitPrice, 0) |  | Static | 1.2 | Active |
| PricingCurrencyListUnitPrice-C-009-M | Validation | PricingCurrencyListUnitPrice |  |  |  |  |  | Dynamic | 1.2 | Active |
| PricingCurrencyListUnitPrice-C-010-C | Validation | PricingCurrencyListUnitPrice |  |  |  |  | CheckValue(ChargeClass, Correction) | Dynamic | 1.2 | Active |
| PricingQuantity-C-000-M | Composite | PricingQuantity |  |  |  | AND of [Check PricingQuantity-C-001-M, Check PricingQuantity-C-002-M, Check PricingQuantity-C-003-M, Check PricingQuantity-C-007-C] |  | Static | 1.2 | Active |
| PricingQuantity-C-001-M | Type | PricingQuantity |  |  |  | TypeDecimal(PricingQuantity) |  | Static | 1.2 | Active |
| PricingQuantity-C-002-M | Format | PricingQuantity |  |  |  | FormatNumeric(PricingQuantity) |  | Static | 1.2 | Active |
| PricingQuantity-C-003-M | Composite | PricingQuantity |  |  |  | AND of [Check PricingQuantity-C-004-C, Check PricingQuantity-C-005-C, Check PricingQuantity-C-006-O] |  | Static | 1.2 | Active |
| PricingQuantity-C-004-C | Nullability | PricingQuantity |  |  |  | CheckValue(PricingQuantity, null) | CheckValue(ChargeCategory, Tax) | Static | 1.2 | Active |
| PricingQuantity-C-005-C | Nullability | PricingQuantity |  |  |  | CheckNotValue(PricingQuantity, null) | AND of [OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)], CheckNotValue(ChargeClass, Correction)] | Static | 1.2 | Active |
| PricingQuantity-C-006-O | Nullability | PricingQuantity |  |  |  |  |  | Dynamic | 1.2 | Active |
| PricingQuantity-C-007-C | Composite | PricingQuantity |  |  |  | AND of [Check PricingQuantity-C-008-M, Check PricingQuantity-C-009-C, Check PricingQuantity-C-010-C] | CheckNotValue(PricingQuantity, null) | Static | 1.2 | Active |
| PricingQuantity-C-008-M | Validation | PricingQuantity |  |  |  | CheckNotValue(PricingQuantity, null) |  | Static | 1.2 | Active |
| PricingQuantity-C-009-C | Validation | PricingQuantity |  |  |  |  | AND of [CheckNotValue(ContractedUnitPrice, null), CheckNotValue(ChargeClass, Correction)] | Dynamic | 1.2 | Active |
| PricingQuantity-C-010-C | Validation | PricingQuantity |  |  |  |  | CheckValue(ChargeClass, Correction) | Dynamic | 1.2 | Active |
| PricingUnit-C-000-M | Composite | PricingUnit |  |  |  | AND of [Check PricingUnit-C-001-M, Check PricingUnit-C-002-M, Check PricingUnit-C-003-O, Check PricingUnit-C-004-C, Check PricingUnit-C-007-C] |  | Static | 1.2 | Active |
| PricingUnit-C-001-M | Type | PricingUnit |  |  |  | TypeString(PricingUnit) |  | Static | 1.2 | Active |
| PricingUnit-C-002-M | Format | PricingUnit |  |  |  | FormatString(PricingUnit) |  | Static | 1.2 | Active |
| PricingUnit-C-003-O | Format | PricingUnit |  |  |  | FormatUnit(PricingUnit) |  | Static | 1.2 | Active |
| PricingUnit-C-004-C | Composite | PricingUnit |  |  |  | AND of [Check PricingUnit-C-005-C, Check PricingUnit-C-006-C] |  | Static | 1.2 | Active |
| PricingUnit-C-005-C | Nullability | PricingUnit |  |  |  | CheckValue(PricingUnit, null) | CheckValue(PricingQuantity, null) | Static | 1.2 | Active |
| PricingUnit-C-006-C | Nullability | PricingUnit |  |  |  | CheckNotValue(PricingUnit, null) | CheckNotValue(PricingQuantity, null) | Static | 1.2 | Active |
| PricingUnit-C-007-C | Composite | PricingUnit |  |  |  | AND of [Check PricingUnit-C-008-M, Check PricingUnit-C-009-C] | CheckNotValue(PricingUnit, null) | Static | 1.2 | Active |
| PricingUnit-C-008-M | Validation | PricingUnit |  |  |  |  |  | Dynamic | 1.2 | Active |
| PricingUnit-C-009-C | Validation | PricingUnit |  |  |  |  |  | Dynamic | 1.2 | Active |
| ProviderName-C-000-M | Composite | ProviderName |  |  |  | AND of [Check ProviderName-C-001-M, Check ProviderName-C-002-M, Check ProviderName-C-003-M] |  | Static | 1.2 | Active |
| ProviderName-C-001-M | Type | ProviderName |  |  |  | TypeString(ProviderName) |  | Static | 1.2 | Active |
| ProviderName-C-002-M | Format | ProviderName |  |  |  | FormatString(ProviderName) |  | Static | 1.2 | Active |
| ProviderName-C-003-M | Nullability | ProviderName |  |  |  | CheckNotValue(ProviderName, null) |  | Static | 1.2 | Active |
| PublisherName-C-000-M | Composite | PublisherName |  |  |  | AND of [Check PublisherName-C-001-M, Check PublisherName-C-002-M, Check PublisherName-C-003-M] |  | Static | 1.2 | Active |
| PublisherName-C-001-M | Type | PublisherName |  |  |  | TypeString(PublisherName) |  | Static | 1.2 | Active |
| PublisherName-C-002-M | Format | PublisherName |  |  |  | FormatString(PublisherName) |  | Static | 1.2 | Active |
| PublisherName-C-003-M | Nullability | PublisherName |  |  |  | CheckNotValue(PublisherName, null) |  | Static | 1.2 | Active |
| RegionId-C-000-C | Composite | RegionId | REGION_SUPPORTED |  |  | AND of [Check RegionId-C-001-M, Check RegionId-C-002-M, Check RegionId-C-003-C] |  | Static | 1.2 | Active |
| RegionId-C-001-M | Type | RegionId |  |  |  | TypeString(RegionId) |  | Static | 1.2 | Active |
| RegionId-C-002-M | Format | RegionId |  |  |  | FormatString(RegionId) |  | Static | 1.2 | Active |
| RegionId-C-003-C | Nullability | RegionId |  |  |  | CheckValue(RegionId, null) |  | Static | 1.2 | Active |
| RegionName-C-000-C | Composite | RegionName | REGION_SUPPORTED |  |  | AND of [Check RegionName-C-001-M, Check RegionName-C-002-M, Check RegionName-C-003-C] |  | Static | 1.2 | Active |
| RegionName-C-001-M | Type | RegionName |  |  |  | TypeString(RegionName) |  | Static | 1.2 | Active |
| RegionName-C-002-M | Format | RegionName |  |  |  | FormatString(RegionName) |  | Static | 1.2 | Active |
| RegionName-C-003-C | Nullability | RegionName |  |  |  | CheckValue(RegionName, null) |  | Static | 1.2 | Active |
| ResourceId-C-000-C | Composite | ResourceId | BILLING_BASED_ON_PROVISIONED_RESOURCES_SUPPORTED, RESOURCE_TYPE_ASSIGNMENT_SUPPORTED |  |  | AND of [Check ResourceId-C-001-M, Check ResourceId-C-002-M, Check ResourceId-C-003-C, Check ResourceId-C-006-C] |  | Static | 1.2 | Active |
| ResourceId-C-001-M | Type | ResourceId |  |  |  | TypeString(ResourceId) |  | Static | 1.2 | Active |
| ResourceId-C-002-M | Format | ResourceId |  |  |  | FormatString(ResourceId) |  | Static | 1.2 | Active |
| ResourceId-C-003-C | Composite | ResourceId |  |  |  | AND of [Check ResourceId-C-004-C, Check ResourceId-C-005-C] |  | Static | 1.2 | Active |
| ResourceId-C-004-C | Nullability | ResourceId |  |  |  |  |  | Dynamic | 1.2 | Active |
| ResourceId-C-005-C | Nullability | ResourceId |  |  |  |  |  | Dynamic | 1.2 | Active |
| ResourceId-C-006-C | Composite | ResourceId |  |  |  | AND of [Check ResourceId-C-007-M, Check ResourceId-C-008-O] | CheckNotValue | Static | 1.2 | Active |
| ResourceId-C-007-M | Validation | ResourceId |  |  |  |  |  | Dynamic | 1.2 | Active |
| ResourceId-C-008-O | Validation | ResourceId |  |  |  |  |  | Dynamic | 1.2 | Active |
| ResourceName-C-000-C | Composite | ResourceName | BILLING_BASED_ON_PROVISIONED_RESOURCES_SUPPORTED, RESOURCE_TYPE_ASSIGNMENT_SUPPORTED |  |  | AND of [Check ResourceName-C-001-M, Check ResourceName-C-002-M, Check ResourceName-C-003-O] |  | Static | 1.2 | Active |
| ResourceName-C-001-M | Type | ResourceName |  |  |  | TypeString |  | Static | 1.2 | Active |
| ResourceName-C-002-M | Format | ResourceName |  |  |  | FormatString |  | Static | 1.2 | Active |
| ResourceName-C-003-O | Nullability | ResourceName |  |  |  |  |  | Dynamic | 1.2 | Active |
| ResourceType-C-000-C | Composite | ResourceType | BILLING_BASED_ON_PROVISIONED_RESOURCES_SUPPORTED, RESOURCE_TYPE_ASSIGNMENT_SUPPORTED |  |  | AND of [Check ResourceType-C-001-M, Check ResourceType-C-002-M, Check ResourceType-C-003-C] |  | Static | 1.2 | Active |
| ResourceType-C-001-M | Type | ResourceType |  |  |  | TypeString(ResourceType) |  | Static | 1.2 | Active |
| ResourceType-C-002-M | Validation | ResourceType |  |  |  | FormatString(ResourceType) |  | Static | 1.2 | Active |
| ResourceType-C-003-C | Composite | ResourceType |  |  |  | AND of [Check ResourceType-C-004-C, Check ResourceType-C-005-C] |  | Static | 1.2 | Active |
| ResourceType-C-004-C | Nullability | ResourceType |  |  |  | CheckValue(ResourceType, null) | CheckValue(ResourceId, null) | Static | 1.2 | Active |
| ResourceType-C-005-C | Nullability | ResourceType |  |  |  | CheckNotValue(ResourceType, null) | CheckNotValue | Static | 1.2 | Active |
| ServiceCategory-C-000-M | Composite | ServiceCategory |  |  |  | AND of [Check ServiceCategory-C-001-M, Check ServiceCategory-C-002-M, Check ServiceCategory-C-003-M] |  | Static | 1.2 | Active |
| ServiceCategory-C-001-M | Type | ServiceCategory |  |  |  | TypeString(ServiceCategory) |  | Static | 1.2 | Active |
| ServiceCategory-C-002-M | Nullability | ServiceCategory |  |  |  | CheckNotValue(ServiceCategory, null) |  | Static | 1.2 | Active |
| ServiceCategory-C-003-M | Validation | ServiceCategory |  |  |  | OR of [CheckValue(ServiceCategory, AI and Machine Learning), CheckValue(ServiceCategory, Analytics), CheckValue(ServiceCategory, Business Applications), CheckValue(ServiceCategory, Compute), CheckValue(ServiceCategory, Databases), CheckValue(ServiceCategory, Developer Tools), CheckValue(ServiceCategory, Multicloud), CheckValue(ServiceCategory, Identity), CheckValue(ServiceCategory, Integration), CheckValue(ServiceCategory, Internet of Things), CheckValue(ServiceCategory, Management and Governance), CheckValue(ServiceCategory, Media), CheckValue(ServiceCategory, Migration), CheckValue(ServiceCategory, Mobile), CheckValue(ServiceCategory, Networking), CheckValue(ServiceCategory, Security), CheckValue(ServiceCategory, Storage), CheckValue(ServiceCategory, Web), CheckValue(ServiceCategory, Other)] |  | Static | 1.2 | Active |
| ServiceName-C-000-M | Composite | ServiceName |  |  |  | AND of [Check ServiceName-C-001-M, Check ServiceName-C-002-M, Check ServiceName-C-003-M, Check ServiceName-C-004-C, Check ServiceName-C-007-C] |  | Static | 1.2 | Active |
| ServiceName-C-001-M | Type | ServiceName |  |  |  | TypeString(ServiceName) |  | Static | 1.2 | Active |
| ServiceName-C-002-M | Format | ServiceName |  |  |  | FormatString(ServiceName) |  | Static | 1.2 | Active |
| ServiceName-C-003-M | Nullability | ServiceName |  |  |  | CheckNotValue(ServiceName, null) |  | Static | 1.2 | Active |
| ServiceName-C-004-C | Composite | ServiceName |  |  |  | AND of [Check ServiceName-C-005-C, Check ServiceName-C-006-C] |  | Static | 1.2 | Active |
| ServiceName-C-005-C | Validation | ServiceName |  |  |  | CheckDistinctCount(ServiceName, ServiceCategory) |  | Static | 1.2 | Active |
| ServiceName-C-006-C | Validation | ServiceName |  |  |  |  |  | Dynamic | 1.2 | Active |
| ServiceName-C-007-C | Composite | ServiceName |  |  |  | AND of [Check ServiceName-C-008-C, Check ServiceName-C-009-C] |  | Static | 1.2 | Active |
| ServiceName-C-008-C | Validation | ServiceName |  |  |  | CheckDistinctCount(ServiceName, ServiceSubcategory) |  | Static | 1.2 | Active |
| ServiceName-C-009-C | Validation | ServiceName |  |  |  |  |  | Dynamic | 1.2 | Active |
| ServiceSubcategory-C-000-O | Composite | ServiceSubcategory |  |  |  | AND of [Check ServiceSubcategory-C-001-M, Check ServiceSubcategory-C-002-M, Check ServiceSubcategory-C-003-M, Check ServiceSubcategory-C-004-M] |  | Static | 1.2 | Active |
| ServiceSubcategory-C-001-M | Type | ServiceSubcategory |  |  |  | TypeString(ServiceSubcategory) |  | Static | 1.2 | Active |
| ServiceSubcategory-C-002-M | Nullability | ServiceSubcategory |  |  |  | CheckNotValue(ServiceSubcategory, null) |  | Static | 1.2 | Active |
| ServiceSubcategory-C-003-M | Validation | ServiceSubcategory |  |  |  | OR of [CheckValue(ServiceSubcategory, AI Platforms), CheckValue(ServiceSubcategory, Bots), CheckValue(ServiceSubcategory, Generative AI), CheckValue(ServiceSubcategory, Machine Learning), CheckValue(ServiceSubcategory, Natural Language Processing), CheckValue(ServiceSubcategory, Other (AI and Machine Learning)), CheckValue(ServiceSubcategory, Analytics Platforms), CheckValue(ServiceSubcategory, Business Intelligence), CheckValue(ServiceSubcategory, Data Processing), CheckValue(ServiceSubcategory, Search), CheckValue(ServiceSubcategory, Streaming Analytics), CheckValue(ServiceSubcategory, Other (Analytics)), CheckValue(ServiceSubcategory, Productivity and Collaboration), CheckValue(ServiceSubcategory, Other (Business Applications)), CheckValue(ServiceSubcategory, Containers), CheckValue(ServiceSubcategory, End User Computing), CheckValue(ServiceSubcategory, Quantum Compute), CheckValue(ServiceSubcategory, Serverless Compute), CheckValue(ServiceSubcategory, Virtual Machines), CheckValue(ServiceSubcategory, Other (Compute)), CheckValue(ServiceSubcategory, Caching), CheckValue(ServiceSubcategory, Data Warehouses), CheckValue(ServiceSubcategory, Ledger Databases), CheckValue(ServiceSubcategory, NoSQL Databases), CheckValue(ServiceSubcategory, Relational Databases), CheckValue(ServiceSubcategory, Time Series Databases), CheckValue(ServiceSubcategory, Other (Databases)), CheckValue(ServiceSubcategory, Developer Platforms), CheckValue(ServiceSubcategory, Continuous Integration and Deployment), CheckValue(ServiceSubcategory, Development Environments), CheckValue(ServiceSubcategory, Source Code Management), CheckValue(ServiceSubcategory, Quality Assurance), CheckValue(ServiceSubcategory, Other (Developer Tools)), CheckValue(ServiceSubcategory, Identity and Access Management), CheckValue(ServiceSubcategory, Other (Identity)), CheckValue(ServiceSubcategory, API Management), CheckValue(ServiceSubcategory, Messaging), CheckValue(ServiceSubcategory, Workflow Orchestration), CheckValue(ServiceSubcategory, Other (Integration)), CheckValue(ServiceSubcategory, IoT Analytics), CheckValue(ServiceSubcategory, IoT Platforms), CheckValue(ServiceSubcategory, Other (Internet of Things)), CheckValue(ServiceSubcategory, Architecture), CheckValue(ServiceSubcategory, Compliance), CheckValue(ServiceSubcategory, Cost Management), CheckValue(ServiceSubcategory, Data Governance), CheckValue(ServiceSubcategory, Disaster Recovery), CheckValue(ServiceSubcategory, Endpoint Management), CheckValue(ServiceSubcategory, Observability), CheckValue(ServiceSubcategory, Support), CheckValue(ServiceSubcategory, Other (Management and Governance)), CheckValue(ServiceSubcategory, Content Creation), CheckValue(ServiceSubcategory, Gaming), CheckValue(ServiceSubcategory, Media Streaming), CheckValue(ServiceSubcategory, Mixed Reality), CheckValue(ServiceSubcategory, Other (Media)), CheckValue(ServiceSubcategory, Data Migration), CheckValue(ServiceSubcategory, Resource Migration), CheckValue(ServiceSubcategory, Other (Migration)), CheckValue(ServiceSubcategory, Other (Mobile)), CheckValue(ServiceSubcategory, Multicloud Integration), CheckValue(ServiceSubcategory, Other (Multicloud)), CheckValue(ServiceSubcategory, Application Networking), CheckValue(ServiceSubcategory, Content Delivery), CheckValue(ServiceSubcategory, Network Connectivity), CheckValue(ServiceSubcategory, Network Infrastructure), CheckValue(ServiceSubcategory, Network Routing), CheckValue(ServiceSubcategory, Network Security), CheckValue(ServiceSubcategory, Other (Networking)), CheckValue(ServiceSubcategory, Secret Management), CheckValue(ServiceSubcategory, Security Posture Management), CheckValue(ServiceSubcategory, Threat Detection and Response), CheckValue(ServiceSubcategory, Other (Security)), CheckValue(ServiceSubcategory, Backup Storage), CheckValue(ServiceSubcategory, Block Storage), CheckValue(ServiceSubcategory, File Storage), CheckValue(ServiceSubcategory, Object Storage), CheckValue(ServiceSubcategory, Storage Platforms), CheckValue(ServiceSubcategory, Other (Storage)), CheckValue(ServiceSubcategory, Application Platforms), CheckValue(ServiceSubcategory, Other (Web)), CheckValue(ServiceSubcategory, Other (Other))] |  | Static | 1.2 | Active |
| ServiceSubcategory-C-004-M | Validation | ServiceSubcategory |  |  |  | OR of [AND of [CheckValue(ServiceSubcategory, AI Platforms), CheckValue(ServiceCategory, AI and Machine Learning)], AND of [CheckValue(ServiceSubcategory, Bots), CheckValue(ServiceCategory, AI and Machine Learning)], AND of [CheckValue(ServiceSubcategory, Generative AI), CheckValue(ServiceCategory, AI and Machine Learning)], AND of [CheckValue(ServiceSubcategory, Machine Learning), CheckValue(ServiceCategory, AI and Machine Learning)], AND of [CheckValue(ServiceSubcategory, Natural Language Processing), CheckValue(ServiceCategory, AI and Machine Learning)], AND of [CheckValue(ServiceSubcategory, Other (AI and Machine Learning)), CheckValue(ServiceCategory, AI and Machine Learning)], AND of [CheckValue(ServiceSubcategory, Analytics Platforms), CheckValue(ServiceCategory, Analytics)], AND of [CheckValue(ServiceSubcategory, Business Intelligence), CheckValue(ServiceCategory, Analytics)], AND of [CheckValue(ServiceSubcategory, Data Processing), CheckValue(ServiceCategory, Analytics)], AND of [CheckValue(ServiceSubcategory, Search), CheckValue(ServiceCategory, Analytics)], AND of [CheckValue(ServiceSubcategory, Streaming Analytics), CheckValue(ServiceCategory, Analytics)], AND of [CheckValue(ServiceSubcategory, Other (Analytics)), CheckValue(ServiceCategory, Analytics)], AND of [CheckValue(ServiceSubcategory, Productivity and Collaboration), CheckValue(ServiceCategory, Business Applications)], AND of [CheckValue(ServiceSubcategory, Other (Business Applications)), CheckValue(ServiceCategory, Business Applications)], AND of [CheckValue(ServiceSubcategory, Containers), CheckValue(ServiceCategory, Compute)], AND of [CheckValue(ServiceSubcategory, End User Computing), CheckValue(ServiceCategory, Compute)], AND of [CheckValue(ServiceSubcategory, Quantum Compute), CheckValue(ServiceCategory, Compute)], AND of [CheckValue(ServiceSubcategory, Serverless Compute), CheckValue(ServiceCategory, Compute)], AND of [CheckValue(ServiceSubcategory, Virtual Machines), CheckValue(ServiceCategory, Compute)], AND of [CheckValue(ServiceSubcategory, Other (Compute)), CheckValue(ServiceCategory, Compute)], AND of [CheckValue(ServiceSubcategory, Caching), CheckValue(ServiceCategory, Databases)], AND of [CheckValue(ServiceSubcategory, Data Warehouses), CheckValue(ServiceCategory, Databases)], AND of [CheckValue(ServiceSubcategory, Ledger Databases), CheckValue(ServiceCategory, Databases)], AND of [CheckValue(ServiceSubcategory, NoSQL Databases), CheckValue(ServiceCategory, Databases)], AND of [CheckValue(ServiceSubcategory, Relational Databases), CheckValue(ServiceCategory, Databases)], AND of [CheckValue(ServiceSubcategory, Time Series Databases), CheckValue(ServiceCategory, Databases)], AND of [CheckValue(ServiceSubcategory, Other (Databases)), CheckValue(ServiceCategory, Databases)], AND of [CheckValue(ServiceSubcategory, Developer Platforms), CheckValue(ServiceCategory, Developer Tools)], AND of [CheckValue(ServiceSubcategory, Continuous Integration and Deployment), CheckValue(ServiceCategory, Developer Tools)], AND of [CheckValue(ServiceSubcategory, Development Environments), CheckValue(ServiceCategory, Developer Tools)], AND of [CheckValue(ServiceSubcategory, Source Code Management), CheckValue(ServiceCategory, Developer Tools)], AND of [CheckValue(ServiceSubcategory, Quality Assurance), CheckValue(ServiceCategory, Developer Tools)], AND of [CheckValue(ServiceSubcategory, Other (Developer Tools)), CheckValue(ServiceCategory, Developer Tools)], AND of [CheckValue(ServiceSubcategory, Identity and Access Management), CheckValue(ServiceCategory, Identity)], AND of [CheckValue(ServiceSubcategory, Other (Identity)), CheckValue(ServiceCategory, Identity)], AND of [CheckValue(ServiceSubcategory, API Management), CheckValue(ServiceCategory, Integration)], AND of [CheckValue(ServiceSubcategory, Messaging), CheckValue(ServiceCategory, Integration)], AND of [CheckValue(ServiceSubcategory, Workflow Orchestration), CheckValue(ServiceCategory, Integration)], AND of [CheckValue(ServiceSubcategory, Other (Integration)), CheckValue(ServiceCategory, Integration)], AND of [CheckValue(ServiceSubcategory, IoT Analytics), CheckValue(ServiceCategory, Internet of Things)], AND of [CheckValue(ServiceSubcategory, IoT Platforms), CheckValue(ServiceCategory, Internet of Things)], AND of [CheckValue(ServiceSubcategory, Other (Internet of Things)), CheckValue(ServiceCategory, Internet of Things)], AND of [CheckValue(ServiceSubcategory, Architecture), CheckValue(ServiceCategory, Management and Governance)], AND of [CheckValue(ServiceSubcategory, Compliance), CheckValue(ServiceCategory, Management and Governance)], AND of [CheckValue(ServiceSubcategory, Cost Management), CheckValue(ServiceCategory, Management and Governance)], AND of [CheckValue(ServiceSubcategory, Data Governance), CheckValue(ServiceCategory, Management and Governance)], AND of [CheckValue(ServiceSubcategory, Disaster Recovery), CheckValue(ServiceCategory, Management and Governance)], AND of [CheckValue(ServiceSubcategory, Endpoint Management), CheckValue(ServiceCategory, Management and Governance)], AND of [CheckValue(ServiceSubcategory, Observability), CheckValue(ServiceCategory, Management and Governance)], AND of [CheckValue(ServiceSubcategory, Support), CheckValue(ServiceCategory, Management and Governance)], AND of [CheckValue(ServiceSubcategory, Other (Management and Governance)), CheckValue(ServiceCategory, Management and Governance)], AND of [CheckValue(ServiceSubcategory, Content Creation), CheckValue(ServiceCategory, Media)], AND of [CheckValue(ServiceSubcategory, Gaming), CheckValue(ServiceCategory, Media)], AND of [CheckValue(ServiceSubcategory, Media Streaming), CheckValue(ServiceCategory, Media)], AND of [CheckValue(ServiceSubcategory, Mixed Reality), CheckValue(ServiceCategory, Media)], AND of [CheckValue(ServiceSubcategory, Other (Media)), CheckValue(ServiceCategory, Media)], AND of [CheckValue(ServiceSubcategory, Data Migration), CheckValue(ServiceCategory, Migration)], AND of [CheckValue(ServiceSubcategory, Resource Migration), CheckValue(ServiceCategory, Migration)], AND of [CheckValue(ServiceSubcategory, Other (Migration)), CheckValue(ServiceCategory, Migration)], AND of [CheckValue(ServiceSubcategory, Other (Mobile)), CheckValue(ServiceCategory, Mobile)], AND of [CheckValue(ServiceSubcategory, Multicloud Integration), CheckValue(ServiceCategory, Multicloud)], AND of [CheckValue(ServiceSubcategory, Other (Multicloud)), CheckValue(ServiceCategory, Multicloud)], AND of [CheckValue(ServiceSubcategory, Application Networking), CheckValue(ServiceCategory, Networking)], AND of [CheckValue(ServiceSubcategory, Content Delivery), CheckValue(ServiceCategory, Networking)], AND of [CheckValue(ServiceSubcategory, Network Connectivity), CheckValue(ServiceCategory, Networking)], AND of [CheckValue(ServiceSubcategory, Network Infrastructure), CheckValue(ServiceCategory, Networking)], AND of [CheckValue(ServiceSubcategory, Network Routing), CheckValue(ServiceCategory, Networking)], AND of [CheckValue(ServiceSubcategory, Network Security), CheckValue(ServiceCategory, Networking)], AND of [CheckValue(ServiceSubcategory, Other (Networking)), CheckValue(ServiceCategory, Networking)], AND of [CheckValue(ServiceSubcategory, Secret Management), CheckValue(ServiceCategory, Security)], AND of [CheckValue(ServiceSubcategory, Security Posture Management), CheckValue(ServiceCategory, Security)], AND of [CheckValue(ServiceSubcategory, Threat Detection and Response), CheckValue(ServiceCategory, Security)], AND of [CheckValue(ServiceSubcategory, Other (Security)), CheckValue(ServiceCategory, Security)], AND of [CheckValue(ServiceSubcategory, Backup Storage), CheckValue(ServiceCategory, Storage)], AND of [CheckValue(ServiceSubcategory, Block Storage), CheckValue(ServiceCategory, Storage)], AND of [CheckValue(ServiceSubcategory, File Storage), CheckValue(ServiceCategory, Storage)], AND of [CheckValue(ServiceSubcategory, Object Storage), CheckValue(ServiceCategory, Storage)], AND of [CheckValue(ServiceSubcategory, Storage Platforms), CheckValue(ServiceCategory, Storage)], AND of [CheckValue(ServiceSubcategory, Other (Storage)), CheckValue(ServiceCategory, Storage)], AND of [CheckValue(ServiceSubcategory, Application Platforms), CheckValue(ServiceCategory, Web)], AND of [CheckValue(ServiceSubcategory, Other (Web)), CheckValue(ServiceCategory, Web)], AND of [CheckValue(ServiceSubcategory, Other (Other)), CheckValue(ServiceCategory, Other)]] |  | Static | 1.2 | Active |
| SkuId-C-000-C | Composite | SkuId | PUBLIC_PRICE_LIST_SUPPORTED, UNIT_PRICING_SUPPORTED |  |  | AND of [Check SkuId-C-001-M, Check SkuId-C-002-M, Check SkuId-C-003-M, Check SkuId-C-007-M, Check SkuId-C-011-C, Check SkuId-C-012-O] |  | Static | 1.2 | Active |
| SkuId-C-001-M | Type | SkuId |  |  |  | TypeString(SkuId) |  | Static | 1.2 | Active |
| SkuId-C-002-M | Format | SkuId |  |  |  | FormatString(SkuId) |  | Static | 1.2 | Active |
| SkuId-C-003-M | Composite | SkuId |  |  |  | AND of [Check SkuId-C-004-C, Check SkuId-C-005-C, Check SkuId-C-006-O] |  | Static | 1.2 | Active |
| SkuId-C-004-C | Nullability | SkuId |  |  |  | CheckValue(SkuId, null) | CheckValue(ChargeCategory, Tax) | Static | 1.2 | Active |
| SkuId-C-005-C | Nullability | SkuId |  |  |  | CheckNotValue(SkuId, null) | AND of [OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)], CheckNotValue(ChargeClass, Correction)] | Static | 1.2 | Active |
| SkuId-C-006-O | Nullability | SkuId |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuId-C-007-M | Composite | SkuId |  |  |  | AND of [Check SkuId-C-008-M, Check SkuId-C-009-M, Check SkuId-C-010-M] |  | Static | 1.2 | Active |
| SkuId-C-008-M | Validation | SkuId |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuId-C-009-M | Validation | SkuId |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuId-C-010-M | Validation | SkuId |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuId-C-011-C | Validation | SkuId |  |  |  |  | OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)] | Dynamic | 1.2 | Active |
| SkuId-C-012-O | Validation | SkuId |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuMeter-C-000-C | Composite | SkuMeter | PUBLIC_PRICE_LIST_SUPPORTED, UNIT_PRICING_SUPPORTED |  |  | AND of [Check SkuMeter-C-001-M, Check SkuMeter-C-002-M, Check SkuMeter-C-003-C, Check SkuMeter-C-006-O] |  | Static | 1.2 | Active |
| SkuMeter-C-001-M | Type | SkuMeter |  |  |  | TypeString(SkuMeter) |  | Static | 1.2 | Active |
| SkuMeter-C-002-M | Format | SkuMeter |  |  |  | FormatString(SkuMeter) |  | Static | 1.2 | Active |
| SkuMeter-C-003-C | Composite | SkuMeter |  |  |  | AND of [Check SkuMeter-C-004-C, Check SkuMeter-C-005-C] |  | Static | 1.2 | Active |
| SkuMeter-C-004-C | Nullability | SkuMeter |  |  |  | CheckValue(SkuMeter, null) | CheckValue(SkuId, null) | Static | 1.2 | Active |
| SkuMeter-C-005-C | Nullability | SkuMeter |  |  |  | CheckNotValue(SkuMeter, null) | CheckNotValue(SkuId, null) | Static | 1.2 | Active |
| SkuMeter-C-006-O | Validation | SkuMeter |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-000-C | Composite | SkuPriceDetails | PUBLIC_PRICE_LIST_SUPPORTED, UNIT_PRICING_SUPPORTED |  |  | AND of [Check SkuPriceDetails-C-001-M, Check SkuPriceDetails-C-002-O, Check SkuPriceDetails-C-003-C, Check SkuPriceDetails-C-006-C, Check SkuPriceDetails-C-019-M] |  | Static | 1.2 | Active |
| SkuPriceDetails-C-001-M | Format | SkuPriceDetails |  |  |  | FormatKeyValue(SkuPriceDetails) |  | Static | 1.2 | Active |
| SkuPriceDetails-C-002-O | Format | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-003-C | Composite | SkuPriceDetails |  |  |  | AND of [Check SkuPriceDetails-C-004-C, Check SkuPriceDetails-C-005-C] |  | Static | 1.2 | Active |
| SkuPriceDetails-C-004-C | Nullability | SkuPriceDetails |  |  |  | CheckValue(SkuPriceDetails, null) | CheckValue(SkuPriceId, null) | Static | 1.2 | Active |
| SkuPriceDetails-C-005-C | Nullability | SkuPriceDetails |  |  |  | CheckValue(SkuPriceDetails, null) | CheckNotValue(SkuPriceId, null) | Static | 1.2 | Active |
| SkuPriceDetails-C-006-C | Composite | SkuPriceDetails |  |  |  | AND of [Check SkuPriceDetails-C-007-M, Check SkuPriceDetails-C-008-M, Check SkuPriceDetails-C-009-C, Check SkuPriceDetails-C-010-C, Check SkuPriceDetails-C-011-O, Check SkuPriceDetails-C-012-O, Check SkuPriceDetails-C-016-O, Check SkuPriceDetails-C-017-C, Check SkuPriceDetails-C-018-C] | CheckNotValue(SkuPriceDetails, null) | Static | 1.2 | Active |
| SkuPriceDetails-C-007-M | Validation | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-008-M | Validation | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-009-C | Validation | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-010-C | Validation | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-011-O | Validation | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-012-O | Composite | SkuPriceDetails |  |  |  | AND of [Check SkuPriceDetails-C-013-O, Check SkuPriceDetails-C-014-O, Check SkuPriceDetails-C-015-O] |  | Static | 1.2 | Active |
| SkuPriceDetails-C-013-O | Validation | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-014-O | Validation | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-015-O | Validation | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-016-O | Format | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-017-C | Format | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-018-C | Validation | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-019-M | Composite | SkuPriceDetails |  |  |  | AND of [Check SkuPriceDetails-C-020-M, Check SkuPriceDetails-C-021-M, Check SkuPriceDetails-C-022-C] |  | Static | 1.2 | Active |
| SkuPriceDetails-C-020-M | Format | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-021-M | Type | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceDetails-C-022-C | Validation | SkuPriceDetails |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceId-C-000-C | Composite | SkuPriceId | PUBLIC_PRICE_LIST_SUPPORTED, UNIT_PRICING_SUPPORTED |  |  | AND of [Check SkuPriceId-C-001-M, Check SkuPriceId-C-002-M, Check SkuPriceId-C-003-M, Check SkuPriceId-C-007-C] |  | Static | 1.2 | Active |
| SkuPriceId-C-001-M | Type | SkuPriceId |  |  |  | TypeString(SkuPriceId) |  | Static | 1.2 | Active |
| SkuPriceId-C-002-M | Format | SkuPriceId |  |  |  | FormatString |  | Static | 1.2 | Active |
| SkuPriceId-C-003-M | Composite | SkuPriceId |  |  |  | AND of [Check SkuPriceId-C-004-C, Check SkuPriceId-C-005-C, Check SkuPriceId-C-006-O] |  | Static | 1.2 | Active |
| SkuPriceId-C-004-C | Nullability | SkuPriceId |  |  |  | CheckValue(SkuPriceId, null) | CheckValue(ChargeCategory, Tax) | Static | 1.2 | Active |
| SkuPriceId-C-005-C | Nullability | SkuPriceId |  |  |  | CheckNotValue(SkuPriceId, null) | AND of [OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)], CheckNotValue(ChargeClass, Correction)] | Static | 1.2 | Active |
| SkuPriceId-C-006-O | Nullability | SkuPriceId |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceId-C-007-C | Composite | SkuPriceId |  |  |  | AND of [Check SkuPriceId-C-008-M, Check SkuPriceId-C-009-M, Check SkuPriceId-C-010-M, Check SkuPriceId-C-011-O, Check SkuPriceId-C-012-C, Check SkuPriceId-C-013-M, Check SkuPriceId-C-014-C, Check SkuPriceId-C-015-C] | CheckNotValue(SkuPriceId, null) | Static | 1.2 | Active |
| SkuPriceId-C-008-M | Validation | SkuPriceId |  |  |  | CheckDistinctCount(SkuPriceId, SkuId) |  | Static | 1.2 | Active |
| SkuPriceId-C-009-M | Validation | SkuPriceId |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceId-C-010-M | Validation | SkuPriceId |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceId-C-011-O | Validation | SkuPriceId |  |  |  | CheckSameValue(SkuPriceId, SkuId) |  | Static | 1.2 | Active |
| SkuPriceId-C-012-C | Validation | SkuPriceId |  |  |  |  | OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)] | Dynamic | 1.2 | Active |
| SkuPriceId-C-013-M | Validation | SkuPriceId |  |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceId-C-014-C | Validation | SkuPriceId | PUBLIC_PRICE_LIST_SUPPORTED |  |  |  |  | Dynamic | 1.2 | Active |
| SkuPriceId-C-015-C | Validation | SkuPriceId | NEGOTIATED_PRICING_SUPPORTED |  |  |  |  | Dynamic | 1.2 | Active |
| SubAccountId-C-000-C | Composite | SubAccountId | SUB_ACCOUNT_SUPPORTED |  |  | AND of [Check SubAccountId-C-001-M, Check SubAccountId-C-002-M, Check SubAccountId-C-003-C] |  | Static | 1.2 | Active |
| SubAccountId-C-001-M | Type | SubAccountId |  |  |  | TypeString(SubAccountId) |  | Static | 1.2 | Active |
| SubAccountId-C-002-M | Format | SubAccountId |  |  |  | FormatString(SubAccountId) |  | Static | 1.2 | Active |
| SubAccountId-C-003-C | Composite | SubAccountId |  |  |  | AND of [Check SubAccountId-C-004-C, Check SubAccountId-C-005-C] |  | Static | 1.2 | Active |
| SubAccountId-C-004-C | Nullability | SubAccountId |  |  |  |  |  | Dynamic | 1.2 | Active |
| SubAccountId-C-005-C | Nullability | SubAccountId |  |  |  |  |  | Dynamic | 1.2 | Active |
| SubAccountName-C-000-C | Composite | SubAccountName | SUB_ACCOUNT_SUPPORTED |  |  | AND of [Check SubAccountName-C-001-M, Check SubAccountName-C-002-M, Check SubAccountName-C-003-C, Check SubAccountName-C-004-C] |  | Static | 1.2 | Active |
| SubAccountName-C-001-M | Type | SubAccountName |  |  |  | TypeString(SubAccountName) |  | Static | 1.2 | Active |
| SubAccountName-C-002-M | Format | SubAccountName |  |  |  | FormatString(SubAccountName) |  | Static | 1.2 | Active |
| SubAccountName-C-003-C | Nullability | SubAccountName |  |  |  | CheckValue(SubAccountName, null) | CheckValue(SubAccountId, null) | Static | 1.2 | Active |
| SubAccountName-C-004-C | Nullability | SubAccountName |  |  |  | CheckNotValue(SubAccountName, null) | CheckNotValue(SubAccountId, null) | Static | 1.2 | Active |
| SubAccountType-C-000-C | Composite | SubAccountType | MULTIPLE_SUB_ACCOUNT_TYPES_SUPPORTED |  |  | AND of [Check SubAccountType-C-001-M, Check SubAccountType-C-002-M, Check SubAccountType-C-003-C, Check SubAccountType-C-006-M] |  | Static | 1.2 | Active |
| SubAccountType-C-001-M | Type | SubAccountType |  |  |  | TypeString(SubAccountType) |  | Static | 1.2 | Active |
| SubAccountType-C-002-M | Format | SubAccountType |  |  |  | FormatString(SubAccountType) |  | Static | 1.2 | Active |
| SubAccountType-C-003-C | Composite | SubAccountType |  |  |  | OR of [Check SubAccountType-C-004-C, Check SubAccountType-C-005-C] |  | Static | 1.2 | Active |
| SubAccountType-C-006-M | Validation | SubAccountType |  |  |  |  |  | Dynamic | 1.2 | Active |
| Tags-C-000-C | Composite | Tags | TAGGING_SUPPORTED |  |  | AND of [Check Tags-C-001-M, Check Tags-C-002-M, Check Tags-C-003-C] |  | Static | 1.2 | Active |
| Tags-C-001-M | Type | Tags |  |  |  | FormatKeyValue(Tags) |  | Static | 1.2 | Active |
| Tags-C-002-M | Format | Tags |  |  |  |  |  | Dynamic | 1.2 | Active |
| Tags-C-003-C | Nullability | Tags |  |  |  | CheckValue(Tags, null) |  | Static | 1.2 | Active |
