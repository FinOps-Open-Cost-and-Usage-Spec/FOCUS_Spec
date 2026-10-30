#!/usr/bin/env python3
"""Classify every difference between two assembled spec.md files.

Used by compare_rendered.sh for migration step 3 (compare how the new source
publishes against the old). Each changed line is reduced to its visible text
plus its inline references, and the difference is sorted into:

* whitespace      only spacing differs (e.g., table padding)
* link added      a reference that was plain text is now a link
* link removed    a link is now plain text (a repeat link the rules drop)
* link retargeted the same text links somewhere else (investigate)
* italics         emphasis added or removed around the same text
* text changed    the visible words differ (investigate; should be 0)

Usage:
    classify_rendered.py BASE.md CURRENT.md [--examples N] [--detail FILE]
"""

import argparse
import collections
import difflib
import re
import sys

LINK = re.compile(r"\[((?:[^\[\]]|\[[^\]]*\])*)\]\((#[^)\s]*)\)")


def links(line):
    return [(re.sub(r"[*_]", "", m.group(1)).strip(), m.group(2)) for m in LINK.finditer(line)]


def plain(line):
    text = LINK.sub(lambda m: m.group(1), line)
    return re.sub(r"[\s*_]+", "", text)


def italic_chars(line):
    return LINK.sub(lambda m: m.group(1), line).count("*")


def kind_of(target):
    if target.startswith("#glossary:"):
        return "glossary term"
    for prefix, name in (("#datamodel.", "column or dataset"), ("#attributes.", "attribute"),
                         ("#operatingmodelconditions.", "operating model condition"),
                         ("#metadata.", "metadata"), ("#schemas.", "schema")):
        if target.startswith(prefix):
            return name
    return "other"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("base")
    parser.add_argument("current")
    parser.add_argument("--examples", type=int, default=3)
    parser.add_argument("--detail", help="write every classified item to this file")
    args = parser.parse_args()

    a = open(args.base, encoding="utf-8").read().splitlines()
    b = open(args.current, encoding="utf-8").read().splitlines()
    heading = ""
    headings = {}
    for n, line in enumerate(b):
        if line.startswith("#"):
            heading = line.lstrip("#").strip()
        headings[n] = heading

    items = []  # (category, detail, where, new line)
    unaligned = 0
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        if i2 - i1 != j2 - j1:
            unaligned += 1
            items.append(("text changed", f"{i2 - i1} line(s) became {j2 - j1}", f"line {j1 + 1}", ""))
            continue
        for k, (old, new) in enumerate(zip(a[i1:i2], b[j1:j2])):
            where = f"line {j1 + k + 1} ({headings.get(j1 + k, '')})"
            if old.split() == new.split():
                items.append(("whitespace", "", where, new))
                continue
            if plain(old) != plain(new):
                items.append(("text changed", "", where, new))
                continue
            if (italic_chars(old) - italic_chars(new)) % 2:
                items.append(("text changed", "an unpaired * was added or removed", where, new))
                continue
            before, after = collections.Counter(links(old)), collections.Counter(links(new))
            removed, added = before - after, after - before
            retargeted = [(t, o, n) for (t, o) in removed for (t2, n) in added if t == t2]
            for text, old_target, new_target in retargeted:
                items.append(("link retargeted", f'"{text}" {old_target} -> {new_target}', where, new))
                removed[(text, old_target)] -= 1
                added[(text, new_target)] -= 1
            for (text, target), count in added.items():
                for _ in range(max(count, 0)):
                    items.append(("link added", f'"{text}" -> {target}', where, new))
            for (text, target), count in removed.items():
                for _ in range(max(count, 0)):
                    items.append(("link removed", f'"{text}" ({target})', where, new))
            if italic_chars(old) != italic_chars(new) and not (added or removed or retargeted):
                items.append(("italics", "", where, new))

    counts = collections.Counter(c for c, *_ in items)
    lines_changed = len({w for _, _, w, _ in items})
    print(f"{lines_changed} changed line(s), {len(items)} difference(s)")
    for category in ("whitespace", "link added", "link removed", "link retargeted", "italics", "text changed"):
        print(f"  {category:16s} {counts.get(category, 0):6d}")
    by_kind = collections.Counter()
    for category, detail, *_ in items:
        if category in ("link added", "link removed"):
            m = re.search(r"(#\S+?)\)?$", detail)
            by_kind[(category, kind_of(m.group(1)) if m else "other")] += 1
    for (category, kind), n in sorted(by_kind.items()):
        print(f"    {category:12s} {kind:28s} {n:6d}")

    for category in ("link retargeted", "text changed"):
        sample = [i for i in items if i[0] == category][:args.examples]
        for _, detail, where, _ in sample:
            print(f"  e.g. {category}: {where} {detail}")

    if args.detail:
        with open(args.detail, "w", encoding="utf-8") as out:
            for category, detail, where, new in items:
                out.write(f"{category}\t{where}\t{detail}\n")
    if unaligned:
        print(f"  ({unaligned} block(s) changed length and could not be compared line by line)", file=sys.stderr)


if __name__ == "__main__":
    main()
