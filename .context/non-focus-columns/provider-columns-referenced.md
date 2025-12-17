# Provider Columns Referenced in FOCUS Repo

> Consolidated list of provider-native columns mentioned in the FOCUS repository.
> This list supports issue #1634 by documenting columns already in discussion.

---

## Summary

This document captures provider columns **explicitly referenced in the FOCUS repo**. It is NOT a comprehensive list of all native columns - providers have many more columns not yet referenced. It's important to note that referenced native columns are generally only included when related to FOCUS columns. This is not representative of all native columns practitioners need.

| Category | Count |
|----------|-------|
| Native columns referenced WITHOUT direct FOCUS mapping | ~20 |
| FOCUS columns providers CAN'T populate | ~15 |
| Native columns referenced that MAP to FOCUS | ~100 |

---

## Native Columns Without Direct FOCUS Mapping

These columns ARE in provider billing exports but do NOT have a 1:1 FOCUS equivalent. They're either "close" mappings or have no FOCUS coverage at all.

### AWS CUR

| Native Column | Context | Source |
|---------------|---------|--------|
| `lineItem/LegalEntity` | Closest to PublisherName but "not equivalent to a publisher" | publishername.md |
| `bill/BillingEntity` | Closest to ProviderName; values: AWS, AWS Marketplace | providername.md |
| `reservation/UnusedQuantity` | Used for utilization calculations | commitmentdiscountquantity.md |
| `reservation/TotalReservedUnits` | For size-flexible Reserved Instances | commitmentdiscountquantity.md |
| `savingsPlan/UsedCommitment` | For Savings Plan utilization | commitmentdiscountquantity.md |
| `savingsPlan/TotalCommitmentToDate` | For Savings Plan utilization | commitmentdiscountquantity.md |
| `costCategories/*` | Custom cost groupings | tags.md, #1030 |
| `commitment_quantity` | Amount committed (proposed, not in CUR today) | #1041 |
| `commitment_start_time` | When commitment begins (proposed) | #1041 |
| `commitment_end_time` | When commitment expires (proposed) | #1041 |
| `commitment_period` | Duration/term (proposed) | #1041 |
| `commitment_name` | Human-readable name (proposed) | #1041 |
| `commitment_convertible` | Whether convertible Y/N (proposed) | #1041 |
| Billing Conductor data | Different structure from official CUR files | #1030 |

### GCP BigQuery Billing Export

| Native Column | Context | Source |
|---------------|---------|--------|
| `product_taxonomy` | Contains publisher info but not in consistent location | publishername.md |
| `business_entity_name` | Requires join with pricing export on `sku.id` for ProviderName | providername.md |
| `credit.type` | Values: COMMITTED_USAGE_DISCOUNT, COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE | commitmentdiscountcategory.md |
| `system_labels` | System-defined labels | tags.md |

### Microsoft Azure Cost Details

| Native Column | Context | Source |
|---------------|---------|--------|
| `PublisherType` / `x_PublisherCategory` | Related to ProviderName but not equivalent | providername.md |
| `Provider` | Only available in Management group data | providername.md |
| `ServiceFamily` / `x_SkuServiceFamily` | Close to ServiceCategory but based on usage | servicecategory.md |

### OCI Cost Reports

| Native Column | Context | Source |
|---------------|---------|--------|
| `cost/unitPriceOverage` | Overage unit price; separate from `cost/unitPrice` | contractedunitprice.md |
| `usage/billedQuantityOverage` | Overage quantity; separate from `usage/billedQuantity` | pricingquantity.md |

---

## FOCUS Columns Without Provider Data

These are FOCUS columns that providers cannot populate from their native billing exports. This is the inverse problem - not directly relevant to "include all native data" but useful context.

| FOCUS Column | Provider | Notes | Source |
|--------------|----------|-------|--------|
| SubAccountName | AWS | Not in CUR; requires Organizations API | subaccountname.md |
| SubAccountName | OCI | Requires OrganizationTenancy API | subaccountname.md |
| ResourceName | AWS | Not separate column; sometimes in ARN | resourcename.md |
| ResourceName | GCP | Not separate column; in `resource.global_name` | resourcename.md |
| ResourceName | OCI | Not present; closest is `product/resourceId` | resourcename.md |
| ResourceType | GCP | Does not exist | resourcetype.md |
| AvailabilityZone | Microsoft | Not available | availabilityzone.md |
| ContractedCost | AWS | Not available | contractedcost.md |
| ContractedUnitPrice | AWS | Not available | contractedunitprice.md |
| ListUnitPrice | GCP | Not in Billing Export; requires Pricing Data Export | listunitprice.md |
| ListUnitPrice | OCI | Requires List Pricing REST API | listunitprice.md |
| PricingCurrency | AWS, GCP, OCI | n/a | pricingcurrency.md |
| SkuPriceId | OCI | Not available (no price level ID) | skupriceid.md |
| SkuMeter | OCI | TBD (not mapped) | skumeter.md |
| CommitmentDiscountQuantity | GCP, Microsoft | Not available | commitmentdiscountquantity.md |

