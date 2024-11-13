sayılar=[1,2,3,4,5]


#'map' fonksiyonu ve 'lambda' ifadesi kullanılarak 'sayılar' listesindeki her elemanın karesi hesaplanıyor.
#Her bir eleman için lambda fonksiyonu (lambda sayı: sayı ** 2) karesini alarak döner.
#'map' fonksiyonu, lambda fonksiyonunu listedeki her elemana uygulayıp sonuçları yeni bir listeye dönüştürür.
sayılarınKaresi=list(map(lambda sayı:sayı**2,sayılar))

#YUKARDAKİ MAP YERİNE BUDA YAPILABİLİR,aynı sonucu verir
sayılarınKaresi2=[]
for sayi in sayılar:
    sayılarınKaresi2.append(sayi**2)


print(sayılarınKaresi)
print(sayılarınKaresi2)