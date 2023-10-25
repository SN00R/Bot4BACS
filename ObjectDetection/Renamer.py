import os
import cv2

dirname = "/Users/noor/Bot4BACS/ObjectDetection/Rotated"
imnum = 1
for img in os.listdir(dirname):
    imgpath = os.path.join(dirname,img) 
    filename = "Img_" + str(imnum) + '.jpg'
    savepath = os.path.join(dirname, filename)
    os.rename(imgpath,savepath)
    imnum = imnum + 1
    print("Rotated picture saved: ", filename)
