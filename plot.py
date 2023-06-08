import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/home/hello-robot/Bot4BACS/F3_B8_07_6C_28_8E.csv')
df.head()

time = df.iloc[2,0]
print(time)
print(time.info())

gas = df.iloc[:,2]
#print(gas)

""" plt.plot(time, gas)
plt.show()
 """

""" df.plot(x="Time", y=["CO2", "Temperature", "Pressure"])
plt.show() """


""" 
plt.plot(df["Time"], df["CO2"])
plt.show()

 """