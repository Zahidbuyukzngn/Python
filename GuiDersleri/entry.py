# Tkinter modülünden gerekli sınıfları içeri aktarıyoruz.
from tkinter import *

# 'Submit' butonuna tıklanınca çağrılan fonksiyon.
def submit():
    # Entry alanından kullanıcı tarafından girilen metni alıyoruz.
    username = entry.get()
    # Konsola "HELLO [kullanıcı adı]" şeklinde bir çıktı yazdırıyoruz.
    print("HELLO " + username)

# 'Delete' butonuna tıklanınca çağrılan fonksiyon.
def delete():
    # Entry alanındaki metni tamamen silmek için 0'dan sona kadar olan kısmı siliyoruz.
    entry.delete(0, END)

# 'Backspace' butonuna tıklanınca çağrılan fonksiyon.
def backspace():
    # Entry alanındaki son karakteri silmek için toplam karakter sayısından 1 çıkarıyoruz.
    entry.delete(len(entry.get()) - 1, END)

# Tkinter ana penceresini oluşturuyoruz.
window = Tk()

# Giriş (Entry) alanını oluşturuyoruz.
entry = Entry(window,  # Pencerenin ebeveyni olarak 'window' belirleniyor.
              font=("Comic Sans", 50),  # Yazı tipi ve boyutu ayarlanıyor.
              fg="#00FF00",  # Yazı rengi (yeşil).
              bg="black"  # Arka plan rengi (siyah).
              )

# EKSTRA YORUM SATIRLARI AÇIKLAMASI:
# 'insert' metodu: Giriş alanına başlangıçta bir varsayılan metin eklemek için kullanılır.
# entry.insert(0, 'Spongebob') -> Giriş alanına başlangıçta 'Spongebob' metnini ekler.
# Örnek: Kullanıcı giriş yapmadan önce bir öneri göstermek için.

# 'show' özelliği: Giriş alanındaki metni gizlemek için kullanılır. Özellikle şifre girişlerinde kullanılır.
# entry.config(show="*") -> Giriş alanındaki her karakteri "*" ile gizler.

# 'state' özelliği: Giriş alanının aktif mi yoksa devre dışı mı olacağını belirler.
# entry.config(state=DISABLED) -> Giriş alanını devre dışı bırakır, kullanıcı herhangi bir giriş yapamaz.

# 'Submit' butonunu oluşturuyoruz.
submit_button = Button(window,  # Pencerenin ebeveyni olarak 'window' belirleniyor.
                       text="Submit",  # Buton üzerinde görünecek yazı.
                       command=submit)  # Butona tıklandığında 'submit' fonksiyonu çağrılır.
submit_button.pack(side="right")  # Buton pencerenin sağına yerleştiriliyor.

# 'Delete' butonunu oluşturuyoruz.
delete_button = Button(window, 
                       text="Delete",  # Buton üzerinde "Delete" yazacak.
                       command=delete)  # Butona tıklandığında 'delete' fonksiyonu çağrılır.
delete_button.pack(side="right")  # Buton pencerenin sağına yerleştiriliyor.

# 'Backspace' butonunu oluşturuyoruz.
backspace_button = Button(window, 
                          text="Backspace",  # Buton üzerinde "Backspace" yazacak.
                          command=backspace)  # Butona tıklandığında 'backspace' fonksiyonu çağrılır.
backspace_button.pack(side="right")  # Buton pencerenin sağına yerleştiriliyor.

# Giriş alanını pencereye yerleştiriyoruz.
entry.pack(side=LEFT)  # Giriş alanı pencerenin soluna yerleştiriliyor.

# Tkinter ana döngüsü başlatılıyor. Uygulama kullanıcı girişini beklemeye başlar.
window.mainloop()
