# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 17:31:12 2018

@author: I340968
"""

k =int(input())
m = list()
for i in range (k):
    j=input()
    m.append(j)
#print(m)
n = [element.upper() for element in m]
for i in n:
    print (i)