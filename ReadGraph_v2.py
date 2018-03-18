__author__ = 'Bhavin.Parekh'
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
print(g.node['A']['infected'])
print(g.node['P']['infected'])
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




current_infected_nodes=[]
unexplored_node=[]
total_iteration=0

def start_infection(graph,prob=0.5,start_node='A'):
    global total_iteration

    if not graph.node[start_node]['infected']:
      total_iteration  = total_iteration  + 1
      print('Round : '+str(total_iteration))
      print('Infected Node:'+ start_node)
      graph.node[start_node]['infected']=True
      if(not(current_infected_nodes.__contains__(start_node))):
            current_infected_nodes.append(start_node)
      new_neigbours=[]
      new_neigbours= find_neigbours(start_node)
      print('neighbours :',new_neigbours)

      add_this_unexplored(new_neigbours,graph)
      listTotal=-1
      listTotal=len(unexplored_node)
      if(listTotal >0 ):
          iterationValues=int(round(listTotal*prob))
          for x in  range(0,iterationValues):
             #print(new_neigbours[x])
             strnode=unexplored_node[x]
             #print(str)
             start_infection(graph,prob,strnode)
#print('end of method')
#print(total_iteration)


def add_this_unexplored(new_neigbours,graph):
    for x in new_neigbours:
        if(not(unexplored_node.__contains__(x)) ):
            unexplored_node.append(x)

current_infected_nodesv2=[]
def start_infection_v2(graph,prob=0.5,start_node='A'):
    if not graph.node[start_node]['infected']:
        graph.node[start_node]['infected']=True
        if(not(current_infected_nodesv2.__contains__(start_node))):
            current_infected_nodesv2.append(start_node)
        new_nbrs=[]
        new_nbrs= find_neigbours(start_node)
        if(prob>0.5):
            for n1 in new_nbrs:
                start_infection_v2(graph,prob,n1)
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
                           start_infection_v2(graph,prob,n)
                 else:
                   start_infection_v2(graph,prob,newX_node)
             else:
                  start_infection_v2(graph,prob,new_node)
    else:
       new_nbrs=[]
       new_nbrs= find_neigbours(start_node)
       if(prob>0.5):
         for n2 in new_nbrs:
          start_infection_v2(graph,prob,n2)
       else:
          new_node=fetch_next_node(graph,new_nbrs)
          start_infection_v2(graph,prob,new_node)


start = timeit.default_timer()
start_infection(g,0.5,'A')
#check any other left out
for u in unexplored_node:
    if g.node[u]['infected']==False:
        start_infection(g,0.5,u)
stop = timeit.default_timer()
print('total run time ; {0}'.format(stop-start))