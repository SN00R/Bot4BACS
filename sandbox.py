import pandas as pd
import numpy as np
from datetime import datetime
import time

df_truth = pd.read_csv("/Users/noor/Bot4BACS/Testo_Cal/2023-09-20-10-35-05.csv")
#df_truth = pd.read_csv("/Users/noor/Bot4BACS/Testo_Cal/2023-09-19-16-01-44.csv")
df_sensoren = pd.read_csv("/Users/noor/Bot4BACS/Sensoring/serial_test_backup.csv")

#df_truth = df_truth.drop(["713 [m/s]","274 Dew point [°C]", "274 Wet bulb temperature [°C]", "274 [g/m³]", "713 [hPa]"], axis=1)
df_truth = df_truth.drop(["714 [m/s]","018 Dew point [°C]", "018 Wet bulb temperature [°C]", "018 [g/m³]", "714 [hPa]"], axis=1)
df_truth.pop(df_truth.columns[-1])
#df_truth = df_truth[df_truth["Date/Time"] <= "07/09/2023 16:47:47"]
df_truth["Date/Time"] = pd.to_datetime(df_truth["Date/Time"], format = '%d/%m/%Y %H:%M:%S')
df_truth = df_truth.rename(columns={"Date/Time": "Time"})
df_sensoren["Time"] = pd.to_datetime(df_sensoren["Time"], format = '%Y-%m-%d %H:%M:%S')
timecol = []

""" for i in range(len(df_sensoren["Time"])):
    if  (df_sensoren[df_sensoren["Time"]] == df_truth[df_truth["Date/Time"]]):
        timecol[i] = df_sensoren["Time"]
    else:
        timecol[i] = "NaN" """
 
#timecol = df_truth[df_truth["Date/Time"] == df_sensoren[df_sensoren["Time"]]]

df = df_truth.merge(df_sensoren, on='Time', how='outer')
df = df.fillna(method='ffill')
df = df.dropna()
df = df.reset_index(drop=True)


df['Diff_TempIR'] = df['018 [°C]'] - df['Amb']
df['Diff_TempSCD'] = df['018 [°C]'] - df['Temp']
df['Diff_Humidity'] = df['018 [%RH]'] - df['Humid']
df['Diff_CO2'] = df['018 [ppm]'] - df['CO2']
df = df.round(4)
print(df)
df.to_csv("/Users/noor/Bot4BACS/Testo_Cal/Morning_data.csv", index=False)
