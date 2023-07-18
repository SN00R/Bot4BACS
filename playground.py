#!/usr/local/bin/local/python3
import numpy as np
import cv2 as cv

#Mouse callback function
def draw_shape(event,x,y,flags,param):
    print("event : ",event)
    if event == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),100,(255,0,0),-1)

#Create a black image, a window and bind the function to the window
img = np.zeros((780,780,3),np.uint8)
cv.namedWindow('DrawWithMouse')
cv.setMouseCallback('DrawWithMouse',draw_shape)

while(1):
    cv.imshow('DrawWithMouse',img)
    if cv.waitKey(10) & 0xFF == 27: #ANDing with 0xFF as my machine is 64 bit
        break

cv.destroyWindow('DrawWithMouse')