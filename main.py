import cv2 as cv
import numpy as np
import os
import pyautogui

while (True):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
    
    cv.imshow('Computer Vision', screenshot)

    # Press q to exit
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print("Done")

