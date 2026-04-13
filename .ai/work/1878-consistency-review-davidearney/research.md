# Research: Issue #1878 — 1.4 Consistency Review (davidearney items)

## Source
GitHub issue #1878 "[Process] 1.4 consistency review" — comments by davidearney.

## Items Confirmed Still Present in working_draft

### 1. `## Content constraints` header (sentence case) — should be title case
- `specification/datasets/cost_and_usage/columns/billedcost.md:43`
- `specification/datasets/cost_and_usage/columns/billingaccountid.md:29`

### 2. Content Constraints table cell value capitalization
- `pricingquantity.md:44`: `Number Range` → `Number range`
- `servicecategory.md:34`: `Allowed Values` → `Allowed values`

### 3. Missing comma after `e.g.` / `i.e.`
- `chargecategory.md:48`: `e.g promotional` → `e.g., promotional`
- `pricingquantity.md:32`: `i.e. when` → `i.e., when` (appears twice on line)

### 4. Double hyphen `--` → em dash `—`
- `attributes_overview.md:3`: two occurrences of ` -- `

### 5. Lowercase normative `must` in `tags.md:47`
- Non-normative explanatory prose uses `must` twice
- Resolution: Option B — rephrase as non-normative

### 6. Contractions in formal prose
- `pricingquantity.md:32`: `it's` × 2 → `it is`
- `listcost.md:32`: `it's` → `it is`
- `tags.md:49`: `let's assume` → `assume`

### 7. Numerals for small cardinal numbers
- `tags.md:49`: `1 [*sub account*]` → `one [*sub account*]`; `1 virtual machine` → `one virtual machine`

### 8. Subject–verb agreement error
- `listcost.md:32`: `whether cost are aggregated` → `whether costs are aggregated`

### 9. Unquoted allowed values in dimension column tables
Editorial guidelines require values enclosed in double quotation marks.
Affected files:
- `chargecategory.md`: Usage, Purchase, Tax, Credit, Adjustment
- `chargeclass.md`: Correction
- `chargefrequency.md`: One-Time, Recurring, Usage-Based
- `servicecategory.md`: all service category values
- `billing_period/columns/billingperiodstatus.md`: Open, Closed

## Items Resolved / No Longer Applicable
- Double spaces after periods: not present
- `etc` without period: `invoice_handling.md` does not exist in working_draft
- Numerals in `tags.md:31`: already uses words

---
> ⚠️ **Cleanup required before merge**: After final approval, delete `.ai/work/1878-consistency-review-davidearney/` before merging.
