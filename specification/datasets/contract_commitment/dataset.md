# Contract Commitment

The Contract Commitment dataset is a supporting dataset that describes the terms of contracts agreed between a service provider and a customer.

## Columns<!--SkipTOC-->

| Column | Column Type | Feature Level | Allows Nulls | Data Type |
| :--- | :--- | :--- | :--- | :--- |
| [Billing Currency](#datamodel.contractcommitment.billingcurrency) | Dimension | Mandatory | True | String |
| [Contract Commitment Applicability](#datamodel.contractcommitment.contractcommitmentapplicability) | Dimension / Metric | Mandatory | False | JSON |
| [Contract Commitment Benefit Category](#datamodel.contractcommitment.contractcommitmentbenefitcategory) | Dimension | Mandatory | False | String |
| [Contract Commitment Category](#datamodel.contractcommitment.contractcommitmentcategory) | Dimension | Mandatory | False | String |
| [Contract Commitment Cost](#datamodel.contractcommitment.contractcommitmentcost) | Metric | Mandatory | True | Decimal |
| [Contract Commitment Created](#datamodel.contractcommitment.contractcommitmentcreated) | Dimension | Mandatory | False | Date/Time |
| [Contract Commitment Description](#datamodel.contractcommitment.contractcommitmentdescription) | Dimension | Mandatory | True | String |
| [Contract Commitment Discount Percentage](#datamodel.contractcommitment.contractcommitmentdiscountpercentage) | Metric | Mandatory | True | Decimal |
| [Contract Commitment Duration Type](#datamodel.contractcommitment.contractcommitmentdurationtype) | Dimension | Mandatory | False | String |
| [Contract Commitment Fulfillment Interval](#datamodel.contractcommitment.contractcommitmentfulfillmentinterval) | Dimension | Mandatory | False | String |
| [Contract Commitment ID](#datamodel.contractcommitment.contractcommitmentid) | Dimension | Mandatory | False | String |
| [Contract Commitment Last Updated](#datamodel.contractcommitment.contractcommitmentlastupdated) | Dimension | Mandatory | False | Date/Time |
| [Contract Commitment Lifecycle Status](#datamodel.contractcommitment.contractcommitmentlifecyclestatus) | Dimension | Mandatory | False | String |
| [Contract Commitment Model](#datamodel.contractcommitment.contractcommitmentmodel) | Dimension | Mandatory | False | String |
| [Contract Commitment Offer Category](#datamodel.contractcommitment.contractcommitmentoffercategory) | Dimension | Mandatory | False | String |
| [Contract Commitment Payment Interval](#datamodel.contractcommitment.contractcommitmentpaymentinterval) | Dimension | Mandatory | False | String |
| [Contract Commitment Payment Model](#datamodel.contractcommitment.contractcommitmentpaymentmodel) | Dimension | Mandatory | False | String |
| [Contract Commitment Payment Upfront Percentage](#datamodel.contractcommitment.contractcommitmentpaymentupfrontpercentage) | Metric | Conditional | False | Decimal |
| [Contract Commitment Period End](#datamodel.contractcommitment.contractcommitmentperiodend) | Dimension | Mandatory | False | Date/Time |
| [Contract Commitment Period Start](#datamodel.contractcommitment.contractcommitmentperiodstart) | Dimension | Mandatory | False | Date/Time |
| [Contract Commitment Quantity](#datamodel.contractcommitment.contractcommitmentquantity) | Metric | Mandatory | True | Decimal |
| [Contract Commitment Type](#datamodel.contractcommitment.contractcommitmenttype) | Dimension | Mandatory | False | String |
| [Contract Commitment Unit](#datamodel.contractcommitment.contractcommitmentunit) | Dimension | Mandatory | True | String |
| [Contract ID](#datamodel.contractcommitment.contractid) | Dimension | Mandatory | False | String |
| [Contract Period End](#datamodel.contractcommitment.contractperiodend) | Dimension | Mandatory | False | Date/Time |
| [Contract Period Start](#datamodel.contractcommitment.contractperiodstart) | Dimension | Mandatory | False | Date/Time |
| [Invoice Issuer Name](#datamodel.contractcommitment.invoiceissuername) | Dimension | Mandatory | False | String |
| [Pricing Currency](#datamodel.contractcommitment.pricingcurrency) | Dimension | Conditional | False | String |
| [Pricing Currency Contract Commitment Cost](#datamodel.contractcommitment.pricingcurrencycontractcommitmentcost) | Metric | Conditional | True | Decimal |
| [Service Provider Name](#datamodel.contractcommitment.serviceprovidername) | Dimension | Mandatory | False | String |

## Relationships<!--SkipTOC-->

The Contract Commitment dataset can be joined to the Cost and Usage dataset through the use of Contract Commitment ID.

* In the Contract Commitment dataset, Contract Commitment ID is a column.
* In the Cost and Usage dataset, Contract Commitment ID is a property within a JSON object array provided in Contract Applied column.

| Dataset A           | Dataset A Column       | Dataset B      | Dataset B Column |
| ------------------- | ---------------------- | -------------- | -----------------|
| Contract Commitment | Contract Commitment ID | Cost and Usage | Contract Applied |

## Requirements<!--SkipTOC-->

ContractCommitment MUST adhere to the following requirements:

* ContractCommitment column presence MUST adhere to the following requirements:
  * ContractCommitment MUST include [BillingCurrency](#datamodel.contractcommitment.billingcurrency).
  * ContractCommitment MUST include [ContractCommitmentApplicability](#datamodel.contractcommitment.contractcommitmentapplicability).
  * ContractCommitment MUST include [ContractCommitmentBenefitCategory](#datamodel.contractcommitment.contractcommitmentbenefitcategory).
  * ContractCommitment MUST include [ContractCommitmentCategory](#datamodel.contractcommitment.contractcommitmentcategory).
  * ContractCommitment MUST include [ContractCommitmentCost](#datamodel.contractcommitment.contractcommitmentcost).
  * ContractCommitment MUST include [ContractCommitmentCreated](#datamodel.contractcommitment.contractcommitmentcreated).
  * ContractCommitment MUST include [ContractCommitmentDescription](#datamodel.contractcommitment.contractcommitmentdescription).
  * ContractCommitment MUST include [ContractCommitmentDiscountPercentage](#datamodel.contractcommitment.contractcommitmentdiscountpercentage).
  * ContractCommitment MUST include [ContractCommitmentDurationType](#datamodel.contractcommitment.contractcommitmentdurationtype).
  * ContractCommitment MUST include [ContractCommitmentFulfillmentInterval](#datamodel.contractcommitment.contractcommitmentfulfillmentinterval).
  * ContractCommitment MUST include [ContractCommitmentId](#datamodel.contractcommitment.contractcommitmentid).
  * ContractCommitment MUST include [ContractCommitmentLastUpdated](#datamodel.contractcommitment.contractcommitmentlastupdated).
  * ContractCommitment MUST include [ContractCommitmentLifecycleStatus](#datamodel.contractcommitment.contractcommitmentlifecyclestatus).
  * ContractCommitment MUST include [ContractCommitmentModel](#datamodel.contractcommitment.contractcommitmentmodel).
  * ContractCommitment MUST include [ContractCommitmentOfferCategory](#datamodel.contractcommitment.contractcommitmentoffercategory).
  * ContractCommitment MUST include [ContractCommitmentPaymentInterval](#datamodel.contractcommitment.contractcommitmentpaymentinterval).
  * ContractCommitment MUST include [ContractCommitmentPaymentModel](#datamodel.contractcommitment.contractcommitmentpaymentmodel).
  * ContractCommitment MUST include [ContractCommitmentPaymentUpfrontPercentage](#datamodel.contractcommitment.contractcommitmentpaymentupfrontpercentage) when the [*operating model*](#glossary:operating-model) [includes partial upfront payments](#conditions.includespartialupfrontpayments).
  * ContractCommitment MUST include [ContractCommitmentPeriodEnd](#datamodel.contractcommitment.contractcommitmentperiodend).
  * ContractCommitment MUST include [ContractCommitmentPeriodStart](#datamodel.contractcommitment.contractcommitmentperiodstart).
  * ContractCommitment MUST include [ContractCommitmentQuantity](#datamodel.contractcommitment.contractcommitmentquantity).
  * ContractCommitment MUST include [ContractCommitmentType](#datamodel.contractcommitment.contractcommitmenttype).
  * ContractCommitment MUST include [ContractCommitmentUnit](#datamodel.contractcommitment.contractcommitmentunit).
  * ContractCommitment MUST include [ContractId](#datamodel.contractcommitment.contractid).
  * ContractCommitment MUST include [ContractPeriodEnd](#datamodel.contractcommitment.contractperiodend).
  * ContractCommitment MUST include [ContractPeriodStart](#datamodel.contractcommitment.contractperiodstart).
  * ContractCommitment MUST include [InvoiceIssuerName](#datamodel.contractcommitment.invoiceissuername).
  * ContractCommitment MUST include [PricingCurrency](#datamodel.contractcommitment.pricingcurrency) when the *operating model* [includes pricing and billing currency differences](#conditions.includespricing-billingcurrencydifferences).
  * ContractCommitment MUST include [PricingCurrencyContractCommitmentCost](#datamodel.contractcommitment.pricingcurrencycontractcommitmentcost) when the *operating model* includes pricing and billing currency differences.
  * ContractCommitment MUST include [ServiceProviderName](#datamodel.contractcommitment.serviceprovidername).
* ContractCommitment MUST conform to [CorrectionHandling](#attributes.correctionhandling) requirements.
* ContractCommitment MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.
* ContractCommitment MUST conform to [DatasetConfiguration](#attributes.datasetconfiguration) requirements.
* ContractCommitment MUST conform to [DeliveryHandling](#attributes.deliveryhandling) requirements.
* ContractCommitment [*FOCUS columns*](#glossary:FOCUS-column) MUST conform to [FocusColumnHandling](#attributes.focuscolumnhandling) requirements.
* ContractCommitment *FOCUS columns* MUST conform to [NullHandling](#attributes.nullhandling) requirements.
* ContractCommitment [*custom columns*](#glossary:custom-column) MUST conform to [CustomColumnHandling](#attributes.customcolumnhandling) requirements.

## Dataset ID<!--SkipTOC-->

ContractCommitment

## Display Name<!--SkipTOC-->

Contract Commitment

## Description<!--SkipTOC-->

Describes the terms of contracts agreed between a service provider and a customer.

## Version Introduced<!--SkipTOC-->

1.3
