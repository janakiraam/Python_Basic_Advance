# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 18:23:00 2018

@author: I340968
"""

myString=input()
mySubString=myString[myString.find("@")+1:myString.find(".")]
print (mySubString)