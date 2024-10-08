# # eşittir: a == b
# # eşit değildir: a != b
# # küçüktür: a < b
# # küçük eşittir: a <= b
# # büyüktür: a > b
# # büyük eşittir : a >= b


# #b a dan büyük mü diye sorduk
# #if tanımlarken : ve aşağıya bir boşluk bırakmayı unutma
# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")

# #Elif anahtar sözcüğü Python'un "önceki koşullar doğru değilse bu koşulu deneyin" deme biçimidir.  
# #kullanımı bu şekildedir
# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")


# #else ise if ve elif de gerçekleşmeyen koşulların çıkış yeridir
# #if olmadan diğerleri olmaz ama elif olmadan da diğerleri olur
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# #bu şekilde de if kullanılabilir
# if a > b: print("a is greater than b")

#if else'nin bir satırda kullanımı
#eğer a büyüktür b ise çıktı a yazdırır.
a = 2
b = 330
print("A") if a > b else print("B")

#3 kondisyonu aynı satırda kullanma
a = 330
b = 330
print(a) if a > b else print("=") if a == b else print("==")

#AND

#2 kondisyonunda gerçekleşmesi gerek
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#OR
#en az birisi gerçekleşse bile print yazdırır
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


#NOT
#a b'den büyük olmadığı için koşul gerçekleşir
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


#iç içe koşullar olabilir
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#ife bir sonuç vermediğimiz için hata vercek kodu pass ile hata almamasını sağladık
a = 33
b = 200

if b > a:
  pass