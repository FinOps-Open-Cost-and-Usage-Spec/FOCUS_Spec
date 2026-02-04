# Marketplace Multi-Provider Scenario Guidance

*This section is non-normative.*

## Overview

In multi-provider marketplace scenarios, billing data may originate from different data generators. For example, a Cloud Service Provider (CSP) might handle the purchase transaction, while a Software-as-a-Service (SaaS) provider generates usage records. This guidance clarifies how FOCUS columns, particularly EffectiveCost, should be populated in such cases.

This guidance addresses the data accuracy concerns outlined in the parent issue [FR] Clarify definitions of EffectiveCost vs BilledCost across providers [#982](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/982), which reframes the problem from "double counting" to providers populating inaccurate EffectiveCost values when lacking actual usage information. It provides scenario-based guidance for marketplace purchases as specified in Milestone 3 of #982.

## Provider Responsibility Matrix

| Scenario | Purchase Provider | Usage Provider | EffectiveCost Population |
|----------|-------------------|----------------|--------------------------|
| CSP Marketplace (CSP as invoice issuer) | CSP | CSP | CSP populates based on actual usage |
| Third-party SaaS via Marketplace (SaaS as usage provider) | CSP | SaaS | SaaS populates based on actual usage; CSP does not estimate |
| Cross-provider | CSP | SaaS | Only provider with actual usage data populates EffectiveCost |

## Key Principles

- **CSP has purchase record but not usage details**: MUST NOT estimate EffectiveCost. (Aligns with #982's conformance requirement that data generators MUST NOT populate EffectiveCost with estimated or made-up values when lacking actual usage/accrual information.)
- **SaaS provider has usage details but not purchase record**: EffectiveCost reflects actual usage.
- **Cross-provider aggregations will NOT match**: This is expected behavior, not an error. (Supports #982's cross-cutting criteria for when aggregations will NOT match in cross-provider marketplace scenarios.)
- **Only provider with actual usage data should populate EffectiveCost**.

## Examples

### AWS Marketplace Example

In [AWS Marketplace](https://aws.amazon.com/marketplace/), a customer purchases a SaaS product through AWS. AWS issues the invoice, but the SaaS provider (e.g., Datadog) provides usage data. As per [AWS Marketplace Billing Documentation](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-paying-for-products.html), AWS consolidates charges but usage details come from the SaaS provider.

- AWS (Purchase Provider): Populates BilledCost, but not EffectiveCost.
- Datadog (Usage Provider): Populates EffectiveCost based on actual usage.

### Azure Marketplace Example

In [Azure Marketplace](https://azure.microsoft.com/en-us/marketplace/), similar to AWS, Azure handles the purchase, and SaaS provides usage. Azure's billing consolidates marketplace purchases, but usage is reported by the SaaS vendor.

### GCP Marketplace Example

[Google Cloud Marketplace](https://cloud.google.com/marketplace/docs/overview) follows the same pattern, where GCP invoices for purchases but SaaS providers supply usage data.

## Correlation Approach for Practitioners

Practitioners can correlate data using common identifiers such as:
- ResourceId
- ChargeId
- InvoiceId (where available)

Note: Correlation may require additional metadata or external systems. For more details on FOCUS columns, see the [FOCUS Column Library](https://focus.finops.org/focus-columns/). Reference the parent issue for this guidance: [FR] Clarify definitions of EffectiveCost vs BilledCost across providers [#982](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/982).

## Warning: Cross-Provider Aggregation Mismatch

When aggregating data from multiple providers, totals may not match due to different data sources. This is expected behavior, not an error, as confirmed by provider documentation (e.g., [AWS Marketplace Billing](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-paying-for-products.html), [Azure Marketplace](https://azure.microsoft.com/en-us/marketplace/), [GCP Marketplace](https://cloud.google.com/marketplace/docs/overview)).

### Addressing Aggregation Mismatches

Practitioners can address mismatches through the following approaches:

1. **Correlation and Matching**: Use shared identifiers (e.g., ResourceId, ChargeId) to link purchase records from CSPs with usage records from SaaS providers. This may require custom ETL processes or third-party tools.

2. **Separate Reporting**: Report CSP and SaaS data separately, with clear labels indicating the source, to avoid misleading aggregations.

3. **Reconciliation Processes**: Implement manual or automated reconciliation workflows to account for discrepancies, such as comparing invoice totals against usage-based calculations.

4. **Provider Communication**: Contact providers for additional metadata or clarification on how their billing data relates.

5. **Documentation and Disclaimers**: Include disclaimers in reports noting that cross-provider totals may not match due to data source differences.

This guidance is supported by provider practices where CSPs handle transactions but SaaS providers deliver usage data, leading to potential mismatches in unified views.

## Validation

This guidance has been validated with implementations from Datadog, Grafana, and Neos. For further details, refer to the related GitHub issue: [AI] Draft Marketplace Multi-Provider Scenario Guidance (Appendix) [#1896](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/1896). It contributes to the broader effort in [FR] Clarify definitions of EffectiveCost vs BilledCost across providers [#982](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/982), specifically supporting Milestone 3 scenario-based guidance for marketplace purchases.

## Possible Enhancements to FOCUS Specification

To further reduce challenges for practitioners in multi-provider scenarios, the following enhancements could be proposed for future FOCUS versions (e.g., 1.4 or later). These are inspired by existing spec content (e.g., marketplace examples in supporting documents and correlation notes in release planning) and aim to build on FOCUS 1.3's additions like ServiceProviderName and HostProviderName. They consider input from various stakeholders, including CSPs, SaaS providers, and FinOps practitioners, to ensure broad applicability.

1. **New Column: MarketplaceTransactionId**
   - A unique identifier shared between CSP and SaaS for the same marketplace transaction, enabling automatic correlation of purchase and usage data.
   - **Proposed GitHub Issue Description**:
     ```
     ## Feature Request: Add MarketplaceTransactionId Column

     ### Description
     In multi-provider marketplace scenarios, practitioners struggle to correlate purchase records from CSPs with usage data from SaaS providers, leading to aggregation mismatches. Propose adding a new column `MarketplaceTransactionId` to the Cost and Usage dataset.

     ### Proposed Changes
     - **Column ID**: MarketplaceTransactionId
     - **Type**: String
     - **Requirements**:
       - MUST be present for marketplace transactions.
       - MUST be a unique ID shared between purchase and usage providers.
       - MAY be null for non-marketplace data.
     - **Description**: Unique identifier for correlating marketplace purchase and usage records across providers.

     ### Rationale
     Builds on existing marketplace guidance in the appendix and correlation needs in RELEASE-PLANNING.md. Reduces practitioner effort in scenarios like AWS Marketplace + Datadog.

     ### Stakeholders
     CSPs (AWS, Azure, GCP), SaaS providers (Datadog, etc.), FinOps practitioners.

     ### References
     - Appendix: Marketplace Multi-Provider Scenario Guidance
     - Issue #1896
     ```

2. **Update EffectiveCost Requirements**
   - Add normative rules for multi-provider scenarios, explicitly stating that only providers with usage data populate EffectiveCost, and that cross-provider mismatches are expected.
   - **Proposed GitHub Issue Description**:
     ```
     ## Feature Request: Update EffectiveCost for Multi-Provider Scenarios

     ### Description
     EffectiveCost population is unclear in multi-provider marketplaces, where CSPs lack usage details. Update the column requirements to clarify responsibilities and allow for expected mismatches.

     ### Proposed Changes
     Add to `specification/datasets/cost_and_usage/columns/effectivecost.md`:
     - "In multi-provider marketplace scenarios, EffectiveCost MUST be populated only by the provider with access to actual usage data. Cross-provider aggregations MAY not match; this is expected."
     - Update description to reference marketplace guidance.

     ### Rationale
     Aligns with appendix guidance and prevents estimation errors. Supports issue #982 on EffectiveCost vs BilledCost.

     ### Stakeholders
     All FOCUS data generators and consumers.

     ### References
     - Appendix: Marketplace Multi-Provider Scenario Guidance
     - Issue #1896, #982
     ```

3. **New Column: DataSourceRole**
   - Indicates the role of the data generator (e.g., "PurchaseProvider", "UsageProvider") to clarify responsibilities without requiring full correlation.
   - **Proposed GitHub Issue Description**:
     ```
     ## Feature Request: Add DataSourceRole Column

     ### Description
     To clarify provider roles in multi-provider scenarios, add a column indicating whether a row represents purchase or usage data.

     ### Proposed Changes
     - **Column ID**: DataSourceRole
     - **Type**: String (enum: "PurchaseProvider", "UsageProvider", "Both")
     - **Requirements**:
       - MUST indicate the data generator's role.
       - MUST be "UsageProvider" for SaaS in marketplaces.
     - **Description**: Role of the provider in supplying purchase vs. usage information.

     ### Rationale
     Complements provider responsibility matrix in appendix. Inspired by reseller/marketplace handling in version migration guidance.

     ### Stakeholders
     CSPs, SaaS providers, tool vendors.

     ### References
     - Appendix: Marketplace Multi-Provider Scenario Guidance
     - Issue #1896
     ```

4. **Enhance Existing Columns**
   - Strengthen InvoiceId and ServiceProviderName for marketplace support, requiring CSPs to include correlatable references.
   - **Proposed GitHub Issue Description**:
     ```
     ## Feature Request: Enhance InvoiceId and ServiceProviderName for Marketplaces

     ### Description
     Existing columns like InvoiceId lack correlation support for marketplaces. Enhance requirements to mandate correlatable references from CSPs.

     ### Proposed Changes
     - Update InvoiceId: Require CSPs to include a reference (e.g., prefix) replicable by SaaS providers.
     - Update ServiceProviderName: Strengthen marketplace notes to ensure clear distinction between seller and operator.

     ### Rationale
     Builds on FOCUS 1.3 additions and correlation focus in RELEASE-PLANNING.md. Improves usability without new columns.

     ### Stakeholders
     CSPs, SaaS vendors.

     ### References
     - Appendix: Marketplace Multi-Provider Scenario Guidance
     - Issue #1896
     ```

5. **Normative Aggregation Guidance**
   - Add spec-level guidance on handling mismatches, encouraging providers to document correlation methods.
   - **Proposed GitHub Issue Description**:
     ```
     ## Feature Request: Add Normative Guidance on Cross-Provider Aggregation

     ### Description
     Practitioners need standardized ways to handle aggregation mismatches in multi-provider data. Add normative guidance to the dataset spec.

     ### Proposed Changes
     Add to `specification/datasets/cost_and_usage/dataset.md`:
     - "In multi-provider scenarios, data generators MUST document correlation methods. Aggregations MAY result in mismatches; practitioners SHOULD use disclaimers or separate reporting."

     ### Rationale
     Elevates appendix advice to normative level, ensuring inclusivity for all provider types. Addresses mismatches as expected behavior.

     ### Stakeholders
     All FOCUS participants.

     ### References
     - Appendix: Marketplace Multi-Provider Scenario Guidance
     - Issue #1896
     ```

These enhancements would make FOCUS more robust for complex billing ecosystems while maintaining backward compatibility. Community feedback is encouraged—consider proposing these via FOCUS Working Group discussions or GitHub issues to gather input from all stakeholders.

These enhancements would make FOCUS more robust for complex billing ecosystems while maintaining backward compatibility. Community feedback is encouraged—consider proposing these via FOCUS Working Group discussions or GitHub issues to gather input from all stakeholders.