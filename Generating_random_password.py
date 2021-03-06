# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 23:10:18 2021

"""
import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
sysmbols ="@#$%"

upper,lower,nums, syms = True,True,True,True

all=""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all+=digits
if syms:
    all += sysmbols
    
print(all)
    



length =20
amont =10

for x in range(amont):
    password = "".join(random.sample(all,length))
    print(password)

