__author__ = 'Bhavin.Parekh'
__author__ = 'Bhavin.Parekh'
import networkx as nx
import matplotlib.pyplot as plt

import timeit
test_file = open(r'1018_edges.csv','r')
#test_file = open(r'edges2.csv','r')
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

prblty_value=0.5

g = nx.read_edgelist(test_file,delimiter=',', nodetype=int, create_using=nx.erdos_renyi_graph(n,p))

attr = {n: {"infected":False,"immune":False} for n in g.nodes()}
nx.set_node_attributes(g, attr)

#g.add_nodes_from(node_list) #NOT NEEDED
nx.draw(g,with_labels=True)
print(g.edges(data=True))

#print '##########'
#print 'Atrribute for one node'
#print(g.node['A']['infected'])
#print(g.node['P']['infected'])
print '#Atrribute for one node'#'
plt.draw()
plt.show()

list_nodes=[]
def find_neigbours(node_name):
    list_nbr=[]
    nbr=g.neighbors(node_name)
    for n in nbr:
       list_nbr.append(n)
       if(not (list_nodes.__contains__(n))):
           list_nodes.append(n)
    return list_nbr

#print 'Find neighbour'
#print(find_neigbours('P'))
#print 'end Find neighbour'

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

total_infected_node=[]
start = timeit.default_timer()
x_val=[]
y_val=[]
infected_node_count=0
def start_infection(graph,prob,start_node=0):
  try:
    global total_iteration
    global infected_node_count
    if not graph.node[start_node]['infected']:
      total_iteration  = total_iteration  + 1


      #print('Round : '+str(total_iteration))
      #print('Infected Node:'+ str(start_node))

      #print('##---------##')
      graph.node[start_node]['infected']=True
      if((graph.node[start_node]['infected']==True) and (not(total_infected_node.__contains__(start_node)))):
       total_infected_node.append(start_node)

      if(not(current_infected_nodes.__contains__(start_node))):
         current_infected_nodes.append(start_node)
      new_neigbours=[]
      new_neigbours= find_neigbours(start_node)

      #print('neighbours :',new_neigbours)

      add_this_unexplored(new_neigbours,graph)
      remove_explored(graph)
      listTotal=-1
      listTotal=len(new_neigbours)
      if(len(unexplored_node)>0):
          iterationValues=int(round(len(unexplored_node)*prob))

      if(iterationValues>0):

          print('total node to be affectd with probability '+str(iterationValues))
         # y_val.append(iterationValues)
          infected_node_count=infected_node_count+iterationValues+1
          if(len(y_val)==0):
              y_val.append(0.4)

          y_val.append(infected_node_count)
          stop = timeit.default_timer()
          if(len(x_val)==0):
              x_val.append(0)
          x_val.append(stop)
          print('Time # ' +str(stop))
          #print(unexplored_node[0])
          print(unexplored_node)
          for x in range(0,iterationValues):
             #print(new_neigbours[x])
             if(len(unexplored_node)>2):
              strnode=unexplored_node[x]             #print(str)
              start_infection(graph,prob,strnode)
          if(len(unexplored_node) >0 and iterationValues==0 or iterationValues==1):
            start_infection(graph,prob,unexplored_node[0])
  except:
      print 'error'

#print('end of method')
#print(total_iteration)

def remove_explored(graph):
    for x in unexplored_node:
        if((graph.node[x]['infected']==True)):
            unexplored_node.remove(x)

def add_this_unexplored(new_neigbours,graph):
    for x in new_neigbours:
        if(not(unexplored_node.__contains__(x)) and (not (graph.node[x]['infected']==True)) ):
            unexplored_node.append(x)

start = timeit.default_timer()
start_infection(g,1,0)
#check any other left out
print('#################')
print('#################done without exiting recursion#############')
print('length of collectiions')
print(len(x_val))
print(len(y_val))
print('####left out node#########')
if(len(unexplored_node)>0):
 for u in unexplored_node:
    if g.node[u]['infected']==False:
       #start_infection(g,0.8,u)
       print (u)
stop = timeit.default_timer()
print(nx.get_node_attributes(g, 'infected'))
print('Total # of Nodes')
print(g.number_of_nodes())
print('Total # of Edges')
print(g.number_of_edges())
print('total run time ; {0}'.format(stop-start))
plt.yscale('symlog', linthreshy=0.0001)
plt.ylabel('Infected nodes')
plt.xlabel('Time->')
#plt.xscale('symlog', linthreshy=0.01)
plt.plot(x_val,y_val)
plt.show()

