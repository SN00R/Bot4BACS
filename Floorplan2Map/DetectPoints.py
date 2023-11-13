import pandas as pd
import cv2
import numpy as np
from PIL import Image

# load image
img = Image.open('/Users/noor/Bot4BACS/Floorplan2Map/HiLo/HiLo_mapped.pgm').convert('RGB')
pixel = img.load()

# calculate the score
score = 0
w=img.size[0]
h=img.size[1]
for i in range(w):
  for j in range(h):
      if pixel[i, j] == (255, 255, 255):
          score += 1
      elif pixel[i, j] == (0, 0, 0):
          score -= 1

""" file_name = "/Users/noor/Bot4BACS/Floorplan2Map/HiLo/HiLo_mapped.pgm"
image = cv2.imread(file_name)

if all(image
cv2.imshow("map", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

 """