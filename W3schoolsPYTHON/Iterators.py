#yineleyiciler 

#iter(kullanımı)
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Dizeler aynı zamanda bir dizi karakter içeren yinelenebilir nesnelerdir:
#banana harflerini tek tek yazdırdık
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#Yinelenebilir bir nesneyi yinelemek için for döngüsünü de kullanabiliriz:ü

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#init() kullanmadanda yineleme yapılabilir
#Bir dizenin karakterlerini yineleyin:
mystr = "banana"

for x in mystr:
  print(x)


#BİR ITERATOR OLUŞTURMA


#1'den başlayarak sayıları döndüren bir yineleyici oluşturun; her dizi birer birer artacaktır (1,2,3,4,5 vb. döndürerek):
#iter ve next birlikte kullanılmalı.ayrıca yazdırıken de next kullan
class MyNumbers:
  def __iter__(self):
    self.b = 1
    return self

  def __next__(self):
    x = self.b
    self.b += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#Yinelemenin sonsuza kadar sürmesini önlemek(for döngüsü olduğu için) için StopIteration deyimini kullanabiliriz.
#__next__() yönteminde, yinelemenin belirli bir sayıda yapılması durumunda hata oluşmasını sağlayacak bir sonlandırma koşulu ekleyebiliriz:

#20 tekrardan sonra durduran kod
class MyNumbers:
  def __iter__(self):
    #0 dan başla
    self.a = 0
    return self

  def __next__(self):
    #eğer self.a 20 den küçükse 
    if self.a <= 20:
      x = self.a
      #self.a yı 1 arttır
      self.a += 1
      return x
    else:
        #ıteration ile durdur20 den büyük olunca
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

#Listeler, tuple'lar, sözlükler ve kümelerin tümü yinelenebilir nesnelerdir.