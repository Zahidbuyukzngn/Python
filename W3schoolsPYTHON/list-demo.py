
# ”Bmw, Mercedes, Opel, Mazda” elemanlarına sahip bir liste oluşturunuz.


ArabaNewList=["BMW","MERCEDES","OPEL","MAZDA"]
#Liste Kaç elemanlıdır ?
print(len(ArabaNewList))


#Listenin ilk ve son elemanı nedir ?
ilk=ArabaNewList[0]
son=ArabaNewList[-1]

print(ilk+" ve "+son)

#Mazda değerini Toyota ile değiştirin.
 
ArabaNewList[-1] ="TOYOTA"
print(ArabaNewList)

#Mercedes listenin bir elemanı mıdır ?(in methodu ile bulabiliriz)

MERCEDES_VAR_Mİ="MERCEDES" in ArabaNewList
print(MERCEDES_VAR_Mİ)

#Listenin -2 indeksindeki değer nedir ?(opel sondan saydı)
print(ArabaNewList[-2])

#Listenin ilk 3 elemanını alın.
print(ArabaNewList[:3])

#Listenin son 2 elemanı yerine "Totoya” ve "Renault” değerlerini ekleyin.
son2=ArabaNewList[-2:]=["TOYOTA","RENAULT"]
print(ArabaNewList)

#Listenin üzerine "Audi” ve "Nissan” değerlerini ekleyin.
print(ArabaNewList + ["AUDİ","NİSSAN"])

#Listenin son elemanını silin.
'''
del ArabaNewList[-1]
print(ArabaNewList)
'''
#Liste elemanlarını tersten yazdırınız.

print(ArabaNewList[::-1])


#Aşağıdaki verileri bir liste içinde saklayınız
'''
studentA:Yiğit Bilgi,2010,(70,60,70)
studentB:Sena Turan,1999,(80, 70,80)
studentC :Ahmet Turan,1998,(80, 70, 90)

'''
studentA=["yiğit bilgi",2010,[70,70,60]]
studentB=["sena ","turan",1999,[80,70,80]]
studentC=["ahmet turan",2010,[80,70,90]]

#13- liste elemanlarını ekrana yazdırınız
print(studentA,
      studentB,
      studentC)

#sena turan 25 yaşında ve not ortalması :{not ortalaması} "'dır"
tanıtım=f"{studentB[0]} {studentB[1]} {2024-studentB[2]} Yaşında ve not ortalaması {(studentB[3][0]+studentB[3][1]+studentB[3][2])//3}'dır"
print(tanıtım),

"""
Liste (List):           Sıralı ve değiştirilebilir bir koleksiyondur. Aynı öğeden birden fazla barındırabilir.
Demet (Tuple):          Sıralı ve değiştirilemez bir koleksiyondur. Aynı öğeden birden fazla barındırabilir.
Küme (Set):             Sırasız, değiştirilemez* ve indekslenmemiş bir koleksiyondur. Aynı öğeden birden fazla barındıramaz.
Sözlük (Dictionary):    Sıralı** ve değiştirilebilir bir koleksiyondur. Aynı öğeden birden fazla barındıramaz.

"""

"""
append()    Listenin sonuna bir eleman ekler.
clear()     Listedeki tüm elemanları kaldırır.
copy()      Listenin bir kopyasını döndürür.
count()     Belirtilen değere sahip elemanların sayısını döndürür.
extend()    Bir listenin (veya herhangi bir iterablın) elemanlarını, mevcut listenin sonuna ekler.
index()     Belirtilen değere sahip ilk elemanın indeksini döndürür.
insert()    Belirtilen konuma bir eleman ekler.
pop()       Belirtilen konumdaki elemanı kaldırır.
remove()    Belirtilen değere sahip öğeyi kaldırır.
reverse()   Listenin sırasını tersine çevirir.
sort()      Listeyi sıralar.

"""
aylar=["mayıs","haziran","ekim"]
aylar.insert(0,"nisan")
print(aylar)