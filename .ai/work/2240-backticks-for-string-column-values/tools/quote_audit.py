#!/usr/bin/env python3

"""Inventory double-quoted prose for issue 2240 without modifying source files."""

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path


QUOTED = re.compile(r'"([^"\n]+)"')
INLINE_CODE_OR_HTML = re.compile(r"`[^`]*`|<[^>]*>")
RAW_CODE_TAG = re.compile(r"<(/?)(code|pre)\b[^>]*>", re.IGNORECASE)
LINK = re.compile(r"\[([^]]+)\]\([^)]+\)")
PREDICATE = re.compile(
    r"(?:\b(?:is|is not|are|are not|be|set to|transitions? to|categorized as|"
    r"has|have|uses?|accepts?)\s*)$",
    re.IGNORECASE,
)
KEY_CONTEXT = re.compile(
    r"(?:\b(?:key|keys|prefix|string|term|phrase|suffix|collection)\s*)$",
    re.IGNORECASE,
)


def read_source(path, source_ref=None):
    if source_ref is None:
        if path.is_symlink():
            return path.readlink().as_posix()
        return path.read_text(encoding="utf-8")
    result = subprocess.run(
        ["git", "show", f"{source_ref}:{path.as_posix()}"],
        check=True,
        stdout=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8")


def tracked_markdown_paths(source_ref):
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", source_ref],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    return [Path(value) for value in result.stdout.splitlines() if value.endswith(".md")]


def visible_segments(line, raw_code_tag=None):
    """Return prose segments and any unclosed raw HTML code/pre tag."""

    raw_segments = []
    cursor = 0
    while cursor < len(line):
        if raw_code_tag:
            close = re.search(rf"</{raw_code_tag}\s*>", line[cursor:], re.IGNORECASE)
            if close is None:
                break
            cursor += close.end()
            raw_code_tag = None
            continue

        opening = RAW_CODE_TAG.search(line, cursor)
        while opening is not None and opening.group(1):
            opening = RAW_CODE_TAG.search(line, opening.end())
        if opening is None:
            raw_segments.append((cursor, line[cursor:]))
            break
        if cursor < opening.start():
            raw_segments.append((cursor, line[cursor : opening.start()]))
        raw_code_tag = opening.group(2).lower()
        cursor = opening.end()

    prose_segments = []
    for base_offset, segment in raw_segments:
        segment_cursor = 0
        for match in INLINE_CODE_OR_HTML.finditer(segment):
            if segment_cursor < match.start():
                prose_segments.append(
                    (base_offset + segment_cursor, segment[segment_cursor : match.start()])
                )
            segment_cursor = match.end()
        if segment_cursor < len(segment):
            prose_segments.append(
                (base_offset + segment_cursor, segment[segment_cursor:])
            )
    return prose_segments, raw_code_tag


def visible_line(line, raw_code_tag=None):
    """Mask excluded spans without changing quote positions on the line."""

    segments, raw_code_tag = visible_segments(line, raw_code_tag)
    masked = [" "] * len(line)
    for offset, segment in segments:
        masked[offset : offset + len(segment)] = segment
    return "".join(masked), raw_code_tag


def normalized_context(text):
    text = LINK.sub(r"\1", text)
    return re.sub(r"[*_]", "", text)


def unmatched_opener(line, position, opener, closer):
    stack = []
    for index, character in enumerate(line[:position]):
        if character == opener:
            stack.append(index)
        elif character == closer and stack:
            stack.pop()
    return stack[-1] if stack else None


def matching_closer(line, opener_index, opener, closer):
    depth = 0
    for index in range(opener_index, len(line)):
        if line[index] == opener:
            depth += 1
        elif line[index] == closer:
            depth -= 1
            if depth == 0:
                return index
    return None


def is_json_span(line, start):
    """Return true only when the quote is inside an object or non-link array."""

    if unmatched_opener(line, start, "{", "}") is not None:
        return True

    bracket = unmatched_opener(line, start, "[", "]")
    if bracket is None:
        return False
    close = matching_closer(line, bracket, "[", "]")
    if close is not None and close + 1 < len(line) and line[close + 1] == "(":
        return False
    return True


def discover_entities(paths, texts):
    entities = set()
    owners = {}
    id_heading = re.compile(r"^## (?:Column|Metadata|Dataset|Property) ID\s*$")
    anchor = re.compile(r"^([A-Z][A-Za-z0-9.]*) (?:MUST|SHOULD|MAY) adhere to")

    for path in paths:
        lines = texts[path].splitlines()
        for index, line in enumerate(lines):
            if id_heading.match(line):
                for candidate in lines[index + 1 : index + 4]:
                    candidate = candidate.strip()
                    if re.fullmatch(r"[A-Z][A-Za-z0-9.]*", candidate):
                        entities.add(candidate)
                        owners[path] = candidate
                        break
            match = anchor.match(line)
            if match:
                entities.add(match.group(1))
    return entities, owners


def find_entities(text, entities):
    return sorted(
        (
            entity
            for entity in entities
            if re.search(rf"(?<![A-Za-z0-9]){re.escape(entity)}(?![A-Za-z0-9])", text)
        ),
        key=lambda entity: (len(entity), entity),
    )


def classify(line, start, end, value, known_entities, owner):
    raw_before = line[max(0, start - 220) : start]
    before = normalized_context(raw_before).rstrip()
    after = normalized_context(line[end : end + 140]).lstrip()
    entities = find_entities(before, known_entities)

    if is_json_span(line, start):
        return "exclude_json", "JSON syntax"
    if value in {"true", "false"}:
        return "exclude_non_string", "Boolean literal"
    if value.startswith(("MUST ", "SHOULD ", "MAY ")):
        return "exclude_ordinary", "Quoted requirement sentence"
    if re.search(r"(?:allowed|valid) value(?:s)?(?: other than)?\s*$", before, re.I):
        return "value_high", "Explicit allowed-value context"
    if re.match(r"^\s*\(capitalized\) refers to a specific allowed value\b", after, re.I):
        return "value_high", "Explicit allowed-value explanation"
    if re.search(r"(?:only the single string|reserved value)\s*$", before, re.I):
        return "value_high", "Explicit string-value context"
    if KEY_CONTEXT.search(before) or re.match(r"^\s*(?:key|keys|collection)\b", after, re.I):
        return "exclude_key", "Property/key notation"
    if re.search(r"(?:values?|status|category|unit|type)\s+of\s*$", before, re.I):
        return "value_high", "Explicit value context"
    if entities and PREDICATE.search(before):
        return "value_high", f"Entity predicate ({entities[-1]})"
    if re.search(r"\[[^]]+\]\([^)]*(?:datamodel|metadata)[^)]*\)", raw_before) and PREDICATE.search(before):
        return "value_high", "Linked entity predicate"
    if entities and re.search(r"\b(?:MUST|MAY|SHOULD)\b", before):
        return "value_high", f"Normative entity context ({entities[-1]})"
    if re.search(r"\b(?:set to|categorized as|values? (?:are|is|for)|denomination (?:is|of)|called)\s*$", before, re.I):
        return "value_high", "Explicit data-value wording"
    if line.lstrip().startswith("|") and re.search(r"\bExamples?:", line, re.I):
        return "value_high", "String example table"
    if re.search(r"\]\([^)]*(?:datamodel|metadata)[^)]*\)\s*:\s*$", line[:start]):
        return "value_high", "Entity designation"
    if re.search(r"\b(?:column|property)\b", before, re.I) and entities:
        return "value_review", f"Column/property context ({entities[-1]})"
    if owner:
        return "value_review", f"Owning entity file ({owner})"
    return "ambiguous", "No deterministic value relationship"


def scan_text(path, text, known_entities, owner):
    records = []
    fenced = False
    raw_code_tag = None
    for line_number, line in enumerate(text.splitlines(), 1):
        if raw_code_tag:
            prose_line, raw_code_tag = visible_line(line, raw_code_tag)
            if not prose_line.strip():
                continue
        elif re.match(r"^(?:`{3,}|~{3,})", line):
            fenced = not fenced
            continue
        elif fenced:
            continue
        else:
            prose_line, raw_code_tag = visible_line(line)
        line_records = []
        for match in QUOTED.finditer(prose_line):
            start = match.start()
            end = match.end()
            value = line[start + 1 : end - 1]
            classification, reason = classify(
                line, start, end, value, known_entities, owner
            )
            line_records.append(
                {
                    "classification": classification,
                    "reason": reason,
                    "file": path.as_posix(),
                    "line": line_number,
                    "column": start + 1,
                    "value": value,
                    "context": line.strip(),
                }
            )
        if any(record["classification"] == "value_high" for record in line_records):
            for record in line_records:
                if record["classification"] in {"ambiguous", "value_review"}:
                    record["classification"] = "value_high"
                    record["reason"] = "Same line as explicit value context"
        records.extend(line_records)
    return records


def scan(paths, source_ref=None):
    texts = {path: read_source(path, source_ref) for path in paths}
    known_entities, owners = discover_entities(paths, texts)
    records = []
    for path in paths:
        records.extend(scan_text(path, texts[path], known_entities, owners.get(path)))
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-ref", help="Read each path from this Git revision")
    parser.add_argument(
        "--tracked-markdown-ref",
        help="Inventory Markdown paths tracked by this Git revision",
    )
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args()

    paths = [Path(value) for value in args.paths]
    if args.tracked_markdown_ref:
        if paths:
            parser.error("paths cannot be combined with --tracked-markdown-ref")
        paths = tracked_markdown_paths(args.tracked_markdown_ref)
    if not paths:
        parser.error("provide paths or --tracked-markdown-ref")

    writer = csv.DictWriter(
        sys.stdout,
        fieldnames=["classification", "reason", "file", "line", "column", "value", "context"],
        delimiter="\t",
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(scan(paths, args.source_ref))


if __name__ == "__main__":
    main()
