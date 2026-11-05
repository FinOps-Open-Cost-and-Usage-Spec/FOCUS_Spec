"""Semantic review pass: decide the open items and correct existing tags, logging every change.

This records the judgment calls of the semantic review (see SEMANTIC_REVIEW.md) as
rules, so the review can be read, rerun after the mechanical conversion, or rolled
back. It runs on the output of convert_all.sh:

* OPEN_ITEMS is build/convert-run.txt from convert_all.sh (every NEEDS-REVIEW item).
* CORRECTIONS below lists the existing tags that were wrong, with the reason.
* decide() turns each open item into a tag, or leaves it plain with a reason.

Without --apply it only writes the log.

Usage: semantic_review.py SPEC_DIR OPEN_ITEMS LOG.tsv [--apply]
"""
import csv
import json
import re
import sys
from pathlib import Path

SPEC = Path(sys.argv[1]).resolve()
OPEN = Path(sys.argv[2])
LOG = Path(sys.argv[3])
APPLY = "--apply" in sys.argv
sys.path.insert(0, str(SPEC.parent / "supporting_content/semantic_markup_prototype"))
from build_registry import split_front_matter  # noqa: E402
from focus_semantic import Registry  # noqa: E402
from tag_sources import LINK, CODE_SPAN, Tagger  # noqa: E402

registry = Registry(json.loads((SPEC / "semantic-registry.json").read_text()))
cols = {}
for e in registry.by_type["col"]:
    cols.setdefault(e["id"], {})[e["dataset"]] = e
meta_by = {(e.get("collection"), e["display"]): e for e in registry.by_type["meta"]}
ds_by_display = {e["display"]: e for e in registry.by_type["ds"]}
display_col = {}
for e in registry.by_type["col"]:
    display_col.setdefault(e["display"], e["id"])

# ---------------------------------------------------------------- existing tags to correct
CORRECTIONS = [
    ("datasets/cost_and_usage/columns/hostprovidername.md", "[Service Provider](#col:ServiceProviderName)",
     "[Service Provider](#term)", "the party that deploys on the host, not the ServiceProviderName column"),
    ("datasets/billing_period/columns/billingperiodcreated.md", "[Billing Period](#term) record",
     "[Billing Period](#ds) record", "a record of the Billing Period dataset, not the billing period time window"),
    ("metadata/schema/column_definition/deprecated.md", "[Dataset Instance](#meta)",
     "[Dataset Instance](#term)", "the dataset instance that holds the column, not the Dataset Instance metadata object"),
    ("datasets/contract_commitment/columns/contractcommitmentperiodend.md",
     "[Contract Commitment Period Start](#col:ContractPeriodStart)",
     "[Contract Commitment Period Start](#col)",
     "the text and the example (with Contract Commitment Period End) mean ContractCommitmentPeriodStart, not ContractPeriodStart"),
    ("datasets/sku_price/columns/skupricecreated.md", "[SKU Price](#term) record",
     "[SKU Price](#ds) record", "a record of the SKU Price dataset; the glossary SKU Price construct excludes prices"),
    ("datasets/sku_price/columns/skupricelastupdated.md", "[SKU Price](#term) record",
     "[SKU Price](#ds) record", "a record of the SKU Price dataset; the glossary SKU Price construct excludes prices"),
    ("appendix/sku_price_examples/price_effectivity_and_currency.md", "[SKU Price](#term) record",
     "[SKU Price](#ds) record", "a record of the SKU Price dataset; the glossary SKU Price construct excludes prices"),
]

# ---------------------------------------------------------------- open items
items = {}
for raw in OPEN.read_text().splitlines():
    m = re.match(r"\s*([^:]+):(\d+): NEEDS-REVIEW (.*)", raw)
    if not m:
        continue
    f, n, msg = m.group(1), int(m.group(2)), m.group(3)
    pm = re.search(r'plain display name "([^"]+)"', msg) or re.match(r"([A-Za-z.]+): ", msg)
    if pm:
        items.setdefault((f, n), set()).add(pm.group(1))

SKU_FILES = ("supported_features/catalog_discovery_and_price_estimation.md",
             "appendix/sku_price_examples/price_effectivity_and_currency.md",
             "appendix/sku_price_examples/commitment_pricing.md")
CHARGE_CONTEXT = re.compile(r"\bcharges?('s)?\b|\bbilled\b|Cost and Usage|\bconsumption\b|\bcorrections?\b", re.I)


