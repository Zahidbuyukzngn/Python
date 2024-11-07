class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
person1=person("mustafa",22)
print(person)

class customer(person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
        
class worker(person):
    def __init__(self, jobTitle):
        self.jobTitle = jobTitle
        
ahmet=person("ahmet",22)

print(ahmet.name)