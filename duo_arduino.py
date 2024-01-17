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

# Adafruit Metro M0 Express on Gripper
ser=serial.Serial("/dev/ttyACM6",9600)
ser.baudrate=9600
# Arduino Nano Every on Head
ser1=serial.Serial("/dev/ttyACM2",9600)
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
constr_brightness =[]
try:
    while ser.isOpen() & ser1.isOpen():
        stamp = datetime.now()
        stamp = stamp.strftime("%Y-%m-%d %H:%M:%S")
        print("datetime: ", stamp)
        input_data = ser.readline().strip().decode("utf-8")
        print("input: ", input_data)
        input_data1 = ser1.readline().strip().decode("utf-8")
        print("input1: ", input_data1)
        floatdata = list(map(float, input_data.split(',')))
        rounddata = list(np.around(np.array(floatdata),2))
        #print('round data: ', rounddata)
        floatdata1 = list(map(float, input_data1.split(',')))
        rounddata1 = list(np.around(np.array(floatdata1),2))
        #print('round data1: ', rounddata1)
        rounddata.insert(0, stamp)
        #combined = np.concatenate(rounddata,rounddata1)
        rawdata.append(rounddata + rounddata1)
        if rounddata1[0] <=50.0 and rounddata1[1] <=50.0:
            print("--------- Room too dark! Switch on the Light! --------- ")
            constr_brightness.append(rounddata1)
        if rounddata1[0] >=2000.0 and rounddata1[1] >=2000.0:
            print("--------- Room too bright! Switch off the Light! --------- ")
            constr_brightness.append(rounddata1)
        if rounddata[4] >= 1100.0:
            print("--------- Room has bad Air Quality! Open the Window! --------- ")

        #print(rawdata)
        with open('/home/hello-robot/Bot4BACS/Sensoring/VisionWood_2211.csv', 'a', newline='') as csvfile:
                    headerwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='', quoting=csv.QUOTE_NONE)
                    headerwriter.writerow(rounddata+rounddata1)

        time.sleep(2)


        #print("input_data length: ", len(input_data))
        #print("rawdata length: ", len(rawdata))
        #if len(rawdata) == 16:
        #   sample = pd.array(rawdata)
        #print(sample)

        #timecheck = datetime.now()
        #print("Timecheck: ", timecheck.strftime("%Y-%m-%d %H:%M:%S"))
        if len(rawdata) > 3650:
            break
except KeyboardInterrupt:
    print("----- INTERRUPTED -----")


df = pd.DataFrame(rawdata, columns=['Time', 'Amb','Obj', 'Temp', 'Humid', 'CO2', 'Elapsed', 'LightTop', 'LightFront'])
print("collected data", rawdata)
df['Time'] = pd.to_datetime(df.loc[:,'Time'])
print("Constraints Violations: ", constr_brightness)
#print("DF: ", df)

df.to_csv("/home/hello-robot/Bot4BACS/Sensoring/VisionWood_Backup.csv", index=False)
