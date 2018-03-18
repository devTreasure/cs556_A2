__author__ = 'Bhavin.Parekh'
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C')])
nx.draw(G, node_size=800, node_color='white', with_labels=True)
plt.show()