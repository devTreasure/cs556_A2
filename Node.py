class Node:
    node_name=''
    infectd=0
    prob_val=0
    visited=False

    def __init__(self,Name):
        self.node_name=Name

    def  DFS(self,newitem,list=[]):
        list.append(newitem)
        print('##--NEW LIST--##')
        print('')
        for i in list:
          print(i)

