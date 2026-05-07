## Diff

Note: Requirements section could not be identified in one or both refs. Falling back to full-document diff.

- Path: `specification/datasets/contract_commitment/dataset.md`
- From ref: `v1.3`
- To ref: `working_draft`
- Requirements found in from ref: `False`
- Requirements found in to ref: `True`

@@ -1,56 +1,109 @@
# Contract Commitment

The Contract Commitment dataset is a supporting dataset that describes the terms of contracts agreed between a service provider and a customer.

[-<div class='h4-nonindex'>Columns</div>-]{+## Columns<!--SkipTOC-->+}

| Column | Column Type | Feature Level | Allows Nulls | Data Type |
| [--------------------------------------------------------------------]{+:---+} | [-------------]{+:---+} | [---------------]{+:---+} | [--------------]{+:---+} | [-----------]{+:---+} |
| Billing Currency | Dimension | Mandatory | True | String |
| Contract Commitment {+Applicability | Dimension | Mandatory | False | JSON |+}
{+| Contract Commitment Benefit Category | Dimension | Mandatory | False | String |+}
{+| Contract Commitment+} Category | Dimension | Mandatory | False | String |
| Contract Commitment Cost | Metric | Mandatory | True | [-Numeric-]{+Decimal |+}
{+| Contract Commitment Created | Dimension | Mandatory | False | Date/Time+} |
| Contract Commitment Description | Dimension | Mandatory | True | String |
| Contract Commitment {+Discount Percentage | Dimension | Mandatory | True | Decimal |+}
{+| Contract Commitment Duration Type | Dimension | Mandatory | False | String |+}
{+| Contract Commitment Fulfillment Interval | Dimension | Mandatory | False | String |+}
{+| Contract Commitment+} ID | Dimension | Mandatory | False | String |
| Contract Commitment {+Last Updated | Dimension | Mandatory | False | Date/Time |+}
{+| Contract Commitment Lifecycle Status | Dimension | Mandatory | False | String |+}
{+| Contract Commitment Model | Dimension | Mandatory | False | String |+}
{+| Contract Commitment Offer Category | Dimension | Mandatory | False | String |+}
{+| Contract Commitment Payment Interval | Dimension | Mandatory | False | String |+}
{+| Contract Commitment Payment Model | Dimension | Mandatory | False | String |+}
{+| Contract Commitment Payment Upfront Percentage | Dimension | Conditional | False | Decimal |+}
{+| Contract Commitment+} Period End | Dimension | Mandatory | False | Date/Time |
| Contract Commitment Period Start | Dimension | Mandatory | False | Date/Time |
| Contract Commitment Quantity | Metric | Mandatory | True | [-Numeric-]{+Decimal+} |
| Contract Commitment Type | Dimension | Mandatory | False | String |
| Contract Commitment Unit | Dimension | Mandatory | True | String |
| Contract ID | Dimension | Mandatory | False | String |
| Contract Period End | Dimension | Mandatory | False | Date/Time |
| Contract Period Start | Dimension | Mandatory | False | Date/Time |
[-<div class='h4-nonindex'>Relationships</div>-]{+| Invoice Issuer Name | Dimension | Mandatory | False | String |+}
{+| Pricing Currency | Dimension | Conditional | False | String |+}
{+| Pricing Currency Contract Commitment Cost | Metric | Conditional | True | Decimal |+}
{+| Service Provider Name | Dimension | Mandatory | False | String |+}

{+## Relationships<!--SkipTOC-->+}

The Contract Commitment dataset can be joined to the Cost and Usage dataset through the use of Contract Commitment ID.

* In the Contract Commitment dataset, Contract Commitment ID is a column.
* In the Cost and Usage dataset, Contract Commitment ID is a property within a JSON object array provided in Contract Applied column.

| Dataset A           | Dataset A Column       | Dataset B      | Dataset B Column |
| ------------------- | ---------------------- | -------------- | -----------------|
| Contract Commitment | Contract Commitment ID | Cost and Usage | Contract Applied |

[-<div class='h4-nonindex'>Requirements</div>-]{+## Requirements<!--SkipTOC-->+}

ContractCommitment [-adheres-]{+MUST adhere+} to the following requirements:

* ContractCommitment MUST be present when the service provider supports *contract commitments*.
* ContractCommitment {+column presence MUST adhere to the following requirements:+}
{+  * ContractCommitment MUST include BillingCurrency.+}
{+  * ContractCommitment MUST include ContractCommitmentApplicability.+}
{+  * ContractCommitment MUST include ContractCommitmentBenefitCategory.+}
{+  * ContractCommitment MUST include ContractCommitmentCategory.+}
{+  * ContractCommitment MUST include ContractCommitmentCost.+}
{+  * ContractCommitment MUST include ContractCommitmentCreated.+}
{+  * ContractCommitment MUST include ContractCommitmentDescription.+}
{+  * ContractCommitment MUST include ContractCommitmentDiscountPercentage.+}
{+  * ContractCommitment MUST include ContractCommitmentDurationType.+}
{+  * ContractCommitment MUST include ContractCommitmentFulfillmentInterval.+}
{+  * ContractCommitment MUST include ContractCommitmentId.+}
{+  * ContractCommitment MUST include ContractCommitmentLastUpdated.+}
{+  * ContractCommitment MUST include ContractCommitmentLifecycleStatus.+}
{+  * ContractCommitment MUST include ContractCommitmentModel.+}
{+  * ContractCommitment MUST include ContractCommitmentOfferCategory.+}
{+  * ContractCommitment MUST include ContractCommitmentPaymentInterval.+}
{+  * ContractCommitment MUST include ContractCommitmentPaymentModel.+}
{+  * ContractCommitment MUST include ContractCommitmentPaymentUpfrontPercentage when the service provider offers "Partial Upfront" payment models.+}
{+  * ContractCommitment MUST include ContractCommitmentPeriodEnd.+}
{+  * ContractCommitment MUST include ContractCommitmentPeriodStart.+}
{+  * ContractCommitment MUST include ContractCommitmentQuantity.+}
{+  * ContractCommitment MUST include ContractCommitmentType.+}
{+  * ContractCommitment MUST include ContractCommitmentUnit.+}
{+  * ContractCommitment MUST include ContractId.+}
{+  * ContractCommitment MUST include ContractPeriodEnd.+}
{+  * ContractCommitment MUST include ContractPeriodStart.+}
{+  * ContractCommitment MUST include InvoiceIssuerName.+}
{+  * ContractCommitment MUST include PricingCurrency when the service provider supports pricing and billing in different currencies.+}
{+  * ContractCommitment MUST include PricingCurrencyContractCommitmentCost when the service provider supports pricing and billing in different currencies.+}
{+  * ContractCommitment MUST include ServiceProviderName.+}
{+* ContractCommitment MUST conform to CorrectionHandling requirements.+}
{+* ContractCommitment MUST conform to DatasetCompleteness requirements.+}
{+* ContractCommitment+} MUST conform to [-ColumnHandling-]{+DatasetConfiguration+} requirements.
* ContractCommitment MUST conform to {+DeliveryHandling requirements.+}
{+* ContractCommitment *FOCUS columns* MUST conform to FocusColumnHandling requirements.+}
{+* ContractCommitment *FOCUS columns* MUST conform to+} NullHandling requirements.
[-<div class='h4-nonindex'>Dataset ID</div>-]{+* ContractCommitment *custom columns* MUST conform to CustomColumnHandling requirements.+}

{+## Dataset ID<!--SkipTOC-->+}

ContractCommitment

[-<div class='h4-nonindex'>Display Name</div>-]{+## Display Name<!--SkipTOC-->+}

Contract Commitment

[-<div class='h4-nonindex'>Description</div>-]{+## Description<!--SkipTOC-->+}

Describes the terms of contracts agreed between a service provider and a customer.

[-<div class='h4-nonindex'>Introduced (version)</div>-]{+## Introduced (version)<!--SkipTOC-->+}

1.3
