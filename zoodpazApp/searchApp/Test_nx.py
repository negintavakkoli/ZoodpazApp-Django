import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pylab as plt


B=nx.Graph()
B.add_nodes_from([1, 2, 3, 4], bipartite=0)
B.add_nodes_from(["a", "b", "c"], bipartite=1)
nx.set_node_attributes(B,{4:"ing2"}, "ID")
nx.set_node_attributes(B,{1:"ing1"}, "ID")

B.add_edges_from([(1, "a"), (1, "b"), (2, "b"), (2, "c"), (3, "c"), (4, "a")])
print(B.nodes())

for neighbor in B.neighbors("a"):
    print(neighbor)
    print(B.nodes[neighbor])
# G=nx.Graph()
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
# G.add_node(4)
# Nodes = G.nodes()
#
# G.add_edge(1,2)
# G.add_edge(1,3)
# G.add_edge(1,4)
# EDGES = G.edges()
# print(Nodes, EDGES)
# nx.draw(G)