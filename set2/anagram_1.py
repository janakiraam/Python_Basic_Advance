# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 06:55:58 2018

@author: I340968
"""

#anagrams

str1=input("Enter the first string:  ")
str2=input("Enter the second string:  ")

# for angram the sum of ascii value of two string should be same
count1=0
count2=0
i=0
while(i<len(str1)):
    count1 = count1+ord(str1[i])
    i=i+1
i=0
while(i<len(str2)):
    count2 = count2+ord(str2[i])
    i=i+1
if(count1==count2):
    print("this are anagrams")
else:
    print("This are not anagrams")