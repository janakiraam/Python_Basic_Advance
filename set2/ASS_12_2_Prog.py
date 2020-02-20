# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 10:19:04 2018

@author: I340968
"""

#string=input("Enter string:")
string=input()
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
#print("The number of lowercase characters is:")
print(count1,count2)
#print("The number of uppercase characters is:")
print(count2)