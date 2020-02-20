# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 00:43:13 2018

@author: I340968
"""

'''string_x = str(input())
total = 0
for char in string_x:
    total = total+int(char)
print(total)
o_total = str(total)
while (int(o_total) > 10):
    for  char in o_total:
        o_total = int(o_total)+int(char)
    print(o_total)'''
    
'''def digits(number, base=10):
    assert number >= 0
    if number == 0:
        return [0]
    l = []
    while number > 0:
        l.append(number % base)
        number = number // base
    return l

digits(48)'''

number = input()
while(int(number) > 10):
    c = int(number)%10
    d = int(number)//10
    #print(c)
    #print(d)
    number = c+d
    #print(number)
print(number)

