# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 07:11:24 2018

@author: I340968
"""

import networkx as nx
import matplotlib.pyplot as plt

#G=nx.gnp_random_graph(50,0.3)

#Different type  of graph

G = nx.barabasi_albert_graph(50,2)

nx.draw(G)
plt.show(G)
'''print(G.nodes())
print()
print()
print()
print(G.edges())
print()
print(G.degree(0))'''

nx.write_gexf(G,"analysis1.gexf")
print(G.edges())