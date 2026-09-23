# Competitor AI knowledge graph

Built from `research_notes/Competitor AI products and achievements/` (as of 23 Sep 2026).

| File | What it is |
|---|---|
| `source.json` | Hand-curated source of truth. Edit this. |
| `build.py` | Validates the source and writes the files below. Run `python3 knowledge-graph/build.py`. |
| `kg.json` | Expanded graph: `nodes` + `edges` (`source`, `rel`, `target`, optional `date`, `rank`, `role`, `conf`, `note`). |
| `nodes.csv`, `edges.csv` | Same graph as flat tables for Neo4j, Gephi or a spreadsheet. |
| `template.html` | Viewer template; the build injects `kg.json` into it. |
| `../reports/competitor-ai-knowledge-graph.html` | Interactive graph and coverage matrix. |

## Model

Node types: `institution` (group and subsidiaries), `product`, `capability`, `partner` (vendors, tech partners, investees), `initiative` (CoEs, academies, governance, research units), `external` (regulators, sandboxes, rankings, awards), `person`.

Each product carries `status` (live / rollout / pilot / announced / historical), `ai` (agentic / genai / ml / rules / none), `audience`, `wealth`, `conf` (verified / secondary / unverified) and `src` URLs. In `source.json` a product declares `by` (its owner), `uses` (partners) and `caps` (capabilities). The build turns these into `offers`, `built_on` and `enables` edges.

Rules-based and non-AI products (for example Nutmeg portfolios, Trading 212 Pies and Barclays Premier Wealth) are kept on purpose, so gaps show up next to genuine AI.

To add a finding, append a node (and any edges) to `source.json` and rebuild. The build fails on unknown IDs, duplicate edges, bad enum values and orphan nodes.
