# add()		    Bir elemana küme ekler.
# clear()		Kümedeki tüm elemanları kaldırır.
# copy()		Kümeyi kopyalar.
# difference()	-	İki veya daha fazla küme arasındaki farkı içeren bir küme döndürür.
# difference_update()	-=	Bu kümede olup diğer belirtilen kümelerde de bulunan elemanları kaldırır.

# discard()		         Belirtilen elemanı kümeden kaldırır. (Eleman yoksa hata vermez.)!!!!!!!!!!!!!!!!
setTanım={"mehmet","zahid","türktür"}
settanım2={"hasan","yelli","türktür"}
setTanım.discard("mehmet")
print(setTanım)
print(len(setTanım))

# intersection()	&	    İki kümenin kesişimini içeren bir küme döndürür.
print(setTanım & settanım2)
print(setTanım.intersection(settanım2))
print(settanım2.intersection(setTanım))

# intersection_update()	&=	    Bu kümede olup diğer belirtilen kümelerde bulunmayan elemanları kaldırır.
# isdisjoint()		İki kümenin kesişimi olup olmadığını döndürür.
# issubset()	<=	    Diğer kümenin bu kümeyi içerip içermediğini döndürür.
# <	         Bu kümedeki tüm elemanların diğer belirtilen kümelerde olup olmadığını döndürür.
# issuperset()	>=	    Bu kümenin diğer kümeyi içerip içermediğini döndürür.
# >	         Diğer belirtilen kümelerdeki tüm elemanların bu kümede olup olmadığını döndürür.
# pop()		 Kümeden bir eleman kaldırır ve döndürür.
# remove()		Belirtilen elemanı kümeden kaldırır. (Eleman yoksa hata verir.)
# symmetric_difference()	^	    İki kümenin simetrik farkını içeren bir küme döndürür (her iki kümede de bulunmayan elemanlar).
# symmetric_difference_update()	^=	    Bu küme ile diğer küme arasındaki simetrik farkı bu kümeye ekler.

# union()	|         Belirtilen kümeler ile birleşim yapar ve yeni bir küme döndürür. Orijinal kümeleri değiştirmez

print(setTanım | settanım2)
print(setTanım.union(settanım2))
print(settanım2.union(setTanım))


# update()	|=        Belirtilen kümeler ile birleşim yapar ve sonucu orijinal kümeye atar. Yani, orijinal kümeyi değiştirir.