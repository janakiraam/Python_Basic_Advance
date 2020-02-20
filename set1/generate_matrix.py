# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 10:17:38 2018

@author: i340968
"""

'''r = int(input())
c = int(input())
count = 1
matrix_range=[]
for i in range(r):
  for j in range(c):
    matrix_range[i][j]=count
    print(matrix_range[i][j],end=" ")
print()'''

'''magic_asquare=[]
for i in range(1):
    for j in range(1): 
        print(magic_asquare[i][j],end=" ")
    print()'''
    
'''import numpy
r=int(input())
c=int(input())    
matrix=[]
count = 1
for i in range(r):
   l=[]
   for j in range(c):
        l.append(count)
        count = count+1
   matrix.append(l)
print(numpy.shape(matrix))    
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()'''

'''r=int(input())
c=int(input())    
matrix=[]
count = 1
for i in range(r):
   l=[]
   for j in range(c):
        l.append(count)
        matrix.append(l)
        count = count+1
        print()
        print(matrix)
        print()
 print(matrix)

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()'''
    
r,c = input().split()
r,c = int(r),int(c)  
matrix=[]
count = 1
for i in range(r):
   l=[]
   for j in range(c):
        l.append(count)
        count = count+1
   matrix.append(l)
 
for i in range(r):
    for j in range(c):
      	if j+1 < c:
      		print(matrix[i][j],end=" ")
      	else:
          	print(matrix[i][j],end="")
    if i+1 < r:
    	print()