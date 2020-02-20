# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:04:18 2018

@author: I340968
"""

'''dic_ho = {"A":1,"B":2,"D":1,"O":1,"P":1,"Q":1,"R":1}
j = input()
#print(len(dic_ho))
print(dic_ho)
if j[1]=="".join(dic_ho):
    print("equle")'''

#Accessing key values alone
'''"".join(dic_ho)
print(dic_ho.keys())'''
    




#Count number of occurance 
'''word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print (d)'''

j = input()
count = 0 
if ('A' in j):
    ca = j.count('A')
    count = count+ca
if ('B' in j):
    cb = j.count('B')
    count = count+(2*cb)
if('D' in j):
    cd = j.count('D')
    count = count+cd
if('O' in j):
    co = j.count('O')
    count = count+co
if('P' in j):
    cp = j.count('P')
    count = count+cp
if('Q' in j):
    cq = j.count('Q')
    count = count+cq
if('R' in j):
    cr = j.count('R')
    count = count+cr
print(count)

    