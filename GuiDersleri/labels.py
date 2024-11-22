from tkinter import *  # Tkinter kütüphanesi GUI (grafiksel arayüz) oluşturmak için kullanılır.

# Ana pencereyi oluşturuyoruz (Tk sınıfını kullanarak). 
# Not: 'Tk' büyük harf T ve küçük harf k ile yazılmalıdır.
window = Tk()

# Bir resim yükleniyor. Dosya yolunun doğru olduğundan emin olun.
photo = PhotoImage(file="C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/GuiDersleri/turuncuKedy.png")

# Etiket (Label) oluşturuluyor.
# Etiket, bir pencere üzerinde sabit bir metin veya resim göstermek için kullanılır.
label = Label(window,
              text="Kedy analiz programına hoşgeldin",  # Gösterilecek metin
              bg="black",  # Arka plan rengi (siyah)
              font=("Arial", 50, 'bold'),  # Yazı tipi, boyutu ve kalınlık stili
              fg="#00FF00",  # Yazı rengi (yeşil - hex renk kodu)
              relief=RAISED,  # Kenarlık stili (yükseltilmiş görünüm)
              bd=20,  # Kenarlık kalınlığı (20 piksel)
              padx=20,  # Etiketin iç kenarlarına yatay boşluk (20 piksel)
              pady=20,  # Etiketin üst ve alt kenarlarına dikey boşluk (20 piksel)
              image=photo,  # Resim dosyasını etikete ekliyoruz
              compound='bottom'  # Metin ve resim hizalaması (resim altta, metin üstte),diğerleride parantez karşısında geliyor
              )

# Etiketi pencereye yerleştiriyoruz.
# 'pack()' metodu etiketi varsayılan yerleşim düzenine göre pencereye ekler.
label.pack()

# Pencereyi çalıştırıyoruz (ana döngü başlatılıyor).
# Bu, pencerenin sürekli açık kalmasını ve kullanıcı girişlerini beklemesini sağlar.
window.mainloop()
