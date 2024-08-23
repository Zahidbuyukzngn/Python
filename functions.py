# #bir fonksiyon tanımlama def ile yapılır
# def my_function():
#   print("Hello from a function")

# #yukardaki fonksiyonu kullanma
# my_function()

#fonksiyon içine değer atama
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function2(fname, lname):
  print(fname + " " + lname)

#eğer 2 değer varsa fonksiyonda mecbur 2 değer girmemiz gerek
my_function2("Emil", "Refsnes")


# * koyarak ağaıdaki isimlerden 2. indeksi seçerek çıktıyı verdirdik
#eğer * olasaydı hata verirdi 1koşula 3 değer veriyorsun diye
def my_function3(*kids):
  print("The youngest child is " + kids[2])

my_function3("Emil", "Tobias", "Linus")


#ayrıca bu şekilde de bir kullanım yapabililirz key=value syntx
def my_function4(child3, child2, child1):
  print("The youngest child is " + child2)

my_function4(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#atamanın ne kadar olduğunu bilmiyorsak öne 2 yıldız koyarız ve key ismiyle değere ulaşırız
def my_function5(**kid):
  print("His last name is " + kid["lname"])

my_function5(fname = "Tobias", lname = "Refsnes")


def my_function6(country = "Norway"):
  print("I am from " + country)

my_function6("Sweden")
my_function6("India")
#burada boş bıraktığımız için norway'i yazırdı,yukarda onu atadığımız için
my_function6()
my_function6("Brazil")


#list ile kullanımı
def my_function7(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function7(fruits)


def my_function8(x):
  return 5 * x

print(my_function8(3))
print(my_function8(5))
print(my_function8(9))


#fonksiyonlarda pass kullanımı
def myfunction10():
  pass


 # '/' işareti, x parametresinin yalnızca pozisyonel olarak kullanılmasını zorunlu kılar.def my_function9(x, /):
def my_function9(x, /):
  print(x)

my_function9(3)
#  my_function9(x=3) yazsaydım hata alırdım

#/ olmadan bu şekilde kullanım yapılabilir
def my_function(x):
  print(x)

my_function(x = 3)

#Bir işlevin yalnızca anahtar kelime bağımsız değişkenlerine sahip olabileceğini belirtmek için bağımsız değişkenlerin önüne * ekleyin:
#x e değer verdiğimiz yerde eğer direkt 3 yazarsak hata alırız
def my_function(*, x):
  print(x)

my_function(x = 3)

#/'den önceki herhangi bir argüman yalnızca konumsaldır ve
# *'dan sonraki herhangi bir argüman yalnızca anahtar kelimedir. = ile bildirmen gerekir
def my_function11(a, b, /,*, c, d):
  print(a + b + c + d)

my_function11(5, 6, c = 7, d = 8)


#Recursion Example
#k ya 6 verdik ve tri_recursion ile 1 azaltarak 1,3,6,10,15,21 aldık

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
