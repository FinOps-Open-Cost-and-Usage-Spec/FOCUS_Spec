# Conformance Dataset: CostAndUsage

| ConformanceRuleId | Function | Reference | ApplicabilityCriteria | MustSatisfy | KeyWord | Requirement | Condition | Type | CRVersionIntroduced | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AvailabilityZone-C-000-M | Composite | AvailabilityZone | AVAILABILITY_ZONE_SUPPORTED |  |  | AND of [Check AvailabilityZone-C-002-M, Check AvailabilityZone-C-003-M, Check AvailabilityZone-C-004-M] |  | Static | 1.2 | Active |
| AvailabilityZone-C-002-M | Type | AvailabilityZone |  |  |  | TypeString(AvailabilityZone) |  | Static | 1.2 | Active |
| AvailabilityZone-C-003-M | Type | AvailabilityZone |  |  |  | FormatString(AvailabilityZone) |  | Static | 1.2 | Active |
| AvailabilityZone-C-004-M | Validation | AvailabilityZone |  |  |  |  |  | Dynamic | 1.2 | Active |
| BilledCost-C-000-M | Composite | BilledCost |  |  |  | AND of [Check BilledCost-C-002-M, Check BilledCost-C-003-M, Check BilledCost-C-004-M, Check BilledCost-C-005-M, Check BilledCost-C-006-M, Check BilledCost-C-007-M] |  | Static | 1.2 | Active |
| BilledCost-C-002-M | Validation | BilledCost |  |  |  | CheckNotValue(BilledCost, null) |  | Static | 1.2 | Active |
| BilledCost-C-003-M | Type | BilledCost |  |  |  | TypeDecimal(BilledCost) |  | Static | 1.2 | Active |
| BilledCost-C-004-M | Format | BilledCost |  |  |  | FormatNumeric(BilledCost) |  | Static | 1.2 | Active |
| BilledCost-C-005-M | Validation | BilledCost |  |  |  | CheckValue(BilledCost, 0) | CheckNotSameValue(ProviderName, InvoiceIssuerName) | Static | 1.2 | Active |
| BilledCost-C-006-M | Validation | BilledCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| BilledCost-C-007-M | Validation | BilledCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| BillingAccountName-C-000-M | Composite | BillingAccountName |  |  |  | AND of [Check BillingAccountName-D-001-M, Check BillingAccountName-C-002-M, Check BillingAccountName-C-003-M, Check BillingAccountName-C-004-C] |  | Static | 1.2 | Active |
| BillingAccountName-C-002-M | Type | BillingAccountName |  |  |  | TypeString(BillingAccountName) |  | Static | 1.2 | Active |
| BillingAccountName-C-003-M | Type | BillingAccountName |  |  |  | FormatString(BillingAccountName) |  | Static | 1.2 | Active |
| BillingAccountName-C-004-C | Validation | BillingAccountName | ACCOUNT_NAMING_SUPPORTED |  |  | CheckNotValue(BillingAccountName, null) |  | Static | 1.2 | Active |
| BillingAccountType-C-000-M | Composite | BillingAccountType |  |  |  | AND of [Check BillingAccountType-C-001-M, Check BillingAccountType-C-002-M, Check BillingAccountType-C-003-M] |  | Static | 1.2 | Active |
| BillingAccountType-C-002-M | Type | BillingAccountType |  |  |  | TypeString(BillingAccountType) |  | Static | 1.2 | Active |
| BillingAccountType-C-003-M | Type | BillingAccountType |  |  |  | FormatString(BillingAccountType) |  | Static | 1.2 | Active |
| BillingPeriodEnd-C-000-M | Composite | BillingPeriodEnd |  |  |  | AND of [Check BillingPeriodEnd-C-002-M, Check BillingPeriodEnd-C-003-M, Check BillingPeriodEnd-C-004-M, Check BillingPeriodEnd-C-005-M] |  | Static | 1.2 | Active |
| BillingPeriodEnd-C-002-M | Type | BillingPeriodEnd |  |  |  | TypeDateTime(BillingPeriodEnd) |  | Static | 1.2 | Active |
| BillingPeriodEnd-C-003-M | Format | BillingPeriodEnd |  |  |  | FormatDateTime(BillingPeriodEnd) |  | Static | 1.2 | Active |
| BillingPeriodEnd-C-004-M | Validation | BillingPeriodEnd |  |  |  | CheckNotValue(BillingPeriodEnd, null) |  | Static | 1.2 | Active |
| BillingPeriodEnd-C-005-M | Validation | BillingPeriodEnd |  |  |  | CheckExclusiveEndBound |  | Dynamic | 1.2 | Active |
| BillingPeriodStart-C-000-M | Composite | BillingPeriodStart |  |  |  | AND of [Check BillingPeriodStart-C-002-M, Check BillingPeriodStart-C-003-M, Check BillingPeriodStart-C-004-M, Check BillingPeriodStart-C-005-M] |  | Static | 1.2 | Active |
| BillingPeriodStart-C-002-M | Type | BillingPeriodStart |  |  |  | TypeDateTime(BillingPeriodStart) |  | Static | 1.2 | Active |
| BillingPeriodStart-C-003-M | Format | BillingPeriodStart |  |  |  | FormatDateTime(BillingPeriodStart) |  | Static | 1.2 | Active |
| BillingPeriodStart-C-004-M | Validation | BillingPeriodStart |  |  |  | CheckNotValue(BillingPeriodStart, null) |  | Static | 1.2 | Active |
| BillingPeriodStart-C-005-M | Validation | BillingPeriodStart |  |  |  | CheckBillingPeriodStartInclusive(BillingPeriodStart) |  | Dynamic | 1.2 | Active |
| CostAndUsage-C-006-M | Presence | BilledCost |  |  |  | ColumnPresent(BilledCost) |  | Static | 1.2 | Active |
| CostAndUsage-C-007-C | Presence | BillingAccountType |  |  |  | ColumnPresent(BillingAccountType) |  | Static | 1.2 | Active |
| CostAndUsage-D-000-M | Composite | CostAndUsage |  |  |  | AND of [Check CostAndUsage-D-001-M, Check CostAndUsage-D-002-M] |  | Static | 1.2 | Active |
| CostAndUsage-D-001-M | Composite | CostAndUsage |  |  |  | AND of [Check CostAndUsage-D-003-C, Check CostAndUsage-D-004-C, Check CostAndUsage-D-005-M, Check CostAndUsage-C-006-M, Check CostAndUsage-C-007-C, Check CostAndUsage-D-008-M, Check CostAndUsage-D-009-M, Check CostAndUsage-D-010-M] |  | Static | 1.2 | Active |
| CostAndUsage-D-002-M | Composite | CostAndUsage |  |  |  | AND of [Check AvailabilityZone-C-000-M, Check BilledCost-C-000-M, Check BillingAccountName-C-000-M, Check BillingAccountType-C-000-M, Check BillingPeriodStart-C-000-M, Check BillingPeriodEnd-C-000-M, Check ListUnitPrice-C-000-C] |  | Static | 1.2 | Active |
| CostAndUsage-D-003-C | Presence | AvailabilityZone | AVAILABILITY_ZONE_SUPPORTED |  |  | ColumnPresent(AvailabilityZone) |  | Static | 1.2 | Active |
| CostAndUsage-D-004-C | Presence | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | ColumnPresent(ListUnitPrice) |  | Static | 1.2 | Active |
| CostAndUsage-D-005-M | Presence | BillingAccountName |  |  |  | ColumnPresent(BillingAccountName) |  | Static | 1.2 | Active |
| CostAndUsage-D-008-M | Presence | ChargeCategory |  |  |  | ColumnPresent(ChargeCategory) |  | Static | 1.2 | Active |
| CostAndUsage-D-009-M | Presence | BillingPeriodStart |  |  |  | ColumnPresent(BillingPeriodStart) |  | Static | 1.2 | Active |
| CostAndUsage-D-010-M | Presence | BillingPeriodEnd |  |  |  | ColumnPresent(BillingPeriodEnd) |  | Static | 1.2 | Active |
| ListUnitPrice-C-000-C | Composite | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | AND of [Check ListUnitPrice-C-002-M, Check ListUnitPrice-C-003-M, Check ListUnitPrice-C-004-C, Check ListUnitPrice-C-005-C, Check ListUnitPrice-C-008-C, Check ListUnitPrice-C-009-C, Check ListUnitPrice-C-010-C, Check ListUnitPrice-C-011-M, Check ListUnitPrice-C-012-C] |  | Static | 1.2 | Active |
| ListUnitPrice-C-002-M | Type | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | TypeDecimal(ListUnitPrice) |  | Static | 1.2 | Active |
| ListUnitPrice-C-003-M | Format | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | FormatNumeric(ListUnitPrice) |  | Static | 1.2 | Active |
| ListUnitPrice-C-004-C | Validation | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | CheckValue(ListUnitPrice, null) | CheckValue(ChargeCategory, Tax) | Static | 1.2 | Active |
| ListUnitPrice-C-005-C | Composite | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | AND of [Check ListUnitPrice-C-006-C, Check ListUnitPrice-C-007-O] | OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)] | Static | 1.2 | Active |
| ListUnitPrice-C-006-C | Validation | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | CheckNotValue(ListUnitPrice, null) | CheckNotValue(ChargeClass, Correction) | Static | 1.2 | Active |
| ListUnitPrice-C-007-O | Validation | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  |  |  | Static | 1.2 | Active |
| ListUnitPrice-C-008-C | Composite | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | AND of [Check ListUnitPrice-C-009-C, Check ListUnitPrice-C-010-C, Check ListUnitPrice-C-011-M] | CheckNotValue(ListUnitPrice, null) | Static | 1.2 | Active |
| ListUnitPrice-C-009-C | Validation | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | CheckGreaterOrEqualThanValue(ListUnitPrice, 0) |  | Static | 1.2 | Active |
| ListUnitPrice-C-010-C | Validation | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  |  |  | Dynamic | 1.2 | Active |
| ListUnitPrice-C-011-M | Format | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | ColumnByColumnEqualsColumnValue(ListUnitPrice, PricingQuantity) -> ListCost | AND of [CheckNotValue(ListUnitPrice, null), CheckNotValue(ChargeClass, Correction)] | Static | 1.2 | Active |
| ListUnitPrice-C-012-C | Validation | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  |  | CheckValue(ChargeClass, Correction) | Dynamic | 1.2 | Active |
