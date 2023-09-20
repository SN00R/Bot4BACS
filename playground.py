#!/usr/local/bin/local/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
#import cv2 as cv

def percentage_change(col1,col2):
    return ((col2 - col1) / col1) * 100

#xaxis = ['SCD30', 'Testo', 'IR']

#print("Mean Difference Truth - IR: ", "%.3f" % testo.mean()-ir.mean())
#print("Mean Difference Truth - SCD: ", "%.3f" % testo.mean()-scd.mean())
#print("Mean Difference Truth - emp1: ", "%.3f" % testo.mean()-emp1.mean())
#print("Mean Difference Truth - emp2: ", "%.3f" % testo.mean()-emp2.mean())

#df_sensoren["Percentage"] = percentage_change(ir,scd)
#df_sensoren["Testo_SCD"] = scd - testo
#df_sensoren["Testo_IR"] = ir - testo


#mean_diff_perc = df_sensoren["Percentage"].mean()
#print("mean_diff: ", "%.3f" % mean_diff_perc)print(df_sensoren) 

fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twiny()
ax.set_title('Comparison of Sensors: Temperature')
#bp = ax.boxplot(data, labels=xaxis, patch_artist=True)
#colors = ['pink', 'lightblue', 'lightgreen', 'plum']
colors = ['pink', 'lightblue', 'thistle','lightgreen', 'plum']
#for patch, color in zip(bp['boxes'], colors):
    #patch.set_facecolor(color)
#ax.grid(True)
ax.set_ylabel('Temperature in °C')
ax.set_xlabel('Time')
#ax.plot(timesens, ir, 'o', label='IR')
#ax.plot(timesens, scd, 'o', label='SCD')
#ax.plot(timesens, df_sensoren["Testo_IR"], label='IR')
#ax.plot(timesens, df_sensoren["Testo_SCD"], label='SCD')
#ax2.plot(time_truth,testo, 'o', label="Testo", color='green')
#ax2.set_xlabel(r"Time")

#ax.plot(time_truth, testo, label='Testo')
#ax.legend()
#plt.plot(time,testo,label='Testo')

#plt.xticks(rotation= 30, ha='right')
plt.grid(True, alpha = 0.4)
ax.legend()
ax2.legend()
#plt.legend()
plt.show()
#fig.savefig('/Users/noor/Bot4BACS/Testo_Cal/CO2.png',bbox_inches='tight', dpi=200)


""" #Mouse callback function
def draw_shape(event,x,y,flags,param):
    ("event : ",event)
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

cv.destroyWindow('DrawWithMouse') """


"""
convdata = list(map(float, input_data.split(',')))
rounded = list(np.around(np.array(convdata),2))
 """

 #convdata = list(input_data.split(','))
#bro.replace("],", "];")