#Yüzdelik dilimleri bulmak için NumPy percentile() yöntemini kullanın:
import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print(x)
#Cevap 43, yani insanların %75'i 43 yaş ve altında.



#İnsanların %90'inin genç olduğu yaş kaçtır?
import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 90)
print(x)