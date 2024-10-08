# import numpy

# speed=(95,90,99,98,97,96,89,88,87,86,85,84)

# #numpy import ederek mean() fonks ile hızların ortalamalarını aldık
# medyanAl=numpy.mean(speed)

# print(medyanAl)



# import numpy

# speed=(80,81,82,83,84,85,86,87,88,89,90)

# #median() ile ortancayı yani medyanı bulduk
# medyanıBul=numpy.median(speed)

# print(medyanıBul)

#En çok görünen sayıyı bulmak için SciPy mode() yöntemini kullanın:

from scipy import stats

speed=[80,81,82,83,84,85,85,80,80]

enSıkGeçenSayı=stats.mode(speed)
print(f"en sık geçen sayı: {enSıkGeçenSayı}")