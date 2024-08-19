website="WWW.zahidbzengin.com"
course="Sadık Turan ile 40 saatlik python ogreniyorum kursu"




#Hello World karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
'''result="   Hello World   ".lstrip()'''

#'www.zahidbzengin.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
'''result="WWW.zahidbzengin.com".strip("W.com")'''

#'course' karakteri dizisindeki tüm harfleri küçük yap
'''result=course.lower()
result=course.upper()'''

#'website' içinde kaç tane a harfi vardır (count('a'))
'''result=website.count('a')'''

#website "www” ile başlayıp com ile bitiyor mu?
'''result=(website.startswith("WWW"))'''
'''result=(website.endswith("com"))'''
'''result=(website.startswith("http"))'''


#'website' içinde .'com' ifadesi var mı?(evet var çıktı kaçıncı indexte olduğunu söylüyor)

'''result=website.find(".com")'''
#course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
'''result=course.isalpha()'''

#' Contents ' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
'''result="Contents".center(50,"*")'''
#ljust ile sola yapıştırır rjust ise sağa dorğru yapıştırır
result="Contents".ljust(50,"*")
result="Contents".rjust(50,"*")

# 'course' karakter dizisindeki tüm boşluk karakterlerini '-'ile değiştirin
result=course.replace(" ","-")
   #KAÇ KERE KULLANACAĞIMIZI 1 İLE BELİRTTİK
result=course.replace(" ","-",1)

#'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result="Hello World".replace("Hello","There")

#'course' karakter dizisini boşluk karakterlerinden ayırın.
result= course.split(" ")
   #5.indekteki kelimeyi yazdır
result=result[5]

#sona yazmayı unutma
result= print(result)
'''
capitalize():     İlk karakteri büyük harfe dönüştürür.
casefold():       String'i küçük harfe dönüştürür.
center():         Ortalanmış bir string döndürür.
count():          Belirtilen değerin string içinde kaç kez geçtiğini döndürür.
encode():         String'in kodlanmış bir versiyonunu döndürür.
endswith():       String'in belirtilen değerle bitip bitmediğini kontrol eder ve doğruysa True döner.
expandtabs():     String'deki tab boyutunu ayarlar.
find():           Belirtilen değeri string içinde arar ve bulunduğu pozisyonu döndürür.
format():         Belirtilen değerleri bir string içinde biçimlendirir.
format_map():     Belirtilen değerleri bir string içinde biçimlendirir.
index():          Belirtilen değeri string içinde arar ve bulunduğu pozisyonu döndürür.
isalnum():        String'deki tüm karakterlerin alfanümerik (harf ya da rakam) olup olmadığını kontrol eder. True döner.
isalpha():        String'deki tüm karakterlerin alfabe karakteri olup olmadığını kontrol eder. True döner.
isascii():        String'deki tüm karakterlerin ASCII karakteri olup olmadığını kontrol eder. True döner.
isdecimal():      String'deki tüm karakterlerin ondalık sayı olup olmadığını kontrol eder. True döner.
isdigit():        String'deki tüm karakterlerin rakam olup olmadığını kontrol eder. True döner.
isidentifier():   String'in geçerli bir tanımlayıcı olup olmadığını kontrol eder. True döner.
islower():       String'deki tüm karakterlerin küçük harf olup olmadığını kontrol eder. True döner.
isnumeric():     String'deki tüm karakterlerin sayısal olup olmadığını kontrol eder. True döner.
isprintable():   String'deki tüm karakterlerin yazdırılabilir olup olmadığını kontrol eder. True döner.
isspace():    String'deki tüm karakterlerin boşluk olup olmadığını kontrol eder. True döner.
istitle():    String'in başlık kurallarına uyup uymadığını kontrol eder. True döner.
isupper():    String'deki tüm karakterlerin büyük harf olup olmadığını kontrol eder. True döner.
join():       Bir iterable'ın (örneğin, liste) elemanlarını string'e ekler.
ljust():      String'in sol tarafında belirli bir genişlikte boşluk bırakılmış halini döndürür.
lower():      String'i küçük harfe dönüştürür.
lstrip():     String'in sol tarafındaki boşlukları kaldırır.
maketrans():    Çevirilerde kullanılmak üzere bir çeviri tablosu döndürür.
partition():   String'i üç parçaya böler ve bir demet (tuple) olarak döndürür.
replace():    Belirtilen değeri başka bir değerle değiştirerek yeni bir string döndürür.
rfind():      Belirtilen değeri string içinde arar ve bulunduğu son pozisyonu döndürür.
rindex():     Belirtilen değeri string içinde arar ve bulunduğu son pozisyonu döndürür.
rjust():      String'in sağ tarafında belirli bir genişlikte boşluk bırakılmış halini döndürür.
rpartition():   String'i üç parçaya böler ve bir demet (tuple) olarak döndürür.
rsplit():     String'i belirtilen ayırıcı ile bölerek bir liste döndürür.
rstrip():     String'in sağ tarafındaki boşlukları kaldırır.
split():      String'i belirtilen ayırıcı ile bölerek bir liste döndürür.
splitlines():  Satır sonlarına göre string'i böler ve bir liste döndürür.
startswith():    String'in belirtilen değerle başlayıp başlamadığını kontrol eder ve doğruysa True döner.
strip():      String'in başındaki ve sonundaki boşlukları kaldırır.
swapcase():    Büyük harfleri küçük harfe, küçük harfleri büyük harfe çevirir.
title():    Her kelimenin ilk harfini büyük yapar.
translate():   Çeviri tablosuna göre string'in çevirilmiş bir versiyonunu döndürür.
upper():    String'i büyük harfe dönüştürür.
zfill():    String'in başına belirli bir sayıda sıfır ekleyerek belirtilen uzunluğa kadar doldurur.
'''