# import matplotlib.pyplot as plt
# import numpy as np

# xpoint=np.array([0,24,24,55,62])
# ypoint=np.array([0,42,43,45,66])

# plt.plot(xpoint, ypoint,)

# #x ve y eksenlerinin yanlarına yazı yazdırdık(yürüyüş yağ yakma oranı gib grafik verilebilir)
# #title ile ise başlık yazdırdık
# plt.title("spor izleme verileri")
# plt.xlabel("ortalama nabız")
# plt.ylabel("kalori yakımı")

# plt.show()


#YAZDIRDIĞIMIZ YAZILARIN FONT RENK BÜYÜKLÜKLERİNİ DEĞİŞTİRME


import matplotlib.pyplot as plt
import numpy as np

xpoint=np.array([0,12,28,55,62])   
ypoint=np.array([0,32,43,45,66])

#fontları belirledik
font1={"family":"Helvetica", "size":"20","color":"blue"}

font2={"family":"Arial", "size":"10","color":"black"}


#fondict ile fonları atadık başlığa fon1'i atadık.x label x eksenini belirtir onada font 2,aynı şekilde ylabel de
#loc= ile başlığın yerini belirleyebiliriiz
plt.title("SPOR İZLEME VERİLERİ", fontdict=font1,loc="left",)
plt.xlabel("ORTALAMA NABIZ",fontdict=font2)
plt.ylabel("KALORİ YAKIMI",fontdict=font2)

#arka plana çizgi ekledik grafiğe
plt.grid()

plt.plot(xpoint, ypoint,color="red")
plt.show()



import matplotlib.pyplot as plt
import numpy as np

xpoint=np.array([0,12,28,55,62])   
ypoint=np.array([0,32,43,45,66])

#fontları belirledik
font1={"family":"Helvetica", "size":"20","color":"blue"}

font2={"family":"Arial", "size":"10","color":"black"}


#fondict ile fonları atadık başlığa fon1'i atadık.x label x eksenini belirtir onada font 2,aynı şekilde ylabel de
#loc= ile başlığın yerini belirleyebiliriiz
plt.title("SPOR İZLEME VERİLERİ", fontdict=font1,loc="left",)
plt.xlabel("ORTALAMA NABIZ",fontdict=font2)
plt.ylabel("KALORİ YAKIMI",fontdict=font2)

#grid()le arka plana çizgi ekledik grafiğe
#axis ile çizgilerin hangi eksende çizilmesi gerektiğini belirtiyoruz
#"y" diyerek y ekseninden sağa doğru çizilmesini sağlarız
#grid arka plan çizgilerinini özelliklerini belirttik;çizgili,yeşil,çizgilerin kalınlığı
plt.grid(axis="y",linestyle="--",linewidth="1",color="green")

plt.plot(xpoint, ypoint,color="red")
plt.show()