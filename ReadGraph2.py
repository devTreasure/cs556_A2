__author__ = 'Bhavin.Parekh'
import networkx as nx
import matplotlib.pyplot as plt

test_file = open(r'edges.csv','r')

node_list=[]
edge_list=[]


#collecting unique nodes
with open(r'edges.csv','r') as csv:
    for r in csv:
        edge_list.append([r[0],r[2]])
        if not node_list.__contains__(r[0]):
            node_list.append(r[0])
        if not node_list.__contains__(r[2]):
            node_list.append(r[2])

print 'type of'
print(type(test_file))
print 'edge list'
print edge_list
print'#######'
print(node_list)
n=len(node_list) # finding total nodes
p=1


g = nx.read_edgelist(test_file,delimiter=',', nodetype=str, create_using=nx.erdos_renyi_graph(n,p))

attr = {n: {"infected":False} for n in g.nodes()}
nx.set_node_attributes(g, attr)

#g.add_nodes_from(node_list) #NOT NEEDED
nx.draw(g,with_labels=True)
print(g.edges(data=True))

print '##########'
print 'Atrribute for one node'
print(g.node['A']['infected'])
print(g.node['P']['infected'])
print '#Atrribute for one node'#'
#plt.draw()
#plt.show()


def find_neigbours(node_name):
    list_nbr=[]
    nbr=g.neighbors(node_name)
    for n in nbr:
       list_nbr.append(n)
    return list_nbr

print 'Find neighbour'
print(find_neigbours('P'))
print 'end Find neighbour'

def fetch_next_node(g,lst):
    for n in lst:
     if not (g.node[n]['infected']):
      return n

     # break;
    #else:
        #for n1 in lst:
        # lst1 = find_neigbours(n1)
        # fetch_next_node(g,lst1)


def start_infection(graph,prob=0.5,start_node='A'):
    if not graph.node[start_node]['infected']:
        graph.node[start_node]['infected']=True
        new_nbrs=[]
        new_nbrs= find_neigbours(start_node)
        if(prob>0.5):
            for n1 in new_nbrs:
                start_infection(graph,prob,n1)
        else:
             last_visited_list=new_nbrs
             new_node=fetch_next_node(graph,new_nbrs)
             if(new_node is None):
                 new_nbrs=[]
                 new_nbrs= find_neigbours(last_visited_list[0])
                 newX_node=fetch_next_node(graph,new_nbrs)
                 if(new_node is None and newX_node is None):
                     find_node=graph.nodes
                     val=''
                     for n in find_node:
                         if not (graph.node[n]['infected']==True):
                           start_infection(graph,prob,n)
                 else:
                   start_infection(graph,prob,newX_node)
             else:
                  start_infection(graph,prob,new_node)
    else:
       new_nbrs=[]
       new_nbrs= find_neigbours(start_node)
       if(prob>0.5):
         for n2 in new_nbrs:
          start_infection(graph,prob,n2)
       else:
          new_node=fetch_next_node(graph,new_nbrs)
          start_infection(graph,prob,new_node)



start_infection(g,0.5,'A')

print('###################################################################################')

#method 2
G_erdos = nx.erdos_renyi_graph(n,p)
#edge_list is the list built dynamically FROM CSV
attr = {n: {"infected":False} for n in G_erdos.nodes()}
nx.set_node_attributes(G_erdos, attr)

G_erdos.add_edges_from(edge_list)

#G_erdos.graph['infected']=False


#setting default attribu
#infected=[]
#nx.set_node_attributes(G_erdos,'infected', 'infected')
#infected.append(False)
print '#Attributes#'
#Iterating loop to set the attrib value
for n in G_erdos.nodes:
    print n
    if n not in [0,1,2,3,4,5]:
        G_erdos.node[n]['infected']=False

print '##########'
print 'Atrribute for one node'
print(G_erdos.node['A']['infected'])
print(G_erdos.node['P']['infected'])
print '#Atrribute for one node'#'

print '##all noded##'

print '#--End all nodes-#'

nx.draw(G_erdos,with_labels=True)

print(G_erdos.edges(data=False))
print 'nearest neighbours'
neighbours_list=G_erdos.neighbors('P')
for n in neighbours_list:
    print n
    # print(G_erdos[n]['infected'])
print '#--End--#'
#plt.draw()
#plt.show()


def find_neighbours():
    pass

#G=nx.erdos_renyi_graph(n,p,seed=None,directed=False)

#with open(r'edges.csv','r') as csv:
 #for r1 in csv:
   # G.add_edge(r1[0],r1[2])

#G.add_nodes_from(node_list)
#nx.draw(G,with_labels=True)
#plt.draw()
#plt.show()