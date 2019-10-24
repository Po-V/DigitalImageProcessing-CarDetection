# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 12:48:08 2018

@author: Swift 3
"""
import cv2
from detect_function import day_count
from detect_function import night_detect

cap = cv2.VideoCapture("cars_night.mp4")
ret, frame = cap.read() 
if ret is True:
   img1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   [nrow,ncol] = img1.shape
   dark = 0
   bright=0
   threshold = 150
   for x in range(0,nrow):
      for y in range(0,ncol):
          if img1[x,y] <= threshold:
             dark=dark+1
          else:
             bright = bright+1
   if (bright > dark):
      day_count()  
   else:
      night_detect()   

