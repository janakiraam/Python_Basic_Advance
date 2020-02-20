# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:54:56 2018

@author: I340968
"""
import random

def choose():
    words=['rainbow','computer','science','maths','Software','English','water','board']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    #jumbled=random.sample(word,len(word))
    #jumbled=" ".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,' Your score is:',p1)
    print(p2n,' Your score is:',p2)
    print('Thnaks for playing')
    
    
def play():
    p1name=input('player 1, please enter your name')
    p2name=input('player 2, Please enter your name')
    pp1=0
    pp2=0
    turn = 0
    while(1):
        #computer task
        picked_word=choose()
        #create the questions
        qn=jumble(picked_word)
        print(qn)
        #player 1
        if turn%2==0:
            print(p1name,"this is your turn")
            ans=input('what is on my mind?')
            if ans==picked_word:
                pp1=pp1+1
                print('your score is',pp1)
            else:
                print('Better luck nexgt time.I thought:',picked_word)
            c=int(input('press 1 to continue and 0 to quit:'))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        #player 2
        else:
            print(p2name,"this is your turn")
            ans=input('what is on my mind?')
            if ans==picked_word:
                pp2=pp2+1
                print('your score is',pp2)
            else:
                print('Better luck nexgt time.I thought:',picked_word)
            c=int(input('press 1 to continue and 0 to quit:'))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn=turn+1
play()