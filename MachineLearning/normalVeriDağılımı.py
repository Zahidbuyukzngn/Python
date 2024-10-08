# Tipik bir normal veri dağılımı:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)
#Ortalama değerin 5.0 ve standart sapmanın 1.0 olduğunu belirtiyoruz.
#100 ise aralık sayısıdır
plt.hist(x, 100)
plt.show()
#Normal dağılım grafiği, bir çanın karakteristik şekli nedeniyle çan eğrisi olarak da bilinir.

#numpy.random.normal(ortalama, standart sapma, adet)
#5.0: Üretilen sayıların ortalaması (mean). Bu, üretilen sayıların çoğunun 5 civarında olacağı anlamına gelir.
#1.0: Standart sapma (standard deviation). Bu değer, sayılar arasındaki yayılımı gösterir. 1.0 standart sapma ile sayılar çoğunlukla 4 ile 6 arasında olacaktır (ortalama ± standart sapma).
#100000: Üretilen sayı adedi, yani burada 100.000 adet sayı üretiyoruz.


# plt.hist(data, bins): Verilen veri kümesi için bir histogram çizer.
# x: Daha önce ürettiğimiz normal dağılıma sahip sayı kümesi.
# 100: Histogramda kullanılacak bölme (bin) sayısı. Yani, histogramdaki çubukların sayısı. Burada 100 aralıklı bölmeler kullanıyoruz.






#NUMPY VE MATPLOTLİB
#NumPy (numpy): Matematiksel işlemler ve veri analizi için kullanılan bir Python kütüphanesidir. 
# Özellikle büyük veri setleriyle çalışırken çok faydalıdır.

#Matplotlib (matplotlib.pyplot): Veri görselleştirme için kullanılan popüler bir kütüphane.
# Grafikler, histogramlar, çizelgeler oluşturmak için kullanılır.


x=False and True
print(x)