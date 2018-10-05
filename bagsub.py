# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 10:58:36 2018

@author: Tanvir Hossain
"""

import cv2
import numpy as np 
from os import listdir
from os.path import isfile, join
import re
import time 

dir_image = "test footage/"
dir_result = "result_footage"

cap=cv2.VideoCapture(r"street2.mp4")
subtractor = cv2.createBackgroundSubtractorMOG2(history = 120, varThreshold = 50, detectShadows = False)

i = 0
name_store = []                     """ 1) do the sleep thing 3)try to capture from screen 4)try to capture from browser 5) tune the pixel value"""
count=[]
while True:
    try:
        name = "street_" + str(i) + ".jpg"
        name = join(dir_result,name)
        ret, frame = cap.read()
        
        if ret:    
            mask = subtractor.apply(frame)
            cv2.imshow('original',frame)
            cv2.imshow('original-mask',mask)
            
            if cv2.countNonZero(mask) <= 50 and cv2.countNonZero(mask) >= 20:
                cv2.imwrite(name, frame)    
                count.append(cv2.countNonZero(mask))
                name_store.append(name)
                print(count[i])  #count non zero pixel
            
                
            
                cv2.imshow('stoppings',frame)
                cv2.imshow('stoppings mask',mask)
                
                i+=1
                
                #time.sleep(60)
    
            elif (cv2.waitKey(40) & 0xFF) == ord('q'): # Hit `q` to exit
                break
        else:
            break
    except Exception as e:
         print(e)
file = 'values.xlsx'
with open(join(dir_image, file), 'w') as f:
            for pix_count, name in zip(count, name_store):
                f.write(str(pix_count))
                f.write("   -----" + str(name))
                f.write("\n")

cap.release()
cv2.destroyAllWindows()
