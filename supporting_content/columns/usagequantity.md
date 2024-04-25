# Column: UsageQuantity

## Example provider mappings

Current column mappings found in available data sets:

| Provider | Data set                | Column               |
|----------|-------------------------|----------------------|
| AWS      | CUR                     | lineItem/UsageAmount |
| Azure    | Cost Details            | quantity             |
| GCP      | BigQuery Billing Export | usage.amount               |

## Discussion Topics - Resulting in hold for post 1.0 action 

Issue Discussion: The group debated how to handle the usage quantity and pricing quantity within their system, particularly focusing on differentiating between usage charges and purchase records. The main point of contention was whether the "usage quantity" should apply uniformly across usage and purchase scenarios or be restricted to just usage scenarios.

Proposal: The initial proposal advocated returning to a previous approach where "usage quantity" was used only for usage-related charges, arguing that its application to purchases could lead to misinterpretations about actual usage versus purchased amounts.
Counterpoints and Suggestions: Various participants brought up alternatives and nuances, such as maintaining distinct units for better clarity and addressing block pricing with an additional column. There was significant back-and-forth on whether to rename or redefine the "usage quantity" to reflect its broader application more accurately.

Terminology and Definitions: The conversation also delved into the appropriate terminology and definitions for different columns, with a focus on ensuring clarity and avoiding confusion in their application across different scenarios.

The group resume the discussion on this topic after dealing with other items.

Usage Quantity Definition: The group debates whether "usage quantity" should strictly apply to actual usage scenarios or if it could be extended to include purchase scenarios where the purchased quantity does not match the charged quantity due to minimum purchase requirements.

Normative Language: There is extensive discussion on how to frame normative text around "usage quantity" to ensure it is clear and applicable across different scenarios without causing confusion or misinterpretation.

Terminology and Clarity: The participants consider renaming "usage quantity" to something more general like "distinct quantity" or "measured quantity" to better capture its intended use across both usage and purchase contexts.

Potential Conflicts and Ambiguity: Concerns are raised about the potential for misinterpretation, especially in purchase scenarios, where the term might imply actual usage rather than just the quantity purchased.

Final Decision:
The group seems to lean towards clarifying the definition of "usage quantity" for usage scenarios only and excluding purchase scenarios from this definition. They discuss creating a new column or adjusting the existing framework to handle purchase-related quantities separately, ensuring clarity and preventing misinterpretation. The decision includes moving forward with drafting and proposing changes to the specification to reflect this narrowed application, with the possibility of revisiting and expanding it in future updates.
