# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:53:52 2018

@author: I340968
"""

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

'''G.add_node(1)
G.add_node(2)
G.add_node(3)'''
# another way of adding nodes

'''l = [1,2,3]
G.add_nodes_from(l)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(1,3)
print(G.nodes())
print(G.edges())'''

#Creating complete graph

#G=nx.complete_graph(10)

#Creating random graph

G = nx.gnp_random_graph(20,0.5)

nx.draw(G)
plt.show()
