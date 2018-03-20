__author__ = 'Bhavin.Parekh'
import networkx as nx
import matplotlib.pyplot as plt
import timeit

test_file = open(r'1018_edges.csv','r')


n=500#len(node_list) # finding total nodes
p=1

prblty_value=0.5

g = nx.read_edgelist(test_file,delimiter=',', nodetype=int, create_using=nx.erdos_renyi_graph(n,p))

attr = {n: {"infected":False,"immune":False} for n in g.nodes()}
nx.set_node_attributes(g, attr)
#
#
# g = nx.Graph();
#
# g.add_node(1, info={'infected': False, 'vaccine': True});
# g.add_node(2, info={'infected': False, 'vaccine': True});
# g.add_node(3, info={'infected': False, 'vaccine': True});
# g.add_node(4, info={'infected': False, 'vaccine': True});
# g.add_node(5, info={'infected': False, 'vaccine': True});
# g.add_node(6, info={'infected': False, 'vaccine': True});
# g.add_node(7, info={'infected': False, 'vaccine': True});
#
# g.add_edge(1, 2);
# g.add_edge(1, 3);
# g.add_edge(2, 4);
# g.add_edge(2, 5);
# g.add_edge(3, 6);
# g.add_edge(3, 7);


completedInfection = set([]);
partiallyInfectedNodes = set([]);



# Test
# print list(g[2])
# print g.node[2]['info']['infected']
# node_to_be_infected(range(1,11), 0.5);
# node_to_be_infected(range(1,4), 0.5);
# node_to_be_infected(range(1,5), 0.5);
# node_to_be_infected(range(1,2), 0.5);

x_val=[]
y_val=[]
infected_node=0

def start_infection(graph, prob, start_node):
    global infected_node
    g.node[start_node]['infected'] = True
    infected_node=infected_node+1
    hn = healthy_neighbours(start_node)
    if len(partiallyInfectedNodes) == 0:
        return;
    else:
        if len(hn) == 0:
            print("node %d completely infected (all neighbours)" % start_node);
            partiallyInfectedNodes.remove(start_node);
            completedInfection.add(start_node);
            if len(partiallyInfectedNodes) == 0:
                return
            else:
                nextNode = next(iter(partiallyInfectedNodes));
        else:
            print "Healthy Neighbours BEFORE- " + str(hn);
            hn = node_to_be_infected(hn, prob);
            print "Healthy Neighbours AFTER probability- " + str(hn);
            infected_node=infected_node+len(hn)
            y_val.append(len(completedInfection) + len(partiallyInfectedNodes))
            stop=  timeit.default_timer()
            x_val.append(stop-start)
            for node in hn:
                print("Infecting %d" % node);
                g.node[node]['infected'] = True;
            partiallyInfectedNodes.update(hn);
            nextNode = start_node;
        print nextNode
        print "continue with node %d" % nextNode
        start_infection(g, prob, nextNode)


# https://stackoverflow.com/questions/15644684/best-practices-for-querying-graphs-by-edge-and-node-attributes-in-networkx
def healthy_neighbours(start):
    query = (n for n in g[start] if g.node[n]['infected'] == False)
    return list(query)


def node_to_be_infected(hn, probability):
    nodes = list();
    length = len(hn);
    if length <= 1:
        return hn
    length = int(length * probability);
    if  length==0:
        return hn[0];
    else:
        return hn[0:length]

partiallyInfectedNodes.add(1)
start = timeit.default_timer()
start_infection(g, 0.3, 1);

print partiallyInfectedNodes
print completedInfection
plt.yscale('log')
plt.xscale('log')
plt.plot(x_val,y_val)

#plt.xscale('log')
plt.show()
# nx.draw(g, with_labels=True)
# plt.show();