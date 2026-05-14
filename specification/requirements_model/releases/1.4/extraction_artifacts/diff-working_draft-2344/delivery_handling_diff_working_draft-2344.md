
"Status": "ReviewNeeded",
"Notes": "Generated from extraction output. Requires review due to structural differences from the existing model, including Condition format, composite Requirement structure, and rule ID classification."

{+  "ModelRules": {+}
{+      "DatasetId": "",+}
{+      "DatasetName": "",+}
{+      "DatasetType": "ATT",+}
[-      "Condition": {},-]
{+        "Condition": [],+}
[-        "ATT-DeliveryHandling-A-002-M",-]
{+          "ATT-DeliveryHandling-A-002-C",+}
[-        "ATT-DeliveryHandling-A-003-C",-]
{+          "ATT-DeliveryHandling-A-005-C",+}
[-        "ATT-DeliveryHandling-A-006-C",-]
{+          "ATT-DeliveryHandling-A-006-O",+}
[-        "ATT-DeliveryHandling-A-007-O",-]
{+          "ATT-DeliveryHandling-A-007-M"+}
[-        "ATT-DeliveryHandling-A-008-C"-]
[-      "MustSatisfy": "Dataset conforming to DeliveryHandling attributes MUST adhere to the following requirements:",-]
{+        "MustSatisfy": "Dataset conforming to DeliveryHandling attribute MUST adhere to the following requirements:",+}
[-      "Requirement": {-]
[-        "CheckFunction": "AND",-]
[-        "Items": [-]
[-            "CheckFunction": "CheckModelRule",-]
[-            "ModelRuleId": "ATT-DeliveryHandling-A-001-M"-]
[-            "CheckFunction": "CheckModelRule",-]
[-            "ModelRuleId": "ATT-DeliveryHandling-A-002-M"-]
[-            "CheckFunction": "CheckModelRule",-]
[-            "ModelRuleId": "ATT-DeliveryHandling-A-003-C"-]
[-            "CheckFunction": "CheckModelRule",-]
[-            "ModelRuleId": "ATT-DeliveryHandling-A-006-C"-]
[-            "CheckFunction": "CheckModelRule",-]
[-            "ModelRuleId": "ATT-DeliveryHandling-A-007-O"-]
[-            "CheckFunction": "CheckModelRule",-]
[-            "ModelRuleId": "ATT-DeliveryHandling-A-008-C"-]
[-        ]-]
{+      "DatasetId": "",+}
{+      "DatasetName": "",+}
{+      "DatasetType": "ATT",+}
[-      "Condition": {},-]
{+        "Condition": [],+}
[-      "MustSatisfy": "FOCUS dataset MUST have its mechanism(s) for delivering dataset artifacts documented and accessible to practitioners (including whether Overwrite or Append is used and under which conditions).",-]
[-  "ATT-DeliveryHandling-A-002-M": {-]
[-      "Condition": {},-]
[-      "MustSatisfy": "FOCUS dataset MUST NOT require practitioners to deduplicate records within or across delivered dataset artifacts.",-]
{+        "MustSatisfy": "*FOCUS dataset* MUST NOT require practitioners to deduplicate records within or across delivered dataset artifacts.",+}
[-  "ATT-DeliveryHandling-A-003-C": {-]
{+    "ATT-DeliveryHandling-A-002-C": {+}
{+      "DatasetId": "",+}
{+      "DatasetName": "",+}
{+      "DatasetType": "ATT",+}
[-      "Condition": {},-]
{+        "Condition": [],+}
{+          "ATT-DeliveryHandling-A-003-M",+}
[-        "ATT-DeliveryHandling-A-004-M",-]
{+          "ATT-DeliveryHandling-A-004-M"+}
[-        "ATT-DeliveryHandling-A-005-M"-]
[-      "MustSatisfy": "When using Overwrite delivery mechanism, FOCUS dataset MUST adhere to the following additional requirements:",-]
{+        "MustSatisfy": "When using Overwrite delivery mechanism, *FOCUS dataset* MUST adhere to the following additional requirements:",+}
[-      "Requirement": {-]
[-        "CheckFunction": "AND",-]
[-        "Items": [-]
[-            "CheckFunction": "CheckModelRule",-]
[-            "ModelRuleId": "ATT-DeliveryHandling-A-004-M"-]
[-            "CheckFunction": "CheckModelRule",-]
[-            "ModelRuleId": "ATT-DeliveryHandling-A-005-M"-]
[-        ]-]
{+    "ATT-DeliveryHandling-A-003-M": {+}
{+      "DatasetId": "",+}
{+      "DatasetName": "",+}
{+      "DatasetType": "ATT",+}
[-      "Condition": {},-]
{+        "Condition": [],+}
[-      "MustSatisfy": "FOCUS dataset MUST represent a complete snapshot for a given delivery scope.",-]
{+        "MustSatisfy": "*FOCUS dataset* MUST represent a complete snapshot for a given *delivery scope*.",+}
[-  "ATT-DeliveryHandling-A-005-M": {-]
{+      "DatasetId": "",+}
{+      "DatasetName": "",+}
{+      "DatasetType": "ATT",+}
[-      "Condition": {},-]
{+        "Condition": [],+}
[-      "MustSatisfy": "FOCUS dataset MUST supersede all previously delivered dataset artifacts for the same delivery scope.",-]
{+        "MustSatisfy": "*FOCUS dataset* MUST supersede all previously delivered *dataset artifacts* for the same *delivery scope*.",+}
[-  "ATT-DeliveryHandling-A-006-C": {-]
{+    "ATT-DeliveryHandling-A-005-C": {+}
{+      "DatasetId": "",+}
{+      "DatasetName": "",+}
{+      "DatasetType": "ATT",+}
[-      "Condition": {},-]
{+        "Condition": [],+}
[-      "MustSatisfy": "FOCUS dataset MUST preserve all previously delivered dataset artifacts when using Append delivery mechanism.",-]
{+        "MustSatisfy": "*FOCUS dataset* MUST preserve all previously delivered *dataset artifacts* when using Append delivery mechanism.",+}
[-  "ATT-DeliveryHandling-A-007-O": {-]
{+    "ATT-DeliveryHandling-A-006-O": {+}
{+      "DatasetId": "",+}
{+      "DatasetName": "",+}
{+      "DatasetType": "ATT",+}
[-      "Condition": {},-]
{+        "Condition": [],+}
[-      "MustSatisfy": "FOCUS dataset SHOULD have delivered dataset artifacts accompanied by corresponding FOCUS Metadata.",-]
{+        "MustSatisfy": "*FOCUS dataset* SHOULD have delivered *dataset artifacts* accompanied by corresponding FOCUS Metadata.",+}
[-  "ATT-DeliveryHandling-A-008-C": {-]
{+    "ATT-DeliveryHandling-A-007-M": {+}
{+      "DatasetId": "",+}
{+      "DatasetName": "",+}
{+      "DatasetType": "ATT",+}
[-      "Condition": {},-]
{+        "Condition": [],+}
{+          "ATT-DeliveryHandling-A-008-M",+}
{+          "ATT-DeliveryHandling-A-009-C",+}
{+          "ATT-DeliveryHandling-A-010-C",+}
{+          "ATT-DeliveryHandling-A-011-M"+}
{+        "MustSatisfy": "*FOCUS dataset* delivery mechanism documentation MUST adhere to the following requirements:",+}
{+    "ATT-DeliveryHandling-A-008-M": {+}
{+      "DatasetId": "",+}
{+      "DatasetName": "",+}
{+      "DatasetType": "ATT",+}
{+        "Condition": [],+}
[-      "MustSatisfy": "FOCUS dataset MUST have its mechanism for correlating dataset artifact with the FOCUS Metadata Schema object documented and accessible to practitioners when the Metadata is delivered.",-]
{+        "MustSatisfy": "*FOCUS dataset* delivery mechanism documentation MUST include the delivery mechanism used (Overwrite or Append).",+}
{+    "ATT-DeliveryHandling-A-009-C": {+}
{+      "DatasetId": "",+}
{+      "DatasetName": "",+}
{+      "DatasetType": "ATT",+}
{+      "Order": 90,+}
{+        "Condition": [],+}
{+        "MustSatisfy": "*FOCUS dataset* delivery mechanism documentation MUST include the conditions under which each delivery mechanism applies when more than one delivery mechanism is used.",+}
{+    "ATT-DeliveryHandling-A-010-C": {+}
{+      "DatasetId": "",+}
{+      "DatasetName": "",+}
{+      "DatasetType": "ATT",+}
{+      "Order": 100,+}
{+        "Condition": [],+}
{+        "MustSatisfy": "*FOCUS dataset* delivery mechanism documentation MUST include the mechanism for correlating *dataset artifacts* with the FOCUS Metadata Schema object when the Metadata is delivered.",+}
{+    "ATT-DeliveryHandling-A-011-M": {+}
{+      "DatasetId": "",+}
{+      "DatasetName": "",+}
{+      "DatasetType": "ATT",+}
{+      "Order": 110,+}
{+        "Condition": [],+}
{+        "MustSatisfy": "*FOCUS dataset* delivery mechanism documentation MUST be accessible to practitioners.",+}
    }
  }
}