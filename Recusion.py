# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 22:24:00 2021

"""

# normal method

def find_sum(n):
     sum=0
     for i in range (1,n+1):
         sum=sum+i
     return sum
if __name__=='__main__':
    print(find_sum(5))


# recursion:

def find_sum1(n):
    if n==1:
        return 1
    return n + find_sum1(n-1)
if __name__=='__main__':
    print(find_sum(5))