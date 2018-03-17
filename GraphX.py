__author__ = 'Bhavin.Parekh'
import networkx as nx
import matplotlib.pyplot as plt


N = 10
G22=nx.grid_2d_graph(N,N)
pos = dict( (n, n) for n in G22.nodes() )
labels = dict( ((i, j), i + (N-1-j) * N ) for i, j in G22.nodes() )
nx.relabel_nodes(G22,labels,False)

G3=nx.erdos_renyi_graph(100,0.1)

# Setting node attribute
attr = {n: {"infected": 0.0} for n in G3.nodes()}
nx.set_node_attributes(G3, attr)

pos = {y:x for x,y in labels.iteritems()}
nx.draw_networkx(G3, pos=pos, with_labels=True, node_size = 300)
print G3.nodes()
plt.axis('off')
plt.draw()
plt.show()

print 'all nodees'
nodes = nx.shortest_path(G3,99).keys()
print 'shortst path'
print nodes
print '------'
print(G3.nodes())
print 'single  node'
print(G3.node[1])

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

def start_infection(node_name): #2
    list_x=[]
    outer_list_neigh.append(node_name)
    print('##--INSIDE the start_infection--##')
    #print(len(g.nodes()))

    list_x=find_neighbours(node_name) # 1,5,and 2
    for x in list_x:
      find_neighbours(x)
    #while (len(list_neigh)< len(g.nodes())):
        #list_neigh=find_neighbours(node_name); # 1,5,and 2

        #for n in list_neigh:  #1
         # new_neigh=[]
         # new_neigh=find_neighbours(n) #2

start_infection(1)




print('#Node Tuple#')
print(g.node[1])
print('#Node Tuple#')

print('#SETTER attributue#')
#Setting up node value
print(g.node[1]['explored'])
g.node[1]['x1']=440;
g.node[4]['x1']=420;

print('###--Print total node-- ###')
print(g.nodes())
print('###--Print total node-- ###')

print('#Function pass the node')

print('length of neighbour_list')

returned_list=[]
returned_list=find_neighbours(2)

for i in returned_list:
  new_list= find_neighbours(i)

print('#List size#')
print(len(returned_list))
print('#--End Function pass the node')

for f in returned_list:
 print(f)

print('#--List Captured at function return--#')
print('##--NODE Attrib-##')
print(g.node[1]['x1'])
print('##--NODE Attrib--##')

for n1 in g.node():
  print(g.node[n1]['x1'])

nx.draw(g,with_labels=True)

plt.draw()
plt.show()

#for G in g.nodes(data=True):
# color=nx.get_node_attributes(G,'x1')
 #print(color[1])
''' for i ,a in enumerate(x):
  ''    print(a)
'''
'''
for x,y in g.adjacency():
    #print('key->',x['infect'])
 for y1 in y:
       print (y1)
'''
