# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 12:35:18 2018

@author: I340968
"""

#bubble_sort

def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                tem=a[j]
                a[j]=a[j+1]
                a[j+1]=tem
                
a=[5,4,1,3,2]
bubble(a)

for i in a:
    print(i)