#!/usr/local/bin/local/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import cv2 as cv

def percentage_change(col1,col2):
    return ((col2 - col1) / col1) * 100

dfm = pd.read_csv("/Users/noor/Bot4BACS/Testo_Cal/Morning_data_new.csv")
dfa = pd.read_csv("/Users/noor/Bot4BACS/Testo_Cal/Afternoon_data_new.csv")
print(dfa)

#xaxis = ['SCD30', 'Testo', 'IR']

#print("Mean Difference Truth - IR: ", "%.3f" % testo.mean()-ir.mean())
#print("Mean Difference Truth - SCD: ", "%.3f" % testo.mean()-scd.mean())
#print("Mean Difference Truth - emp1: ", "%.3f" % testo.mean()-emp1.mean())
#print("Mean Difference Truth - emp2: ", "%.3f" % testo.mean()-emp2.mean())

#df_sensoren["Percentage"] = percentage_change(ir,scd)
#df_sensoren["Testo_SCD"] = scd - testo
#df_sensoren["Testo_IR"] = ir - testo


#mean_diff_perc = df_sensoren["Percentage"].mean()
#print("mean_diff: ", "%.3f" % mean_diff_perc)print(df_sensoren) 
mean_val = dfa['Diff_TempIR'].mean()
mean_val2 = dfm['Diff_TempSCD'].mean()
print('Mean Difference Testo - SCD: ', mean_val)
print('Mean Difference Testo - SCD: ', mean_val2)
#mean_ajeeb = dfm['018 [°C]'].mean() - dfm['Amb'].mean()
#print('IR Temp Mean for checking', mean_ajeeb)

timecol = pd.to_datetime(dfa["Time"], format = '%Y-%m-%d %H:%M:%S') 

fig, (ax1,ax2) = plt.subplots(1,2, figsize=(12,6))
#fig, ax1 = plt.subplots()
fig.suptitle('Afternoon Data Distribution in Measurement Difference: Temperature')
#fig.tight_layout()
data1 = dfa['Diff_TempIR']
ax1.set_title('Testo400 - MLX90614')
ax1.set_ylabel('Samples')
ax1.set_xlabel('Difference in °C')
height, bins, patches = ax1.hist(data1, color = '#0065bd', edgecolor = 'black', bins = 8)
ax1.set(yticks=range(0,1101,100))
ticks = [(patch.get_x() + (patch.get_x() + patch.get_width()))/2 for patch in patches] ## or ticklabels
ax1.grid(alpha=0.4, axis='y')
ticklabels = (bins[1:] + bins[:-1]) / 2 ## or ticks
ax1.set_xticks(ticks, np.round(ticklabels, 2))
median1 = np.median(data1)          # Median: 50% der Daten über oder drunter
sigma1 = data1.std()                # Standardverteilung
textstr1 = '\n'.join((
    r'$\mu=%.2f$' % (mean_val, ),
    r'$\mathrm{median}=%.2f$' % (median1, ),
    r'$\sigma=%.2f$' % (sigma1, )))
# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords
ax1.text(0.05, 0.95, textstr1, transform=ax1.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

data2 = dfa['Diff_TempSCD']
ax2.set_title('Testo 400 – SCD30')
ax2.set_ylabel('Samples')
ax2.set_xlabel('Difference in °C')
height, bins, patches = ax2.hist(dfm['Diff_TempSCD'], color = '#0065bd', edgecolor = 'black', bins = 8)
ax2.grid(alpha=0.4, axis='y')
ax2.set(yticks=range(0,1101,100))
ticks = [(patch.get_x() + (patch.get_x() + patch.get_width()))/2 for patch in patches] ## or ticklabels
ticklabels = (bins[1:] + bins[:-1]) / 2 ## or ticks
ax2.set_xticks(ticks, np.round(ticklabels, 2))
median2 = np.median(data2)          # Median: 50% der Daten über oder drunter
sigma2 = data2.std()                # Standardverteilung
textstr2 = '\n'.join((
    r'$\mu=%.2f$' % (mean_val2, ),
    r'$\mathrm{median}=%.2f$' % (median2, ),
    r'$\sigma=%.2f$' % (sigma2, )))

# place a text box in upper left in axes coords
ax2.text(0.55, 0.95, textstr2, transform=ax2.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

#plt.show()
fig.savefig('/Users/noor/Bot4BACS/Sensor_Figures/Temp_hist_afternoon.pdf',bbox_inches='tight', dpi=200) 

fig, ax = plt.subplots()
ax.set_title('Afternoon Data: Difference in Measurements: Temperature')
ax.plot(timecol, abs(data1), label='Testo400 – MLX90614', color='#0065bd')
ax.plot(timecol, abs(data2), label='Testo400 – SCD30', color='plum')
ax.set_xlabel(r'Time')
ax.set_ylabel(r'Abs. Temperature Difference in °C')
ax.grid(alpha=0.4)
ax.legend()
plt.show()

fig.savefig('/Users/noor/Bot4BACS/Sensor_Figures/Temp_afternoon.pdf',bbox_inches='tight', dpi=200)

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

 #convdata = list(input_data.split(','))
#bro.replace("],", "];")
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