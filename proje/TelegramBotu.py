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


mesaj=f"Tarih: {tarih} \ntoplam vaka: {vaka} \ntoplam ölen kişi: {olum} \niyileşenlerin sayısı: {iyilesme} \nsağlıklı günler dileriz!"

#responseye eşitlemeyi ve sondaki printi yazmaya dikkat et
response = requests.post(
    url='https://api.telegram.org/bot8057948066:AAH7MG-QYm4125EbdIJ9XPfj3dM7kl9R9sU/sendMessage',
    data={'chat_id': 5436403100, 'text': mesaj}
).json()

print(response)

#https://api.telegram.org/bot<token>/sendMessage
#<token>  tamaen sil ve yerine bottan aldığın linki yazs