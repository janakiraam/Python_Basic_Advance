# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 08:04:33 2018

@author: I340968
"""

import random
import matplotlib.pyplot as plt
 
'''bet = int(input("Your bet from 1 to 10 :  "))
lucky_draw = random.randint(1,10)
print(lucky_draw)
account = 0
if (bet==lucky_draw): 
    account=account+900-100 # spent 100 so rduced
else:
    account =  account-100
print(account)'''


'''account = 0
for i in range(30):
    bet = random.randint(1,10)
    lucky_draw = random.randint(1,10)
    print("Lucky draw ",lucky_draw)
    print("Bet", bet)
    if (bet==lucky_draw): 
        account=account+900-100 # spent 100 so rduced
    else:
        account =  account-100
print("amount in your game account", account)'''

#for visuvalizing plot
account = 0
x = []
y = []
for i in range(30):
    x.append(i+1)
    bet = random.randint(1,10)
    lucky_draw = random.randint(1,10)
    print("Lucky draw ",lucky_draw)
    print("Bet", bet)
    if (bet==lucky_draw): 
        account=account+900-100 # spent 100 so rduced
    else:
        account =  account-100
    y.append(account)
print("amount in your game account", account)
plt.plot(x,y)
plt.show()
