import pyautogui
import time
screenWidth, screenHeight = pyautogui.size()
import mainAnime
# x = 0
# while x == 0:
#    currentMouseX, currentMouseY = pyautogui.position()
#    print(pyautogui.position())
time.sleep(10)
for i in range(mainAnime.startEpisode, mainAnime.endEpisode + 1):
    pyautogui.click(1575 , 450)
    time.sleep(2)
    pyautogui.click(800, 625)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2)