#!/usr/bin/env python3

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


sys.dont_write_bytecode = True
MODULE_PATH = Path(__file__).with_name("quote_audit.py")
SPEC = importlib.util.spec_from_file_location("quote_audit", MODULE_PATH)
QUOTE_AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(QUOTE_AUDIT)


class JsonDetectionTests(unittest.TestCase):
    def test_markdown_link_followed_by_colon_is_not_json(self):
        line = '[ChargeCategory](#datamodel.costandusage.chargecategory) is "Purchase": example'
        start = line.index('"Purchase"')
        self.assertFalse(QUOTE_AUDIT.is_json_span(line, start))

    def test_markdown_link_before_value_is_not_json(self):
        line = '[ChargeCategory](#datamodel.costandusage.chargecategory) is "Purchase".'
        start = line.index('"Purchase"')
        self.assertFalse(QUOTE_AUDIT.is_json_span(line, start))

    def test_json_object_is_json(self):
        line = '| {"ProgramType": "Flexible Spend Plan"} |'
        for value in ('"ProgramType"', '"Flexible Spend Plan"'):
            self.assertTrue(QUOTE_AUDIT.is_json_span(line, line.index(value)))

    def test_json_array_is_json(self):
        line = '["Usage", "Tax"]'
        for value in ('"Usage"', '"Tax"'):
            self.assertTrue(QUOTE_AUDIT.is_json_span(line, line.index(value)))

    def test_quote_inside_markdown_link_is_not_json(self):
        line = '[the "quoted" label](#target)'
        self.assertFalse(QUOTE_AUDIT.is_json_span(line, line.index('"quoted"')))


class ScanningTests(unittest.TestCase):
    def scan(self, text):
        return QUOTE_AUDIT.scan_text(
            Path("example.md"), text, {"ChargeCategory"}, None
        )

    def test_linked_entity_value_is_detected(self):
        records = self.scan(
            '[ChargeCategory](#datamodel.costandusage.chargecategory) is "Purchase".'
        )
        self.assertEqual(records[0]["classification"], "value_high")

    def test_multiple_values_on_one_line_are_detected(self):
        records = self.scan('ChargeCategory is "Usage" or "Purchase".')
        self.assertEqual([record["value"] for record in records], ["Usage", "Purchase"])
        self.assertTrue(all(record["classification"] == "value_high" for record in records))

    def test_inline_code_is_ignored(self):
        self.assertEqual(self.scan('Use `value = "Usage"` here.'), [])

    def test_inline_code_inside_quotation_preserves_quote_pairing(self):
        records = self.scan(
            'Use "when ChargeCategory is `Purchase`" or '
            '"ChargeCategory MAY be `Usage`".'
        )
        self.assertEqual(
            [record["value"] for record in records],
            [
                "when ChargeCategory is `Purchase`",
                "ChargeCategory MAY be `Usage`",
            ],
        )

    def test_raw_html_code_is_ignored(self):
        self.assertEqual(self.scan('<pre>{"Value": "Usage"}</pre>'), [])

    def test_multiline_raw_html_code_is_ignored(self):
        records = self.scan(
            '<td title="layout"><pre>\n'
            '{"Value": "Usage"}\n'
            '</pre> ChargeCategory is "Tax".\n'
        )
        self.assertEqual([record["value"] for record in records], ["Tax"])

    def test_fenced_code_is_ignored(self):
        self.assertEqual(self.scan('```json\r\n{"Value": "Usage"}\r\n```\r\n'), [])

    def test_tilde_fenced_code_is_ignored(self):
        self.assertEqual(self.scan('~~~json\n{"Value": "Usage"}\n~~~\n'), [])

    def test_crlf_prose_is_scanned(self):
        records = self.scan('ChargeCategory is "Usage".\r\n')
        self.assertEqual(records[0]["value"], "Usage")

    def test_entity_order_is_deterministic(self):
        entities = QUOTE_AUDIT.find_entities(
            "AlphaBeta and GammaBeta", {"GammaBeta", "AlphaBeta"}
        )
        self.assertEqual(entities, ["AlphaBeta", "GammaBeta"])

    def test_worktree_symlink_is_not_followed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target.md"
            target.write_text('ChargeCategory is "Usage".', encoding="utf-8")
            link = root / "link.md"
            link.symlink_to(target.name)
            self.assertEqual(QUOTE_AUDIT.read_source(link), target.name)


if __name__ == "__main__":
    unittest.main()
