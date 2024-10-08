#min ve max alır çıktı)(5,25)
x = min(5, 10, 25)
y = max(6, 10, 25)

print(x)
print(y)

#parantez içindeki sayının mutlak değerini döndürür.
#burda girdiyi mutlak değere çevirir 
girdi=input()
x = abs(int(girdi))
print(x)

#üs alma.4üzeri 3 
x = pow(4, 3)
print(x)

#üs alma girdiyle
taban=input("lütfen tabanı giriniz: ")
üs=input("lütfen üssü giriniz: ")

y=pow(int(taban),int(üs)) 
print(y)


#math işemleri için içeri import etmek gerekiyor.burda sqrt ile 64ün kökünü aldık çıktı 8.0
#int ekleyince floatttan int dönüştü 8 oldu
import math

x = math.sqrt(64)
print(int(x))


#math.ceil() yöntemi bir sayıyı yukarı doğru en yakın tamsayısına yuvarlar ve math.
#floor() yöntemi bir sayıyı aşağı doğru en yakın tamsayısına yuvarlar ve şu sonucu verir:

import math
#yukarı en yuvarlar
x = math.ceil(1.4)
#aşağı yuvarlar
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#math.pi sabiti, PI'nin değerini döndürür (3.14...):
#hesaplamalrda kullanılabilr
import math

x = math.pi

print(x)