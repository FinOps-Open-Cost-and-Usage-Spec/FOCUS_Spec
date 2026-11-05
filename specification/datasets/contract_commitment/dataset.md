# Contract Commitment

The [Contract Commitment](#ds) dataset is a supporting dataset that describes the terms of contracts agreed between a service provider and a customer.

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

The [Contract Commitment](#ds) dataset can be joined to the [Cost and Usage](#ds) dataset through the use of [Contract Commitment ID](#col).

* In the [Contract Commitment](#ds) dataset, [Contract Commitment ID](#col) is a column.
* In the [Cost and Usage](#ds) dataset, [Contract Commitment ID](#col) is a property within a JSON object array provided in [Contract Applied](#col:CostAndUsage.ContractApplied) column.

| Dataset A           | Dataset A Column       | Dataset B      | Dataset B Column |
| ------------------- | ---------------------- | -------------- | -----------------|
| Contract Commitment | Contract Commitment ID | Cost and Usage | Contract Applied |

## Requirements<!--SkipTOC-->

[ContractCommitment](#ds) MUST adhere to the following requirements:

* [ContractCommitment](#ds) column presence MUST adhere to the following requirements:
  * [ContractCommitment](#ds) MUST include [BillingCurrency](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentApplicability](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentBenefitCategory](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentCategory](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentCost](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentCreated](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentDescription](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentDiscountPercentage](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentDurationType](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentFulfillmentInterval](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentId](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentLastUpdated](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentLifecycleStatus](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentModel](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentOfferCategory](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentPaymentInterval](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentPaymentModel](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentPaymentUpfrontPercentage](#col) when the [operating model](#term) [includes partial upfront payments](#omc).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentPeriodEnd](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentPeriodStart](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentQuantity](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentType](#col).
  * [ContractCommitment](#ds) MUST include [ContractCommitmentUnit](#col).
  * [ContractCommitment](#ds) MUST include [ContractId](#col).
  * [ContractCommitment](#ds) MUST include [ContractPeriodEnd](#col).
  * [ContractCommitment](#ds) MUST include [ContractPeriodStart](#col).
  * [ContractCommitment](#ds) MUST include [InvoiceIssuerName](#col).
  * [ContractCommitment](#ds) MUST include [PricingCurrency](#col) when the [operating model](#term) [includes pricing and billing currency differences](#omc:IncludesPricingBillingCurrencyDifferences).
  * [ContractCommitment](#ds) MUST include [PricingCurrencyContractCommitmentCost](#col) when the [operating model](#term) includes pricing and billing currency differences.
  * [ContractCommitment](#ds) MUST include [ServiceProviderName](#col).
* [ContractCommitment](#ds) MUST conform to [CorrectionHandling](#attr) requirements.
* [ContractCommitment](#ds) MUST conform to [DatasetCompleteness](#attr) requirements.
* [ContractCommitment](#ds) MUST conform to [DatasetConfiguration](#attr) requirements.
* [ContractCommitment](#ds) MUST conform to [DeliveryHandling](#attr) requirements.
* [ContractCommitment](#ds) [FOCUS columns](#term) MUST conform to [FocusColumnHandling](#attr) requirements.
* [ContractCommitment](#ds) [FOCUS columns](#term) MUST conform to [NullHandling](#attr) requirements.
* [ContractCommitment](#ds) [custom columns](#term) MUST conform to [CustomColumnHandling](#attr) requirements.

## Dataset ID<!--SkipTOC-->

ContractCommitment

## Display Name<!--SkipTOC-->

Contract Commitment

## Description<!--SkipTOC-->

Describes the terms of contracts agreed between a service provider and a customer.

## Version Introduced<!--SkipTOC-->

1.3
