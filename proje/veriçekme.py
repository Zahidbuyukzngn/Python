import requests

corona="https://pomber.github.io/covid19/timeseries.json"

durum=requests.get(corona)
 #json() ile düz metin gibi görünen kodu key value değerine çevirdik
veri=durum.json()
#turkey ile diğer ülkelre arsından türkiyeyi bulduk
tr=veri["Turkey"]
#-1 ile son veriyi aldık,eğer o yazsaydık ilk veriyi verecekti bize yani ilk günün verisi
sonveri=tr[-1]

#f formatında güzelcene yazdırmak için keyleri ayıkladık
tarih=sonveri["date"]
vaka=sonveri["confirmed"]
olum=sonveri["deaths"]
iyilesme=sonveri["recovered"]

print(f"Tarih: {tarih} \ntoplam vaka: {vaka} \ntoplam ölen kişi: {olum} \niyileşenlerin sayısı: {iyilesme}")
print("sağlıklı günler dileriz!")