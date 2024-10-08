thisdict={
  "car":"bmw",
  "years":2010
}
#bu döngü sadece key leri yazdırır
for x in thisdict:
  print(x)

#bu ise valueleri yazdırır
for x in thisdict:
  print(thisdict[x])



#üsttekilere göre daha kullanışlılar
#bu şekilde de valueleri direkt yazdırabiliriz
for x in thisdict.values():
  print(x)

#keysleri yazdırmanın diğer bir yolu
for x in thisdict.keys():
  print(x)

#bu şekilde hem key hem value çıktıda olur
for x, y in thisdict.items():
  print(x, y)