#not operatörü ile çıkan sonucun tam tersini çıkarır(false çıktısı vercekse true çıktısı veriri)
#NOT OPERATÖRÜ
'çıktı false olması gerekirken not ile tersine çevirdik'
x=not 5<4
print(x)

#AND OPERATÖRÜ(birinden biri false ise çıktı=false)

#iki ifade de true(veya false) ise çıktı true;ifadelerden biri bile farklıysa false verir
x=True and False
print(x)
x=False and False
print(x)
#iki tarafta doğru bu yüzden çıktı true
a=2
b=3
c=4
x=(b<c) and (a<c)
print(x)

'& işaretinin kullanımı'
#and ile aynı işi yapar ama short-circuit davranış göstermez


#OR OPERATÖRÜ(bir tane bile doğru varsa çıktı=true)

#sadece iki tarfta false false ise çıktı false onun haricinde full true
x=False or False
y=True or False
print(x,y)

(5<3) or print("sol yanlışsa sağa bakar ve bir komut varsa onu yapar")

#burda | işareti  short-circuit davranışını göstermez 
#normalde bakamması lazım sağ tarafa,soldaki true(false) olunca.sağdaki komutu gerçekleştirir ama hata verir
x=((2<3) | print("sa"))
print(x)