#!/usr/bin/env python3
import json
from collections import deque
import logging
import argparse
import sys

def init_logger(level):
    # Create a logger instance
    logger = logging.getLogger(__name__)
    if (logger.hasHandlers()):
        logger.handlers.clear()
    match level:
        case 'DEBUG':
            logger.setLevel(logging.DEBUG)
        case 'INFO':
            logger.setLevel(logging.INFO)
        case 'WARNING':
            logger.setLevel(logging.WARNING)
        case 'ERROR':
            logger.setLevel(logging.ERROR)
        case 'CRITICAL':
            logger.setLevel(logging.CRITICAL)
        case _:
            logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger

def get_args():
    parser = argparse.ArgumentParser(description='SCR Table Generator.')
    parser.add_argument('-t', '--table-name', default="FOCUS", help='Table to generate SCR table for')
    parser.add_argument('-f', '--scr-filename', type=str, default='scr-1.2.json', help='SCR definition filename to load')
    parser.add_argument('--logging-level', type=str, default='WARNING', choices={"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}, help='Logging level to use')
    return parser.parse_args()

def summarize_check(node):
    if not node:
        return ""
    func = node.get("CheckFunction")
    if func == "CheckSCR":
        return f"Check {node.get('SCR')}"
    elif "ColumnName" in node:
        val = node.get("Value")
        return f"{func}({node['ColumnName']}, {val})" if val is not None else f"{func}({node['ColumnName']})"
    elif "Items" in node:
        return f"{func} of [" + ", ".join(summarize_check(i) for i in node["Items"]) + "]"
    elif "ColumnAName" in node and "ColumnBName" in node:
        return f"{func}({node['ColumnAName']}, {node['ColumnBName']})"
    return func or ""

def generate_markdown(data, generate_table_name):
    output_tables = []

    for table_name, table in data.get("ConformanceTables", {}).items():
        if table_name != generate_table_name:
            continue

        headers = [
            "ConformanceRuleId", "Function", "Status", "ApplicabilityCriteria",
            "Type", "mustSatisfy", "Requirement", "Condition"
        ]
        md = [
            f"# Conformance Table: {table_name}",
            "",
            "| " + " | ".join(headers) + " |",
            "| " + " | ".join(["---"] * len(headers)) + " |"
        ]

        visited = set()
        queue = deque(table["ConformanceRules"])
        all_rows = {}

        while queue:
            rule_id = queue.popleft()
            if rule_id in visited or rule_id not in data["ConformanceRules"]:
                continue
            visited.add(rule_id)

            rule = data["ConformanceRules"][rule_id]
            vc = rule.get("ValidationCriteria", {})
            req = vc.get("Requirement", {})
            cond = vc.get("Condition", {})

            # Resolve dependencies from Requirement
            deps = []
            if req.get("CheckFunction") == "AND":
                deps = [i.get("SCR") for i in req.get("Items", []) if i.get("CheckFunction") == "CheckSCR"]
            elif req.get("CheckFunction") == "CheckSCR":
                deps = [req.get("SCR")]
            
            for dep in deps:
                if dep and dep not in visited:
                    queue.append(dep)

            row = [
                rule_id,
                rule.get("Function", ""),
                rule.get("Status", ""),
                ", ".join(rule.get("ApplicabilityCriteria", [])),
                rule.get("Type", ""),
                vc.get("mustSatisfy", ""),
                summarize_check(req),
                summarize_check(cond)
            ]
            all_rows[rule_id] = "| " + " | ".join(cell.replace("\n", " ").replace("|", "\\|") for cell in row) + " |"

        for rule_id in sorted(all_rows):
            md.append(all_rows[rule_id])

        output_tables.append("\n".join(md))

    return "\n\n".join(output_tables)

if __name__ == "__main__":
    args = get_args()

    logger = init_logger(args.logging_level)

    with open(args.scr_filename, "r") as f:
        scr_data = json.load(f)
    
    markdown_output = generate_markdown(scr_data, generate_table_name=args.table_name)

    with open("conformance_tables.md", "w") as f:
        f.write(markdown_output)
    
    print("Markdown table generated: conformance_tables.md")
