# -*- coding: utf-8 -*-
"""
Created on Fri May 18 18:36:59 2018

@author: Admin
"""
# to import image on to the python using opencv
import cv2 as cv
import numpy as np
image_black=np.zeros((256,256))
image_1=np.ones((256,256,3))*255
cv.imshow("black", image_black)
cv.waitKey(0)