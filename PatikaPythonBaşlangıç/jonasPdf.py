
adaSehrimi=False
nufus=40#milyon cinsinden
ulkeingilizcekonusuyormu=True

türkiye=[adaSehrimi,nufus,ulkeingilizcekonusuyormu]

if ulkeingilizcekonusuyormu and nufus <50 and not adaSehrimi:
        print (f"LİSA için yaşamaya uygun bir şehir {türkiye}")

else:
        print (f"yaşamaya uygun değil")

kedi="merhaba ben benben!"
print(type(kedi))

kediSpilit=kedi.split(" ") 
print(kediSpilit)

mydict={"mehmet":42,
        "veli":36}

v1,v2,v3=kediSpilit

print(v1,v2,v3)
print(type(kediSpilit))


tupples={
        "ali":42,
}

a1,a2,*a3 = 10,20,30,40
print(a1,a2,a3)

#keys veya values yazarak tuples'dan key veya value çekebiliriz
x,y=mydict.keys()
print(x,y)


x1,x2=20,32

if x1<x2:
        print(f"{x1} küçüktür {x2}'den ")
else:
        print(f"{x2} küçüktür {x1}'den ")

deg1,deg2,deg3=100,2000,30

if deg1<deg2 and deg2<deg3:
        print(f"en büyük değişken {deg3}")

elif deg2<deg1 and deg3<deg1:
        print(f"en büyük değişken {deg1}")

elif deg1<deg2 and deg3<deg2:
        print(f"en büyük değişken {deg2}")

else:
        print(f"büyük bir sayı yok")