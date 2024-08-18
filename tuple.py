"""

#list ile yakın görevler yapar ama liste üzerinden silme ekleme gibi şeyler yapamıyoruz
tuple=("ali","veli",3,"veli")
list=[1,4,6]
newTuple=("mehmet","zahid")


print(type(tuple))
print(type(list))

print(len(tuple))

list[0]="merhaba"
#tuple[0]="Ekleme yapmaya çalıştık 0. indekste ama hata verdi,ekleme yapılamaz"
print(list)

print(tuple.index("veli"))
#kaç tane veli olduğunu söyledi
print(tuple.count("veli"))
#tuple listesiyle newTuple listesini birleştirdik.Tanım yerinde de birleştirebiliriz.sadece tuple da geçerlidir
print(tuple+newTuple)

#tuple değiştirilemez olduğu için x'e atadığımız tuple'ı y ye atayarak 
#bir liste dönüştürüp banana yı kiwi yaptık ve tekrar tuple'a dönüştürdük
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#bu şekildede ekleme yapabiliriz
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#bu şekilde de kaldırabiliriz listeye dönüştürüp geri tuple yaparak 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#tuple'ı silme
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #hata verecek çünkü tuple'ı tamamne kaldırdık

#tuple Unpack (apple=green etc. gibi atadık)
meyveler = ("apple", "banana", "cherry")

(green, yellow, red) = meyveler

print(green)
print(yellow)
print(red)



#burda ise * kullanarak fazla olan meyveleri red'e atadık ki kodumuz hata vermesin dizi dışına fazlaları yazar
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
"""
arabalar=("BMW","MERCEDES","NİSSAN","AUDİ","VOLVO")

(*bir,iki,üç) =arabalar
