import time

import pyautogui
import win32api
import win32con

from auto.keyboard import keyboard
from auto.mouse import mouse

k = keyboard(True)
m = mouse(True)

if not m.findandgo("images/crome_taskbar_loggedin.png", True, 1):
    m.findandgo("images/crome_taskbar.png", True, 1)

m.findandgo("images/profile.png", True, 3)

if (m.findandgo("images/crome_newtab_btn.png", True, 1) == False):
    m.findandgo("images/crome_newtab_btn2.png", True, 1)

m.findandgo("images/reload.png")
m.moveto(m.location[0] + 200, m.location[1], True)

k.write("https://creativecapsule.greythr.com/")
k.enter()
m.findandgo("images/login_btn.png", True, 5)  # click login button

m.findandgo("tps://creativecapsule.greythr.com/"
            "images/signin.png", False, 5)  # click login button

print("The End")
time.sleep(4);
