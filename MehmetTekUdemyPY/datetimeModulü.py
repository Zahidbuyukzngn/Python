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