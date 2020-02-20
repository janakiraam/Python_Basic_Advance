# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 10:15:12 2018

@author: I340968
"""

'''for i in range (1,51):
    if(i%3==0):
        print(str(i)+" = FIZZ")
    else:
        if(i%5==0):
            print(str(i)+" = BUZZ")
        else:
            if(i%3==0 and i%5==0):
                print(str(i)+" = FizzBuzz")
            else:
                print(i)'''
                
'''for i in range (1,51):
    if(i%3==0 and i%5==0):
                print(str(i)+" = FizzBuzz")
    else:
        if(i%5==0):
            print(str(i)+" = BUZZ")
        else:
            if(i%3==0):
                print(str(i)+" = FIZZ")            
            else:
                print(i)'''
                
##========================================================
#Function definition
##================================================
def FizzBuzz(r):
    for i in range (1,r):
        if(i%3==0 and i%5==0):
                    print(str(i)+" = FizzBuzz")
        else:
            if(i%5==0):
                print(str(i)+" = BUZZ")
            else:
                if(i%3==0):
                    print(str(i)+" = FIZZ")            
                else:
                    print(i)

FizzBuzz(51)
            