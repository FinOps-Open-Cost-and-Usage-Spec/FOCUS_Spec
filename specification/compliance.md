# FOCUS Compliance

Most billing datasets are unique based on the provider, its method of determining cost (e.g. fixed vs consumption-based billing), support for various concepts (e.g. commitment-based discounts), and the provider's billing system's maturity level.

FOCUS aims to help FinOps practitioners perform common FinOps capabilities by using a generic set of instructions. FOCUS accomplishes this by defining compliance requirements that account for the provider-level differences mentioned above.

## Enabling FinOps Capabilities For Heterogeneous Cost Datasets

Cloud Service Providers (CSPs) generate detailed cost and usage data in near real-time enabling an extensive set of FinOps capabilities to drive accountability and efficiency for dynamic consumption-based costs.  Non-CSP providers typically provide billing datasets that lack the same level of detail. The purpose of FOCUS Essential's reduced data set is to allow easier access for non-CSP providers to be incorporated in the full FOCUS data cube without breaking any primary FinOps capabilities, performing invoice reconciliation, data ingestion, and data normalization. Simplified versions of additional FinOps capabilities like cost reporting, chargeback, showback, and budgeting/forecasting can also be performed using a less-detailed billing dataset when essential requirements are met.

Performing these capabilities will ultimately benefit organizations by enabling efficient, data-driven decision-making. The essential requirements needed to perform the important FinOps capabilities defined above are hereby referred to as the 'FOCUS Essential' requirements.

## Meeting FOCUS Requirements

FOCUS [Columns](#columns) designated as FOCUS Essential are required to be present in all compliant datasets and comply with the requirements (e.g. nullability and various other semantics) specified in the normative prose of such columns.

Non-FOCUS Essential columns defined in the specification may be omitted from the billing dataset based on the semantics defined in the normative prose of such columns. For example, columns related to commitment-based discounts can specify that they can be omitted when a provider doesn't support commitment-based discounts. Conversely, the providers that do support this discount construct are required to provide this column and meet all requirements defined in the normative prose of those columns.

Requirements defined under FOCUS [Attributes](#attributes) must be met regardless of the FOCUS Essential designation.
