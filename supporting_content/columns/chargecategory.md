# Column: ChargeCategory

## Example provider mappings

Current column mappings found in available data sets:

## Example usage scenarios

Current scenarios considered:

### Option 1

| Value      | Description                          |
| :--------- | :------------------------------------|
| Refund     | Any adjustments that are applied after the original usage or purchase row. Adjustments may be related to multiple charges. (NOTE: Tax excluded)   |
| Credit     | Credits assoicated with promotional usage or incentives   |
| Purchase   | Charges for the acquisition of a service or resource bought upfront or on a recurring basis.              |
| Tax        | Applicable taxes that are levied by the relevant authorities. Tax charges may vary depending on factors such as the location, jurisdiction, and local or federal regulations. |
| Usage      | Charges based on the quantity of a service or resource that was consumed over a given period of time.     |

ISSUE: Tax cannot be classified correctly, assuming refunds and purchases have a tax implication then we would need to look for negative tax values matching the refund line in order ot acertain the total value of the refund.

### Option 2:

| Value      | Description                          |
| :--------- | :------------------------------------|
| Purchase   | Charges for the acquisition of a service or resource bought upfront or on a recurring basis.              |
| Tax        | Applicable taxes that are levied by the relevant authorities. Tax charges may vary depending on factors such as the location, jurisdiction, and local or federal regulations. |
| Usage      | Charges based on the quantity of a service or resource that was consumed over a given period of time.     |


New Column: Adjustment Category

| Value      | Description                          |
| :--------- | :------------------------------------|
| NULL       | Default value for all incomming charges.             |
| Refund     | Refunded related to usage or purchase specific activities (expects a matching 'tax' transaction) |
| Credit     | Promotional / negotiated / incentive credits provided at providers discression (does NOT expect a matching 'tax' transaction)       |

Permutations:

| Charge Category     | Adjustment Category         | Example usage                 |
| :--------- | :------------------------------------|:------------------------------|
|Usage       | NULL                                 | general usage                                                                                |
|Usage       | Refund                               | service specific refunds /..e.g miss billing                                                 |
|Usage       | Credit                               | service specific incentives                                                                  |
|Purchase    | NULL                                 | general marketplace or 3rd party purchase                                                    |
|Purchase    | Refund                               | bulk / general refunds                                                                       |
|Purchase    | Credit                               | Non-service / usage specific credits                                                         |
|Tax         | NULL                                 | general tax                                                                                  |
|Tax         | Refund                               | tax refund for usage or purchase refunded                                                    |
|Tax         | Credit                               | NOT APPLICABLE                                                                               |

### Option 3:

| Value      | Description                          |
| :--------- | :------------------------------------|
| Credit     | Credits assoicated with promotional usage or incentives   |
| Purchase   | Charges for the acquisition of a service or resource bought upfront or on a recurring basis.              |
| Tax        | Applicable taxes that are levied by the relevant authorities. Tax charges may vary depending on factors such as the location, jurisdiction, and local or federal regulations. |
| Usage      | Charges based on the quantity of a service or resource that was consumed over a given period of time.     |

New Column: Adjustment Category

| Value      | Description                          |
| :--------- | :------------------------------------|
| NULL       | Default value for all incomming charges.             |
| Refund     | Refunded related to usage or purchase specific activities (expects a matching 'tax' transaction) |
| Bulk Refund     | General refund (expects a matching 'tax' transaction) |
| Rounding Error     | Small corrections - Applicable to current billing period only |
| Other    | Catch all       |

Permutations:

| Charge Category     | Adjustment Category         | Example usage                 |
| :--------- | :------------------------------------|:------------------------------|
|Usage       | NULL                                 | general usage                                                                                |
|Usage       | Refund                               | service specific refunds /..e.g miss billing                                                 |
|Purchase    | NULL                                 | general marketplace or 3rd party purchase                                                    |
|Purchase    | Refund                               | specific / 3rd party refund                                                                  |
|Tax         | NULL                                 | general tax                                                                                  |
|Tax         | Refund                               | tax refund for usage or purchase refunded                                                    |
|Credit      | NULL                                 | service specific incentives                                                                  |
|Credit      | Other                                | vendor specific / non usage related incentives                                               |


## Discussion / Scratch space

- What adjustment categories do we need to group?
- Do we need to normalize adjustment categories?
- Refunds - $s coming back after the original charge
- Credits are typically based on agreements for migration of workloads, or promotional items negotiated with the provider
- Balance transfers - how do you show what a balance transfer is if in the unliely event you close an account with a positive value and open a new account

### Example mappings for normalized values

| Provider  | Usage                                                                                                | Purchase                                                         | Adjustment               | Tax |
| --------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------ | --- |
