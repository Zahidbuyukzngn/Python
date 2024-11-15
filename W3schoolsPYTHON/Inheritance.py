# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Bir nesne oluşturmak için Person sınıfını kullanın ve ardından printname yöntemini yürütün:


# x = Person("Ahmet","Aydoğdu")
# x.printname()

# #person'dan student'e miras aldık
# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()

# # class Student(Person):
# #  def __init__(self, fname, lname):
# #    #özellik vb eklenir buraya


# #Not: Çocuğun __init__() işlevi, ebeveynin __init__() işlevinin mirasını geçersiz kılar.
# #Ebeveynin __init__() işlevinin mirasını korumak için ebeveynin __init__() işlevine bir çağrı ekleyin:
# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# #Python ayrıca alt sınıfın tüm yöntemleri ve özellikleri üst sınıfından miras almasını sağlayacak bir super() işlevine de sahiptir:
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     #person yerine super yazarak üstten otomatik aldırdık
#     super().__init__(fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()
# #super() işlevini kullandığınızda, ana öğenin adını kullanmanıza gerek kalmaz;
# #yöntem ve özellikleri otomatik olarak üst öğesinden devralır.



# class Person2:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student2(Person2):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear = 2019

# x = Student2("Mike", "Olsen")
# print(x.graduationyear)


# #inite e year eklenmiş hali
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

# x = Student("Mike", "Olsen", 2019)
# print(x.graduationyear)


# #Öğrenci sınıfına hoş geldiniz adlı bir yöntem ekleme

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2024)
# x.welcome()


#inheritance çalış



"INHERİTANCE UDEMY MEHMET TEK ÇALIŞMASI"
class okul():
  def __init__(self,ad,soyad,yaş):
    self.ad=ad
    self.soyad=soyad
    self.yaş=yaş
  def info(self):
    print(f"Adı: {self.ad}, Soyadı: {self.soyad}, Yaşı: {self.yaş}")

ahmet=okul("Ahmet","Kılınç",22)

ahmet.info()


#super() ile okuldan kalıtım aldık
class öğrenci(okul):
  def __init__(self, ad, soyad, yaş,sınıf,notortalama):
    super().__init__(ad, soyad, yaş)
    self.sınıf=sınıf
    self.notortalama=notortalama
  def info(self):
    print(f"öğrenci {self.ad} {self.soyad}\'ın yaşı {self.yaş}, sınıfı {self.sınıf} ve not ortalaması ise {self.notortalama}")

#bir değişkene atayıp bilgileri burda veriyoruz
muaz=öğrenci("Muaz","Akdağ",20,12,90)
muaz.info()



class öğretmen(okul):
  def __init__(self, ad, soyad, yaş,alan,maaş):
    #okuldan aldıklarımızı super() ile inherit ettik
    super().__init__(ad, soyad, yaş)
    #eğer ekstra bilgiler ekleyeceksek superin altına bu şekilde ekleyebilirim
    self.alan=alan
    self.maaş=maaş

  #self yazmayı unutma
  def info(self):
    print(f"öğretmen {self.ad} {self.soyad}\'nın yaşı {self.yaş},alanı {self.alan} ve maaşı ise {self.maaş}")
  #maaşına %50 zam yaptık return ile döndürdük
  def zam(self):
   return self.maaş * 1.5 
  

mehmet=öğretmen("Mehmet","Kaya",35,"Coğrafya",42000)

mehmet.info()
print(mehmet.zam())