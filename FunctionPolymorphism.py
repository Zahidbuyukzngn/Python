#len()

#x içindeki toplam karakter sayısını söyler 12
x = "Hello World!"

print(len(x))

#tuplslar için len(), demetteki öğelerin sayısını döndürür:
#çıktımız 3.3 eleman var çünkü
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))


#Sözlükler için len(), sözlükteki anahtar/değer çiftlerinin sayısını döndürür:
#3 tane key value eşleşmesi var
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))


#move()
#Aynı yöntemle farklı sınıflar:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #araba sınıfı oluştur
boat1 = Boat("Ibiza", "Touring 20") #bot sınıfı oluştur
plane1 = Plane("Boeing", "747")     #uçak sınıfı oluştur

for x in (car1, boat1, plane1):
  x.move()


#Araç adında bir sınıf oluşturun ve Araç'ın Araba, Tekne, Uçak alt sınıflarını yapın:

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()