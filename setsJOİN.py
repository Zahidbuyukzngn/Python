"""

Python'da iki veya daha fazla kümeyi birleştirmenin birkaç yolu vardır.

union() ve update() metotları,  her iki kümeden de tüm öğeleri birleştirir.
intersection() metodu,     SADECE ortak olan öğeleri tutar.
difference() metodu,       ilk kümedeki diğer küme(ler)de bulunmayan öğeleri tutar.
symmetric_difference()     metodu, SADECE ortak olmayan öğeleri tutar (ortak olanları hariç tutar).

"""
#union kullanımı
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# union == | =>ikiside aynı işlevi görür
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#union ile çoklu birleştirme yapılabilir
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# | ile çoklu birleştirim
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

#umion ile set ile tuple birleştirme
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# UPDATE   
# update ile birleştirim                                 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


#intersection
#aynı olanları bulur ve yazdırır farklı olanları yazdırmaz
#çıktı burda apple
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# & operatörü ile de aynsıı yapılabilir ama & farklı dizi türlerini anlayamayaz hata verir
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

#intersection_update
#intersection ile aynı işlevde burada ama burda set1'i değiştirdi intersection dizi içini değiştirmez
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#set1 kümesinde olan ve set 2 de olmayan öğeleri ekrana yazdırdık
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#difference methodu yerine - operatörü kullanabiliriz,buda aynı & gibi farklı türlerde olmaz
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

#difference_update
#intersection gibi mantığı seti değiştirir direkt 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

#symmetric_difference
#iki sets'de ortak olmayanları aldık apple çıktıda yok bu yüzden
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

# ^ operatoru ile kullanabiliriz
#sadece setsde yapabilirz bunu 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

#direkt seti değiştirdi diğer updateler gibi 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)












