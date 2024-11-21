from tkinter import *  # Tkinter kütüphanesini içe aktarıyoruz (grafiksel kullanıcı arayüzü oluşturmak için kullanılır).

# Ana pencereyi (window) oluşturuyoruz.
window = Tk()

# Pencerenin boyutunu ayarlıyoruz (genişlik x yükseklik).
window.geometry("440x440")

# Pencerenin başlık adını "kedi analiz programı" olarak ayarlıyoruz.
window.title("kedi analiz programı")

# Bir ikon (pencere simgesi) yükleniyor.
# Burada 'PhotoImage' sınıfını kullanarak PNG formatındaki bir resmi penceremize ikon olarak atıyoruz.
icon = PhotoImage(file="C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/GuiDersleri/turuncuKedy.png")

# Yüklenen resmi pencerenin simgesi olarak belirliyoruz.
window.iconphoto(True, icon)

# Pencerenin arka plan rengini ayarlıyoruz (hex renk koduyla: açık mavi #5cfcff).
window.config(background="#5cfcff")

# Pencereyi sürekli olarak çalıştırıyoruz (kullanıcı etkileşimlerini bekler).
window.mainloop()
