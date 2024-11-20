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

while keyboard.is_pressed('q') ==False:
    try:
        #fotoğrafı tek tırnak ile yazmazsak hata alıyoruz
        #greyscale kodu daha hızlı çalışmasını sağlar,gri renge dönüştürür renkleri
        #confidance=1 verdiğimiz foto ile tıpatıp aynı olması lazım kodun çalışması için
        #confidance=0.8 olunca ufak bozulmalara rağmen kod çalışır.ne kadar düşerse tıpa tıp benzeme özelliği ortadan kalkar

        #region amacı pcnin tüm ekranı değilde sadece belirlediğimiz pixeller arasında tıklamasını sağlar,ve program daha hızlı çalışır

        x_koordinatı,y_koordinatı= pyautogui.locateCenterOnScreen('hedef.png', region=(451,317,1011,616),confidence=0.8, grayscale=True)

        print(x_koordinatı,y_koordinatı)
        click(x_koordinatı,y_koordinatı)
        time.sleep(0.02)
    except:
        pass

print("PROGRAM BİTTİ")
"region hesaplama"
# Sol Üst Köşe ve Sağ Alt Köşe Koordinatlarını Not Edin

# Sol Üst Köşe: (x1, y1)
# Sağ Alt Köşe: (x2, y2)
# Örneğin:

# Sol üst köşe: (100, 200)
# Sağ alt köşe: (300, 400)
# region Parametresini Hesaplama width ve height şu şekilde hesaplanır:

# width = x2 - x1
# height = y2 - y1
# Örneğin:

# width = 300 - 100 = 200
# height = 400 - 200 = 200
"""
region=(x, y, width, height)
x: Arama bölgesinin sol üst köşesinin x koordinatı.
y: Arama bölgesinin sol üst köşesinin y koordinatı.

#SAĞ AL KÖŞE X DEĞERİ - SOL ÜST KÖŞE X DEĞER
width: Arama bölgesinin genişliği.

#SAĞ ALT KÖŞE Y DEĞERİ - SOL ÜST KÖŞE Y DEĞER
height: Arama bölgesinin yüksekliği.
"""

#EKSİK: ÜST ÜSTE 2 HEDEFİ VURAMIYOR BAZEN BİRİNİ VURUYOR