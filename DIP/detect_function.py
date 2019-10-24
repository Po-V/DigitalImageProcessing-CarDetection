# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:22:42 2018

@author: Swift 3
"""
import cv2
import numpy as np
cap = cv2.VideoCapture("")
_, frame = cap.read() 

def day_count():
    i = 0
    k = 0
    minArea = 1
    subtractor = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25, detectShadows=True)
 
    while True:
        mask = subtractor.apply(frame)
     
        moments=cv2.moments(mask,True)               #moments method applied
        area=moments['m00']    
        if moments['m00'] >=minArea:
            x=int(moments['m10']/moments['m00'])
            y=int (moments['m01']/moments['m00'])
            if x>396 and x<567 and y>428 and y<438:       #range of line coordinates for values on left lane
                 cv2.putText(frame,'LEFT LANE', (100,600), cv2.FONT_HERSHEY_SIMPLEX,
                       1, (255, 0, 0), 2)
                 print("number of cars in left lane ")
                 i=i+1
                 print(i)
               
            elif (x>765 and x<1100) and (y>524 and y<540): #range of line coordinatess for values on right lane
                cv2.putText(frame,'RIGHT LANE', (800,500), cv2.FONT_HERSHEY_SIMPLEX,
                       1, (255, 0, 0), 2)
                print("number of cars in right lane")
                k=k+1
                print(k)
            
                cv2.putText(frame,'COUNT(left lane): %r' %i, (10,30), cv2.FONT_HERSHEY_SIMPLEX,
                       1, (255, 0, 0), 2)
        
                cv2.putText(frame,'COUNT(right lane): %r' %k, (10,100), cv2.FONT_HERSHEY_SIMPLEX,
                       1, (255, 0, 0), 2)
 
        image, contours, hierarchy =  cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
             if cv2.contourArea(c) < 500:
                  continue 
             x, y, w, h = cv2.boundingRect(c)
             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
             cv2.drawContours(frame,[c], -1, (0, 0, 255), 2)
             cv2.imshow("final", frame)
             if cv2.waitKey(25) & 0xFF == ord('q'):
                 break
             #release the videocapture object
             cap.release()
             #close all the frames
             cv2.destroyAllWindows()
             
def night_detect():
    master = None
    
    while True:
        frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # blur frame
        frame2 = cv2.GaussianBlur(frame1,(21,21),0)
        # initialize master
        if master is None:
           master = frame2
           continue
        frame3 = cv2.absdiff(frame1,frame2)
        # threshold frame
        frame4 = cv2.threshold(frame3,25,255,cv2.THRESH_BINARY)[1]
        # dilate the thresholded image to fill in holes
        kernel = np.ones((3,3),np.uint8)
        frame4 = cv2.erode(frame4,kernel,iterations=1)
        frame5 = cv2.dilate(frame4,kernel,iterations=4)
        # find contours on thresholded image
        nada,contours,nada = cv2.findContours(frame5.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
 
        for c in contours:
            area = cv2.contourArea(c)
            # if the contour is too small, ignore it
            if area > 1000 and area <5000:
               x,y,w,h = cv2.boundingRect(c)
               # plot contours
               if w < 150 and w > 40 and h < 200 and h > 20:
                   cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 3)
    
    
 
        cv2.imshow("final", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
             #release the videocapture object
            cap.release()
             #close all the frames
            cv2.destroyAllWindows()