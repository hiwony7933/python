
import pyautogui as pag

while True :
    x, y = pag.position()
    position_str = "x : " + str(x) + " y : " + str(y)
    print(position_str)



left_icon_pos = {'top': 603, 'left': 110, 'width': 75, 'height': 75}
right_icon_pos = {'top': 603,'left': 270, 'width': 75, 'height': 75}
left_button = [36, 715]
right_button = [345,715]