def col_target(colid, dataset):
    return ("col", cols[colid][dataset]) if dataset in cols.get(colid, {}) else (None, f"{colid} not in {dataset}")


def parent_bullet(lines, n):
    """Dataset or collection named by the nearest less-indented bullet above line n."""
    indent = len(lines[n - 1]) - len(lines[n - 1].lstrip())
    for i in range(n - 2, -1, -1):
        s = lines[i]
        if s.strip().startswith("* ") and len(s) - len(s.lstrip()) < indent:
            return re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s.strip()[2:]).strip()
        if s.startswith("#"):
            return None
    return None


def sentence_before(text, start):
    head = text[:start]
    cut = max(head.rfind(". "), head.rfind("? "), head.rfind(": "))
    return head[cut + 1:] if cut >= 0 else head


def decide(f, n, lines, text, start, phrase):
    """text is the whole line and start the phrase's position in it, so context spans links."""
    line = lines[n - 1]
    before, after = text[:start], text[start + len(phrase):]
    plain_before = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", before)

    # names that are also glossary terms
    if phrase in ("SKU Price", "Billing Period", "Contract Commitment"):
        dsid = ds_by_display[phrase]
        if (re.match(r"\s*(\*\*)?\s*(datasets?|records?|record's|schema|snapshots|column names)\b", after)
                or re.match(r"\s*\[(FOCUS datasets?|Charge Category|dataset)", after)
                or re.match(r",\s*\[[^\]]+\]\(#ds\)", after)
                or re.match(r"\s+and\s+\[(Cost and Usage|Invoice Detail)\]\(#ds\)", after)
                or re.search(r"(Joining|joining .{0,40}to|include|only for|represents|\(#ds\),? and)\s*$", before)):
            return ("ds", dsid), "names the dataset (followed by dataset/record/schema, or joined or listed as a dataset)"
        return (None, "the concept, used as ordinary prose")
    if phrase in ("List Unit Price", "Contracted Unit Price", "Billing Currency", "Availability Zone"):
        if f == "glossary.md":
            return (None, "the glossary entry's own term")
        if "= 1 - (" in line:
            return (None, "a formula about unit prices in general")
        colid = display_col[phrase]
        fds = Tagger(registry, f).dataset
        target = fds if fds in cols[colid] else "CostAndUsage"
        return col_target(colid, target), "Display Name capitalization means the column (#2765)"
    if phrase == "Dataset Instance":
        if f == "metadata/dataset_instance/dataset_instance_overview.md" and "metadata object" in after[:20]:
            return ("meta", meta_by[(None, "Dataset Instance")]), "the Dataset Instance metadata object"
        if f.startswith("supported_features/") and line.strip().startswith("* "):
            return ("meta", meta_by[(None, "Dataset Instance")]), "listed under Applicable Metadata"
        return (None, "the dataset instance as a concept")

    # metadata names
    if phrase == "FOCUS Version":
        if re.match(r"\s*\d", after) or before.rstrip().endswith("adopt a new"):
            return (None, "the version of FOCUS, not the field")
        return ("meta", meta_by[("Schema", "FOCUS Version")]), "the FocusVersion field of the schema object"
    if phrase == "Data Generator Version":
        return ("meta", meta_by[("Schema", "Data Generator Version")]), "the DataGeneratorVersion field"
    if phrase in ("Data Generator", "DataGenerator"):
        return (None, "the data generator role (no glossary entry yet)")

    # shared columns
    colid = phrase if phrase in cols else display_col.get(phrase)
    if colid is None:
        return (None, "not a column")
    is_list_entry = bool(re.fullmatch(r"\s*\* (\[[^\]]+\]\([^)]*\)|\S+)\s*", line))
    if f.endswith("rate_optimization_and_contract_evaluation.md"):
        if is_list_entry:
            parent = parent_bullet(lines, n)
            return col_target(colid, parent), f"listed under {parent}"
        if colid in ("BillingCurrency", "BilledCost", "BillingAccountId"):
            return col_target(colid, "CostAndUsage"), "a charge's value in Cost and Usage"
        if colid == "ContractId":
            return col_target(colid, "SkuPrice"), "a SKU Price record's contract"
        if (re.search(r"\bon\s*$", before) and colid == "SkuPriceId") or \
                (re.search(r"[Mm]atching on\s*$", before) and colid not in ("BillingCurrency",)):
            return (None, "the join key, meaning both datasets")
        if re.search(r"(published under (that|the|a)|since a)\s*$", before):
            return col_target(colid, "SkuPrice"), "a price published in the SKU Price dataset"
        if CHARGE_CONTEXT.search(sentence_before(plain_before, len(plain_before))):
            return col_target(colid, "CostAndUsage"), "the sentence is about a charge in Cost and Usage"
        return col_target(colid, "SkuPrice"), "the sentence is about SKU Price records"
    if f in SKU_FILES:
        return col_target(colid, "SkuPrice"), "a SKU Price record's value"
    if f == "supported_features/contract_commitments.md":
        if is_list_entry:
            return col_target(colid, parent_bullet(lines, n)), "listed under its dataset"
        return col_target(colid, "CostAndUsage"), "the query reads Cost and Usage"
    if f == "supported_features/billed_cost_and_invoice_alignment.md":
        return col_target(colid, "CostAndUsage"), "the page's query reads Cost and Usage"
    if f.startswith("appendix/examples/commitment_discount_flexibility_examples/"):
        return col_target(colid, "CostAndUsage"), "a Cost and Usage charge in the example"
    if colid == "BillingAccountId":
        return col_target(colid, "CostAndUsage"), "the account a charge belongs to"
    if f == "appendix/invoice_and_billing_period_handling.md":
        if colid == "InvoiceDetailId":
            return col_target(colid, "InvoiceDetail"), "in the Invoice Detail dataset"
        return (None, "means the column in both Invoice Detail and Cost and Usage")
    if f == "appendix/json_object_examples/contract_applied_examples.md":
        if colid == "ContractId":
            return (col_target(colid, "ContractCommitment"), "the contract in the Contract Commitment dataset") if "ContractId =" in text[start:start + 14] else (None, "a ContractApplied element value, not a column")
        if colid == "ChargeCategory":
            return col_target(colid, "CostAndUsage"), "a Cost and Usage charge in the example"
        return (None, "a ContractApplied element value, not a column")
    if f == "datasets/cost_and_usage/dataset.md" and colid == "ContractCommitmentId":
        if "Contract Commitment dataset" in plain_before:
            return col_target(colid, "ContractCommitment"), "the column in the Contract Commitment dataset"
        return (None, "a property inside ContractApplied, not a column")
    if f == "datasets/invoice_detail/columns/invoicedetailgrain.md":
        return (None, "a ContractApplied element, not a column")
    if f == "datasets/sku_price/columns/pricingregionid.md" and colid == "RegionId":
        return col_target(colid, "CostAndUsage"), "contrasted with PricingRegionId: the usage record's region"
    if f == "datasets/sku_price/columns/pricingservicename.md" and colid == "ServiceName":
        return col_target(colid, "CostAndUsage"), "contrasted with PricingServiceName: the usage record's service"
    return (None, "undecided")


