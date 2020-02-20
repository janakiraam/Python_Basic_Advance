# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 09:57:39 2018

@author: I340968
"""

import scipy.misc
from PIL import Image
import numpy as np
import random 

img=scipy.misc.imread("map-01.jpg")
count_pun=0
count_in=0
count=0
while(count<=10000):
    x=random.randint(0,52)
    y=random.randint(0,89)
    z=0
    if(img[x][y][z]==89):
        count_in=count_in+1
        count=count+1
    else:
        if(img[x][y][z]==253):
            count_pun=count_pun+1
            count=count+1
area_pun=(count_pun/count_in)*3287263
print(area_pun)