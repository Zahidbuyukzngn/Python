'''
daire alanı:pi.R kare
daire çevresi: 2.pi.R

yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız
pi=3.14
'''
pi=float(3.14)
r=float(input("r değerini giriniz: "))

daireCevresi=float(2*pi*r)
daireAlanı=float(pi*(r**2))

#print("Dairenin alanı:"+str(daireAlanı))

#yukardaki gibi daire alanını stringe çevirmeye gerek kalmadan aşağıdakileri de yaparak aynı çıktıyı alabilriz
print("Dairenin alanı:", daireAlanı)
print(f"Dairenin alanı: {daireAlanı}")
print(f"Dairenin alanı: {daireAlanı}")

print("Dairenin çevresi: "+str(daireCevresi))