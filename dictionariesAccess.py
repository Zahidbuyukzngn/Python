# #keys()kullanınca sadece color ekleyebildik white ekleyemedik
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change


#yukardakinin items() hali bunda hem key hem value eklendi
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "white"

print(x) #after the change



#car dictindeki  year'ı 2020 yaptık
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

#values() ile dict içini aldık
x = car.values()

print(x) #değiştirmeden önceki aldığımız çıktı

car["year"] = 2020

print(x) #değiştirdikten sonra aldığımız çıktı


#bunla hem key value ekledik
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


#belirli key dict'in içinde var mı yok mu onu sorduk
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")