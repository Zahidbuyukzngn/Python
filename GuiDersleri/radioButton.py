from tkinter import *
from PIL import Image, ImageTk  # Pillow kütüphanesi

# Ana pencereyi oluştur
window = Tk()

# Kullanıcının seçimini değerlendiren fonksiyon
def order():
    if x.get() == 0:
        print("Pizza siparişi!")  # Pizza seçimi yapılırsa
    elif x.get() == 1:
        print("Hamburger siparişi!")  # Hamburger seçimi yapılırsa
    elif x.get() == 2:
        print("Hotdog siparişi!")  # Hotdog seçimi yapılırsa
    else:
        print("?????????")  # Hiçbir seçim yapılmadıysa

# Radiobutton'lar için bir IntVar değişkeni tanımla
x = IntVar()

# Resimleri Pillow kütüphanesiyle yükleyip boyutlandır(bunu brocode değil kendim ekledim fotolar büyük geliyordu)
pizza_image = ImageTk.PhotoImage(
    Image.open("C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/GuiDersleri/pizza.png").resize((150, 150))
)  # Pizza resmi, 150x150 boyutunda
hamburger_image = ImageTk.PhotoImage(
    Image.open("C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/GuiDersleri/hamburger.png").resize((150, 150))
)  # Hamburger resmi, 150x150 boyutunda
hottog_image = ImageTk.PhotoImage(
    Image.open("C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/GuiDersleri/hottog.png").resize((150, 150))
)  # Hotdog resmi, 150x150 boyutunda

# Resimleri bir listeye ekle
yiyecekler = [pizza_image, hamburger_image, hottog_image]  # Her bir yiyeceğin resmi listede tutulur

# Radiobutton'ları döngüyle oluştur ve ekrana yerleştir
for index in range(len(yiyecekler)):
    radio_button = Radiobutton(
        window,
        text=["Pizza", "Hamburger", "Hotdog"][index],  # Yiyecek isimleri
        variable=x,  # Seçim değişkeni
        value=index,  # Her buton için farklı bir değer
        padx=25,  # Butonun yatay boşluğu
        pady=5,  # Butonun dikey boşluğu
        image=yiyecekler[index],  # Butona atanacak resim
        compound='left',  # Resim metnin solunda olacak şekilde konumlanır
        indicatoron=0,  # Radiobutton'da standart yuvarlak göstergeleri kaldırır (bunu kullanmazsak yuvarlak seçme tuşu gelir bunu yapınca sütünü seçiyoruz)
        width=200,  # Buton genişliği
        command=order,  # Butona tıklandığında `order` fonksiyonu çağrılır
    )
    radio_button.pack(anchor=W)  # Radiobutton'ları sola hizala (west yani batıya hitafen)

# Ana döngüyü başlat
window.mainloop()
