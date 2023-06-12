# Charge Type

A charge type indicates whether the record represents an upfront or recurring fee, cost of usage that already occurred, an after-the-fact adjustment (e.g., credits), or taxes.

## Allowed values

| Value      | Description                                                                                                                                                                   |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Adjustment` | Any adjustments that are applied after the original usage or purchase record. Adjustments may be related to multiple charges.                                                 |
| `Purchase`   | Charges for the acquisition of a service or resource bought upfront or on a recurring basis.                                                                                  |
| `Tax`        | Applicable taxes that are levied by the relevant authorities. Tax charges may vary depending on factors such as the location, jurisdiction, and local or federal regulations. |
| `Usage`      | Charges based on the quantity of a service or resource that was consumed over a given period of time.                                                                         |
