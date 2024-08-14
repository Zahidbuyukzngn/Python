# #girilen 2 sayıdan hangisi daha büyüktür

# a=int(input("a sayısı: "))
# b=int(input("b sayısı: "))

# buyukMu=(a>b)
# print(f"{a} sayısı {b}'den büyüktür {buyukMu}")

# #kullanıcıdan 2 vize notu al(%60) ve 1 final notu al(%40) ve ortalama 50 den büyükse dersten
# #geçti true yazsın

# vize1=float(input("vize 1'i giriniz: "))
# vize2=float(input("vize 2'i giriniz: "))
# final=float(input("final: "))

# ortalama=(((vize1+vize2)/2)*0.6)+(final*0.4)
# print(f"not ortalamanız :{ortalama} dersten geçme durumunuz {ortalama>=50}")


# #girilen sayının tek mi çift mi olduğunu yazdırın
# girilensayi=float(input("bir sayı giriniz: "))

# tekcifthesapla=girilensayi %2 ==0

# print(f"sayınız çift olma durumu {tekcifthesapla}")



# #girilen sayı pozitif mi negatif hesapla
# girilensayı=int(input("lütfen bir sayı giriniz: "))

# pozNegHesapla=girilensayı>0
# print(f"girilen sayının pozitif olma durumu {pozNegHesapla}")


#parola ve e-mail iste ve doğruluğunu kontrol et
                    #("zahidbaba@gmail.com")
                    #("zayo123")
email=(str(input("lütfen e-postanızı giriniz: ")))
sifre=(str(input("lütfen şifrenizi giriniz: ")))

emailControl=email=="zahidbaba@gmail.com"
sifreControl=sifre=="zayo123"

print(f"email bilgisi {emailControl} sifre bilgisi {sifreControl}")
