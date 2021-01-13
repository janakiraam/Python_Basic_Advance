##Python Assert
##==============

'''
Python provide the assert statement to check if a given logical expression is true or false. Program execution proceeds only if the expression
is true and raise AssertionError when it is false.

Code for the assert statement

'''


# Syntax
#==========
#num = 10
#assert num > 11

try:
    num = int(input("Enter a number : "))
    assert num%2 ==0
    print("The number is even")
except AssertionError:
    print("Please enter even number")