"""

Before strating mypy need to be installed

Scenario 1:
============


def myfunction(myparameter :int):
    print(myparameter)

myfunction("Hello World")

Output:
=======

on executing the above code:

dir : > python mypytypehinting.py
Hello World

dir : > mypy mypytypehinting.py
mypytypehinting.py:4: error: Argument 1 to "myfunction" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)



Scenario 2:
============

def myfunction1(myparameter :int):
    print(myparameter)

myfunction1(10)


Output:
=========

dir : > python mypytypehinting.py
10

dir : > mypy mypytypehinting.py
Success: no issues found in 1 source file
"""

""":cvar


Scenario 3:
===========





def myfunction1(myparameter :int) -> str: # retrun srting
    return f"{myparameter + 10}"

def otherfunction(otherparameter :str):
    print(otherparameter)

otherfunction(myfunction1(10))


output:
=======

dir : >mypy mypytypehinting.py
Success: no issues found in 1 source file

dir: >python mypytypehinting.py
20

"""

def myfunction1(myparameter :int) -> str: # retrun srting
    return f"{myparameter + 10}"

def otherfunction(otherparameter :int):
    print(otherparameter)

otherfunction(myfunction1(10))



"""

output:

dir : > mypy mypytypehinting.py
mypytypehinting.py:85: error: Argument 1 to "otherfunction" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)


"""





