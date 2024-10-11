# Belki bir şart sağlandığı zaman döngüden aniden çıkmak istersek, bunu break ile sağlıyoruz.
# break komutunu gördüğümüz yerde döngüden çıkıyoruz.
for i in range(10): 
    if i == 3: break 
    print(i)