#lampda ile fonksiyonları tek satırda yazabiliriiz
üçgenAlanıHesapla= lambda x,y: (x*y)/2
print(üçgenAlanıHesapla(4,4))


#fonksiyonu başka bir şeye atamamız mümkün
a=üçgenAlanıHesapla
print(a(2,3))