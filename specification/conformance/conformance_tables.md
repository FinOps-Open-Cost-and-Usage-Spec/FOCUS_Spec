# Conformance Table: FOCUS

| ConformanceRuleId | Function | Status | ApplicabilityCriteria | Type | mustSatisfy | Requirement | Condition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BilledCost-C-000-M | Presence | active |  | Static |  | AND of [Check BilledCost-C-001-M, Check BilledCost-C-002-M, Check BilledCost-C-003-M, Check BilledCost-C-004-M, Check BilledCost-C-005-M, Check BilledCost-C-006-M, Check BilledCost-C-007-M] |  |
| BilledCost-C-001-M | Presence | active |  | Static | MUST be present in a FOCUS dataset | ColumnPresent(BilledCost) |  |
| BilledCost-C-002-M | Validation | active |  | Static | MUST NOT be null | CheckNotValue(BilledCost) |  |
| BilledCost-C-003-M | Type | active |  | Static | MUST be of type Decimal | TypeDecimal(BilledCost) |  |
| BilledCost-C-004-M | Format | active |  | Static | MUST conform to NumericFormat requirements | FormatNumeric(BilledCost) |  |
| BilledCost-C-005-M | Validation | active |  | Static | MUST be 0 for charges where payments are received by a third party | CheckValue(BilledCost, 0) | CheckNotSameValue(ProviderName, InvoiceIssuerName) |
| BilledCost-C-006-M | Validation | active |  | Dynamic | MUST be denominated in the BillingCurrency |  |  |
| BilledCost-C-007-M | Validation | active |  | Dynamic | SUM(BilledCost) MUST equal payable amount in invoice from InvoiceIssuer |  |  |
| ListUnitPrice-C-000-C | Composite | active | PUBLIC_PRICE_LIST_SUPPORTED | Static |  | AND of [Check ListUnitPrice-C-001-C, Check ListUnitPrice-C-002-M, Check ListUnitPrice-C-003-M, Check ListUnitPrice-C-004-C, Check ListUnitPrice-C-005-C, Check ListUnitPrice-C-008-C, Check ListUnitPrice-C-009-C, Check ListUnitPrice-C-010-M, Check ListUnitPrice-C-011-C] |  |
| ListUnitPrice-C-001-C | Presence | active | PUBLIC_PRICE_LIST_SUPPORTED | Static | MUST be present in a FOCUS dataset when the data generator publishes unit prices exclusive of discounts | ColumnPresent(ListUnitPrice) |  |
| ListUnitPrice-C-002-M | Type | active | PUBLIC_PRICE_LIST_SUPPORTED | Static | MUST be of type Decimal | TypeDecimal(ListUnitPrice) |  |
| ListUnitPrice-C-003-M | Format | active | PUBLIC_PRICE_LIST_SUPPORTED | Static | MUST conform to NumericFormat requirements | FormatNumeric(ListUnitPrice) |  |
| ListUnitPrice-C-004-C | Validation | active | PUBLIC_PRICE_LIST_SUPPORTED | Static | MUST be null when ChargeCategory is 'Tax' | CheckValue(ListUnitPrice) | CheckValue(ChargeCategory, Tax) |
| ListUnitPrice-C-005-C | Composite | active | PUBLIC_PRICE_LIST_SUPPORTED | Static | when ChargeCategory is 'Usage' or 'Purchase' | AND of [Check ListUnitPrice-C-006-C, Check ListUnitPrice-C-007-O] | OR of [CheckValue(ChargeCategory, Usage), CheckValue(ChargeCategory, Purchase)] |
| ListUnitPrice-C-006-C | Validation | active | PUBLIC_PRICE_LIST_SUPPORTED | Static | MUST NOT be null when ChargeCategory is 'Usage' or 'Purchase' and ChargeClass is not 'Correction' | CheckNotValue(ListUnitPrice) | CheckNotValue(ChargeClass, Correction) |
| ListUnitPrice-C-007-O | Validation | active | PUBLIC_PRICE_LIST_SUPPORTED | Static | MAY be null in all other cases |  |  |
| ListUnitPrice-C-008-C | Validation | active | PUBLIC_PRICE_LIST_SUPPORTED | Static | MUST be a non-negative decimal value, when ListUnitPrice is not null | CheckGreaterOrEqualThanValue(ListUnitPrice, 0) | CheckNotValue(ListUnitPrice) |
| ListUnitPrice-C-009-C | Validation | active | PUBLIC_PRICE_LIST_SUPPORTED | Dynamic | MUST be denominated in the BillingCurrency |  |  |
| ListUnitPrice-C-010-M | Format | active | PUBLIC_PRICE_LIST_SUPPORTED | Static | MUST conform to NumericFormat requirements | ColumnByColumnEqualsColumnValue(ListUnitPrice, PricingQuantity) | AND of [CheckNotValue(ListUnitPrice), CheckNotValue(ChargeClass, Correction)] |
| ListUnitPrice-C-011-C | Validation | active | PUBLIC_PRICE_LIST_SUPPORTED | Dynamic | DiConformanceRuleIdepancies MAY exist when ChargeClass is 'Correction' |  | CheckValue(ChargeClass, Correction) |