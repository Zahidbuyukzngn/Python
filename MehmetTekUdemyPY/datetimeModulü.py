import datetime

simdi=datetime.datetime.now()

datetime.datetime.today()

#anlık tarih ve zaman bilgisi
print(simdi.strftime("%d/%m/%Y %H:%M:%S"))

from datetime import date

bugun=date.today()
print(bugun.day)
print(bugun.month)
print(bugun.year)

#Yeni bir tarih oluşturduk
yeni=date(2005,10,25)
print(yeni)

"TİME SINIFI"
from datetime import time

nowtime=time(23,20,20,222)

print(nowtime)

#Saat bilgisini aldık
print(nowtime.hour)
#dakika bilgisini aldık
print(nowtime.minute)
#saniye bilgisini aldık
print(nowtime.second)
#microsaniye bilgisini aldık
print(nowtime.microsecond)


zaman1=date(2020,3,10)
zaman2=date(2024,11,17)
print(zaman2-zaman1)


import time 
#anlık zaman bilgisi aldık
print(time.localtime())

#anlık tarih ve zamanı formatlı olarak aldık,çektik
print(time.strftime("%d/%m/%Y %H:%M:%S"))

#gün-ay-yıl
print(time.strftime("%d.%m.%y"))

#SAAT-DAKİKA-SANİYE anlık
print(time.strftime("%H:%M:%S"))

#her 1 saniyede anlık tarih ve zamanı yazdırdık
while True:
    print(time.strftime("%d/%m/%Y %H:%M:%S"))
    time.sleep(1)  # 1 saniyede bir güncelleme yap 
    
#döngüyü durdurmak için konsola gel ve ctrl+c yap
