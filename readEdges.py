__author__ = 'Bhavin.Parekh'
__author__ = 'Bhavin.Parekh'
import networkx as nx
import matplotlib.pyplot as plt
test_file = open(r'a.txt','r')

print(test_file.readline())
g=nx.read_edgelist(test_file,create_using=nx.gnp_random_graph(100,0.1,None,False),nodetype=str)
print(nx.info(g))
nx.draw(g)
plt.show()