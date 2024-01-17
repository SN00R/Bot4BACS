# Script to convert floorplan into map.


import numpy as np
import cv2
import math
import os.path
 
prompt = '> '
 
print("What is the name of your floor plan you want to convert to a ROS map:") 
file_name = input(prompt)
print("You will need to choose the x coordinates horizontal with respect to each other")
print("Single Click the first x point to scale")

# Read in the image
image = cv2.imread(file_name)

ix,iy = -1,-1
x1 = [0,0,0,0]
y1 = [0,0,0,0]
font = cv2.FONT_HERSHEY_SIMPLEX

# Register the point where you click on the image 

def draw_point(event,x,y,flags,param):
  global ix,iy,x1,y1n,sx,sy
  if event == cv2.EVENT_FLAG_LBUTTON:
    ix,iy = x,y
    print(ix,iy)

# Draws the point with lines around it so you can see it

    image[iy,ix]=(0,0,255)
    cv2.line(image,(ix+2,iy),(ix+10,iy),(0,0,255),1)
    cv2.line(image,(ix-2,iy),(ix-10,iy),(0,0,255),1)
    cv2.line(image,(ix,iy+2),(ix,iy+10),(0,0,255),1)
    cv2.line(image,(ix,iy-2),(ix,iy-10),(0,0,255),1)

# This is for the 4 mouse clicks and the x and y lengths

    if x1[0] == 0:
      x1[0]=ix
      y1[0]=iy
      print('Single click a second x point')   
    elif (x1[0] != 0 and x1[1] == 0):
      x1[1]=ix
      y1[1]=iy
      prompt = '> '
      print("What is the x distance in meters between the 2 points?") 
      deltax = float(input(prompt))
      dx = math.sqrt((x1[1]-x1[0])**2 + (y1[1]-y1[0])**2)*.05
      sx = deltax / dx
      print("You will need to choose the y coordinates vertical with respect to each other")
      print('Single Click a y point')
    elif (x1[1] != 0 and x1[2] == 0):
      x1[2]=ix
      y1[2]=iy
      print('Single click a second y point')
    else:
      prompt = '> '
      print("What is the y distance in meters between the 2 points?") 
      deltay = float(input(prompt))
      x1[3]=ix
      y1[3]=iy    
      dy = math.sqrt((x1[3]-x1[2])**2 + (y1[3]-y1[2])**2)*.05
      sy = deltay/dy 
      print(sx, sy)
      res = cv2.resize(image, None, fx=sx, fy=sy, interpolation = cv2.INTER_CUBIC)
      # Convert to grey
      res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
      cv2.imwrite("KEC_BuildingCorrected.pgm", res );
      cv2.imshow("Image2", res)

      prompt = '> '
      print("What is the name of the new map?")
      mapName = input(prompt)
 
      prompt = '> '
      print("Where is the desired location of the map and yaml file?") 
      mapLocation = input(prompt)
      completeFileNameMap = os.path.join(mapLocation, mapName +".pgm")
      completeFileNameYaml = os.path.join(mapLocation, mapName +".yaml")
      yaml = open(completeFileNameYaml, "w")
      cv2.imwrite(completeFileNameMap, res );

      # write yaml file 
      
      yaml.write("image: " + mapLocation + "/" + mapName + ".pgm\n")
      yaml.write("resolution: 0.050000\n")
      yaml.write("origin: [" + str(-1) + "," +  str(-1) + ", 0.000000]\n")
      yaml.write("negate: 0\noccupied_thresh: 0.65\nfree_thresh: 0.196")
      yaml.close()
      exit()
 
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image',draw_point)
#
#  Waiting for a Esc hit to quit and close everything
#
while(1):
  cv2.imshow('image',image)
  k = cv2.waitKey(20) & 0xFF
  if k == 27:
    break
  elif k == ord('a'):
    print('Done')
cv2.destroyAllWindows()