# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 22:09:58 2021

@author: I340968
"""

"""

a =b 
b

1.Ways to handle exceotion,2. Exception with exact error,3. defining known exception,4. getiing default  exception, 
5.try.. Else block,6. Finally block,7. Custom exception:

"""

### 1.Ways to handle exceotion
###============================

try:
    #code block where exception can occur
    a=b
    
except:
    print("some exception may have occured")
    
    
### 2. Exception with exact error
###================================

try:
    #code block where exception can occur
    a=b
    
except Exception as ex:
    print(ex)
    
### 3. defining known exception:
###==============================

try:
    #code block where exception can occur
    a=b
    
except NameError as ex1:
    print("User is not defined the exception")

    
except Exception as ex:
    print(ex)


### 4. getiing default  exception:
###==============================


try:
    #code block where exception can occur
    a=1
    b="5"
    c=a+b
    
except NameError as ex1:
    print("User is not defined the exception")

    
except Exception as ex:  ### generic expression best practice to have at last
    print(ex)
    
### 5.try.. Else block
###====================

try:
    #code block where exception can occur
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    c=a+b
    d=a*b
    e=a/b
    f=a-b
    
except NameError:
    print("User is not defined the exception")

except ZeroDivisionError:
    print("Please don't divide by zero")

except TypeError:
    print("Please use similar type")

    
except Exception as ex:  ### generic expression best practice to have at last
    print(ex)
    
else:  ### trigger once the exception is not triggered
    print(c)
    print(d)
    print(e)
    print(f)


### 6. Finally block
###=================

try:
    #code block where exception can occur
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    c=a+b
    d=a*b
    e=a/b
    f=a-b
    
except NameError:
    print("User is not defined the exception")

except ZeroDivisionError:
    print("Please don't divide by zero")

except TypeError:
    print("Please use similar type")

    
except Exception as ex:  ### generic expression best practice to have at last
    print(ex)
    
else:  ### trigger once the exception is not triggered
    print(c)
    print(d)
    print(e)
    print(f)

finally: ### Finally block will executed at any point
    print("Exceution is done")


#### 7. Custom exception:
#### ===================

class Error(Exception):
    pass
class dobException(Error):
    pass

year = int(input("Please enter the year of birth: "))
age = 2021-year

try:
    if age<=30 & age>20:
        print("You can apply for exame, age is fine")        
        
    else:
        raise dobException

except dobException:
    print("The year age is not valid")









