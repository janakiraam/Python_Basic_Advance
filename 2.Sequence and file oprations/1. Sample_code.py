# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 05:38:22 2020

@author: I340968
"""

#1.len output
nums=set([1,1,2,3,3,3,4,4])
print(len(nums))

#2.Output for keys.

d={"john":40,"peter":45}
print(list(d.keys()))

#3.Python module to check possward
import re
password=input("Enter Password : " )
flag = 0
'''print(len(password))'''
if(len(password)<6 or len(password)>12):
    flag=-1
elif not re.search("[a-z]",password):
    flag=-1
elif not re.search("[A-Z]",password):
    flag=-1
elif not re.search("[@_$]",password):
    flag=-1
elif not re.search("[0-9]",password):
    flag=-1

if(flag==-1):
    print("Invalid Passowrd")
else:
    print("Valid Password")
    
#4. printing list along with position

a=[4,7,3,2,5,9]
for i in a:
    print(a.index(i),i)
    
#5. Printing even index in a string
inputchar=input("String for pirnitn even index:  ")
if inputchar:
    string=""
    for i in inputchar:
        if inputchar.index(i)%2==0:
            string+=str(i)
print(string)

#5.1. Printing even index in a string(another way)
inputchar1=input("String for pirnitn even index:  ")
j=list(inputchar1)
print(j)
s1=""
for i in j:
    if j.index(i)%2==0:
        s1+=str(i)
print(s1)

#6. reversing a string
rvs=input("Enter the string for reverse:  ")
svr=rvs[::-1]
print(svr)

#7.count and print no.of.occurance of each character
import string

s = input()
for letter in string.ascii_lowercase:
    cnt = s.count(letter)
    if cnt > 0:
        print("{},{}".format(letter,cnt))
        
#8. Intesection of two set

j=[1,3,6,78,35,55]
k=[12,24,35,24,88,120,155]
r=list(set(j) & set(k)) 
print(r)

#9. removing duplicate and printing in reverse

a = [12,24,35,24,88,120,155,88,120,155]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

j=uniq_items
print(j)
print(j[::-1])

#10. Removing 24

n1=[12,24,35,24,88,120,155]
for x in n1:
    if (x==24):
        n1.remove(24)
print(n1)

#11.removing the 0th,4th,5th

n2=[12,24,35,70,88,120,155]
#n3=enumerate(n2)
#print(list(n3))
el1=[]
for (i,x) in enumerate(n2):
    if i not in(0,4,5):
        el1.append(x)
print(el1)


#12.rmoving divisbles of 5 and 7
n3=[12,24,35,70,88,120,155]
el2=[]
for x in n3:
    if x%5!=0 and x%7!=0:
        el2.append(x)
print(el2)
'''
#13. Random 5 number divisible by 5 and 7 
import random
el3=[]
for i in range (1,1001):
    if i%5==0 and i%7==0:
        el3.append(i)
#print(el3)
print(random.sample(el3,5))
'''
#12.program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input

n=int(input())
s=0
for i in range(1,n+1):
    s=s+(i/(i+1))
print(s)


'''
Answers:
=======

runfile('C:/Users/i340968/Desktop/ed-code/Python/2.Sequence and file operation/Case1.py', wdir='C:/Users/i340968/Desktop/ed-code/Python/2.Sequence and file operation')
4
['john', 'peter']

Enter Password : janaki
Invalid Passowrd
0 4
1 7
2 3
3 2
4 5
5 9

String for pirnitn even index:  janakiraam
jnkr

String for pirnitn even index:  janakiraam
['j', 'a', 'n', 'a', 'k', 'i', 'r', 'a', 'a', 'm']
jnkr

Enter the string for reverse:  jnkdle
eldknj

janakiraam
a,4
i,1
j,1
k,1
m,1
n,1
r,1
[35]
[12, 24, 35, 88, 120, 155]
[155, 120, 88, 35, 24, 12]
[12, 35, 88, 120, 155]
[24, 35, 70, 155]
[12, 24, 88]
[910, 140, 175, 455, 665]

5
0.5
1.1666666666666665
1.9166666666666665
2.716666666666667
3.5500000000000003
'''
