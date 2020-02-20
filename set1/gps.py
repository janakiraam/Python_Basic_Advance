# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:12:55 2018

@author: I340968
"""

import csv
from gmplot import gmplot
'''with open('route.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        lat = row[0]
        long = row[1]
        print(lat)
        print(long)
        print()'''
        
gmap = gmplot.GoogleMapPlotter(27.687738,76.32448,17)
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

with open('route.csv','r') as f:
    reader = csv.reader(f)
    k=0
    for row in reader:
        lat = float(row[0])
        long = float(row[1])
        
        if(k==0):
            gmap.marker(lat,long,'yellow')
            k = 1
        else:
            gmap.marker(lat,long,'red')

#gmap.marker(lat,long,'blue')
gmap.draw("mymap.html")
            

    