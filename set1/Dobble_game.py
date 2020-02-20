# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:58:03 2018

@author: i340968

Alogrithm:
==========
1) list have set of symbols
2) Here list of symbols indicate alphabets
3) only one sysmbol should be there common between any set.

"""
import string
import random
symbols=[]
symbols = list(string.ascii_letters)
card1=[0]*5
card2=[0]*5
pos1=random.randrange(0,5)
pos2=random.randrange(0,5)
#pos1 and pos2 are same symbol position in card 1 and card2 respectively
samesymbol=random.choice(symbols) # Remove based on line 31 and 33 random should not select same symbol
symbols.remove(samesymbol)
if(pos1==pos2):
    card2[pos1]=samesymbol
    card1[pos1]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbols) # at pos2 in card1 different symbol need to be selcted
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols) # at pos1 in card2  different symbol need to be selected
    symbols.remove(card2[pos1])
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        alphabet1=random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2=random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i]=alphabet1
        card2[i]=alphabet2
    i=i+1
print(card1)
print(card2)
ch=input("spot the similar symbol")
if(ch==samesymbol):
    print("right")
else:
    print("wrong")