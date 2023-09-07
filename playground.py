#!/usr/local/bin/local/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import cv2 as cv

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


""" input_data = str('534.17,535.00,23.49,28.75,26.43,46.11,693.543,414')
print("input: ", input_data)
convdata = list(map(float, input_data.split(',')))
rounded = list(np.around(np.array(convdata),2))
 """

#convdata = list(input_data.split(','))
#convertdata = 
""" print(convdata)
print(rounded) """
#bro = [[1693817873.0380318, 75.0, 75.0, 23.27, 25.59, 25.63, 51.38, 686.28, 77661.0],[1693817875.298624, 74.17, 74.17, 23.27, 25.75, 25.67, 51.39, 687.22, 80075.0]]
#bro = [1693817873.0380318, 75.0, 75.0, 23.27, 25.59, 25.63, 51.38, 686.28, 77661.0]
#bro.insert(0, 1693817873.0380318)
#bro.replace("],", "];")
#print(bro)
#print(data)

def percentage_change(col1,col2):
    return ((col2 - col1) / col1) * 100

df = pd.read_csv("/Users/noor/Bot4BACS/Sensoring/serial_testreal.csv")
df_selected = df.loc[1:,['Time','Amb','Temp']]
df_selected = df_selected.dropna()

plt.title("Compare IR Ambient and SCD30 Ambient Temperature")
plt.xlabel("Time")
time = df_selected["Time"]
time = pd.to_datetime(time)
ir = df_selected["Amb"]
scd = df_selected["Temp"]
df_selected["Difference"] = scd-ir
print("smallest difference: ", "%.3f" % df_selected["Difference"].min())
print("highest difference: ", "%.3f" % df_selected["Difference"].max())
mean_diff = df_selected["Difference"].mean()
print("mean_diff: ", "%.3f" % mean_diff)
df_selected["Percentage"] = percentage_change(ir,scd)
mean_diff_perc = df_selected["Percentage"].mean()
print("mean_diff: ", "%.3f" % mean_diff_perc)
plt.ylabel("Temperature in °C")
plt.plot(time,ir,label='IR') 
plt.plot(time,scd,label='SCD30')
plt.xticks(rotation= 30, ha='right')
plt.grid(alpha=0.25)
plt.legend()
#plt.show()
print(df_selected.head())




#print("Collected Data: ", rawdata)

#print("DF: ", df)

#df.to_csv("/Users/noor/Bot4BACS/Sensoring/serial_test.csv", index=False)

#dff = pd.read_csv("/Users/noor/Bot4BACS/Sensoring/serial_test.csv")
#print(dff)


