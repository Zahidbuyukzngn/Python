cars = ["Ford", "Volvo", "BMW"]

# #göyle tanımlamak yerine array tipi tanımlayabililirz
# car1 = "Ford"
# car2 = "Volvo"
# car3 = "BMW"

#fordu toyata yaptık
cars[0] = "Toyota"

#3 öğe olduğu için çıktımız 3
x = len(cars)
print(x)
print(type(cars))

#hondayı sona ekler append methodu
cars.append("Honda")
print(cars)

#2.elemanı siler ford silindi
cars.pop(1)

#volvoyu bulur ve kaldırır
cars.remove("Volvo")



# append():  Listeye bir eleman ekler, listenin sonuna ekler.
# clear():   Listeden tüm elemanları kaldırır.
# copy():    Listenin bir kopyasını döndürür.
# count():   Belirtilen değere sahip elemanların sayısını döndürür.
# extend():  Bir listeyi (veya herhangi bir yineleyeni) mevcut listenin sonuna ekler.
# index():   Belirtilen değere sahip ilk elemanın indeksini döndürür.
# insert():  Belirtilen pozisyona bir eleman ekler.
# pop():     Belirtilen pozisyondaki elemanı kaldırır.
# remove():  Belirtilen değere sahip ilk öğeyi kaldırır.
# reverse(): Listenin sırasını tersine çevirir.
# sort():    Listeyi sıralar.