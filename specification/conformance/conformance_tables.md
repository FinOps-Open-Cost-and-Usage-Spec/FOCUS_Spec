# Conformance Table: FOCUS

| ConformanceRuleId | Function | Reference | ApplicabilityCriteria | mustSatisfy | KeyWord | Requirement | Condition | Type | CRVersionIntroduced | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BilledCost-C-000-M | Composite | BilledCost |  |  | MUST | AND of [Check BilledCost-C-001-M, Check BilledCost-C-002-M, Check BilledCost-C-003-M, Check BilledCost-C-004-M, Check BilledCost-C-005-M, Check BilledCost-C-006-M, Check BilledCost-C-007-M] |  | Static | 1.2 | active |
| BilledCost-C-001-M | Presence | BilledCost |  | MUST be present in a FOCUS dataset | MUST | ColumnPresent(BilledCost) |  | Static | 1.2 | active |
| BilledCost-C-002-M | Validation | BilledCost |  | MUST NOT be null | MUST | CheckNotValue(BilledCost, null) |  | Static | 0.5 | active |
| BilledCost-C-003-M | Type | BilledCost |  | MUST be of type Decimal | MUST | TypeDecimal(BilledCost) |  | Static | 1.2 | active |
| BilledCost-C-004-M | Format | BilledCost |  | MUST conform to NumericFormat requirements | MUST | FormatNumeric(BilledCost) |  | Static | 1.2 | active |
| BilledCost-C-005-M | Validation | BilledCost |  | MUST be 0 for charges where payments are received by a third party | MUST | CheckValue(BilledCost, 0) | CheckNotSameValue(ProviderName, InvoiceIssuerName) | Static | 1.2 | active |
| BilledCost-C-006-M | Validation | BilledCost |  | MUST be denominated in the BillingCurrency | MUST |  |  | Dynamic | 1.2 | active |
| BilledCost-C-007-M | Validation | BilledCost |  | SUM(BilledCost) MUST equal payable amount in invoice from InvoiceIssuer | MUST |  |  | Dynamic | 1.2 | active |
| ListUnitPrice-C-000-C | Composite | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED |  | MUST | AND of [Check ListUnitPrice-C-001-C, Check ListUnitPrice-C-002-M, Check ListUnitPrice-C-003-M, Check ListUnitPrice-C-004-C, Check ListUnitPrice-C-005-C, Check ListUnitPrice-C-008-C, Check ListUnitPrice-C-009-C, Check ListUnitPrice-C-010-C, Check ListUnitPrice-C-011-M, Check ListUnitPrice-C-012-C] |  | Static | 1.2 | active |
| ListUnitPrice-C-001-C | Presence | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED | MUST be present in a FOCUS dataset when the data generator publishes unit prices exclusive of discounts | MUST | ColumnPresent(ListUnitPrice) |  | Static | 1.2 | active |
| ListUnitPrice-C-002-M | Type | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED | MUST be of type Decimal | MUST | TypeDecimal(ListUnitPrice) |  | Static | 1.2 | active |
| ListUnitPrice-C-003-M | Format | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED | MUST conform to NumericFormat requirements | MUST | FormatNumeric(ListUnitPrice) |  | Static | 1.2 | active |
| ListUnitPrice-C-004-C | Validation | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED | MUST be null when ChargeCategory is 'Tax' | MUST | CheckValue(ListUnitPrice, null) | CheckValue(ChargeCategory, Tax) | Static | 1.2 | active |
| ListUnitPrice-C-005-C | Composite | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED | when ChargeCategory is 'Usage' or 'Purchase' | MUST | AND of [Check ListUnitPrice-C-006-C, Check ListUnitPrice-C-007-O] | OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)] | Static | 1.2 | active |
| ListUnitPrice-C-006-C | Validation | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED | MUST NOT be null when ChargeCategory is 'Usage' or 'Purchase' and ChargeClass is not 'Correction' | MUST | CheckNotValue(ListUnitPrice, null) | CheckNotValue(ChargeClass, Correction) | Static | 1.2 | active |
| ListUnitPrice-C-007-O | Validation | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED | MAY be null in all other cases | MAY |  |  | Static | 1.2 | active |
| ListUnitPrice-C-008-C | Composite | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED | When ListUnitPrice is not null | MUST | AND of [Check ListUnitPrice-C-009-C, Check ListUnitPrice-C-010-C, Check ListUnitPrice-C-011-M] | CheckNotValue(ListUnitPrice, null) | Static | 1.2 | active |
| ListUnitPrice-C-009-C | Validation | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED | MUST be a non-negative decimal value | MUST | CheckGreaterOrEqualThanValue(ListUnitPrice, 0) |  | Static | 1.2 | active |
| ListUnitPrice-C-010-C | Validation | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED | MUST be denominated in the BillingCurrency | MUST |  |  | Dynamic | 1.2 | active |
| ListUnitPrice-C-011-M | Format | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED | The product of ListUnitPrice and PricingQuantity MUST match the ListCost when PricingQuantity is not null and ChargeClass is not 'Correction' | MUST | ColumnByColumnEqualsColumnValue(ListUnitPrice, PricingQuantity) -> ListCost | AND of [CheckNotValue(ListUnitPrice, null), CheckNotValue(ChargeClass, Correction)] | Static | 1.2 | active |
| ListUnitPrice-C-012-C | Validation | ListUnitPrice | PUBLIC_PRICE_LIST_SUPPORTED | Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY exist when ChargeClass 'Correction' | MAY |  | CheckValue(ChargeClass, Correction) | Dynamic | 1.2 | active |
