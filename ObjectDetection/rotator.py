import os
import cv2

imnum = 1
dirname = "/Users/noor/Bot4BACS/ObjectDetection/Img"

while True:
    for img in os.listdir(dirname):
        imgpath = os.path.join(dirname,img) 
        #print(imgpath)
        frame = cv2.imread(imgpath)
        rotated = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        #cv2.imshow(str(img),rotated)
        rotpath =  "/Users/noor/Bot4BACS/ObjectDetection/Rotated"
        savepath = os.path.join(rotpath, img)
        cv2.imwrite(savepath, rotated)
        print("Rotated picture saved: ", img)