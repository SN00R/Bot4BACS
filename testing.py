import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime

terms=[]

df1 = pd.read_csv('/home/hello-robot/Bot4BACS/F3_B8_07_6C_28_8E.csv')    #Window
df2 = pd.read_csv('/home/hello-robot/Bot4BACS/C3_23_CF_79_6C_FB.csv')    #Coffee Desk
df3 = pd.read_csv('/home/hello-robot/Bot4BACS/DD_3F_BC_9B_56_EC.csv')    #Meeting Table
df4 = pd.read_csv('/home/hello-robot/Bot4BACS/E9_FC_42_4B_FB_7C.csv')    #Robot
df5 = pd.read_csv('/home/hello-robot/Bot4BACS/FE_ED_E9_B2_20_8E.csv')    #Not in Flight Arena
helpertime= []

for i in range(5):
    helpertime = pd.to_datetime(df["Time"])


time1 = pd.to_datetime(df1["Time"])
time2 = pd.to_datetime(df2["Time"])
time3 = pd.to_datetime(df3["Time"])
time4 = pd.to_datetime(df4["Time"])
time5 = pd.to_datetime(df5["Time"])
#new_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")

gas1 = df1.iloc[:,3]
gas2 = df2.iloc[:,3]
gas3 = df3.iloc[:,3]
gas4 = df4.iloc[:,3]
gas5 = df5.iloc[:,3]
#ax = plt.axes()
plt.title('Temperature Measurements on 08.06.2023')
plt.plot(time1, gas1/100, label="Window")
plt.plot(time2, gas2/100, label="Coffee")
plt.plot(time3, gas3/100, label="Meeting")
plt.plot(time4, gas4/100, label="Robot")
plt.plot(time5, gas5/100, label="Secret")
plt.legend(loc='lower right')
plt.xlabel('Time')
plt.ylabel('Temperature in °C')
plt.xticks(rotation= 30, ha='right')
plt.show()


""" df.plot(x="Time", y=["CO2", "Temperature", "Pressure"])
plt.show() """


""" 
plt.plot(df["Time"], df["CO2"])
plt.show()
 """

"""fig, axs = plt.subplots(2, 3)
axs[0,0].plot(time,merged,label=["Window","Coffee","Meeting","Robot"])
axs[0,0].set_title('CO2 Measurements on 21.06.2023 for calibration')
plt.show() 

merged = pd.concat([df1["CO2"],df2["CO2"],df3["CO2"],df4["CO2"]],axis=1)
merged = merged.dropna()
"""