# Plotting the Empair Data to compare the sensored value differences 

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import numpy as np
from math import sqrt

df1 = pd.read_csv('/Users/noor/Bot4BACS/cal3/F3_B8_07_6C_28_8E.csv')    #Window
df2 = pd.read_csv('/Users/noor/Bot4BACS/cal3/C3_23_CF_79_6C_FB.csv')    #Coffee Desk
df3 = pd.read_csv('/Users/noor/Bot4BACS/cal3/DD_3F_BC_9B_56_EC.csv')    #Meeting Table
df4 = pd.read_csv('/Users/noor/Bot4BACS/cal3/E9_FC_42_4B_FB_7C.csv')    #Robot
df5 = pd.read_csv('/Users/noor/Bot4BACS/cal3/FE_ED_E9_B2_20_8E.csv')    #Not in Flight Arena -> Hidden

helperparam=[]
df_param=pd.DataFrame()
sheetnames = [df1,df2,df3,df4,df5]
time=pd.DataFrame()
param=pd.DataFrame()    #to be plotted parameter, e.g. co2, temp, humidity..
values=["CO2","Temperature","Humidity","Pressure","Photo"]

for x in values:
    for i in range(len(sheetnames)):
        df = sheetnames[i]
        time[i] = pd.to_datetime(df["Time"])
        #helperparam = df["CO2"]
        helperparam = df[x]
        param[i] = helperparam
    param = param.dropna()
    time = time.dropna()
    time[5] = time.mean(axis=1)
    param[5] = param.iloc[:,0:5].mean(axis=1)           # Add mean column
    param[5] = round(param[5],1)   
    # Root Mean Square Error
    #mse_1 = mean_squared_error(param[5])
    #rmse1 = sqrt(mse_1) 
    plt.title(str(x)+' Measurements on 22.06.2023 for calibration')
    if x == "CO2":
        plt.ylabel('CO2 in ppm')
        plt.plot(time,param,label=["F3","C3","DD","E9","FE","Mean"])
    elif x == "Temperature":
        plt.ylabel('Temperature in °C')
        plt.plot(time,param/100,label=["F3","C3","DD","E9","FE","Mean"])
    elif x == "Humidity":
        plt.ylabel('Humidity in %RC')
        plt.plot(time,param/100,label=["F3","C3","DD","E9","FE","Mean"])
    elif x == "Pressure":
        plt.ylabel('Pressure in Pa')
        plt.plot(time,param/100,label=["F3","C3","DD","E9","FE","Mean"])
    elif x == "Photo":
        plt.ylabel('ADC')
        plt.plot(time,param,label=["F3","C3","DD","E9","FE","Mean"])
    plt.legend()    
    plt.xlabel('Time')
    #plt.xticks(rotation= 30, ha='right')
    plt.grid(alpha=0.25)
    plt.savefig('/Users/noor/Bot4BACS/cal3/'+str(x)+'.png',bbox_inches='tight', dpi=200)
    plt.show()

