# Tkinter modülündeki tüm sınıfları (*) içeri aktarıyoruz.
# Bu, etiket (Label), düğme (Button) ve diğer bileşenlere kolayca erişmemizi sağlar.
from tkinter import *  

# Global bir sayaç değişkeni oluşturuyoruz. Tıklama sayısını tutmak için kullanılıyor.
count = 0

# Pencere (window) objesi oluşturuluyor. Bu, ana uygulama penceresi.
window = Tk()

# Tıklama olayını işleyen bir fonksiyon.
def click():
    global count  # Global değişkeni fonksiyon içinde değiştirebilmek için 'global' anahtar kelimesi.
    count += 1  # Her tıklamada sayaç bir artırılır.
    print(count)  # Tıklama sayısı konsola yazdırılır.

# Resim dosyasını bir PhotoImage nesnesine yüklüyoruz.
# Bu resim düğme üzerinde görünecek.
photo = PhotoImage(file="C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/GuiDersleri/turuncuKedy.png")

# Bir düğme (Button) nesnesi oluşturuluyor.
button = Button(window,  # Düğmenin hangi pencereye ekleneceği (parent) belirleniyor.
                text="click me!",  # Düğmenin üzerindeki yazı.
                command=click,  # Düğmeye tıklandığında çalışacak fonksiyon.
                font=("Comic Sans", 40),  # Yazı tipi ve boyutu.
                fg="#00FF00",  # Yazı rengi (yeşil).
                bg="black",  # Düğmenin arka plan rengi (siyah).
                activebackground="#00FF00",  # Düğme tıklandığında arka plan rengi.
                activeforeground="black",  # Düğme tıklandığında yazı rengi.
                state=ACTIVE,  # Düğme başlangıçta aktif durumda.
                image=photo,  # Düğme üzerinde gösterilecek resim.
                compound='top')  # Resim ve metnin düzenlenme biçimi (resim üstte, metin altta).

# BUTONU pencereye yerleştiriyoruz.
button.pack()

# Tkinter döngüsünü başlatıyoruz. Uygulama penceresi açılır ve kullanıcı etkileşimleri beklenir.
window.mainloop()
