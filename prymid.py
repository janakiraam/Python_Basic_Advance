# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 23:24:18 2021

"""

row =5
k=2*row-2
for i in range(0,row):
    for j in range(0,k):
        print(end='-')
    k=k-1
    for j in range (0,i+1):
        print("*",end="")
    print("")