#!/usr/bin/env python3
import argparse
import json
from collections import deque
from build_helpers import init_logger


def get_args():
    parser = argparse.ArgumentParser(description='CR Table Generator.')
    parser.add_argument('-t', '--dataset-name', default="FOCUS", help='Dataset to generate CR table for')
    parser.add_argument('-f', '--cr-filename', type=str, default='cr-1.2.json', help='Conformance definition filename to load')
    parser.add_argument('--logging-level', type=str, default='INFO', choices={"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}, help='Logging level to use')
    return parser.parse_args()

def summarize_check(node):
    if not node:
        return ""
    func = node.get("CheckFunction")
    if func == "CheckConformanceRule":
        return f"Check {node.get('ConformanceRuleId')}"
    elif "ColumnName" in node:
        val = node.get("Value")
        if "Value" in node:
            return f"{func}({node['ColumnName']}, {val})" if val is not None else f"{func}({node['ColumnName']}, null)"
        return f"{func}({node['ColumnName']})"
    elif "Items" in node:
        return f"{func} of [" + ", ".join(summarize_check(i) for i in node["Items"]) + "]"
    elif "ColumnAName" in node and "ColumnBName" in node:
        if "EqualsColumnName" in node:
            return f"{func}({node['ColumnAName']}, {node['ColumnBName']}) -> {node['EqualsColumnName']}"
        return f"{func}({node['ColumnAName']}, {node['ColumnBName']})"
    return func or ""

def generate_markdown(data, dataset_name, logger):
    output_tables = []
    dataset = data["ConformanceDatasets"].get(dataset_name, {})
    if not dataset:
        logger.warning(f'Dataset {dataset_name} not found')

    headers = [
        "ConformanceRuleId",
        "Function",
        "Reference",
        "ApplicabilityCriteria",
        "mustSatisfy",
        "KeyWord",            
        "Requirement",
        "Condition",
        "Type",
        "CRVersionIntroduced",
        "Status"
    ]
    md = [
        f"# Conformance Dataset: {dataset_name}",
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |"
    ]

    visited = set()
    queue = deque(dataset["ConformanceRules"])
    all_rows = {}

    while queue:
        rule_id = queue.popleft()
        if rule_id in visited or rule_id not in data["ConformanceRules"]:
            continue
        logger.info(f'Adding rule {rule_id}')
        visited.add(rule_id)

        rule = data["ConformanceRules"][rule_id]
        vc = rule.get("ValidationCriteria", {})
        req = vc.get("Requirement", {})
        cond = vc.get("Condition", {})

        # Resolve dependencies from Requirement
        deps = []
        if req.get("CheckFunction") == "AND":
            deps = [i.get("ConformanceRuleId") for i in req.get("Items", []) if i.get("CheckFunction") == "CheckConformanceRule"]
        elif req.get("CheckFunction") == "CheckConformanceRule":
            deps = [req.get("ConformanceRuleId")]
        
        for dep in deps:
            if dep and dep not in visited:
                queue.append(dep)

        row = [
            rule_id,
            rule.get("Function", ""),
            rule.get("Reference", ""),
            ", ".join(rule.get("ApplicabilityCriteria", [])),
            vc.get("mustSatisfy", ""),
            vc.get("KeyWord", ""),
            summarize_check(req),
            summarize_check(cond),
            rule.get("Type", ""),
            rule.get("CRVersionIntroduced", ""),
            rule.get("Status", "")
        ]
        all_rows[rule_id] = "| " + " | ".join(cell.replace("\n", " ").replace("|", "\\|") for cell in row) + " |"

    for rule_id in sorted(all_rows):
        md.append(all_rows[rule_id])

    output_tables.append("\n".join(md))

    return "\n\n".join(output_tables)

if __name__ == "__main__":
    args = get_args()

    logger = init_logger(args.logging_level)

    with open(args.cr_filename, "r") as f:
        cr_data = json.load(f)
    
    markdown_output = generate_markdown(cr_data, dataset_name=args.dataset_name, logger=logger)

    with open("conformance_tables.md", "w") as f:
        f.write(markdown_output + '\n')
    
    logger.info("Markdown table generated: conformance_tables.md")
