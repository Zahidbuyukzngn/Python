import pyautogui
import time

def mesaj():
    pyautogui.write("Merhaba Garıp Kont")
    pyautogui.press('enter')

while True:
    mesaj()
    time.sleep(1)  # 1 saniye aralıkla tekrar mesaj gönderir