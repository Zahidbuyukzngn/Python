# List Comprehensions


# Yine o yeni bir şey öğrenmediğimiz ama yaptığımız şeyleri daha farklı ve kolay yapmayı öğrendiğimiz bir konudayız.


# Diyelim ki 1'den 10'a kadar olan sayıların karelerinden bir liste oluşturmak istiyorum. Bunu aşağıdaki gibi yapabilirim.


# squares = []

# for i in range(1,11):
#     squares.append(i*i)


# squares


# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Bunun aynısını list comprehension kullanarak da yapabiliriz.


# squares = [i * i for i in range(1,11)]


# squares


# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# # list comprehension ve fonksiyon mantığını birleştirme

# def cube(x):
#     return x * x * x # x ** 3


# cubes = [cube(x) for x in range(1,11)]


# cubes


# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


# List Comprehension'larda Conditional Yapıların Kullanılması


# squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# print(squares)


# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# odd_squares = []

# for e in squares:
    
#     if e % 2 == 1:
#         odd_squares.append(e)


# odd_squares


# [1, 9, 25, 49, 81]


# # squares listindeki tek elemanlardan yeni bir liste yaratmak

# odd_squares = [e for e in squares if e % 2 == 1]


# odd_squares


# [1, 9, 25, 49, 81]


# # bu test mantığını fonksiyonla da sağlayabilirdik

# def is_odd(x): 
    
#     if x % 2 == 0:
#         return False
    
#     if x % 2 == 1:
#         return True


# odd_squares = [e for e in squares if is_odd(e)]


# odd_squares


# [1, 9, 25, 49, 81]


# def empty(x): 
    
#     if x % 2 == 0:
#         return False
    
#     if x % 2 == 1:
#         return False


# empty_squares = [e for e in squares if empty(e)]


# empty_squares


# []


# def is_even(x):
    
#     if x % 2 == 0:
#         return True
    
#     if x % 2 == 1:
#         return False


# even_squares = [e for e in squares if is_even(e)]


# even_squares


# [4, 16, 36, 64, 100]


# squares


# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# weird_squares = [e if e % 2 == 0 else -1 for e in squares]


# weird_squares


# [-1, 4, -1, 16, -1, 36, -1, 64, -1, 100]


# ultra_weird_squares = [e if e % 2 == 0 else -1 for e in squares if is_even(e)]


# # Q. Soru: Bunun çıktısı ne olur ?
# ultra_weird_squares


# [4, 16, 36, 64, 100]


# Set Comprehension
# numbers = [1,2,3,4,5,6,7,1,2]


# set_numbers = {s for s in numbers if s in [1,2,3,4,5,6,1,2]}


# set_numbers


# {1, 2, 3, 4, 5, 6}

# Dictionary Comprehension


# square_dict = {e:e * e for e in range(1,11)}


# square_dict


# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


# square_dict[9]


# 81


# Nested List Comprehension


# m = [[j for j in range(7)] for i in range(5)]


# m = [[j for j in range(7)] for _ in range(5)]


# m


# [[0, 1, 2, 3, 4, 5, 6],
#  [0, 1, 2, 3, 4, 5, 6],
#  [0, 1, 2, 3, 4, 5, 6],
#  [0, 1, 2, 3, 4, 5, 6],
#  [0, 1, 2, 3, 4, 5, 6]]


# m = [[10, 11, 12], [13, 14], [15, 16, 17, 18]] 


# for l in m:
#     print(l)


# [10, 11, 12]
# [13, 14]
# [15, 16, 17, 18]


# new_m = []
# for l in m:
#     print(l)
#     for e in l:
#         new_m.append(e)
#         print(e)


# [10, 11, 12]
# 10
# 11
# 12
# [13, 14]
# 13
# 14
# [15, 16, 17, 18]
# 15
# 16
# 17
# 18


# new_m


# [10, 11, 12, 13, 14, 15, 16, 17, 18]


# m


# [[10, 11, 12], [13, 14], [15, 16, 17, 18]]


# # matrixi list comprehension ile flat etmek

# flatten_m = [e for l in m for e in l]


# flatten_m


# [10, 11, 12, 13, 14, 15, 16, 17, 18]


# # Sadece çift değerleri kabul edecek

# flatten_m = [e for l in m for e in l if e % 2 == 0]


# flatten_m


# [10, 12, 14, 16, 18]