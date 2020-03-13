import cv2
import mss
import numpy as np
import pyautogui as pag
import time

from colorama import init

init(autoreset=True)

pag.PAUSE = 0.08

fail_limit = 10
initial_dalay = 0.08


# 위치값을 정확이 못잡으면 컬러 평균을 못구함..
left_icon_pos = {'top': 600, 'left': 110, 'width': 75, 'height': 75}
right_icon_pos = {'top': 600,'left': 270, 'width': 75, 'height': 75}
left_button = [36, 715]
right_button = [345,715]



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

if __name__ == "__main__":
    pag.countdown(3)
    n_fails = 0
    n_frames = 0
    fever = False
    last_fever = time.time()
    last_icons = []

    while True:
        n_frames += 1

        if fever and time.time() - last_fever > 10:
            print('############### FEVER ################')
            pag.click(x=left_button[0], y=left_button[1])

            if time.time() - fever > 5:
                fever = False
                last_fever = time.time()
            else:
                continue

        with mss.mss() as sct:

            left_img = np.array(sct.grab(left_icon_pos))[:, :, :3]
            right_img = np.array(sct.grab(right_icon_pos))[:, :, :3]
            # cv2.imshow('OpenCV/Numpy normal', np.concatenate((left_img, right_img), axis=1))
            # cv2.waitKey(1)
            # continue
            #cv2.imwrite('d:/python/%s.jpg' % (str(n_frames)), np.concatenate((left_img, right_img), axis=1))
            #cv2.imshow('left_img', left_img)
            #cv2.imshow('right_img', right_img)
            #cv2.waitKey(0)

        left = get_colors(left_img)
        right = get_colors(right_img)
        left_icon = left[0]
        right_icon = right[0]

        #print(left_icon)
        #print(right_icon)


        if left_icon == 'SWORD' and (right_icon == 'BOMB' or right_icon == 'POISON'):
            print('TAP LEFT!')
            pag.click(x=left_button[0], y=left_button[1])
            n_fails = 0
        elif right_icon == 'SWORD' and (left_icon == 'BOMB' or left_icon == 'POISON'):
            print('TAP RIGHT!')
            pag.click(x=right_button[0], y=right_button[1])
            n_fails = 0
        elif left_icon == 'JEWEL' and right_icon == 'JEWEL':
            pag.click(x=left_button[0], y=left_button[1])
            n_fails = 0
            fever = time.time()
            cv2.imwrite('D:/python/fever_%s.jpg' % (str(n_frames)), np.concatenate((left_img, right_img), axis=1))
        else:

            n_fails += 1
            if n_fails > fail_limit:
                print('failed %s times, terminate!' % (fail_limit))
                break

        # get_mouse_position()
        # print('========================')
        time.sleep(initial_dalay)
