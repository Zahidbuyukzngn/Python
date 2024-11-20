# #başka dosyadaki metne burdan erişebiliriz
# f = open("regex.py", "r")

# print(f.read())

# #başka dosyalardan açma
# #f = open("D:\\myfiles\welcome.txt", "r")

# #print(f.read())

# #sadece 5 karakter alır adını belirttiğimiz dosyadan
# f = open("regex.py", "r")
# print(f.read(5))

# #sadece 1 tane satırı alır(ile satırı aldı)
# f = open("regex.py", "r")
# print(f.readline())
# #readline() iki kez çağırarak, ilk iki satırı okuyabilirsiniz:

# #dosyada satır satır dolaşma
# f = open("sets.py", "r")
# for x in f:
#   print(x)


# #dosyayı kapatma
# f = open("sets.py", "r")
# print(f.readline())
# f.close()

# #Not: Dosyalarınızı her zaman kapatmalısınız, bazı durumlarda arabelleğe alma nedeniyle bir dosyada yapılan değişiklikler siz dosyayı kapatana kadar gösterilmeyebilir.

"DOSYA OKUMA MEHMET TEK İLE TEKRAR"

# readlines  Bu metot ile de dosyanın içeriğini satır satır liste içine atıyor.

#utf-8 (Unicode Transformation Format - 8 bit): En yaygın kullanılan karakter kodlamasıdır.
#İngilizce metinlerden diğer dillerdeki özel karakterlere kadar geniş bir destek sunar.
dosya=open("Benimdosyam.txt","r",encoding="utf-8")

liste =dosya.readlines()

print(liste)
print(liste[1])


#seek() ve tell() metotlarını kullanarak dosya içinde hareket edebilirsiniz. 
#Seek() metodu ile istediğiniz karakter sayısına gidebilir , 
#tell() metodu ile de kaçıncı karakterde olduğunu öğrenebilirsiniz


with open("Benimdosyam.txt","r",encoding="utf-8") as cv:
   #10.karakter itibaren başlayacak
    cv.seek(10)
    #10dan itibaren 20 karakter kadar oku dedik
    print(cv.read(20))
    #kaçıncı karakterde olduğumuzu söylettirdik
    print(cv.tell())