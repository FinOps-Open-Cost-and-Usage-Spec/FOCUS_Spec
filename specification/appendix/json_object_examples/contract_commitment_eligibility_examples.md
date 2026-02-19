# Examples: Contract Commitment Eligibility

## Global Scope and Applicability

If the commitment is 100% applicable to all resources, the `Applicability` object can be omitted entirely.

```json
{
  "IsGlobalScope": true
}
```

## Global Scope with Specific Exceptions

Organization-wide coverage **except** for Database services running in BillingAccountId 123456789012.

```json
{
  "IsGlobalScope": true,
  "ExclusionOperator": "AND",
  "Exclusions": [
    {
      "Dimension": "BillingAccountId",
      "Operator": "In",
      "Values": ["123456789012"]
    },
    {
      "Dimension": "ServiceCategory",
      "Operator": "In",
      "Values": ["Database"]
    }
  ]
}
```

## Regional Scope

A commitment purchased for a specific region (e.g., `us-east-1`). Since `IsGlobalScope` and `IsComplexScope` are omitted, they default to `false`, requiring the inclusion block.

```json
{
  "InclusionOperator": "OR",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1"]
    }
  ]
}
```

## Custom Scope

A commitment that is only applicable to a specific value (Pay-As-You-Go) for a custom entity (x_BillingModel) in the `us-east-1` region.

```json
{
  "InclusionOperator": "OR",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1"]
    },
    {
      "Dimension": "x_BillingModel",
      "Operator": "In",
      "Values": ["Pay-As-You-Go"]
    }
  ]
}
```

## Regional Compute Commitment with Exceptions

Applies to Compute in `us-east-1` and `us-west-2`, excluding any resources or services tagged with an `Environment` of `Sandbox`.

```json
{
  "InclusionOperator": "AND",
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
  "ExclusionOperator": "OR",
  "Exclusions": [
    {
      "Dimension": "Tags",
      "Operator": "Contains",
      "Values": ["\"Environment\": \"Sandbox\""]
    }
  ]
}
```

## Regional Applicability

A commitment that applies fully to `us-east-1` but only 50% of cost and usage in `us-west-2` is eligible. Note the use of the object even for symmetrical applicability.

```json
{
  "InclusionOperator": "OR",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1"]
    },
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-west-2"],
      "Applicability": {
        "Cost": 0.5,
        "Usage": 0.5
      }
    }
  ]
}
```

## Granular Applicability (Partial Object)

A scenario where 100% of Marketplace **Usage** counts toward a volume commitment, but only 50% of the **Cost** is applicable for financial credit. The engine defaults the missing `Usage` key to `1.0`.

```json
{
  "InclusionOperator": "OR",
  "Inclusions": [
    {
      "Dimension": "InvoiceIssuerName",
      "Operator": "In",
      "Values": ["Cloud Marketplace"],
      "Applicability": {
        "Cost": 0.5
      }
    }
  ]
}
```

## Complex Fallback

A commitment with dynamic or conditional logic that requires calculation against the total aggregate of cost or usage.

```json
{
  "IsComplexScope": true
}
```
