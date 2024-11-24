from tkinter import *  # Tkinter modülünü içe aktarıyor (GUI oluşturmak için)
from PIL import Image, ImageTk  # Pillow kütüphanesinden Image ve ImageTk sınıflarını içe aktarıyor

window = Tk()  # Tkinter penceresini oluşturuyor

# Submit fonksiyonu: butona tıklanınca Scale (ölçek) değerini yazdırıyor
def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")  # Ölçek değeri yazdırılır

# Sıcak emoji yeniden boyutlandırma
hotimage_path = 'C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/GuiDersleri/HotEmoji.png'  # Sıcak emoji dosyasının yolu
hotimage = Image.open(hotimage_path)  # Resmi açma
hotimage = hotimage.resize((hotimage.width // 5, hotimage.height // 5))  # Resmi genişlik ve yükseklik olarak 1/5'e indiriyor
hotphoto = ImageTk.PhotoImage(hotimage)  # Tkinter ile uyumlu hale getirmek için Pillow görüntüsünü PhotoImage'ye dönüştürme

# Sıcak emoji görüntüsünü pencereye ekliyor
hotlabel = Label(image=hotphoto)  # Label widget'ı, hotphoto görselini içeriyor
hotlabel.image = hotphoto  # Referansı korumak için hotphoto'yu label.image'ye atıyoruz
hotlabel.pack()  # Görseli pencereye yerleştiriyor

# Ölçek (Scale) widget'ı oluşturuluyor
scale = Scale(window,
              from_=100,  # Ölçeğin başlangıç değeri
              to=0,  # Ölçeğin bitiş değeri
              length=600,  # Ölçeğin uzunluğu
              orient=VERTICAL,  # Ölçeği dikey olarak hizalıyor
              font=("Consolas", 20),  # Ölçek yazısının fontunu belirliyor
              tickinterval=10,  # Ölçek işaretlerinin aralığı
              resolution=5,  # Ölçek çözünürlüğü
              troughcolor="#69EAFF",  # Ölçek altındaki boşluğun rengi
              fg="#FF1C00",  # Ölçek üzerindeki işaretlerin rengi
              bg="#111111",  # Ölçeğin arka plan rengini ayarlıyor
              )
scale.set(((scale["from"] - scale["to"]) / 2) + scale["to"])  # Ölçeği ortalıyor (başlangıçta orta değeri ayarlıyor)
scale.pack()  # Ölçeği pencereye yerleştiriyor

# Soğuk emoji yeniden boyutlandırma
coldimage_path = r'C:\Users\Zahid\OneDrive\Masaüstü\YAZILIM\Python\GuiDersleri\coldEmoji.png'  # Soğuk emoji dosyasının yolu
coldimage = Image.open(coldimage_path)  # Resmi açma
coldimage = coldimage.resize((coldimage.width // 5, coldimage.height // 5))  # Resmi genişlik ve yükseklik olarak 1/5'e indiriyor
coldphoto = ImageTk.PhotoImage(coldimage)  # Tkinter ile uyumlu hale getirmek için Pillow görüntüsünü PhotoImage'ye dönüştürme

# Soğuk emoji görüntüsünü pencereye ekliyor
coldlabel = Label(image=coldphoto)  # Label widget'ı, coldphoto görselini içeriyor
coldlabel.image = coldphoto  # Referansı korumak için coldphoto'yu label.image'ye atıyoruz
coldlabel.pack()  # Görseli pencereye yerleştiriyor

# Submit düğmesi oluşturuluyor
button = Button(window, text="Submit", command=submit)  # "Submit" metni olan bir buton oluşturuluyor ve submit fonksiyonuna bağlanıyor
button.pack()  # Butonu pencereye yerleştiriyor

window.mainloop()  # Tkinter penceresinin sürekli olarak açık kalmasını sağlıyor
