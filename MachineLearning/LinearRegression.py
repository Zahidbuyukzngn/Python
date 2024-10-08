#Doğrusal regresyon, hepsi arasında düz bir çizgi çizmek için veri noktaları arasındaki ilişkiyi kullanır.
#Bu çizgi gelecekteki değerleri tahmin etmek için kullanılabilir.

#NOT:Makine Öğreniminde geleceği tahmin etmek çok önemlidir.

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#Doğrusal Regresyonun bazı önemli anahtar değerlerini döndüren bir yöntem yürütün:
slope, intercept, r, p, std_err = stats.linregress(x, y)

#Yeni bir değer döndürmek için slope ve intercept değerlerini kullanan bir işlev oluşturun. 
#Bu yeni değer, karşılık gelen x değerinin y ekseninde nereye yerleştirileceğini temsil eder:
def myfunc(x):
  return slope * x + intercept

#x dizisinin her değerini işlev aracılığıyla çalıştırın. 
#Bu, y ekseni için yeni değerlere sahip yeni bir diziyle sonuçlanacaktır:
mymodel = list(map(myfunc, x))

#Orijinal dağılım grafiğini çizin:
plt.scatter(x, y)

#Doğrusal regresyon çizgisini çizin:
plt.plot(x, mymodel)

#Diyagramı görüntüleyin:
plt.show()

"""r yazmamızın amacı"""
#X ekseninin değerleri ile y ekseninin değerleri arasındaki ilişkinin nasıl olduğunu bilmek önemlidir, 
#eğer bir ilişki yoksa doğrusal regresyon hiçbir şeyi tahmin etmek için kullanılamaz.

# Bu ilişki - korelasyon katsayısı - r olarak adlandırılır.

# r değeri -1 ile 1 arasında değişir, burada 0 ilişki olmadığı anlamına gelir ve 1 (ve -1) %100 ilişkili anlamına gelir.

# Python ve Scipy modülü bu değeri sizin için hesaplayacaktır, tek yapmanız gereken bunu x ve y değerleri ile beslemek.


#X ve y ekseni için bu değerler, doğrusal regresyon için çok kötü bir uyumla sonuçlanmalıdır:
#x ve y değerleri düzensiz olduğu için düz yamuk bir şekil çıktı
import matplotlib.pyplot as plt
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


#Sonuç: 0,013 çok kötü bir ilişkiyi gösterir ve bize bu veri setinin doğrusal regresyon için uygun olmadığını söyler.
import numpy
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)