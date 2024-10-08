#Bir dağılım grafiği diyagramı çizmek için scatter() yöntemini kullanın:
#scatterin farklı kullanımları python dosyasında

import matplotlib.pyplot as plt
import numpy as np

x=np.array([7,6,5,4,3,2,1])
y=np.array([100,105,110,115,120,125,130])

plt.scatter(x,y)
plt.show()