import pandas as pd
df1 = pd.read_csv('/home/hello-robot/Bot4BACS/F3_B8_07_6C_28_8E.csv')    #Window
df2 = pd.read_csv('/home/hello-robot/Bot4BACS/C3_23_CF_79_6C_FB.csv')    #Coffee Desk
df3 = pd.read_csv('/home/hello-robot/Bot4BACS/DD_3F_BC_9B_56_EC.csv')    #Meeting Table
df4 = pd.read_csv('/home/hello-robot/Bot4BACS/E9_FC_42_4B_FB_7C.csv')    #Robot
df5 = pd.read_csv('/home/hello-robot/Bot4BACS/FE_ED_E9_B2_20_8E.csv')    #Not in Flight Arena -> Secret

helpertime=[]
sheetnames = [df1,df2,df3,df4,df5]
time=[]
for i in range(5):
    df = sheetnames[i]
    helpertime = pd.to_datetime(df["Time"])
    #time+str(i) = helpertime
    time[i].append(helpertime)
    print(time)

print(time)
