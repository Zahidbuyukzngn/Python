class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Bir nesne oluşturmak için Person sınıfını kullanın ve ardından printname yöntemini yürütün:


x = Person("Ahmet","Aydoğdu")
x.printname()

#person'dan student'e miras aldık
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

# class Student(Person):
#  def __init__(self, fname, lname):
#    #özellik vb eklenir buraya


#Not: Çocuğun __init__() işlevi, ebeveynin __init__() işlevinin mirasını geçersiz kılar.
#Ebeveynin __init__() işlevinin mirasını korumak için ebeveynin __init__() işlevine bir çağrı ekleyin:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

#Python ayrıca alt sınıfın tüm yöntemleri ve özellikleri üst sınıfından miras almasını sağlayacak bir super() işlevine de sahiptir:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    #person yerine super yazarak üstten otomatik aldırdık
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()
#super() işlevini kullandığınızda, ana öğenin adını kullanmanıza gerek kalmaz;
#yöntem ve özellikleri otomatik olarak üst öğesinden devralır.



class Person2:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student2(Person2):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student2("Mike", "Olsen")
print(x.graduationyear)


#inite e year eklenmiş hali
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)


#Öğrenci sınıfına hoş geldiniz adlı bir yöntem ekleme

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()


#inheritance çalış