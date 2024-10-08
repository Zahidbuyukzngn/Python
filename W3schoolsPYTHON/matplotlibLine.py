import matplotlib.pyplot as plt
import numpy as np

xpoint=np.array([1,3,5,10])

#grafik çizgisini noktalardan oluşturduk.linestyle yerine ls de yazabiliriz
#marker="0" ile işaretleri yuvarlak yaptık
#plt.plot(xpoint,linestyle="dotted",marker="o")

#dashed ile de çizgi yaptık veya -- kullan
# plt.plot(xpoint,linestyle="dashed",marker="o")
# plt.show()

#kısaltılmış kullanımılar
"""
Satır stili daha kısa bir sözdizimiyle yazılabilir:

linestyle   ls    olarak yazılabilir.

dotted şu şekilde yazılabilir:    :

dashed şu şekilde yazılabilir:    --
"""

"""

'solid' (default)	'-'	
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'	
'None'	'' or ' '

"""
ypoint=np.array([0,3,2,3])
#çizginin rengini color ile değiştridik
plt.plot(xpoint,color="red")
plt.show()

#c ile color aynıdır.ayrıca renk paleti kodu da kullanabiliriz
#plt.plot(ypoints, c = '#4CAF50')

#veya desteklenenen 140 renkten birini
#plt.plot(ypoints, c = 'hotpink')


#Satırın genişliğini değiştirmek için linewidth anahtar kelime argümanını veya daha kısa lw kullanabilirsiniz.
#Değer, nokta cinsinden kayan bir sayıdır:

# #lw ile çizgi kalınlığı belirleme
# plt.plot(xpoint, linewidth = '20.5')

#Her satır için bir plt.plot() fonksiyonu belirterek iki çizgi çizin:
#iki çizgiyi aynı grafikte gösterme
plt.plot(xpoint)
plt.plot(ypoint)
plt.show()


#plot()  fonk her grafiği ayrı ayrı oluşturduk
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()