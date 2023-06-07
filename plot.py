import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('/home/hello-robot/Bot4BACS/F3_B8_07_6C_28_8E.csv')
print(df.info())
""" time = df.iloc[:,0]
co2 = df.iloc[:,1]
print(time.head())
print(co2.head()) """
""" print(df.head())
plt(df['Time'], df['CO2'])
plt.show() """