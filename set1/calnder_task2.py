# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 09:50:56 2018

@author: I340968
"""

from datetime import datetime as dt
import pytz as pt
timezones=pt.all_timezones

for i in range (len(timezones)):
    zone=timezones[i]
    tz=pt.timezone(zone)
    print("current time at zone", zone ," is ",dt.now(tz))
    