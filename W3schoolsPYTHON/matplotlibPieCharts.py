# #Pyplot ile pasta grafikler çizmek için pie() fonksiyonunu kullanabilirsiniz:

# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([35, 25, 25, 15])

# #belirli oranda pasta grafiğini oluşturduk
# #ilk dilimin çizimi x ekseninden başlar ve saat yönünün tersine hareket eder:
# plt.pie(y)
# plt.show() 



# #labels parametresiyle pasta grafiğe etiketler ekleyin.
# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([35, 25, 25, 15])
# mylabels=np.array(["FB","GS","BJK","TS"])
# #belirli oranda pasta grafiğini oluşturduk
# #ilk dilimin çizimi x ekseninden başlar ve saat yönünün tersine hareket eder:


# plt.pie(y,labels=mylabels)
# plt.show() 



# #startangel ile kaçıncı dereceden başlaması gerektiğini söyledik,tersten başladığı için grafiğin en üst kısmından sola doğruelmalar ile başlar
# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# #elmayı 0.2 birim dışardan başlattık
# myexplode = [0.2, 0, 0, 0]
# mycolors=["black","green","yellow","orange",]

# #mycolors ile her dilime farklı renk verdik
# #shadow=true ile grafiğimize gölge ekledik
# plt.pie(y, labels = mylabels, startangle = 90,explode=myexplode,shadow=True,colors=mycolors)
# plt.show() 



#Her bir kama için bir açıklama listesi eklemek üzere legend() fonksiyonunu kullanın:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
#legend içine başlık eklemek için title'ı legend içinde kulllan
plt.legend(title="fruits")
plt.show() 