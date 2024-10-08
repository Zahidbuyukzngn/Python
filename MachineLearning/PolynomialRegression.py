"""
Python, veri noktaları arasında bir ilişki bulmak ve bir polinom regresyon çizgisi çizmek için yöntemlere sahiptir. Matematik formülünü gözden geçirmek yerine bu yöntemleri nasıl kullanacağınızı size göstereceğiz.

Aşağıdaki örnekte, belirli bir gişeden geçerken 18 araba kaydettik.

Aracın hızını ve geçişin gerçekleştiği günün (saat) saatini kaydettik.

X ekseni günün saatlerini, y ekseni ise hızı temsil eder:
"""


import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

#NumPy'nin bir polinom modeli yapmamıza izin veren bir yöntemi vardır:
#3 eğimi ayarlıyor,1 veya 0 verirsek çizgi düzleşiyor
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

#Ardından satırın nasıl görüntüleneceğini belirtin, 1. konumdan başlıyoruz ve 22. konumda bitiriyoruz:
myline = numpy.linspace(1, 22, 100)

#Orijinal dağılım grafiğini çizin:
plt.scatter(x, y)
#Polinom regresyon çizgisini çizin:
plt.plot(myline, mymodel(myline))
plt.show()



#Verilerim bir polinom regresyonuna ne kadar iyi uyuyor?
import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))
#Not: 0.94 sonucu, çok iyi bir ilişki olduğunu ve gelecekteki tahminlerde polinom regresyonu kullanabileceğimizi gösteriyor.


"Gelecekteki Değerleri Tahmin Etme"
# Artık topladığımız bilgileri gelecekteki değerleri tahmin etmek için kullanabiliriz.
# Örnek: Saat 17:00 civarında gişeden geçen bir arabanın hızını tahmin etmeye çalışalım:
# Bunu yapmak için, yukarıdaki örnekte yer alan aynı mymodel dizisine ihtiyacımız var:

"Saat 17:00'de geçen bir arabanın hızını tahmin edin:"

import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

speed = mymodel(17)
print(speed)



#X ve y ekseni için bu değerler, polinom regresyonu için çok kötü bir uyumla sonuçlanmalıdır:

import numpy
import matplotlib.pyplot as plt

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(2, 95, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()


"Çok düşük bir r-kare değeri almalısınız."
#0.009 iyi bir değer olmadı verilen değerlere dikkat et
import numpy
from sklearn.metrics import r2_score

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))