# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:29:07 2018

@author: I340968
"""

#Binary_search:

def binary_search(a,x):
    first_pos = 0
    last_pos = len(a)-1
    flag=0 # flag value 0 indicate the number is not found yet
    
    count = 0
    
    while(first_pos<=last_pos and flag==0):
        count+=1
        mid = (first_pos+last_pos)//2
        if(x==a[mid]):
            flag=1
            print("the element is present in the position" + str(mid+1))
            print("The number of iterations are "+str(count))
            return
        else:
            if(x<a[mid]):
                last_pos=mid-1
            else:
                first_pos=mid+1
    
    print("The number is not present")
    
a=[]
for i in range(1,1001):
    a.append(i)
binary_search(a,998)