from tkinter import *
from tkinter import colorchooser

# Kullanıcının tıkladığında renk seçici açmasını sağlayan bir fonksiyon
def click():
    # Renk seçici açılır ve seçilen rengin RGB ve HEX kodları döner
    color = colorchooser.askcolor()
    # Seçilen rengin HEX kodu alınır (ör. #FF5733)
    colorHex = color[1]
    # Pencerenin arka plan rengi seçilen renkle değiştirilir
    window.config(bg=colorHex)
    # Seçilen rengin HEX kodu konsola yazdırılır
    print(color[1])

# Ana pencere oluşturuluyor
window = Tk()

# Pencerenin başlangıç boyutları belirleniyor
window.geometry("420x420")

# Kullanıcıdan renk seçmesini isteyen bir buton oluşturuluyor
button = Button(text="Color Chooser", command=click)
# Buton pencere üzerine yerleştiriliyor
button.pack()

# Ana döngü çalıştırılıyor
window.mainloop()
