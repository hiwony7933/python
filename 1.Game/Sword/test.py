import cv2, time, sys, random, mss
import numpy as np
import pyautogui as pag
from colorama import init, Fore, Back, Style
init(autoreset=True)
from helpers import *

# while True :
#     x, y = pag.position()
#     position_str = "x : " + str(x) + " y : " + str(y)
#     print(position_str)


def get_colors(img):
    mean = np.mean(img, axis=(0, 1))

    result = None

    if mean[0] > 50 and mean[0] < 55 and mean[1] > 50 and mean[1] < 55 and mean[2] > 50 and mean[2] < 55:
        result = 'BOMB'
    elif mean[0] > 250 and mean[1] > 85 and mean[1] < 110 and mean[2] > 250:
        result = 'SWORD'
    elif mean[0] > 100 and mean[0] < 130 and mean[1] > 150 and mean[1] < 200 and mean[2] > 90 and mean[2] < 110:
        result = 'POISON'
    elif mean[0] > 210 and mean[0] < 230 and mean[1] > 200 and mean[1] < 225 and mean[2] > 120 and mean[2] < 135:
        result = 'JEWEL'

    return (result, mean)

left_icon_pos = {'top': 600, 'left': 110, 'width': 75, 'height': 75}
right_icon_pos = {'top': 600,'left': 270, 'width': 75, 'height': 75}
left_button = [36, 715]
right_button = [345,715]

print(left_icon_pos)
print(right_icon_pos)
with mss.mss() as sct :
    left_img = np.array(sct.grab(left_icon_pos))[:,:,:3]
    right_img = np.array(sct.grab(right_icon_pos))[:,:,:3]

    cv2.imshow('left_img', left_img)
    cv2.imshow('right_img', right_img)
    cv2.waitKey(0)

left = get_colors(left_img)
right = get_colors(right_img)
left_icon = left[0]
right_icon = right[0]

print(left_icon)
print(right_icon)