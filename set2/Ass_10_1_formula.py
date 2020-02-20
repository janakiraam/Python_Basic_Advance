# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 21:43:20 2018

@author: I340968
"""

import math
C=50
H=30
D=input().split(',')

for i in range (len(D)):
    #K=int(2*C*D[i])/H
    Q=round(math.sqrt((2*C*int(D[i]))/H))
    #j=int(Q)
    if i < (len(D))-1:
        print(Q,end=',')
    else:
        print(Q)
