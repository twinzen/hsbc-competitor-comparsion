"""Build the competitor AI knowledge graph.

Reads source.json (hand-curated from research_notes/Competitor AI products and achievements),
validates it, expands product shorthand (by / uses / caps) into explicit edges, and writes:

  kg.json      nodes + edges, the canonical graph
  nodes.csv    one row per entity (for Neo4j / Gephi / spreadsheets)
  edges.csv    one row per relationship (source, rel, target, attributes)
  ../reports/competitor-ai-knowledge-graph.html   interactive viewer (template.html + kg.json)

Usage: python3 knowledge-graph/build.py
"""
import csv
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPORT = ROOT / "reports" / "competitor-ai-knowledge-graph.html"
PLACEHOLDER = "/*__KG_DATA__*/null"

NODE_TYPES = {"institution", "product", "capability", "partner", "person", "initiative", "external"}
STATUSES = {"live", "rollout", "pilot", "announced", "historical"}
AI_KINDS = {"agentic", "genai", "ml", "rules", "none"}
CONFS = {"verified", "secondary", "unverified"}


def fail(msg):
    sys.exit(f"build.py: {msg}")


def main():
    src = json.loads((HERE / "source.json").read_text())
    group_ids = {g["id"] for g in src["groups"]}

    nodes = [{**c, "type": "capability"} for c in src["capabilities"]] + src["nodes"]
    by_id = {}
    for n in nodes:
        if n["id"] in by_id:
            fail(f"duplicate id {n['id']}")
        if n["type"] not in NODE_TYPES:
            fail(f"{n['id']}: unknown type {n['type']}")
        for field, allowed in (("status", STATUSES), ("ai", AI_KINDS), ("conf", CONFS)):
            if field in n and n[field] not in allowed:
                fail(f"{n['id']}: bad {field} {n[field]!r}")
        if n.get("group") and n["group"] not in group_ids:
            fail(f"{n['id']}: unknown group {n['group']}")
        by_id[n["id"]] = n

    edges = []

    def add(s, rel, t, attrs=None):
        for end in (s, t):
            if end not in by_id:
                fail(f"edge {s} -{rel}-> {t}: unknown node {end}")
        edges.append({"source": s, "rel": rel, "target": t, **(attrs or {})})

    for n in nodes:
        if n["type"] != "product":
            continue
        owner = by_id.get(n.pop("by", None))
        if not owner or owner["type"] != "institution":
            fail(f"{n['id']}: product needs `by` pointing at an institution")
        n["group"] = owner["group"]
        add(owner["id"], "offers", n["id"])
        for v in n.pop("uses", []):
            add(n["id"], "built_on", v)
        for c in n.pop("caps", []):
            if by_id.get(c, {}).get("type") != "capability":
                fail(f"{n['id']}: {c} is not a capability")
            add(n["id"], "enables", c)

    for e in src["edges"]:
        add(e[0], e[1], e[2], e[3] if len(e) > 3 else None)

    seen = Counter((e["source"], e["rel"], e["target"]) for e in edges)
    dupes = [k for k, v in seen.items() if v > 1]
    if dupes:
        fail(f"duplicate edges: {dupes}")

    degree = Counter()
    for e in edges:
        degree[e["source"]] += 1
        degree[e["target"]] += 1
    orphans = [n["id"] for n in nodes if degree[n["id"]] == 0]
    if orphans:
        fail(f"nodes with no edges: {orphans}")

    kg = {"meta": src["meta"], "groups": src["groups"], "nodes": nodes, "edges": edges}
    (HERE / "kg.json").write_text(json.dumps(kg, indent=1, ensure_ascii=False) + "\n")

    node_cols = ["id", "type", "label", "group", "date", "status", "ai", "audience", "region",
                 "wealth", "conf", "desc", "metrics", "src"]
    with open(HERE / "nodes.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(node_cols)
        for n in nodes:
            row = {**n, "metrics": " | ".join(n.get("metrics", [])), "src": " ".join(n.get("src", []))}
            w.writerow(["" if row.get(c) is None else row.get(c) for c in node_cols])

    edge_cols = ["source", "rel", "target", "date", "rank", "role", "conf", "note"]
    with open(HERE / "edges.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(edge_cols)
        for e in edges:
            w.writerow([e.get(c, "") for c in edge_cols])

    template = (HERE / "template.html").read_text()
    if PLACEHOLDER not in template:
        fail("template.html is missing the data placeholder")
    payload = json.dumps(kg, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    REPORT.write_text(template.replace(PLACEHOLDER, payload))

    types = Counter(n["type"] for n in nodes)
    print(f"{len(nodes)} nodes ({', '.join(f'{k} {v}' for k, v in sorted(types.items()))}), "
          f"{len(edges)} edges -> {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
