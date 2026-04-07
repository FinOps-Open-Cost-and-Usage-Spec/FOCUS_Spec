## Diff

ContractCommitment [-adheres-]{+MUST adhere+} to the following requirements:

* ContractCommitment MUST be present when the service provider supports *contract commitments*.
* ContractCommitment {+column presence MUST adhere to the following requirements:+}
{+  * ContractCommitment MUST include [BillingCurrency](#datasets.contractcommitment.billingcurrency).+}
{+  * ContractCommitment MUST include [ContractCommitmentApplicability](#datasets.contractcommitment.contractcommitmentapplicability).+}
{+  * ContractCommitment MUST include [ContractCommitmentBenefitCategory](#datasets.contractcommitment.contractcommitmentbenefitcategory).+}
{+  * ContractCommitment MUST include [ContractCommitmentCategory](#datasets.contractcommitment.contractcommitmentcategory).+}
{+  * ContractCommitment MUST include [ContractCommitmentCost](#datasets.contractcommitment.contractcommitmentcost).+}
{+  * ContractCommitment MUST include [ContractCommitmentCreated](#datasets.contractcommitment.contractcommitmentcreated).+}
{+  * ContractCommitment MUST include [ContractCommitmentDescription](#datasets.contractcommitment.contractcommitmentdescription).+}
{+  * ContractCommitment MUST include [ContractCommitmentDiscountPercentage](#datasets.contractcommitment.contractcommitmentdiscountpercentage).+}
{+  * ContractCommitment MUST include [ContractCommitmentDurationType](#datasets.contractcommitment.contractcommitmentdurationtype).+}
{+  * ContractCommitment MUST include [ContractCommitmentFulfillmentInterval](#datasets.contractcommitment.contractcommitmentfulfillmentinterval).+}
{+  * ContractCommitment MUST include [ContractCommitmentId](#datasets.contractcommitment.contractcommitmentid).+}
{+  * ContractCommitment MUST include [ContractCommitmentLastUpdated](#datasets.contractcommitment.contractcommitmentlastupdated).+}
{+  * ContractCommitment MUST include [ContractCommitmentLifecycleStatus](#datasets.contractcommitment.contractcommitmentlifecyclestatus).+}
{+  * ContractCommitment MUST include [ContractCommitmentModel](#datasets.contractcommitment.contractcommitmentmodel).+}
{+  * ContractCommitment MUST include [ContractCommitmentOfferCategory](#datasets.contractcommitment.contractcommitmentoffercategory).+}
{+  * ContractCommitment MUST include [ContractCommitmentPaymentInterval](#datasets.contractcommitment.contractcommitmentpaymentinterval).+}
{+  * ContractCommitment MUST include [ContractCommitmentPaymentModel](#datasets.contractcommitment.contractcommitmentpaymentmodel).+}
{+  * ContractCommitment MUST include [ContractCommitmentPaymentUpfrontPercentage](#datasets.contractcommitment.contractcommitmentpaymentupfrontpercentage) if the service provider offers "Partial Upfront" [payment models](#datasets.contractcommitment.contractcommitmentpaymentmodel).+}
{+  * ContractCommitment MUST include [ContractCommitmentPeriodEnd](#datasets.contractcommitment.contractcommitmentperiodend).+}
{+  * ContractCommitment MUST include [ContractCommitmentPeriodStart](#datasets.contractcommitment.contractcommitmentperiodstart).+}
{+  * ContractCommitment MUST include [ContractCommitmentQuantity](#datasets.contractcommitment.contractcommitmentquantity).+}
{+  * ContractCommitment MUST include [ContractCommitmentType](#datasets.contractcommitment.contractcommitmenttype).+}
{+  * ContractCommitment MUST include [ContractCommitmentUnit](#datasets.contractcommitment.contractcommitmentunit).+}
{+  * ContractCommitment MUST include [ContractId](#datasets.contractcommitment.contractid).+}
{+  * ContractCommitment MUST include [ContractPeriodEnd](#datasets.contractcommitment.contractperiodend).+}
{+  * ContractCommitment MUST include [ContractPeriodStart](#datasets.contractcommitment.contractperiodstart).+}
{+  * ContractCommitment MUST include [InvoiceIssuerName](#datasets.contractcommitment.invoiceissuername).+}
{+  * ContractCommitment MUST include [PricingCurrency](#datasets.contractcommitment.pricingcurrency) when the service provider supports pricing and billing in different currencies.+}
{+  * ContractCommitment MUST include [PricingCurrencyContractCommitmentCost](#datasets.contractcommitment.pricingcurrencycontractcommitmentcost) when the service provider supports pricing and billing in different currencies.+}
{+  * ContractCommitment MUST include [ServiceProviderName](#datasets.contractcommitment.serviceprovidername).+}
{+* ContractCommitment MUST conform to [ColumnHandling](#attributes.columnhandling) requirements.+}
{+* ContractCommitment MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.+}
{+* ContractCommitment+} MUST conform to [-[ColumnHandling](#columnhandling)-]{+[NullHandling](#attributes.nullhandling)+} requirements.
* ContractCommitment MUST conform to [-[NullHandling](#nullhandling)-]{+[DatasetConfiguration](#attributes.datasetconfiguration)+} requirements.