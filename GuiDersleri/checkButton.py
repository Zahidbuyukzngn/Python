from tkinter import *  # Tkinter modülünü içe aktararak GUI (grafik kullanıcı arayüzü) geliştirme araçlarını kullanıyoruz.

# Pencereyi oluşturuyoruz
window = Tk()

# Kullanıcının seçim durumunu kontrol eden fonksiyon
def display():
    if x.get() == True:  # Eğer checkbutton işaretliyse (True)
        print("Kedy koşulları kabul edildi")  # Konsola kabul mesajı yazdır
    else:  # Eğer checkbutton işaretli değilse (False)
        print("Kedy koşulları kabul edilmedi ):")  # Konsola reddedildi mesajı yazdır

# Boolean değer (True/False) tutmak için bir değişken oluşturuyoruz
x = BooleanVar()

# Checkbutton için kullanılacak bir görüntü oluşturuyoruz
kedy_photo = PhotoImage(file='C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/GuiDersleri/turuncuKedy.png')

# Checkbutton (seçim kutusu) oluşturuyoruz
check_button = Checkbutton(
    window,  # Checkbutton'ın ekleneceği pencere (ana pencere)
    text="Kedy koşulları",  # Checkbutton üzerinde görünen metin
    variable=x,  # Checkbutton'un durumunu kontrol eden değişken
    onvalue=True,  # Checkbutton işaretliyken değişkene atanacak değer
    offvalue=False,  # Checkbutton işaretli değilken değişkene atanacak değer
    image=kedy_photo,  # Checkbutton'da gösterilecek görsel
    compound=LEFT,  # Görseli metnin sol tarafına yerleştirir
    command=display,  # Checkbutton'un durumu değiştiğinde çağrılacak fonksiyon
    font=("Arial", 20),  # Metnin yazı tipi ve boyutu
    fg='#00FF00',  # Metnin rengi (yeşil)
    bg="black",  # Checkbutton arka plan rengi (siyah)
    activeforeground="#00FF00",  # Aktif durumdayken metnin rengi (yeşil)
    activebackground="black",  # Aktif durumdayken arka plan rengi (siyah)
    padx=20,  # Checkbutton içindeki yatay boşluk
    pady=20  # Checkbutton içindeki dikey boşluk
)

# Checkbutton'ı pencereye yerleştiriyoruz
check_button.pack()

# Pencereyi sürekli açık tutmak için ana döngüyü başlatıyoruz
window.mainloop()
