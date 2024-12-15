from tkinter import *  # Tkinter modülünün tüm bileşenlerini içe aktarıyoruz.
from tkinter import filedialog  # Tkinter'dan dosya seçici diyalog kutusunu içe aktarıyoruz.

# Dosya açma işlevi tanımlanıyor
def openFile():
    # Kullanıcıdan dosya seçmesi isteniyor; başlangıç dizini, başlık ve dosya türleri ayarlanıyor.
    filepath = filedialog.askopenfilename(
        initialdir="C:\\Users\\Zahid\\OneDrive\\Masaüstü\\YAZILIM",  # Dosya seçici için başlangıç dizini.
        title="OPEN FİLE OKEY?",  # Dosya seçici başlığı.
        filetypes=(("text files", "*.txt"),  # Yalnızca metin dosyalarını filtreler.
                   ("all files", "*.*"))  # Tüm dosya türlerini gösterir.
    )
    # Seçilen dosyayı okuma modunda açıyoruz.
    file = open(filepath, 'r')
    # Dosya içeriğini konsola yazdırıyoruz.
    print(file.read())
    # Dosya kapatılıyor.
    file.close()

# Tkinter penceresi oluşturuluyor.
window = Tk()

# "OPEN" butonu oluşturuluyor ve openFile fonksiyonu tetikleme işlevi atanıyor.
button = Button(
    text="OPEN",  # Butonun üzerinde yazacak metin.
    command=openFile  # Butona tıklandığında çalışacak fonksiyon.
)

# Buton pencereye ekleniyor.
button.pack()

# Tkinter uygulaması döngüye alınıyor ve pencere ekranda tutuluyor.
window.mainloop()
