# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 11:50:54 2018

@author: I340968
"""

#wEEK-3 Monte Hall:
import random
doors=[0]*3
goatdoor=[0]*2
swap=0 # result for win after swap
no_swap=0 #without swap win
j=0
while(j<10):
    x=random.randint(0,2)
    doors[x]="BMW"
    for i in range(0,3):
        if(x==i):
            continue
        else:
            doors[i]="Goat"
            goatdoor.append(i)
    choice=int(input("Enter your choice  "))
    door_open=random.choice(goatdoor) #open a door that comprose of goar
    while(door_open==choice):#door_open and choice should not be same
        door_open=random.choice(goatdoor)
    ch=input("Do you want to swap Y/ N  ")
    if(ch=='Y'):
        if(doors[choice]=='Goat'):
            print("player wins")
            swap=swap+1
        else:
            print("player lost")
    else:
        if(doors[choice]=='Goat'):
            print("player lost")
        else:
            print("player wins")
            no_swap=no_swap+1
    j=j+1
print("the value of swap "+ str(swap))
print("The value of no_swap" +  str(no_swap))
    