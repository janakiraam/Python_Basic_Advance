# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 00:03:30 2018

@author: I340968
"""

import calendar

def check_leap(y):
    if y%100==0:
        if y%100==0:
            return True
        else:
            return False
    else:
        if y%4==0:
            return True
        else:
            return False
        
def check_valid_date(dt,m,y,l):
    if l:
        if m==2:
            if dt<30:
                return True
            else:
                return False
        else:
            if m<8:
                if(m%2==1):
                    if dt < 32:
                        return True
                    else:
                        return False
                else:
                    if dt < 31:
                        return True
                    else:
                        return False
            else:
                if(m%2==0):
                    if dt < 32:
                        return True
                    else:
                        return False
                else:
                    if dt < 31:
                        return True
                    else:
                        return False
    else:
        if m==2:
            if dt<29:
                return True
            else:
                return False
        else:
            if m<8:
                if(m%2==1):
                    if dt < 32:
                        return True
                    else:
                        return False
                else:
                    if dt < 31:
                        return True
                    else:
                        return False
            else:
                if(m%2==0):
                    if dt < 32:
                        return True
                    else:
                        return False
                else:
                    if dt < 31:
                        return True
                    else:
                        return False
def get_day(day_index):
    list_of_days=['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday']
    return list_of_days[day_index]
                
while(1):
    year = int(input("Enter year 1970-2018:  "))
    if year < 1970:
        print("Not valid please enter valid value ")
    else:
        break
    
while(1):
    month = int(input("Enter year 1-12:  "))
    if month < 13 and month > 0:
        break
    else:
        print("Not valid please enter valid value  ")

leap = check_leap(year)

while(1):
    date = int(input("Enter the date:  "))
    if date > 0 and check_valid_date(date,month,year,leap):
        break
    else:
        print("Not valid please enter valid value  ")
        
day_index=calendar.weekday(year,month,date)
day=get_day(day_index)

print(date,"/",month,"/",year," falls on ",day )

