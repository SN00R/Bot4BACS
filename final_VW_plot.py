# Script used for plotting 

#!/usr/local/bin/local/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import cv2 as cv

def percentage_change(col1,col2):
    return ((col2 - col1) / col1) * 100

dfm = pd.read_csv("/Users/noor/Bot4BACS/Sensoring/VisionWood_Backup.csv")
dfm = dfm[dfm['LightFront']<100]
dfm = dfm[dfm['LightTop']<750]

print(dfm)
dfa = pd.read_csv("/Users/noor/Bot4BACS/Testo_Cal/Afternoon_data_new.csv")
#print(dfa)

#xaxis = ['SCD30', 'Testo', 'IR']

timecol = pd.to_datetime(dfm["Time"], format = '%Y-%m-%d %H:%M:%S') 

fig, (ax1,ax2) = plt.subplots(1,2, figsize=(12,6))
#fig, ax1 = plt.subplots()
fig.suptitle('Brightness Data of Sensing Routine in Vision Wood')
#fig.tight_layout()
data1 = dfm['LightFront']
ax1.set_title('Front Sensor; B1')
ax1.set_ylabel(r'Brightness in lux')
ax1.set_xlabel('Time')
ax1.set(rotation= 30, ha='right')
#height, bins, patches = ax1.hist(data1, color = '#0065bd', edgecolor = 'black', bins = 'fd')
ax1.plot(timecol, data1,  color = '#0065bd')
#ax1.set(yticks=range(0,1101,100))
#ticks = [(patch.get_x() + (patch.get_x() + patch.get_width()))/2 for patch in patches] ## or ticklabels
ax1.grid(alpha=0.4, axis='y')
#ticklabels = (bins[1:] + bins[:-1]) / 2 ## or ticks
#ax1.set_xticks(ticks, np.round(ticklabels, 2))


data2 = dfm['LightTop']
ax2.set_title('Top Sensor; B2')
ax2.set_ylabel('Brightness in lux')
ax2.set_xlabel('Time')
ax2.set(rotation= 30, ha='right')
#height, bins, patches = ax2.hist(data2, color = '#0065bd', edgecolor = 'black', bins ='fd')
ax2.plot(timecol, data2, color = '#0065bd')
ax2.grid(alpha=0.4, axis='y')
#ax2.set(yticks=range(0,1101,100))
""" ticks = [(patch.get_x() + (patch.get_x() + patch.get_width()))/2 for patch in patches] ## or ticklabels
ticklabels = (bins[1:] + bins[:-1]) / 2 ## or ticks
#ax2.set_xticks(ticks, np.round(ticklabels, 2))
mean_val2 = data2.mean()
median2 = np.median(data2)          # Median: 50% der Daten über oder drunter
sigma2 = data2.std()                # Standardverteilung
textstr2 = '\n'.join((
    r'$\mu=%.2f$' % (mean_val2, ),
    r'$\mathrm{median}=%.2f$' % (median2, ),
    r'$\sigma=%.2f$' % (sigma2, )))

# place a text box in upper left in axes coords
ax2.text(0.55, 0.95, textstr2, transform=ax2.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
 """
plt.show()
fig.savefig('/Users/noor/Bot4BACS/Sensor_Figures/VW_Final_Brightness.png',bbox_inches='tight', dpi=200) 
""" print('Mean Difference Testo - SCD: ', mean_val)
print('Mean Difference Testo - SCD: ', mean_val2) """


""" 
fig, ax = plt.subplots()
ax.set_title('Afternoon Data: Difference in Measurements: Temperature')
ax.plot(timecol, abs(data1), label='Testo400 – MLX90614', color='#0065bd')
ax.plot(timecol, abs(data2), label='Testo400 – SCD30', colsor='plum')
ax.set_xlabel(r'Time')
ax.set_ylabel(r'Abs. Temperature Difference in °C')
ax.grid(alpha=0.4)
ax.legend()
plt.show()

fig.savefig('/Users/noor/Bot4BACS/Sensor_Figures/Temp_afternoon.pdf',bbox_inches='tight', dpi=200) """

""" #Mouse callback function
def draw_shape(event,x,y,flags,param):
    ("event : ",event)
    if event == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),100,(255,0,0),-1)

#Create a black image, a window and bind the function to the window
img = np.zeros((780,780,3),np.uint8)
cv.namedWindow('DrawWithMouse')
cv.setMouseCallback('DrawWithMouse',draw_shape)

while(1):
    cv.imshow('DrawWithMouse',img)
    if cv.waitKey(10) & 0xFF == 27: #ANDing with 0xFF as my machine is 64 bit
        break

cv.destroyWindow('DrawWithMouse') """


"""
convdata = list(map(float, input_data.split(',')))
rounded = list(np.around(np.array(convdata),2))
 """

""" 
def percentage_change(col1,col2):
    return ((col2 - col1) / col1) * 100

df = pd.read_csv("/Users/noor/Bot4BACS/Sensoring/serial_testreal.csv")
df_selected = df.loc[1:,['Time','Amb','Temp']]
df_selected = df_selected.dropna()

plt.title("Compare IR Ambient and SCD30 Ambient Temperature")
plt.xlabel("Time")
time = df_selected["Time"]
time = pd.to_datetime(time)
ir = df_selected["Amb"]
scd = df_selected["Temp"]
df_selected["Difference"] = scd-ir
print("smallest difference: ", "%.3f" % df_selected["Difference"].min())
print("highest difference: ", "%.3f" % df_selected["Difference"].max())
mean_diff = df_selected["Difference"].mean()
print("Mean Difference: ", "%.3f" % mean_diff)
df_selected["Percentage"] = percentage_change(ir,scd)
mean_diff_perc = df_selected["Percentage"].mean()
print("Percentage of Mean Difference: ", "%.3f" % mean_diff_perc)
plt.ylabel("Temperature in °C")
plt.plot(time,ir,label='IR') 
plt.plot(time,scd,label='SCD30')
plt.xticks(rotation= 30, ha='right')
plt.grid(alpha=0.25)
plt.legend()
#plt.show()
print(df_selected.head())

 """


#print("Collected Data: ", rawdata)

#print("DF: ", df)

#df.to_csv("/Users/noor/Bot4BACS/Sensoring/serial_test.csv", index=False)

#dff = pd.read_csv("/Users/noor/Bot4BACS/Sensoring/serial_test.csv")
#print(dff)



#ax2 = ax.twiny()
#for patch, color in zip(bp['boxes'], colors):
    #patch.set_facecolor(color)

#ax.plot(timecol, dfm['Diff_TempIR'], label='Testo – IR')
#ax.plot(dfm['Time'], dfm['Diff_TempSCD'], label='Testo – SCD')

#ax2.plot(time_truth,testo, 'o', label="Testo", color='green')
#ax2.set_xlabel(r"Time")

#ax.plot(time_truth, testo, label='Testo')
#ax.legend()
#plt.plot(time,testo,label='Testo')
#plt.xticks(rotation= 30, ha='right')
#bp = ax.boxplot(data, labels=xaxis, patch_artist=True)
#colors = ['pink', 'lightblue', 'thistle','lightgreen', 'plum']