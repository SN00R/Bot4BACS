import os

dirname = "/Users/noor/Bot4BACS/ObjectDetection/Img"
imnum = 1
for img in os.listdir(dirname):
    imgpath = os.path.join(dirname,img) 
    filename = "Img_" + str(imnum) + '.jpg'
    savepath = os.path.join(dirname, filename)
    os.rename(imgpath,savepath)
    imnum = imnum + 1
    print("Rotated picture saved: ", filename)
    
print("imnunm: ", imnum)
