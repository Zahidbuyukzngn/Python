NUMBERS=[1,3,5,7,23,46,21,3,2]
letters=["a","b","h","n","z","v","r","c"]

print(min(NUMBERS))
print(max(NUMBERS))

print(min(letters))
print(max(letters))

val=NUMBERS[2:4]
val=NUMBERS[ :3]
val=NUMBERS[2: ]

val=NUMBERS[0]=99

 #print(val)

#sayıların sonuna 42 ekledik
NUMBERS.append(42)
  #3.index yerine 777 ekledik
NUMBERS.insert(3,777)
NUMBERS.insert(-1,0)

#sondan 3.sünü kaldırma
NUMBERS.pop(-3)

#42 yi buldu ve kaldrıdı
NUMBERS.remove(42)
letters.remove("a")

#sayıları sıraladı küçükten büyüğe
NUMBERS.sort()
#harfleri tersten yazdırdı
letters.reverse()
letters.sort()

print(len(NUMBERS))
print(len(letters))


print(NUMBERS)
print(letters)

#kaçıncı indekste olduğunu söyler paranteze girdiğimiz sayının
print(NUMBERS.count(3))

#tüm elemanları siler
print(NUMBERS.clear)

#kullanıcıdan girdi alarak verdiği 3 araba markasını listede saklayınız

cars=[]

#inputları aldık ve append ile en sona ekler
marka=input("Marka Giriniz:")
cars.append(marka)

marka=input("Marka Giriniz:")
cars.append(marka)

marka=input("Marka Giriniz:")
cars.append(marka)


print(cars)

#range ile 10 tane sayı oluşturduk ve if ile 5den küçüklerini aldık
newlist = [x for x in range(10) if x < 5]

print(newlist)


w3list=["banana","apple","orange","kiwi"]

#false yaparsak düzden yazdırır
#true ise tersten 
w3list.sort(reverse=True)
print(w3list)

#büyük harflerde sıralama yaparken büyük harflere öncelik tanır ve o harfi
#b'den sonra olsa bile orange bana dan önce sıralanır
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#key leri str.lower ile harflerini küçültürek bu sorunu ortadan kaldırabiliriz
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


#extend ile append farkı
#biri diziye dizi ekler extend ise her dizi içndeki elemanı tek tek ekler
listxx = ["a", "b" , "c"]
listyy = [1, 2, 3]

listxx.append(listyy)
listxx.extend(listyy)
print(listxx)