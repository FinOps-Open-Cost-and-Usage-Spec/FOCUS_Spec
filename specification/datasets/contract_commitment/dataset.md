# Contract Commitment

The Contract Commitment dataset is a supporting dataset that describes the terms of contracts agreed between a service provider and a customer.

## Columns<!--SkipTOC-->

| Column | Column Type | Feature Level | Allows Nulls | Data Type |
| :--- | :--- | :--- | :--- | :--- |
| [Billing Currency](#datasets.contractcommitment.billingcurrency) | Dimension | Mandatory | True | String |
| [Contract Commitment Applicability](#datasets.contractcommitment.contractcommitmentapplicability) | Dimension | Mandatory | False | JSON |
| [Contract Commitment Benefit Category](#datasets.contractcommitment.contractcommitmentbenefitcategory) | Dimension | Mandatory | False | String |
| [Contract Commitment Category](#datasets.contractcommitment.contractcommitmentcategory) | Dimension | Mandatory | False | String |
| [Contract Commitment Cost](#datasets.contractcommitment.contractcommitmentcost) | Metric | Mandatory | True | Decimal |
| [Contract Commitment Created](#datasets.contractcommitment.contractcommitmentcreated) | Dimension | Mandatory | False | Date/Time |
| [Contract Commitment Description](#datasets.contractcommitment.contractcommitmentdescription) | Dimension | Mandatory | True | String |
| [Contract Commitment Discount Percentage](#datasets.contractcommitment.contractcommitmentdiscountpercentage) | Dimension | Mandatory | True | Decimal |
| [Contract Commitment Duration Type](#datasets.contractcommitment.contractcommitmentdurationtype) | Dimension | Mandatory | False | String |
| [Contract Commitment Fulfillment Interval](#datasets.contractcommitment.contractcommitmentfulfillmentinterval) | Dimension | Mandatory | False | String |
| [Contract Commitment ID](#datasets.contractcommitment.contractcommitmentid) | Dimension | Mandatory | False | String |
| [Contract Commitment Last Updated](#datasets.contractcommitment.contractcommitmentlastupdated) | Dimension | Mandatory | False | Date/Time |
| [Contract Commitment Lifecycle Status](#datasets.contractcommitment.contractcommitmentlifecyclestatus) | Dimension | Mandatory | False | String |
| [Contract Commitment Model](#datasets.contractcommitment.contractcommitmentmodel) | Dimension | Mandatory | False | String |
| [Contract Commitment Offer Category](#datasets.contractcommitment.contractcommitmentoffercategory) | Dimension | Mandatory | False | String |
| [Contract Commitment Payment Interval](#datasets.contractcommitment.contractcommitmentpaymentinterval) | Dimension | Mandatory | False | String |
| [Contract Commitment Payment Model](#datasets.contractcommitment.contractcommitmentpaymentmodel) | Dimension | Mandatory | False | String |
| [Contract Commitment Payment Upfront Percentage](#datasets.contractcommitment.contractcommitmentpaymentupfrontpercentage) | Dimension | Conditional | False | Decimal |
| [Contract Commitment Period End](#datasets.contractcommitment.contractcommitmentperiodend) | Dimension | Mandatory | False | Date/Time |
| [Contract Commitment Period Start](#datasets.contractcommitment.contractcommitmentperiodstart) | Dimension | Mandatory | False | Date/Time |
| [Contract Commitment Quantity](#datasets.contractcommitment.contractcommitmentquantity) | Metric | Mandatory | True | Decimal |
| [Contract Commitment Type](#datasets.contractcommitment.contractcommitmenttype) | Dimension | Mandatory | False | String |
| [Contract Commitment Unit](#datasets.contractcommitment.contractcommitmentunit) | Dimension | Mandatory | True | String |
| [Contract ID](#datasets.contractcommitment.contractid) | Dimension | Mandatory | False | String |
| [Contract Period End](#datasets.contractcommitment.contractperiodend) | Dimension | Mandatory | False | Date/Time |
| [Contract Period Start](#datasets.contractcommitment.contractperiodstart) | Dimension | Mandatory | False | Date/Time |
| [Invoice Issuer Name](#datasets.contractcommitment.invoiceissuername) | Dimension | Mandatory | False | String |
| [Pricing Currency](#datasets.contractcommitment.pricingcurrency) | Dimension | Conditional | False | String |
| [Pricing Currency Contract Commitment Cost](#datasets.contractcommitment.pricingcurrencycontractcommitmentcost) | Metric | Conditional | True | Decimal |
| [Service Provider Name](#datasets.contractcommitment.serviceprovidername) | Dimension | Mandatory | False | String |

## Relationships<!--SkipTOC-->

The Contract Commitment dataset can be joined to the Cost and Usage dataset through the use of Contract Commitment ID.

* In the Contract Commitment dataset, Contract Commitment ID is a column.
* In the Cost and Usage dataset, Contract Commitment ID is a property within a JSON object array provided in Contract Applied column.

| Dataset A           | Dataset A Column       | Dataset B      | Dataset B Column |
| ------------------- | ---------------------- | -------------- | -----------------|
| Contract Commitment | Contract Commitment ID | Cost and Usage | Contract Applied |

## Requirements<!--SkipTOC-->

ContractCommitment MUST adhere to the following requirements:

* ContractCommitment MUST be present when the service provider supports *contract commitments*.
* ContractCommitment column presence MUST adhere to the following requirements:
  * ContractCommitment MUST include [BillingCurrency](#datasets.contractcommitment.billingcurrency).
  * ContractCommitment MUST include [ContractCommitmentApplicability](#datasets.contractcommitment.contractcommitmentapplicability).
  * ContractCommitment MUST include [ContractCommitmentBenefitCategory](#datasets.contractcommitment.contractcommitmentbenefitcategory).
  * ContractCommitment MUST include [ContractCommitmentCategory](#datasets.contractcommitment.contractcommitmentcategory).
  * ContractCommitment MUST include [ContractCommitmentCost](#datasets.contractcommitment.contractcommitmentcost).
  * ContractCommitment MUST include [ContractCommitmentCreated](#datasets.contractcommitment.contractcommitmentcreated).
  * ContractCommitment MUST include [ContractCommitmentDescription](#datasets.contractcommitment.contractcommitmentdescription).
  * ContractCommitment MUST include [ContractCommitmentDiscountPercentage](#datasets.contractcommitment.contractcommitmentdiscountpercentage).
  * ContractCommitment MUST include [ContractCommitmentDurationType](#datasets.contractcommitment.contractcommitmentdurationtype).
  * ContractCommitment MUST include [ContractCommitmentFulfillmentInterval](#datasets.contractcommitment.contractcommitmentfulfillmentinterval).
  * ContractCommitment MUST include [ContractCommitmentId](#datasets.contractcommitment.contractcommitmentid).
  * ContractCommitment MUST include [ContractCommitmentLastUpdated](#datasets.contractcommitment.contractcommitmentlastupdated).
  * ContractCommitment MUST include [ContractCommitmentLifecycleStatus](#datasets.contractcommitment.contractcommitmentlifecyclestatus).
  * ContractCommitment MUST include [ContractCommitmentModel](#datasets.contractcommitment.contractcommitmentmodel).
  * ContractCommitment MUST include [ContractCommitmentOfferCategory](#datasets.contractcommitment.contractcommitmentoffercategory).
  * ContractCommitment MUST include [ContractCommitmentPaymentInterval](#datasets.contractcommitment.contractcommitmentpaymentinterval).
  * ContractCommitment MUST include [ContractCommitmentPaymentModel](#datasets.contractcommitment.contractcommitmentpaymentmodel).
  * ContractCommitment MUST include [ContractCommitmentPaymentUpfrontPercentage](#datasets.contractcommitment.contractcommitmentpaymentupfrontpercentage) if the service provider offers "Partial Upfront" [payment models](#datasets.contractcommitment.contractcommitmentpaymentmodel).
  * ContractCommitment MUST include [ContractCommitmentPeriodEnd](#datasets.contractcommitment.contractcommitmentperiodend).
  * ContractCommitment MUST include [ContractCommitmentPeriodStart](#datasets.contractcommitment.contractcommitmentperiodstart).
  * ContractCommitment MUST include [ContractCommitmentQuantity](#datasets.contractcommitment.contractcommitmentquantity).
  * ContractCommitment MUST include [ContractCommitmentType](#datasets.contractcommitment.contractcommitmenttype).
  * ContractCommitment MUST include [ContractCommitmentUnit](#datasets.contractcommitment.contractcommitmentunit).
  * ContractCommitment MUST include [ContractId](#datasets.contractcommitment.contractid).
  * ContractCommitment MUST include [ContractPeriodEnd](#datasets.contractcommitment.contractperiodend).
  * ContractCommitment MUST include [ContractPeriodStart](#datasets.contractcommitment.contractperiodstart).
  * ContractCommitment MUST include [InvoiceIssuerName](#datasets.contractcommitment.invoiceissuername).
  * ContractCommitment MUST include [PricingCurrency](#datasets.contractcommitment.pricingcurrency) when the service provider supports pricing and billing in different currencies.
  * ContractCommitment MUST include [PricingCurrencyContractCommitmentCost](#datasets.contractcommitment.pricingcurrencycontractcommitmentcost) when the service provider supports pricing and billing in different currencies.
  * ContractCommitment MUST include [ServiceProviderName](#datasets.contractcommitment.serviceprovidername).
* ContractCommitment MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.
* ContractCommitment MUST conform to [DatasetConfiguration](#attributes.datasetconfiguration) requirements.
* ContractCommitment MUST conform to [ColumnHandling](#attributes.columnhandling) requirements for each column.
* ContractCommitment MUST conform to [CurrencyFormat](#attributes.currencyformat) requirements for each column representing national currency.
* ContractCommitment MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements for each column containing date/time values.
* ContractCommitment MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements for each column containing JSON values.
* ContractCommitment MUST conform to [NullHandling](#attributes.nullhandling) requirements for each column.
* ContractCommitment MUST conform to [NumericFormat](#attributes.numericformat) requirements for each column containing numeric values.
* ContractCommitment MUST conform to [StringHandling](#attributes.stringhandling) requirements for each column containing string values.
* ContractCommitment SHOULD conform to [UnitFormat](#attributes.unitformat) requirements for each column representing measurement unit.

## Dataset ID<!--SkipTOC-->

ContractCommitment

## Display Name<!--SkipTOC-->

Contract Commitment

## Description<!--SkipTOC-->

Describes the terms of contracts agreed between a service provider and a customer.

## Introduced (version)<!--SkipTOC-->

1.3
