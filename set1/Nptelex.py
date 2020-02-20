# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 10:20:52 2018

@author: I340968
"""
#Week2-first disount
#===================

"""c=input("enter the cost\n")
d=int(c)
answer = d*0.9
print(answer)"""


#While condition
#=================

'''n=1
c=1
while(c==1):
    print("Token number",n,"may please come in")
    c=int(input("continue?(0/1)"))
    n=n+116
print("Thanks you this is the end of the day")'''
#'''
#=====
#List
#=====

'''shopping = ["Bread","coffee","Sugar"]
print(shopping)
for item in shopping:
    print(item)
#===========
#append
#===========
shopping.append("Curd")
print(shopping)
print(shopping[1]) 
for i in range(3):
    print(shopping[i])
shopping.insert(1,"oil")
print(shopping)

#+++++++++++++++++
#Count the number of occurence
#============================


ages = [12,23,42,35,12,23,56,78,42,57,70,3,23,43,57,56]
print(ages.count(23))

#=======================
#count of element in a list - using length
#=========================

print(len(ages))
print(len(shopping))
for i in range(len(shopping)):
    print(shopping[i])

#==========================
#To get distinct value from a list
#================================
    
a = set(ages)
print(a)

#===========================
#sorting from a list
#======================

#ages.sort()
#print(ages)

ages.reverse()
print(ages)'''

#=======================================
#slicing
#list_name[start_index:end_index+1]
#==========================================

'''students = ["Arun","Avinash","Ragavan","Aravind","Bibhu","Priyanka","Amulya","Kiran","shubham"]
students.sort()

import numpy as np
ages = [12,23,42,35,12,23,56,78,42,57,70,3,23,43,57,56]
ages_1 = np.sort(ages)
print(ages_1)
j = students[0:5]
print(j)
print(len(students))'''


#============================

# Crowde computing
#=============================

'''import statistics 
#from statistics import mean
Estimates = [1111,342,454,567,750,120,234,561,324,1050,1500,100,180,1000,150,250]
Estimates.sort()
print(Estimates)
tv = int(0.1 * len(Estimates))
Estimates = Estimates[tv:]
Estimates = Estimates[:len(Estimates)-tv]
print(Estimates)
#print(mean(Estimates))
print(statistics.mean(Estimates))'''

##========================================

##Another way to do above program

##========================================
'''import statistics 
#from scipy import stats
import scipy
Estimates = [1111,342,454,567,750,120,234,561,324,1050,1500,100,180,1000,150,250]
Estimates.sort()
#m = stats.trim_mean(Estimates,0.1)
m = scipy.stats.trim_mean(Estimates,0.1)
print(m)'''

##========================================

# Plotting sample
##==========================================

'''import matplotlib.pyplot as plt
#plt.plot([1,2,3,2.5])
#plt.plot([1,2,3,4],[1,4,9,16])
#plt.plot([1,2,3,4],[1,4,9,16],'ro')
#plt.plot([1,2,3,4],[1,4,9,16],'r--')
#plt.plot([1,2,3,4],[1,4,9,16],'bs')
plt.plot([1,2,3,4],[1,4,9,16],'g^')
plt.ylabel("Some Value")
plt.xlabel("testing")'''

#=====================================
#Ploting the estimates
#===============================
'''import statistics 
import matplotlib.pyplot as plt
Estimates = [1111,342,454,567,750,120,234,561,324,1050,1500,100,180,1000,150,250]
y=[]
#for i in range(len(Estimates)): # as len(estimates) is changed it has to add after changing
#    y.append(5)
Estimates.sort()
tv = int(0.1 * (len(Estimates)))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv]
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates,y,'r--')
plt.plot([statistics.mean(Estimates)],[5],'ro')
plt.plot([statistics.median(Estimates)],[5],'bs')'''

##==================================================
# week3 assignment 2
#==================================================

'''list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
a,b = input().split()
a,b = int(a),int(b)
list_1 = list_1[a:b]
print (list_1)
for i in range(len(list_1)):
    print(list_1[i])'''

##==================================================
#Week3 assignment 2
##===================================================

list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
a = int(input())
count = 0
for i in range(len(list_1)):
    if list_1[i] != a:
     if list_1[i]%a==0:
         count=count+1
print(count)
    
