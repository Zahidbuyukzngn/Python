txt = f"The price is 49 dollars"
print(txt)

#f koymaı unutma f formatı.
price = 59
txt = f"The price is {price} dollars"
print(txt)

#59 dan sonra 2 tane 00 koydurduk=59.00 çıktı
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#bir değişkende tutmadan da 95 tanımlayabiliriz=95.00 çıktı
txt = f"The price is {95:.2f} dollars"
print(txt)

#çarpma işlemini yaptık f stringinde
txt = f"The price is {20 * 59} dollars"
print(txt)

#f stringinde matematiksel işlemler.vergiyi ekleme
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

#if else blokları ile kullanımı
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

#fonksiyonlar da kullanılabilir
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

#feet birimini metreye dönüştürme
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

#binlik ayırıcı olan virgül kullanımı ile çıktı 59,000
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)



#İşte Python'da kullanılan format operatörlerinin Türkçe açıklamaları:
"""
:< :    Sonucu (mevcut alan içinde) sola yaslar.
:> :    Sonucu (mevcut alan içinde) sağa yaslar.
:^ :    Sonucu (mevcut alan içinde) ortalar.
:= :    İşareti en sol pozisyona yerleştirir.
:+ :    Sonucun pozitif veya negatif olduğunu göstermek için artı işareti kullanır.
:- :    Yalnızca negatif değerler için eksi işareti kullanır.
: :     Pozitif sayılardan önce ekstra boşluk (ve negatif sayılardan önce eksi işareti) ekler.
:, :    Binlik ayırıcı olarak virgül kullanır.
:_ :    Binlik ayırıcı olarak alt çizgi kullanır.
:b :    İkilik (binary) format.
:c :    Değeri karşılık gelen Unicode karakterine dönüştürür.
:d :    Ondalık sayı formatı.
:e :    Küçük "e" ile bilimsel gösterim formatı.
:E :    Büyük "E" ile bilimsel gösterim formatı.
:f :    Sabit noktalı sayı formatı.
:F :    Sabit noktalı sayı formatı (sonsuzluğu INF ve NaN'ı NAN olarak gösterir).
:g :    Genel format.
:G :    Genel format (bilimsel notasyon için büyük "E" kullanır).
:o :    Sekizlik (octal) format.
:x :    Küçük harfli onaltılık (hexadecimal) format.
:X :    Büyük harfli onaltılık format.
:n :    Sayı formatı (bölgesel ayarlara göre biçimlendirilir).
:% :    Yüzde formatı.
"""
#STRİNGS FORMAT
#format ile kullanımı ama f stringi daha kullanışlı
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

#birden fazla yeretutucu ile kullanımı
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#0,1,2 diye indekse göre belirledik
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


#aynı dize indeksini 2 kere kullandık
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

#isim ile direkt ulaşma
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))