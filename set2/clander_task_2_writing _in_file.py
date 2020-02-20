# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 09:59:15 2018

@author: I340968
"""

from datetime import datetime as dt
import pytz as pt
timezones=pt.all_timezones
f=open("timezone.txt","w+")

for i in range (len(timezones)):
    zone=timezones[i]
    tz=pt.timezone(zone)
    print("current time at zone", zone ," is ",dt.now(tz))
    f.write("current time at zone  " + str(zone) +" is " + str(dt.now(tz)))
f.close
    