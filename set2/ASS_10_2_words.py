# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 20:27:26 2018

@author: I340968
"""

'''words = input().split(',')
words.sort()
for word in range (len(words)):
    if word < (len(words))-1:
        print(words,end=',')
    else:
        print(words)'''
        
        
words = input().split(',')

# sort the list
words.sort()
#print(len(words))

# display the sorted words

#print("The sorted words are:")
for i in range (len(words)):
    if i < len(words)-1:
        print(words[i],end=',')
    else:
        print(words[i])