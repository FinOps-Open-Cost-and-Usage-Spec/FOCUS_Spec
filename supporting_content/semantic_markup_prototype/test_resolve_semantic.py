"""Tests for the checks in resolve_semantic.py. Run with: pytest test_resolve_semantic.py"""

import contextlib
import io
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from focus_semantic import Registry  # noqa: E402
from resolve_semantic import SemanticResolver  # noqa: E402

CU = "datasets/cost_and_usage"


def col(ident, display, dataset="CostAndUsage", folder=CU):
    return {"type": "col", "id": ident, "display": display, "dataset": dataset, "aliases": [],
            "anchor": f"datamodel.{dataset.lower()}.{ident.lower()}",
            "source": f"{folder}/columns/{ident.lower()}.md"}


ENTRIES = [
    {"type": "ds", "id": "CostAndUsage", "display": "Cost and Usage", "aliases": [],
     "anchor": "datamodel.costandusage", "source": f"{CU}/dataset.md"},
    col("BilledCost", "Billed Cost"),
    col("BilledCost", "Billed Cost", "InvoiceDetail", "datasets/invoice_detail"),
    col("ChargeCategory", "Charge Category"),
    col("ContractApplied", "Contract Applied"),
    col("Tags", "Tags"),
    {"type": "val", "id": "ChargeCategory.Usage", "column": "ChargeCategory", "value": "Usage",
     "dataset": "CostAndUsage", "display": '"Usage"', "aliases": [],
     "anchor": "datamodel.costandusage.chargecategory", "source": f"{CU}/columns/chargecategory.md"},
    {"type": "attr", "id": "JsonObjectFormat", "display": "JSON Object Format", "aliases": [],
     "anchor": "attributes.jsonobjectformat", "source": "attributes/json_object_format.md"},
    {"type": "omc", "id": "IncludesRegions", "display": "Includes Regions", "aliases": [],
     "anchor": "omc.includesregions", "source": "operating_model_conditions/includesregions.md"},
    {"type": "term", "id": "charge", "display": "Charge", "aliases": [],
     "anchor": "glossary:charge", "source": "glossary.md#glossary:charge"},
    {"type": "term", "id": "pascalcase", "display": "Pascal Case", "aliases": [],
     "anchor": "glossary:pascalcase", "source": "glossary.md#glossary:pascalcase"},
    {"type": "term", "id": "sku", "display": "SKU", "aliases": [],
     "anchor": "glossary:sku", "source": "glossary.md#glossary:sku"},
]


def run(body, path="supported_features/sample.md"):
    """Resolve body as the content of one source file; return the codes reported."""
    resolver = SemanticResolver(Registry(ENTRIES), strict=False, spec_dir=Path("/nonexistent"))
    lines = [f"<!-- focus:begin {path} -->\n", *(f"{line}\n" for line in body.splitlines()),
             f"<!-- focus:end {path} -->\n"]
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        resolver.run(lines)
    return re.findall(r"(?:WARN|ERROR) (FOCUS\d+)", err.getvalue())


IN_CU = f"{CU}/columns/billedcost.md"


@pytest.mark.parametrize("body", [
    "[Charge Category](#col) and [ChargeCategory](#col)",
    "[JSON Object Format](#attr) and [JsonObjectFormat](#attr)",
    "[includes regions](#omc) and [Includes Regions](#omc)",
    "A [charge](#term), [charges](#term), a [Charge](#term) and [SKUs](#term).",
    "[Charges](#term) start this sentence. [Pascal case](#term) can too: [Pascal Case](#term).",
    "Each [Pascal Case](#term) ID.",
    "[charge category](#col:ChargeCategory) [ChargeCategory](#col) uses [\"Usage\"](#val:ChargeCategory).",
    "[Billed Costs](#col:CostAndUsage.BilledCost) and [CostAndUsage.BilledCost](#col:CostAndUsage.BilledCost)",
    "Tags are words; `ChargeCategory` is code; [ChargeCategory](#datamodel.chargecategory).",
])
def test_clean(body):
    assert run(body) == []


@pytest.mark.parametrize("body,code", [
    ("[charge category](#col)", "FOCUS012"),
    ("[Chargecategory](#col)", "FOCUS012"),
    ("[JSON object format](#attr)", "FOCUS012"),
    ("[cost and usage](#ds)", "FOCUS012"),
    ("Each [Pascal case](#term) ID.", "FOCUS013"),
    ("A [CHARGE](#term).", "FOCUS013"),
    ("A [Charge](#term) mid-sentence.", None),
    ("[ChargeCategory](#col) is [Usage](#val:ChargeCategory)", "FOCUS014"),
    ("Rows with [\"Usage\"](#val:ChargeCategory) only.", "FOCUS015"),
    ("[*charge*](#term)", "FOCUS016"),
    ("## About [ChargeCategory](#col)", "FOCUS017"),
    ("[ChargeCategory](#col:ChargeCategory)", "FOCUS018"),
    ("[Charge Category](#col:ChargeCategory)", "FOCUS018"),
    ("[ContractApplied](#col:CostAndUsage.ContractApplied)", "FOCUS018"),
    ("The ChargeCategory column.", "FOCUS004"),
])
def test_reported(body, code):
    codes = run(body)
    # A capitalized term mid-sentence is the glossary's own form, so it is allowed
    assert codes == ([code] if code else [])


def test_qualifier_equal_to_file_dataset():
    assert run("[BilledCost](#col:CostAndUsage.BilledCost)", IN_CU) == ["FOCUS018"]
    assert run("[BilledCost](#col:InvoiceDetail.BilledCost)", IN_CU) == []


def test_value_in_its_own_column_file():
    assert run('Rows with ["Usage"](#val:ChargeCategory) only.', f"{CU}/columns/chargecategory.md") == []


def test_requirement_mixing_columnids_and_display_names():
    requirements = "## Requirements\n\n* [ChargeCategory](#col) MUST be null when [Billed Cost](#col) is 0.\n"
    # FOCUS003 reports the Display Name; FOCUS019 the mix within one requirement
    assert run(requirements, IN_CU) == ["FOCUS003", "FOCUS019"]


def test_untagged_columnid_exemptions():
    assert run("## Column ID\n\nChargeCategory\n") == []
    assert run("| ChargeCategory | text |\n") == []
    assert run('<a name="ChargeCategory"></a>\n') == []
    assert run("```\nChargeCategory\n```\n") == []
