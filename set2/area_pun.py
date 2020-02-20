# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:06:02 2018

@author: I340968
"""

from PIL import Image
import random
im=Image.open("map-01.jpg")
rgb_im=im.convert("RGB")
count_in=0
count_pun=0
count=0
while(count<=100000):
    x=random.randint(0,56)
    y=random.randint(0,99)
    z=0
    r,g,b=rgb_im.getpixel((x,y))
    if(r==60):
        count_in=count_in+1
        count=count+1
    else:
        if(r==80):
            count_pun=count_pun+1
            count=count+1

area_pun=(count_pun/count_in)*3287263
print(area_pun)