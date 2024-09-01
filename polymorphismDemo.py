
#classlarda tanımladık
class Cat:
    def sound(self):
        return "Miyav"
    
class Dog:
    def sound(self):
        return "Havhav"
    
def animal_sound(animal):
    print(animal.sound())
#eşitleme sadece daha anlaşılır olması için
dog=Dog()
cat=Cat()
#yazdırma
animal_sound(dog)
animal_sound(cat)


#2.örneğim

class Bird:
    def fly(self):
        return("flying high!")
    
class Airplane:
    def fly(self):
        return("taking off!")
    
def perform_fly(obj):
    print(obj.fly())

bird=Bird()
airplane=Airplane()

perform_fly(bird)
perform_fly(airplane)