__author__ = 'Bhavin.Parekh'
import networkx as nx
import matplotlib.pyplot as plt
import timeit
test_file = open(r'edges.csv','r')

node_list=[]
edge_list=[]

#collecting unique nodes
# with open(r'edges.csv','r') as csv:
#     for r in csv:
#         edge_list.append([r[0],r[2]])
#         if not node_list.__contains__(r[0]):
#             node_list.append(r[0])
#         if not node_list.__contains__(r[2]):
#             node_list.append(r[2])

# print 'type of'
# print(type(test_file))
# print 'edge list'
# print edge_list
# print'#######'
# print(node_list)
n=4#len(node_list) # finding total nodes
p=1


g = nx.read_edgelist(test_file,delimiter=',', nodetype=str, create_using=nx.erdos_renyi_graph(n,p))

attr = {n: {"infected":False} for n in g.nodes()}
nx.set_node_attributes(g, attr)

#g.add_nodes_from(node_list) #NOT NEEDED
nx.draw(g,with_labels=True)
print(g.edges(data=True))

print '##########'
print 'Atrribute for one node'
#print(g.node['A']['infected'])
#print(g.node['P']['infected'])
print '#Atrribute for one node'#'
#plt.draw()
#plt.show()

list_nodes=[]
def find_neigbours(node_name):
    list_nbr=[]
    nbr=g.neighbors(node_name)
    for n in nbr:
       list_nbr.append(n)
       if(not (list_nodes.__contains__(n))):
           list_nodes.append(n)
    return list_nbr

print 'Find neighbour'
#print(find_neigbours('P'))
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



explored_node=[]
current_infected_nodes=[]
unexplored_node=[]
total_iteration=0



def remove_vistited_item():
    pass


total_list_nodes=g.number_of_nodes()

def start_infection(graph,prob=0.4,start_node='A'):
    global total_iteration

    if not graph.node[start_node]['infected']:
      total_iteration  = total_iteration  + 1
      print('Round : '+str(total_iteration))
      print('Infected Node:'+ str(start_node))
      graph.node[start_node]['infected']=True

      if(not(explored_node.__contains__(start_node))):
          explored_node.append(start_node)

     # if(not(current_infected_nodes.__contains__(start_node))):
          # current_infected_nodes.append(start_node)
      new_neigbours=[]
      new_neigbours= find_neigbours(start_node)

    # for item in explored_node:
    #  while new_neigbours.count(item) > 0:
    #   new_neigbours.remove(item)
    new_neigbours=remove_explored_from_the_new_neighborts(new_neigbours)
    print('neighbours :',new_neigbours)

    #add_this_unexplored(new_neigbours,graph)
    listTotal=-1
    listTotal=len(new_neigbours)
    if(listTotal >0 ):
          iterationValues=int(round(listTotal*prob))
          for x in  range(0,iterationValues):
             #print(new_neigbours[x])
             strnode=new_neigbours[x]
             #print(str)
             start_infection(graph,prob,strnode)


def remove_explored_from_the_new_neighborts(lst):
   for item in explored_node:
     while lst.count(item) > 0:
      lst.remove(item)
   return lst

def add_this_unexplored(new_neigbours,graph):
    for x in new_neigbours:
        if(not(unexplored_node.__contains__(x)) ):
            unexplored_node.append(x)

start = timeit.default_timer()
start_infection(g,0.4,'A')
#check any other left out
for u in unexplored_node:
    if g.node[u]['infected']==False:
       start_infection(g,0.4,u)
stop = timeit.default_timer()
print(nx.get_node_attributes(g, 'infected'))
print(nx)
print('Total # of Nodes')
print(g.number_of_nodes())
print('Total # of Edges')
print(g.number_of_edges())
print('total run time ; {0}'.format(stop-start))