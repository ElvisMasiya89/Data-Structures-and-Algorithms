"""Minimal executable Dijkstra used by the episode's code panel."""

from __future__ import annotations

import heapq
import json
import math
from pathlib import Path


def shortest_path(graph: dict, start: int, destination: int) -> tuple[list[int], list[str], float]:
    adjacency: dict[int, list[dict]] = {node["id"]: [] for node in graph["nodes"]}
    for edge in graph["edges"]:
        adjacency[edge["from"]].append(edge)

    distance = {start: 0.0}
    previous: dict[int, tuple[int, str]] = {}
    frontier = [(0.0, start)]
    settled: set[int] = set()

    while frontier:
        cost, node = heapq.heappop(frontier)
        if node in settled:
            continue
        settled.add(node)
        if node == destination:
            break

        for edge in adjacency[node]:
            candidate = cost + edge["lengthMeters"]
            if candidate < distance.get(edge["to"], math.inf):
                distance[edge["to"]] = candidate
                previous[edge["to"]] = (node, edge["edgeId"])
                heapq.heappush(frontier, (candidate, edge["to"]))

    if destination not in settled:
        raise ValueError("destination is unreachable")

    nodes = [destination]
    edges: list[str] = []
    while nodes[-1] != start:
        parent, edge_id = previous[nodes[-1]]
        nodes.append(parent)
        edges.append(edge_id)
    return list(reversed(nodes)), list(reversed(edges)), distance[destination]


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    graph = json.loads((root / "data/road-graph.v1.json").read_text(encoding="utf-8"))
    expected = json.loads((root / "data/dijkstra-trace.v1.json").read_text(encoding="utf-8"))
    path_nodes, path_edges, cost = shortest_path(
        graph, expected["start"]["nodeId"], expected["destination"]["nodeId"]
    )
    assert path_nodes == expected["pathNodeIds"]
    assert path_edges == expected["pathEdgeIds"]
    assert math.isclose(cost, expected["totalCostMeters"], abs_tol=0.001)
    print(f"{len(path_edges)} roads | {cost:,.3f} metres | verified")
