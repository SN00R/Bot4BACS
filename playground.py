#!/usr/local/bin/local/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import cv2 as cv

def percentage_change(col1,col2):
    return ((col2 - col1) / col1) * 100

# Read measurements from own I2C Bus
df_sensoren = pd.read_csv("/Users/noor/Bot4BACS/Testo_Cal/serial_test_cal.csv")
df_sensoren = df_sensoren.loc[1:,:].dropna()

# Read measurements from testo 500 
df_truth = pd.read_csv("/Users/noor/Bot4BACS/Testo_Cal/2023-09-07-16-48-42.csv")
df_truth = df_truth.dropna()

# Read measurements from Empairs
df1 = pd.read_csv('/Users/noor/Bot4BACS/Testo_Cal/F3_B8_07_6C_28_8E.csv')    
df2 = pd.read_csv('/Users/noor/Bot4BACS/Testo_Cal/DD_3F_BC_9B_56_EC.csv')    
df1 = df1.dropna()
df2 = df2.dropna()

plt.title("Compare Temperature")
plt.xlabel("Time")
time = df_sensoren["Time"]
time = pd.to_datetime(time)
ir = df_sensoren["Amb"]
scd = df_sensoren["Temp"]
testo = df_truth["274 [°C]"]
emp1 = df1["Temperature"]
emp2 = df2["Temperature"]
#print("Mean Difference Truth - IR: ", "%.3f" % testo.mean()-ir.mean())
#print("Mean Difference Truth - SCD: ", "%.3f" % testo.mean()-scd.mean())
#print("Mean Difference Truth - emp1: ", "%.3f" % testo.mean()-emp1.mean())
#print("Mean Difference Truth - emp2: ", "%.3f" % testo.mean()-emp2.mean())

#df_sensoren["Percentage"] = percentage_change(ir,scd)
#mean_diff_perc = df_sensoren["Percentage"].mean()
#print("mean_diff: ", "%.3f" % mean_diff_perc)
plt.ylabel("Temperature in °C")
plt.plot(time,ir,label='IR') 
plt.plot(time,scd,label='SCD30')
plt.plot(time,testo,label='Testo')
#plt.plot(time,emp1,label='Empair_1')
#plt.plot(time,emp2,label='Empair_2')
plt.xticks(rotation= 30, ha='right')
plt.grid(alpha=0.25)
#plt.savefig('/Users/noor/Bot4BACS/cal3/'+str(x)+'.png',bbox_inches='tight', dpi=200)
plt.legend()
plt.show()


""" #Mouse callback function
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

cv.destroyWindow('DrawWithMouse') """


"""
convdata = list(map(float, input_data.split(',')))
rounded = list(np.around(np.array(convdata),2))
 """

 #convdata = list(input_data.split(','))
#bro.replace("],", "];")