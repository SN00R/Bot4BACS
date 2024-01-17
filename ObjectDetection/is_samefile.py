# helper script to check dataset for double 
import os
import filecmp

rotdirname = "/Users/noor/Bot4BACS/ObjectDetection/renamed"

imgdirname = "/Users/noor/Bot4BACS/ObjectDetection/Img"

common = os.listdir(rotdirname)

match, mismatch, errors = filecmp.cmpfiles(imgdirname, rotdirname, common)
# Print the result of
# deep comparison
print("Deep comparison:")
print("Match :", match)
print("Mismatch :", mismatch)
print("Errors :", errors)

