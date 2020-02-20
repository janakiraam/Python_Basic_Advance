# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 07:18:05 2018

@author: I340968
"""

str1=input("Enter the first string:  ")
str2=input("Enter the second string:  ")
sot_str1 = sorted(str1)
sot_str2 = sorted(str2)
print("sorted version: ",sot_str1," ",sot_str2)
if(sot_str1==sot_str2):
    print("These are angrame")
else:
    print("These are not anagrame")