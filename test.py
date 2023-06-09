import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('/Users/noor/Bot4BACS/F3_B8_07_6C_28_8E.csv')    #Window
df2 = pd.read_csv('/Users/noor/Bot4BACS/C3_23_CF_79_6C_FB.csv')    #Coffee Desk
df3 = pd.read_csv('/Users/noor/Bot4BACS/DD_3F_BC_9B_56_EC.csv')    #Meeting Table
df4 = pd.read_csv('/Users/noor/Bot4BACS/E9_FC_42_4B_FB_7C.csv')    #Robot
df5 = pd.read_csv('/Users/noor/Bot4BACS/FE_ED_E9_B2_20_8E.csv')    #Not in Flight Arena -> Secret

helpertime=[]
helperparam=[]
sheetnames = [df1,df2,df3,df4,df5]
time=pd.DataFrame()
param=pd.DataFrame()    #to be plotted parameter, e.g. co2, temp, humidity..

for i in range(5):
    df = sheetnames[i]
    helpertime = pd.to_datetime(df["Time"])
    helperparam = df["rssi"]
    #time+str(i) = helpertime
    time[i] = helpertime
    param[i] = helperparam
    #print(time)
    
#for i in range(5):
plt.title('RSSI Measurements on 08.06.2023')
#plt.title('Temperature Photo Comparison')
plt.plot(time ,param, 'o',label=["Window","Coffee","Meeting","Robot","Hidden"])
#plt.plot(pd.to_datetime(df3['Time']),df3['Temperature'], label="Temp")
#plt.plot(pd.to_datetime(df3['Time']),df3['Photo']/100, label="Photo")
plt.legend()
plt.xlabel('Time')
plt.ylabel('Received Signal Strength')
plt.xticks(rotation= 30, ha='right')
plt.show()
print(time)
print(param)
#print(df3['Photo'])
""" def plot(): 

 """