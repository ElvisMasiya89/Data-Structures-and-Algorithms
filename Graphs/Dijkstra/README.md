# Dijkstra's shortest-path algorithm

This folder contains the exact Python implementation and tests used in the
Guides.sh visual lesson, **Python Dijkstra's Algorithm Finds the Shortest
Path**.

## Run it

From this directory:

```bash
python reference/dijkstra.py
python -m unittest discover -s reference -p "test_*.py"
```

The implementation uses a min-heap priority queue and supports directed graphs
with non-negative edge weights. It returns the path nodes, path edge IDs and
total cost. An unreachable destination raises `ValueError`.

## Files

- `reference/dijkstra.py` — the implementation shown in the video.
- `reference/test_dijkstra.py` — the lesson and boundary tests.
- `data/road-graph.v1.json` — the recorded Cape Town road graph used by the
  demonstration.
- `data/dijkstra-trace.v1.json` — the verified shortest-path trace.

## Data attribution

The Cape Town road graph is derived from OpenStreetMap data and is provided
under the Open Database License (ODbL). © OpenStreetMap contributors:
https://www.openstreetmap.org/copyright

Watch the lesson: https://youtu.be/k6QBKBt9RvI
