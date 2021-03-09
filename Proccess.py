# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:25:27 2021

@author: Avinash vishwakarma
"""

from PIL import Image 
import numpy

def process(img):
    
    ar=numpy.array(img)  
    gimg = img.convert('L') # converting it into gray scale

    new_image=gimg.resize((28,28))
    
    ar=numpy.array(new_image)
       
    img_array=ar.flatten()
    return img_array



