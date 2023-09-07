import asyncio
from bleak import BleakScanner
from bleak import AdvertisementData
from datetime import datetime
import logging
import threading
import os
import csv
import time
import array
import statistics
import platform

start_time = time.time()
print("Start Time: ", start_time)

async def runBleScan():
    global dict_devices
    global default_list_mac_past_rssi
    global lenOfRssiFilter
    global strongestSignal

    devices = await BleakScanner.discover(timeout=5.0) # could use AdvertisementFilter, BluetoothLEAdvertisementFilter.BytePatterns Property
    print(devices)
    print('#devices: ', len(devices))
    dataList = []
    macList = []
    rssiList = []
    for d in devices:
        d.details
        if d.metadata.keys().__contains__('manufacturer_data'): #has manufacturer data      #need to change
            manData = d.metadata.get('manufacturer_data')
            if  str(manData.keys()) == 'dict_keys([65535])': #has manufacturerID 0xFF        #need to change
                manDataStr = manData.get(65535)
                #print(manDataStr)
                """
                if manDataStr[0] == 2 and manDataStr[1] == 236:
                    print('Has Empa ID with AND operator')
                elif manDataStr[0] == 2 or manDataStr[1] == 236:
                    print('Has Empa ID with OR operator') """
                if manDataStr[0] == 2  and manDataStr[1] == 236: #has Empa CO2 ID "0xEC02"        # change AND to OR operator, since manDataStr[0] jumps around 2 and 3, even though it shouldnt
                    #add to list
                    dataList.append(manDataStr)
                    macList.append(d.address)
                    rssiList.append(d.rssi)
    if len(dataList) > 0:
        for count, sensor in enumerate(dataList):
            #check if file exists
            fileName = (macList[count]+".csv").replace(":",'_')
            try:
                f = open(fileName, 'r', newline='')
                f.close()
            except:
            #create new file
                with open(fileName, 'w', newline='') as csvfile:
                    headerwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='', quoting=csv.QUOTE_NONE)
                    headerwriter.writerow(['Time'] + ['Status'] + ['CO2'] + ['Temperature'] + ['Humidity'] + ['Pressure'] + ['Photo'] + ['Battery'] + ['HWVersion'] + ['SWVersion']+ ['rssi'])
            #append
            try:
                now = datetime.now()
                stat = sensor[2]
                co2 = sensor[4]*256 + sensor[3]
                temp = (sensor[6]*256 + sensor[5])
                humi = (sensor[8]*256 + sensor[7])
                press = (sensor[11]*256*256 + sensor[10]*256 + sensor[9])
                photo = (sensor[13]*256 + sensor[12])
                batt = (sensor[15]*256 + sensor[14])
                swVers = sensor[16] & 7
                hwVers = sensor[16] >> 4
                if macList[count] not in dict_devices:
                    dict_devices[macList[count]] = default_list_mac_past_rssi[:]
                    for i in range(lenOfRssiFilter):
                        dict_devices[macList[count]][3+i]= rssiList[count]
                    #dict_devices[macList[count]][3:3+lenOfRssiFilter] = rssiList[count]
                    dict_devices[macList[count]][1] = (sensor[2] & 15) - 1

                if (sensor[2] & 15) != dict_devices[macList[count]][1]:
                    dict_devices[macList[count]][1] = (sensor[2] & 15)
                    with open(fileName, 'a+', newline='') as csvfile:
                        datawriter = csv.writer(csvfile, delimiter=',',
                                                quotechar='', quoting=csv.QUOTE_NONE)
                        datawriter.writerow([now] + [stat] + [co2] + [temp] + [humi] + [press] + [photo] + [batt] + [hwVers] + [swVers] + [rssiList[count]])
                    print("saved value to " + fileName + " at " + str(now) + " CO2: " + str(co2) + "ppm, rssi: " +str(rssiList[count]))
            except:
                print("Error happened. Couldn't access file or corrupted data")
            newIndex = (dict_devices[macList[count]][2] + 1)%lenOfRssiFilter
            dict_devices[macList[count]][2] = newIndex
            dict_devices[macList[count]][3+ newIndex] = rssiList[count]
            dict_devices[macList[count]][0] = 0
            dict_devices[macList[count]][-1] = co2

    strongestSignal = ""
    maxRssi = -200
    for device in dict_devices:
        dict_devices[device][0] = dict_devices[device][0] + 1 #increase timout counter
        if dict_devices[device][0] < maxTimeout: # find strongest device among the active ones
            thisRssi = statistics.median(dict_devices[device][3:lenOfRssiFilter])
            if thisRssi > maxRssi:
                strongestSignal = device
                maxRssi = thisRssi

        #print("Timeout: " + str(dict_devices[device][0]) + " rssi: " + str(dict_devices[device][3:8]))
    if strongestSignal == "":
        print("No Device detected")
        try:
            green.off()
            orange.off()
            red.off()
        except:
            pass
        try:
            colorWipe(strip, Color(0, 0, 0))
            strip.show()
        except:
            pass
    else:
        co2_strongest = dict_devices[strongestSignal][-1]
        print("strongest device: " + str(strongestSignal) +" with rssi of: " + str(maxRssi) +" and CO2 of: " + str(co2_strongest) )


def thread_listenAndWriteToFile():
    print("thread_listenAndWriteToFile starting...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    while(True):
        secNow = time.time()
        secTot = secNow - start_time
        print('secNow: ', secNow)
        print('secTot: ', secTot)
        loop.run_until_complete(runBleScan())
        while(time.time() < (secNow + 2)):
            time.sleep(1)

# Main:
#print("Script starting on a " + platform.machine() + " platform")

dict_devices = dict()
default_list_mac_past_rssi = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # [timeoutCnt, cycleCnt, rssiFilterIdx, rssi1, rssi2, ..., rssi_n, CO2]  # also unendlich viele ble geräte erkennbar?
lenOfRssiFilter = len(default_list_mac_past_rssi) - 4           #warum  - 4?
maxTimeout = 5 #5 iterations  
strongestSignal = ""

x = threading.Thread(target=thread_listenAndWriteToFile, daemon=True)
x.start()

try:
    while True:
        time.sleep(1)
        print('processing...')  
        if time.time() - start_time > 2000:
            print("Process stopped after: ", (time.time() - start_time)/60, "mins")
            print("exiting...")
            print('------ BREAK ------ exiting after time limit...')
            break

except KeyboardInterrupt:
    print("Process stopped after: ", (time.time() - start_time)/60, "mins")
    print("exiting...")
    print('------ BREAK ------ exiting after interrupt...')
    print("Process stopped after: ", (time.time() - start_time)/60, "mins")
    print("exiting...")