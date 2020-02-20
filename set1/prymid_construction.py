# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 07:09:56 2018

@author: I340968
"""

def pypart(n): 
     for i in range(1, n+1):
        for j in range(1, i+1):
            print(j,end=" ") 
        print() 


n = int(input())
pypart(n)
