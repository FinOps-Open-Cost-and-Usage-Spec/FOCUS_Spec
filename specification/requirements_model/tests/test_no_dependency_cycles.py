"""
No rule may depend on itself, directly or through the rules it depends on.

A rule points at another rule in two ways, and both count here:

* entries in its `ValidationCriteria.Dependencies` array
* `CheckModelRule` references anywhere in its `Requirement` or `Condition`
  (including inside `AND`/`OR` `Items`)

When those references lead back to the rule they started from, there is no order
in which the rules can be evaluated: each one is waiting on the other to resolve
first. A validator following the references has to either loop forever or pick a
place to break the chain on its own.
"""
import pytest


def _collect_check_model_rules(node, out):
    """Recursively collect CheckModelRule targets from a Requirement/Condition tree."""
    if not isinstance(node, dict):
        return
    check_function = node.get("CheckFunction")
    if check_function in {"AND", "OR"}:
        for item in node.get("Items") or []:
            _collect_check_model_rules(item, out)
    elif check_function == "CheckModelRule":
        target = node.get("ModelRuleId")
        if isinstance(target, str):
            out.add(target)


def _build_graph(rules):
    """Map each rule id to the set of rule ids it depends on."""
    graph = {}
    for rule_id, rule in rules.items():
        edges = set()
        vc = rule.get("ValidationCriteria") or {}
        for dep in vc.get("Dependencies") or []:
            if isinstance(dep, str):
                edges.add(dep)
        _collect_check_model_rules(vc.get("Requirement") or {}, edges)
        _collect_check_model_rules(vc.get("Condition") or {}, edges)
        # Dangling references are covered by test_dependencies_exist.py
        graph[rule_id] = {e for e in edges if e in rules}
    return graph


def _find_cycles(graph):
    """Return cycles found by DFS, each normalized so a given loop is reported once."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}
    cycles = set()

    def visit(node, stack):
        color[node] = GRAY
        stack.append(node)
        for nxt in sorted(graph[node]):
            if color[nxt] == GRAY:
                cycle = tuple(stack[stack.index(nxt):])
                pivot = cycle.index(min(cycle))
                cycles.add(cycle[pivot:] + cycle[:pivot])
            elif color[nxt] == WHITE:
                visit(nxt, stack)
        stack.pop()
        color[node] = BLACK

    for node in sorted(graph):
        if color[node] == WHITE:
            visit(node, [])
    return sorted(cycles, key=lambda c: (len(c), c))


@pytest.mark.dependency(name="no_dependency_cycles", scope="session")
def test_no_dependency_cycles(cr_json):
    """No rule may depend on itself, directly or transitively."""
    rules = cr_json.get("ModelRules") or {}
    cycles = _find_cycles(_build_graph(rules))

    assert not cycles, (
        f"{len(cycles)} dependency cycle(s) found in ModelRules:\n" +
        "\n".join(
            "- " + " -> ".join(cycle) + f" -> {cycle[0]}"
            for cycle in cycles
        )
    )
