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

timecol = pd.to_datetime(dfa["Time"], format = '%Y-%m-%d %H:%M:%S') 

fig, (ax1,ax2) = plt.subplots(1,2, figsize=(12,6))
#fig, ax1 = plt.subplots()
fig.suptitle('Morning Data Distribution in Measurement Difference: Temperature')
#fig.tight_layout()
data1 = dfm['Diff_TempIR']
ax1.set_title('Testo400 - MLX90614')
ax1.set_ylabel('Samples')
ax1.set_xlabel('Difference in °C')
height, bins, patches = ax1.hist(data1, color = '#0065bd', edgecolor = 'black', bins = 'fd')
#ax1.set(yticks=range(0,1101,100))
#ticks = [(patch.get_x() + (patch.get_x() + patch.get_width()))/2 for patch in patches] ## or ticklabels
ax1.grid(alpha=0.4, axis='y')

mean_val = data1.mean()
median1 = np.median(data1)          # Median: 50% der Daten über oder drunter
sigma1 = data1.std()                # Standardverteilung
textstr1 = '\n'.join((
    r'$\mu=%.2f$' % (mean_val, ),
    r'$\mathrm{median}=%.2f$' % (median1, ),
    r'$\sigma=%.2f$' % (sigma1, )))
# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords
ax1.text(0.6, 0.95, textstr1, transform=ax1.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

data2 = dfm['Diff_TempSCD']
ax2.set_title('Testo 400 – SCD30')
ax2.set_ylabel('Samples')
ax2.set_xlabel('Difference in °C')
height, bins, patches = ax2.hist(data2, color = '#0065bd', edgecolor = 'black', bins ='fd')
ax2.grid(alpha=0.4, axis='y')
#ax2.set(yticks=range(0,1101,100))
ticks = [(patch.get_x() + (patch.get_x() + patch.get_width()))/2 for patch in patches] ## or ticklabels
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

plt.show()
print('Mean Difference Testo - SCD: ', mean_val)
print('Mean Difference Testo - SCD: ', mean_val2)
fig.savefig('/Users/noor/Bot4BACS/Sensor_Figures/Temp_hist_morning.pdf',bbox_inches='tight', dpi=200) 
