#aldığımız verileri bir histograma dönüştürdük
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

#52 değer 0 ile 1 arasındadır
# 48 değer 1 ile 2 arasındadır
# 49 değer 2 ile 3 arasındadır
# 51 değer 3 ile 4 arasındadır
# 50 değer 4 ile 5 arasındadır

# Dizi değerleri rastgele sayılardır ve bilgisayarınızda tam olarak aynı sonucu göstermez.



#100000 rastgele sayı içeren bir dizi oluşturun ve bunları 100 çubuklu bir histogram kullanarak görüntüleyin:
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()