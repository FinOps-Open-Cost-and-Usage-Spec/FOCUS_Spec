## Diff

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