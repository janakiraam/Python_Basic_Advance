# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:50:31 2021

"""

import threading

'''
def helloworld():
    print("Hello world")

t1=threading.Thread(target=helloworld)
t1.start()
'''
'''

def function1():
    for x in range(100):
        print("one")

def function2():
    for x in range(100):
        print("Two")
        
t1=threading.Thread(target=function1)
t2=threading.Thread(target=function2)

t1.start()
t2.start()
'''


"""
if the above code is as 
function1()
function2()

instead of threads then one will print first then two
"""

### waiting for a thread.

def function1():
    for x in range(10):
        print("one")
t1=threading.Thread(target=function1)
t1.start()

print("an another text")

### tha another text will print before 10 times printing of one eventhough it is last. Now we need to interdue
### wait for tread to complete by using join

def function1():
    for x in range(10):
        print("one")
t1=threading.Thread(target=function1)
t1.start()

t1.join()

print("an another text")






