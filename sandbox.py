import pandas as pd
import numpy as np
from datetime import datetime
import time

df_truth = pd.read_csv("/Users/noor/Bot4BACS/Testo_Cal/2023-09-07-16-48-42.csv")
df_sensoren = pd.read_csv("/Users/noor/Bot4BACS/Testo_Cal/serial_test_cal.csv")

df_truth = df_truth.drop(["713 [m/s]","274 Dew point [°C]", "274 Wet bulb temperature [°C]", "274 [g/m³]", "713 [hPa]"], axis=1)
df_truth.pop(df_truth.columns[-1])
df_truth = df_truth[df_truth["Date/Time"] <= "07/09/2023 16:47:47"]
df_truth["Date/Time"] = pd.to_datetime(df_truth["Date/Time"], format = '%d/%m/%Y %H:%M:%S')
df_sensoren["Time"] = pd.to_datetime(df_sensoren["Time"], format = '%Y-%m-%d %H:%M:%S')
timecol = []

for i in range(len(df_sensoren["Time"])):
    if  (df_sensoren[df_sensoren["Time"]] == df_truth[df_truth["Date/Time"]]):
        timecol[i] = df_sensoren["Time"]
    else:
        timecol[i] = "NaN"
 
#timecol = df_truth[df_truth["Date/Time"] == df_sensoren[df_sensoren["Time"]]]
print(timecol)

print(type(df_truth["Date/Time"]))
print(df_truth["Date/Time"])
print(df_sensoren["Time"])
#print(df_truth)