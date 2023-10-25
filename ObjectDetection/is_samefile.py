import os
import filecmp

rotdirname = "/Users/noor/Bot4BACS/ObjectDetection/Rotated"

imgdirname = "/Users/noor/Bot4BACS/ObjectDetection/Img"

common = os.listdir(imgdirname)

match, mismatch, errors = filecmp.cmpfiles(imgdirname, rotdirname, common, shallow=False)
# Print the result of
# deep comparison
print("Deep comparison:")
print("Match :", match)
print("Mismatch :", mismatch)
print("Errors :", errors)


""" for img in os.listdir(imgdirname):
    for rot in os.listdir(rotdirname):
        if img == rot:
            print("Ok!")
        else:
            print("Data missing in RotateDir: ", img) """