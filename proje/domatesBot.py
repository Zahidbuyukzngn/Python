#xler 674,1240
#y de 900"piano tuşlarının kordinatları"
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
    #burdaki değerlere web oyununa gir ve komut sistemine sırasıyla  1.= python 2.=import pyautogui  3.=pyautogui.displayMousePosition()
    #yaz ve çıkan kordinatları mouse ile hesapla.< işaretinin sağı ise rengi belirtiyor
    #eğer renk 100 den küçükse tıkla. renkte komut sistemindeki kordinatların sağında ona göre ayarla
    if pyautogui.pixel(674,900)[0] >=253:
        click(674,900)
    if pyautogui.pixel(700,900)[0] >=253:
        click(700,900)
    if pyautogui.pixel(730,900)[0] >=253:
        click(730,900)
    if pyautogui.pixel(760,900)[0] >= 253:
        click(760,900)
    if pyautogui.pixel(790,870)[0] >= 253:
        click(790,870)
    if pyautogui.pixel(820,850)[0] >= 253:
        click(820,850)
    if pyautogui.pixel(850,890)[0] >= 253:
        click(850,890)
    if pyautogui.pixel(880,800)[0] >= 253:
        click(880,800)
    if pyautogui.pixel(920,790)[0] >= 253:
        click(920,900)
    if pyautogui.pixel(950,900)[0] >= 253:
        click(950,900)
    if pyautogui.pixel(980,850)[0] >= 253:
        click(980,850)
    if pyautogui.pixel(1020,700)[0] >= 253:
        click(1020,700)
    if pyautogui.pixel(1050,750)[0] >= 253:
        click(1050,750)
    if pyautogui.pixel(1100,880)[0] >= 253:
        click(1100,880)
    if pyautogui.pixel(1140,800)[0] >= 253:
        click(1140,800)
    if pyautogui.pixel(1180,850)[0] >= 253:
        click(1180,850)
    if pyautogui.pixel(1210,700)[0] >= 253:
        click(1210,700)
    if pyautogui.pixel(1230,700)[0] >=253:
        click(1230,700)
    if pyautogui.pixel(1120,700)[0] >=253:
        click(1120,700)
    if pyautogui.pixel(1075,800)[0] >=253:
        click(1075,800)
    if pyautogui.pixel(1000,700)[0] >=253:
        click(1000,700)
    if pyautogui.pixel(650,700)[0] >=253:
        click(650,700)
    if pyautogui.pixel(900,720)[0] >=253:
        click(900,720)
print("PROGRAM TAMAMLANDI!")

#şuanda kod çoğu domatesi yakalıyor ama arada kaçanlar var
#yıldızları ve dondurmaları bazen yakalıyor
#bu koddan sonra 1 kere bomba geçti dokunmadı ona
