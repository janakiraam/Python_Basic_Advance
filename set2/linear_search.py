# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 17:32:54 2018

@author: I340968
"""
def linear_search(n,x):
    elemnet = []
    for i in range(1,n):
        elemnet.append(i)
    count=0
    flag=0    
    for i in elemnet:
        count+=1
        if(i==x):
            print("The number is found at place"+str(i))
            flag=1
        count+=1
    if(flag==0):
        print("Number is not found  ")
    print("Number of iteration   " + str(count))

n = int(input("Enter the value of n  "))
x = int(input("Enter the value you need to search  "))

linear_search(n,x)
