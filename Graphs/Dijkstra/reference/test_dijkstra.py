import json
import math
import unittest
from pathlib import Path

from dijkstra import shortest_path


class DijkstraTests(unittest.TestCase):
    def test_teaching_graph_matches_the_animation(self) -> None:
        graph = {
            "nodes": [{"id": value} for value in range(6)],
            "edges": [
                {"edgeId": "A-B", "from": 0, "to": 1, "lengthMeters": 4},
                {"edgeId": "A-C", "from": 0, "to": 2, "lengthMeters": 2},
                {"edgeId": "C-B", "from": 2, "to": 1, "lengthMeters": 1},
                {"edgeId": "B-D", "from": 1, "to": 3, "lengthMeters": 5},
                {"edgeId": "B-E", "from": 1, "to": 4, "lengthMeters": 4},
                {"edgeId": "C-E", "from": 2, "to": 4, "lengthMeters": 7},
                {"edgeId": "D-F", "from": 3, "to": 5, "lengthMeters": 3},
                {"edgeId": "E-F", "from": 4, "to": 5, "lengthMeters": 1},
            ],
        }
        nodes, edges, cost = shortest_path(graph, 0, 5)
        self.assertEqual(nodes, [0, 2, 1, 4, 5])
        self.assertEqual(edges, ["A-C", "C-B", "B-E", "E-F"])
        self.assertEqual(cost, 8)

    def test_small_weighted_graph_prefers_lower_total_cost(self) -> None:
        graph = {
            "nodes": [{"id": value} for value in range(4)],
            "edges": [
                {"edgeId": "direct", "from": 0, "to": 3, "lengthMeters": 10},
                {"edgeId": "a", "from": 0, "to": 1, "lengthMeters": 2},
                {"edgeId": "b", "from": 1, "to": 2, "lengthMeters": 2},
                {"edgeId": "c", "from": 2, "to": 3, "lengthMeters": 2},
            ],
        }
        nodes, edges, cost = shortest_path(graph, 0, 3)
        self.assertEqual(nodes, [0, 1, 2, 3])
        self.assertEqual(edges, ["a", "b", "c"])
        self.assertEqual(cost, 6)

    def test_unreachable_destination(self) -> None:
        graph = {"nodes": [{"id": 0}, {"id": 1}], "edges": []}
        with self.assertRaisesRegex(ValueError, "unreachable"):
            shortest_path(graph, 0, 1)

    def test_cape_town_trace_matches(self) -> None:
        root = Path(__file__).resolve().parents[1]
        graph = json.loads((root / "data/road-graph.v1.json").read_text(encoding="utf-8"))
        trace = json.loads((root / "data/dijkstra-trace.v1.json").read_text(encoding="utf-8"))
        nodes, edges, cost = shortest_path(graph, trace["start"]["nodeId"], trace["destination"]["nodeId"])
        self.assertEqual(nodes, trace["pathNodeIds"])
        self.assertEqual(edges, trace["pathEdgeIds"])
        self.assertTrue(math.isclose(cost, trace["totalCostMeters"], abs_tol=0.001))


if __name__ == "__main__":
    unittest.main()
