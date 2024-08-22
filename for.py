#bir for tanımlama 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#ankara'nın harflerini tek tek yazdırmış olduk
for x in "Ankara":
  print(x)

#banana da döngüyü kırdı chery yazdırmadı
meyveler = ["apple", "banana", "cherry"]
for x in meyveler:
  print(x)
  if x == "banana":
    break

#döngü bananda kırılacak ve aşağıdaki printe gitmeden bitecek çıktı=apple
meyveler2 = ["apple", "banana", "cherry"]
for x in meyveler2:
  if x == "banana":
    break
  print(x)

#continue ile banayı atlayıp apple chery çıktı yaptık
fruits2 = ["apple", "banana", "cherry"]
for x in fruits2:
  if x == "banana":
    continue
  print(x)

#range methodu kullanımı
#0 dan 6(dahil)yazdırdı
for x in range(7):
  print(x)

#2 den başla 6 ya kadar yazdır(2,3,4,5 çıktı)
for x in range(2, 6):
  print(x)

#2 den 30 a kadar yazdır ama sayılar arasında 3'er 3'er git 
#(BAŞLANGIÇ,BİTİŞ,ARTIŞ DEĞERİ)
for x in range(2, 30, 3):
  print(x)


#en sonda bitince else ile finally finished yazdırdık
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  

#eğer range(3 ve aşağısı olursa)else çalışır,bu kodun mantığına biraz daha çalışmalıyım
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


#kullanışlı oldu.adj listesindeki her bir eleman alttaki elemanlarla eşleşiyor yan
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


#eğer bir sonuç istemiyorsak pass ile pas geçebiliriz
for x in [0, 1, 2]:
  pass