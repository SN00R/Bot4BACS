import serial
import time
import serial.tools.list_ports
import time
import pandas as pd
import numpy as np
from datetime import datetime
import csv 

t = time.localtime()
start_time = time.strftime("%H:%M:%S", t)
print("Current Time: ", start_time)
count_time = time.time()
#print("Start counting Time: ", count_time)

""" # Find the USB port we are on
commports = serial.tools.list_ports.comports() # get possible port
numPorts = len(commports)
if (numPorts == 0):
    print("No serial ports available\n\n")
    exit()
if (numPorts>1):
    # Have user pick one
    portNum = 0
    for port in commports:
        print("port number ",portNum)
        print(port)
        portNum = portNum+1
    usePort = int(input('enter port number to use 0-'+str(numPorts-1)+':'))
else:
    usePort = 0

thePort = commports[usePort][0]
print(thePort)
ser = serial.Serial(port=str(thePort),baudrate=9600, timeout=1) """

ser=serial.Serial("/dev/ttyACM6",9600)
ser.baudrate=9600
ser1=serial.Serial("/dev/ttyACM",9600)
ser1.baudrate=9600
ser.close()
ser.open()
ser1.close()
ser1.open()
time.sleep(2) 

rawdata=[]
count=0
df = []
sample = []
try:
    while ser.isOpen() & ser1.isOpen():
        stamp = datetime.now()
        stamp = stamp.strftime("%Y-%m-%d %H:%M:%S")
        print("datetime: ", stamp)
        input_data = ser.readline().strip().decode("utf-8")
        print("input: ", input_data)
        input_data1 = ser.readline().strip().decode("utf-8")
        print("input: ", input_data)
        floatdata = list(map(float, input_data.split(',')))
        rounddata = list(np.around(np.array(floatdata),2))
        print('round data: ', rounddata)
        rounddata.insert(0, stamp)
        rawdata.append(rounddata)
        """         with open('/Users/noor/Bot4BACS/Sensoring/serial_test_cal.csv', 'a', newline='') as csvfile:
                    headerwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='', quoting=csv.QUOTE_NONE)
                    headerwriter.writerow(rounddata) """
        time.sleep(2)


        #print("input_data length: ", len(input_data))
        #print("rawdata length: ", len(rawdata))
        #if len(rawdata) == 16:
        #   sample = pd.array(rawdata)
        #print(sample)

        timecheck = datetime.now()
        print("Timecheck: ", timecheck.strftime("%Y-%m-%d %H:%M:%S"))
        if len(rawdata) > 6000:
            break
except KeyboardInterrupt:
    print("----- INTERRUPTED -----")



df = pd.DataFrame(rawdata, columns=['Time', 'Amb','Obj', 'Temp', 'Humid', 'CO2', 'LightFront', 'LightTop'])

print("collected data", rawdata)
#df['Time'] = pd.to_datetime(df.loc[:,'Time'])

print("Collected Data: ", rawdata)
#print("DF: ", df)

#df.to_csv("/Users/noor/Bot4BACS/Sensoring/serial_finalsetup_test.csv", index=False)
