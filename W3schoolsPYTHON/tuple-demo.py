#join tuple(2 ile çarpıp meyveleri 2 kere yazdırdık)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#2 tupplı toplama birlşetirme
fruits2=("kiwi","mango")
myFruits=fruits+fruits2

print(myFruits)

#count(): Belirtilen değerin bir demet (tuple) içinde kaç kez geçtiğini döndürür.
#index(): Bir demet içinde belirtilen değeri arar ve bulunduğu konumun indeksini döndürür.

#kaç kere geçtiğini söylemesi için"banana"yazdık çıktı 1
takeCount=fruits.count("banana")
print(takeCount)

#kaçıncı indekste olduğunu söyledi çıktı 0
takeİndex=fruits2.index("kiwi")
print(takeİndex)