---

## Provider Columns That Map TO FOCUS

These are documented mappings - native columns that ARE covered by FOCUS:

### AWS CUR → FOCUS Mappings

| AWS Column | FOCUS Column | Source |
|------------|--------------|--------|
| `lineItem/AvailabilityZone` | AvailabilityZone | availabilityzone.md |
| `bill_payer_account_id` | BillingAccountId | billingaccountid.md |
| `CurrencyCode` | BillingCurrency | billingcurrency.md |
| `bill/BillingPeriodStartDate` | BillingPeriodStart | billingperiodstart.md |
| `bill/BillingPeriodEndDate` | BillingPeriodEnd | billingperiodend.md |
| `lineItem/NetUnblendedCost` | BilledCost | billedcost.md |
| `line_item_unblended_cost` | BilledCost (if no EDP) | billedcost.md |
| `bill/BillType` | ChargeCategory, ChargeFrequency | chargecategory.md |
| `lineItem/LineItemType` | ChargeCategory, CommitmentDiscountStatus | chargecategory.md |
| `lineItem/LineItemDescription` | ChargeDescription | chargedescription.md |
| `line_item_usage_start_date` | ChargePeriodStart | chargeperiod.md |
| `line_item_usage_end_date` | ChargePeriodEnd | chargeperiod.md |
| `reservation/ReservationARN` | CommitmentDiscountId | commitmentdiscountid.md |
| `savingsPlan/SavingsPlanArn` | CommitmentDiscountId | commitmentdiscountid.md |
| `lineItem/UsageAmount` | ConsumedQuantity, PricingQuantity | consumedquantity.md |
| `bill/InvoicingEntity` | InvoiceIssuerName | invoiceissuername.md |
| `pricing/publicOnDemandCost` | ListCost | listcost.md |
| `pricing/publicOnDemandRate` | ListUnitPrice | listunitprice.md |
| `product/PurchaseOption` | PricingCategory | pricingcategory.md |
| `pricing/unit` | PricingUnit, ConsumedUnit | pricingunit.md |
| `Product_region` | RegionId | regionid.md |
| `line_item_resource_id` | ResourceId | resourceid.md |
| `lineItem/ResourceId` | ResourceId, ResourceType | resourceid.md |
| `line_item_product_code` | ServiceName | servicename.md |
| `product/sku` | SkuId | skuid.md |
| `line_item_usage_type` | SkuMeter | skumeter.md |
| `pricing/rate_code`, `pricing/rate_id` | SkuPriceId | skupriceid.md |
| `lineItem/UsageAccountId` | SubAccountId | subaccountid.md |
| `resourceTags/user:*` | Tags | tags.md |

### GCP BigQuery → FOCUS Mappings

| GCP Column | FOCUS Column | Source |
|------------|--------------|--------|
| `location.zone` | AvailabilityZone | availabilityzone.md |
| `billing_account_id` | BillingAccountId | billingaccountid.md |
| `Currency` | BillingCurrency | billingcurrency.md |
| `invoice.month` | BillingPeriodStart/End | billingperiodstart.md |
| `credits` + `cost` | BilledCost | billedcost.md |
| `Cost type` | ChargeCategory | chargecategory.md |
| `sku.description` | ChargeDescription | chargedescription.md |
| `usage_start_time` | ChargePeriodStart | chargeperiod.md |
| `usage_end_time` | ChargePeriodEnd | chargeperiod.md |
| `credits.id` | CommitmentDiscountId, CommitmentDiscountType | commitmentdiscountid.md |
| `credits.full_name` | CommitmentDiscountName | commitmentdiscountname.md |
| `usage.amount` | ConsumedQuantity | consumedquantity.md |
| `usage.unit` | ConsumedUnit | consumedunit.md |
| `cost` | ContractedCost | contractedcost.md |
| `usage.amount_in_pricing_units` | PricingQuantity | pricingquantity.md |
| `usage.pricing_unit` | PricingUnit | pricingunit.md |
| `Location.location` | RegionId | regionid.md |
| `resource.global_name` | ResourceId | resourceid.md |
| `service.description` | ServiceName, SkuMeter | servicename.md |
| `sku.id` | SkuId, SkuPriceId (derived) | skuid.md |
| `project.id` | SubAccountId | subaccountid.md |
| `project.name` | SubAccountName | subaccountname.md |
| `tags`, `labels`, `project.labels` | Tags | tags.md |

