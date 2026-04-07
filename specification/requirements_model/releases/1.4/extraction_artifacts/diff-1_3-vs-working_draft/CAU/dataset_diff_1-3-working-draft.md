## Diff

CostAndUsage [-adheres-]{+MUST adhere+} to the following requirements:

* CostAndUsage MUST be present.
* CostAndUsage {+column presence MUST adhere to the following requirements:+}
{+  * CostAndUsage SHOULD include [AllocatedMethodDetails](#datasets.costandusage.allocatedmethoddetails) when the data generator supports [Data Generator-Calculated Split Cost Allocation](#datagenerator-calculatedsplitcostallocationhandling).+}
{+  * CostAndUsage MUST include [AllocatedMethodId](#datasets.costandusage.allocatedmethodid) when the data generator supports [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling).+}
{+  * CostAndUsage MUST include [AllocatedResourceId](#datasets.costandusage.allocatedresourceid) when the data generator supports [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling).+}
{+  * CostAndUsage MUST include [AllocatedResourceName](#datasets.costandusage.allocatedresourcename) when the data generator supports [Data Generator-Calculated Split Cost Allocation](#attributes.datagenerator-calculatedsplitcostallocationhandling).+}
{+  * CostAndUsage MUST include [AllocatedTags](#datasets.costandusage.allocatedtags) when the service provider supports [Data Generator-Calculated Split Cost Allocation](#datagenerator-calculatedsplitcostallocationhandling).+}
{+  * CostAndUsage SHOULD include [AvailabilityZone](#datasets.costandusage.availabilityzone) when the host provider supports deploying resources or services within an *availability zone*.+}
{+  * CostAndUsage MUST include [BilledCost](#datasets.costandusage.billedcost).+}
{+  * CostAndUsage MUST include [BillingAccountId](#datasets.costandusage.billingaccountid).+}
{+  * CostAndUsage MUST include [BillingAccountName](#datasets.costandusage.billingaccountname).+}
{+  * CostAndUsage MUST include [BillingAccountType](#datasets.costandusage.billingaccounttype) when the invoice issuer supports more than one possible BillingAccountType value.+}
{+  * CostAndUsage MUST include [BillingCurrency](#datasets.costandusage.billingcurrency).+}
{+  * CostAndUsage MUST include [BillingPeriodEnd](#datasets.costandusage.billingperiodend).+}
{+  * CostAndUsage MUST include [BillingPeriodStart](#datasets.costandusage.billingperiodstart).+}
{+  * CostAndUsage MUST include [CapacityReservationId](#datasets.costandusage.capacityreservationid) when the service provider supports *capacity reservations*.+}
{+  * CostAndUsage MUST include [CapacityReservationStatus](#datasets.costandusage.capacityreservationstatus) when the service provider supports *capacity reservations*.+}
{+  * CostAndUsage MUST include [ChargeCategory](#datasets.costandusage.chargecategory).+}
{+  * CostAndUsage MUST include [ChargeClass](#datasets.costandusage.chargeclass).+}
{+  * CostAndUsage MUST include [ChargeDescription](#datasets.costandusage.chargedescription).+}
{+  * CostAndUsage SHOULD include [ChargeFrequency](#datasets.costandusage.chargefrequency).+}
{+  * CostAndUsage MUST include [ChargePeriodEnd](#datasets.costandusage.chargeperiodend).+}
{+  * CostAndUsage MUST include [ChargePeriodStart](#datasets.costandusage.chargeperiodstart).+}
{+  * CostAndUsage MUST include [CommitmentDiscountCategory](#datasets.costandusage.commitmentdiscountcategory) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [CommitmentDiscountName](#datasets.costandusage.commitmentdiscountname) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [CommitmentDiscountQuantity](#datasets.costandusage.commitmentdiscountquantity) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [CommitmentDiscountUnit](#datasets.costandusage.commitmentdiscountunit) when the service provider supports *commitment discounts*.+}
{+  * CostAndUsage MUST include [ConsumedQuantity](#datasets.costandusage.consumedquantity) when the service provider supports the measurement of usage.+}
{+  * CostAndUsage MUST include [ConsumedUnit](#datasets.costandusage.consumedunit) when the service provider supports the measurement of usage.+}
{+  * CostAndUsage MUST include [ContractApplied](#datasets.costandusage.contractapplied) when the service provider supports *contract commitments*.+}
{+  * CostAndUsage MUST include [ContractedCost](#datasets.costandusage.contractedcost).+}
{+  * CostAndUsage MUST include [ContractedUnitPrice](#datasets.costandusage.contractedunitprice) when the service provider supports negotiated pricing concepts.+}
{+  * CostAndUsage MUST include [EffectiveCost](#datasets.costandusage.effectivecost).+}
{+  * CostAndUsage MUST include [HostProviderName](#datasets.costandusage.hostprovidername).+}
{+  * CostAndUsage MUST include [InvoiceDetailId](#datasets.costandusage.invoicedetailid).+}
{+  * CostAndUsage MUST include [InvoiceId](#datasets.costandusage.invoiceid).+}
{+  * CostAndUsage MUST include [InvoiceIssuerName](#datasets.costandusage.invoiceissuername).+}
{+  * CostAndUsage MUST include [ListCost](#datasets.costandusage.listcost).+}
{+  * CostAndUsage MUST include [ListUnitPrice](#datasets.costandusage.listunitprice) when the service provider publishes unit prices exclusive of discounts.+}
{+  * CostAndUsage MUST include [PricingCategory](#datasets.costandusage.pricingcategory) when the service provider supports more than one pricing category across all [*SKUs*](#glossary:sku).+}
{+  * CostAndUsage MUST include [PricingCurrency](#datasets.costandusage.pricingcurrency) when the service provider supports pricing and billing in different currencies.+}
{+  * CostAndUsage MUST include [PricingCurrencyContractedUnitPrice](#datasets.costandusage.pricingcurrencycontractedunitprice) when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.+}
{+  * CostAndUsage MUST include [PricingCurrencyEffectiveCost](#datasets.costandusage.pricingcurrencyeffectivecost) when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.+}
{+  * CostAndUsage MUST include [PricingCurrencyListUnitPrice](#datasets.costandusage.pricingcurrencylistunitprice) when the service provider supports prices in virtual currency and publishes unit prices exclusive of discounts.+}
{+  * CostAndUsage MUST include [PricingQuantity](#datasets.costandusage.pricingquantity).+}
{+  * CostAndUsage MUST include [PricingUnit](#datasets.costandusage.pricingunit).+}
{+  * CostAndUsage MUST include [RegionId](#datasets.costandusage.regionid) when the host provider supports deploying resources or services within a region.+}
{+  * CostAndUsage MUST include [RegionName](#datasets.costandusage.regionname) when the host provider supports deploying resources or services within a region.+}
{+  * CostAndUsage MUST include [ResourceId](#datasets.costandusage.resourceid) when the service provider supports billing based on provisioned *resources*.+}
{+  * CostAndUsage MUST include [ResourceName](#datasets.costandusage.resourcename) when the service provider supports billing based on provisioned resources.+}
{+  * CostAndUsage MUST include [ResourceType](#datasets.costandusage.resourcetype) when the service provider supports billing based on provisioned *resources* and supports assigning types to *resources*.+}
{+  * CostAndUsage MUST include [ServiceCategory](#datasets.costandusage.servicecategory).+}
{+  * CostAndUsage MUST include [ServiceName](#datasets.costandusage.servicename).+}
{+  * CostAndUsage MUST include [ServiceProviderName](#datasets.costandusage.serviceprovidername).+}
{+  * CostAndUsage SHOULD include [ServiceSubcategory](#datasets.costandusage.servicesubcategory).+}
{+  * CostAndUsage MUST include [SkuId](#datasets.costandusage.skuid) when the service provider supports unit pricing concepts and publishes price lists, publicly or as part of contracting.+}
{+  * CostAndUsage MUST include [SkuMeter](#datasets.costandusage.skumeter) when the service provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.+}
{+  * CostAndUsage MUST include [SkuPriceDetails](#datasets.costandusage.skupricedetails) when the service provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.+}
{+  * CostAndUsage MUST include [SkuPriceId](#datasets.costandusage.skupriceid) when the service provider supports unit pricing concepts and publishes *price lists*, publicly or as part of contracting.+}
{+  * CostAndUsage MUST include [SubAccountId](#datasets.costandusage.subaccountid) when the service provider supports a *sub account* construct.+}
{+  * CostAndUsage MUST include [SubAccountName](#datasets.costandusage.subaccountname) when the service provider supports a *sub account* construct.+}
{+  * CostAndUsage MUST include [SubAccountType](#datasets.costandusage.subaccounttype) when the service provider supports more than one possible SubAccountType value.+}
{+  * CostAndUsage MUST include [Tags](#datasets.costandusage.tags) when the data generator supports setting user or provider-defined tags.+}
{+* CostAndUsage MUST conform to [ColumnHandling](#attributes.columnhandling) requirements.+}
{+* CostAndUsage MUST conform to [NullHandling](#attributes.nullhandling) requirements.+}
{+* CostAndUsage+} MUST conform to [-[ColumnHandling](#columnhandling)-]{+[DiscountHandling](#attributes.discounthandling)+} requirements.
* CostAndUsage MUST conform to [-[NullHandling](#nullhandling)-]{+[InvoiceHandling](#attributes.invoicehandling)+} requirements.
* CostAndUsage MUST conform to [-[DiscountHandling](#discounthandling)-]{+[DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling)+} requirements.
* CostAndUsage MUST conform to [-[InvoiceHandling](#invoicehandling)-]{+[DatasetCompleteness](#attributes.datasetcompleteness)+} requirements.
* CostAndUsage MUST conform to [-[DataGeneratorCalculatedSplitCostAllocationHandling](#datagenerator-calculatedsplitcostallocationhandling)-]{+[DatasetConfiguration](#attributes.datasetconfiguration)+} requirements.