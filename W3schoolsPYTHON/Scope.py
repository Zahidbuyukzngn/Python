
#fonksiyon dışındaki oluşturulan veriable fonksiyon içini ilgilendirmez
#çıktı ilk 200 yazar sonra 300
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#Yerel değişkene, işlev içindeki bir işlevden erişme
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#global ile dışardan da erişilebilir hale gelir
def myfunc():
  global xx
  xx = 300

myfunc()

print(x)

#değiştirme 300,200 ile changeledik
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

#bir iç fonksiyon, dış fonksiyonun yerel değişkenini değiştirmek istediğinde nonlocal kullanılır.

def myfunc1():
  x = "Jane"
  def myfunc2():
    #janeyi helloya dönüştürdük
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())