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