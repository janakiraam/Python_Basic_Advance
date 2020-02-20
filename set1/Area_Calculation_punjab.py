# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 08:30:32 2018

@author: I340968
"""

import numpy as np
from PIL import Image
width=5
height=4
array=np.zeros([height,width,3],dtype=np.uint8)
#np.zero-> make array of size given dimention, 3-> each pixel contain 3 bytes R,B,G each one byte
#dtype ->  data type assigned here, uint-> unsigned int
img=Image.fromarray(array)
img.save('test.jpg')
array1=np.zeros([100,200,3],dtype=np.uint8)
array1[: , :100]=[255,128,0]
array1[: , 100:]=[0,0,255]
img1 = Image.fromarray(array1)
img1.save('test1.jpg')