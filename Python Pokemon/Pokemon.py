import numpy as np
import time
import argparse
import pyautogui
import cv2
def ClickCentre():
    centre = pyautogui.size()
    pyautogui.click(centre[0]/2, centre[1]/2)
    #im1 = pyautogui.screenshot()
    #im1.save("Screenshot.png")

def MyChoice():
    MyChoice = True
    while MyChoice:
            try:
                ClickCentre()
                time.sleep(0.2)
                PinkLocation = pyautogui.locateOnScreen('Fight.png', grayscale=True, confidence=.9)
                print("J2",PinkLocation)
                Point = pyautogui.center(PinkLocation)
                print("J3")
                time.sleep(0.3)
                pyautogui.click(Point[0], Point[1])
                PinkLocation = pyautogui.locateOnScreen('Fight.png', grayscale=True, confidence=.9)
                if PinkLocation != None:
                    pyautogui.click(Point[0], Point[1])
                PinkLocation = pyautogui.locateOnScreen('Fight.png', grayscale=True, confidence=.9)
                if PinkLocation != None:
                    pyautogui.click(Point[0], Point[1])
                return True
            except:
                ClickCentre()
                if IfWon():
                    return False
def ClickGust():
    Fight = True
    while Fight:
        try:
            time.sleep(0.2)
            Test2 = pyautogui.locateOnScreen('Fight2.png', grayscale=True, confidence=.9)
            Point2 = pyautogui.center(Test2)
            time.sleep(0.3)
            pyautogui.click(Point2[0], Point2[1])
            Test2 = pyautogui.locateOnScreen('Fight2.png', grayscale=True, confidence=.9)
            if Test2 != None:
                pyautogui.click(Point2[0], Point2[1])
            Test2 = pyautogui.locateOnScreen('Fight2.png', grayscale=True, confidence=.9)
            if Test2 != None:
                pyautogui.click(Point2[0], Point2[1])
            Fight = False
        except:
            pass
def IfWon():
    try:
        Won = pyautogui.locateOnScreen('Won.png', confidence=0.5)
        Point = pyautogui.center(Won)
        pyautogui.click(Point[0], Point[1])
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        return True
    except:
        return False


firstTime = True
try:
    while True:
        try:
            LevelUp = pyautogui.locateOnScreen('Ability.png', grayscale=True, confidence=.5)
            Point = pyautogui.center(LevelUp)
            pyautogui.click(Point[0], Point[1])
            i = input("")
        except:
            pass
        time.sleep(1)
        pyautogui.click(button='right')
        time.sleep(15)
        pyautogui.write('r')
        time.sleep(2)
        if firstTime:
            pyautogui.write('b')
            time.sleep(1)
            try:
                PinkLocation = pyautogui.locateOnScreen('Pink.png', grayscale=True, confidence=.5)
                Point = pyautogui.center(PinkLocation)
                pyautogui.click(Point[0], Point[1])
                firstTime = False
            except:
                pass
        time.sleep(1)
        pyautogui.write('g')
        time.sleep(1)
        ClickCentre()
        time.sleep(0.3)
        Battle = True
        while Battle:
            if not MyChoice():
                break
            time.sleep(0.2)
            pyautogui.click()
            time.sleep(0.4)
            ClickGust()
            time.sleep(0.2)
            pyautogui.click()
            time.sleep(0.2)    
except KeyboardInterupt:
    pass
