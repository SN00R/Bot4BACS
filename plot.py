import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime

df1 = pd.read_csv('/home/hello-robot/Bot4BACS/F3_B8_07_6C_28_8E.csv')    #Window
df2 = pd.read_csv('/home/hello-robot/Bot4BACS/C3_23_CF_79_6C_FB.csv')    #Coffee Desk
df3 = pd.read_csv('/home/hello-robot/Bot4BACS/DD_3F_BC_9B_56_EC.csv')    #Meeting Table
df4 = pd.read_csv('/home/hello-robot/Bot4BACS/E9_FC_42_4B_FB_7C.csv')    #Robot
df5 = pd.read_csv('/home/hello-robot/Bot4BACS/FE_ED_E9_B2_20_8E.csv')    #Not in Flight Arena
print(df1.head())
print(df2.head())

time = pd.to_datetime(df1["Time"])
#new_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
print(time)
print(type(time))
gas1 = df1.iloc[:,2]
gas2 = df2.iloc[:,2]
gas3 = df3.iloc[:,2]
plt.plot(time, (gas1,gas2,gas3))
plt.show()


""" df.plot(x="Time", y=["CO2", "Temperature", "Pressure"])
plt.show() """


""" 
plt.plot(df["Time"], df["CO2"])
plt.show()

 """