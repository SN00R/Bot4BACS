import os
import re

destdirname = "/Users/noor/Bot4BACS/ObjectDetection/Img_final/"
dirname = "/Users/noor/Bot4BACS/ObjectDetection/Img_renamed/"

imnum = 1
imglist = os.listdir(dirname)
sortedlist = sorted(imglist)
print(imglist)
print(sortedlist)

for img in sortedlist:
    #imgpath = os.path.join(dirname,img) 
    imgpath = dirname + img 
    print(imgpath)
    if imnum < 10:
        filename = "Img_00" + str(imnum) + '.jpg'
    elif imnum >= 10 and imnum <= 99:
        filename = "Img_0" + str(imnum) + '.jpg'
    elif imnum >= 100:
        filename = "Img_" + str(imnum) + '.jpg'
    #savepath = os.path.join(dirname, filename)
    savepath = destdirname + filename
    os.rename(imgpath,savepath)
    imnum = imnum + 1
    
print("imnunm: ", imnum) 

print('All Files Renamed')

print('New Names are')
# verify the result
res = os.listdir(destdirname)
print(res) 

"""

for i in range(1,331):
    filename = "Img_" + str(i) + '.jpg'
    #imgpath = dirname + filename
    for img in imglist:
        print("img: ", img)
        number = int(re.search('Img_(.*).jpg', img).group(1))
        print("Number: ",number)
        if img not in os.listdir(destdirname):
            if img == filename:
                imgpath = dirname + img
                savepath = destdirname + filename
                os.rename(imgpath,savepath)
                print("1) original img: " ,img)
                break
            elif number + 1 == i:
                imgpath = dirname + img
                savepath = destdirname + filename
                os.rename(imgpath,savepath)
                print("2) original img: " ,img)
                break
            else: 
                print("leftover number: ", filename)
        elif img in os.listdir(destdirname):
            print(img, " already in dest. directory!")

print("All images renamed!")
            

for i in imglist:
    for img in range(1,331):
        filename = "Img_" + str(imnum) + '.jpg'
        imgpath = dirname + filename
        if imglist[i] == filename:
            savepath = destdirname + imglist[i]
            os.rename(imgpath,savepath)
            print("original img" ,imglist[i])
            print()
        else:
            print()
            savepath = destdirname + filename
 """