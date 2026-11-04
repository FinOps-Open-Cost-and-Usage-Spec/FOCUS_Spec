# Examples: Commitment Applicability

This section describes examples for the [Commitment Applicability](#datamodel.skuprice.commitmentapplicability) column in the [SKU Price](#datamodel.skuprice) dataset. Each object belongs to a SKU Price record that represents the purchase of a [*commitment discount*](#glossary:commitment-discount).

## Usage-Based Commitment with Flexibility

A one-year reservation for the standard virtual machine family (SKU Price ID "AURAWEB-COMPUTE-RESERVATION-VM-STD-1YR-ALL-UPFRONT", Commitment Discount Category "Usage", Pricing Unit "Units"). One reservation covers one hour of the 8X32 size, two hours of the 4X16 size, or half an hour of the 16X64 size.

```json
{
  "Coverage": {
    "Factor": 1.0
  },
  "InclusionOperator": "Or",
  "Inclusions": [
    {
      "Dimension": "SkuId",
      "Operator": "In",
      "Values": ["AURAWEB-COMPUTE-VM-STD-4X16"],
      "Coverage": {
        "Factor": 0.5
      }
    },
    {
      "Dimension": "SkuId",
      "Operator": "In",
      "Values": ["AURAWEB-COMPUTE-VM-STD-8X32"]
    },
    {
      "Dimension": "SkuId",
      "Operator": "In",
      "Values": ["AURAWEB-COMPUTE-VM-STD-16X64"],
      "Coverage": {
        "Factor": 2.0
      }
    }
  ]
}
```

## Usage-Based Commitment Without Flexibility

A reservation that covers a single SKU in a single region. The top-level `Coverage` applies to all usage matched by the inclusion rules.

```json
{
  "Coverage": {
    "Factor": 1.0
  },
  "InclusionOperator": "And",
  "Inclusions": [
    {
      "Dimension": "SkuId",
      "Operator": "In",
      "Values": ["AURAWEB-COMPUTE-VM-STD-8X32"]
    },
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1"]
    }
  ]
}
```

## Spend-Based Commitment with a Discount

A one-year flexible spend plan (SKU Price ID "AURAWEB-COMMITMENT-FLEXSPEND-1YR-ALL-UPFRONT", Commitment Discount Category "Spend", Pricing Unit "USD"). It covers all compute usage at 28 percent off its unit price, except GPU virtual machines at 12 percent off, and it does not cover dynamically priced usage. The plan is applied first to the usage with the highest discount.

```json
{
  "Coverage": {
    "Discount": 0.28
  },
  "ApplicationOrder": "HighestDiscountFirst",
  "InclusionOperator": "Or",
  "Inclusions": [
    {
      "Dimension": "SkuId",
      "Operator": "StartsWith",
      "Values": ["AURAWEB-COMPUTE-VM-GPU-"],
      "Coverage": {
        "Discount": 0.12
      }
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
      "Dimension": "PricingCategory",
      "Operator": "In",
      "Values": ["Dynamic"]
    }
  ]
}
```

The GPU rule comes first, because the first matching rule determines the coverage.

## Spend-Based Commitment with Published Unit Prices

A spend plan for which the *service provider* publishes the unit price of each covered SKU Price instead of a discount.

```json
{
  "ApplicationOrder": "HighestDiscountFirst",
  "InclusionOperator": "Or",
  "Inclusions": [
    {
      "Dimension": "SkuPriceId",
      "Operator": "In",
      "Values": ["AURAWEB-USEAST1-COMPUTE-ONDEMAND-STANDARD"],
      "Coverage": {
        "UnitPrice": 0.2765
      }
    },
    {
      "Dimension": "SkuPriceId",
      "Operator": "In",
      "Values": ["AURAWEB-USEAST1-COMPUTE-ONDEMAND-BURST"],
      "Coverage": {
        "UnitPrice": 0.0691
      }
    }
  ]
}
```

## Global Scope

A spend plan that covers all usage of the *service provider* at 10 percent off the unit price of covered usage.

```json
{
  "IsGlobalScope": true,
  "Coverage": {
    "Discount": 0.1
  }
}
```

## Complex Scope

When the coverage logic of a *commitment discount* exceeds what the object can express, the value for `IsComplexScope` is set to `true`, and the object does not determine coverage.

```json
{
  "IsComplexScope": true
}
```
