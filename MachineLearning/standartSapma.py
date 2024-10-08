#Standart sapmayı bulmak için NumPy std() yöntemini kullanın:

import numpy

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)

print(x)


#bunda da 37... çıktı
import numpy
speed = [32,111,138,28,59,77,97]

x = numpy.std(speed)

print(x)


#Varyansı bulmak için NumPy var() yöntemini kullanın:
import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)
print(x)

#Standart Sapma genellikle Sigma sembolü ile temsil edilir: σ
#Varyans genellikle Sigma Kare sembolü ile temsil edilir: σ2(2 karesi olacak yanında değil üstte)