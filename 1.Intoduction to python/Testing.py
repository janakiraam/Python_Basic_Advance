# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 23:34:28 2020

@author: I340968
"""


values=[]
for x in range(1000,3000):
    s=str(x)
    if (int(s[0]) %2 == 0) and (int(s[1]) %2 == 0) and (int(s[2]) %2 == 0) and (int(s[3]) %2 == 0):
        values.append(s)
print ((values))