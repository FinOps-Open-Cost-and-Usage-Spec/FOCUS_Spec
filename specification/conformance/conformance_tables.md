# Conformance Dataset: FOCUS

| ConformanceRuleId | Function | Reference | ApplicabilityCriteria | mustSatisfy | KeyWord | Requirement | Condition | Type | CRVersionIntroduced | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AvailabilityZone-C-000-M | Composite | AvailabilityZone | AVAILABILITY_ZONE_SUPPORTED |  |  | AND of [Check AvailabilityZone-C-001-C, Check AvailabilityZone-C-002-M, Check AvailabilityZone-C-003-M, Check AvailabilityZone-C-004-M] |  | Static | 1.2 | Active |
| AvailabilityZone-C-001-C | Presence | AvailabilityZone | AVAILABILITY_ZONE_SUPPORTED |  |  | ColumnPresent(SampleColumn) |  | Static | 1.2 | Active |
| AvailabilityZone-C-002-M | Type | AvailabilityZone |  |  |  | TypeString(AvailabilityZone) |  | Static | 1.2 | Active |
| AvailabilityZone-C-003-M | Type | AvailabilityZone |  |  |  | FormatString(AvailabilityZone) |  | Static | 1.2 | Active |
| AvailabilityZone-C-004-M | Validation | AvailabilityZone |  |  |  |  |  | Dynamic | 1.2 | Active |
| BilledCost-C-000-M | Composite | BilledCost |  |  |  | AND of [Check BilledCost-C-001-M, Check BilledCost-C-002-M, Check BilledCost-C-003-M, Check BilledCost-C-004-M, Check BilledCost-C-005-M, Check BilledCost-C-006-M, Check BilledCost-C-007-M] |  | Static | 1.2 | Active |
| BilledCost-C-001-M | Presence | BilledCost |  |  |  | ColumnPresent(BilledCost) |  | Static | 1.2 | Active |
| BilledCost-C-002-M | Validation | BilledCost |  |  |  | CheckNotValue(BilledCost, null) |  | Static | 1.2 | Active |
| BilledCost-C-003-M | Type | BilledCost |  |  |  | TypeDecimal(BilledCost) |  | Static | 1.2 | Active |
| BilledCost-C-004-M | Format | BilledCost |  |  |  | FormatNumeric(BilledCost) |  | Static | 1.2 | Active |
| BilledCost-C-005-M | Validation | BilledCost |  |  |  | CheckValue(BilledCost, 0) | CheckNotSameValue(ProviderName, InvoiceIssuerName) | Static | 1.2 | Active |
| BilledCost-C-006-M | Validation | BilledCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| BilledCost-C-007-M | Validation | BilledCost |  |  |  |  |  | Dynamic | 1.2 | Active |
| BillingAccountType-C-000-M | Composite | BillingAccountType |  |  |  | AND of [Check BillingAccountType-C-001-M, Check BillingAccountType-C-002-M, Check BillingAccountType-C-003-M] |  | Static | 1.2 | Active |
| BillingAccountType-C-002-M | Type | BillingAccountType |  |  |  | TypeString(BillingAccountType) |  | Static | 1.2 | Active |
| BillingAccountType-C-003-M | Type | BillingAccountType |  |  |  | FormatString(BillingAccountType) |  | Static | 1.2 | Active |
| ListUnitPrice-C-000-C | Composite | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | AND of [Check ListUnitPrice-C-001-C, Check ListUnitPrice-C-002-M, Check ListUnitPrice-C-003-M, Check ListUnitPrice-C-004-C, Check ListUnitPrice-C-005-C, Check ListUnitPrice-C-008-C, Check ListUnitPrice-C-009-C, Check ListUnitPrice-C-010-C, Check ListUnitPrice-C-011-M, Check ListUnitPrice-C-012-C] |  | Static | 1.2 | Active |
| ListUnitPrice-C-001-C | Presence | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  |  | ColumnPresent(ListUnitPrice) |  | Static | 1.2 | Active |
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
