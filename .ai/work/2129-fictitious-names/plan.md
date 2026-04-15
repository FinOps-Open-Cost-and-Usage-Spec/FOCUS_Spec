# Plan: #2129 Fictitious Names — Replacement Safety Rules

## Replacement Safety Protocol

These rules MUST be followed for ALL find-and-replace operations on issue #2129 to prevent substring corruption bugs like the "StoreStackrp" incident in PR #2247.

### Rule 1: Build a Complete Variant Inventory First

Before replacing ANY name in a file, grep for ALL case/format variants:
- Exact case: `AwesomeCorp`
- With spaces: `Awesome Corp`
- ALL CAPS: `AWESOMECORP`
- Hyphenated: `awesome-corp`, `Awesome-Corp`
- Underscored: `awesome_corp`
- CamelCase compounds: `AwesomeCorpDemo`
- As substring in IDs: `cr-arc-acme-001`, `x_awesome_column1`

### Rule 2: Replace Longest Matches First

When multiple search patterns overlap, always process the longest pattern first to prevent partial matches:

**Correct order:**
1. `AwesomeCorp` → `Acme Corp` (longest first)
2. `Awesome Corp` → `Acme Corp`
3. `AwesomeDB` → target service name
4. `Acme Co` → target provider name (only AFTER "Acme Corp" replacements are done)

**Incorrect order:**
1. `Acme Co` → `StoreStack` (would corrupt "Acme Corp" → "StoreStackrp")

### Rule 3: Use Exact Whole-String Matches

Never use a prefix or substring as the search pattern. Always match the complete name:
- Search for `AwesomeCorp` NOT `AwesomeCo`
- Search for `Acme Corp` NOT `Acme Co` (unless "Acme Co" is the actual distinct string)
- Search for `ACMECORP` NOT `ACME`

When a shorter name IS a legitimate distinct value (e.g., "Acme Co" is a different entity from "Acme Corp"), handle the longer variant first per Rule 2.

### Rule 4: Handle Compound Identifiers Explicitly

Names embedded in identifiers (IDs, anchors, tags, resource paths) must be replaced with compound forms of the fictitious name:

| Original Pattern | Replacement Pattern | Context |
|:---|:---|:---|
| `awssavingsplan` | `aurawebflexiblespendplan` | Markdown anchor IDs |
| `awsreservedinstance` | `aurawebresourcereservation` | Markdown anchor IDs |
| `azurereservation` | `crestnoderesourcereservation` | Markdown anchor IDs |
| `gcpresourcecud` | `latticescaleresourcereservation` | Markdown anchor IDs |
| `gcpflexcud` | `latticescaledynamiccomputecommitment` | Markdown anchor IDs |
| `cr-arc-acme-001` | `cr-arc-auraweb-001` (or similar) | Resource IDs in CSVs |
| `x_awesome_column1` | Context-appropriate replacement | Custom columns |

### Rule 5: Verify After Every Replacement

After completing replacements in each file, run these verification checks:

```bash
# 1. Grep for fragments of OLD names to catch partial replacements
grep -i 'awesome\|acmecorp\|tinycloud\|serenity' <file>

# 2. Grep for mangled NEW names (fictitious name + unexpected suffix)
grep -oE '(StackLens|StoreStack|OmniQuery|CrestNode|AuraWeb|LatticeScale|SprintCanvas|PipelCRM)[a-z]+' <file>

# 3. Verify no real provider names leaked in
grep -i 'amazon web services\|microsoft azure\|google cloud platform' <file>
```

### Rule 6: Distinguish Provider vs Customer Roles

Many original files use "ACME" variants for BOTH provider and customer roles. Before replacing, identify which role the name plays in context:

- **Provider role** → Replace with the appropriate fictitious Data Generator (e.g., Aura Web, CrestNode, StoreStack)
- **Customer role** → Replace with a fictitious Customer (Acme Corp, AeroScale, GearPeak Outdoors)

The mapping depends on the file's scenario context, not just the name string.

### Rule 7: Handle CSV and Markdown in Tandem

When a markdown file references CSV data files:
1. Check both the markdown AND the corresponding CSVs for the same names
2. Ensure the replacement is consistent across both
3. Note that CSVs may use different column schemas — correction handling CSVs lack provider columns entirely

## PR Checklist

For each PR in the #2129 series, before marking ready for review:

- [ ] All name variants inventoried (Rule 1)
- [ ] Replacements applied longest-first (Rule 2)
- [ ] No substring matches used (Rule 3)
- [ ] Compound identifiers handled (Rule 4)
- [ ] Post-replacement grep verification passed (Rule 5)
- [ ] Provider/customer roles correctly distinguished (Rule 6)
- [ ] Markdown and CSV files consistent (Rule 7)
