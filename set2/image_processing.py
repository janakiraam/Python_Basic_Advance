# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:48:38 2018

@author: I340968
"""
'''
#flipping the image.

from PIL import Image

image = Image.open('img1.jpg')

#transportsing
transposed_img = image.transpose(Image.FLIP_LEFT_RIGHT)

#save in a file after transpose
transposed_img.save('imag1.jpg')
print('Done fliping')'''

#Image Enhancement - histrogram equvalization (CLAHE)

import cv2

#read the image

img = cv2.imread('img1.jpg')

#preparation fro CLAHE
clahe = cv2.createCLAHE()

#Converting into grey scale image
gray_img = cv2.cvtColor(img, cv2.Color_BGR2GRAY)

#Apply enhancement process
enh_img = clahe.apply(gray_img)

#save in a file
cv2.imWrite('enhance_img.jpg', enh_img)
print('done enhancement')