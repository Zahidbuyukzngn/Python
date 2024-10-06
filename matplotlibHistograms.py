# Histogram, frekans dağılımlarını gösteren bir grafiktir.
# Her verilen aralıktaki gözlem sayısını gösteren bir grafiktir.,


# #numpy ile normal veri dağılımı
# import numpy as np
# x = np.random.normal(170, 10, 250)

# print(x)


# basit bir örnek
#hist() fonk kullanırsak rastgele sonuç üretmeyecek
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()

print(x)
