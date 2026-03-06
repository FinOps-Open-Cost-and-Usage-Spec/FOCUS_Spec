## Diff

ContractCommitment [-adheres-]{+MUST adhere+} to the following requirements:

* ContractCommitment MUST be present when the service provider supports *contract commitments*.
* ContractCommitment {+column presence MUST adhere to the following requirements:+}
{+  * ContractCommitment MUST include [BillingCurrency](#datasets.contractcommitment.billingcurrency).+}
{+  * ContractCommitment MUST include [ContractCommitmentCategory](#datasets.contractcommitment.contractcommitmentcategory).+}
{+  * ContractCommitment MUST include [ContractCommitmentCost](#datasets.contractcommitment.contractcommitmentcost).+}
{+  * ContractCommitment MUST include [ContractCommitmentDescription](#datasets.contractcommitment.contractcommitmentdescription).+}
{+  * ContractCommitment MUST include [ContractCommitmentId](#datasets.contractcommitment.contractcommitmentid).+}
{+  * ContractCommitment MUST include [ContractCommitmentPeriodEnd](#datasets.contractcommitment.contractcommitmentperiodend).+}
{+  * ContractCommitment MUST include [ContractCommitmentPeriodStart](#datasets.contractcommitment.contractcommitmentperiodstart).+}
{+  * ContractCommitment MUST include [ContractCommitmentQuantity](#datasets.contractcommitment.contractcommitmentquantity).+}
{+  * ContractCommitment MUST include [ContractCommitmentType](#datasets.contractcommitment.contractcommitmenttype).+}
{+  * ContractCommitment MUST include [ContractCommitmentUnit](#datasets.contractcommitment.contractcommitmentunit).+}
{+  * ContractCommitment MUST include [ContractId](#datasets.contractcommitment.contractid).+}
{+  * ContractCommitment MUST include [ContractPeriodEnd](#datasets.contractcommitment.contractperiodend).+}
{+  * ContractCommitment MUST include [ContractPeriodStart](#datasets.contractcommitment.contractperiodstart).+}
{+* ContractCommitment MUST conform to [ColumnHandling](#attributes.columnhandling) requirements.+}
{+* ContractCommitment+} MUST conform to [-[ColumnHandling](#columnhandling)-]{+[NullHandling](#attributes.nullhandling)+} requirements.
* ContractCommitment MUST conform to [-[NullHandling](#nullhandling)-]{+[DatasetConfiguration](#attributes.datasetconfiguration)+} requirements.