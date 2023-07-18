import serial
import time
import serial.tools.list_ports
import time

t = time.localtime()
start_time = time.strftime("%H:%M:%S", t)
print("Current Time: ", start_time)

count_time = time.time()
print("Start counting Time: ", count_time)

rawdata=[]
count=0

#
# Find the USB port we are on
#
commports = serial.tools.list_ports.comports() # get possible ports
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

ser = serial.Serial(port=str(thePort),baudrate=9800, timeout=1)
ser.close()
ser.open()
time.sleep(2)

while ser.isOpen():
    input_data=ser.readline().strip().decode("utf-8")
    rawdata.append(input_data)
    print(input_data)
    if len(rawdata) > 5:
        break



print("collected data", rawdata)
#print(rawdata) """
""" 
try:
    while True:
        time.sleep(1)
        print('processing...')  
        if time.time() - count_time > 3000:
            print("Process stopped after: ", (time.time() - count_time)/60, "mins")
            t = time.localtime()
            end_time = time.strftime("%H:%M:%S", t)
            print("Current Time: ", end_time)
            print("exiting...")
            print('------ BREAK ------ exiting after time limit...')
            break

except KeyboardInterrupt:
    t = time.localtime()
    end_time = time.strftime("%H:%M:%S", t)
    print("Current Time: ", end_time)
    print('------ BREAK ------ exiting after interrupt...')  """