def applicable_metadata(f, lines):
    """Tag every entry of an Applicable Metadata list by its nesting."""
    changes = []
    inside = False
    for n, line in enumerate(lines, 1):
        if line.startswith("## "):
            inside = line.strip() == "## Applicable Metadata"
            continue
        if not inside or not line.strip().startswith("* ") or "](#" in line:
            continue
        name = line.strip()[2:].strip()
        parent = parent_bullet(lines, n)
        coll = None
        if parent:
            p = meta_by.get((None, parent)) or next((e for (c, d), e in meta_by.items() if d == parent), None)
            coll = p["id"] if p else None
        entity = meta_by.get((coll, name))
        if entity:
            changes.append((n, name, "meta", entity, "listed under Applicable Metadata"))
    return changes


rows = []
files = sorted({f for f, _ in items} | {c[0] for c in CORRECTIONS} |
               {str(p.relative_to(SPEC)) for p in SPEC.glob("supported_features/*.md")})
for f in files:
    path = SPEC / f
    original = path.read_text()
    lines = original.split("\n")
    tagger = Tagger(registry, f, split_front_matter(original)[0].get("dataset") or None)
    tagger.infer_dataset(original)
    new_lines = list(lines)

    for cf, old, new, why in CORRECTIONS:
        if cf != f:
            continue
        hits = [i for i, l in enumerate(new_lines) if old in l]
        assert len(hits) == 1, (f, old, hits)
        i = hits[0]
        new_lines[i] = new_lines[i].replace(old, new, 1)
        rows.append(dict(file=f, line=i + 1, change="corrected", before=old, after=new, reason=why))

    meta_changes = applicable_metadata(f, new_lines) if f.startswith("supported_features/") else []
    for n, name, kind, entity, why in meta_changes:
        before = new_lines[n - 1]
        tag = tagger.reference(kind, entity, name)
        new_lines[n - 1] = before.replace(name, tag, 1)
        rows.append(dict(file=f, line=n, change="added", before=name, after=tag, reason=why))

    for (inf, n), phrases in sorted(items.items()):
        if inf != f or any(r["file"] == f and r["line"] == n and r["change"] == "added" and "Applicable Metadata" in r["reason"] for r in rows):
            continue
        line = new_lines[n - 1]
        parts = CODE_SPAN.split(line)
        pos = 0
        for pi in range(len(parts)):
            if pi % 2:
                pos += len(parts[pi])
                continue
            pieces = LINK.split(parts[pi])
            for k in range(0, len(pieces), 3):
                chunk = pieces[k]
                chunk_pos = pos
                matches = []
                for rx in (tagger.name_re, tagger.id_word):
                    if rx is not None:
                        matches += [(m.start(1), m.group(1)) for m in rx.finditer(chunk)]
                out, last = [], 0
                for start, phrase in sorted(set(matches)):
                    if start < last or phrase not in phrases:
                        continue
                    target, why = decide(f, n, new_lines, line, chunk_pos + start, phrase)
                    if target is None or target[0] is None:
                        reason = why if target is None else target[1]
                        rows.append(dict(file=f, line=n, change="left", before=phrase, after="", reason=reason))
                        continue
                    kind, entity = target
                    tag = tagger.reference(kind, entity, phrase)
                    out.append(chunk[last:start] + tag)
                    last = start + len(phrase)
                    rows.append(dict(file=f, line=n, change="added", before=phrase, after=tag, reason=why))
                out.append(chunk[last:])
                pieces[k] = "".join(out)
                pos += len(chunk)
                if k + 2 < len(pieces):
                    pos += len(pieces[k + 1]) + len(pieces[k + 2]) + 4
            parts[pi] = "".join(pieces[k] if k % 3 == 0 else (f"[{pieces[k]}]" if k % 3 == 1 else f"({pieces[k]})")
                                for k in range(len(pieces)))
        new_lines[n - 1] = "".join(parts)

    # Plurals of a Display Name do not resolve by text, so they take an explicit ID
    if f in ("appendix/correction_handling_examples/closed_billing_period.md",
             "appendix/correction_handling_examples/open_billing_period.md",
             "datasets/cost_and_usage/columns/listunitprice.md"):
        entity = cols["SkuPriceId"]["CostAndUsage"]
        for i, l in enumerate(new_lines):
            if l.startswith("#"):
                continue
            for m in reversed(list(re.finditer(r"(?<![\[\w])SKU Price IDs(?![\w\]])", l))):
                tag = tagger.reference("col", entity, "SKU Price IDs")
                l = l[:m.start()] + tag + l[m.end():]
                rows.append(dict(file=f, line=i + 1, change="added", before="SKU Price IDs", after=tag,
                                 reason="plural of the SKU Price ID column on charges; plurals need an explicit ID"))
            new_lines[i] = l
    # An italic possessive of a glossary term is the term
    if f in ("datasets/sku_price/columns/skupricedescription.md", "datasets/sku_price/columns/skupriceeligibility.md"):
        for i, l in enumerate(new_lines):
            for _ in range(l.count("*SKU Price's*")):
                rows.append(dict(file=f, line=i + 1, change="added", before="*SKU Price's*",
                                 after="[SKU Price's](#term:sku-price)",
                                 reason="italic possessive of the SKU Price glossary term"))
            new_lines[i] = l.replace("*SKU Price's*", "[SKU Price's](#term:sku-price)")

    if APPLY and new_lines != lines:
        path.write_text("\n".join(new_lines))

with LOG.open("w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["file", "line", "change", "before", "after", "reason"], delimiter="\t")
    w.writeheader()
    w.writerows(rows)
from collections import Counter
print(Counter(r["change"] for r in rows))
print(Counter(r["reason"] for r in rows if r["change"] == "left").most_common())
