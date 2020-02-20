# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 06:56:47 2018

@author: I340968
"""

def unique(list1): 
    unique_list = [] 
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x) 
    for x in unique_list: 
        print (x,end=',') 
        
new_list =[] # A list which holds the numbers
m=int(input())
n=int(input())
if 1000<=m<=9000 and 1000<=n<=9000:
    for a in range(m,n):
        for b in str(a):
            if int(b) % 2 == 1:
                new_list.append(a)
unique (new_list)