### Microsoft Azure → FOCUS Mappings

| Azure Column | FOCUS Column | Source |
|--------------|--------------|--------|
| `BillingAccountId` (EA) | BillingAccountId | billingaccountid.md |
| `BillingProfileId` (MCA) | BillingAccountId | billingaccountid.md |
| `SubscriptionId` (MOSA) | BillingAccountId | billingaccountid.md |
| `BillingAccountName` (EA) | BillingAccountName | billingaccountname.md |
| `BillingProfileName` (MCA) | BillingAccountName | billingaccountname.md |
| `BillingCurrency` (EA) | BillingCurrency | billingcurrency.md |
| `BillingPeriodStartDate` | BillingPeriodStart | billingperiodstart.md |
| `BillingPeriodEndDate` | BillingPeriodEnd | billingperiodend.md |
| `Cost`, `CostInBillingCurrency` | BilledCost | billedcost.md |
| `ChargeType` | ChargeCategory, CommitmentDiscountStatus | chargecategory.md |
| `PricingModel` | ChargeCategory, PricingCategory | chargecategory.md |
| `Frequency` | ChargeCategory, ChargeFrequency | chargefrequency.md |
| `ProductName` | ChargeDescription | chargedescription.md |
| `date` | ChargePeriodStart/End | chargeperiod.md |
| `ReservationId` / `BenefitId` | CommitmentDiscountId | commitmentdiscountid.md |
| `ReservationName` / `BenefitName` | CommitmentDiscountName | commitmentdiscountname.md |
| `UnitOfMeasure` | ConsumedUnit, PricingUnit | consumedunit.md |
| `quantity` | ConsumedQuantity | consumedquantity.md |
| `UnitPrice` | ContractedUnitPrice | contractedunitprice.md |
| `pay-as-you-goPrice` / `PayGPrice` | ListUnitPrice | listunitprice.md |
| `PricingCurrency` | PricingCurrency | pricingcurrency.md |
| `ResourceLocation` | RegionId | regionid.md |
| `ResourceId` | ResourceId | resourceid.md |
| `ResourceType` | ResourceType | resourcetype.md |
| `ResourceName` | ResourceName | resourcename.md |
| `ConsumedService`, `ServiceName`, `MeterCategory` | ServiceName | servicename.md |
| `PartNumber` | SkuId | skuid.md |
| `MeterName` | SkuMeter | skumeter.md |
| `SubscriptionGuid` | SubAccountId | subaccountid.md |
| `SubscriptionName` | SubAccountName | subaccountname.md |
| `PublisherName` | PublisherName | publishername.md |
| `Tags` | Tags | tags.md |

### OCI Cost Reports → FOCUS Mappings

| OCI Column | FOCUS Column | Source |
|------------|--------------|--------|
| `product/availabilityDomain` | AvailabilityZone | availabilityzone.md |
| `cost/subscriptionId` | BillingAccountId | billingaccountid.md |
| `cost/currencyCode` | BillingCurrency | billingcurrency.md |
| `cost/myCostOverage` | BilledCost | billedcost.md |
| `lineItem/intervalUsageStart` | ChargePeriodStart | chargeperiod.md |
| `lineItem/intervalUsageEnd` | ChargePeriodEnd | chargeperiod.md |
| `cost/myCost` | ContractedCost | contractedcost.md |
| `cost/unitPrice` | ContractedUnitPrice | contractedunitprice.md |
| `usage/billedQuantity` | PricingQuantity | pricingquantity.md |
| `cost/billingUnitReadable` | PricingUnit | pricingunit.md |
| `product/region` | RegionId | regionid.md |
| `product/resourceId` | ResourceId | resourceid.md |
| `product/service` | ServiceName | servicename.md |
| `cost/productSku` | SkuId | skuid.md |
| `lineItem/tenantId` | SubAccountId | subaccountid.md |
| `tags/*` | Tags | tags.md |

---

## Sources Searched

- `supporting_content/datasets/cost_and_usage/columns/*.md` (53 files)
- `supporting_content/attributes/*.md`
- GitHub issues: #1030 (JSON column), #1041 (commitment columns), #1094 (completeness FR)

## Not Yet Searched

- [ ] Google Drive documents
- [ ] Deep dive into all GitHub issues for specific column mentions
