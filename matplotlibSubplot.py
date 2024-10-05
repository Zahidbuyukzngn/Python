#subplot() birden fazla grafiği yadırmak için kullanılabilir
#plt.subplot(nrows, ncols, index)
# nrows: Grafiğin kaç satıra bölüneceğini belirtir. (Satır sayısı)
# ncols: Grafiğin kaç sütuna bölüneceğini belirtir. (Sütun sayısı)
# index: Hangi pozisyona grafiğin yerleştirileceğini belirtir. Bu değer, 1'den başlar ve soldan sağa, yukarıdan aşağıya olacak şekilde artar.
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1) #1tablo 1 satır 2 sütün 1.tablo
plt.plot(x,y,color="red")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)#2.tablo 1 satır 2 sütün 2.tablo
plt.plot(x,y,color="green")

plt.show()



#yanyana değil grafiklerim üst üste gözükmesini sağlama
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1) #1tablo 2 satır 1 sütün 1.tablo
plt.plot(x,y,color="red")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2,1, 2)#2.tablo 2 satır 1 sütün 2.tablo
plt.plot(x,y,color="green")

plt.show()



#6tane grafik çizme
#plt.title ile başlık ekleyebiliriz
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)
plt.title("faiz",color="red",size="20")

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

#SUPTİTLE İLE GRAFİKLERE ANA BAŞLIK ATTIK
plt.subplot(2, 3, 2)
plt.plot(x,y)
plt.suptitle("ECONOMY",font="borrow",color="green")

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)
plt.title("fiyatlar",color="blue",size="20")

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()