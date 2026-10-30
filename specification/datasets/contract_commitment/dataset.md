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

The Contract Commitment dataset can be joined to the [Cost and Usage](#ds) dataset through the use of [Contract Commitment ID](#col).

* In the Contract Commitment dataset, [Contract Commitment ID](#col) is a column.
* In the [Cost and Usage](#ds) dataset, [Contract Commitment ID](#col) is a property within a JSON object array provided in [Contract Applied](#col:CostAndUsage.ContractApplied) column.

| Dataset A           | Dataset A Column       | Dataset B      | Dataset B Column |
| ------------------- | ---------------------- | -------------- | -----------------|
| Contract Commitment | Contract Commitment ID | Cost and Usage | Contract Applied |

## Requirements<!--SkipTOC-->

ContractCommitment MUST adhere to the following requirements:

* ContractCommitment column presence MUST adhere to the following requirements:
  * ContractCommitment MUST include [BillingCurrency](#col).
  * ContractCommitment MUST include [ContractCommitmentApplicability](#col).
  * ContractCommitment MUST include [ContractCommitmentBenefitCategory](#col).
  * ContractCommitment MUST include [ContractCommitmentCategory](#col).
  * ContractCommitment MUST include [ContractCommitmentCost](#col).
  * ContractCommitment MUST include [ContractCommitmentCreated](#col).
  * ContractCommitment MUST include [ContractCommitmentDescription](#col).
  * ContractCommitment MUST include [ContractCommitmentDiscountPercentage](#col).
  * ContractCommitment MUST include [ContractCommitmentDurationType](#col).
  * ContractCommitment MUST include [ContractCommitmentFulfillmentInterval](#col).
  * ContractCommitment MUST include [ContractCommitmentId](#col).
  * ContractCommitment MUST include [ContractCommitmentLastUpdated](#col).
  * ContractCommitment MUST include [ContractCommitmentLifecycleStatus](#col).
  * ContractCommitment MUST include [ContractCommitmentModel](#col).
  * ContractCommitment MUST include [ContractCommitmentOfferCategory](#col).
  * ContractCommitment MUST include [ContractCommitmentPaymentInterval](#col).
  * ContractCommitment MUST include [ContractCommitmentPaymentModel](#col).
  * ContractCommitment MUST include [ContractCommitmentPaymentUpfrontPercentage](#col) when the [operating model](#term) [includes partial upfront payments](#omc).
  * ContractCommitment MUST include [ContractCommitmentPeriodEnd](#col).
  * ContractCommitment MUST include [ContractCommitmentPeriodStart](#col).
  * ContractCommitment MUST include [ContractCommitmentQuantity](#col).
  * ContractCommitment MUST include [ContractCommitmentType](#col).
  * ContractCommitment MUST include [ContractCommitmentUnit](#col).
  * ContractCommitment MUST include [ContractId](#col).
  * ContractCommitment MUST include [ContractPeriodEnd](#col).
  * ContractCommitment MUST include [ContractPeriodStart](#col).
  * ContractCommitment MUST include [InvoiceIssuerName](#col).
  * ContractCommitment MUST include [PricingCurrency](#col) when the [operating model](#term) [includes pricing and billing currency differences](#omc:IncludesPricingBillingCurrencyDifferences).
  * ContractCommitment MUST include [PricingCurrencyContractCommitmentCost](#col) when the [operating model](#term) includes pricing and billing currency differences.
  * ContractCommitment MUST include [ServiceProviderName](#col).
* ContractCommitment MUST conform to [CorrectionHandling](#attr) requirements.
* ContractCommitment MUST conform to [DatasetCompleteness](#attr) requirements.
* ContractCommitment MUST conform to [DatasetConfiguration](#attr) requirements.
* ContractCommitment MUST conform to [DeliveryHandling](#attr) requirements.
* ContractCommitment [FOCUS columns](#term) MUST conform to [FocusColumnHandling](#attr) requirements.
* ContractCommitment [FOCUS columns](#term) MUST conform to [NullHandling](#attr) requirements.
* ContractCommitment [custom columns](#term) MUST conform to [CustomColumnHandling](#attr) requirements.

## Dataset ID<!--SkipTOC-->

ContractCommitment

## Display Name<!--SkipTOC-->

Contract Commitment

## Description<!--SkipTOC-->

Describes the terms of contracts agreed between a service provider and a customer.

## Version Introduced<!--SkipTOC-->

1.3
