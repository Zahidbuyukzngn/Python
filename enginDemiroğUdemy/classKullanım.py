# class Matematik():
#     def topla(self,a,b):
#         return a+b
#     def cıkar(self,a,b):
#         return a-b
#     def carp(self,a,b):
#         return a*b
#     def bol(self,a,b):
#         return a/b

# #her fonks başına self yazmam gerekiyor yoksa hata alırım
# matematik=Matematik()

# print(matematik.topla(5,10))
# print(matematik.carp(2,30))
# print(matematik.cıkar(10,0))
# print(matematik.bol(8,2))


#selfi bu şekilde de kullanabiliriz
class Matematik2():
    def __init__(self,a,b):
        #birinci ave b yi başka değrler verebilriirdik 
        self.a=a
        self.b=b

    def topla(self):
        #aynı klastaki farklı fonksiyonları self ile eçağırabiliriz
        self.bol()
        return self.a+self.b
    def cıkar(self):
        return self.a-self.b
    def carp(self):
        return self.a*self.b
    def bol(self):
        return self.a/self.b

#değeri burda belirttik
matematik2=Matematik2(10,20)

print (matematik2.topla())

class person():
    def __init__(self,name,lastName,age):
        self.name=name
        self.lastName=lastName
        self.age=age
    
person1=person("mustafa","emre",28)
print(person1.name)