
#jsonu pythona dönüştürme
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

#pythona dönüşüm
# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


#pythondan json a dönüştürme
import json

#bir sözlükten
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

#jsona dönüşüm dumps(x)ile
# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#jsona dönüştürülebilen formatlar
'''
dict
list
tuple
string
int
float
True
False
None'''



#jsona dönüşüm örnekleri
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#pythondan jsona dönüşüm karşılıkları
'''
Python	        JSON
dict	        Object
list	        Array
tuple	        Array
str     	    String
int	            Number
float	        Number
True	        true
False	        false
None	        null
'''


import json

#jsona dönüşüm
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

#indent ile aralarında 4 birim boşluk bırakıyoruz.
json.dumps(x, indent=4)
print(json.dumps(x))


#Varsayılan seperatorsu değiştirmek için ayırıcılar parametresini kullanın:
json.dumps(x, indent=4, separators=(". ", " = "))


#Sonucun sıralanıp sıralanmayacağını belirtmek için sort_keys parametresini kullanın:
print(json.dumps(x, indent=4, sort_keys=True))


import json
a= {
    "isim" :"zahid",
    "soyisim": "bzngn",
    "yas" : "18",
}

b=json.dumps(a,indent=10)

print(b)