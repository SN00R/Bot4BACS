#!/usr/local/bin/local/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import cv2 as cv

dfm = pd.read_csv("/Users/noor/Bot4BACS/Sensoring/VisionWood_Backup.csv")
dfm = dfm[dfm['LightFront']<100]
dfm = dfm[dfm['LightTop']<750]
timecol = pd.to_datetime(dfm["Time"], format = '%Y-%m-%d %H:%M:%S') 

plt.xlabel("Time")
plt.ylabel("Brightness in lux")

data1 = dfm['LightTop']
plt.title('Top Sensor Measurements')
plt.xticks(rotation= 30, ha='right')
plt.plot(timecol, data1)
plt.show()
plt.savefig('/Users/noor/Bot4BACS/Sensor_Figures/VW_Final_BrightnessTop.png',bbox_inches='tight', dpi=200) 
#plt.savefig('/Users/noor/Bot4BACS/Sensor_Figures/VW_Final_BrightnessTop.pdf',bbox_inches='tight', dpi=200) 