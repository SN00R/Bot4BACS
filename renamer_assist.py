import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
import os
import re

destdirname = "/Users/noor/Bot4BACS/ObjectDetection/Img_renamed/"
dirname = "/Users/noor/Bot4BACS/ObjectDetection/Img_selected/"
imglist = os.listdir(dirname)
newimglist = []
newstringlist = []
#print(len(imglist))
counter = 1
counter1 = 1

#print(sorted(imglist))
""" for img in imglist:
    #imgpath = os.path.join(dirname,img) 
    imgpath = dirname + img 
    #print(imgpath)
    filename = "Img_" + str(imnum) + '.jpg'
    #savepath = os.path.join(dirname, filename)
    savepath = destdirname + filename
    os.rename(imgpath,savepath)
    imnum = imnum + 1 """

def getSum(n): 
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum

for img in imglist:
    split = img.replace('.', '_').split('_')
    print("split: ", split)
    number = int(split[1])
    #print(number)
    #newimglist.append(number)
    if number < 10:
        newnumber = "00" + str(number)
    elif number >= 10 and number <= 99:
        newnumber = "0" + str(number)
    elif number >= 100:
        newnumber = str(number)
    print(newnumber)
    newstringlist.append(newnumber)
    imgpath = dirname + img
    for i in newstringlist:
        filename = "Img_" + i + '.jpg'
        if getSum(i) == getSum(newnumber) and filename not in os.listdir(destdirname):
            print(i)
            savepath = destdirname + filename
            os.rename(imgpath,savepath)

print("All done!")


#sortedlist =   imglist.sort(key=lambda x: int(x.strip('Img_')))
""" split = imglist[0].replace('.', '_').split('_')
number = int(split[1])


print(number)
counter = 1 """

""" for img in imglist:
    split = img.replace('.', '_').split('_')
    print("split: ", split)
    number = int(split[1])
    print(number)
    newimglist.append(number)

sortedlist = sorted(newimglist)
print("unsorted list: ", newimglist)
print("sorted list: ", sortedlist)
 """

""" print(type(counter))
if type(counter) != int:
    print(counter,"ajeeb")
else:
    print("tired") """
damaged = []
#print(imglist.index("Img_307.jpg"))
#print(type(imglist[36]))
""" for img in imglist:
    print("counter = ", counter)
    print(img)
    #print("counter = ", counter)
    if type(img) is None:
        print(img, " is damaged!")
        damaged.append(img)
        break
    elif type(img) is not None:
        number = re.search('Img_(.*).jpg', img)
        print(number)
        #print(type(number))
        gnumber = int(number.group(1))
        print(type(gnumber))
        print(gnumber)

        newimglist.append(gnumber)
        counter = counter + 1

print("unsorted list: ", newimglist)
print("sorted list: ", sorted(newimglist)) """

#print(type(number))

""" img = "Img_242.jpg"
if img not in imglist:
    print(img, " not in directory")
elif img in imglist:
    print(img, " is in directory") """

#x = range(0,100,1)
#print(len(x))
#result = 3%3
#print("Modulo: ", result)
""" 
for i in range(1,11):
    print(i)
    for x in range(3,16,2):
        print(x)
        if x == i:
            print(str(x)+ " = "+ str(i))
            break """

""" terms=[]

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
 """

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