# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 08:01:26 2018

@author: i340968
"""
#Week4- assignment3 

import random
list_1 =[]
n = int(input())
for x in range(0,n):
    j = int(input())
    list_1.append(j)

#print(list_1)
list_1.sort()
print(*list_1,sep=' ')

