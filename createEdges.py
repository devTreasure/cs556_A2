__author__ = 'Bhavin.Parekh'
import networkx as nx
import matplotlib.pyplot as p
G= nx.erdos_renyi_graph(500,0.008052)
gb= nx.barabasi_albert_graph(500,10)
#G= nx.erdos_renyi_graph(5,0.6)
for x in nx.generate_edgelist(gb, data=False):
    print(x)
# g=nx.Graph.add_nodes_from(A'','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
#                            'A1','B1','C1','D1','E1','F1','G1','H1','I1','J1','K1','L1','M1','N1','O1','P1','Q1','R1','S1','T1','U1','V1','W1','X1','Y1','Z1')
#
#
