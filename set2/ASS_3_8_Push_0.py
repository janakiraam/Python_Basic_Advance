# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 12:18:58 2018

@author: I340968
"""

def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [ i for i in num_list if i != 0]
    x.extend(a)
    return(x)

print(move_zero([0,2,3,4,6,7,10]))
print(move_zero([10,0,11,12,0,14,17]))