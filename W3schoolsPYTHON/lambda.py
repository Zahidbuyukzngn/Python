#5 + 10 çıktı 15 
x = lambda a : a + 10
print(x(5))

#6 * 5=30 çıktı
x = lambda a, b : a * b
print(x(5, 6))

#3lü lambda 13 çıktı
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


#3*11 işlemi yaptık
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)

print(mydoubler(11))

 
#myfunc 2 yani n=2 ,alttakinde de 3 yani 3=n
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #2a 
mytripler = myfunc(3) #3a

#mydoublere(11) girdik ve 11*2 çıktı sonuç

print(mydoubler(11))  #11*2
print(mytripler(11))  #11*3
