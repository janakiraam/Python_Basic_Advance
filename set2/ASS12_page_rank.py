# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:54:47 2018

@author: I340968
"""

import networkx as nx
import random
import matplotlib.pyplot as  plt

G=nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(G,with_labels=True)
plt.show()
#x is the random source node from number of nodes
x=random.choice([i for i in range(G.number_of_nodes())])
dict_counter={}
for i in range(G.number_of_nodes()):
    dict_counter[i]=0
    
dict_counter[x]=dict_counter[x]+1
for i in range(100):
    list_n=list[G.neighbors(x)]
#if the given node is sync then, select the node randomly from given set of node otherwise
#select a node from neighbour node.
    
    