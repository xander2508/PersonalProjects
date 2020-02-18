import numpy as np
import time
import argparse
import pyautogui
import cv2

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("Fight2.png", image)
