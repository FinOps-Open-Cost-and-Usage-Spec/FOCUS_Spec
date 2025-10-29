# tests/test_rule_id_duplicates_in_sources.py
import json
from pathlib import Path
import pytest

@pytest.mark.dependency(name="no_duplicate_rule_ids_in_source_files", scope="session")
def test_no_duplicate_rule_ids_in_source_files():
    # tests/.../this_file.py -> .../specification/conformance
    REQUIREMENTS_MODEL = Path(__file__).resolve().parents[1]
    SRC_DIR = REQUIREMENTS_MODEL / "model_rules"

    assert SRC_DIR.is_dir(), f"Source folder not found: {SRC_DIR}"

    json_files = sorted(SRC_DIR.rglob("*.json"))
    assert json_files, f"No JSON files found under {SRC_DIR}"

    within_file_dupes = []     # [(file, json_path_hint, dup_key)]
    across_file_map = {}       # rule_id -> [files...]
    across_file_dupes = []     # [(rule_id, [files...])]

    # Helper: record duplicate keys in ANY dict; also capture top-level keys for cross-file check.
    def scan_file_for_dupes(path: Path):
        # We'll capture the *last* object_pairs_hook call as "top level" (json builds objects bottom-up)
        last_pairs = None
        json_path_stack = []  # rough stack to hint where a duplicate occurred

        def hook(pairs):
            nonlocal last_pairs
            # track duplicates at this dict level
            seen = set()
            local_dupes = []
            for k, _ in pairs:
                if k in seen:
                    local_dupes.append(k)
                else:
                    seen.add(k)
            if local_dupes:
                # json doesn't give us a formal path; we provide a simple depth hint
                within_file_dupes.extend((str(path), f"dict@depth{len(json_path_stack)}", k) for k in local_dupes)

            # this dict becomes a value of its parent next; push/pop depth markers
            json_path_stack.append("{}")
            obj = dict(pairs)
            json_path_stack.pop()

            # save the last seen pairs as top-level candidate
            last_pairs = pairs
            return obj

        text = path.read_text(encoding="utf-8")
        try:
            json.loads(text, object_pairs_hook=hook)
        except json.JSONDecodeError as e:
            raise AssertionError(f"Invalid JSON in {path}:\n{e}") from e

        # last_pairs now corresponds to the top-level object in this file
        if isinstance(last_pairs, list):
            for k, _ in last_pairs:
                across_file_map.setdefault(k, []).append(str(path))

    # Scan all files
    for p in json_files:
        scan_file_for_dupes(p)

    # Build cross-file duplicates report
    for rule_id, files in sorted(across_file_map.items()):
        if len(files) > 1:
            across_file_dupes.append((rule_id, files))

    # Assertions with clean, actionable output
    msgs = []
    if within_file_dupes:
        msgs.append("Duplicate keys within a source JSON file (keys repeated in the same dict):\n" +
                    "\n".join(f"- {f} @ {where}: '{k}'" for f, where, k in within_file_dupes))
    if across_file_dupes:
        msgs.append("ConformanceRule Ids defined in multiple files:\n" +
                    "\n".join(f"- {rid}: {', '.join(files)}" for rid, files in across_file_dupes))

    assert not msgs, "\n\n".join(msgs)
