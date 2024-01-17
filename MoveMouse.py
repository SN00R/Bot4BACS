# Helper script to keep my computer active by moving the mouse during Object Detection training
import time
import pyautogui as pg

def keep_scrolling():
    pg.scroll(200)
    time.sleep(5)
    pg.scroll(-200)
    time.sleep(5)

while True:
    pg.moveTo(311, 599, duration = 3)
    pg.click(311,599)
    time.sleep(2)
    keep_scrolling()
    
    

