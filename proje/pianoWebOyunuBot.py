"piano tuşlarının kordinatları"
# 950-700
# 824-700
# 700-700
# 600-700

import time
import keyboard
import random
import win32api,win32con
import pyautogui

def click(x,y):
    win32api.SetCursorPos((x,y))

    #mouse sol tıka bas 0,05 saniye sonra kaldır
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

print("başlamak için 's' tuşuna basın")
print("çıkmak için 'q' tuşuna basın" )
#klavyeden s tuşunun girilmesini bekle
keyboard.wait('s')
print("BAŞLADI")

#q harfine basılmadıysa döngü çalışır
while keyboard.is_pressed('q') ==False:
    #burdaki konum ve rgb renk değerlerine ulaşmak için
    #web oyununa gir ve konsole sırasıyla  1.= python 2.=import pyautogui.displayMousePosition()
    #sağ taraf rgb değerini ifade ediyor 100den küçük değerlere tıklıyor
    if pyautogui.pixel(600,700)[0] < 100:
        click(600,700)
    if pyautogui.pixel(700,700)[0] < 100:
        click(700,700)
    if pyautogui.pixel(820,700)[0] < 100:
        click(820,700)
    if pyautogui.pixel(950,700)[0] < 100:
        click(950,700)

print("PROGRAM TAMAMLANDI!")