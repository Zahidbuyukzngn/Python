#Bir dağılım grafiği diyagramı çizmek için scatter() yöntemini kullanın:
#scatterin farklı kullanımları python dosyasında

import matplotlib.pyplot as plt
import numpy as np

x=np.array([7,6,5,4,3,2,1])
y=np.array([100,105,110,115,120,125,130])

plt.scatter(x,y)
plt.show()



import matplotlib.pyplot as plt
import numpy as np
#en son ile(1000)ile çokluğu ayarladık düşük olursa çalışmıyor
#1.dizinin ortalaması   2.ise standart sapmadır
x=np.random.normal(5,1,1000)
y=np.random.normal(10,2,1000)

plt.scatter(x,y)
plt.show()

#loc (ortalama): Üretilen dağılımın ortalama değeri. Bu, dağılımın merkezinin nerede olduğunu belirler. Senin örneğinde, x dizisi için ortalama 5, y dizisi için ortalama 10 verilmiş. Bu demektir ki, x etrafında sayılar çoğunlukla 5 civarında, y ise 10 civarında olacak.

#scale (standart sapma): Standart sapma, sayıların ortalamadan ne kadar uzaklaştığını gösterir. Bu, dağılımın genişliğini belirler. Yani dağılım ne kadar yaygın veya dar olacak, buna karar verir. Örneğin, x için standart sapma 1, yani x dizisindeki sayılar çoğunlukla 5 civarında ve 5’ten çok fazla sapma göstermeyecekler.
#y için ise standart sapma 2, yani y dizisindeki sayılar 10 civarında olacak, ama 10’dan biraz daha geniş bir aralıkta dağılım gösterecekler.

#size (boyut): Kaç adet rastgele sayı üretileceğini belirtir. Burada 1000 kullanılmış, yani hem x hem de y dizileri için 1000 adet rastgele sayı üretilmiş.

