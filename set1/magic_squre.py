# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 07:51:42 2018

@author: i340968

=============================================================================================

Alogorithm for the same
======================

Fact:

Magic number M=n(n^2+1)/2

Steps:
========
1) 1 position -> (n/2,n-1)

2) if 1 located in (p,q) then position of 2 is (p-1,q+1)
if row positon becomes -1 then make it n-1 if coloumn postion becomes n then make it 0

3)if calculated position already contains a number then decrement the column by2 and increment the row by 1

4)If anytime row position becomes -1 and column becomes n, switch t to (0,n-2)
==========================================================================================

"""

def magic_square(n):
    
    magic_asquare=[]
    for i in range(n):
        l=[]
        for j in range(n): 
            l.append(0)
        magic_asquare.append(l)
#magic = [[0 for i in range(3)] for j in range(3)]
    i = n//2
    j = n-1
    num = n*n
    count = 1
    while (count <= num):
        if(i==-1 and j==n):   #condition 4
            j=n-2
            i=0
        else:
            if(j==n):  #column value is exceeding
                 j = 0
            if(i<0):             #if rowbecomes -1 
                i = n-1
        if(magic_asquare[i][j] != 0):
            j = j-2
            i = i+1
            continue
        
        else:
            magic_asquare[i][j]=count
            count+=1
        i = i-1
        j = j+1   #condition 1
        
    for i in range(n):
        for j in range(n): 
            print(magic_asquare[i][j],end=" ")
        print()
    print("the sum of each row/column/dia: "+str(n*(n**2+1)/2))
        
magic_square(3)
            