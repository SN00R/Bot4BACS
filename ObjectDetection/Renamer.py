import os

destdirname = "/Users/noor/Bot4BACS/ObjectDetection/Img_selected/"
dirname = "/Users/noor/Bot4BACS/ObjectDetection/rename/"

imnum = 1
#print(os.listdir(dirname))
for img in os.listdir(dirname):
    #imgpath = os.path.join(dirname,img) 
    imgpath = dirname + img 
    #print(imgpath)
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