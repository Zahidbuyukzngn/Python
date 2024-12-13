from tkinter import *  # Tkinter modülünü içe aktararak GUI (grafiksel kullanıcı arayüzü) uygulaması oluşturmak için kullanılır.

# Kullanıcının metin girişini alıp işleyecek bir fonksiyon tanımlıyoruz.
def submit():
    imput = text.get("1.0", END)  # Text widget'inden 1. satırın başından (1.0) sonuna kadar olan metni alır.
    print(imput)  # Alınan metni konsola yazdırır.

# Ana pencereyi oluşturuyoruz.
window = Tk()

# Metin girişi için bir Text widget'i oluşturuyoruz.
text = Text(window,            # Metin widget'i ana pencereye eklenir.
            font=("Ink Free", 25),  # Yazı tipi ve yazı boyutunu ayarlar.
            bg="light yellow",     # Arka plan rengini açık sarı yapar.
            width=30,              # Widget'in genişliğini (karakter sayısı olarak) ayarlar.
            height=15,             # Widget'in yüksekliğini (satır sayısı olarak) ayarlar.
            padx=30,               # Widget'in iç yatay boşluğunu ayarlar.
            pady=30,               # Widget'in iç dikey boşluğunu ayarlar.
            fg="purple")           # Yazı rengini mor yapar.
text.pack()  # Metin widget'ini pencereye yerleştirir.

# Submit butonunu oluşturuyoruz.
button = Button(window,         # Buton ana pencereye eklenir.
                text="Submit",  # Buton üzerinde görünecek yazı.
                command=submit) # Butona tıklandığında çalıştırılacak fonksiyon.
button.pack()  # Butonu pencereye yerleştirir.

# Ana döngüyü çalıştırarak pencereyi sürekli açık tutar.
window.mainloop()
