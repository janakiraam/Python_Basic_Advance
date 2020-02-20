# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 09:47:02 2018

@author: I340968
"""

from PIL import Image
im=Image.open('test.jpg')
rgb_im=im.convert('RGB')
r,g,b=rgb_im.getpixel((1,1))
print(r,g,b)
