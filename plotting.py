import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('/Users/noor/Bot4BACS/cal2/F3_B8_07_6C_28_8E.csv')    #Window
df2 = pd.read_csv('/Users/noor/Bot4BACS/cal2/C3_23_CF_79_6C_FB.csv')    #Coffee Desk
df3 = pd.read_csv('/Users/noor/Bot4BACS/cal2/DD_3F_BC_9B_56_EC.csv')    #Meeting Table
df4 = pd.read_csv('/Users/noor/Bot4BACS/cal2/E9_FC_42_4B_FB_7C.csv')    #Robot
#df5 = pd.read_csv('/Users/noor/Bot4BACS/cal1/FE_ED_E9_B2_20_8E.csv')    #Not in Flight Arena -> Secret

helpertime=[]
helperparam=[]
df_param=pd.DataFrame()
sheetnames = [df1,df2,df3,df4]
time=pd.DataFrame()
param=pd.DataFrame()    #to be plotted parameter, e.g. co2, temp, humidity..
values=["CO2","Temperature","Humidity","Pressure","Photo"]

for x in values:
    for i in range(4):
        df = sheetnames[i]
        time[i] = pd.to_datetime(df["Time"])
        #helperparam = df["CO2"]
        helperparam = df[x]
        param[i] = helperparam
        print(x)
    plt.title(str(x)+' Measurements on 21.06.2023 for calibration')
    if x == "CO2":
        plt.ylabel('CO2 in ppm')
        plt.plot(time,param,label=["Window","Coffee","Meeting","Robot"])
    elif x == "Temperature":
        plt.ylabel('Temperature in °C')
        plt.plot(time,param/100,label=["Window","Coffee","Meeting","Robot"])
    elif x == "Humidity":
        plt.ylabel('Humidity in %RC')
        plt.plot(time,param/100,label=["Window","Coffee","Meeting","Robot"])
    elif x == "Pressure":
        plt.ylabel('Pressure in Pa')
        plt.plot(time,param/100,label=["Window","Coffee","Meeting","Robot"])
    elif x == "Photo":
        plt.ylabel('ADC')
        plt.plot(time,param,label=["Window","Coffee","Meeting","Robot"])
    plt.legend()    
    plt.xlabel('Time')
    #plt.xticks(rotation= 30, ha='right')
    plt.grid(alpha=0.25)
    plt.savefig('/Users/noor/Bot4BACS/cal2/'+str(x)+'.png',bbox_inches='tight', dpi=200)
    plt.show()

