# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 22:34:27 2018

@author: i340968
"""
#Wee4-2 assignment
num = int(input())
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
print(factorial)

'''def fact(num):
    if num ==1:
        return 1
    else:
        return num*fact(num-1)
number = int(input())

if number >0 :
    print(fact(number)) 

def fact(num):
    if num ==1 or num==0:
        return 1
    else:
        return num*fact(num-1)
number = int(input())

if number >=0 :
    print(fact(number)) '''