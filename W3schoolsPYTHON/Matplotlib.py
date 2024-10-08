import matplotlib

print(matplotlib.__version__)

#çizim yapma
"""
plot() fonksiyonu, bir diyagramda noktalar (işaretçiler) çizmek için kullanılır.

Varsayılan olarak, plot() fonksiyonu noktadan noktaya bir çizgi çizer.

Fonksiyon, diyagramdaki noktaları belirtmek için parametreler alır.

Parametre 1, x ekseni üzerindeki noktaları içeren bir dizidir.

Parametre 2, y ekseni üzerindeki noktaları içeren bir dizidir.

(1, 3) ile (8, 10) arasında bir çizgi çizmemiz gerekirse, çizim fonksiyonuna [1, 8] ve [3, 10] olmak üzere iki dizi geçirmemiz gerekir.
"""

# #kısaltmaları yaptık as dan sonraki kısaltma oluyor 
# import matplotlib.pyplot as plt
# import numpy as np

# #x ve y eksenindeki noktaları belirledik
# xpoint=np.array([1,8])
# ypoint=np.array([3,10])

# #çizgi çizmek için plot() fonksiyonunu çağırıyoruz
# plt.plot(xpoint,ypoint)
# plt.show()


# #kısaltmaları yaptık as dan sonraki kısaltma oluyor 
# import matplotlib.pyplot as plt
# import numpy as np

# #x ve y eksenindeki noktaları belirledik
# xpoint=np.array([1,8])
# ypoint=np.array([3,10])

# #çizgi çizmek için plot() fonksiyonunu çağırıyoruz
# #çizgisiz grafik oluşturmak için ise 'o'
# plt.plot(xpoint,ypoint,'o')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# #x ve y eksenindeki noktaları belirledik xde 4 point varsa y de de 4 tane olmalıdır
# xpoint=np.array([1,3,5,8])
# ypoint=np.array([2,3,4,7])

# plt.plot(ypoint,xpoint)
# plt.show()
# #eğer noktalardan birini belirtmezsek xveya y yi belirli düzen halinde sayılar veririr,0.0,0.5,1.0 gibi gider

#Her noktayı belirli bir işaretçiyle vurgulamak için anahtar kelime bağımsız değişken "marker" kullanabilirsiniz:

# #Her noktayı bir daire ile işaretleyin:
# import matplotlib.pyplot as plt
# import numpy as np

# xpoint=np.array([1,3,5,8])
# ypoint=np.array([2,4,6,8])

# #marker ile her koordinataı işaretledik
# #"*" ile her koordinata * işareti kullanıldı
# #"o"ile ise içi dolu o harfi kullanıldı
# plt.plot(xpoint,ypoint,marker="D")
# plt.show()


"""
TÜM KULLANILABİLİR İŞARETLER
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline

"""



#satır referansları
"""
'-' Kesintisiz çizgi	
':' Noktalı çizgi	
'--' Kesikli çizgi	
'-'	Kesikli/noktalı çizgi
"""


import matplotlib.pyplot as plt
import numpy as np

xpoint=np.array([1,3,5,8])
ypoint=np.array([2,4,6,8])

#: ile grafik çizgisini kesikli hale getirdik ve yanına harf koyarak rengini belirleyebilriirz
plt.plot(xpoint,ypoint,"o:g")
plt.show()


"""
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
"""


import matplotlib.pyplot as plt
import numpy as np

xpoint=np.array([1,3,5,8])
ypoint=np.array([2,4,6,8])

#işaretçiyi 20 boyutuna çıkardık ms ile.mec ile ise işaretçinin dışının rengini belirledik r diyerek kırmızı yaptık
#mfc ile işaretçi rengini değiştirdik
#eğer işaretçi rek renk olsun istiyorsak hem mec hemde mfc yi aynı renk yapabilirisin
plt.plot(xpoint,ypoint,marker="o",ms=20,mec="r",mfc="m")
plt.show()


#color paletinden bulduğumuz renkleri de kullanabiliriz
#plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')

#renk yerine 140 tane destekelenen renkleri de yazabiliriz ing olacak
#plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')