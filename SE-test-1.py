import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp

#set up access for webcam
cap=cv2.VideoCapture(0)
#accessing webcams,0 stands for "capture video capture device 0 which is the webcam",cap ussed read webcam feed from now
#while cap.isOpened(): #initiate loop for access to webcam
    #read feed,reading frames from the webcam,stack rfames to make it look like a video,ret=return value,frame=imagefrom webcam
 #   ret, frame=cap.read()
    #showing user the result
  #  cv2.imshow('opencv Feed',frame)
    
    #breaking gracfully
    #waitkey=wait for key to be pressed
    #if current key is q then break
#    if cv2.waitKey(100000) & 0xFF == ord('q'):
 #           break
  #  cap.release()
   # cv2.destroyAllWindows()

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    
    
    cv2.imshow('Frame', frame)

    
    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
