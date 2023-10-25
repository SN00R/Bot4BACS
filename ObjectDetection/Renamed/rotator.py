import os
import cv2
import glob
from PIL import Image

imnum = 1
dirname = "/Users/noor/Bot4BACS/ObjectDetection/Renamed/"
rotpath =  "/Users/noor/Bot4BACS/ObjectDetection/rot/"

print(glob.glob("*.jpg"))
for file in glob.glob("*.jpg"):
    src_im = Image.open(file)
    src_im .rotate(90)

""" for img in os.listdir(dirname):
    imgpath = dirname + img
    #print(imgpath)
    #frame = cv2.imread(imgpath)
    frame = cv2.imread(str(imgpath), cv2.IMREAD_UNCHANGED)
    rotated = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    #cv2.imshow(str(img),rotated)
    #cv2.waitKey(0)
    filename = "Rot_" + str(imnum) + '.jpg'
    savepath = rotpath + filename
    print("savepath: ", savepath)
    cv2.imwrite(str(filename), rotated)
    print("Rotated picture saved: ", img)
    imnum = imnum + 1 """

#cv2.destroyAllWindows()

