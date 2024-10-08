# #Pyplot ile bir dağılım grafiği çizmek için scatter() fonksiyonunu kullanabilirsiniz.

# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array([7,6,5,4,3,2,1])
# y=np.array([60,70,80,90,100,110,120])

# plt.scatter(x,y,color='black')

# #2 dağılımı aynı grafikte karşılaştırdık
# x=np.array([10,7,6,12,3,2,1])
# y=np.array([65,70,75,80,85,90,105])

# plt.scatter(x,y,c='hotpink')

# plt.show()  
# #x'i yaş olarak düşündük y'yi ise hız arabanın yaşı ne kadar düşükse o kadar hızlı varsayımı çıktı





# #her işaretçiyi farklı belirlediğimiz renklerde yazdırma
# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array([7,6,5,4,3,2,1])
# y=np.array([60,70,80,90,100,110,120])

# #10'a 65 kırmızı oldu sırayla gidiyor
# color=['red','blue','green','yellow','pink','purple','orange']

# plt.scatter(x,y,c=color)

# #2 dağılımı aynı grafikte karşılaştırdık
# x=np.array([10,7,6,12,3,2,1])
# y=np.array([65,70,75,80,85,90,105])

# plt.scatter(x,y,c=color)

# plt.show()  
# #x'i yaş olarak düşündük y'yi ise hız arabanın yaşı ne kadar düşükse o kadar hızlı varsayımı çıktı




# # Renk haritasını, renk haritasının değeriyle cmap anahtar kelime argümanıyla belirtebilirsiniz,
# # bu durumda Matplotlib'de bulunan yerleşik renk haritalarından biri olan 'viridis'.

# #Ek olarak, dağılım grafiğindeki her nokta için bir değer olmak üzere değerlere (0 ile 100 arasında) sahip bir dizi oluşturmanız gerekir:
# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array([10,9,8,7,6,5,4,3,2,1])
# y=np.array([60,65,70,75,80,85,90,95,100,105])

# color=np.array([10,20,30,40,50,60,70,80,90,100])
# #sizes ile hepsine tek tek boyut değeri verebilrsin veya sadece 50 yazdım hepsi 50 oldu
# sizes=np.array([50])

# plt.scatter(x,y,c=color, cmap='viridis',s=sizes)
# #colorbar ile sola viridisin çizelgesini ekledik
# plt.colorbar()
# plt.show()
# #not:VİRİDİS'TEN başka çok fazla renk palet tipi vardır ör=winter,rainbow_r,prism,magma...100 eyakın var



# #alpha bağımsız değişkeniyle noktaların saydamlığını ayarlayabilirsiniz.
# import matplotlib.pyplot as plt
# import numpy as np 

# x=np.array([10,9,8,7,6,5,4,3,2,1])
# y=np.array([60,65,70,75,80,85,90,95,100,105])

# #alpha ile hepsinini opaklığını 0.5 yaptık
# plt.scatter(x,y,alpha=0.5,s=500)
# plt.show()


#x noktaları, y noktaları, renkler ve boyutlar için 100 değer içeren rastgele diziler oluşturun:

import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(100,size=(100))
y=np.random.randint(100,size=(100))

color=np.random.randint(100,size=(100))
#sizeını 5 ile çarparak büyülttüm
size=5*np.random.randint(100,size=(100))


plt.scatter(x,y,c=color, cmap='nipy_spectral',s=size)

plt.colorbar()
plt.show()