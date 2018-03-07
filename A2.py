__author__ = 'Bhavin.Parekh'
import  networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph(infect=0)
g.add_nodes_from([1,2,3,4,5],x1=0,explored=False)
g.add_edge(1,2,)
g.add_edge(4,2)
g.add_edge(3,5)
g.add_edge(5,2)
g.add_edge(2,5)
g.add_edge(5,4)

total_node_list=[]

def find_neighbours(node_name):
    nbr_list=[]
    lists_neighbours= g.neighbors(node_name)
    for x in lists_neighbours:
     nbr_list.append(x)
     print(x)
    return nbr_list

outer_list_neigh=[]
list_x=[]
list_infected_nodes=[]
def start_infection(node_name): #2
#    if(node_name not in list_x):
#        list_x.append(node_name)
    if(not (g.node[node_name]['explored'])):
        g.node[node_name]['explored']= True
        g.node[node_name]['infect']=1
        if( node_name not in list_infected_nodes):
          list_infected_nodes.append(node_name)

    new_nbrs=[]
    new_nbrs=find_neighbours(node_name) # 1,5,and 2
    print(new_nbrs)


    for x in new_nbrs:
      if (x not in list_infected_nodes):
        list_x.append(x)
        start_infection(x)
    print('printing list_x')
    print(list_infected_nodes)


##call to infection
#mnetion START random node with its ID
#let say we have ID: 1

list_nodes=[]
list_nodes=start_infection(1)




