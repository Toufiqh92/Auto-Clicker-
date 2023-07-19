import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2
import pyautogui as pg
from pyautogui import *
import os
import win32api, win32con, win32gui, win32ui, win32con
import time
import keyboard

# img = cv2.imread("Screenshot 2023-07-19 014418.png")
# print(img.shape)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def auto_click():
    while keyboard.is_pressed("q") == False:
        if pg.pixel(700, 600)[0] == 0:
            click(700, 600)
        if pg.pixel(900, 600)[0] == 0:
            click(900, 600)
        if pg.pixel(1000, 600)[0] == 0:
            click(1000, 600)
        if pg.pixel(1200, 600)[0] == 0:
            click(1200, 600)


auto_click()
