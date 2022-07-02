import pyautogui
import random
import time

class keyboard:

    def __init__(self,verbouse=True):
        self.verbouse=verbouse;
        self.speed=0.5;
        self.sleep=1;
  
    def debug(self,message):
        if(self.verbouse): print(message);

    def write(self,text=""):
        pyautogui.write(text)
    
    def enter(self):
        pyautogui.press('enter')
