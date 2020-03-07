# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:46:38 2020

@author: I340968
"""


#1. Factorial program

num=int(input())
factorial=1
if num<0:
    print("No factorial for negative")
elif num==0:
    print("For 0 factorial is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("factoral of numbe ",num," is ", factorial)
if(factorial%2==0):
    print("Factoral is even")
else:
    print("factorial is odd")
    
 



#2.Taking words and arranging in ahphabatical order
    
str1=input()
word=str1.split()
word.sort()
for i in word:
    print(i)


#3. Finding eveen number in range 1000 to 30000
   

values=[]
for x in range(1000,3000):
    s=str(x)
    if (int(s[0]) %2 == 0) and (int(s[1]) %2 == 0) and (int(s[2]) %2 == 0) and (int(s[3]) %2 == 0):
        values.append(s)
print ("-".join(values))


#4.Digits and number count.

s = input()
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)
    


#5.Planidrom or not

i=input()
j=(''.join(reversed(i)))
if(i==j):
  print('YES')
else:
  print('NO')





    
