#tarih ve saati yazdırdık
import datetime

x = datetime.datetime.now()
print(x)

#yıl ve günü döndürür
#2024 ,WEDNESDAY DÖNER
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#tarihi kendimiz belirttik
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)


#ayın adını çıktısını aldık
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


#yüzyılı yazdırma
import datetime

x=datetime.datetime.now()

print(x.strftime("%C"))


#ISO da geçen yıl
import datetime

x=datetime.datetime.now()

print(x.strftime("%G"))

'''
%a	Haftanın günü,      kısa hali	             Çar
%A	Haftanın günü,      tam hali	                Çarşamba
%w	Haftanın günü,      0-6 arası (0 Pazar)	        3
%d	Ayın günü,          01-31 arası	            31
%b	Ay ismi,         kısa hali	Ara
%B	Ay ismi,        tam hali	Aralık
%m	Ay numarası,            01-12 arası	12
%y	Yıl,             kısa hali (yüzyıl olmadan)	18
%Y	Yıl,                 tam hali	2018
%H	Saat,            00-23 arası	17
%I	Saat,            00-12 arası	05
%p	ÖÖ/ÖS	    ÖS
%M	Dakika,             00-59 arası	41
%S	Saniye,          00-59 arası	08
%f	Mikrosaniye,            000000-999999 arası	548513
%z	UTC farkı	+0100
%Z	Zaman dilimi	CST
%j	Yılın gün numarası,              001-366 arası	365
%U	Yılın hafta numarası,            haftanın ilk günü Pazar (00-53 arası)	52
%W	Yılın hafta numarası,            haftanın ilk günü Pazartesi (00-53 arası)	52
%c	Yerel tarih ve zaman	        Pzt Ara 31 17:41:00 2018
%C	Yüzyıl	        20
%x	Yerel tarih versiyonu	    31.12.18
%X	Yerel zaman versiyonu	    17:41:00
%%	Yüzde karakteri	%
%G	ISO 8601 yılı	    2018
%u	ISO 8601 haftanın günü (1-7)	    1
%V	ISO 8601 hafta numarası     (01-53)	01
'''