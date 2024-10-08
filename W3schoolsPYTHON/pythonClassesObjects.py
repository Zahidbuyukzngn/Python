# #bir class tanımlama
# class MyClass:
#   x = 5

# p1 = MyClass()


#self: Bu, sınıfın örneğini temsil eden bir parametredir. self, her zaman metotların ilk parametresi olmalıdır.
#Sınıfın içindeki diğer özelliklere ve yöntemlere erişmek için kullanılır.
#__init__ () kullanımı

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


# #__str__() kullanımı 
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)

#Self parametresi sınıfın geçerli örneğine bir referanstır ve sınıfa ait değişkenlere erişmek için kullanılır.
#self özel bir parametre değildir,başka bir şey de tanımlayabililirz
#
class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)


p1 = Person2("John", 36)
p1.myfunc()

#Self parametresi sınıfın geçerli örneğine bir referanstır ve sınıfa ait değişkenlere erişmek için kullanılır. 
#Self olarak adlandırılmasına gerek yoktur,
#onu istediğiniz gibi adlandırabilirsiniz, ancak sınıftaki herhangi bir işlevin ilk parametresi olmalıdır:

p1.age = 40
p1.name="ahmet"
print(p1.age)
print(p1.name)

#silme
del p1.age

del p1

#pass ile hata almamasını sağladık
class Person:
  pass