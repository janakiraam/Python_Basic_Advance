# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 07:11:51 2018

@author: I340968
"""

'''list_1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str_1 = input()
for i in range (len(list_1)):
    str_2 = (str_1.replace(".",list_1[i]))
    j=(''.join(reversed(str_2)))
    if (str_2 == j):
        print(str_2)
    else:
        print("-1")'''
        

list_1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str_1 = input()
pal=[]
j=[]
for i in range (len(list_1)):
    str_2 = (str_1.replace(".",list_1[i]))
    #j=(''.join(reversed(str_2)))
    pal.append(str_2)
#print(pal)
for i in range (len(pal)):
    if (pal[i]== ''.join(reversed(pal[i]))):
        print(pal[i])
        j.append(pal[i])
        break
#print(j)
if not j:
    print("-1")
       