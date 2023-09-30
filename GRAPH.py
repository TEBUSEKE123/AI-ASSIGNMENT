# G = (V, E)
# from collections import namedtuple

Graph = {}

nodes = ["S", "A", "B", "C", "D", "G"]
for node in nodes:
    Graph[node] = set()


edges = [
    ("S", "A"),
    ("S", "B"),
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("C", "D"),
    ("C", "G"),
    ("D", "G")

]
for edge in edges:
    Source, target = edge
    Graph[Source].add(target)

for node, neighbors in Graph.items():
    print(f"Node {node} is connected to nodes: {neighbors}")
