# Examples: SKU Price Eligibility

This section describes examples for the [SKU Price Eligibility](#datamodel.skuprice.skupriceeligibility) column in the [SKU Price](#datamodel.skuprice) dataset.

## Global Scope

When a unit price is generally available to all entities without restriction (e.g., standard public list prices), the value for `IsGlobalScope` is set to `true`.

```json
{
  "IsGlobalScope": true
}
```

## Enterprise Scope with Exceptions

An enterprise-wide negotiated rate that covers all accounts **except** a specific sandbox account (BillingAccountId 123456789012).

```json
{
  "IsGlobalScope": true,
  "ExclusionOperator": "And",
  "Exclusions": [
    {
      "Dimension": "BillingAccountId",
      "Operator": "In",
      "Values": ["123456789012"]
    }
  ]
}
```

## Specific Account Scope

A custom contracted unit price that is only eligible for two specific Billing Accounts. Since `IsGlobalScope` and `IsComplexScope` are omitted, they default to `false`, requiring the inclusion block.

```json
{
  "InclusionOperator": "Or",
  "Inclusions": [
    {
      "Dimension": "BillingAccountId",
      "Operator": "In",
      "Values": [
        "123456789012",
        "987654321098"
      ]
    }
  ]
}
```

## Regional Scope

A unit price that is only eligible for consumption within a specific region (e.g., `us-east-1`).

```json
{
  "InclusionOperator": "Or",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1"]
    }
  ]
}
```

## Macro-Region Scope

A unit price where the catalog's base Pricing Region ID represents a broad macro-region (e.g., "us"), but the eligibility is explicitly mapped to the specific operational regions where consumption actually occurs.

```json
{
  "InclusionOperator": "Or",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": [
        "us-east-1",
        "us-east-2",
        "us-west-1",
        "us-west-2"
      ]
    }
  ]
}
```

## Global Region Scope

A unit price for a non-regionalized service (e.g., DNS, IAM, or CDN) where consumption occurs outside of a specific physical geography, which a service provider may represent with a Region ID value such as `"global"`.

```json
{
  "InclusionOperator": "Or",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["global"]
    }
  ]
}
```

## Custom Attribute Scope

A unit price that is only eligible for a specific value (Bring-Your-Own-License) for a custom entity (`x_LicenseModel`) in the `us-east-1` region.

```json
{
  "InclusionOperator": "And",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1"]
    },
    {
      "Dimension": "x_LicenseModel",
      "Operator": "In",
      "Values": ["Bring-Your-Own-License"]
    }
  ]
}
```

## Multi-Condition Scope with Exceptions

A unit price applicable to Compute services in either `us-east-1` or `us-west-2`, excluding any resources tagged with an `Environment` of `Sandbox`.

```json
{
  "InclusionOperator": "And",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1", "us-west-2"]
    },
    {
      "Dimension": "ServiceCategory",
      "Operator": "In",
      "Values": ["Compute"]
    }
  ],
  "ExclusionOperator": "Or",
  "Exclusions": [
    {
      "Dimension": "Tags",
      "Operator": "Contains",
      "Values": ["\"Environment\": \"Sandbox\""]
    }
  ]
}
```

## Complex Fallback

A unit price with dynamic or legacy eligibility logic that exceeds standard schema capabilities and requires provider-specific documentation.

```json
{
  "IsComplexScope": true
}
```
