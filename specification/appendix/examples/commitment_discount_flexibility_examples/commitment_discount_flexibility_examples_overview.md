# Examples: Commitment Discount Flexibility

A usage-based [commitment discount](#term) obligates a customer to a usage amount for one or more related SKUs in return for reduced rates. For example, when a usage-based [commitment discount](#term) is purchased to cover a specific database SKU, this commitment will cover every hour over the period where at least one instance of this SKU is running. The usage-based commitment can cover 1 resource over the hour, or in the case of [commitment discount flexibility](#term), it can cover a portion of 1 resource or multiple resources at a time.

When mixing usage-based commitment discounts with and without [commitment discount flexibility](#term) and [CommitmentDiscountQuantity](#col) measured by time, it is important to differentiate the [CommitmentDiscountUnit](#col) for each type of [commitment discount](#term). In each scenario below, [commitment discounts](#term) *without* [commitment discount flexibility](#term) applied use "Hour" as the *[CommitmentDiscountUnit](#col)*, and conversely commitment discounts *with* [commitment discount flexibility](#term) applied use "Normalized Hour" as the *[CommitmentDiscountUnit](#col)*.

For more details on exactly how [commitment discounts](#term) purchase and usage rows appear with and without [commitment discount flexibility](#term), see the following scenarios:
