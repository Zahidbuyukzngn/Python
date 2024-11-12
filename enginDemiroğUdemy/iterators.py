#for döngüsü de bir iteratör'dür

cities=["ankara","İstanbul","konya","denizli"]

#iter() fonksiyonu listeyi bir iteratör objesi dönüyor

myiter=iter(cities)
#next ile birini bitirip diğerine geçmesini sağlıyoruz.
#eğer fazla verirsek hata alırız
#2 tane print(next(myiter)) yazsaydık ankara ve istanbulu yazdıracaktı sadece                               
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


#iter yerine for da kullanılabilir
for city in cities:
    print(city)